# Prompt Eval in Braintrust

**Requires:** Free Braintrust account · braintrust.dev

---

## Overview

You'll write two versions of a system prompt for a task from your own work, run the same five test cases through both, and use Braintrust's "AI judge" scoring to see which prompt actually performs better. Not "feels better." Actually better — with numbers.

If some of the words below are new to you, that's expected. This activity assumes you have never done this before. Every step has an example you can copy and follow.

When you finish, **Part 2 at the end** explains how a real company uses a tool like this at full scale — which looks a little different from the simplified version you'll practice here.

---

## Goals

- Experience the evaluation workflow firsthand: dataset → experiment → score → compare
- See how a small change in prompt wording produces measurable quality differences
- Build the habit of designing prompts to be testable, not just intuitive
- Walk away with a free account you can use on your own agent builds

---

## Plain-English Words You'll See

Read this once before you start. You don't need to memorize it — you'll use each word in context below.

| Word | What it actually means |
|---|---|
| **System prompt** | The instructions you give the AI *before* it sees any input. Think of it as the AI's job description. |
| **Dataset** | A list of test cases — the text you feed the AI — plus the answer you *wish* it would give for each one. Like a quiz with an answer key. |
| **Scorer** | An automatic grader. It compares the AI's answer to your answer key and gives a score. |
| **Experiment** | One test run: take a prompt, feed it every case in your dataset, collect a score for each. |
| **`{{input}}`** | A fill-in-the-blank marker. When the test runs, Braintrust drops each of your test cases into this blank. |

---

## Step 1 — Create Your Free Account

Go to **braintrust.dev** and sign up. The free tier includes everything you need for this activity. No credit card required.

Once you're in, you'll land on your organization dashboard. Click **+ New Project** and name it something like `prompt-eval-` followed by your initials (for example, `prompt-eval-sjt`).

<!-- 📸 SCREENSHOT FOR SCOTT: The Braintrust dashboard right after sign-up, with the "+ New Project" button visible. -->
![Braintrust dashboard with the New Project button](./m03_braintrust_images/01_new_project.png)

<!-- 📸 SCREENSHOT FOR SCOTT: The project overview screen showing the left navigation (Datasets, Prompts, Scorers, Experiments). -->
![Project overview with left navigation](./m03_braintrust_images/02_project_overview.png)

The left navigation is your home base for the rest of this activity: **Datasets**, **Prompts**, **Scorers**, **Experiments**. You'll visit each one.

---

## Step 2 — Choose Your Task and Write Two Prompts

### 2a — Pick a task

Pick a task you'd realistically want an AI to handle at work. Use one you identified in the Module 1 Discovery Interview, or pick a new one.

The single most important rule for *this* activity: **pick a task where everything the AI needs is right there in the input.** The AI you're testing here has only two things in front of it — its instructions and the test case. It has no access to your company's files, your database, or the internet. So:

**Good tasks for this activity** — everything the AI needs is in the input:

- Read a customer support ticket and label how urgent it is
- Summarize a block of meeting notes into three bullet points
- Pull the action items out of a meeting description
- Decide whether a customer review is positive, negative, or neutral
- Draft a follow-up email from a short description of a meeting's outcome

**Tasks that will NOT work here** — they need knowledge the AI was never given:

- Answering questions about your company's policies (the AI doesn't have your handbook)
- Answering questions about your specific products, prices, or customers
- Anything where the correct answer lives in a document the AI can't see

If your task is in that second group, it's still a great agent idea — it just isn't testable in *this* simplified setup. Part 2 at the end explains how real companies handle exactly that kind of task. For now, pick something self-contained.

**Too vague to test at all:**

- "Be a helpful assistant"
- "Help me with my work"

For the rest of this activity, we'll follow one example all the way through so you can see what each step looks like. **Our example task: read a customer support ticket and label how urgent it is — High, Medium, or Low.** Wherever you see the example, swap in your own task.

### 2b — Understand what a system prompt is

A **system prompt** is the instruction block the AI reads before it ever sees the input. It sets the AI's role, its rules, and the format of its answer. You're going to write **two** versions of this and find out which one is better.

### 2c — Write two prompts

