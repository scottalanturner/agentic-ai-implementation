"""Function tools for syllabus search (vector store) and assignment lookup (local JSON)."""

from __future__ import annotations

import json
import os
from pathlib import Path

from agents import function_tool
from dotenv import load_dotenv
from openai import OpenAI

_ROOT = Path(__file__).resolve().parent
_ASSIGNMENTS_PATH = _ROOT / "data" / "assignments.json"

# Realtime tool calls run in this process; always load the app .env from disk (cwd-independent).
load_dotenv(_ROOT / ".env")


def _require_vector_store_id() -> str:
    raw = os.environ.get("SYLLABUS_VECTOR_STORE_ID", "").strip().strip('"').strip("'")
    if not raw:
        raise RuntimeError(
            "SYLLABUS_VECTOR_STORE_ID is not set. Run `python ingest.py` once and add it to your .env file."
        )
    return raw


def _load_assignments() -> list[dict]:
    if not _ASSIGNMENTS_PATH.is_file():
        return []
    with open(_ASSIGNMENTS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return list(data.get("assignments", []))


def _chunk_text(chunk: object) -> str:
    if isinstance(chunk, dict):
        return (chunk.get("text") or "").strip()
    return (getattr(chunk, "text", None) or "").strip()


def _format_vector_hits(page: object) -> list[str]:
    lines: list[str] = []
    data = getattr(page, "data", None) or []
    for hit in data:
        if isinstance(hit, dict):
            fn = hit.get("filename") or "document"
            score = hit.get("score")
            chunks = hit.get("content") or []
        else:
            fn = getattr(hit, "filename", None) or "document"
            score = getattr(hit, "score", None)
            chunks = getattr(hit, "content", None) or []
        score_s = f"{score:.3f}" if isinstance(score, (int, float)) else "?"
        for chunk in chunks:
            text = _chunk_text(chunk)
            if text:
                lines.append(f"[{fn} | score={score_s}]\n{text}")
    return lines


@function_tool
def search_syllabus(query: str) -> str:
    """Search the ingested ISYS 398U syllabus and module markdown (OpenAI vector store). Use for schedules, policies, dates, outcomes, and module themes — call before stating any syllabus-specific fact."""
    load_dotenv(_ROOT / ".env")
    client = OpenAI()
    vs_id = _require_vector_store_id()
    # Prefer a simple search first (most reliable), then optional rewrite + rerank.
    base_kw: dict = {"max_num_results": 20}
    page = client.vector_stores.search(vs_id, query=query, **base_kw)
    lines = _format_vector_hits(page)
    if len(lines) < 2:
        page_r = client.vector_stores.search(
            vs_id,
            query=query,
            rewrite_query=True,
            max_num_results=15,
            ranking_options={"ranker": "auto"},
        )
        lines = _format_vector_hits(page_r)
    if not lines:
        expanded = f"{query} ISYS 398U syllabus schedule instructor credits outcomes assignment"
        page2 = client.vector_stores.search(vs_id, query=expanded, **base_kw)
        lines = _format_vector_hits(page2)
    if not lines:
        return (
            "No matching passages in the ingested syllabus pack. "
            "Re-run `python ingest.py` after syncing files into data/syllabus/ (ingest copies from "
            "../Syllabus/ when present), then verify SYLLABUS_VECTOR_STORE_ID in .env matches the new store."
        )
    return "\n\n---\n\n".join(lines)


@function_tool
def list_assignments() -> str:
    """List known assignments and activities with module, due timing, and short summaries."""
    items = _load_assignments()
    if not items:
        return "No assignments are configured in data/assignments.json."
    rows = []
    for a in items:
        name = a.get("name", "?")
        module = a.get("module", "?")
        due = a.get("due", "?")
        rows.append(f"- {name} ({module}) — due: {due}")
    return "Known assignments:\n" + "\n".join(rows)


@function_tool
def get_assignment(name: str) -> str:
    """Get details for one assignment. Pass a substring of the assignment name (e.g. 'discovery interview')."""
    needle = name.strip().lower()
    if not needle:
        return "Please provide part of the assignment name."
    items = _load_assignments()
    matches = []
    for a in items:
        hay = (a.get("name", "") + " " + a.get("summary", "")).lower()
        if needle in hay or needle in a.get("name", "").lower():
            matches.append(a)
    if not matches:
        return f"No assignment matched {name!r}. Use list_assignments to see options."
    if len(matches) > 1:
        names = ", ".join(m.get("name", "?") for m in matches[:5])
        return f"Multiple matches ({names}). Ask the student to be more specific."
    a = matches[0]
    parts = [
        f"Name: {a.get('name')}",
        f"Module: {a.get('module')}",
        f"Due: {a.get('due')}",
        f"Summary: {a.get('summary', '')}",
    ]
    if a.get("details"):
        parts.append(f"Details: {a['details']}")
    return "\n".join(parts)
