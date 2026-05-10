# Course Concierge (voice demo)

Small desktop demo for **ISYS 398U — Agentic AI Implementation**: a **Course Concierge** triage agent on the **OpenAI Realtime API** (`gpt-realtime-1.5`) that **hands off** the live voice session to:

| Agent | Capability pattern |
|--------|-------------------|
| **SyllabusAgent** | RAG via OpenAI **vector store search** (`search_syllabus` tool) |
| **AssignmentAgent** | Local **JSON** (`data/assignments.json`) |
| **DataAgent** | **MCP** — `@modelcontextprotocol/server-postgres` (stdio) against your `DATABASE_URL` |

The default UI (`python app.py`) uses your **browser** for microphone and speaker: the page streams **PCM16** over a **WebSocket** to this repo’s **FastAPI** server, which runs the same **RealtimeRunner** session as the teaching stack (semantic VAD, interruptions). **Input speech-to-text is disabled** (`transcription: null`); the model consumes audio natively.

For a **terminal-only** desktop loop with **sounddevice** (no browser), use `python run_cli.py`.

## Prerequisites

- **Python 3.10+**
- **Node.js** with `npx` (for the Postgres MCP server).
- **PortAudio** only if you use **`run_cli.py`**: on macOS, `brew install portaudio` if `import sounddevice` fails.
- **OpenAI API key** with access to Realtime and vector stores.
- **Local Postgres** (e.g. **Supabase** `supabase start`) reachable via `DATABASE_URL`.

## Setup

```bash
cd Applications/mcp_powered_voice_agent
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env: OPENAI_API_KEY, DATABASE_URL
```

### 1) Syllabus vector store (one-time, re-run after syllabus edits)

```bash
python ingest.py
```

`ingest.py` copies `*.md` from the repo’s top-level [`Syllabus/`](../../Syllabus/) folder into `data/syllabus/` when that folder exists, then uploads those files. Copy the printed `SYLLABUS_VECTOR_STORE_ID` into `.env` (no quotes). Re-run after you change the canonical syllabus so the vector store matches.

### 2) Optional demo rows for Postgres

```bash
psql "$DATABASE_URL" -f data/demo_seed.sql
```

### 3) Run the UI

```bash
python app.py
```

Your browser opens to a small page: tap **Call in**, allow the microphone, speak, then **Hang up**.

### CLI (local mic/speaker, no browser)

```bash
python run_cli.py
```

Use **Ctrl+C** to hang up. Status and errors print in the terminal.

### Server only (optional)

```bash
uvicorn web_server:app --host 127.0.0.1 --port 8765
```

Then open `http://127.0.0.1:8765/` manually.

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI key |
| `SYLLABUS_VECTOR_STORE_ID` | Yes | From `ingest.py` |
| `DATABASE_URL` | Yes | Postgres URL (Supabase local often `postgresql://postgres:postgres@127.0.0.1:54322/postgres`) |

## How to extend

- **Agents and handoffs:** edit [`agents_def.py`](agents_def.py) — add `RealtimeAgent`s and `realtime_handoff(...)`, or change concierge routing instructions.
- **Tools:** edit [`tools.py`](tools.py) — add `@function_tool` functions and attach them to the right `RealtimeAgent`.
- **Syllabus corpus:** add or replace `.md` files under [`data/syllabus/`](data/syllabus/), then re-run **`python ingest.py`** (or create a new vector store in the dashboard and update `.env`).
- **Assignments:** edit [`data/assignments.json`](data/assignments.json).
- **Audio / session wiring:** see [`voice_session.py`](voice_session.py) (CLI / desktop) and [`web_server.py`](web_server.py) (browser path), both aligned with OpenAI’s [`examples/realtime/cli/demo.py`](https://github.com/openai/openai-agents-python/blob/main/examples/realtime/cli/demo.py).

## Project files

| File | Role |
|------|------|
| `app.py` | Starts uvicorn + opens the browser |
| `web_server.py` | FastAPI + WebSocket ↔ Realtime session (MCP Postgres, no input STT) |
| `static/` | Minimal call-in page and AudioWorklets |
| `run_cli.py` | Headless runner |
| `voice_session.py` | RealtimeRunner, MCP stdio, sounddevice mic/speaker loop |
| `agents_def.py` | Four `RealtimeAgent` definitions + handoffs |
| `tools.py` | `search_syllabus`, `list_assignments`, `get_assignment` |
| `ingest.py` | Create vector store + upload `data/syllabus/*.md` |

## Notes

- **Canvas LMS** is not integrated. Syllabus answers come from files you ingested into the vector store; assignment blurbs from `data/assignments.json`; structured rows from **Supabase** via MCP.
- The Postgres MCP package is **read-only**; the model can `SELECT` but not mutate data.
- **Secrets:** this demo is for local teaching; do not ship your API key or production `DATABASE_URL` in student-facing repos.
