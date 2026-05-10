# Activity: Trace the ReAct Loop

## Overview

You just learned that AI agents don't just answer a question and stop — they run a loop. They Reason about what to do, take an Action, Observe the result, then go back around. This loop is what separates an agent from a chatbot.

This activity makes that loop concrete. You'll trace exactly what an agent would do — step by step — on a task from your own work. Then you'll find where it breaks.

---

## Goals

- Internalize the Reason → Act → Observe → Repeat cycle at the level of a specific task
- Identify the moments where a loop can stall, spiral, or silently fail
- Start thinking about your work in terms of agent-sized steps

---

## Step 1: Personalize Your Scenario

Before starting, open Claude or ChatGPT and paste the following. Fill in the brackets with your real situation.

```
I'm about to do an exercise tracing an AI agent through a multi-step task.
I work as [your role] at [your company or type of company, e.g. "a mid-size
logistics company" or "a healthcare system"]. My main responsibilities include
[2–3 things you actually do day to day].

Generate a realistic, specific task that an AI agent could theoretically handle
on my behalf — something that involves at least 3–4 steps, uses at least two
different tools or systems, and produces a concrete output. Write it as a
one-paragraph scenario I can use for a loop-tracing exercise.
```

Copy the scenario it generates. You'll use it for the rest of this activity.

---

## Step 2: Trace the First Loop Cycle

Using your scenario, fill in this table for the **first** ReAct cycle only.

| Stage | What happens in your scenario? |
|-------|-------------------------------|
| **Reason** | What does the agent figure out it needs to do first? What's the plan for step one? |
| **Act** | What specific action does it take? What tool, API, or system does it touch? What exactly does it send or request? |
| **Observe** | What comes back? What does the agent now know that it didn't know before? |
| **Next Reason** | Given what it just observed, what does the agent decide to do next? |

---

## Step 3: Find the Break Point

Now imagine one of these goes wrong. Pick one from the list below and describe what happens to your loop:

- **The action succeeds but returns an error code the agent doesn't recognize** — does it stop? retry? pretend it worked?
- **The observation is ambiguous** — two valid readings of the same result. Which one does the agent pick, and on what basis?
- **The tool call is made but takes 45 seconds to return** — what does the agent do while it waits? What if it times out?
- **The agent's next action would require a permission it doesn't have** — does it fail gracefully, ask a human, or try anyway?

Write 2–3 sentences describing exactly what breaks and why.

---

## Reflection Questions

Answer these before the debrief:

1. How many ReAct cycles do you think your scenario actually requires from start to finish? Walk through the count.

2. At which cycle is a human most likely to need to step in? What would trigger that intervention?

3. What's the difference between the agent *completing* the task and the agent *finishing successfully*? Is there a gap in your scenario?

4. If you were writing the system prompt for this agent, what would the escalation trigger look like — the exact condition that makes the agent stop and hand off to a human?

---

## Why This Matters

Every agent you encounter in production — in a vendor demo, in a job interview, in a business case — is running this loop under the hood. When something goes wrong, it went wrong in one of these four stages. Knowing how to trace a loop is how you stop treating agents like magic and start being able to evaluate them.
