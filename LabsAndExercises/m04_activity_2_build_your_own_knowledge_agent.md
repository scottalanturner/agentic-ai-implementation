# Activity 2 — Build Your Own Knowledge Agent

**Requires:** Free Google account · notebooklm.google.com

---

## Overview

You just saw the four stages of retrieval-augmented generation on a slide: chunk, embed, retrieve, generate. Stages on a slide are easy to nod along to. They get interesting the moment you watch one of them go wrong on material you actually understand.

In this activity you'll stand up a working knowledge agent in NotebookLM using three sources you choose, ask it five questions you know the answers to, and score what comes back. The point isn't to prove NotebookLM is good or bad. The point is to catch the pipeline in the act — to see chunking, retrieval, and generation as three separate things that can each help or hurt the final answer.

---

## Goals

- Stand up a working knowledge agent grounded in source material you provide
- Experience all four stages of the retrieval pipeline on content you know well enough to judge
- Build a habit of scoring answers against citations, not against vibes
- Notice at least one moment where chunking or retrieval shaped the answer in a way you can name

---

## Step 1 — Pick a Topic You Already Know Well

Pick something you have real depth in. Not "something I read about once" — something you could answer follow-up questions on without looking anything up. The point is depth of familiarity, not professional relevance.

Examples:

- A hobby (woodworking, knitting, fly fishing, a specific video game, fantasy football)
- A sport you play or follow closely
- Your major or a course you've taken
- An internship area or your day job
- Volunteer work, a club you're in, a fan interest
- A topic you've researched for fun (a historical period, a band's discography, a TV show's lore)

You need to know the topic well enough to spot when an answer is subtly wrong. That's the whole assignment — you are the ground truth.

---

## Step 2 — Gather Three Source Materials

Find three pieces of source material about your topic. **Mix the formats if you can** — that's where you'll see chunking behave differently.

Acceptable sources:

- PDFs (papers, manuals, rulebooks, guides)
- Web pages and articles
- Official documentation
- Public-domain books
- YouTube videos that NotebookLM can ingest
- Plain text notes you've written yourself

Aim for sources that actually contain answers to the questions you'll ask in Step 4 — not just sources that mention the topic. If two of your three sources need to be combined to answer a question, even better.

---

## Step 3 — Build the Notebook

Go to **notebooklm.google.com** and sign in with a Google account.

1. Click **+ New** (or **Create new notebook**)
2. Upload or paste in all three sources
3. Wait for NotebookLM to finish processing — this is the chunk + embed step happening in front of you

Give the notebook a name that matches your topic. You'll need this notebook again in the debrief.

---

## Step 4 — Write Five Questions of Varying Difficulty

Open a text editor or a doc and write five questions about your topic. Vary the difficulty deliberately:

- **One easy lookup** — the answer is stated directly in one of the sources
- **One detail question** — a specific number, date, name, or exception
- **One synthesis question** — the answer requires combining information from **two of the three sources**
- **One edge case** — a question where the sources are ambiguous, contradict each other, or don't quite cover it
- **One question of your choice** — pick whatever you're curious about

You should know the right answer to all five before you ask them. That's what makes the scoring meaningful.

---

## Step 5 — Ask and Score

Ask each question in NotebookLM's chat. For each answer, score it 1 to 3:

| Score | What it means |
|-------|---------------|
| **1** | Wrong, fabricated, or unsupported by what you uploaded |
| **2** | Partially supported — paraphrase drift, missed an exception, or only one of two needed sources was used |
| **3** | Directly supported by a citation that checks out when you click into the source |

**Click every citation.** A score of 3 requires that the cited passage actually says what the answer claims. NotebookLM is good at producing confident-sounding answers; the citation check is what keeps you honest.

Record your results in a table like this:

| # | Question | Answer (short) | Score | Source(s) cited |
|---|----------|----------------|-------|-----------------|
| 1 |          |                |       |                 |
| 2 |          |                |       |                 |
| 3 |          |                |       |                 |
| 4 |          |                |       |                 |
| 5 |          |                |       |                 |

---

## Step 6 — One Observation About the Pipeline

Pick the single moment where retrieval surprised you. Some candidates:

- The wrong heading dominated the answer ("it kept quoting the intro, not the section that actually answered the question")
- An obvious answer was missed entirely
- A clean PDF lost a table and the numbers came back garbled
- The synthesis question only pulled from one source when the answer needed both
- A direct quote got paraphrased into something subtly wrong
- A citation pointed to a passage that didn't actually support the claim

Write **one sentence** naming what likely happened in the chunking or retrieval step. You don't need to be right — you need to have a hypothesis you can defend.

Example: *"The synthesis question only cited Source A because the relevant paragraph in Source B was buried inside a long bulleted list that probably got chunked as one giant block, so the matching part didn't surface."*

---

## Deliverable

Bring three things to the debrief:

1. A working NotebookLM notebook with three sources loaded
2. Your five-row scoring table (question, answer, score, source(s) cited)
3. One sentence on the chunking or retrieval moment you noticed

---

## Reflection Questions

Answer these before the debrief:

1. Which stage of the pipeline — chunk, embed, retrieve, or generate — did you see fail most clearly in your five questions? How could you tell it was that stage and not a different one?

2. The synthesis question is usually the hardest. What happened on yours? If the agent only used one source when it needed two, what does that tell you about how retrieval ranks chunks?

3. Look at your score-3 answers. Were the citations exact quotes, paraphrases, or summaries? Does the kind of citation change how much you trust it?

4. If you were going to build a real knowledge agent for work — same four stages, different source material — what's the single thing you'd want to control or inspect that NotebookLM doesn't let you see?

5. What's one type of question your sources clearly cannot answer well, and what would you add to the source material to fix that?

---

## Why This Matters

A knowledge agent is only as good as what it can retrieve. You can have the best language model in the world generating the final answer — if the chunk it's grounding on is the wrong chunk, the answer is wrong. Sometimes confidently wrong.

Today you ran the same pipeline that sits underneath every "AI assistant trained on your company's documents" product on the market. The vendors hide the four stages behind a clean chat interface. You just looked under the hood for twenty-five minutes. The next time someone pitches you a knowledge agent, you'll know exactly which four questions to ask.
