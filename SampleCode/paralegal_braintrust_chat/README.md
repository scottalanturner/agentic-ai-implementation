# Paralegal Braintrust chat demo

A minimal teaching demo: a **simple web chat** talks to a **Node server** that runs a **while-loop agent** (model ↔ tools in a loop) with **Braintrust** tracing and **OpenAI** chat completions. The scenario is a **litigation paralegal** assistant; all “systems” are **mock data in memory**—no real court APIs.

Related background: [Braintrust — Building reliable AI agents (AgentWhileLoop)](https://www.braintrust.dev/docs/cookbook/recipes/AgentWhileLoop) and the [example source](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/AgentWhileLoop).

---

## What runs where

| Piece | Role |
|--------|------|
| `public/index.html` + `public/app.js` | Browser UI; sends the user message to `POST /api/chat`, keeps a `sessionId` for multi-turn history. |
| `src/server.ts` | Express app; builds the message list (system prompt + prior turns + new user message), calls the agent, stores history per session. |
| `src/agent.ts` | **While-loop agent**: calls OpenAI with `tools`; if the model asks for tool calls, runs your code and sends results back; repeats until the model returns plain text (or max iterations). Uses `wrapOpenAI` and `traced` so Braintrust records spans. |
| `src/tools.ts` | Definitions of the **callable functions** the model is allowed to use (name, description, JSON schema for arguments, and the TypeScript `execute` body). |
| `src/mock-store.ts` | Fake matters, deadlines, e-filings, and conflict rows—the **only source of truth** the tools read from. |
| `src/run-scores.ts` | **Rules-based automated scores** (0–1) computed after each run; attached to the root trace via Braintrust **`logFeedback`** so the dashboard shows numeric signals without manual clicking. |
| `src/capture-dataset.ts` | When the user prefixes a message with **`/capture`**, inserts one row into a Braintrust **dataset** (`live-captures` by name) after a successful reply—so you can promote a live turn into eval data without touching the UI. |

API keys stay on the **server** (`.env`), not in the browser.

---

## Setup

1. Copy `.env.example` to `.env` and set `BRAINTRUST_API_KEY` and `OPENAI_API_KEY` (see comments in `.env.example`).
2. `npm install`
3. `npm start` — open the URL printed in the terminal (default port `3847`).

---

## `/capture` — save a live turn to a Braintrust dataset

For class demos, prefix a message with **`/capture`** and a space, then your question, e.g.  
`/capture What is the status of filing EF-88402?`

- The **model** only sees the part after `/capture` (the prefix is stripped server-side).
- After a successful assistant reply, the server calls **`initDataset` + `insert` + `flush`** so a row appears under **Project → Datasets →** `live-captures` (or `BRAINTRUST_CAPTURE_DATASET` if you set it).
- **`input`** on the row: `{ user_message, session_id }` (good for replaying a single-turn eval later).
- **`metadata`**: full raw line (including `/capture`), assistant reply, timestamps, tags `demo` / `slash-capture`.
- **`expected`** is left unset so you can add a gold answer later in the Braintrust UI when curating.

The green box on the chat page explains this for students; the chat log shows a **Braintrust** note with the dataset name and record id when capture succeeds.

---

## Understanding `tools.ts` (what is actually going on?)

You are **not** creating tools inside Braintrust. Braintrust **observes** what happens when tools run (spans, inputs, outputs). The tools themselves are **ordinary TypeScript objects** in your repo that the **OpenAI Chat Completions API** understands as **function tools**.

### The `Tool` shape

Each tool is one object with four fields:

1. **`name`** — Stable identifier the model must use (e.g. `search_matters`). OpenAI sends this back when it wants a tool.
2. **`description`** — Human-readable text **for the model**: when to use this tool and what it is for. Good descriptions steer behavior.
3. **`parameters`** — A **Zod** schema describing the **arguments** the model should pass (types, required fields, and `.describe()` hints that become part of the JSON Schema).  
   In `agent.ts`, `zodToJsonSchema` converts that Zod object into **JSON Schema**, which OpenAI requires for function calling.
4. **`execute`** — **Your code**. When the model returns a tool call, the agent parses the JSON arguments, calls `execute`, and appends the **string** result to the conversation as a `tool` message. The model then continues and may call more tools or answer the user.

So: **“Programmatically creating tools”** here means **defining a list of `{ name, description, schema, function }` objects in code** and registering them with each completion request. The model picks among them; your server runs `execute`.

### End-to-end flow for one tool call

1. User asks something in the browser.
2. Server sends messages to `WhileLoopAgent.run(...)`.
3. Agent calls `chat.completions.create` with `tools: [...]` built from every entry in `getAllTools()`.
4. The model may respond with **`tool_calls`**: each has a function `name` and JSON `arguments`.
5. The agent looks up `name` in a `Map`, runs `tool.execute(parsedArgs)`, gets a **string** (often multi-line text for the model to read).
6. That string is sent back to the model as a tool result; the loop continues.
7. Braintrust records nested spans (iterations, tool names, logged inputs/outputs) so you can audit the run in the UI.

### What each tool in this file does

All four tools only read or format **mock data** from `mock-store.ts`. They return **text** for the model to summarize for the user.

| Tool | Purpose |
|------|--------|
| **`search_matters`** | Filter the in-memory matter list by a free-text `query` (client name, matter id fragment, caption words, etc.). |
| **`get_matter_calendar`** | Given a **`matterId`** (e.g. `M-24087`), return upcoming events and open deadlines for that one matter. |
| **`check_efiling_status`** | Either look up one **`submissionId`** (e.g. `EF-88402`) or list filings for a **`matterId`**. |
| **`conflict_check_contact`** | Run a toy conflict screen on **`contactName`** (+ optional **`organization`**) against a tiny mock index. |

`getAllTools()` simply returns an array of those four objects so `server.ts` / `agent.ts` can pass one list into the agent.

### Why Zod + `.describe()`?

- **Validation**: `execute` uses `SomeSchema.parse(raw)` so bad model output fails fast with a clear Zod error (then surfaced as a tool error string).
- **Documentation for the model**: `.describe()` on each field is included in the JSON Schema OpenAI sees, which usually improves argument quality.

---

## Evaluation foundation (terminology + Braintrust setup)

**Terms (short):**

| Term | Meaning here |
|------|----------------|
| **Trace / log** | One end-to-end run (your chat turn): nested spans (`paralegal_agent_run` → `iteration_*` → tool spans) plus model traffic from `wrapOpenAI`. |
| **Span** | One unit of work in that tree (whole agent run, one LLM iteration, one tool execution). |
| **Scorer** | Anything that turns a run into **numbers or labels** (human rubric, code rules, LLM-as-judge, etc.). |
| **Feedback** | Braintrust’s way to attach **scores** (and optional comments) **to an existing logged event**—here, the root span after the run finishes (`Span.logFeedback` with `scores`). |
| **Experiment / dataset** (not in this demo) | Offline **batch** eval: many inputs in a **dataset**, same agent, aggregate scores—typical for CI and regression. This repo uses **online-style** rule scores on each live run instead. |

**What you need in Braintrust (manual):**

1. Account + **`BRAINTRUST_API_KEY`** (same as logging).  
2. A **project** — still created automatically from `BRAINTRUST_PROJECT_NAME` / `initLogger` when logs arrive.  
3. **Nothing extra is required** for the automated scores to appear: they are sent in **code** with the same API key. In the UI, open the latest **`paralegal_agent_run`** row and look for **scores / feedback** on that event (labels vary by Braintrust version; it is the data attached by `logFeedback`).

**Scores this demo attaches (all 0–1, rules-based):**

| Score key | Interpretation |
|-----------|----------------|
| `used_tools` | `1` if the transcript includes at least one `tool` message (model invoked a tool at least once). |
| `clean_tool_execution` | `1` if there were no tool messages, or none whose text looks like a tool error. |
| `completed_with_assistant_reply` | `1` if the run ended with a non-empty assistant text message. |
| `stopped_before_iteration_ceiling` | `1` if the while-loop exited before hitting `maxIterations`. |

These are **pedagogical signals**, not product-ready quality metrics. In class you can say: *real teams add scorers that encode policy (“must call `search_matters` when user asks about an unknown matter”), LLM judges with rubrics, and human review on low scores.*

**Suggested class arc (your plan, refined):**

1. **Live chat** — Have a realistic dialogue (docket + e-filing + conflict).  
2. **Braintrust** — Open the project → **Logs** → the newest **`paralegal_agent_run`**: expand spans (prove tool path), then show **scores / feedback** on that same row.  
3. **“So what?”** — Explain what a team does next: filter logs where `used_tools === 0` but the user asked a factual question; investigate `clean_tool_execution === 0`; add a **dataset** case from that trace; fix prompt/tools; re-run an **experiment** or CI eval; watch scores move.

**Important caveat:** If you **removed** the `logFeedback` code, a chat would still be **logged**, but it would **not** “be scored” unless you or Braintrust ran something else. Scoring is always **someone’s policy** encoded in code, humans, or batch jobs—not magic inside “logging only.”

---

## Braintrust in one line

**Chat shows the final answer; Braintrust shows the trace** (LLM rounds, tool names, arguments, tool output strings) **and, in this repo, a few automated scores attached as feedback** on the root run.

---

## Scripts

| Command | Purpose |
|---------|--------|
| `npm start` | Run the server (production-style single process). |
| `npm run dev` | Same with `tsx watch` for local editing. |