**Prompt A** is your first instinct — whatever feels natural. **Prompt B** is your improved version, using the SOP structure from Module 2: role, inputs, constraints, output format, and what to do when unsure.

**Important — every prompt has TWO parts.** When you build a prompt in Braintrust, you don't type it as one block. You split it into:

- A **System message** — the role and the rules. This is the instructions part.
- A **User message** — the line that holds `{{input}}`, the test case.

You need *both*. A system message by itself is not a valid request and the experiment will fail. (More on exactly where to type each part in Step 3c.)

Here is exactly what Prompt A and Prompt B might look like for our example task. Notice how much more specific Prompt B is.

**Example — Prompt A (first instinct):**

*System message:*

```
You read customer support tickets and say how urgent each one is.
```

*User message:*

```
Support ticket: {{input}}
```

**Example — Prompt B (improved, using the Module 2 SOP structure):**

*System message:*

```
You are a support triage assistant. You read one customer support ticket
and assign it an urgency level.

Use exactly one of these three labels:
- High: the customer cannot use the product, money is at risk, or a
  deadline is at stake
- Medium: something is broken or confusing, but the customer has a
  workaround
- Low: a question, a piece of feedback, or a minor cosmetic issue

Rules:
- If a ticket could fit two levels, choose the higher one.
- Decide based only on what the ticket says. Do not assume details that
  are not written.

Format your answer as exactly two lines:
Urgency: <High, Medium, or Low>
Reason: <one short sentence>
```

*User message:*

```
Support ticket: {{input}}
```

Notice that the User message is the *same* for both prompts. The only thing you're changing between Prompt A and Prompt B is the System message — the instructions. That's the level of difference you're going for: not one word swapped, but a real change in structure and clarity.

> ⚠️ **Critical: `{{input}}` goes in the User message, in both prompts.**
> `{{input}}` is a fill-in-the-blank marker. When the experiment runs, Braintrust replaces `{{input}}` with each test case from your dataset, one at a time. Without it, the AI never sees your test cases.
>
> It must live in a **User message**, not the System message. If you put everything in the System box, the run fails with an error about "at least one non-system message." Step 3c shows you exactly how to add the User message.

### 2d — Don't want to write the prompts from scratch? Use this

If you'd rather have a language model draft the two prompts for you, open ChatGPT, Claude, or Gemini and **copy-paste the prompt below.** Replace the text in `[BRACKETS]` with your own task, then send it.

```
I'm testing two versions of a system prompt for an AI assistant.

The assistant's job is: [DESCRIBE WHAT YOUR ASSISTANT DOES — for example,
"read a customer support ticket and label how urgent it is"]
My field or industry is: [YOUR FIELD — for example, "healthcare", "real
estate", "manufacturing", "education"]

Everything the assistant needs will be inside the input I give it — it has
no access to outside files or the internet.

Please write TWO prompts for this assistant. For EACH one, give me two
separate parts: a "System message" and a "User message".

Prompt A — a short, basic version. The System message is just a sentence or
two, the way someone would write it without much thought.

Prompt B — an improved version. The System message gives the assistant a
clear role, lists 3 to 4 rules or constraints, specifies the exact output
format, and says what it should do when it is unsure.

For BOTH prompts, the User message should be one short line that ends with
the placeholder. Keep the {{input}} part exactly as written, like this:
Input: {{input}}
```

Whether you wrote them yourself or used the generator, **paste both prompts into a plain text editor for now.** You'll move them into Braintrust in Step 3c.

---

## Step 3 — Set Up Your Evaluation in Braintrust

Complete all four sub-steps below **before** running the experiment in Step 4.

---

### 3a — Create Your Dataset

**First, what is a dataset?** A dataset here is just a small list of test cases, and for each one, the answer you'd consider correct. It's a quiz with an answer key. Braintrust will run the AI on every case on the list, then compare the AI's answers to your answer key.

In the left nav, click **Datasets**.

<!-- 📸 SCREENSHOT FOR SCOTT: The Datasets page with the "Create" button highlighted in the top right. -->
![Datasets page showing the Create button](./m03_braintrust_images/03_datasets_create.png)

Click **Create** (top right) → **Empty dataset**. Name it `test-cases`.

> **Note:** The button says "Empty dataset", not "New Dataset".

