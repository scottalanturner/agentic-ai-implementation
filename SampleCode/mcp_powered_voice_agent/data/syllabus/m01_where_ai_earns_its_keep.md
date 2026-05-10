# M01 — Where AI Earns Its Keep: Spotting the Moments in Your Work
## ISYS 398U · Agentic AI Implementation · University of Richmond SPCS

**Session:** May 12, 2026 · Tue · 6:30–8:30 PM EST · Live via Zoom  
**Format:** 2 hours — 3 sections + 2 in-class activities · *(Live 90/30 variant noted in [course-outline.md](../../Syllabus/course-outline.md))*  
**SLO focus:** See [l1-l11-slo-matrix.md](../../Syllabus/l1-l11-slo-matrix.md) — L1 row  
**Activities:** `m01_activity_1_agent_discovery_interview.md` · `m01_activity_2_transcript_lab.md`

---

## Learning Objectives

By the end of this module, students will be able to:

1. **Explain** why the current AI moment represents a genuine shift in how work gets done — and what that means for working professionals who aren't developers
2. **Distinguish** between AI as an assistant (helps you do tasks) and AI as an agent (completes tasks on your behalf, end to end)
3. **Identify** at least three agentic AI opportunities in their own job using a structured, AI-guided discovery process
4. **Apply** conversation as a prototyping method — starting from a raw document or real-world input and producing a structured, actionable work product
5. **Describe** the "glue work" and "pollinator" roles as the highest-value human positions in an agentic work environment

---

## Pre-class preparation *(assign in LMS)*

- Skim the **course description and SLOs** in [syllabus-draft.md](../../Syllabus/syllabus-draft.md) — come ready to name one phrase that matters for *your* job.
- Optional: read one short industry example in [master-lists.md](../../Syllabus/master-lists.md) (Case Studies table — pick any row) and note **one number** that stuck with you.
- Bring to class: **one real task** from your work that eats time every week (you will use it in the audit).

---

## Discussion & reflection *(speaking — not graded exercises)*

**Opening (5–8 min, whole group or think-pair-share):**  
> *The Bank of America “Erica” opener in Section 2 cites billions of interactions. Before we go there: which matters more for trust at scale — speed, accuracy, or transparency? Draw on the case study you skimmed or on your own experience with chatbots at work.*

**Mid-session (after “From Doing to Directing,” ~5 min):**  
> *Where in your organization is “directing” already a job skill (managers, PMs, ops leads), and where is it still invisible? Who gets left behind if AI only rewards people who already know how to delegate?*

---

## Section 1 — Where We Are and Where We're Going

---
### SLIDE: Title
**Agentic AI Implementation**
Module 1 · Section 1

---

---
### SLIDE: The Last Time This Happened

[INSERT IMAGE — early Netscape/Mosaic browser screenshot, circa 1993–1995, or dial-up AOL era imagery]

**The birth of the World Wide Web — 1993**

> *"The internet is for academics and the military. Normal people don't need this."*

---

#### 🗣 Talking Points (instructor narrative — not a slide)

This is one of those rare moments where you can actually feel a shift happening in real time — not read about it in a textbook afterward. The last time most of us saw something like this was the early internet.

In 1993, the first web browser — Mosaic — was released. Within two years, Netscape went public and the dot-com era exploded. The technology itself wasn't new: the internet had existed for decades. What changed was *access* — suddenly anyone could use it, build on it, and find information with it.

And the reaction at the time? A lot of skepticism. "I don't need this." "It's too complicated." "It's for tech people." Sound familiar? The people who moved early — who started building real things with it before the dust settled — ended up defining the next 30 years of business.

We are at that same inflection point again. Generative AI has been developing for years, but the last two years have been a light-switch moment. The interface became so accessible that anyone can use it. And we haven't even begun to scratch the surface of what gets built next.

The question this course answers is: *how do you actually build things with it?*

Let's start with three real examples — no theory, no PhD required.

---

---
### SLIDE: Example 1 — The Weed in the Yard

[INSERT WEED PHOTO HERE]

**The problem:** Unknown weed on the property. What is it — and when do you treat for it?

