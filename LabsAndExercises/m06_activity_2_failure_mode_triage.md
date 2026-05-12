# Activity 2 — Failure Mode Triage: What Kind of Broken Is This?

**Requires:** No tools — pen, paper, and the three-category framework from Module 6

---

## Overview

A browser agent failed. That sentence is not enough information to fix anything.

The module introduced a three-category framework for diagnosing agent failures: **setup failures** (bad instructions, missing tools, wrong access), **model failures** (incorrect reasoning, hallucination, wrong model tier for the task), and **production failures** (the environment changed — the website updated, the CAPTCHA appeared, the session timed out).

Each category points to a different fix and a different person who owns the repair. If you misclassify the failure, you send the work to the wrong team and the problem stays broken.

This activity gives you four scenarios. Three have a clear answer. One is genuinely ambiguous — there is no single correct classification, and the point is to notice why it's hard to call and what you would do to find out.

---

## Goals

- Apply the three-category failure framework to realistic browser agent scenarios
- Distinguish between failures that point to the prompt, the model, and the infrastructure
- Recognize when a failure is ambiguous and identify how you would triage it in practice
- Connect the failure type to the person or team who owns the fix

---

## The Framework — Quick Reference

| Failure type | What went wrong | Who fixes it |
|-------------|----------------|-------------|
| **Setup failure** | The agent had bad instructions, was missing a tool, lacked access to something it needed, or was told to look for something that doesn't exist in the actual environment | Prompt engineer / workflow designer — fix the instructions or the configuration |
| **Model failure** | The agent had everything it needed but reasoned incorrectly, hallucinated a field or fact, applied criteria in the wrong order, or chose a path a well-configured model shouldn't have taken | Model tier decision or prompt revision — add a verification step, upgrade the model, or add a worked example to the prompt |
| **Production failure** | The agent and its instructions were fine, but something in the external environment changed — a website update, a CAPTCHA, a rate limit, a session timeout, a moved button | Infrastructure / monitoring team — update selectors, add monitoring, coordinate with vendors on change notifications |

---

## The Scenarios

Read each scenario carefully before classifying it. For each one, fill out the triage worksheet below the scenario.

---

### Scenario A — The Expense Portal

An accounts payable team at a mid-sized company deploys a browser agent to process employee expense reports through their finance portal. The agent is configured to read each submission and verify that the "Cost Center" field is filled in before flagging the report as ready for approval.

On day one, the agent fails on every single report. The error log shows: *"Field 'Cost Center' not found on page."* A human team member logs in manually, looks at the form, and immediately spots the issue: the field exists, but it is labeled **"Department Code"** in the portal — not "Cost Center." The agent's instructions used the company's internal accounting term, which doesn't match what the vendor actually put on the screen.

---

**Triage worksheet — Scenario A**

| Question | Your answer |
|----------|------------|
| What failure type is this? (Setup / Model / Production) | |
| In one sentence: what specifically went wrong? | |
| Who fixes it? | |
| What is the fix? | |
| Could this have been caught before deployment? How? | |

---

### Scenario B — The Claims Reviewer

An insurance company deploys a browser agent to pre-screen incoming claims and flag which ones qualify for expedited review. The qualification criteria are documented in the company's policy guide: a claim qualifies if it meets **at least two** of four criteria — high dollar amount, vulnerable claimant, prior claim history, or emergency category.

After three weeks, a compliance auditor notices the agent is flagging claims for expedited review at nearly twice the expected rate. A sample review reveals the agent is correctly reading the criteria and correctly reading each claim's data. The error is in the reasoning: the agent is treating the criteria as **any one of four** rather than **at least two of four**. It has been approving single-criterion claims all along.

The model is the same fast/small tier that handles routing and classification tasks elsewhere in the company's stack.

---

**Triage worksheet — Scenario B**

| Question | Your answer |
|----------|------------|
| What failure type is this? (Setup / Model / Production) | |
| In one sentence: what specifically went wrong? | |
| Who fixes it? | |
| What is the fix? | |
| What made this failure hard to catch — why did it take three weeks? | |

---

### Scenario C — The Vendor Portal

A procurement team has been using a browser agent to retrieve invoice status updates from a vendor's web portal every morning. The agent logs in, navigates to the invoice status page, and exports a summary. It has run reliably for six weeks.

On Monday morning, every run fails. The agent reports: *"Login button not found."* Nothing in the agent's configuration changed over the weekend. The IT team checks the logs and confirms no updates were deployed to the agent or its infrastructure.

On Friday afternoon, the vendor had sent an automated email announcing a scheduled maintenance window and a "refreshed user interface launching Monday." The procurement team's inbox flagged the email as a newsletter and it was never read.

---

**Triage worksheet — Scenario C**

| Question | Your answer |
|----------|------------|
| What failure type is this? (Setup / Model / Production) | |
| In one sentence: what specifically went wrong? | |
| Who fixes it? | |
| What is the fix? | |
| What process failure contributed to this — beyond the agent itself? | |

---

### Scenario D — The Application Tracker *(Ambiguous — no single correct answer)*

A recruiting team deploys a browser agent to help with high-volume job application intake. The agent reads candidate profiles from an internal database, then fills out application forms on partner company portals on the candidates' behalf (with the candidates' consent).

After two weeks, the team notices the agent is consistently leaving the **"Years of experience in a leadership role"** field blank on every form — even for candidates whose profiles clearly state things like "managed a team of 8 for three years" or "led cross-functional initiative across four departments."

The field is clearly visible on the form. The agent is not throwing an error — it is simply not filling it in. Everything else on the form is filled in accurately.

---

**Triage worksheet — Scenario D**

| Question | Your answer |
|----------|------------|
| What failure type does this *look like* at first? | |
| What is an argument that it's a **setup failure**? | |
| What is an argument that it's a **model failure**? | |
| How would you test to find out which it actually is? (Describe one specific test.) | |
| If you had to make a call right now without further testing, which type would you classify it as — and why? | |

---

## Deliverable

Submit all four completed triage worksheets.

---

## Reflection Questions

Answer these after completing all four scenarios:

1. Scenario B's agent had access to the correct criteria and the correct data — and still got the wrong answer. What does that tell you about when it is and isn't appropriate to use a fast/small model for an agent task?

2. Scenario C's failure was triggered by something completely outside the agent's control. What monitoring practice would have caught this failure before the team noticed it on Monday morning?

3. Scenario D is designed to be genuinely ambiguous. In a real organization, who would you pull into a ten-minute conversation to figure out whether it's a setup or model failure — and what would you ask them?

4. Looking at all four scenarios: which failure type do you think would be the most expensive to leave undetected for a week? Make an argument for your answer.

---

## Why This Matters

When a browser agent breaks in production, the first thing someone is going to say is "the AI is broken." That is not a fix. It is a description of a symptom.

The triage framework you practiced in this activity is what turns that symptom into an action. A setup failure means someone reviews the configuration. A model failure means someone reviews the model tier and the prompt. A production failure means someone calls the vendor or updates the selectors. Each answer involves different people, different timelines, and different costs.

The worst outcome is misclassifying the failure — telling the infrastructure team to fix something that's actually a prompt problem, or telling the prompt engineer to revise instructions when the website just moved a button. That wastes time, delays resolution, and erodes trust in the agent and the team running it.

You are the person in the room who knows the difference. Use it.
