# Activity 1 — Browser Agent Live: Watch It Work, Then Drive It Yourself

**Requires:** Claude Cowork desktop app · Claude in Chrome extension (free, install from the Chrome Web Store)

---

## Overview

Reading about browser agents is one thing. Watching one navigate a real web page — deciding what to click, what to read, what to skip — is something else entirely. And doing it yourself, with a task you designed, is where the learning actually sticks.

In this activity you will give Claude Cowork access to your Chrome browser, watch it complete a structured research task across multiple live websites, and then design and run your own task. Along the way you will observe exactly the things the module warned you about: the agent reading the page before it reasons, the moments where it slows down or asks for help, and the difference between a task that's a good fit for browser automation and one that isn't.

This is not a demo you watch. It is a demo you operate.

---

## Goals

- Experience a browser agent completing a multi-step research task in real time
- Observe how the agent perceives a web page (what it reads, what it misses, how it decides what to do next)
- Notice at least one moment where the agent struggles, pauses, or behaves unexpectedly
- Design and run your own browser task and reflect on what happened

---

## Before You Start — Install the Chrome Extension

1. Open Chrome and go to the **Chrome Web Store**
2. Search for **Claude** — look for the extension published by Anthropic
3. Click **Add to Chrome** and confirm the installation
4. Open the Cowork desktop app. In the conversation panel, you should see an option to connect to your browser. Follow the on-screen prompt to link the extension.
5. When you see confirmation that Cowork is connected to Chrome, you are ready.

**If you already have the extension installed:** Open Cowork, start a new session, and confirm the browser connection is active before proceeding.

---

## Part 1 — Watch Claude Complete a Research Task

You will give Claude a specific, multi-step research task. Your job during this part is to **watch and take notes**, not to intervene. Let the agent work.

### The task — copy and paste this prompt into Cowork:

> I need you to use my browser to research current API pricing for two AI providers: Anthropic (claude.ai or anthropic.com) and OpenAI (openai.com). For each provider, find the current price per million input tokens and per million output tokens for their fastest/cheapest model and their most capable model. Build a simple comparison table with your findings. Note the date you retrieved this information, because pricing changes frequently.

**While Claude is working, fill out the observation log below in real time. Don't wait until it's done.**

### Observation log — Part 1

| Observation point | What you saw |
|-------------------|-------------|
| How did the agent start? (What did it do first before navigating anywhere?) | |
| How many separate web pages did it visit to complete the task? | |
| Was there a moment where it slowed down, re-read something, or seemed uncertain? Describe it. | |
| Did it ask you for anything, or did it work autonomously the whole time? | |
| Did the final table look accurate to you? Did you spot anything it got wrong or skipped? | |
| One thing that surprised you about watching it work: | |

---

## Part 2 — Design and Run Your Own Task

Now it is your turn to give Claude a browser task. The task should involve at least two steps (navigate somewhere, then do something with what you find) and should relate to something genuinely useful for your work, your field, or this course.

**Task design rules:**
- Keep it to public websites only — do not ask Claude to log into accounts, access internal systems, or touch anything with personal credentials
- The task should have a clear, checkable output (a table, a list, a short summary — something you can evaluate)
- Choose something where you can independently verify at least one fact Claude returns

### Task design worksheet

Answer these three questions before you run the task:

1. **What is the task?** (Write it as a one-sentence prompt you will give Claude)

2. **What output are you expecting?** (What would "done" look like?)

3. **What is one specific fact in the output you will manually verify?** (Name the fact before you run the task, not after)

---

Now run your task. Use the same observation log format as Part 1:

| Observation point | What you saw |
|-------------------|-------------|
| How did the agent start? | |
| Did it take the path you expected, or did it navigate differently than you predicted? | |
| Did it succeed, partially succeed, or fail? | |
| What was the quality of the output — accurate, incomplete, or wrong in some specific way? | |
| When you manually verified the one fact you named above — was it correct? | |
| If you ran this task again tomorrow, what do you think would be different? | |

---

## Deliverable

Submit the following:

1. **Your completed Part 1 observation log** (the pricing research task)
2. **Your task design worksheet** (the three pre-run questions)
3. **Your completed Part 2 observation log** (your own task)
4. **One paragraph** — no more than 150 words — answering this question: Based on what you saw, is the task you designed in Part 2 a good fit for browser automation, a bad fit, or somewhere in the middle zone? Use the three deployment questions from the module (Is there an API? Is it reversible? What does one mistake cost?) to frame your answer.

---

## Reflection Questions

Answer these after completing both parts:

1. The module described three ways agents perceive a web page: accessibility tree, DOM snapshot, and screenshot. Based on what you observed, which of these do you think Claude was primarily using — and what made you think that?

2. You named one specific fact to verify before running your task. Was it correct? What does that single data point tell you about how much you should trust the rest of the output?

3. If someone on your team said "great, let's run this every morning automatically," what is the first governance question you would ask before approving that?

---

## Why This Matters

Most people who evaluate browser agents never actually watch one work. They see polished demos, read blog posts, or take a vendor's word for it. The observation log you just filled out is more valuable than any of those sources — because it is grounded in a real task, on real websites, with real output you could check.

The skepticism you built in this activity is the skill. An AI product that looks good in a demo can still fail in production the first time the website updates its layout, adds a CAPTCHA, or changes a field label. You now know what that looks like, because you watched the agent navigate real uncertainty — not a scripted walkthrough.

