#!/usr/bin/env python3
"""
build_module_pptx.py
────────────────────
Build a module's PowerPoint deck from two inputs:

  1. lesson .md            slide content, talking points, tables
  2. <lesson>_image_prompts.md   sidecar file with per-slide image prompts
                                 (auto-detected next to the lesson; optional)

Streaming dispatch
──────────────────
Slides are parsed AND their image generation is dispatched in one walk through
the lesson markdown. Each slide's generation starts immediately on a thread;
the parser keeps moving. After parsing is done, the script awaits every
in-flight generation, then assembles the .pptx.

Slide treatment is determined per slide:

  · prose prompt in sidecar         → OpenAI image generation
  · [existing: <path>] in sidecar   → use that image as-is, no generation
  · [text-only] in sidecar          → render slide.body_lines as native PPT text
  · lesson has a markdown table     → run table render-then-stylize pipeline
  · (no spec, no table)             → ERROR (warn + white placeholder slide)

Legacy support: if the sidecar file doesn't exist, falls back to the old
**[Image prompt: ...]** inline blocks in the lesson markdown (M2/M3 style).

Output
──────
  <module-dir>/images/<slug>.png    slug derived from slide title
  <module-dir>/<lesson-stem>.pptx

Image filenames are slug-based (e.g., "customer-story-asana.png"), not
indexed — so reordering slides does NOT rename images. Title collisions
within a module get -2, -3 suffixes automatically.

Usage
─────
  python3 build_module_pptx.py <lesson.md> [--slides N] [--no-images]
"""

import argparse
import base64
import os
import re
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")

from openai import OpenAI
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn

from test_table_render import render_table_markdown_to_png
from test_table_stylize import stylize_table


# ── Constants ────────────────────────────────────────────────────────────────

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

C_BLACK   = RGBColor(0x00, 0x00, 0x00)
C_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
C_GRAY_LT = RGBColor(0xEB, 0xEB, 0xEB)
C_GRAY_MD = RGBColor(0x55, 0x55, 0x55)

IMAGE_SIZE          = "1536x1024"
IMAGE_MODEL         = "gpt-image-2"
TABLE_STYLIZE_SIZE  = "1536x1024"
MAX_WORKERS         = 50          # high enough that nothing blocks in practice


# ── Data structures ──────────────────────────────────────────────────────────

@dataclass
class SlideSpec:
    """A slide's image-generation specification from the prompts sidecar."""
    kind: str                         # 'image' | 'existing' | 'text-only'
    prompt: Optional[str] = None
    existing_path: Optional[Path] = None


@dataclass
class SlideData:
    index: int
    title: str
    slug: str
    body_lines: list = field(default_factory=list)
    table_rows: list = field(default_factory=list)
    table_md: Optional[str] = None
    talking_points: list = field(default_factory=list)
    image_path: Optional[Path] = None
    inline_image_prompt: Optional[str] = None  # legacy: prompt inline in lesson
    spec: Optional[SlideSpec] = None
    treatment: str = "unspecified"             # set during dispatch


