# Capstone Project — Bring Your Own Agent

**Worth:** 20% of final grade
**Written brief due:** The night before Demo Day, per the course LMS
**Presented:** Module 12 — Demo Day (live)
**Platform required:** Your choice — any agentic AI tool that was *not* used or demonstrated in this course. Free tier or paid are both allowed.
**Submission:** One PDF or Word document (the written brief) uploaded to GitHub, plus a live 5–6 minute presentation with a working demo at Demo Day.

---

## Overview

For the whole course, you have been building agents on tools your instructor chose. The capstone flips that.

You will go out into the agentic AI landscape — which is enormous and changing almost weekly — find a tool this class has *not* touched, build something real with it that matters to your own field, and show the class something none of us have seen before. Then you will explain it through the lens of what this course taught you.

There are two deliverables. The **presentation** is what you show. The **written brief** is where the deeper thinking lives — the security considerations, the evaluation plan, the business case — the analysis there is no time to say out loud in five minutes.

This is the capstone, and it is deliberately open. There is no template to fill in. The discipline comes from the four required concept ties and the rubric — not from a fixed structure.

---

## What "a tool we haven't seen" means

The tool you choose must be one this course did **not** use or demonstrate. The point of the capstone is genuine discovery — both for you and for the class watching your demo.

- **"New" applies to the tool itself, not just your use of it.** Building a clever new workflow on a platform we already used does not qualify.
- **The tool must be genuinely agentic** — something that can take actions, use other tools, follow multi-step goals, or operate with some autonomy. A plain chatbot or a one-shot content generator does not count. If you are not sure whether a tool qualifies as agentic, that is a good question for class hours.
- **Free tier or paid are both fine.** A free tier is completely acceptable — do not feel you have to spend money to do well on this assignment. If you do choose a paid tool, that is your decision and is not reimbursed by the course.
- **When in doubt, ask first.** If you are unsure whether a tool counts as new or as agentic, confirm with your instructor *before* you start building, so you are not surprised at grading time.

### Tools already used or demonstrated in this course (off-limits)

Claude, ChatGPT, Google AI Studio / Gemini, NotebookLM, Notion agents, ElevenLabs, Voiceflow, Chatbase, n8n, Zapier, Dify, Flowise, CrewAI Studio, Braintrust, Cursor, Perplexity Comet / the Cowork browser, and Groq.

If a tool you are considering is closely related to one on this list, ask before you build.

---

## What you build

- Build something **real and relevant to the industry you work in** — or, if you are not currently working in your target field, the industry you are preparing to enter.
- It must **actually function.** A live demo is part of your presentation. A set of screenshots is not a working agent.
- **Scope it to what you can demo in about two minutes.** A small thing that works beats a big thing that half-works — you learned that in Project 2. Pick a narrow, real task and make it solid.
- **A caution from Module 8:** do not load real confidential workplace data into a tool you have not vetted. Use realistic but non-sensitive content, the same way you did in the earlier projects.

---

## The four required concept ties

Every capstone must connect the build to **all four** of the ideas below — fully in the written brief, and at least briefly in the presentation. These are the through-lines of the entire course, and they apply to any agentic tool no matter what it is.

**1. Agent Card / SOP — from Module 2 and Project 1.**
Write an Agent Card for what you built: purpose, role, inputs (what it has access to and what it does *not*), task steps, constraints, output format, escalation trigger, and success metric. Even if your chosen tool never asks you for one, you write it anyway. The Agent Card is how you prove you *designed* the agent rather than just clicked around until something worked.

**2. Evaluation — from Module 3.**
How do you know it actually works? Score your agent on the four dimensions — correctness, completeness, safety, and fit. Include at least three documented test runs and what they told you. "It looked good" is not an evaluation.

**3. Risk and governance — from Module 8.**
What is the blast radius? Walk through the threat classes that apply to your tool — prompt injection, tool abuse, over-permissioning, data leakage — name the ones that are genuinely real for your build, and say what you would do about each. This section belongs mostly in the written brief; you will not have time for all of it on stage.

**4. Business case — from Module 3 (ROI) and Module 10 (adoption).**
Why would your industry care? Give a defensible ROI estimate using the three levers — time saved, error reduction, deflection. If ROI genuinely does not fit your build, make the adoption case instead: who would use this, what would make them trust it, and what would make them abandon it.

If a fifth course idea is central to what you built — grounding and RAG from Module 4, tool connection and permission scoping from Module 5, or multi-agent handoffs from Module 9 — bring it in as well. But the four above are required of everyone.

---

## The presentation — Demo Day (Module 12)

- **5–6 minutes, live.** Aim for 5. You will be signaled at the 5-minute mark and be stopped at 6. Practice with a timer — running long is the most common and most avoidable way to lose points.
- **Suggested shape** (not a rule): about 30 seconds on what the tool is and why the class has not seen it; about 2 minutes of live demo; about 2 minutes on the concept ties — touch all four briefly, then go deeper on one; about 30 seconds of honest limits.
- **Test your screen share, audio, and demo path twice** on the machine you will actually present from.
- **Prepare one backup slide with screenshots** in case the live demo fails. A demo failing is normal in this field; not having a backup is a preparation miss.
- **Be ready for questions.** After your demo, your instructor and classmates may ask how the system works, why you designed it the way you did, and where it breaks. Being able to answer those questions — knowing your own build well enough to defend it — is part of your grade.
- **Show us something new.** That is the entire point. The class should walk away knowing a tool — and a real use for it — they did not know before.

---

## The written brief

One PDF or Word document, uploaded to GitHub the night before Demo Day. There is no strict page limit, but it should be noticeably more detailed than your presentation — it is where the analysis lives that you could not fit on stage. It must contain, in order:

1. **The tool** — what it is, a link, why it qualifies as new to this class, whether you used a free tier or paid, and why you chose it.
2. **The build** — what you built, who it is for, and proof it works: a share link if the tool offers one, or clearly labeled screenshots of it running.
3. **Agent Card** — the full card for your build (all eight elements from Project 1).
4. **Evaluation** — your four-dimension scoring and at least three documented test runs.
5. **Risk and governance** — the threat classes that apply to your tool and your specific mitigations. This is expected to be the most detailed section, because it is the one you will say the least about out loud.
6. **Business case** — your ROI estimate or your adoption case.
7. **Honest limits and next steps** — what broke, what you would not trust this agent with yet, and what you would instrument or build next if you had another month.

**A note on honest limits:** this course rewards honest limits as heavily as happy paths — in the presentation and in the brief. A capstone that says "here is what works, here is exactly where it breaks, and here is what I would fix" scores higher than one that claims everything is fine. That is what senior work looks like.

---

## Grading

This capstone is graded out of 100 points across five criteria: tool discovery and novelty, the build, the presentation and demo, the written brief, and honest limits and reflection. See [rubric.md](rubric.md) for the full three-level rubric.

---

## A note on starting early

The hardest part of this capstone is not the build — it is finding the right tool. Give yourself time to look around, try two or three options, and abandon the ones that do not fit. Directories and roundups of AI agents and tools are a reasonable starting point, but verify any tool's free tier and check what data it asks for before you commit to building on it. Students who start tool-hunting the week before Demo Day end up presenting something they do not fully understand — and it shows.

---
