# Activity: Pattern Spotter

## Overview

Every real-world AI agent runs on one or more design patterns under the hood. Some agents reflect on their own output and revise it. Some reach out and use tools. Some break big goals into tracked sub-plans. Some hand off to specialist agents.

Vendors rarely tell you which pattern their product uses. This activity trains you to spot them yourself — in real marketing copy, real product descriptions, and real use cases — so you can evaluate what you're actually buying or building.

---

## Goals

- Recognize the four core agent design patterns (Reflection, Tool Use, Planning, Multi-Agent) in real-world descriptions
- Distinguish between single-pattern agents and compound agents that combine multiple patterns
- Develop vocabulary to describe and evaluate agent architectures clearly

---

## The Four Patterns — Quick Reference

Before you start, internalize these:

| Pattern | What it means in plain English |
|---------|-------------------------------|
| **Reflection** | Agent generates output, then critiques its own output and revises before handing it back |
| **Tool Use** | Agent calls an external system (API, database, calendar, browser) to get or act on real data |
| **Planning** | Agent decomposes a big goal into tracked sub-tasks and executes them in sequence or parallel |
| **Multi-Agent** | One agent delegates to another specialized agent; each optimized for a different sub-problem |

---

## Step 1: Identify the Patterns

Read each description below. For each one:
- Name **every pattern** you can identify (there may be more than one)
- Write one sentence explaining **what specific behavior** told you which pattern it was
- Note if the description is **ambiguous** — if you genuinely can't tell, say why

---

**Scenario A**
> "Our AI reviews every customer email before sending it to support staff. It drafts a proposed response, scores its own confidence, and rewrites sections where confidence is below 85% before the draft appears in the agent's queue."

*Patterns:* _______________  
*Evidence:* _______________

---

**Scenario B**
> "When a sales rep asks for a competitor analysis, the system queries our CRM for recent deal losses, pulls the competitor's latest pricing page, and cross-references against our own product catalog before generating a response."

*Patterns:* _______________  
*Evidence:* _______________

---

**Scenario C**
> "To onboard a new employee, the system creates a 14-step task list, assigns due dates to each item, and tracks completion — automatically triggering IT provisioning, HR paperwork, and facilities access requests in parallel."

*Patterns:* _______________  
*Evidence:* _______________

---

**Scenario D**
> "Complex support tickets are routed to a triage agent that classifies severity and intent, then passed to either a billing specialist agent, a technical agent, or an escalation agent depending on the classification."

*Patterns:* _______________  
*Evidence:* _______________

---

**Scenario E**
> "Our research assistant receives a question, searches three databases, drafts a synthesis, checks its own draft for unsupported claims, removes or flags them, and sends the final output to the user — without any human review."

*Patterns:* _______________  
*Evidence:* _______________

---

## Step 2: Your Own Example

Think of one AI product you've seen, heard about, or used — at work, in the news, or in a vendor pitch.

Describe what it does in 2–3 sentences, then name the pattern(s) at work. If you can't tell from the description what pattern it uses, write that too — *"I can't tell because the vendor doesn't disclose how it reasons."*

---

## Reflection Questions

1. Which pattern is the easiest to identify in a marketing description? Which is the hardest to spot — and why might a vendor want to obscure it?

2. Scenario E combines multiple patterns. Why does that make it harder to evaluate, audit, or debug?

3. You're evaluating a vendor pitch for an agent that will handle sensitive HR requests. The vendor says "our AI reviews and improves its own answers before you see them." What follow-up question do you ask to understand whether that reflection is real or just a longer response time?

---

## Why This Matters

Pattern literacy is how you move from being a consumer of AI marketing to being an evaluator of AI architecture. The question isn't whether a vendor's agent "uses AI" — it's which patterns it runs, how they're chained, and which failure modes come with each.
