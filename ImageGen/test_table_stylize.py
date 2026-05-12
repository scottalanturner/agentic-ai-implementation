#!/usr/bin/env python3
"""
test_table_stylize.py — standalone prototype, step 2 of the table pipeline
──────────────────────────────────────────────────────────────────────────
Take a structurally-clean table PNG (produced by test_table_render.py) and
restyle it as a colored-pencil sketch via OpenAI's image edit endpoint.

The stylization prompt explicitly says "preserve every word, every row, and
every column" so the model treats the input as a structural anchor rather
than free-form inspiration.

Usage:
    python test_table_stylize.py <input.png> <output.png> [--model gpt-image-2]

Reads OPENAI_API_KEY from a .env file in this directory.
"""

import argparse
import base64
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

from openai import OpenAI


STYLIZE_PROMPT = (
    "Redraw this table as a colored-pencil sketch on a solid white background. "
    "Preserve every word, every row, and every column exactly as shown — do not "
    "add, remove, rephrase, or rearrange any text. Hand-letter all text in a "
    "casual pencil style. Replace the rigid black table borders with loose, "
    "slightly-imperfect hand-drawn pencil lines. Keep the layout, alignment, and "
    "structure unchanged — only the visual aesthetic changes. Use a muted "
    "earth-tone palette with one warm accent color."
)


def stylize_table(
    input_png: Path,
    output_png: Path,
    model: str = "gpt-image-2",
    size: str = "1536x1024",
    client: "OpenAI | None" = None,
) -> None:
    if not input_png.exists():
        sys.stderr.write(f"ERROR: input file not found: {input_png}\n")
        sys.exit(1)

    if client is None:
        if not os.environ.get("OPENAI_API_KEY"):
            sys.stderr.write(
                "ERROR: OPENAI_API_KEY not set. Check the .env file next to this script.\n"
            )
            sys.exit(1)
        client = OpenAI()

    with open(input_png, "rb") as f:
        result = client.images.edit(
            model=model,
            image=f,
            prompt=STYLIZE_PROMPT,
            size=size,
        )

    image_bytes = base64.b64decode(result.data[0].b64_json)
    output_png.parent.mkdir(parents=True, exist_ok=True)
    output_png.write_bytes(image_bytes)


def main():
    p = argparse.ArgumentParser(
        description="Restyle a structural table PNG as a colored-pencil sketch via OpenAI image edit."
    )
    p.add_argument("input_png", type=Path, help="Structural PNG from test_table_render.py")
    p.add_argument("output_png", type=Path, help="Where to write the stylized PNG")
    p.add_argument(
        "--model",
        default="gpt-image-2",
        help="OpenAI image model (default: gpt-image-2; falls back to gpt-image-1 if unsupported)",
    )
    p.add_argument(
        "--size",
        default="1536x1024",
        help='Output size — "1024x1024", "1536x1024", "1024x1536", or "auto"',
    )
    args = p.parse_args()

    stylize_table(args.input_png, args.output_png, model=args.model, size=args.size)
    print(f"✓ Stylized {args.input_png} → {args.output_png}")


if __name__ == "__main__":
    main()
