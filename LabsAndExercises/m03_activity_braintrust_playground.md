# Prompt Eval in Braintrust

**Requires:** Free Braintrust account · braintrust.dev

---

## Overview

You just watched companies like LangSmith and Google run evaluations at scale — thousands of outputs, automated scoring, regression tracking. This activity puts the same idea in your hands in under 30 minutes.

You'll write two versions of a system prompt for a task from your own work, run the same five test questions through both, and use Braintrust's LLM-as-judge scoring to see which prompt actually performs better. Not "feels better." Actually better — with numbers.

---

## Goals

- Experience the evaluation workflow firsthand: dataset → experiment → score → compare
- See how a small change in prompt wording produces measurable quality differences
- Build the habit of designing prompts to be testable, not just intuitive
- Walk away with a free account you can use on your own agent builds

---

## Step 1 — Create Your Free Account

Go to **braintrust.dev** and sign up. The free tier includes everything you need for this activity. No credit card required.

Once you're in, you'll land on your organization dashboard. Click **+ New Project** and name it something like `prompt-eval-[your initials]`.

![Project overview with left navigation](./m03_braintrust_images/01_project_overview.png)

The left navigation is your home base for the rest of this activity: **Datasets**, **Prompts**, **Scorers**, **Experiments**.

---

## Step 2 — Choose Your Task and Write Two Prompts

Pick a task you'd realistically want an agent to handle at work. Use one you identified in the Module 1 Discovery Interview or pick a new one. It should be:

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

Now write **two versions** of a system prompt for your chosen task. Make them meaningfully different — not just one word swapped. Think about what you learned in Module 2 about what makes a strong SOP: role, inputs, constraints, output format, escalation trigger.

**Prompt A** — your first instinct. Write whatever feels natural.

**Prompt B** — your improved version. Apply the SOP structure from Module 2. Be explicit about format, constraints, and what "done" looks like.

> ⚠️ **Critical: include `{{input}}` in both prompts.**
> Braintrust uses `{{input}}` as a placeholder that gets replaced with each row from your dataset when the experiment runs. Without it, the model never sees your test questions — it just runs your system prompt in a vacuum.
>
> Your prompt body should end with something like:
> ```
> Employee question: {{input}}
> ```
> Place it wherever the user's question would naturally appear in your prompt.

Write both prompts in a text editor before going into Braintrust.

---

## Step 3 — Set Up Your Evaluation in Braintrust

Complete all four sub-steps below **before** running the experiment in Step 4.

---

### 3a — Create Your Dataset

In the left nav, click **Datasets**.

![Datasets page showing the Create button](./m03_braintrust_images/02_datasets_create.png)

Click **Create** (top right) → **Empty dataset**. Name it `test-questions`.

> **Note:** The button says "Empty dataset", not "New Dataset".

You'll see a spreadsheet-style editor. Add **5 rows** — each row represents one test question you'll run through both prompts.

![Dataset row editor with input and expected columns](./m03_braintrust_images/03_dataset_row_editor.png)

Fill in **two columns** for each row:

| Column | What to put here |
|---|---|
| **`input`** | The test question itself — what a real user would type |
| **`expected`** | The correct or ideal answer — used by the Factuality scorer to grade responses |

Use realistic inputs, not edge cases you already know will fail. Think: what would an actual user submit?

> ⚠️ **Don't skip the `expected` column.** The Factuality scorer compares the model's output against this value to produce a score. If you leave it blank, every score will be meaningless.

---

### 3b — Create Your Scorer

In the left nav, click **Scorers**.

![Scorers page showing built-in templates](./m03_braintrust_images/04_scorers_templates.png)

Scroll to **"Or start from a template"** and click **Factuality** (for most tasks) or **Summary** (if your task is summarization).

> **Note:** "Quality" is not a scorer option in the current UI. Use **Factuality** for Q&A tasks and **Summary** for summarization tasks.

![Factuality scorer creation form](./m03_braintrust_images/05_scorer_save.png)

Give it a name (e.g., `factuality-scorer`) and click **Save**. It will now appear in the scorer dropdown when you create an experiment.

---

### 3c — Create Your Prompts

In the left nav, click **Prompts**, then **New Prompt**.

![Prompts page showing New Prompt button](./m03_braintrust_images/06_prompts_new.png)

You'll see the prompt editor. There are a few things to configure:

![Prompt editor with system message, {{input}}, slug field, and model selector](./m03_braintrust_images/07_prompt_editor.png)

**System message:** Paste in Prompt A. Make sure it ends with `{{input}}` (or has it embedded where the user question goes). The system message box is the top text area in the editor.

**Slug (name):** In the field at the top of the editor, type `prompt-a`. This is the identifier you'll select when creating the experiment.

**Model:** Click **Params** to open the parameters panel.

![Params panel showing model selector](./m03_braintrust_images/08_prompt_params.png)

> ⚠️ **Set the model before saving.** If the model field is blank or set to an unavailable model, your experiment will fail with a confusing "Request failed" error. Select **Claude Sonnet 4.5** (or the model your instructor specifies).

Click **Save prompt**.

Repeat for **Prompt B** — name it `prompt-b`.

---

## Step 4 — Run the Experiment

In the left nav, click **Experiments**.

![Experiments empty-state setup form](./m03_braintrust_images/09_experiments_form.png)

> **Note:** There is no "New Experiment" button. On your first visit, the experiment setup form appears directly on the page under **"Get started with experiments"** — fill it in there.

Complete the form:

1. **Experiment name** — type `prompt-a-run`
2. **Task** — click the `Task` toggle and switch to **Prompt**, then select `prompt-a`
3. **Dataset** — click **Select a dataset** and choose `test-questions`
4. **Scorers** — click **Select scorers** and choose the Factuality scorer you created in Step 3b
5. Click **Create**

The experiment will run in about 30–60 seconds.

> ⚠️ **If you see "Request failed":** go back to your prompt, click Params, and confirm the model is set to a valid option. Then re-run.

Once `prompt-a-run` completes, repeat the process for `prompt-b-run` — same dataset, same scorer, but select `prompt-b` as the prompt.

Now you have two experiments to compare.

---

## Step 5 — Compare and Read the Results

Click **Experiments** in the left nav. Open both runs side by side.

![Completed experiment results with per-row scores](./m03_braintrust_images/10_experiment_results.png)

Look at:

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

This is Project 3 later in the course. When you build your knowledge agent, this is how you'll know whether it's working. Not "it seemed fine when I tested it" — a score, a dataset, and a comparison run you can reproduce.

---

## Quick Reference — Braintrust Concepts

| Term | What it means |
|------|--------------|
| **Project** | A workspace for one agent or application |
| **Dataset** | Your set of test inputs and expected answers |
| **Prompt** | The system instruction you're testing — must include `{{input}}` |
| **Experiment** | One run of a prompt against a dataset — produces scores |
| **Scorer** | The evaluation function — Factuality compares output to expected answer |
| **`{{input}}`** | Placeholder replaced by each dataset row when the experiment runs |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "Request failed" when running | Go to Prompts → open your prompt → Params → set model to Claude Sonnet 4.5 |
| All scores are 0.00 | Check that your dataset has values in the `expected` column |
| Model never sees my questions | Make sure `{{input}}` appears somewhere in your prompt body |
| Can't find "New Experiment" button | On first use, the form is embedded on the Experiments page under "Get started with experiments" |
| Scorer not appearing in dropdown | Go to Scorers, click a template, save it — it must be created before it appears |
