# ROI Calculator

## Overview

A business case for an AI agent lives or dies on the numbers. Not because finance wants to be difficult — because "it saves time" doesn't survive a budget review. "It saves 1,400 hours per year at a fully loaded cost of $65/hour" does.

This exercise walks you through the three-lever ROI calculation for a real candidate use case from your own work. The math is simple. The discipline is figuring out which numbers you actually know vs. which ones you're making up.

---

## Goals

- Apply the three-lever ROI framework (time savings, error reduction, deflection) to a real use case
- Distinguish between defensible estimates and optimistic assumptions
- Produce a number you could present to a manager or include in a project proposal

---

## Step 1: Choose Your Use Case

Pick one task from your M01 Discovery Interview — ideally the one you're most likely to actually pursue. If you want to try a different one, choose a task that is:

- Repetitive (happens multiple times per week)
- Time-consuming enough that automation would matter
- Consequential enough that errors have a real cost

Write a one-sentence description of the task:

________________________________

---

## Step 2: Fill In the Worksheet

Work through each row. Use round numbers — the goal is directional accuracy, not precision.

### Lever 1: Time Saved

| Input | Your number |
|-------|------------|
| How often does this task happen? (times per week) | |
| How many minutes does it currently take per occurrence? | |
| What fraction of that time could AI handle? (50–70% is more realistic than 100%) | |
| Fully loaded hourly cost of the person doing it (rough rule: 1.3–1.5× base salary ÷ 2000 hours) | |
| **Annual time savings ($)** = (occurrences/week × 52 × minutes saved ÷ 60) × hourly rate | |

### Lever 2: Error Reduction *(skip if errors aren't a material concern)*

| Input | Your number |
|-------|------------|
| Current error rate for this task (rough %) | |
| What does one error cost? (rework time, customer impact, compliance exposure) | |
| Realistic error reduction if AI handles it | |
| **Annual error reduction savings ($)** = errors/year × cost per error × reduction rate | |

### Lever 3: Deflection *(use if this task involves answering questions or routing requests)*

| Input | Your number |
|-------|------------|
| How many of these requests hit a human per year? | |
| What fraction could be fully deflected to the agent without human review? | |
| Cost to serve one request when it hits a human (minutes × hourly rate) | |
| **Annual deflection savings ($)** = requests × deflection rate × cost to serve | |

---

## Step 3: Total and Gut-Check

Add up your levers. Write the annual estimate: **$_________**

Now ask yourself honestly:
- Which input number are you least confident in? Mark it with a *.
- What's the realistic low end if that number is half what you estimated?
- What's the realistic high end if adoption is higher than you assumed?

---

## Step 4: Sensitivity Test

Change your key uncertain input by 15 percentage points in each direction and recalculate.

| Scenario | Annual savings |
|----------|--------------|
| Conservative (your * input at −15%) | |
| Base case | |
| Optimistic (your * input at +15%) | |

This range — not just the base number — is what you'd report in a real business case.

---

## Reflection Questions

1. Which lever dominates your estimate — time savings, error reduction, or deflection? Does that match your intuition, or did the math surprise you?

2. You marked one input with a *. What would it actually cost (time, access, a pilot study) to get a more reliable number? Is that worth doing before you make a recommendation?

3. Imagine presenting your base-case number to your manager. What's the first question they'd ask? Do you have a good answer?

4. What's the biggest assumption baked into your estimate that you'd want to validate in a 30-day pilot before committing to a full rollout?

---

## Why This Matters

The gap between AI projects that get funded and AI projects that die in pilot purgatory is almost never the technology. It's whether someone built a defensible business case before asking for resources. This worksheet is the minimum viable version of that case. In M10, you'll use the same numbers to build the three-bullet executive pitch — metric, risk, ask.
