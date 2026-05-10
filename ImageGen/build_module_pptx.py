#!/usr/bin/env python3
"""
build_module_pptx.py
────────────────────
Parses a module markdown file, generates slide images via OpenAI gpt-image-2
(up to 10 in parallel), then assembles a polished .pptx deck with speaker notes.

Design rules:
  • Image slides — full-bleed art, NO text overlaid, NO black bar.
  • Table slides — clean table only, NO title on the slide.
  • ALL text (including slide title) lives in the speaker notes.
  • Notes are formatted: bold where markdown has **, bullets for '- ' lines.

Usage:
    python build_module_pptx.py <module.md> [--slides N] [--no-images]

Environment:
    OPENAI_API_KEY  — loaded from .env in this script's directory, or set externally

Output:
    <module-dir>/images/slide_NN.png   (cached; skipped on re-runs)
    <module-dir>/<module-stem>.pptx
"""

import argparse
import base64
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Load .env from the script's own directory
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")

from openai import OpenAI
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn

# ── Constants ────────────────────────────────────────────────────────────────

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# Black & white palette
C_BLACK   = RGBColor(0x00, 0x00, 0x00)
C_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
C_GRAY_LT = RGBColor(0xEB, 0xEB, 0xEB)
C_GRAY_MD = RGBColor(0x55, 0x55, 0x55)

IMAGE_SIZE  = "1536x1024"
IMAGE_MODEL = "gpt-image-2"
BATCH_SIZE  = 10


# ── Data structures ──────────────────────────────────────────────────────────

@dataclass
class SlideData:
    index: int
    title: str
    image_prompt: Optional[str] = None
    body_lines: list = field(default_factory=list)
    table_rows: list = field(default_factory=list)
    talking_points: list = field(default_factory=list)
    image_path: Optional[Path] = None


# ── Markdown parsing ─────────────────────────────────────────────────────────

def _strip_md_bold(text: str) -> str:
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    return text


def _clean_title(raw: str) -> str:
    """Strip italic parentheticals like *(instructor demo narrative)* from slide titles."""
    cleaned = re.sub(r'\s*\*\([^)]+\)\*', '', raw)
    return cleaned.strip()


def _parse_table(section_text: str) -> list:
    rows = []
    for line in section_text.splitlines():
        if not re.match(r'^\s*\|', line):
            continue
        if re.match(r'^\s*\|[\-: |]+\|\s*$', line):
            continue
        cells = [_strip_md_bold(c.strip()) for c in line.split('|') if c.strip()]
        if cells:
            rows.append(cells)
    return rows


def _parse_body_lines(text: str) -> list:
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#') or line == '---':
            continue
        if re.match(r'^\|', line):
            continue
        cleaned = _strip_md_bold(line)
        if cleaned.startswith('- '):
            lines.append(('bullet', cleaned[2:]))
        elif cleaned:
            lines.append(('text', cleaned))
    return lines


def parse_markdown(md_path: Path, max_slides: Optional[int] = None) -> list:
    text = md_path.read_text(encoding='utf-8')
    slide_re = re.compile(r'^### SLIDE:\s*(.+)$', re.MULTILINE)
    matches = list(slide_re.finditer(text))

    slides = []
    for i, m in enumerate(matches):
        if max_slides and i >= max_slides:
            break

        title  = m.group(1).strip()
        start  = m.end()
        end    = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end]

        slide = SlideData(index=i + 1, title=title)

        img_m = re.search(r'\*\*\[Image prompt:\s*(.*?)\]\*\*', section, re.DOTALL)
        if img_m:
            slide.image_prompt = img_m.group(1).strip()

        tp_m = re.search(
            r'####\s+🗣\s+Talking points.*?\n(.*?)(?=\n---|\Z)',
            section, re.DOTALL
        )
        tp_start = tp_m.start() if tp_m else len(section)
        if tp_m:
            slide.talking_points = [
                l.strip() for l in tp_m.group(1).splitlines() if l.strip()
            ]

        body_section = section[:tp_start]
        if img_m:
            body_section = section[img_m.end():tp_start]
        body_section = re.sub(r'\*\*\[Image prompt:.*?\]\*\*', '', body_section, flags=re.DOTALL)

        slide.table_rows = _parse_table(body_section)
        slide.body_lines = _parse_body_lines(body_section)

        slides.append(slide)

    return slides


# ── Image generation ─────────────────────────────────────────────────────────

def _gen_one(client: OpenAI, slide: SlideData, images_dir: Path) -> None:
    out = images_dir / f"slide_{slide.index:02d}.png"
    if out.exists():
        print(f"  [cached] slide {slide.index:02d} → {out.name}")
        slide.image_path = out
        return

    print(f"  [gen]    slide {slide.index:02d} — requesting…")
    try:
        result = client.images.generate(
            model=IMAGE_MODEL,
            prompt=slide.image_prompt,
            size=IMAGE_SIZE,
        )
        image_bytes = base64.b64decode(result.data[0].b64_json)
        out.write_bytes(image_bytes)
        slide.image_path = out
        print(f"  [done]   slide {slide.index:02d} → {out.name}")
    except Exception as exc:
        print(f"  [error]  slide {slide.index:02d}: {exc}", file=sys.stderr)


