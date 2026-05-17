# Activity 3 — Will It Survive in the Wild?

**Format:** In-class activity — solo
**Time:** 12–15 minutes
**Requires:** A web browser · two free LLM accounts (the same two from Activity 2, or any other pair)

---

## Overview

The second way a shipped agent gets you fired: it breaks in the wild. It drifts, it gets exploited, the bill runs away, or it does something nobody planned for and no one knows how to freeze it.

This activity uses the same two-LLM pattern as the one before it, but the framework changes. You are drafting the *operations* plan for a deployed agent — what happens **after** it ships, not before. The critic will then attack it against the five things that kill live agents in production.

You can reuse the agent and organization from Activity 2 (most efficient — keep the same context, switch from "will they use it" to "will it survive") or pick a new one. Fresh chats either way.

---

## Step 1 — Fresh chats in both tabs (about 1 minute)

Use the same two browser tabs from Activity 2, but start a **new chat** in each one. Keep the same roles:

- **LLM #1 — the planner**
- **LLM #2 — the critic**

---

## Step 2 — Set up your context and build the plan with LLM #1 (about 4–5 minutes)

In LLM #1, paste this prompt and fill in the three blanks before sending:

> I'm drafting the operations plan for an AI agent that has already been built — what happens AFTER we ship it, not before. Help me think it through.
>
> My context:
> — My area of study or interest: **[fill in]**
> — An organization I know (or the same one from Activity 2): **[fill in]**
> — The agent's job, in one sentence: **[fill in]**
>
> **Step 1.** Once you understand the agent, help me draft a five-sentence operations plan covering: (1) what we'll monitor and who actually looks at the dashboard, (2) the cost controls — monthly budget with a named owner, per-run cap, circuit breaker, (3) how we version the prompts and tools so we can roll back when something breaks, (4) what access and permissions the agent has — and what's off-limits, (5) the incident plan — who gets paged when something goes wrong, and how we freeze the agent.
>
> Ask me follow-up questions if I'm being vague. Push me to name actual roles, numbers, and limits — no platitudes.

Iterate with the planner for two or three turns. The planner's job is to push you off generic language. *"We'll monitor things"* is not a plan. *"The Claims operations lead reviews the executions dashboard every Monday and alerts on tool-failure rate above 5%"* is.

When you have a five-sentence plan you actually believe in, copy it.

---

## Step 3 — Move to LLM #2, the critic (about 1 minute)

Open the second tab. Start a *fresh* chat. Paste this prompt — including your five-sentence plan in the spot indicated:

> You are a harsh but constructive critic of AI agent operations plans. Your only job is to find the place this agent will most likely break, drift, or get exploited after launch.
>
> Here's the operations plan I drafted:
>
> **[paste your five-sentence plan]**
>
> Critique it against this framework — the **five production killers** that take down live agents in the wild:
>
> 1. **Drifted in silence** — nobody monitored after launch; the agent slowly got worse and the first sign was an angry user
> 2. **Cost ran away** — no budget owner, no per-run cap, no circuit breaker; one bad weekend produced a five-figure bill
> 3. **No rollback** — when a prompt change broke something, there was no version to go back to
> 4. **Over-permissioned** — the agent had access to more than it needed, so one prompt injection or bug had a huge blast radius
> 5. **No incident plan** — when something went wrong, nobody knew who got paged, how to freeze the agent, or whether to notify users
>
> Tell me three things:
> — Which **one** killer is most likely to bite this specific plan
> — The exact sentence (or missing sentence) in my plan that gives it away
> — The single change that would defuse it
>
> **Do not stop there.** Wait for my response. I will push back, ask a follow-up, or revise the plan. Keep the critique alive across three or four turns until I land somewhere you can't easily break.

---

## Step 4 — Iterate with the critic (about 5–6 minutes)

Three or four turns. Same rule as before:

> Do not defend the plan. Pressure-test it.

The **over-permissioned** killer is the one most likely to surface — most plans hand-wave permissions in the planner phase. If that is yours, do not skip past it. That is exactly where the security material from Module 8 meets the operations material from Module 10: the blast radius of a single bad prompt or compromised account is set by the permissions you decided to grant.

Stop when the critic can no longer easily break the plan — or when 15 minutes is up.

---

## Coming Back to Class

Keep both tabs open. Be ready to share aloud:

- The agent's job in one sentence
- The production killer that landed on you
- One concrete change to the operations plan that you would actually make tomorrow

---

## Why This Matters

Most agent projects end at "we launched it." Nobody decided what *still working* looks like, nobody named who gets paged when it breaks, and nobody scoped the agent's permissions tight enough to survive a single bad day. You just walked a plan through the five most common ways live agents die — and the cheapest mistake is usually the most dangerous one. The discipline you practiced here is what an AgentOps mindset feels like in your hands.

---

*Activity for Module 10 — ISYS 398U Agentic AI Implementation | University of Richmond SPCS*
