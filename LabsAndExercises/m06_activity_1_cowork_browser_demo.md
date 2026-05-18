# Activity 1 — Browser Agent Live: Watch It Work, Then Drive It Yourself

---

## A Note Before You Begin — Choose Your Path

This activity asks you to watch an AI agent take real-time control of a web browser and complete a research task. The original walkthrough was built around the Claude Cowork desktop app plus the Claude in Chrome extension, but **Cowork is a paid product and you are not required to buy anything for this course**. Several other tools do the same thing.

Pick whichever of the three paths below fits your situation. All three earn full credit — the observation skills are what we are grading, not the brand of tool.

**Path A — A paid browser-agent product, if you already have access to one.** Any of these will work:

- **Claude Cowork desktop app + Claude in Chrome extension** — the original setup this activity was written around (Anthropic; paid subscription).
- **ChatGPT Agent** — the agentic mode inside a paid ChatGPT account; this was previously called Operator and is the closest direct equivalent to Cowork-controls-Chrome.
- **Perplexity Comet** — an AI-native browser; the agentic features require a paid Perplexity plan.
- **Google Gemini in Chrome** — browser-agent features available on some paid Google AI plans.
- Any other commercial product that can take live control of a Chrome or Edge tab on your machine and complete a multi-step research task.

**Path B — A free or open-source browser-agent option.** No subscription needed:

- **OpenAI Codex** — primarily an agentic coding tool, but the current version can browse the web during a task. Free tier available.
- **Browser Use** — open source; runs locally on your computer. Some setup required.
- **Manus AI** — free tier with limited monthly credits; web-based.
- Any other free agent you can find that drives a real browser end-to-end.

**Path C — Watch the recorded walkthrough.** If you can't install or run any of the above, watch the demo video posted on Blackboard alongside this assignment, and complete the observation log and reflection questions based on what you see in the video. If you take Path C, replace Part 2 with the short written alternative at the bottom of this document.

If you are unsure which path fits your situation, pick Path C. We care about what you notice, not which tool you used.

---

## Overview

Reading about browser agents is one thing. Watching one navigate a real web page — deciding what to click, what to read, what to skip — is something else entirely. And doing it yourself, with a task you designed, is where the learning actually sticks.

In this activity you will give a browser agent access to a Chrome (or equivalent) tab, watch it complete a structured research task across multiple live websites, and then design and run your own task. Along the way you will observe exactly the things the module warned you about: the agent reading the page before it reasons, the moments where it slows down or asks for help, and the difference between a task that's a good fit for browser automation and one that isn't.

This is not a demo you watch. It is a demo you operate (unless you are on Path C, in which case it is a demo you observe closely — same observation skills, smaller scope).

---

## Goals

- Experience a browser agent completing a multi-step research task in real time
- Observe how the agent perceives a web page (what it reads, what it misses, how it decides what to do next)
- Notice at least one moment where the agent struggles, pauses, or behaves unexpectedly
- Design and run your own browser task and reflect on what happened (Paths A and B)

---

## Before You Start — Get Your Tool Connected

The exact setup depends on which path you chose. Here are the general steps, which apply across most browser-agent products:

1. Install or open the product you picked from Path A or B above.
2. If it uses a browser extension (Claude in Chrome, for example), install the extension from the Chrome Web Store first, then sign in.
3. Open the agent's interface and look for a control that says something like **Connect to browser**, **Take over this tab**, or **Browser mode**. Turn it on.
4. Confirm that the agent can see and control your browser before you start — most tools show a small status indicator or a confirmation banner.

If you can't get the connection working after fifteen minutes, switch to Path C. Time spent troubleshooting is not the point of this activity.

---

## Part 1 — Watch the Agent Complete a Research Task

You will give your browser agent a specific, multi-step research task. Your job during this part is to **watch and take notes**, not to intervene. Let the agent work.

### The task — copy and paste this prompt into whichever tool you're using:

> I need you to use my browser to research current API pricing for two AI providers: Anthropic (claude.ai or anthropic.com) and OpenAI (openai.com). For each provider, find the current price per million input tokens and per million output tokens for their fastest/cheapest model and their most capable model. Build a simple comparison table with your findings. Note the date you retrieved this information, because pricing changes frequently.

**If you are on Path C**, watch this same task being completed in the demo video and answer the observation log from the video instead.

**While the agent is working, fill out the observation log below in real time. Don't wait until it's done.**

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

## Part 2 — Design and Run Your Own Task (Paths A and B only)

Now it is your turn to give the agent a browser task. The task should involve at least two steps (navigate somewhere, then do something with what you find) and should relate to something genuinely useful for your work, your field, or this course.

**Task design rules:**

- Keep it to public websites only — do not ask the agent to log into accounts, access internal systems, or touch anything with personal credentials.
- The task should have a clear, checkable output (a table, a list, a short summary — something you can evaluate).
- Choose something where you can independently verify at least one fact the agent returns.

### Task design worksheet

Answer these three questions before you run the task:

1. **What is the task?** (Write it as a one-sentence prompt you will give the agent)

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

## Part 2 — Written Alternative (Path C only)

If you watched the demo video instead of running the agent yourself, replace Part 2 with this short written exercise.

Imagine you have just been given access to a browser agent at work. Describe a task you would actually want it to do for you — keep it to public websites only, no logins. Then answer:

1. **What is the task?** (One-sentence prompt)
2. **What output would "done" look like?**
3. **What is one specific fact you would manually verify before trusting the rest?**
4. **What is the worst thing that could go wrong if the agent silently got something wrong on this task?** (Two or three sentences)

---

## Reflection Questions

Answer these after completing the parts above.

1. The module described three ways agents perceive a web page: accessibility tree, DOM snapshot, and screenshot. Based on what you observed (live or on video), which of these do you think the agent was primarily using — and what made you think that?

2. You named one specific fact to verify before running your task (or, on Path C, one fact you would verify). Was it correct, or how confident are you it would be? What does that single data point tell you about how much you should trust the rest of the output?

3. If someone on your team said "great, let's run this every morning automatically," what is the first governance question you would ask before approving that?

---

## Why This Matters

Most people who evaluate browser agents never actually watch one work. They see polished demos, read blog posts, or take a vendor's word for it. The observation log you just filled out is more valuable than any of those sources — because it is grounded in a real task, on real websites, with real output you could check.

The skepticism you built in this activity is the skill. An AI product that looks good in a demo can still fail in production the first time the website updates its layout, adds a CAPTCHA, or changes a field label. You now know what that looks like, because you watched the agent navigate real uncertainty — not a scripted walkthrough.
