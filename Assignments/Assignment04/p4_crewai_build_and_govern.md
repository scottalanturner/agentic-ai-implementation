# Project 4 — Build a Crew and Govern It


---

## Overview

In Module 9 you saw how multi-agent systems are structured — orchestration patterns, handoff contracts, the manager-worker relationship, what goes wrong when the design is loose. In this project you build a real crew around a workflow you actually know, and then you govern it.

The governance is not a separate step you bolt on at the end. It is built into how you configure the crew: which tools each agent gets, where you place a human checkpoint, and what the execution timeline tells you after the crew runs. These are the same controls you would apply in a production deployment. The difference between a demo and a system someone can trust is whether you made those decisions deliberately.

CrewAI Studio exposes three governance mechanisms directly in its visual editor:

- **Tool scoping** — each agent is given only the tools it needs for its task. An agent that summarizes text has no business making web requests. You decide.
- **Human-in-the-loop (HITL)** — tasks can be flagged to require human review and approval before the crew continues. This is the tripwire concept from Module 8, built into the platform.
- **Execution timeline** — every run produces a log of which agent fired, what it received, and what it produced. This is the audit trail. You will read it.

By the end of this project you will have built something that works, made deliberate governance decisions, and documented the risks that remain.

---

## What You Need Before You Start

- Your CrewAI Studio account (free tier, 50 executions per month — created during Module 9 content)
- A specific multi-step workflow you want to automate — from work, school, a club, a volunteer role, or any recurring task you actually do. The more real it is, the more useful this project becomes.
- 60–90 minutes of focused work time. Do not split this into short sessions — the build, run, and audit steps build on each other and the context matters.

**Choosing your workflow:** the best workflows for this project have three to five steps, a clear end product, and at least one step where you would normally want a human to review the output before it goes anywhere. If you are unsure, any of the four scenarios from the Module 9 activity (deal desk, internal research request, onboarding documentation, or your own) work well — but push further than you did in the activity.

---

## Part 1 — Design Before You Build

Before you open CrewAI Studio, answer these questions in writing. They become the benchmark you audit against in Part 4.

### 1a — Workflow Description

In two to four sentences, describe the workflow you are automating. Name:
- What triggers it (what causes it to start)
- What the end product is (what someone receives when it is done)
- Who would normally do each step manually

### 1b — Agent Design

Name the agents your crew will need. For each one, fill in this table:

| Agent name | Role in one sentence | Tools it needs | Tools it does NOT need |
|------------|---------------------|----------------|------------------------|
| | | | |
| | | | |
| | | | |

The "tools it does NOT need" column is not optional. Naming what an agent should *not* have access to is the permission scoping decision. If you give every agent every tool, you have not made a scoping decision — you have skipped one.

### 1c — Orchestration Pattern

Which process will you use — Sequential or Hierarchical — and why? Answer in two to four sentences. Reference the specific characteristics of your workflow that drove the choice. "The AI Copilot picked it" is not an answer.

### 1d — Human Checkpoint

Name one task in your crew where you would require human review before the crew continues. Answer these three questions:

1. Which task is it, and why is that the right place to pause?
2. What would a reviewer need to see in the approval packet? Name five fields, no more.
3. Is the action that follows the checkpoint reversible or not? (If it is not reversible — an email sent, a document published, a record updated — that is exactly where the checkpoint belongs.)

---

## Part 2 — Build the Crew in CrewAI Studio

Now build what you designed. Use the AI Copilot to generate your initial crew, then shape it to match your Part 1 design.

### Step 1 — Generate with the AI Copilot

Open CrewAI Studio. In the Crew Studio canvas, paste a prompt describing your workflow. Let the Copilot generate the initial crew.

**Do not edit yet.** Screenshot the canvas as it was generated. You will compare it to your final version in Part 4.

### Step 2 — Align with Your Design

Review what the Copilot built against your Part 1 answers. Make adjustments so the crew matches your design:

- Confirm or change the **Process type** to match your Part 1c choice
- For each agent, review the **tools attached** and remove any that violate your Part 1b scoping decisions
- Add or remove agents if what the Copilot generated does not match your Part 1a workflow

Screenshot the final canvas with the Process type visible in the settings panel.

### Step 3 — Enable the Human Checkpoint

Find the task you identified in Part 1d. In that task's settings, enable **Human Input** (the toggle or flag that pauses the crew and requests human review before continuing).

If you cannot find the Human Input toggle for a task in the current version of CrewAI Studio:

> Use the AI assistant built into the Studio and ask: *"How do I enable human input on a specific task in this crew?"* If the feature is not available via the visual editor in the current platform version, document what you would configure and why, and proceed with the run.

Screenshot the task settings panel showing the Human Input setting enabled (or your documentation if the feature is not currently available in the UI).

---

## Part 3 — Run the Crew and Read the Timeline

Run your crew once. Provide realistic test input — not placeholder text. A crew built to research a company should receive an actual company name, not "Company X."

**Free-tier limit reminder:** the 50 executions per month is shared across everything you do in your account. One careful, deliberate run is worth more than five rushed ones.

After the run completes:

1. Open the **Execution Timeline** (or Traces panel, depending on the current UI label).
2. Read through each agent's entry. For each agent, note:
   - What input it received
   - What output it produced
   - Whether the handoff to the next agent looks correct
