# Activity: Build Your First Crew in CrewAI Studio

**Format:** Solo, async-safe (works on your own schedule)
**Effort scope:** Roughly 30 minutes — longer if you choose to iterate on your crew
**Requires:** A web browser · Free CrewAI account (created during Step 1) · No credit card

---

## Overview

In the lesson you saw five orchestration patterns on paper. In this activity you build one in software — using **CrewAI Studio**, the no-code visual editor on **CrewAI AMP** (their cloud platform).

The interesting thing about CrewAI Studio for our purposes is not the framework code underneath — most working professionals will never write a line of it. The interesting thing is that the platform **renders two of the five patterns from the lesson as real software:**

- **Sequential process** = the **Pipeline** pattern from the lesson
- **Hierarchical process** = the **Orchestrator-Worker** pattern from the lesson

You will use the AI Copilot to generate a crew from a natural-language description, see which pattern it picked, inspect the result, switch patterns to see the difference, run it once, and observe what the execution timeline shows you.

The goal is **pattern recognition in a real tool**, not mastery of CrewAI.

---

## Goals

- Stand up a working multi-agent crew using CrewAI Studio's AI Copilot
- Identify which orchestration pattern the platform chose by default
- Map CrewAI's process types (Sequential, Hierarchical) onto the lesson patterns
- Read the execution timeline as an audit trail
- Make one deliberate modification and observe what changes

---

## Step 1 — Create a Free CrewAI Account (3 min)

