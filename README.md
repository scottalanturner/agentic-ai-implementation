# Agentic AI Implementation

Course application materials for **ISYS 398U — Agentic AI Implementation**: assignments, labs, optional image/PPTX helpers, and runnable sample code for teaching agentic patterns (voice, tools, MCP, RAG).

## What’s in this repo

| Folder | Contents |
|--------|----------|
| `Assignments/` | Project prompts, rubrics, and exemplars by assignment. |
| `LabsAndExercises/` | In-class activities and exercises (markdown). |
| `ImageGen/` | Scripts for assembling module visuals / decks (see files in that folder). |
| `SampleCode/mcp_powered_voice_agent/` | **Course Concierge** demo: FastAPI + OpenAI Realtime, syllabus RAG, Postgres via MCP. See its [README](SampleCode/mcp_powered_voice_agent/README.md) for setup and run instructions. |

## Local setup notes

- **Secrets:** Do not commit API keys or database URLs. This repo’s root `.gitignore` excludes `.env` files; create your own locally where samples expect them (for example under `SampleCode/mcp_powered_voice_agent/`).
- **Python:** Sample code targets **Python 3.10+**. Use a virtual environment inside the sample project before `pip install -r requirements.txt`.

## Contributing / teaching

Clone, branch, and open pull requests as you normally would. Students typically work from copies of assignment and lab files rather than editing this repo directly unless you assign that workflow.