You'll see a spreadsheet-style editor. You'll add **5 rows** — each row is one test case.

<!-- 📸 SCREENSHOT FOR SCOTT: The empty dataset editor, before any rows are filled in, showing where to type. -->
![Empty dataset row editor](./m03_braintrust_images/04_dataset_empty_editor.png)

Each row has **two columns** to fill in:

| Column | What to put here |
|---|---|
| **`input`** | The text the AI works from — for our example, the full support ticket |
| **`expected`** | The correct or ideal answer — the AI grader uses this as the answer key |

Here's what 5 filled-in rows look like for our example ticket-triage task. (These are made-up support tickets — for your own task, *you* decide what the correct answer is.)

| input | expected |
|---|---|
| I was charged twice for my subscription this month, and I need the duplicate charge refunded before my rent comes out on Friday. | Urgency: High — The customer was double-charged and has a money deadline this week. |
| The export-to-PDF button doesn't work in Safari, but it works fine when I switch to Chrome. | Urgency: Medium — A feature is broken, but the customer has a working workaround. |
| Just wanted to say the new dashboard looks great. One small thing — the font on the settings page feels a little small. | Urgency: Low — This is positive feedback plus a minor cosmetic suggestion. |
| Our whole team of 40 people has been locked out of the platform since this morning, and we have a client demo at 2pm. | Urgency: High — An entire team cannot access the product and a deadline is at stake. |
| How do I change the email address on my account? I looked in settings but couldn't find it. | Urgency: Low — This is a how-to question with nothing broken. |

<!-- 📸 SCREENSHOT FOR SCOTT: The dataset editor with all 5 rows filled in, so students see the finished state. -->
![Dataset editor with five completed rows](./m03_braintrust_images/05_dataset_filled.png)

Use realistic test cases — the kind of thing that actually comes in — not trick cases you already know will fail.

> ⚠️ **Don't skip the `expected` column.** The grader compares the AI's answer to this value to produce a score. If you leave it blank, every score will be meaningless.

**Don't want to write the 5 test cases from scratch? Use this.** Open ChatGPT, Claude, or Gemini and copy-paste the prompt below. Replace the `[BRACKETS]`, send it, then copy its answers into your Braintrust dataset.

```
I'm building a small test set to evaluate an AI assistant.

The assistant's job is: [DESCRIBE WHAT YOUR ASSISTANT DOES — for example,
"read a customer support ticket and label how urgent it is"]
My field or industry is: [YOUR FIELD — for example, "healthcare", "real
estate", "manufacturing", "education"]

Please give me 5 realistic test cases for this assistant. A test case is
the text the assistant would receive — everything it needs should be inside
that text. For each test case, also give me the correct or ideal answer.

Put the output in a simple two-column table:
- Column 1: input  (the text the assistant receives)
- Column 2: expected  (the correct answer)

Keep each test case short and realistic — the kind of thing that actually
comes in, not a trick case.
```

> **Tip:** Read the answers the language model gives you before you paste them in. You are the expert on your task — fix anything in the `expected` column that isn't actually right.

---

### 3b — Create Your Scorer

**First, what is a scorer?** A scorer is an automatic grader. After the AI answers a test case, the scorer compares that answer to your `expected` answer and gives it a score between 0 and 1, where higher is better. You don't grade anything by hand — the scorer does it for every row. (Step 5 breaks down exactly how the Factuality score is calculated — read it once your results are in, because the numbers are less obvious than they look.)

In the left nav, click **Scorers**.

<!-- 📸 SCREENSHOT FOR SCOTT: The Scorers page, scrolled down to the "Or start from a template" section showing Factuality and Summary. -->
![Scorers page showing built-in templates](./m03_braintrust_images/06_scorers_templates.png)

Scroll to **"Or start from a template"** and click **Factuality** (use this for most tasks, including labeling and classification) or **Summary** (use this only if your task is summarizing something).

> **Note:** "Quality" is not a scorer option in the current interface. Use **Factuality** for most tasks and **Summary** for summarization tasks.

Give it a name (for example, `factuality-scorer`) and click **Save**.

<!-- 📸 SCREENSHOT FOR SCOTT: The scorer creation form with a name typed in and the Save button visible. -->
![Factuality scorer creation form](./m03_braintrust_images/07_scorer_save.png)