**What happened:** One photo + one question → species identified, growth cycle explained, optimal treatment window returned.

**What this replaced:** Calling an extension office. Waiting. Maybe getting a wrong answer.

**The unlock:** You don't need to be an expert. You need to ask the right question.

---

---
### SLIDE: Example 2 — The Lawn Mower

[INSERT LAWN MOWER PHOTO HERE]

**The problem:** Large property needs spraying. Options: buy a $15,000 tractor, rent complex equipment — or find another way.

**What happened:** One photo of the existing mower → AI identified the make and model, found the correct trailer hitch spec, and recommended a compatible spraying system that attached to what was already owned.

**What this replaced:** A specialist consult, hours of research, and a five-figure purchase.

**The unlock:** AI connected what you already have to what you actually need.

---

---
### SLIDE: Example 3 — Building "Greater"

[INSERT GREATER APP SCREENSHOT HERE]

**The problem:** Sports analytics is dominated by expensive platforms and large data teams. What if one person could build something competitive?

**What's happening:** *Greater* — a sports analytics app — is currently in development, with generative AI involved at every step: architecture, code, features, iteration.

**What this replaced:** A full development team. A large budget. Years of runway.

**The unlock:** A problem that once required a team is now within reach of one person with the right tools and the right questions.

---

---
### SLIDE: The Pattern

Every example follows the same structure:

1. A **real problem** — not a classroom exercise
2. A **photo or prompt** — accessible to anyone with a phone or laptop
3. An answer that used to require **expensive expertise or equipment**
4. A result achieved at **dramatically lower cost and time**

This isn't a demo. This is a new way of working — and it's available right now.

---

---
### SLIDE: Agentic vs. AI Agent — What's the Difference?

**Agentic** — describes *behavior*

Acting autonomously toward a goal across multiple steps — not just answering once and stopping. An AI that searches the web, reads articles, writes a draft, runs it past a checker, and revises — all in sequence — is behaving agentically.

**Agentic = how it operates.**

---

**AI Agent** — describes *a system*

A system designed to operate agentically. It typically has:
- A goal to pursue
- Tools it can use (search, code, files, APIs)
- The ability to decide what to do next
- Memory across steps

**AI Agent = what it is.**

---

> *Think of it like a smart friend: answering your question = **chatbot**. Running your errands all week = **AI agent**. The step-by-step way they work through those errands = **agentic**.*

---

#### 🗣 Talking Points (instructor narrative — not a slide)

The terminology gets muddled fast, so it's worth slowing down here. Students often use "AI agent," "agentic AI," and "chatbot" interchangeably — and they're not the same thing.

**Agentic** is an adjective that describes how something operates. It means multi-step, autonomous pursuit of a goal. You can have a *moment* of agentic behavior without having a full AI agent system — for example, a model that searches the web before answering your question is doing something agentic, but it might not be what most people would call an agent.

**An AI agent** is a system — something built and configured to operate that way persistently and across a broader set of tasks. It has tools. It has memory. It has a goal. It decides what to do next based on what it just learned.

**A chatbot** is the baseline: one question, one answer. There's nothing wrong with chatbots — they're extremely useful — but they're not agents, and they're not behaving agentically. They respond; they don't pursue.

The reason this matters: as students start identifying automation opportunities in their work, they need to know *what kind of thing* they're building toward. "I want AI to answer my questions" is a chatbot use case. "I want AI to handle my inbox while I'm traveling" is an agent use case. The difference shapes everything about how you build it.

The blurry edge: modern AI systems exist on a spectrum. There's no bright line between "agentic" and "not agentic" — it's a matter of degree. That's fine. The framework is a tool for thinking, not a legal classification.

---

---
### SLIDE: Quick Check — Chatbot, Agentic, or AI Agent?

*For each scenario below, decide which category fits best — and be ready to explain why.*

| Category | What it means |
|----------|--------------|
| 🟥 **Chatbot** | One exchange. You ask, it answers. Done. |
| 🟩 **Agentic** | Multi-step autonomous behavior toward a goal. |
| 🟦 **AI Agent** | A system built to operate agentically, with tools and memory. |

