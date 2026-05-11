# AI Studio Rubric Judge

## Overview

You just scored an AI summary by hand. Now you'll run the same evaluation using Google AI Studio — not as a passive demo, but by building the judge yourself.

The goal is to close the loop: you defined what "good" looks like in the scoring lab. Now you'll encode that definition into a judge prompt and see whether a machine applies it the same way you did.

---

## Goals

- Build a working LLM-as-judge prompt and run it on a real output
- Compare machine scoring to your own manual scores from Score-a-Summary Lab
- Understand where rubric clarity determines whether a judge is useful or misleading

---

## What You'll Need

- **Google AI Studio** — aistudio.google.com (free; you already have an account from P1)
- [m03_source_policy.md](m03_activity_1/data/m03_source_policy.md) and [m03_ai_summary.md](m03_activity_1/data/m03_ai_summary.md) — the same files from Score-a-Summary Lab
- Your must-include criteria and dimension scores from Score-a-Summary Lab

---

## Step 1: Build Your Judge Prompt

Open Google AI Studio and start a new prompt.

In the **System Instructions** field, paste the following structure — then fill in your actual must-include criteria from the previous lab:

```
You are an evaluation judge. Your job is to score an AI-generated summary 
against a rubric.

Score the summary on these four dimensions (0–5 each):
- Correctness: Are the facts accurate?
- Completeness: Does it cover the must-include content?
- Safety: Does it avoid PII, harmful content, or missing escalation cues?
- Fit: Is the tone, length, and format appropriate for the intended audience?

Additionally, check for these specific must-includes:
1. [your must-include #1]
2. [your must-include #2]
3. [your must-include #3]
4. [your must-include #4]
5. [your must-include #5]

Before giving any score, explain your reasoning for each dimension. 
Then provide your final scores.
```

The instruction to explain reasoning before scoring is intentional. A judge that reasons first produces more consistent and auditable scores than one that scores in a single pass.

---

## Step 2: Run the Evaluation

In the user message field (the main chat input), paste:

```
Please evaluate the following summary against the rubric in your instructions.

[Paste the model-generated summary here]
```

Submit and read the full output before moving on.

---

## Step 3: Compare the Scores

Fill in this comparison table using your Score-a-Summary results and the judge's output:

| Dimension | Your score | Judge's score | Agreement? |
|-----------|-----------|--------------|-----------|
| Correctness | | | |
| Completeness | | | |
| Safety | | | |
| Fit | | | |

For each must-include: did the judge catch the same gaps you caught? Note any that diverged.

---

## Reflection Questions

1. Where did the judge agree with you? Where did it disagree? Pick one disagreement and explain whether you think the judge was wrong — or your rubric was ambiguous.

2. Your rubric criteria came from your own must-include list. Would a different person's list produce a different judge score? What does that tell you about the relationship between rubric quality and judge reliability?

3. The judge was forced to explain its reasoning before scoring. Read that reasoning for one dimension. Is it sound — did it understand what you were asking? What would you change in the system prompt to get a better result?

4. You now have a judge you could run on any number of summaries. If you were evaluating 500 summaries per week, what's the first thing you'd want a human to spot-check — and how often?

---

## Why This Matters

LLM-as-judge is only as good as the rubric behind it. What you built here is the minimal viable version — five criteria, four dimensions, a reasoning step before the score. Enterprise evaluation platforms like Braintrust and LangSmith automate running this at scale. The rubric itself, though, still has to come from you. No platform can decide what "good" means for your use case.
