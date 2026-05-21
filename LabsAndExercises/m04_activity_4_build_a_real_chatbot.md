# Activity 4 — Build a Real Chatbot in Chatbase

**Requires:** Free Chatbase account · chatbase.co · Google sign-in (no credit card)

---

## Overview

So far in Module 4 you've used NotebookLM to chat with your own documents. That's powerful, but it lives inside Google's app — only you can use it, and you can't drop it onto a website.

Chatbase is the productized version of the same idea. You feed it source material, it builds a chatbot you can test inside the dashboard, and it hands you back two artifacts a real business would actually use: a **public chat URL** and an **embed snippet** you can paste into a website's HTML.

You'll go from "research tool for me" to "agent on a page." No code, no credit card, no install.

---

## Goals

- Stand up a working knowledge chatbot from source material you choose
- Configure a simple system instruction that grounds the bot in your documents
- Test the bot at three points: clearly in scope, edge case, and clearly out of scope
- Walk out with a real chat URL and a real embed snippet — the same artifacts a small business would put on a website

---

## Step 1 — Create Your Free Account

Go to **chatbase.co** and click **Sign up**. The fastest path is Google sign-in. No credit card required for the free tier.

A couple of things to know about the free tier before you start:

- The free tier caps messages at roughly **30 per month per chatbot**. That's plenty for this activity, but if you keep iterating after class you'll hit the ceiling.
- The free tier also limits how much training data one bot can hold. Keep your first upload small — one short PDF or one URL is enough. You can always add more later.

---

## Step 2 — Pick Something to Feed the Bot

This is the open-ended part. The bot is only as interesting as the material you give it, so pick something you actually want to chat with.

Some ideas to spark thinking — pick from this list or bring your own:

- A company FAQ page or help center
- A public-facing policy document (HR handbook excerpt, terms of service, a city ordinance)
- A product manual or user guide
- An industry primer or whitepaper
- A hobby or sport guide — climbing routes, board game rules, a recipe collection
- A research paper, a long article, a Wikipedia page on a topic you know well
- Anything else you'd like to be able to ask questions of in plain English

You don't need anything proprietary or confidential. A single short PDF or one URL is plenty.

---

## Step 3 — Create the Chatbot and Add Your Source Material

In the Chatbase dashboard, click **New AI Agent** (or **Create new chatbot** — wording varies by week).

Chatbase will ask you to add **data sources**. You have three options. Use whichever fits what you picked in Step 2:

| Source type | When to use it |
|---|---|
| **File upload** | You have a PDF, DOC, or TXT file on your computer |
| **Website / URL** | You have a public web page or site — Chatbase will crawl it |
| **Text** | You want to paste raw text directly |

Add your source. Wait for Chatbase to finish processing — it usually takes under a minute for small inputs. The dashboard will show you a character or token count when it's done. That's how you know the bot has the content loaded.

---

## Step 4 — Configure the Bot

Give the bot a **name**. Anything short — "Policy Helper," "Trail Guide Bot," "Manual Assistant."

Find the **system prompt** or **instructions** field (Chatbase sometimes labels this "Persona" or "Instructions" depending on where you are in the UI). Replace whatever default is there with one sentence that grounds the bot in your material. For example:

> Answer only from the uploaded documents. If the answer isn't in the source material, say so plainly. Cite the source when possible.

That's it. You don't need to write a long persona. The goal here is to feel how a single sentence of instruction changes the bot's behavior.

Save your changes.

---

## Step 5 — Test the Bot With Three Questions

Open the chat preview inside Chatbase. Ask it three questions, in this order:

1. **A question your source material clearly covers.** The bot should answer it confidently and ideally cite the source.
2. **An edge-case question** — something near the boundary of what your material covers, but not directly stated. Watch how it handles ambiguity. Does it hedge? Does it answer anyway?
3. **A question completely unrelated to your source.** "What's a good recipe for lasagna?" if your bot is trained on city ordinances. Watch how it refuses — or doesn't.

Don't grade the bot harshly. The point is to see, in your own bot, the same three behaviors you've been watching all module: in-scope answers, edge cases, and refusals.

---

## Step 6 — Capture the Deployment Artifacts

This is the step that turns "research tool" into "deployable product."

In Chatbase, find the **Connect**, **Embed**, or **Share** section (again, naming varies — look for a link/share icon or the deployment tab).

Grab both of these and paste them into a personal scratch document (Word, Google Doc, a plain text file — whatever you'll be able to find again):

- **Chat URL** — the public link to the standalone chat page. Anyone with this link can use your bot.
- **Embed snippet** — the iframe or `<script>` tag you'd paste into a website's HTML to put the chat widget on a real page.

You don't have to actually embed it anywhere. The point is to *have* it. That snippet is the difference between a research tool and a deployable agent.

---

## Reflection Questions

Answer these in your head before the debrief — we'll talk through a few of them together:

1. What did your bot do on the **out-of-scope** question? Did it refuse, hallucinate, or hedge? What does that tell you about the one-sentence instruction you wrote?

2. The edge-case question is the most informative one. What did the bot do — and would you trust that behavior if this bot were live on a real website?

3. You now have a chat URL and an embed snippet. Imagine showing those to someone at your workplace, your school, or in a hobby community you're part of. Who in that group would actually use it, and what would they ask it?

4. What's missing from this bot before you'd be willing to put it in front of real users? Be specific — name one thing.

---

## Why This Matters

Before this activity, a deployable chatbot was something you assumed required a developer, a budget, and a six-week project plan. You just produced one in fifteen minutes with no money down.

That's the shift. The interesting question is no longer "can we build one?" — it's "what's worth building, and how do we know if it's any good?" Those are the questions the rest of the course is built around.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Bot won't answer at all | Confirm the source finished processing — Chatbase shows a character count when training is done |
| Bot answers from outside your documents | Re-check the system prompt. Add the phrase "Answer only from the uploaded documents" if it's not already there |
| Hit the 30-message monthly limit | You're done for this activity. Note the limit and move on |
| Embed snippet missing | Look under **Connect**, **Embed**, **Integrations**, or **Share** in the dashboard. It's there — Chatbase renames the tab from time to time |
| Sign-up loops or won't accept your account | Try Google sign-in if you didn't already, or use a different browser. If still stuck, flag the instructor |

---