1. You type a question and get an answer. One exchange, done.
2. An AI monitors your inbox overnight, drafts replies, schedules meetings, and flags urgent items.
3. Before answering your question, an AI searches ten websites, reads them, and synthesizes the findings.
4. Siri tells you the weather when you ask.
5. An AI reads your project files, writes code, runs it, catches the errors, fixes them, and delivers finished output.
6. A customer service system routes incoming tickets, escalates based on urgency, and updates the queue — continuously.
7. An AI browses the web, books a flight, and sends your boarding pass to your phone.
8. You ask an AI to explain a concept and it gives you a clear, well-written paragraph.

---

#### 🗣 Talking Points / Answer Key (instructor only)

Run this as a quick show-of-hands or think-pair-share — 5 minutes max. The goal is to make the vocabulary stick before moving on, not to quiz anyone.

Expected answers (reasonable debate is fine):
1. **Chatbot** — single exchange, no autonomy
2. **AI Agent** — persistent system with tools, memory, and goal (inbox management)
3. **Agentic** (behavior) — multi-step, but could be a one-off; the *behavior* is agentic even if it's not a full agent system
4. **Chatbot** — Siri answering a factual question is single-exchange
5. **AI Agent** — has tools, pursues a goal across steps, handles errors autonomously
6. **AI Agent** — persistent, tool-using, goal-driven system
7. **Agentic** or **AI Agent** — good debate item; the *behavior* is clearly agentic; whether it's a "system" depends on how it's built
8. **Chatbot** — clear, well-written, but still one exchange

Items 3 and 7 are intentionally ambiguous — use them to surface the spectrum point: agentic behavior and an AI agent system aren't always the same thing.

---

---
### SLIDE: How Agents Actually Work — Three Patterns

Most AI agents you'll encounter follow one of three design patterns. You don't need to build them to understand them — but recognizing the pattern tells you a lot about what an agent can and can't do.

---

**ReAct — Reason, then Act, then Look, then Repeat**

The most common pattern. The agent thinks about what to do, takes one action, sees what happened, thinks again, and repeats until it's done. It's a loop: Reason → Act → Observe → Reason → Act → Observe…

*Best for:* tasks where the right next step depends on what you just learned. Research, troubleshooting, multi-step workflows with unknowns.

---

**Plan and Execute — Map the Route First, Then Drive**

The agent builds a full plan upfront ("here are the 6 steps I'll take"), then executes each step in order. Less flexible than ReAct — it can't easily adapt if step 3 produces a surprise — but more predictable and easier to audit.

*Best for:* well-defined tasks with known steps. Report generation, data pipelines, structured workflows where you want to see the plan before it runs.

---

**Multi-Agent — A Team of Specialists**

Instead of one agent doing everything, different agents handle different parts of the job and hand off to each other. A researcher agent gathers information, a writer agent drafts, a critic agent reviews. Each is optimized for its role.

*Best for:* complex, long-horizon tasks that exceed what a single agent can reliably hold in memory or handle well. Also useful for quality control — having one agent check another's work.

---

#### 🗣 Talking Points (instructor narrative — not a slide)

You don't need to go deep on the mechanics here — this is a conceptual orientation, not a technical lecture. The goal is to give students a mental model they'll recognize later in the course when they start building.

**On ReAct:**

ReAct stands for Reasoning + Acting, and it was introduced in a 2022 research paper that became highly influential. The core insight is that agents perform dramatically better when they alternate between *thinking* and *doing* rather than trying to plan everything upfront. The reasoning steps also make the agent's behavior much more interpretable — you can actually see why it did what it did.

The analogy that lands well: imagine a detective at a crime scene. They don't sit in a room and deduce the solution from first principles. They look at a clue, form a hypothesis, look for the next clue, revise the hypothesis. That's ReAct. It's the pattern behind most of the AI agent demos you'll see on the internet — Claude browsing the web, ChatGPT running code and checking the result.

The limitation worth naming: because it goes one step at a time, ReAct can be slow on complex tasks. And if it gets confused early, it can go down a wrong path and not recover.

**On Plan and Execute:**

The intuition here is project management. Before you start a big project, you write a plan. The plan might change, but having it upfront helps everyone see where things are going and catch problems early.

