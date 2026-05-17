# Activity 2 — Will Anyone Actually Use It?

**Format:** In-class activity — solo
**Time:** 12–15 minutes
**Requires:** A web browser · two free LLM accounts (any pair — for example, Claude + ChatGPT, or ChatGPT + Gemini)

---

## Overview

In Module 10 you heard that a shipped agent can fail two very different ways — nobody adopts it, or it breaks in the wild. This activity is about the *adoption* side: a working agent that gives fine answers and still gets abandoned.

You will draft a rollout plan for an agent at an organization you actually know, with one LLM helping you build it. Then you will hand that plan to a *different* LLM and let it find the place your plan is most likely to die. The conversation with the critic is iterative — three or four turns, not one shot. You are not defending your plan; you are pressure-testing it.

---

## Why two different LLMs

The planner does not know what framework the critic will use, so it will help you build something that looks fine on its face. Most rollout plans look fine to the person who wrote them — they only look fragile to someone applying an outside framework. The second model is that outside framework.

Using two *different* products (different accounts, not two tabs of the same model) is the felt experience of "this other system found something my first one missed." That cross-model second-opinion pattern is a fluency move worth practicing — it works on more than rollout plans.

---

## Step 1 — Open two tabs (about 1 minute)

Open two browser tabs in two *different* free LLM products. Suggested pairings:

- **Claude** (claude.ai) + **ChatGPT** (chatgpt.com)
- **ChatGPT** + **Google Gemini** (gemini.google.com)
- Any other combination, as long as the two tabs are different products.

Pick one tab to be **LLM #1 — the planner.** The other will be **LLM #2 — the critic.**

---

## Step 2 — Set up your context and build the plan with LLM #1 (about 4–5 minutes)

In LLM #1, paste this prompt and fill in the three blanks before sending:

> I'm sketching the rollout plan for an AI agent. Help me think it through.
>
> My context:
> — My area of study or interest: **[fill in]**
> — An organization I know well — workplace, internship, prior employer, volunteer org, campus department: **[fill in]**
> — The kind of work that happens there, in one sentence: **[fill in]**
>
> **Step 1.** Propose one realistic workflow at that organization where an AI agent could plausibly do part — not all — of the work. Pick a specific task done repeatedly, not a vague category.
>
> **Step 2.** Once we agree on the workflow, help me draft a five-sentence rollout plan covering: (1) the workflow and who the users are, (2) who owns adoption — a named role, (3) the one north-star metric that says it's working, (4) how the users will be trained, (5) how we'll handle concerns from staff who fear being replaced.
>
> Ask me follow-up questions if my context is too thin. Don't write the whole plan in one shot — push me to make real choices.

Iterate with the planner for two or three turns. Do not accept the first draft. Make it specific — real role names, a real metric, a training approach that fits adult learners at that organization.

When you have a five-sentence plan you actually believe in, copy it.

---

## Step 3 — Move to LLM #2, the critic (about 1 minute)

Open the second tab. Start a *fresh* chat. Paste this prompt — including your five-sentence plan in the spot indicated:

> You are a harsh but constructive critic of AI agent rollout plans. Your only job is to find the place this plan will most likely fail.
>
> Here's the rollout plan I drafted:
>
> **[paste your five-sentence plan]**
>
> Critique it against this framework — the **five adoption killers** that cause working agents to die in real organizations:
>
> 1. **No owner** — nobody is accountable for keeping the content or system fresh
> 2. **No success metric** — nothing is falsifiable; the sponsor loses patience
> 3. **Training was a link** — adults didn't get practice, just a video they skimmed
> 4. **Fear unmanaged** — rumors won because nobody addressed them honestly
> 5. **Shadow workarounds** — the official tool is slower than the workaround, so people route around it
>
> Tell me three things:
> — Which **one** killer is most likely to bite this specific plan
> — The exact sentence (or missing sentence) in my plan that gives it away
> — The single change that would defuse it
>
> **Do not stop there.** Wait for my response. I will push back, ask a follow-up, or revise the plan. Keep the critique alive across three or four turns until I land somewhere you can't easily break.

---

## Step 4 — Iterate with the critic (about 5–6 minutes)

Three or four turns. The most important rule:

> Do not defend the plan. Pressure-test it.

Your instinct will be to argue *against* the critic. The activity is more valuable when you argue *with* the critic — testing each objection. If the critic names a weakness you disagree with, ask "why specifically?" If you agree, revise one sentence and ask the critic to look at the new version.

Stop when the critic can no longer easily break the plan — or when 15 minutes is up, whichever comes first.

---

## Coming Back to Class

Keep both tabs open. Be ready to share aloud:

- One sentence of context — your area of study or interest, and the organization
- The single adoption killer the critic landed on
- One specific change you made to the plan — or one place you refused to change it, and why

---

## Why This Matters

You did not just learn the five adoption killers — you watched one of them surface in a plan you had just built and were ready to defend. That is the gap between *knowing* the framework and *seeing* it in your own thinking, which is the gap every rollout has to close. The cross-model pattern — build in one, critique in another — is one of the most useful fluency moves in this course, and you can re-use it any time you need a second opinion on your own work.

---

*Activity for Module 10 — ISYS 398U Agentic AI Implementation | University of Richmond SPCS*
