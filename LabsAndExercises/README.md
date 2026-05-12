# Labs & Exercises

In-class activities and labs for ISYS 398U — Agentic AI Implementation. One file per activity, named by module and short title.

This is a working index. Activities continue to be developed, revised, and re-sequenced as the course evolves.

---

## Conventions

- **Naming:** `mNN_activity_*.md` — `NN` is the module number; the rest is a short slug.
- **Format:** Every activity is **solo** and **Zoom-compatible (possibly async)**. Free tools only — no credit card, no IT install.
- **Supporting assets:** When an activity needs source files, they live in a `data/` subfolder next to the activity file (e.g., `m03_activity_1/data/`, `m04_activity_3_failure_detective/data/`).
- **Planning doc:** Module 4's activities-in-progress outline lives at `m04_activities_outline.md`.

---

## Module 1 — Where AI Earns Its Keep

- **`m01_activity_1_agent_discovery_interview.md`** — Use an AI tool to interview yourself and surface specific places in your work (or, for undergrads, the work you're headed into) where agentic AI could act end-to-end, not just assist.
- **`m01_activity_2_transcript_lab.md`** — Generate a realistic meeting transcript from your own context, then use AI to extract action items, surface hidden intelligence, and produce a structured work product (project brief, stakeholder summary, or risk register).

---

## Module 2 — Inside an Agent's Head

- **`m02_activity_1_react_loop_trace.md`** — Trace two full Reason → Act → Observe cycles by hand on a scenario you generate yourself. Identify the exact step where the loop breaks under a given failure condition.
- **`m02_activity_2_pattern_spotter.md`** — Read five real-world agent descriptions and identify which of the four design patterns (reflection, tool use, planning, multi-agent) are at work — citing the specific behavior that gave each one away.
- **`m02_activity_3_sop_makeover.md`** — Take a deliberately weak system prompt and rewrite it as a Standard Operating Procedure using the six-element structure: role, inputs, task, constraints, output format, escalation trigger. Direct prep for Project 1.
- **`m02_activity_4_failure_detective.md`** — Diagnose four failure scenarios (masked error, hallucinated tool call, runaway loop, permission mismatch), then generate one from your own planned agent. Build the habit of spotting failures hiding in your own deployments.

---

## Module 3 — Did the Agent Actually Do the Job?

- **`m03_activity_1_score_a_summary.md`** — Score a deliberately flawed AI summary against the four evaluation dimensions (correctness, completeness, safety, fit) using a real policy document as ground truth. Source files in `m03_activity_1/data/`.
- **`m03_activity_2_ai_studio_rubric_judge.md`** — Encode your Score-a-Summary rubric into a judge prompt in Google AI Studio. Run it against the same summary and compare machine scores to your own.
- **`m03_activity_3_roi_calculator.md`** — Apply the three-lever ROI framework (time savings, error reduction, deflection) to a candidate use case from your Module 1 Discovery Interview. Produce a defensible annual estimate with a sensitivity range.
- **`m03_activity_braintrust_playground.md`** — Create a free Braintrust account, write two versions of a system prompt, run both against five test questions, and use LLM-as-judge to see which version actually performs better — with numbers, not vibes.

---

## Module 4 — Make Your Agent an Expert on Your Company

- **`m04_activity_1_two_answers_live.md`** — Upload a source document of your choice to NotebookLM, then ask the same three questions in NotebookLM (grounded) and in ChatGPT (ungrounded). Feel the difference between fluent and accountable answers.
- **`m04_activity_2_build_your_own_knowledge_agent.md`** — Stand up a working knowledge agent in NotebookLM using three sources on a topic you know well. Score five questions to catch chunking, retrieval, and generation in the act.
- **`m04_activity_3_failure_detective.md`** — Upload two deliberately conflicting syllabi plus the UR academic calendar to NotebookLM. Ask five diagnostic questions — one per grounding failure mode — and document what the tool actually does. Source files in `m04_activity_3_failure_detective/data/`.
- **`m04_activity_4_build_a_real_chatbot.md`** — Build a deployable knowledge chatbot in Chatbase (free tier). Walk out with a public chat URL and an embed snippet — the same artifacts a small business would put on a website.

---

## Module 5 — Agents With Hands

- **`m05_activity_elevenlabs_mcp_slack.md`** — Wire your Project 2 ElevenLabs voice agent to the class Slack workspace via MCP. When the escalation branch fires, a message posts automatically. Experience MCP as a practitioner, not just a concept.

---

*Modules 6 through 12 will be added as their activities are developed.*