In an agent context, this matters because you can show the plan to a human before executing it. That's a significant safety and oversight advantage — especially in professional environments where you want someone to sanity-check what the AI is about to do before it does it.

The limitation: if reality doesn't match the plan — if step 3 returns something unexpected — a pure Plan and Execute agent may struggle to adapt without essentially starting over. More sophisticated versions handle this with replanning loops, which starts to look like a hybrid of both patterns.

**On Multi-Agent:**

This is where agentic AI starts to look less like a tool and more like a team. Each agent is a specialist: one searches, one writes, one checks. They communicate results and hand off tasks. Orchestration — knowing which agent should do what, and when — becomes the critical skill, and that's increasingly a human role.

The analogy: a newsroom. The reporter gets the story. The editor shapes it. The fact-checker reviews it. The headline writer packages it. No single person does all four equally well, and the workflow improves because of the specialization.

For students, this is the pattern that makes the "glue work" and "pollinator" concepts from the next slide feel concrete. In a multi-agent system, the most important work is often the coordination between agents — and between agents and humans. That coordination is human work.

One practical note: multi-agent systems are also how you break the context window problem. A single AI model can only hold so much in its working memory at once. If your task is long enough — a weeks-long research project, a complex software build — you need multiple agents with different memory scopes working together.

---

---
### SLIDE: The Human Edge in Agentic Systems

As AI handles more technical execution, the most valuable skills shift to what holds systems — and teams — together.

- **Glue Work** — the coordination, context-setting, and relationship-building that keeps agentic projects from falling apart
- **Pollinators** — cross-functional bridge-builders who carry requirements, insight, and context between agents, teams, and decisions

---

#### 🗣 Talking Points (instructor narrative — not a slide)

**On Glue Work:**

- The term comes from software engineering — coined in 2019 by Tanya Reilly to describe the largely invisible work that holds projects together: knowing who to call, noticing when two teams are working at cross-purposes, onboarding new people, filling the gaps no one owns. It was always essential but chronically undervalued — often career-limiting for junior engineers who spent time on it instead of writing code.

- AI is flipping that calculus. When AI can generate competent code on demand, the skill that's suddenly scarce isn't technical execution — it's knowing *what to build*, *for whom*, and *how to coordinate the people and agents doing the building*. Managing an AI agent means defining its context clearly, catching when it's drifting, and connecting it to the actual human need it's supposed to serve. That is glue work.

- Worth noting from the reader comments: someone described their own job as "business liaison, system design, and scripting" — and said AI has now taken over the scripting, leaving more time for everything else. They found a great term for what they'd always been doing. That shift is happening across roles right now.

- A GitHub staff engineer put it directly: the people who were already fluent in this kind of connective work are having an easier time with the AI transition. The people struggling are often those who built their identity around code craft. Not a knock — just an illustration of how fast value can move.

**On Pollinators:**

- If glue work is about holding a *single* project together vertically, pollinators work horizontally — they move between teams, domains, and systems carrying ideas, requirements, and context that wouldn't otherwise travel.

- In a traditional org, this is the person who knows what the data team just figured out that would completely change how the product team is building the next feature — and actually tells them. In an agentic context, it's the person who understands what each AI workflow can and can't do, and routes the right problem to the right tool or agent.

- Pollinators are especially valuable in agentic systems because AI agents don't naturally coordinate with each other or with human stakeholders. Someone has to do that. That someone is a pollinator.

- Neither of these roles is glamorous or loud — the comments on the article make the point that glue workers are often the first cut in a downsizing, because their value is invisible until it's gone. Your job in this course is to make that value visible — to yourself and to the organizations you work in.

---

---
### SLIDE: What This Course Is About

One central question drives everything we do this semester:

> **How do you solve real problems with agentic AI — and build things that didn't exist before?**

We move from concepts directly to hands-on implementation.

You'll leave with actual tools, workflows, and projects — not just frameworks.

**Let's get started.**

---

