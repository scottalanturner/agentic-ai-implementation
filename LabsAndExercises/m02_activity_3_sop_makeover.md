# Activity: SOP Makeover

## Overview

Most people's first instinct when talking to an AI is to write something like: *"Summarize this and tell me what to do."* That instruction is technically valid. It's also nearly useless for an agent operating on your behalf.

An agent's system prompt is its Standard Operating Procedure — its standing instructions for what it is, what it has access to, what it must never do, and when to stop and ask a human. A weak SOP produces generic output. A strong SOP produces accountable, repeatable behavior you can actually defend to a manager.

This activity gives you a broken SOP and a framework to fix it — using a scenario from your own work.

---

## Goals

- Apply the SOP framework (role, inputs, task, constraints, output format, escalation trigger) to a real workplace scenario
- Understand *why* each element matters — not just what it is
- Produce a first draft of an agent instruction set you could actually use

---

## The SOP Framework

Every strong agent system prompt contains six elements:

| Element | What it defines | Why it matters |
|---------|----------------|---------------|
| **Role** | Who the agent is and what it's optimized for | Sets the reasoning frame — a compliance agent reasons differently than a sales agent |
| **Inputs** | What data the agent has access to and can read | Prevents hallucination by defining the edges of the agent's knowledge |
| **Task** | The specific thing it must accomplish, step by step | Keeps the agent on-task in a multi-turn loop |
| **Constraints** | What it must never do, never say, never access | Defines the blast radius if something goes wrong |
| **Output Format** | Exactly how the response should be structured | Makes downstream use predictable and auditable |
| **Escalation Trigger** | The specific condition that makes the agent stop and hand off to a human | The most important element in any production deployment |

---

## Step 1: Personalize Your Scenario

Open Claude or ChatGPT and paste the following. Fill in the brackets with your real situation.

```
I'm about to practice writing a system prompt (SOP) for an AI agent.
I work as [your role] at [your company or type of company].
My main responsibilities include [2–3 things you actually do].

Describe a realistic, specific task that an AI agent could handle on my behalf —
something repetitive, multi-step, and important enough that doing it wrong would
have a real consequence. Write it as 2–3 sentences. Then write a deliberately
weak version of a system prompt someone might write for it in a hurry (one or
two vague sentences, missing most of the SOP elements).
```

You'll use both the task description and the weak prompt it generates for this activity.

---

## Step 2: Diagnose the Broken Prompt

Using the weak prompt your AI generated, fill in this diagnosis table:

| SOP Element | Present? (Y/N) | What's missing or wrong |
|-------------|---------------|-------------------------|
| Role | | |
| Inputs | | |
| Task | | |
| Constraints | | |
| Output Format | | |
| Escalation Trigger | | |

Circle the single most dangerous missing element — the one that could cause the biggest problem in a real deployment.

---

## Step 3: Write the Real SOP

Rewrite the prompt using all six elements. Be specific. No vague language. If you write "be helpful" or "do a good job," rewrite it until it's concrete enough that two different agents following this instruction would behave identically.

Use this structure:

```
ROLE: [One sentence — who this agent is and what it's optimized for]

INPUTS: [What data or documents it has access to. What it does NOT have access to.]

TASK:
1. [First step — specific]
2. [Second step — specific]
3. [Continue until complete]

CONSTRAINTS:
- [What it must never do]
- [What it must never say]
- [What it must never access or modify]

OUTPUT FORMAT: [Exactly how the response should look — structure, length, required fields]

ESCALATION TRIGGER: [The exact condition — specific, not vague — that makes the agent stop and hand off to a human]
```

---

## Reflection Questions

1. Which SOP element was hardest to write for your scenario? Why?

2. Your escalation trigger is the most important safety mechanism your agent has. Read yours aloud. Is it specific enough that the agent would reliably know when to trigger it — or is there an edge case where it would fail to escalate when it should?

3. How would you test whether your SOP is working? What's the simplest question you could ask the agent that would reveal whether it understood its constraints?

4. Imagine you hand this SOP to a new AI platform six months from now. Does anything in it become stale or incorrect? What's your maintenance plan?

---

## Why This Matters

This is P1. The Agent Card you'll submit next week is a structured version of what you just built here. The difference between a toy agent and a production agent is almost never the model — it's whether someone wrote a real SOP before they hit deploy.