> ⚠️ **Check the scorer's model.** The Factuality scorer is itself an AI — it uses a model to do the grading, and that model is *separate* from the one your prompt uses. The template may default to a model your account can't reach (you'll see an error like *"unknown model or provider not configured"* when you run the experiment). Open the scorer's settings and set its model to one your account supports — the same model your instructor specified for the prompts is a safe choice.

Once it's saved, it will show up in the scorer dropdown when you create an experiment in Step 4.

---

### 3c — Create Your Prompts

Now you'll move the two prompts you wrote in Step 2 into Braintrust.

In the left nav, click **Prompts**, then **New Prompt**.

<!-- 📸 SCREENSHOT FOR SCOTT: The Prompts page with the "New Prompt" button highlighted. -->
![Prompts page showing the New Prompt button](./m03_braintrust_images/08_prompts_new.png)

You'll see the prompt editor. Four things to set, in order:

<!-- 📸 SCREENSHOT FOR SCOTT: The full prompt editor, labeled to point out (1) the system message box, (2) the "+ Add to prompt" button, (3) the slug/name field, (4) the Params button. -->
![Prompt editor with the system message, Add to prompt button, name field, and Params button](./m03_braintrust_images/09_prompt_editor.png)

**1. System message** — This is the big text box labeled **System**. Paste in *only the System message part* of Prompt A — the role and rules. **Do not** paste the `Support ticket: {{input}}` line here.

**2. Add the User message** — Click **"+ Add to prompt"** (below the System box). This adds a second message. Set its role to **User**, and paste the `Support ticket: {{input}}` line into it.

<!-- 📸 SCREENSHOT FOR SCOTT: The prompt editor after "+ Add to prompt" has been clicked, showing a second message with its role set to User and the {{input}} line in it. -->
![Prompt editor with a User message added below the System message](./m03_braintrust_images/10_prompt_user_message.png)

> ⚠️ **You must have both a System message and a User message.** If everything goes in the System box, the experiment fails with: *"Anthropic requires at least one non-system message."* The AI's instructions go in System; the `{{input}}` line goes in User.

**3. Name (slug)** — In the field at the top of the editor, type `prompt-a`. This is the label you'll pick later when you create the experiment.

**4. Model** — Click **Params** to open the parameters panel, then choose the model.

<!-- 📸 SCREENSHOT FOR SCOTT: The Params panel open, with the model dropdown set to the model you want students to use. -->
![Params panel showing the model selector](./m03_braintrust_images/11_prompt_params.png)

> ⚠️ **Set the model before saving.** If the model field is blank or set to a model that isn't available, your experiment will fail later with a confusing "Request failed" error. Select **Claude Sonnet 4.5** (or whichever model your instructor specifies).

Click **Save prompt**.

Now **do the whole thing again for Prompt B** — click **New Prompt**, paste Prompt B's System message into the System box, add a User message with the `Support ticket: {{input}}` line, name it `prompt-b`, set the model, and save. When you're done you should have two saved prompts: `prompt-a` and `prompt-b`.

---

## Step 4 — Run the Experiment

An **experiment** is one test run: it takes one prompt, runs it on every test case in your dataset, and collects a score for each answer. You'll run two experiments — one per prompt.

In the left nav, click **Experiments**.

<!-- 📸 SCREENSHOT FOR SCOTT: The Experiments page on first visit, showing the embedded "Get started with experiments" setup form. -->
![Experiments setup form](./m03_braintrust_images/12_experiments_form.png)

> **Note:** There is no "New Experiment" button on your very first visit — the setup form appears directly on the page under **"Get started with experiments"**. After you've run one experiment, look for a **"+ New experiment"** button, usually top-right.

Fill in the form:

1. **Experiment name** — type `prompt-a-run`
2. **Task** — find the `Task` toggle, switch it to **Prompt**, then select `prompt-a`
3. **Dataset** — click **Select a dataset** and choose `test-cases`
4. **Scorers** — click **Select scorers** and choose the `factuality-scorer` you made in Step 3b
5. Click **Create**

The experiment runs in about 30 to 60 seconds.

<!-- 📸 SCREENSHOT FOR SCOTT: An experiment in progress or just-completed, showing the rows being scored. -->
![Experiment running](./m03_braintrust_images/13_experiment_running.png)

> ⚠️ **If you see "Request failed":** go back to **Prompts**, open your prompt, click **Params**, and confirm the model is set to a valid option. Then run the experiment again.
>
> ⚠️ **If it gets stuck on scoring** (answers appear but no score shows up after a minute or two): the *scorer's* model probably isn't configured. Stop the run, go to Step 3b, and set the scorer's model. Then start a fresh run.

Once `prompt-a-run` finishes, **run it again for Prompt B.** Same steps, but name it `prompt-b-run` and select `prompt-b` as the prompt. Use the same dataset and the same scorer.

Now you have two experiments to compare.

---

## Step 5 — Compare and Read the Results

Click **Experiments** in the left nav. You'll see both runs listed. Open them so you can view them side by side.

<!-- 📸 SCREENSHOT FOR SCOTT: The experiments list showing prompt-a-run and prompt-b-run with their overall scores. -->
![Experiments list with two completed runs](./m03_braintrust_images/14_experiments_list.png)

<!-- 📸 SCREENSHOT FOR SCOTT: A single completed experiment opened up, showing per-row scores and the output column. -->
![Completed experiment with per-row scores](./m03_braintrust_images/15_experiment_results.png)

Three things to look at:

- **Overall score** — Which prompt scored higher on average? For example, you might see `prompt-a-run` at 0.62 and `prompt-b-run` at 0.88. That gap is your evidence.
- **Per-row scores** — Which specific test cases did each prompt handle better or worse? Look for rows where one prompt scored much higher than the other.
- **Output content** — Click into an individual row and read the actual answer the AI gave. Does the score match your gut? If not, why not?

You'll probably notice that Prompt A's answers are all over the place — different wording, no consistent label — while Prompt B's answers come back in the same tidy `Urgency: ... / Reason: ...` shape every time. That consistency is *why* it scores higher. That's the whole lesson in one screen.

### How the Factuality score works — and why a "correct" answer can still score low

The Factuality scorer is **not** a simple match / no-match check. It's an AI judge that sorts every answer into one of five buckets, and each bucket is worth a fixed score from 0 to 1:

- **0.0** — the answer **disagrees** with your expected answer (it's wrong)
- **0.4** — the answer is a **subset** of your expected answer (correct, but says less than the answer key)
- **0.6** — the answer is a **superset** of your expected answer (correct, but says *more* than the answer key)
- **1.0** — the answer is **fully consistent** with your expected answer (same content)
- **1.0** — the answer and the expected answer differ, but the difference **doesn't matter**

Here's the part that surprises everyone: an answer you would call completely correct can still score **0.6**. If the AI gives the right label and the right reasoning but *adds* a detail that isn't in your answer key, the judge files it under "superset" — "everything the reference said, plus extra I can't verify against anything" — and that's 0.6, not 1.0.

That is not the AI being wrong. It's the judge being strict about anything that goes beyond the answer key. Which points to the real lesson of this whole activity: **the score is a tool, not a verdict.** Always click into the rows and read the actual answers. A 0.6 might be a genuine miss — or it might be a great answer that got dinged for being thorough. Only reading it tells you which one.

> **Tip:** If you want fewer "superset" surprises, write your `expected` answers in the dataset to be as complete as a strong answer would be. The closer your answer key is to a full, good answer, the more often a good output lands in the 1.0 "fully consistent" bucket instead of the 0.6 "superset" one.

---

## Reflection Questions

Answer these before the debrief:

1. Which prompt scored higher? Was it the one you expected? If not — what does that tell you about your instincts versus measured performance?

2. Look at the rows where the scores were most different between Prompt A and Prompt B. What specifically changed in those answers? Was it correctness, completeness, consistency, or format?

3. The AI judge gave each answer a score. Pick one score you **disagree with** — one where you think the judge got it wrong. What did it miss, and why? What would a better answer key have caught?

4. You ran 5 test cases. How confident are you that these 5 are representative of the real task? What kinds of inputs did you *not* test that could change your conclusion?

5. If you were presenting these results to your manager to justify using Prompt B going forward — what would your one-line summary be, and what caveat would you add?

---

## Why This Matters

Most teams pick prompts the way they pick fonts — by feel, in a meeting, until someone wins an argument. What you just did is the alternative: define what good looks like, measure it consistently, and let the evidence decide.

This is exactly the kind of skill you'll lean on later in the course when you build your own agent. When you do, this is how you'll know whether it's working — not "it seemed fine when I tested it," but a score, a dataset, and a comparison run you can reproduce.

---

## Part 2 — How a Real Enterprise Actually Uses Braintrust

The activity you just did is the training-wheels version. It's real, but it's small on purpose. Here's what changes when an actual company uses a tool like this — and why the limits you ran into don't exist for them.

**They don't test a bare prompt — they test the whole system.** In the activity, your prompt had nothing but its own instructions and the test case to work from. That's why a task like "answer questions about company policy" doesn't work here — the AI was never given the policy, so it can't possibly know the answer. A real company doesn't have that problem, because they're not testing a lone prompt. They're testing a complete agent that *already* has the company handbook, the customer database, or a search tool wired into it. (Connecting an agent to your company's own documents is something you'll learn later in the course.) When Braintrust runs, it runs that whole system — so the agent can actually look up "15 vacation days," because looking things up is part of what it does. Braintrust just feeds it cases and grades the results. Nobody is pasting documents in by hand.

**They don't hand-write 5 test cases — they harvest hundreds from real life.** Your dataset was five examples you typed yourself. A real company builds its dataset from actual production traffic: real customer tickets, real support chats, real questions employees asked last month. And it grows over time — every time the agent gets something embarrassingly wrong in production, that example gets added to the dataset so it can never quietly break the same way again.

**They don't run it once — it runs constantly, like a smoke alarm.** You ran two experiments by hand. A company wires Braintrust into their development process so the whole evaluation re-runs automatically every time someone changes the prompt, swaps the model, or adjusts how the agent searches for information. The question they're answering isn't "is this good?" once — it's "did the change I just made make anything worse?" every single time. That is the real payoff: catching a quality drop before a customer does, not after.

**Their scorers are custom, not generic.** You used the built-in Factuality scorer. A real team writes scorers tuned to their business — "did the answer cite a real policy section," "did it stay under the required disclaimer length," "did it refuse the request it was supposed to refuse." The grader encodes *their* definition of good.

The thing to take away: the workflow is identical to what you just practiced — dataset, experiment, score, compare. Enterprises just run it bigger, on a real connected system instead of a bare prompt, with real data instead of hand-typed examples, and automatically instead of by hand. You've now seen the whole shape of it at small scale. Everything else is just volume.

---

## Quick Reference — Braintrust Concepts

| Term | What it means |
|------|--------------|
| **Project** | A workspace for one agent or application |
| **Dataset** | Your list of test cases and their expected answers |
| **Prompt** | The system instruction you're testing — must include `{{input}}` in a User message |
| **Experiment** | One run of a prompt against a dataset — produces scores |
| **Scorer** | The automatic grader — Factuality compares the answer to the expected answer |
| **`{{input}}`** | The fill-in-the-blank marker, replaced by each dataset row when the experiment runs |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "Anthropic requires at least one non-system message" | Your whole prompt is in the System box. Click "+ Add to prompt", set the new message's role to User, and move the `{{input}}` line into it. |
| "Request failed" when running | Go to Prompts → open your prompt → Params → set the model to Claude Sonnet 4.5 (or your instructor's model). |
| "Unknown model or provider not configured" | This is the *scorer's* model, not your prompt's. Open your scorer's settings (Step 3b) and set its model to one your account supports. |
| Experiment stuck — answers appear but no score | Same cause as above: the scorer's model isn't set. Stop the run, fix the scorer's model, start a fresh run. |
| All scores are 0.00 | Check that every row of your dataset has a value in the `expected` column. |
| The AI never sees my test cases | Make sure `{{input}}` appears in the User message of your prompt. |
| Can't find a "New Experiment" button | On your very first use, the form is embedded on the Experiments page under "Get started with experiments." After that, look for "+ New experiment" top-right. |
| Scorer not showing in the dropdown | Go to Scorers, click a template, save it — it must be created before it appears. |