> 📋 **→ ACTIVITY 1: Agent Discovery Interview** (`m01_activity_1_agent_discovery_interview.md`)
> *10–15 min | Solo with AI tool → Pair share → Class debrief*
> Students use an agent to interview themselves and surface agentic AI opportunities in their own work. Keep the opportunity tables — they'll be referenced throughout the semester.

---

## Section 2 — AI at Work: How I Use It Every Day

---
### SLIDE: Title
**AI at Work: How I Use It Every Day**
Module 1 · Section 2

---

---
### SLIDE: Work Feels Like Magic

> *"These days, work feels a lot like magic — like I'm some sorcerer that's able to conjure things that shouldn't be possible. The truth is it really is magical now because I'm using AI and AI agents every single day for everything I do."*

— Vanderbilt GenAI & Agents for Leadership, Module 1

That resonated with me — because I feel it too.

In this section, I'll show you what that looks like in my own work: the specific tools, workflows, and moments where AI went from "interesting" to indispensable.

---

#### 🗣 Talking Points (instructor narrative — not a slide)

Open by letting this quote land. Don't rush past it. The Vanderbilt instructor — a computer science professor — is describing his daily experience with AI, and it sounds like something out of a fantasy novel. That's intentional.

The point isn't hype. The point is that this is coming from someone who has been building software for decades and *still* finds it remarkable. When people who understand the machinery say it feels like magic, that's worth paying attention to.

Use this slide to set the tone: what follows is a personal, honest look at how AI has changed the actual texture of your work. Not a demo, not a vendor pitch — just what you actually do now that you didn't do a year ago.

---

---
### SLIDE: What My Work Looks Like Now

[PLACEHOLDER — Scott fills in 3–4 daily workflows with brief descriptions]

**Examples of what to include:**
- A morning routine or daily briefing task you've handed to AI
- A research or writing workflow that used to take hours
- An automation or agentic task you set up to run without you
- A decision-support use case (analyzing options, summarizing input, etc.)

> *"I could go and code all these things, but [AI] can do it a thousand times faster — and because it can, I can experiment with 10 different ways of doing it."*

---

#### 🗣 Talking Points (instructor narrative — not a slide)

This is the heart of the section — and the most personal part. The goal is to show, not tell. Walk through your actual workflows with enough specificity that students can see themselves doing something similar.

Some things to consider sharing:
- **The "before" state**: What were you doing manually that you no longer do?
- **The tool**: What are you actually using — Claude, ChatGPT, a custom agent, something you built?
- **The prompt or trigger**: How did you kick it off? What did you say or type?
- **The result**: What came back, and how did it change what you did next?

The Vanderbilt example walked through organizing a downloads folder and then setting up an automated expense-receipt workflow — both real, mundane things that became instant. Lean into the mundane. Students relate to tasks that sound unglamorous more than polished demos.

---

---
### SLIDE: [PLACEHOLDER — Workflow Deep Dive]

[PLACEHOLDER — Pick one workflow from the previous slide and go deeper]

**Suggested structure:**
- **The task:** What were you trying to accomplish?
- **What you did:** The exact prompt or setup (screenshot optional but powerful)
- **What came back:** The result — good, surprising, or unexpected
- **What changed:** How does this affect your work going forward?

[INSERT SCREENSHOT OR DEMO HERE if available]

---

#### 🗣 Talking Points (instructor narrative — not a slide)

Choose whichever workflow from the previous slide is most visual or most relatable to your students. Working adult professionals in the SPCS context tend to respond well to workflows that map to things they already do — email triage, meeting prep, writing first drafts, analyzing data from a report.

If you have a screenshot or a short recording of the workflow in action, use it here. Seeing the actual interface and the actual output is far more convincing than a description of it.

---

---
### SLIDE: The Shift — From Doing to Directing

**Before:** You are the executor. Every task requires your direct time and skill. You are the bottleneck.

**Now:** You are the director. You describe what you want. AI figures out how, executes it, and returns results.

> *"It's kind of like you handed your computer to a PhD in computer science — and you just talk to it."*

The unlock isn't just speed. It's that you can now **dream up something and actually realize it** — without needing to be an expert in how it gets built.

---

#### 🗣 Talking Points (instructor narrative — not a slide)

