# Activity: Agent Decision Framework — Should This Task Be Delegated?

**Module 5 | Estimated time: 10–12 minutes | Solo activity**

---

## What This Activity Is About

Not every task should be handed to an AI agent. Knowing when to delegate — and when not to — is one of the most practical skills in agentic AI work. It's also one that separates thoughtful implementers from people who automate things they shouldn't.

In this activity, you'll apply a structured decision framework to five real-world scenarios. For each one, you'll assess whether the task is a good candidate for AI delegation, and why.

---

## Learning Objectives

By the end of this activity, you will be able to:

- Apply a four-criteria framework to evaluate whether a task is safe to delegate to an AI agent
- Identify the factors that increase or decrease the risk of AI-assisted task execution
- Use the verification cost test to sharpen your delegation recommendations

---

## Materials Needed

- This document
- Something to write in (a document, spreadsheet, notes app — anything works)
- No AI tool required for this activity, though you're welcome to use one to think through your reasoning

---

## The Decision Framework

Use these four criteria to evaluate any proposed AI delegation:

| Criterion | What to ask |
|---|---|
| **Ambiguity** | Does this task require judgment calls, or is it rule-based? High ambiguity means the AI has to guess at intent — that's a risk. |
| **Mistake cost** | If the AI gets it wrong, what happens? Is it reversible? Embarrassing? Costly? Irreversible? |
| **AI capability** | Does current AI actually have the skills for this task under real conditions — not ideal ones? |
| **Mistake rate** | How often would an AI realistically get this wrong? Once a week? Once a month? Once ever? |

**Also apply the verification cost test:**

> Is checking the AI's output cheaper — in time and attention — than doing the task yourself?

If checking the work is nearly as hard as doing the work, delegation doesn't save much. If checking is fast and errors are obvious, delegation makes more sense.

**Your recommendation should be one of:**

- **Delegate** — the task is a good candidate for full AI handling
- **Review carefully** — delegate with a mandatory human review step before any output is acted on
- **Do not delegate** — the risk, ambiguity, or AI capability gap makes this too dangerous right now

---

## The Five Scenarios

Read each scenario and fill in one row of the decision table below.

**Scenario 1:** "Summarize 40 customer support transcripts and identify the top 5 complaint categories."

**Scenario 2:** "Review incoming job applications and flag candidates who meet minimum qualifications."

**Scenario 3:** "Draft responses to routine vendor invoice disputes under $500."

**Scenario 4:** "Automatically renew software licenses for tools with fewer than 5 active users."

**Scenario 5:** "Generate a first draft of the quarterly board report from our internal dashboards."

---

## Decision Table

Copy this table into your notes and fill in one row per scenario. Your entries don't need to be long — a phrase or sentence per cell is enough.

| Scenario | Ambiguity level (Low / Med / High) | Mistake cost (Low / Med / High — and why) | AI capable? (Yes / Partial / No) | Verification cost (Low / Med / High) | Recommendation |
|---|---|---|---|---|---|
| 1 — Summarize transcripts | | | | | |
| 2 — Flag job applications | | | | | |
| 3 — Draft invoice dispute responses | | | | | |
| 4 — Auto-renew software licenses | | | | | |
| 5 — Draft board report | | | | | |

---

## Worked Example

Here is a completed row for **Scenario 1** to show you what level of analysis is expected.

**Scenario 1:** "Summarize 40 customer support transcripts and identify the top 5 complaint categories."

| Criterion | Assessment |
|---|---|
| **Ambiguity** | Low-to-medium. The task has a clear structure: read transcripts, group themes, rank by frequency. The main judgment call is how to define category boundaries — a reasonable AI can handle this. |
| **Mistake cost** | Low. If the AI misclassifies some complaints or misses a category, a human reviewer can catch it before any decision is made. The output is informational, not actionable on its own. |
| **AI capable?** | Yes. Summarization and categorization of text is one of the strongest current AI capabilities. |
| **Verification cost** | Low. A manager can skim the summary and categories in 5 minutes and spot anything obviously wrong. |
| **Recommendation** | **Review carefully.** This is a good delegation candidate — but a human should spot-check the categories against a few source transcripts before the summary is shared with leadership. |

---

## What to Do With Your Table

Hold on to your completed table. You may be asked to share one or two of your assessments during class discussion or submit the table as part of a module check-in.

If you want to go further: think about a task from your own work, internship, organization, or a company you know. Run it through the same framework and add it as a sixth row.

---

*Activity for Module 5 — ISYS 398U Agentic AI Implementation | University of Richmond SPCS*