1. Go to [app.crewai.com](https://app.crewai.com).
2. Click **Sign up** (or **Start free**). Sign up with email or Google.
3. The free tier includes **50 executions per month**, **1 deployed crew**, and **1 seat** — no credit card required. That is plenty for this activity.
4. After signup you will land in the CrewAI AMP dashboard.

> **If signup asks for a phone number or organization:** put in your real info — it stays on the free plan unless you click **Upgrade**.

---

## Step 2 — Open Crew Studio (1 min)

1. From the dashboard, find **Crew Studio** in the left navigation. (It may also appear as **Build a Crew** or under a **+ New** menu — the label moves occasionally as the product evolves.)
2. You should see two main panes: a **prompt input** on the left or top, and a **blank canvas** in the center.

If you cannot find Crew Studio, search the in-app help for "Crew Studio" or check **Settings → Features** to make sure it is enabled.

---

## Step 3 — Pick a Scenario (2 min)

You will describe the crew you want in plain English. The AI Copilot does the rest.

**Pick one scenario** — use one of the three below, or write your own based on a workflow you actually know.

> **Option A — Deal desk** *(matches the lesson's worked example)*
> Build a crew that, given a request for proposal from a prospect company, does three things: researches the prospect and their industry, drafts a tailored proposal document, and produces a one-paragraph executive summary for the salesperson to review.

> **Option B — Internal research request**
> Build a crew that, given a question from a colleague about a public company or a public topic, gathers three sources, summarizes the findings, and produces a short memo with citations and an "open questions" section.

> **Option C — Onboarding documentation**
> Build a crew that, given a role title and a department name, generates a first-day checklist for a new hire — including a learning resources list, a list of people they should meet in their first week, and a one-page welcome document.

> **Option D — Your own scenario**
> Pick a recurring multi-step task you actually know — from work, a club, a school project, a volunteer org. Write it as one to three sentences describing what should happen end-to-end.

**What makes a good prompt:** name the inputs the crew will receive, name the outputs you want, and name two or three intermediate steps you want done. Keep it under 100 words.

---

## Step 4 — Let the AI Copilot Build Your Crew (5–7 min)

1. Paste your scenario into the **prompt input**.
2. Hit **Generate** (or **Build**, depending on the current label).
3. Watch the **AI Thoughts** panel stream the reasoning — this is the Copilot deciding what agents to create, what tasks to assign, and what tools they need.
4. Watch the **canvas** populate. You should see:
   - **Agents** appear as labeled nodes
   - **Tasks** appear as connected nodes between agents
   - **Tools** appear as small icons attached to agents

**Do not edit yet.** Just observe what the AI Copilot produced.

> **If the AI Copilot takes more than two or three minutes:** it is probably stuck. Refresh, simplify your prompt, and try again. The platform's free-tier compute can be slow at peak hours.

---

## Step 5 — Inspect What the Copilot Built (5 min)

Click around on the canvas and look at the settings panels.

Answer these questions in your notes:

1. **Which process did it pick?** Look at the crew's top-level settings — there should be a **Process** field. It will be either **Sequential** or **Hierarchical.**
   - **Sequential** = the **Pipeline** pattern from the lesson — each agent runs in order, the next one starts when the previous finishes
   - **Hierarchical** = the **Orchestrator-Worker** pattern from the lesson — a manager agent routes tasks to workers
2. **What roles did it assign?** Each agent has a **role**, a **goal**, and a **backstory**. Read all three for at least two agents.
3. **What tools did it attach?** Click on each agent and look at its tool list. Did it attach a search tool, a writing tool, anything that talks to an external system?
4. **What does each task expect as input and output?** Click on a task node. The **description** is what the agent is being asked to do; the **expected output** is the handoff contract — what the next agent will receive.

---

## Step 6 — Switch the Process Type, See What Changes (3 min)

This is the most useful pedagogical move of the activity.

1. In the crew's settings, find the **Process** field and **switch it to the other option** — Sequential to Hierarchical, or vice versa.
2. Save the change. The canvas should reorganize:
   - **Sequential** lays the agents out as a left-to-right chain
   - **Hierarchical** introduces a **manager** agent at the top that routes work to the others

You just rendered two of the five lesson patterns side by side, in the same crew, in about ten seconds. **Look at the difference.** That's the architectural decision the lesson said to make on paper — visualized in software.

> **Pick which version you want to run.** Either is fine. Note in your reflection why you picked the one you did.

---

## Step 7 — Run It and Read the Execution Timeline (5 min)

1. Switch to the **Execution** view (it usually appears as a tab or a sidebar item near the top of the canvas).
2. Click **Run** (or **Test**). Provide any inputs the crew expects.
3. Watch the **event timeline** populate as each agent works:
   - Each event shows which agent fired
   - The **Details / Messages / Raw Data** tabs show what each agent received and what it produced
4. When the run finishes, scroll through the timeline.

**Look specifically at the handoffs** — the moments where one agent's output becomes the next agent's input. That is the **handoff contract** in action.

> **Free-tier limit reminder:** the 50 executions per month is per account. One run of a small crew typically counts as one execution. Don't repeatedly rerun "to see what happens" — you'll burn through your quota fast.

---

## Step 8 — Take Screenshots and Reflect (3 min)

Take **two screenshots:**

1. The **canvas** showing your crew (with the process type visible in the settings, if possible)
2. The **execution timeline** showing at least one agent's output

Then answer the **four reflection questions** below.

---

## Deliverable

- **Two screenshots** (canvas + execution timeline)
- **One note** stating which scenario you chose (A, B, C, or your own) and which process the AI Copilot picked first
- **Written answers** to all four reflection questions

---

## Reflection Questions

**1. Which orchestration pattern did CrewAI choose first — Sequential (Pipeline) or Hierarchical (Orchestrator-Worker)? Why might it have picked that one?**
Look at the scenario you wrote. Were the steps strictly dependent on each other (Pipeline territory), or was there branching judgment about which specialist to use (Orchestrator-Worker territory)? Does CrewAI's choice match what you would have picked?

**2. Look at the handoffs between tasks. Are agents passing structured data, or natural-language descriptions?**
The lesson made the case for a JSON schema as the handoff contract. What does CrewAI Studio actually pass between agents? What would happen if a downstream agent received an upstream output that was missing a key piece of information — for example, in the deal-desk scenario, what if the research agent forgot the prospect's industry?

**3. Where would a human-in-the-loop checkpoint belong in this crew?**
Pick a specific step in your crew. State (a) where you would add an approval gate, (b) what the approver would need to see in the approval packet (five fields, no more — see the lesson), and (c) whether the action that follows is reversible or not.

**4. Which of the six multi-agent failure modes is this crew most exposed to — and what would you do about it?**
The lesson named six failure modes: cascading hallucinations, handoff loops, cost explosion, dropped tasks, duplicate actions, schema drift. Pick the one that worries you most about *this specific crew you just built*, explain why, and name one concrete mitigation you would add before deploying it.

---

## Common Pitfalls and Workarounds

| Problem | Workaround |
|---|---|
| The AI Copilot is slow or hangs | Refresh; simplify your prompt; try again at a less-busy time |
| You can't find the Process toggle | Look in the crew's main settings, not the individual agent settings; it may also be labeled **Crew Type** or **Workflow Type** depending on platform version |
| Your run uses too many tokens | Make your test input small — one short paragraph, not a full document |
| Tools you expected aren't attached | The AI Copilot only attaches tools it thinks the crew needs; you can manually drag more from the Resources panel |
| The crew "ran" but produced gibberish | Read the execution timeline backward from the failure point; usually one agent got an input it couldn't parse — that's a schema-drift failure in the wild |

---

## Why This Matters

What you just built is **the same architectural shape** that enterprises pay platforms like Salesforce Agentforce, Moveworks, Cognigy, or Automation Anywhere tens of thousands of dollars per year for.

The tools are different. The price tag is different. The patterns are identical.

Every multi-agent system you encounter at work for the rest of your career will be a variation of what you just generated, inspected, and ran in about thirty minutes. Knowing how to **read** one of these systems — what process it's using, what the handoffs are, where HITL belongs, which failure modes it's exposed to — is the durable skill. The specific platform is the disposable detail.

---

## Quick Reference — CrewAI Studio Concepts Mapped to the Lesson

| CrewAI Studio term | Lesson concept |
|---|---|
| **Crew** | The multi-agent system as a whole |
| **Agent** (with role, goal, backstory) | A specialist node in the workflow |
| **Task** (with description and expected output) | The handoff contract — what's required of each agent |
| **Process: Sequential** | The Pipeline pattern |
| **Process: Hierarchical** | The Orchestrator-Worker pattern (with a manager agent at the top) |
| **Tools** | MCP-style external capabilities the agent can call (Module 5 territory) |
| **Execution timeline** | The audit trail — Module 8's "what was accessed, what was changed, who approved" |
| **AI Copilot** | The natural-language prompt-to-canvas generator — the platform's distinguishing feature |
| **Free tier (50 executions/month)** | Module 6 cost realism in action — multi-agent runs are not free |

---

## What This Maps to in the Lesson

- **Section 3 (Five Orchestration Patterns)** — you just rendered two of them in software
- **Section 4 (Orchestrator-Worker Deep Dive)** — the Hierarchical process is exactly this pattern; if you switched processes in Step 6, you saw a manager agent appear
- **Section 5 (Choosing a Framework)** — you just used one of the five frameworks named in the lesson (CrewAI), specifically its commercial AMP / Studio offering
- **Section 6 (Handoff Contract)** — every task's "expected output" is a handoff contract; reflection question 2 asks you to assess whether it's strong enough
- **Section 8 (What Goes Wrong)** — reflection question 4 asks which of the six failure modes this crew is most exposed to
- **Section 9 (Cost Honesty)** — the 50-executions-per-month free-tier ceiling is the lesson's "5 to 20× the bill" realism made personal

---

## If You Want to Go Further (Optional, Not Required)

- **Try the Marketplace.** CrewAI Studio has a **Marketplace** of pre-built crews — browse it and find one that maps to a workflow you know. Note which process it uses and what tools it expects.
- **Look at the Traces feature.** Once you've run a crew, the **Traces** panel shows the detailed reasoning at each step — this is the same observability layer Module 3 (evals) and Module 8 (audit trails) said you need.
- **Compare to your Module 5 n8n build.** Both n8n and CrewAI Studio implement the same orchestration patterns, with different defaults and a different mental model. Working professionals will encounter both. Knowing the differences is procurement-literacy.

---

## Sources

- [Crew Studio documentation](https://docs.crewai.com/en/enterprise/features/crew-studio)
- [CrewAI Cookbooks](https://docs.crewai.com/en/examples/cookbooks)
- [CrewAI pricing](https://crewai.com/pricing)
- [CrewAI AMP signup](https://app.crewai.com)