# ── Slug derivation ──────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert a slide title to a filesystem-safe kebab-case slug."""
    # Strip italic parentheticals and bold markdown
    text = re.sub(r'\s*\*\([^)]+\)\*', '', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    # ASCII-fold, lowercase, replace non-alphanumeric with '-'
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    text = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return text or "slide"


# ── Markdown parsing — shared helpers ─────────────────────────────────────────

def _strip_md_bold(text: str) -> str:
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    return text


def _clean_title(raw: str) -> str:
    """Strip italic parentheticals like *(instructor demo narrative)* from slide titles."""
    return re.sub(r'\s*\*\([^)]+\)\*', '', raw).strip()


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


def _extract_table_md(section_text: str) -> Optional[str]:
    """Return the raw markdown table block (preserves **bold**) or None."""
    lines = []
    in_table = False
    for line in section_text.splitlines():
        if re.match(r'^\s*\|', line):
            lines.append(line)
            in_table = True
        elif in_table and not line.strip():
            break
        elif in_table:
            break
    return "\n".join(lines) if lines else None


def _parse_body_lines(text: str) -> list:
    """Returns list of (kind, text) tuples — kind is 'bullet' or 'text'."""
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


def parse_lesson(md_path: Path, max_slides: Optional[int] = None) -> list:
    """Parse a lesson .md into SlideData list. Resolves slug collisions."""
    text = md_path.read_text(encoding='utf-8')
    slide_re = re.compile(r'^### SLIDE:\s*(.+)$', re.MULTILINE)
    matches = list(slide_re.finditer(text))

    slides = []
    seen_counts = {}
    for i, m in enumerate(matches):
        if max_slides and i >= max_slides:
            break

        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end]

        base = slugify(title)
        seen_counts[base] = seen_counts.get(base, 0) + 1
        slug = base if seen_counts[base] == 1 else f"{base}-{seen_counts[base]}"

        slide = SlideData(index=i + 1, title=title, slug=slug)

        img_m = re.search(r'\*\*\[Image prompt:\s*(.*?)\]\*\*', section, re.DOTALL)
        if img_m:
            slide.inline_image_prompt = img_m.group(1).strip()

        # Match any 🗣 sub-section: "Talking points", "Closing notes",
        # "Facilitation", "Instructor notes", etc.
        tp_m = re.search(
            r'####\s+🗣[^\n]*\n(.*?)(?=\n---|\Z)',
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
        slide.table_md   = _extract_table_md(body_section)
        slide.body_lines = _parse_body_lines(body_section)

        slides.append(slide)

    return slides


# ── Sidecar prompts file parsing ──────────────────────────────────────────────

def parse_prompts_file(path: Path) -> dict:
    """Parse a sidecar prompts .md into {slide_title: SlideSpec}.

    Sidecar format:

        # Module N — Image Prompts

        ## SLIDE: <exact slide title from lesson>

        <prose prompt>      OR      [text-only]      OR      [existing: path/to.png]

        ## SLIDE: <next slide title>

        ...

    A slide with no entry in the sidecar falls back to either its inline
    [Image prompt: ...] block (legacy) or, if it has a markdown table, the
    table pipeline.
    """
    if not path.exists():
        return {}

    text = path.read_text(encoding='utf-8')
    slide_re = re.compile(r'^##\s+SLIDE:\s*(.+)$', re.MULTILINE)
    matches = list(slide_re.finditer(text))

    specs = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()

        # Strip trailing '---' section separators so marker regexes match cleanly
        body = re.sub(r'\n\s*---\s*$', '', body).strip()

        if not body:
            continue

        if re.match(r'^\[text-only\]\s*$', body, re.IGNORECASE):
            specs[title] = SlideSpec(kind='text-only')
            continue

        ex_m = re.match(r'^\[existing:\s*([^\]]+)\]\s*$', body, re.IGNORECASE)
        if ex_m:
            specs[title] = SlideSpec(kind='existing', existing_path=Path(ex_m.group(1).strip()))
            continue

        # Otherwise: prose prompt
        specs[title] = SlideSpec(kind='image', prompt=body)

    return specs


def attach_specs(slides: list, prompts: dict) -> None:
    """Decide each slide's treatment and attach its spec."""
    for slide in slides:
        spec = prompts.get(slide.title)
        if spec:
            slide.spec = spec
            slide.treatment = spec.kind          # 'image' | 'existing' | 'text-only'
        elif slide.inline_image_prompt:
            slide.spec = SlideSpec(kind='image', prompt=slide.inline_image_prompt)
            slide.treatment = 'image'
        elif slide.table_rows:
            slide.treatment = 'table'
        else:
            slide.treatment = 'unspecified'


# ── Image generation — streaming dispatch ─────────────────────────────────────

def _gen_image(client: OpenAI, slide: SlideData, images_dir: Path) -> None:
    out = images_dir / f"{slide.slug}.png"
    if out.exists():
        print(f"  [cached] {slide.slug} → {out.name}")
        slide.image_path = out
        return
    print(f"  [gen]    {slide.slug} — requesting…")
    try:
        result = client.images.generate(
            model=IMAGE_MODEL,
            prompt=slide.spec.prompt,
            size=IMAGE_SIZE,
        )
        image_bytes = base64.b64decode(result.data[0].b64_json)
        out.write_bytes(image_bytes)
        slide.image_path = out
        print(f"  [done]   {slide.slug}")
    except Exception as exc:
        print(f"  [error]  {slide.slug}: {exc}", file=sys.stderr)


def _gen_table(client: OpenAI, slide: SlideData, images_dir: Path) -> None:
    out = images_dir / f"{slide.slug}.png"
    if out.exists():
        print(f"  [cached] {slide.slug} (table) → {out.name}")
        slide.image_path = out
        return

    title = _clean_title(slide.title)
    md_content = f"## {title}\n\n{slide.table_md}\n"
    structural = images_dir / f"{slide.slug}-structural.png"

    print(f"  [render] {slide.slug} (table) — pandoc→pdf→png…")
    try:
        render_table_markdown_to_png(md_content, structural)
    except Exception as exc:
        print(f"  [error]  {slide.slug} render: {exc}", file=sys.stderr)
        return

    print(f"  [gen]    {slide.slug} (table) — stylizing…")
    try:
        stylize_table(structural, out,
                      model=IMAGE_MODEL,
                      size=TABLE_STYLIZE_SIZE,
                      client=client)
        slide.image_path = out
        print(f"  [done]   {slide.slug} (table)")
    except Exception as exc:
        print(f"  [error]  {slide.slug} stylize: {exc}", file=sys.stderr)


def _resolve_existing(slide: SlideData, module_dir: Path) -> None:
    p = slide.spec.existing_path
    if not p.is_absolute():
        p = module_dir / p
    if p.exists():
        slide.image_path = p
        print(f"  [exist]  {slide.slug} → {p.name}")
    else:
        print(f"  [warn]   {slide.slug} existing path missing: {p}", file=sys.stderr)


def dispatch_all(slides: list, images_dir: Path, module_dir: Path,
                 skip_generation: bool = False) -> None:
    """Stream through slides, fire generations concurrently up to MAX_WORKERS."""
    images_dir.mkdir(exist_ok=True)
    client = None
    if not skip_generation:
        if not os.environ.get("OPENAI_API_KEY"):
            sys.exit("❌  OPENAI_API_KEY not set — add to Application/ImageGen/.env")
        client = OpenAI()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = []
        for slide in slides:
            if slide.treatment == 'existing':
                _resolve_existing(slide, module_dir)
            elif slide.treatment == 'text-only':
                pass        # nothing to dispatch; build_text_slide renders at assembly
            elif slide.treatment == 'image' and not skip_generation:
                futures.append(pool.submit(_gen_image, client, slide, images_dir))
            elif slide.treatment == 'table' and not skip_generation:
                futures.append(pool.submit(_gen_table, client, slide, images_dir))
            elif slide.treatment == 'unspecified':
                print(f"  [warn]   {slide.slug} — no spec, no table; will render as white placeholder",
                      file=sys.stderr)

        # Await everything in flight
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
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    return box


def _set_bg(slide_obj, color: RGBColor):
    fill = slide_obj.background.fill
    fill.solid()
    fill.fore_color.rgb = color


# ── Notes formatting ─────────────────────────────────────────────────────────

def _parse_md_inline(text: str) -> list:
    """Parse **bold** inline markdown. Returns list of (segment, is_bold) tuples."""
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
    ntf = slide_obj.notes_slide.notes_text_frame
    txBody = ntf._txBody
    for p in list(txBody.findall(qn('a:p'))):
        txBody.remove(p)
    if title:
        _notes_para(txBody, [(title, True)])
        etree.SubElement(txBody, qn('a:p'))
    for raw in lines:
        raw = raw.strip()
        if not raw:
            etree.SubElement(txBody, qn('a:p'))
            continue
        is_bullet = raw.startswith('- ')
        text = raw[2:] if is_bullet else raw
        _notes_para(txBody, _parse_md_inline(text), is_bullet=is_bullet)
        etree.SubElement(txBody, qn('a:p'))


# ── Slide builders ───────────────────────────────────────────────────────────

def build_image_slide(prs: Presentation, slide: SlideData):
    """Full-bleed image. Title + content in speaker notes."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    display_title = _clean_title(slide.title)
    if slide.image_path:
        _set_bg(sl, C_BLACK)
        sl.shapes.add_picture(str(slide.image_path), 0, 0, SLIDE_W, SLIDE_H)
    else:
        _set_bg(sl, C_WHITE)
    _set_notes(sl, display_title, slide.talking_points)
    return sl


def build_text_slide(prs: Presentation, slide: SlideData):
    """Native PPT text slide for text-only treatment (Key Takeaways, etc).

    Visual identity: clean white background, thin black rule top and bottom,
    slide title in upper-left, body lines as a numbered list.
    """
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    _set_bg(sl, C_WHITE)

    display_title = _clean_title(slide.title)
    ML = Inches(0.7)
    W = Inches(11.93)

    # Top rule
    _solid_rect(sl, ML, Inches(0.55), W, Inches(0.014), C_BLACK)

    # Title
    _textbox(sl, ML, Inches(0.75), W, Inches(0.7),
             display_title, 28, C_BLACK, bold=True)

    # Body lines
    y = Inches(1.85)
    for kind, txt in slide.body_lines:
        _textbox(sl, ML, y, W, Inches(0.7),
                 txt, 20, C_BLACK,
                 bold=False)
        y += Inches(0.75)

    # Bottom rule
    _solid_rect(sl, ML, Inches(6.93), W, Inches(0.014), C_BLACK)

    _set_notes(sl, display_title, slide.talking_points)
    return sl


def build_table_slide_native(prs: Presentation, slide: SlideData):
    """Fallback: native PPT table when image generation is skipped."""
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    _set_bg(sl, C_WHITE)

    rows = slide.table_rows
    if not rows:
        _set_notes(sl, _clean_title(slide.title), slide.talking_points)
        return sl

    header_row = rows[0]
    data_rows  = rows[1:]
    n_cols     = max(len(r) for r in rows)

    ML       = Inches(0.55)
    TBL_W    = Inches(12.2)
    COL0_W   = Inches(1.6)
    REST_W   = (TBL_W - COL0_W) / max(n_cols - 1, 1)

    col_x = [ML + (COL0_W + REST_W * (ci - 1) if ci > 0 else 0)
             for ci in range(n_cols)]
    col_w = [COL0_W] + [REST_W] * (n_cols - 1)

    HDR_Y   = Inches(0.50)
    HDR_H   = Inches(0.38)
    RULE1_Y = Inches(0.90)
    RULE1_H = Inches(0.014)
    ROW_Y0  = Inches(0.96)
    ROW_H   = Inches(1.08)

    for ci in range(1, n_cols):
        label = header_row[ci] if ci < len(header_row) else ""
        _textbox(sl, col_x[ci], HDR_Y, col_w[ci], HDR_H,
                 label.upper(), 11, C_GRAY_MD, bold=True)

    _solid_rect(sl, ML, RULE1_Y, TBL_W, RULE1_H, C_BLACK)

    INNER_PAD_T = Inches(0.18)
    INNER_PAD_B = Inches(0.10)

    for ri, row_data in enumerate(data_rows):
        y = ROW_Y0 + ROW_H * ri
        if ri > 0:
            _solid_rect(sl, ML, y, TBL_W, Inches(0.007), RGBColor(0xCC, 0xCC, 0xCC))
        for ci in range(n_cols):
            cell_text = row_data[ci] if ci < len(row_data) else ""
            is_label = (ci == 0)
            _textbox(sl,
                     col_x[ci],
                     y + INNER_PAD_T,
                     col_w[ci],
                     ROW_H - INNER_PAD_T - INNER_PAD_B,
                     cell_text,
                     15 if is_label else 14,
                     C_BLACK,
                     bold=is_label)

    bottom_y = ROW_Y0 + ROW_H * len(data_rows)
    _solid_rect(sl, ML, bottom_y, TBL_W, Inches(0.007), RGBColor(0xCC, 0xCC, 0xCC))

    _set_notes(sl, _clean_title(slide.title), slide.talking_points)
    return sl


# ── Deck assembly ────────────────────────────────────────────────────────────

def build_pptx(slides: list, out_path: Path) -> None:
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H

    for slide in slides:
        if slide.treatment == 'text-only':
            build_text_slide(prs, slide)
        elif slide.image_path:
            # Image generated, table stylized, or existing image — all full-bleed
            build_image_slide(prs, slide)
        elif slide.treatment == 'table':
            # Fallback: stylize failed or --no-images; render native table
            build_table_slide_native(prs, slide)
        else:
            # Unspecified / missing — white placeholder
            build_image_slide(prs, slide)

    prs.save(str(out_path))
    print(f"\n✓  Saved → {out_path}")


# ── Entry point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Stream-dispatch image generation for a module and assemble its .pptx."
    )
    parser.add_argument("markdown", help="Path to the module lesson .md file")
    parser.add_argument("--slides", "-n", type=int, default=None,
                        help="Max number of slides to process (omit for all)")
    parser.add_argument("--no-images", action="store_true",
                        help="Skip image generation; render placeholders / native tables")
    parser.add_argument("--prompts", type=Path, default=None,
                        help="Path to image-prompts sidecar (default: <lesson-stem>_image_prompts.md)")
    args = parser.parse_args()

    md_path = Path(args.markdown).expanduser().resolve()
    if not md_path.exists():
        sys.exit(f"❌  File not found: {md_path}")

    # Auto-detect sidecar prompts file
    if args.prompts:
        prompts_path = args.prompts.expanduser().resolve()
    else:
        # Try several conventions
        stem = md_path.stem
        candidates = [
            md_path.with_name(f"{stem}_image_prompts.md"),
            md_path.with_name("image_prompts.md"),
            md_path.parent / f"{stem.split('_')[0]}_image_prompts.md",
        ]
        prompts_path = next((p for p in candidates if p.exists()), candidates[0])

    print(f"Lesson    {md_path.name}")
    print(f"Prompts   {prompts_path.name}{' (not found — falling back to inline)' if not prompts_path.exists() else ''}")

    slides = parse_lesson(md_path, max_slides=args.slides)
    prompts = parse_prompts_file(prompts_path)
    attach_specs(slides, prompts)

    # Treatment summary
    counts = {}
    for s in slides:
        counts[s.treatment] = counts.get(s.treatment, 0) + 1
    print(f"Found {len(slides)} slides — " +
          ", ".join(f"{n} {k}" for k, n in counts.items()))
    print()

    module_dir = md_path.parent
    images_dir = module_dir / "images"

    if args.no_images:
        print("Images    → skipped (--no-images)")
    else:
        print(f"Images    → {images_dir}")

    dispatch_all(slides, images_dir, module_dir, skip_generation=args.no_images)

    out_path = md_path.parent / (md_path.stem + ".pptx")
    print(f"\nBuilding  → {out_path}")
    build_pptx(slides, out_path)


if __name__ == "__main__":
    main()