3. If you enabled the Human Input checkpoint: document what the pause looked like and what information was presented to you for review. Did it give you what you said you needed in Part 1d?

Screenshot the execution timeline showing at least two agents' outputs.

---

## Part 4 — Governance Audit

Now audit what you built against your Part 1 plan and against the Module 8 threat framework. This is the part of the project that mirrors what a real review would look like before a system goes into production.

### 4a — Design vs. Reality

Compare the crew the AI Copilot generated in Part 2, Step 1 against the crew you actually submitted.

Answer in writing:
- Which agents or tools did you change, and why?
- Did the Copilot's process type match your Part 1c choice? If not, what did it pick and what does that tell you about how the platform reads your scenario?
- Is there anything the Copilot included that you do not fully understand? Name it honestly.

### 4b — Tool Scope Review

For each agent in your final crew, verify that its tool list matches your Part 1b plan. Fill in this table:

| Agent | Tools in Part 1b plan | Tools in final crew | Match? | If not, explain |
|-------|-----------------------|---------------------|--------|-----------------|
| | | | | |
| | | | | |

If an agent ended up with tools you did not plan for, that is not automatically wrong — but it requires an explanation.

### 4c — Threat Class Assessment

The Module 8 framework named four threat classes that apply to any agent system. Apply them here:

| Threat class | What it could look like in your crew | Does your crew have a mitigation? |
|--------------|--------------------------------------|----------------------------------|
| **Prompt injection** — an input to your crew contains hidden instructions that redirect an agent's behavior | | |
| **Tool abuse** — an agent uses a tool in a way the workflow did not intend | | |
| **Over-permissioning** — an agent has access to more than it needs to do its job | | |
| **Data leakage** — one agent's output surfaces information to another agent (or to the final output) that should not be there | | |

For each threat class, the mitigation you name should be something specific to your crew's design — not a generic statement. "I limited the research agent to web search only" is specific. "Be careful" is not.

### 4d — Audit Trail Evaluation

Look at the execution timeline from Part 3. Answer these three questions in two to four sentences each:

- **What does the timeline capture, and what is missing?** Could you reconstruct a problematic agent decision from the timeline alone, or would you need something else?
- **Who in a real organization would need access to this log, and how often?** Daily, weekly, only after an incident? Why?
- **What is the longest period you would feel comfortable letting this crew run with no human reviewing the timeline?** Be specific about the threshold beyond which review becomes mandatory — and say what about your specific crew drives that number.

### 4e — Top 3 Risks + Top 3 Mitigations

Close the audit with two short lists.

**Top 3 risks remaining** — what would you flag to a manager before this crew ran for real outside this course?

**Top 3 mitigations to implement before that happens** — concrete next steps, in priority order.

These two lists are what a real handoff to operations looks like. If you were handing this crew to someone else to own next quarter, this is the page they would read first.

---

## Part 5 — Reflection

Answer both questions in two to four sentences each. Specific answers from your actual build and audit earn more credit than general statements.

**1. You made at least one governance decision in this project that the platform did not make for you — scoping a tool, placing a checkpoint, or removing something the AI Copilot generated. Describe that decision and the reasoning behind it.**

The AI Copilot is generating a crew based on pattern matching, not based on your organization's risk tolerance or your workflow's specific failure modes. The decision you made manually is the one that reflects judgment, not just generation. Name it.

**2. If this crew ran at your workplace and produced a wrong or harmful output, who would own the response — and what specifically would they need from the execution timeline to investigate?**

Not "IT." Not "the person who built it." Name the actual function — operations, legal, a content owner, a specific team — and say what entry in the timeline would tell them where the failure happened.

---

## Submission Requirements

Your submission is a single PDF or Word document uploaded to Blackboard. It must contain, in order:

1. **Part 1** — Workflow description, agent design table, orchestration pattern rationale, human checkpoint design (all four sections)
2. **Screenshot 1** — The AI Copilot's initial canvas output (before your edits)
3. **Screenshot 2** — Your final canvas with the Process type visible
4. **Screenshot 3** — The task settings panel showing the Human Input setting (or documentation of the platform limitation)
5. **Part 3** — Run notes: handoff observations and (if enabled) the human checkpoint experience
6. **Screenshot 4** — Execution timeline showing at least two agents' outputs
7. **Part 4** — Full governance audit: design vs. reality, tool scope table, threat class table, audit trail evaluation, top 3 risks + top 3 mitigations
8. **Part 5** — Both reflection questions answered

---

## Grading Rubric

See the separate **rubric.md** file in this folder for the full three-level rubric (Novice / Competent / Proficient) for each criterion.

---

## A Note on "The AI Copilot Built It, Not Me"

The AI Copilot generates a crew. You govern it. If you submit the Copilot's output without changes and cannot explain why each agent has the tools it does, you have not done Part 2. The governance decisions in Part 1 exist so that when you look at what the Copilot built, you have a benchmark to measure it against. The delta between what the Copilot produced and what you submitted is where the learning happened.

---

## A Note on Platform Changes

CrewAI Studio is a live product that updates frequently. Labels move, features appear and disappear from the free tier, and the canvas layout changes. If something looks different from what this document describes, ask the AI assistant built into the Studio: *"I'm trying to [do X]. Here's what I see — where do I find it?"* That is a legitimate use of the tool and a legitimate skill.

---