def generate_all_images(slides: list, images_dir: Path) -> None:
    images_dir.mkdir(exist_ok=True)
    client = OpenAI()
    prompted = [s for s in slides if s.image_prompt]
    for i in range(0, len(prompted), BATCH_SIZE):
        batch = prompted[i : i + BATCH_SIZE]
        with ThreadPoolExecutor(max_workers=len(batch)) as pool:
            futures = {pool.submit(_gen_one, client, s, images_dir): s for s in batch}
            for f in as_completed(futures):
                f.result()


# ── PPTX helpers ─────────────────────────────────────────────────────────────

def _solid_rect(slide, left, top, width, height, color: RGBColor):
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def _textbox(slide, left, top, width, height,
             text, font_size, color: RGBColor,
             bold=False, italic=False, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf  = box.text_frame
    tf.word_wrap = True
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size      = Pt(font_size)
    run.font.color.rgb = color
    run.font.bold      = bold
    run.font.italic    = italic
    return box


def _set_bg(slide_obj, color: RGBColor):
    fill = slide_obj.background.fill
    fill.solid()
    fill.fore_color.rgb = color


# ── Notes formatting ──────────────────────────────────────────────────────────

def _parse_md_inline(text: str) -> list:
    """Parse **bold** inline markdown. Returns list of (segment_text, is_bold) tuples."""
    result = []
    pos = 0
    for m in re.finditer(r'\*\*(.+?)\*\*', text):
        if m.start() > pos:
            result.append((text[pos:m.start()], False))
        result.append((m.group(1), True))
        pos = m.end()
    if pos < len(text):
        result.append((text[pos:], False))
    return result if result else [(text, False)]


def _notes_para(txBody, segments, is_bullet=False):
    """Append one formatted paragraph to a notes txBody element."""
    p = etree.SubElement(txBody, qn('a:p'))
    if is_bullet:
        pPr = etree.SubElement(p, qn('a:pPr'))
        buChar = etree.SubElement(pPr, qn('a:buChar'))
        buChar.set('char', '•')
    for seg_text, bold in segments:
        if not seg_text:
            continue
        r = etree.SubElement(p, qn('a:r'))
        rPr = etree.SubElement(r, qn('a:rPr'))
        rPr.set('lang', 'en-US')
        if bold:
            rPr.set('b', '1')
        t = etree.SubElement(r, qn('a:t'))
        t.text = seg_text


def _set_notes(slide_obj, title: str, lines: list):
    """Set speaker notes with proper formatting.

    title  — slide title, rendered as a bold header at the top.
    lines  — talking points; may contain **bold** markdown and '- ' bullets.
    """
    ntf    = slide_obj.notes_slide.notes_text_frame
    txBody = ntf._txBody

    # Clear all existing paragraphs
    for p in list(txBody.findall(qn('a:p'))):
        txBody.remove(p)

    # Title — bold header
    if title:
        _notes_para(txBody, [(title, True)])
        etree.SubElement(txBody, qn('a:p'))   # blank line after title

    # Body lines — blank paragraph after every non-empty line for readability
    for raw in lines:
        raw = raw.strip()
        if not raw:
            etree.SubElement(txBody, qn('a:p'))
            continue
        is_bullet = raw.startswith('- ')
        text = raw[2:] if is_bullet else raw
        _notes_para(txBody, _parse_md_inline(text), is_bullet=is_bullet)
        etree.SubElement(txBody, qn('a:p'))   # blank line after each point


# ── Slide builders ────────────────────────────────────────────────────────────

def build_title_slide(prs: Presentation, slide: SlideData):
    """Full-bleed image — no overlay, no bar.
    Placeholder (no image): clean white background, no text.
    Title + notes go entirely into speaker notes."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])

    raw = _clean_title(slide.title)
    em_match = re.search(r'[—–]\s*(.+)$', raw)
    display_title = em_match.group(1).strip() if em_match else raw

    if slide.image_path:
        _set_bg(sl, C_BLACK)
        sl.shapes.add_picture(str(slide.image_path), 0, 0, SLIDE_W, SLIDE_H)
    else:
        _set_bg(sl, C_WHITE)

    _set_notes(sl, display_title + '  ·  MODULE 2  ·  ISYS 398U', slide.talking_points)
    return sl


def build_image_slide(prs: Presentation, slide: SlideData):
    """Full-bleed image — no overlay, no bar.
    Placeholder (no image): clean white background, no text.
    Title goes entirely into speaker notes."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])

    display_title = _clean_title(slide.title)

    if slide.image_path:
        _set_bg(sl, C_BLACK)
        sl.shapes.add_picture(str(slide.image_path), 0, 0, SLIDE_W, SLIDE_H)
    else:
        _set_bg(sl, C_WHITE)

    _set_notes(sl, display_title, slide.talking_points)
    return sl


def build_table_slide(prs: Presentation, slide: SlideData):
    """
    Apple / Jony Ive-inspired table — no slide title.
    Title goes into speaker notes. Table starts near the top of the slide.
    """
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    _set_bg(sl, C_WHITE)

    rows = slide.table_rows
    if not rows:
        _set_notes(sl, _clean_title(slide.title), slide.talking_points)
        return sl

    header_row = rows[0]
    data_rows  = rows[1:]
    n_cols     = max(len(r) for r in rows)

    # ── Layout ──────────────────────────────────────────────────────────────
    ML       = Inches(0.55)
    TBL_W    = Inches(12.2)
    COL0_W   = Inches(1.6)
    REST_W   = (TBL_W - COL0_W) / max(n_cols - 1, 1)

    col_x = [ML + (COL0_W + REST_W * (ci - 1) if ci > 0 else 0)
             for ci in range(n_cols)]
    col_w = [COL0_W] + [REST_W] * (n_cols - 1)

    # Table starts near the top now that the title is in notes
    HDR_Y   = Inches(0.50)   # column header labels
    HDR_H   = Inches(0.38)
    RULE1_Y = Inches(0.90)   # thick black rule
    RULE1_H = Inches(0.014)
    ROW_Y0  = Inches(0.96)   # first data row
    ROW_H   = Inches(1.08)   # generous row height (more vertical space available)

    # ── Column headers (skip empty col 0) ────────────────────────────────────
    for ci in range(1, n_cols):
        label = header_row[ci] if ci < len(header_row) else ""
        _textbox(sl, col_x[ci], HDR_Y, col_w[ci], HDR_H,
                 label.upper(), 11, C_GRAY_MD, bold=True)

    # ── Thick rule under column headers ──────────────────────────────────────
    _solid_rect(sl, ML, RULE1_Y, TBL_W, RULE1_H, C_BLACK)

    # ── Data rows ────────────────────────────────────────────────────────────
    INNER_PAD_T = Inches(0.18)
    INNER_PAD_B = Inches(0.10)

    for ri, row_data in enumerate(data_rows):
        y = ROW_Y0 + ROW_H * ri
        if ri > 0:
            _solid_rect(sl, ML, y, TBL_W, Inches(0.007), RGBColor(0xCC, 0xCC, 0xCC))
        for ci in range(n_cols):
            cell_text = row_data[ci] if ci < len(row_data) else ""
            is_label  = (ci == 0)
            _textbox(sl,
                     col_x[ci],
                     y + INNER_PAD_T,
                     col_w[ci],
                     ROW_H - INNER_PAD_T - INNER_PAD_B,
                     cell_text,
                     15 if is_label else 14,
                     C_BLACK,
                     bold=is_label)

    # ── Bottom hairline ───────────────────────────────────────────────────────
    bottom_y = ROW_Y0 + ROW_H * len(data_rows)
    _solid_rect(sl, ML, bottom_y, TBL_W, Inches(0.007), RGBColor(0xCC, 0xCC, 0xCC))

    _set_notes(sl, _clean_title(slide.title), slide.talking_points)
    return sl


# ── Deck assembly ─────────────────────────────────────────────────────────────

def build_pptx(slides: list, out_path: Path) -> None:
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H

    for slide in slides:
        if slide.index == 1:
            build_title_slide(prs, slide)
        elif slide.table_rows:
            build_table_slide(prs, slide)
        else:
            build_image_slide(prs, slide)

    prs.save(str(out_path))
    print(f"\n✓  Saved → {out_path}")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate slide images and build a .pptx from a module markdown file."
    )
    parser.add_argument("markdown",       help="Path to the module .md file")
    parser.add_argument("--slides", "-n", type=int, default=None,
                        help="Max number of slides to process (omit for all)")
    parser.add_argument("--no-images",    action="store_true",
                        help="Skip image generation; render all slides as white placeholders")
    args = parser.parse_args()

    md_path = Path(args.markdown).expanduser().resolve()
    if not md_path.exists():
        sys.exit(f"❌  File not found: {md_path}")
    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("❌  OPENAI_API_KEY not set — add it to Application/ImageGen/.env")

    print(f"Parsing   {md_path.name} …")
    slides = parse_markdown(md_path, max_slides=args.slides)
    print(f"Found {len(slides)} slides  "
          f"({sum(1 for s in slides if s.image_prompt)} with image prompts, "
          f"{sum(1 for s in slides if s.table_rows)} with tables)\n")

    images_dir = md_path.parent / "images"
    if args.no_images:
        print("Images    → skipped (--no-images)")
    else:
        print(f"Images    → {images_dir}")
        generate_all_images(slides, images_dir)

    out_path = md_path.parent / (md_path.stem + ".pptx")
    print(f"\nBuilding  → {out_path}")
    build_pptx(slides, out_path)


if __name__ == "__main__":
    main()
