#!/usr/bin/env python3
"""Create an OpenAI vector store and upload all Markdown files from data/syllabus/."""

from __future__ import annotations

import shutil
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

_ROOT = Path(__file__).resolve().parent
_SYLLABUS_DIR = _ROOT / "data" / "syllabus"
# Canonical syllabus in the teaching repo (one level above Applications/)
_REPO_SYLLABUS = _ROOT.parent.parent / "Syllabus"


def _sync_syllabus_md_from_repo() -> int:
    """Copy *.md from repo Syllabus/ into data/syllabus/ so ingest always uploads the same files you edit."""
    if not _REPO_SYLLABUS.is_dir():
        return 0
    _SYLLABUS_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for src in sorted(_REPO_SYLLABUS.glob("*.md")):
        dest = _SYLLABUS_DIR / src.name
        shutil.copy2(src, dest)
        print(f"  Synced {src.name} → data/syllabus/")
        n += 1
    return n


def main() -> int:
    load_dotenv(_ROOT / ".env")
    client = OpenAI()

    synced = _sync_syllabus_md_from_repo()
    if synced:
        print(f"Synced {synced} markdown file(s) from {_REPO_SYLLABUS}\n")

    files = sorted(_SYLLABUS_DIR.glob("*.md"))
    if not files:
        print(f"No .md files found in {_SYLLABUS_DIR}", file=sys.stderr)
        return 1

    print(f"Creating vector store (uploading {len(files)} file(s))…")
    vs = client.vector_stores.create(name="ISYS 398U Syllabus (Course Concierge demo)")

    for path in files:
        print(f"  Uploading {path.name}…")
        with open(path, "rb") as fh:
            uploaded = client.files.create(file=fh, purpose="assistants")
        client.vector_stores.files.create(vector_store_id=vs.id, file_id=uploaded.id)

    print("Waiting for vector store file processing…")
    for _ in range(60):
        st = client.vector_stores.retrieve(vs.id)
        fc = st.file_counts
        completed = getattr(fc, "completed", 0) if fc else 0
        failed = getattr(fc, "failed", 0) if fc else 0
        if completed >= len(files) and failed == 0:
            break
        if failed > 0:
            print(f"Vector store reports failed uploads: {fc}", file=sys.stderr)
            return 1
        time.sleep(2)
    else:
        print("Timed out waiting for processing; check platform.openai.com/storage", file=sys.stderr)

    print("\nDone. Add this to your .env file:\n")
    print(f"SYLLABUS_VECTOR_STORE_ID={vs.id}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
