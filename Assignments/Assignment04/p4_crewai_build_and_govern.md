# Project 4 — Build a Crew and Govern It


---

## Overview

In Module 9 you saw how multi-agent systems are structured — orchestration patterns, handoff contracts, the manager-worker relationship, what goes wrong when the design is loose. In this project you build a real crew around a workflow you actually know, and then you govern it.

The governance is not a separate step you bolt on at the end. It is built into how you configure the crew: which tools each agent gets, where you place a human checkpoint, and what the run timeline tells you after the crew runs. These are the same controls you would apply in a production deployment. The difference between a demo and a system someone can trust is whether you made those decisions deliberately.

CrewAI Studio gives you three governance levers you will use in this project:

- **Tool scoping** — each agent is given only the tools it needs for its task. An agent that drafts a memo has no business making web requests. You decide.
- **Human-in-the-loop (HITL) as a design pattern** — you can dedicate a task in the crew to "wait for human approval" before the workflow finalizes. As you will discover in Part 3, the cloud-hosted visual editor does not actually pause execution for a real human — the agent generally fabricates approval. That gap is itself one of the most important governance findings in this project.
- **Run timeline (traces)** — every run produces a log of which agent fired, which LLM calls and tool calls it made, and what each one produced. This is the audit trail. You will read it.

By the end of this project you will have built something that works, made deliberate governance decisions, and documented the risks that remain.

---

## What You Need Before You Start

- Your CrewAI Studio account (free tier, 50 executions per month — created during Module 9 content)
- A specific multi-step workflow you want to automate — from work, school, a club, a volunteer role, or any recurring task you actually do. The more real it is, the more useful this project becomes.
- 60–90 minutes of focused work time. Do not split this into short sessions — the build, run, and audit steps build on each other and the context matters.

**Choosing your workflow:** the best workflows for this project have three to five steps, a clear end product, and at least one step where you would normally want a human to review the output before it goes anywhere. If you are unsure, any of the four scenarios from the Module 9 activity (deal desk, internal research request, onboarding documentation, or your own) work well — but push further than you did in the activity.

### First-time account setup — read this before you sign up

If you have already created your CrewAI account, skip this box. If this is your first time, the signup wizard will ask in **step 6** whether you want to start from a preset workflow (for example, a "GitHub Automation" template).

- **Do not pick the GitHub preset or any other right-hand preset.** It pre-populates a crew you did not design and locks you into someone else's choices.
- **Click the option on the left and leave the description blank.** This finishes the wizard and drops you on the empty dashboard at <https://app.crewai.com/crewai_plus/dashboard>, which is where this project starts.

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

1. From the dashboard, click **Crew Studio** in the left navigation.
2. In the "Build AI Powered Automations" prompt box at the center of the screen, paste a description of your workflow. Reference what your crew should do, what the inputs are, and which step should wait for human approval before finalizing. Then click the submit arrow.
3. The Studio editor opens with a four-step in-Studio tour ("Welcome to CrewAI Studio"). Click through or dismiss it.
4. The AI Copilot generates the crew live on the **Canvas** tab. The conversation panel on the left streams its thought process — read it; it tells you what tools the Copilot considered and why it kept the ones it did.

**Do not edit yet.** When the Copilot finishes, click the **Fit View** button in the bottom-left of the canvas controls so the whole crew is visible, then screenshot the canvas. This is your benchmark for Part 4.

### Step 2 — Align with Your Design

Review what the Copilot built against your Part 1 answers. Make adjustments so the crew matches your design:

- Confirm or change the **Process Type** dropdown (top-left of the canvas) to match your Part 1c choice — Sequential or Hierarchical.
- For each agent, click the pencil icon on the card to open the side panel. Under **Tools**, remove any tools that violate your Part 1b scoping decisions. Under **Agent Settings**, decide whether **Allow Delegation** should be on or off — this is itself a governance decision.
- Add or remove agents and tasks if what the Copilot generated does not match your Part 1a workflow. You can also drag a fresh **Task** or **Agent** from the right-side palette onto the canvas.

Screenshot the final canvas with the Process Type dropdown visible at the top-left.

### Step 3 — Make the Human Checkpoint a First-Class Step

This is where you discover what the no-code platform does and does not enforce — and the gap is itself part of the lesson.

**There is no "Human Input" toggle in the current CrewAI Studio visual editor.** In the cloud-hosted free tier, a task's settings panel exposes only: Name, Description, Expected Output, Async Execution, Markdown Output, Guardrail, and Response Format. None of these *forces* the crew to pause and wait for a real human.

The mechanism the platform actually gives you is design-by-description: you make the human checkpoint a **dedicated task** in the crew, owned by an approval-coordinator agent, whose Description tells the agent to wait for human confirmation and whose Expected Output requires evidence that approval happened. Do all three of the following:

1. **Confirm the dedicated checkpoint task exists.** If your Part 1d step is not already a separate task in the canvas, either ask the Copilot in chat to add it ("add a final task that waits for human approval before finalizing the memo") or drag a Task onto the canvas and wire it as the last step.
2. **Open that task's settings panel (pencil icon)** and verify the **Description** explicitly says the agent must wait for explicit human confirmation before proceeding. Edit it if it does not.
3. **In the same panel, set the Guardrail** to require the kind of approval evidence you said you would need in Part 1d. Example: `Output must include an "Approved by:" line with a non-empty approver name and an "Approval timestamp:" line.` A guardrail is not a real pause, but it is the strongest mechanical check this tier gives you.

Screenshot the task settings panel for that step with the Description, Expected Output, and Guardrail fields all visible.

> **Heads up — and this matters for Part 4:** in Part 3 you will run the crew. The "wait for human" instruction in the task Description is treated as a suggestion to the agent, not as a platform-enforced pause. The agent will almost certainly fabricate an approval and finalize the memo on its own. **That outcome is not a failure of your build — it is the central governance finding this project asks you to document.**

---

## Part 3 — Run the Crew and Read the Timeline

Run your crew once. Provide realistic test input — not placeholder text. A crew built to research a company should receive an actual company name, not "Company X."

**Free-tier limit reminder:** the 50 executions per month is shared across everything you do in your account. One careful, deliberate run is worth more than five rushed ones.

1. Click the **Run** icon (the blue play button in the top-right of the editor).
2. The **Run parameters** modal opens with one input field for every `{variable}` referenced anywhere in your tasks. Fill them in with realistic values — the right-side **Preview** panel shows your inputs substituted into the first task's description, so you can see what the agent will actually receive. Click **Execute**.
3. The view switches to the **Run** tab. The left panel is the **Timeline** (the per-run audit trail); the right panel is **Event details**.
4. Watch the run progress. The Timeline nests events: each Agent expands to its Task; each Task expands to Started → LLM calls (with durations) → tool calls (by tool name) → Tool Usage Finished → Completed.

After the run completes, click into individual events. The Event details panel has up to three tabs:

- **Details** — what the event was, when it happened, and the agent's response text
- **Messages** (LLM events only) — the system and user prompts that were sent to the model
- **Raw Data** — the underlying JSON for the event

For each agent, note in your submission:
- What input it received
- What output it produced
- Whether the handoff to the next agent looks correct

**On the human-checkpoint task specifically:** record exactly how long that task took, what the agent did in those seconds, and whether any real human ever entered anything. The expected observation is that the task completed in under a minute with no pause and no real human input. Save the agent's "approval" output verbatim — note specifically whether the approver is named, a placeholder ("[Your Name]"), or fabricated.

Screenshot the Timeline panel showing at least two agents' completed task entries.

> **Note on terminology:** the per-run view is the **Run tab Timeline** for the crew you are working on. The **Traces** link in the left navigation goes to "Trace Batches," a global list of every run across your account — the same data, organized for cross-run review rather than for the run you just executed.

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

Look at the run Timeline from Part 3. Answer these four questions in two to four sentences each:

- **What does the Timeline capture, and what is missing?** Could you reconstruct a problematic agent decision from the Timeline alone, or would you need something else?
- **The human-approval task — what does the Timeline say happened, and is that what should have happened?** Walk through the seconds between the task starting and completing. If no real human entered anything, the Timeline still records the task as "Completed." What does that mean for your trust in this audit trail?
- **Who in a real organization would need access to this log, and how often?** Daily, weekly, only after an incident? Why?
- **What is the longest period you would feel comfortable letting this crew run with no human reviewing the Timeline?** Be specific about the threshold beyond which review becomes mandatory — and say what about your specific crew drives that number.

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

**2. If this crew ran at your workplace and produced a wrong or harmful output, who would own the response — and what specifically would they need from the Run Timeline to investigate?**

Not "IT." Not "the person who built it." Name the actual function — operations, legal, a content owner, a specific team — and say what entry in the Timeline would tell them where the failure happened.

---

## Submission Requirements

Your submission is a single PDF or Word document uploaded to Blackboard. It must contain, in order:

1. **Part 1** — Workflow description, agent design table, orchestration pattern rationale, human checkpoint design (all four sections)
2. **Screenshot 1** — The AI Copilot's initial canvas output (Fit View, before your edits)
3. **Screenshot 2** — Your final canvas with the Process Type dropdown visible at the top-left
4. **Screenshot 3** — The settings panel for your human-checkpoint task, showing the Description, Expected Output, and Guardrail fields you configured
5. **Part 3** — Run notes: per-agent handoff observations AND your specific observations about whether the human-approval task actually paused for a real human
6. **Screenshot 4** — The Run tab Timeline showing at least two agents' completed task entries
7. **Part 4** — Full governance audit: design vs. reality, tool scope table, threat class table, audit trail evaluation (all four questions), top 3 risks + top 3 mitigations
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
