#!/usr/bin/env python3
"""
test_table_render.py — standalone prototype
────────────────────────────────────────────
Convert a markdown table to a clean PNG via local tooling only.

Pipeline:
    markdown → PDF (pandoc + xelatex) → PNG (pdftoppm)

This is step 1 of the table-stylization workflow. The PNG produced here is
structural ground truth — preserving exact rows, columns, and text. Step 2
(stylize via OpenAI image edit into colored-pencil sketch) will be added once
this prototype is validated.

Usage:
    python test_table_render.py <input.md> <output.png> [--dpi 300]

Dependencies (Mac: `brew install pandoc basictex poppler`):
    pandoc          (markdown processor)
    xelatex         (PDF engine — Unicode-safe; comes with basictex/mactex)
    pdftoppm        (Poppler — PDF rasterizer)
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def _require(binary: str) -> None:
    """Exit with a helpful message if a required binary is missing."""
    if shutil.which(binary) is None:
        sys.stderr.write(
            f"ERROR: '{binary}' not found on PATH.\n"
            f"Install on macOS via Homebrew. Quick mapping:\n"
            f"  pandoc   → brew install pandoc\n"
            f"  xelatex  → brew install --cask mactex  (or basictex for a slimmer install)\n"
            f"  pdftoppm → brew install poppler\n"
        )
        sys.exit(1)


def render_table_to_png(
    md_path: Path,
    png_path: Path,
    dpi: int = 300,
    paper_width_in: float = 11.0,
    paper_height_in: float = 6.0,
    margin_in: float = 0.4,
    fontsize: str = "11pt",
    columns: int = 200,
) -> None:
    """Render a markdown file (containing a table) to a clean, trimmed PNG."""

    for bin_name in ("pandoc", "xelatex", "pdftoppm"):
        _require(bin_name)

    if not md_path.exists():
        sys.stderr.write(f"ERROR: input file not found: {md_path}\n")
        sys.exit(1)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        pdf_path = tmp_path / "table.pdf"

        # Step 1 — markdown → PDF (pandoc + xelatex)
        # Tight custom paper so the page is mostly the table.
        geometry = (
            f"paperwidth={paper_width_in}in,"
            f"paperheight={paper_height_in}in,"
            f"margin={margin_in}in"
        )
        subprocess.run(
            [
                "pandoc",
                str(md_path),
                "-o", str(pdf_path),
                "--pdf-engine=xelatex",
                "--columns", str(columns),     # hint pandoc the page is wide so cells don't get cramped
                "-V", f"geometry:{geometry}",
                "-V", f"fontsize={fontsize}",
                "-V", "pagestyle=empty",       # suppress page numbers
            ],
            check=True,
        )

        # Step 2 — PDF → PNG (pdftoppm names outputs <prefix>-1.png, -2.png, ...)
        out_stem = tmp_path / "page"
        subprocess.run(
            [
                "pdftoppm",
                "-png",
                "-r", str(dpi),
                str(pdf_path),
                str(out_stem),
            ],
            check=True,
        )

        pages = sorted(tmp_path.glob("page-*.png"))
        if not pages:
            sys.stderr.write("ERROR: pdftoppm produced no output.\n")
            sys.exit(1)

        png_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(pages[0], png_path)


def render_table_markdown_to_png(
    md_content: str,
    png_path: Path,
    **kwargs,
) -> None:
    """Convenience wrapper: render markdown content (string) to a PNG.

    Writes the string to a temp file and delegates to render_table_to_png().
    Useful when calling from another script that already has the markdown in
    memory (e.g., build_module_pptx.py).
    """
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(md_content)
        tmp_md = Path(tmp.name)
    try:
        render_table_to_png(tmp_md, png_path, **kwargs)
    finally:
        try:
            tmp_md.unlink()
        except FileNotFoundError:
            pass


def main():
    p = argparse.ArgumentParser(description="Render a markdown table to a clean PNG.")
    p.add_argument("input_md", type=Path, help="Path to the markdown file")
    p.add_argument("output_png", type=Path, help="Where to write the PNG")
    p.add_argument("--dpi", type=int, default=300, help="Render DPI (default 300)")
    args = p.parse_args()

    render_table_to_png(args.input_md, args.output_png, dpi=args.dpi)
    print(f"✓ Rendered {args.input_md} → {args.output_png}")


if __name__ == "__main__":
    main()