This slide captures the conceptual shift that makes everything else in the course make sense. It's not that AI is a faster search engine, or a better autocomplete, or a way to save 20 minutes on email. It's that the *relationship* between you and computing has fundamentally changed.

You used to be limited by what you could personally build or afford to hire. Now you can direct. That changes the scope of what's possible for any individual.

Use the "PhD in computer science" analogy deliberately. It's not about replacing people — it's about having a very capable, patient collaborator that doesn't charge by the hour and works at whatever pace you set.

For your students — working adults with real jobs — this framing matters. They're not here to become AI engineers. They're here to become better directors of the AI tools they already have access to.

---

---
### SLIDE: What This Means for You

You don't need to be a developer. You need to learn to think like a director.

1. **Notice what you do repeatedly** — those are your first automation candidates.
2. **Pick one workflow from today's section** and try it yourself this week.
3. **Describe tasks in plain language** to an AI tool instead of doing them manually.
4. **Keep a running list** of tasks AI handled well — that list becomes your automation portfolio.

The rest of this course is about building that portfolio, one workflow at a time.

---

#### 🗣 Talking Points (instructor narrative — not a slide)

Close with action. The biggest risk after a section like this is that students find it impressive but don't try anything until the next assignment forces them to. Head that off here.

The "running list" framing is important: it gives them something low-stakes and ongoing to do. They're not being asked to build a system right now — just to notice. That noticing habit is actually the foundation of everything else in the course.

If you have a specific prompt or tool you want them to try before next class, name it here. Something small and achievable: "Take one task from your actual job this week. Describe it to Claude. See what happens."

---

## Section 3 — How AI Gets Built: It's All Conversation

---
### SLIDE: Title
**How AI Gets Built: It's All Conversation**
Module 1 · Section 3

---

---
### SLIDE: The Foundation — It's All Conversation

- **Everything runs on conversation.** Prompting, agents, complex multi-step systems — at the core of almost all of it is a conversation. Even sophisticated agents are, behind the scenes, a conversation with the right context and instructions baked in.
- **The skill that matters isn't programming.** It's learning to architect conversations: what context to provide, what to ask, and how to iterate toward a solution.
- **Getting the right information in is the unlock.** A screenshot, a photo, a document — you don't need elaborate integrations. Get the right context into the conversation and the model can reason powerfully from it.
- **Conversations are iterative, not one-shot.** You refine, critique, and adapt — fundamentally different from search or static tools. That back-and-forth is where the real capability lives.
- **Chat is your prototyping environment.** Once a conversation reliably gets you what you need, you can build from it — hand it to an agent, extend it into a workflow, or simply repeat it as a practice. Not everything becomes an automation; all of it starts as a conversation.

---

#### 🗣 Talking Points (instructor narrative — not a slide)

This slide exists to reframe a common misconception before it takes root. Students often arrive assuming that working with AI is a technical discipline — something that belongs to data scientists and ML engineers. This is the moment to correct that.

The Vanderbilt professor who made this point has spent his career in computer science. His argument is that classical programmers are actually *less* well-positioned for this era than people who know how to solve problems through conversation — because the interface has changed. The API to AI is language, not code.

The practical implication: every skill students build in this course — prompting, context-setting, iterating, chaining tasks — is essentially learning to be a better conversational architect. That framing should carry through the rest of the semester.

The whiteboard, lunch order, and calendar meal-planning examples from the source video are good illustrations if you want to reference them verbally. The pattern in all three: get a piece of real-world context into the conversation (a photo, a menu, a screenshot), then iterate from there. That's the move.

Close with the prototyping point carefully. The course is agentic AI, not automation — and those aren't the same thing. Some of what students build will be agents; some will be repeatable workflows; some will just be a prompt they run every morning. Chat is where all of it starts, and that's the point. Don't promise that everything becomes a system — promise that getting good at conversation is the foundation for whatever they build next.

---

---
### SLIDE: Conversation in Action — [Your Example Here]

[PLACEHOLDER — Walk through a real project or task where you used a document, transcript, output, or artifact as the starting point for a conversation with AI]

