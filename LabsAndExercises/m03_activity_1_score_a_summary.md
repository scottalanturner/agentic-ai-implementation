# Score-a-Summary Lab

## Overview

Most people review AI output the same way they review email — they skim it, it sounds reasonable, they move on. That's not evaluation. Evaluation means applying consistent criteria to decide whether an output is actually correct, complete, safe, and appropriate for its purpose.

This lab gives you a real policy document and an AI-generated summary to score. The summary sounds professional. It is not entirely accurate. Your job is to find out where it fails — and why those failures matter.

---

## Goals

- Apply the four evaluation dimensions (correctness, completeness, safety, fit) to a real AI output
- Discover which dimension is hardest to score consistently — and why
- Build the habit of reading the source before judging the summary

---

## Your Materials

Open both files before you start:

- **Source document:** [m03_source_policy.md](m03_activity_1/data/m03_source_policy.md) — the original policy
- **AI-generated summary:** [m03_ai_summary.md](m03_activity_1/data/m03_ai_summary.md) — what an agent produced from it

---

## Step 1: Read the Policy First

Read `m03_source_policy.md` in full before you look at the summary.

As you read, write down **5 things** that any accurate summary of this policy must include. These are your must-includes — the criteria you'll score against.

Do not look at the summary yet. Your must-includes should come from the policy, not from whatever the summary happened to mention.

---

## Step 2: Score the Summary

Now open `m03_ai_summary.md` and score it using the tables below.

**Four dimensions (0–5 for each):**

| Dimension | Your score | What specifically went right or wrong |
|-----------|-----------|--------------------------------------|
| **Correctness** — Are the facts stated accurately? | | |
| **Completeness** — Did it cover what a reader needs to know? | | |
| **Safety** — Does it omit or misrepresent anything that could cause harm or compliance exposure? | | |
| **Fit** — Is the tone, length, and detail level appropriate for a workplace policy summary? | | |

**Must-includes check:**

| Must-Include | Covered? (Y / Partially / N) | Notes |
|-------------|------------------------------|-------|
| 1. | | |
| 2. | | |
| 3. | | |
| 4. | | |
| 5. | | |

---

## Step 3: Find the Specific Text

For any dimension where you scored below 4, go back into the summary and identify the exact sentence or gap responsible.

For each problem, write:
- What the summary says (or doesn't say)
- What the policy actually says
- Why the gap matters — what could go wrong if an employee relied on the summary instead of the original?

---

## Reflection Questions

1. Which dimension was hardest to score — not because the summary was obviously wrong, but because the criterion itself was difficult to apply? What made it hard?

2. The summary sounds professional and well-organized. If you hadn't read the source document first, would you have trusted it? What does that tell you about how most AI output gets reviewed in practice?

3. Look at your must-includes list. Did the summary cover any of them partially — enough to seem complete, but not enough to be safe to act on? How do you score something that's half-right?

4. Imagine an employee reads only the summary and then acts on it. For the specific gaps you found, what's the worst realistic outcome?

---

## Why This Matters

Evaluation systems fail before they're built — not because of technical problems, but because no one defined what "good" looks like before running a test. What you just did manually is what LLM-as-judge, rubrics, and eval harnesses automate at scale. The tool can apply the check consistently. Only you can decide what passing means — and whether the rubric is specific enough to catch the things that actually matter.
