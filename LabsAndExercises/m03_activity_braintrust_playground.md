# Activity: Prompt Eval in Braintrust Playground

**Format:** In-class activity — solo  
**Time:** 15–20 minutes  
**Requires:** Free Braintrust account · braintrust.dev

---

## Overview

You just watched companies like LangSmith and Google run evaluations at scale — thousands of outputs, automated scoring, regression tracking. This activity puts the same idea in your hands in under 20 minutes.

You'll write two versions of a system prompt for a task from your own work, run the same five test questions through both, and use Braintrust's LLM-as-judge scoring to see which prompt actually performs better. Not "feels better." Actually better — with numbers.

---

## Goals

- Experience the evaluation workflow firsthand: dataset → experiment → score → compare
- See how a small change in prompt wording produces measurable quality differences
- Build the habit of designing prompts to be testable, not just intuitive
- Walk away with a free account you can use on your own agent builds

---

## Step 1: Create Your Free Account (2 min)

Go to **braintrust.dev** and sign up. The free tier includes everything you need for this activity. No credit card required.

Once you're in, you'll land on your organization dashboard. You'll see options to create a **Project**. Create one and name it something like `prompt-eval-[your initials]`.

---

## Step 2: Choose Your Task and Write Two Prompts (5 min)

Pick a task you'd realistically want an agent to handle at work. Use one you identified in the M01 Discovery Interview or pick a new one. It should be:

- Something with a **right and wrong** answer or a clear quality bar (not purely subjective)
- Repeatable — the same type of question asked multiple times
- Specific enough that you can write 5 test questions for it

**Good examples:**
- Summarize a customer support ticket and classify its urgency
- Answer a question about company policy from a provided document
- Draft a follow-up email for a specific meeting outcome
- Extract action items from a meeting description

**Bad examples (too vague to evaluate):**
- "Be a helpful assistant"
- "Help me with my work"

Now write **two versions** of a system prompt for your chosen task. Make them meaningfully different — not just one word swapped. Think about what you learned in M02 about what makes a strong SOP: role, inputs, constraints, output format, escalation trigger.

**Prompt A** — your first instinct. Write whatever feels natural.

**Prompt B** — your improved version. Apply the SOP structure from M02. Be explicit about format, constraints, and what "done" looks like.

Write both prompts in a text editor before going into Braintrust.

---

## Step 3: Set Up Your Evaluation in Braintrust (5 min)

In your Braintrust project:

**Create a Dataset:**
- Click **Datasets** → **New Dataset**
- Name it `test-questions`
- Add 5 rows — each row is one test question or input for your task
  - Use realistic inputs, not edge cases you already know will fail
  - Think: what would an actual user submit?

**Create a Prompt:**
- Click **Prompts** → **New Prompt**
- Paste in **Prompt A** as your system message
- Save it as `prompt-a`
- Repeat for **Prompt B** — save as `prompt-b`

---

## Step 4: Run the Experiment (5 min)

- Click **Experiments** → **New Experiment**
- Select your dataset (`test-questions`)
- Select **Prompt A** as the prompt to evaluate
- Under **Scoring**, add an **LLM-as-judge** scorer — Braintrust has built-in options. Choose **Factuality** or **Quality** depending on your task type
- Run the experiment. It will take about 30–60 seconds.
- Repeat with **Prompt B**

Now you have two experiments side by side.

---

## Step 5: Compare and Read the Results (3 min)

Go to **Experiments** and open both runs. Look at:

- **Overall score** — which prompt scored higher on average?
- **Per-row scores** — which specific test questions did each prompt handle better or worse?
- **Output content** — click into individual rows and read the actual responses. Does the score match your gut? If not, why?

---

## Reflection Questions

Answer these before the debrief:

1. Which prompt scored higher? Was it the one you expected? If not — what does that tell you about your instincts vs. measured performance?

2. Look at the rows where the scores diverged the most between Prompt A and Prompt B. What specifically changed in those outputs? Was it correctness, completeness, safety, or fit?

3. The LLM-as-judge gave each output a score. Pick one score you **disagree with** — one where the judge got it wrong in your view. What did it miss, and why? What would a better rubric have caught?

4. You ran 5 test questions. How confident are you that these 5 questions are representative of the real task? What types of inputs did you *not* test that could change your conclusion?

5. If you were presenting these results to your manager to justify using Prompt B going forward — what would your one-line summary be, and what caveat would you add?

---

## Why This Matters

Most teams pick prompts the way they pick fonts — by feel, in a meeting, until someone wins an argument. What you just did is the alternative: define what good looks like, measure it consistently, and let the evidence decide.

This is P3 later in the course. When you build your knowledge agent, this is how you'll know whether it's working. Not "it seemed fine when I tested it" — a score, a dataset, and a comparison run you can reproduce.

---

## Quick Reference — Braintrust Concepts

| Term | What it means |
|------|--------------|
| **Project** | A workspace for one agent or application |
| **Dataset** | Your set of test inputs — the questions you'll evaluate against |
| **Prompt** | The system instruction you're testing |
| **Experiment** | One run of a prompt against a dataset — produces scores |
| **Scorer** | The evaluation function — LLM-as-judge, exact match, or custom code |
| **Trace** | The full record of one model call — inputs, outputs, latency, cost |