**Structure to follow:**
- What was the raw material you started with?
- What did you ask first — and why that question, not a generic one?
- How did the conversation evolve from there?
- What work product came out of it that would have taken much longer to produce manually?

---

#### 🗣 Talking Points (instructor narrative — not a slide)

These are the points worth making when you walk through your own example.

**Don't use AI as a summarizer. That's the floor, not the ceiling.**
The instinct most people have is to hand something to AI and say "summarize this." That's the laziest and least useful application. The power comes from asking from *your* perspective and *your* needs — not a generic output, but the specific thing you actually need to do next. Whatever your example is, make this contrast explicit: here's what the lazy version looks like, and here's what actually useful looks like.

**You can go from raw material directly to work product — skipping the intermediate grind.**
Before AI, going from "we just finished a meeting / a draft / a discovery session" to "here are organized phases, open questions, and next steps" required hours of synthesis work. The conversation collapses that gap. Whatever your example is, name what it *replaced* — what you used to have to do manually that you no longer do.

**Structure and priorities emerge from the conversation, not just extraction.**
There's a difference between pulling information out of something and organizing it into something useful. You can ask AI to impose structure: order these by dependency, group these by theme, identify which of these are prerequisites for the others. That's not summarizing — that's reasoning. Make sure your example shows at least one moment where you asked for structure, not just content.

**Ask what's missing, not just what's there.**
One of the most powerful moves in any project-oriented conversation is to ask: what did we not discuss that we need to? What are the open questions? What assumptions are we making that we haven't examined? This surfaces blind spots the human doing the work would likely miss because we're too close to it. If your example has a natural place for this, use it.

**AI outputs become inputs for your next human conversation.**
The work product from a good AI conversation isn't the final answer — it's the thing that gets the right human discussion started faster and better-informed. Organized work, surfaced questions, estimated effort — these become your agenda, your talking points, your team's next meeting. Make the point that AI isn't replacing the human conversation; it's improving the quality of it.

**Devil's advocate as a discipline.**
Once you have a plan, a draft, or a design, you can ask AI to attack it: poke holes, challenge assumptions, find what you haven't thought about, argue the other side. This is genuinely hard for humans to do to their own work. It's a free adversarial review available on demand. If your example has a natural place to show this — even briefly — it lands well with students.

---

> 📋 **→ ACTIVITY 2: The Transcript Lab** (`m01_activity_2_transcript_lab.md`)
> *20–25 min | Solo (3 rounds) → Class debrief*
> Students apply conversation techniques to a real meeting transcript — extracting action items, surfacing hidden intelligence, and producing a work product (project brief, stakeholder summary, or risk register). Debrief connects the experience back to the agentic AI framing at the end of the activity file.

---

## Key Takeaways

---
### SLIDE: Key Takeaways

**What to carry out of today:**

1. **You don't need to be a developer.** The most important skill in the agentic era is knowing how to direct — what to ask, how to describe what you need, and how to evaluate what comes back. That's a human skill, and you already have the foundation for it.

2. **Every agentic AI opportunity starts as a conversation.** Chat is your prototyping environment. If you can get a conversation to reliably do something useful, you can build from it — automate it, extend it, hand it to an agent. Not everything becomes a system. All of it starts here.

3. **The gap between "AI helps me" and "an agent handles this for me" is exactly what this course teaches you to close.** Your Discovery Interview output from today is your map. We'll come back to it.

4. **The most durable human skills in an agentic workplace are coordination, context, and judgment.** The people who hold systems together — the glue workers, the pollinators — are the ones whose value goes up as AI takes over execution. That's the role you're building toward.

---

#### 🗣 Talking Points (instructor narrative — not a slide)

Don't rush this slide. It's the one that students will photograph or screenshot, and it should land as a summary of the whole session, not just a checklist.

Walk through each point briefly and connect it back to something concrete from today — a moment in the Discovery Interview, something that surprised them in the Transcript Lab, a line from the "From Doing to Directing" slide. The callbacks make the takeaways stick.

Close by bridging forward: next session we go inside the agent itself — how it thinks, how it makes decisions, and what the four design patterns are that underlie almost every agentic system they'll encounter. Today was the *why*. What comes next is the *how*.
