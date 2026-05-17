# Activity: Read the Monitoring Dashboard in n8n

**Format:** In-class activity — solo
**Time:** 12–15 minutes
**Requires:** A web browser · The free n8n account you created in Module 5

---

## Overview

In Module 5 you *built* a tool-calling agent in n8n and read its execution trace once — as a builder, checking that your wiring worked.

This activity uses the same workflow, but with a different job. A shipped agent runs over and over with nobody watching by default. The only way you know it is still healthy is to **look** — and n8n already keeps the record. Every time a workflow runs, n8n logs it in the **Executions** view: when it ran, whether it succeeded, how long it took, and what happened at every node.

That Executions view is a **monitoring dashboard**. Today you are the operator, not the builder. You will run an agent several times, read its dashboard, and find the run that should worry you.

---

## Goals

- Open and read n8n's Executions view as a monitoring dashboard — status, timing, run history
- Drill into a single run's trace to see *why* one run behaved differently from the others
- Tell the difference between a run that **errored** and a run that "succeeded" but produced a **bad answer** — and say why surface monitoring misses the second one
- Name the one metric you would put an alert on if this agent were live

---

## Step 1 — Reopen your Module 5 agent (about 2 minutes)

1. Go to [n8n.io](https://n8n.io) and sign in to the account you created in Module 5.
2. Open the workflow you built in Module 5 — **Chat Trigger → AI Agent (Wikipedia + Calculator) → Chat Reply**.

> **If you can't find your Module 5 workflow:** rebuild a minimal version fast — add a **When chat message received** node, an **AI Agent** node, attach the built-in **Wikipedia** and **Calculator** tools, and a **Chat Reply** node. No configuration beyond picking the model. Three minutes, and the Module 5 activity file has the full steps if you need them.

---

## Step 2 — Run it several times — including one run built to struggle (about 4 minutes)

Open the chat window (**Test workflow** or the **Chat** button) and send these prompts **one at a time**, letting each finish before the next:

1. `What is the population of Iceland?`
2. `How many times would the population of Iceland fit inside the population of the United States? Show your math.`
3. `What is the population of Canada divided by the population of Australia?`

Now send one more — a prompt the agent's two tools **cannot cleanly answer**:

4. `What is the current temperature in Reykjavik right now, and is it warmer than yesterday?`

The agent has a Wikipedia tool and a Calculator tool. Neither one returns live weather. Watch what the agent does with a question it isn't equipped for — it may stall, take extra steps, or hand back a confident answer that isn't actually grounded in anything.

---

## Step 3 — Open the Executions view — your monitoring dashboard (about 3 minutes)

1. Leave the chat. In the workflow, find the **Executions** tab (near the top of the workflow, sometimes shown as a list or clock icon).
2. You should see a row for **each run** you just did. For each row, n8n shows you:
   - **Status** — succeeded or errored
   - **Started** — the timestamp
   - **Run time** — how long it took
3. Read the dashboard like an operator. Ask:
   - Which runs took **longer** than the others?
   - Did run 4 (the weather question) look different in status or run time?
   - If you saw this list every morning for a live agent, what would "a normal day" look like — and what would make you stop and click?

This list is the same thing a production monitoring tool gives you, just smaller. It is the difference between *knowing* your agent is healthy and *hoping* it is.

---

## Step 4 — Drill into one run — read the trace (about 3 minutes)

1. Click the **run 4** execution (the weather question) to open it.
2. Click the **AI Agent node** to expand its trace — the same trace view you read in Module 5.
3. Look for:
   - How many tool calls did it make? More than the simple runs?
   - Did a tool return something useless, and did the agent try again, or just push forward?
   - What did the **final answer** actually say — and was any of it really grounded in a tool result?

Here is the key observation: **run 4 may show "succeeded" in the dashboard even though the answer was bad.** The status light is green. The answer is not. Surface monitoring — did it run, did it error — cannot catch that. Catching it needs someone looking at *outcomes*, not just status.

---

## Step 5 — Reflect (about 3 minutes)

Answer these two questions in a few sentences each:

**1. Which one metric would you alert on?**
If this agent were live and you could only watch *one* number — run time, error rate, number of tool calls per run, something else — which would you pick, and what would the alarm threshold be? Why that one?

**2. What would the dashboard *not* tell you?**
Run 4 may have shown "succeeded." Name one thing that could go wrong with a live agent that this Executions view would never reveal on its own — and what you'd need *in addition* to catch it.

---

## Reflection

Think about your answer to question 1. The concepts here connect to the slide that comes next — *Pick the metric that matters* — and to the idea of **behavioral drift**: the agent that keeps showing "succeeded" while quietly getting worse.

---

## Why This Matters

Most agent projects end at "we launched it." Nobody decided what *still working* looks like, and nobody looks until a user complains. The Executions view you just read is the cheapest possible version of the discipline that prevents that — **Layer 4 monitoring**, the one part of evaluation that happens after launch and never stops.

You did not need a paid observability platform. You needed to know the dashboard was there, and to look at it like an operator.

---

## Quick Reference — What You Read

| Part of the dashboard | What it tells you | What it cannot tell you |
|-----------------------|-------------------|--------------------------|
| **Status** (succeeded / errored) | Did the workflow finish without crashing | Whether the answer was actually correct |
| **Run time** | How long this run took — your latency signal | Why it was slow |
| **Run history list** | The pattern over time — what "normal" looks like | When "normal" has slowly drifted |
| **Per-node trace** | What happened at each step — tool calls, data, final answer | The user's reaction to the answer |

---

*Activity for Module 10 — ISYS 398U Agentic AI Implementation | University of Richmond SPCS*
