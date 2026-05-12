# Activity 1 — Two Answers, Live

**Requires:** Free NotebookLM account (Google login) · notebooklm.google.com · Free ChatGPT account (OpenAI login) · chat.openai.com

---

## Overview

You've heard the line: a fluent answer is not the same as a correct one. This activity makes you feel the difference.

You'll pick a real source document, hand it to NotebookLM (which can only answer from what you give it), and then ask the exact same questions to ChatGPT (which has no idea what your document says). Same questions. Two very different kinds of answer. Your job is to notice where each one helps you and where each one quietly lies.

---

## Goals

- Experience a grounded answer side-by-side with an ungrounded one
- See what "custody of sources" looks like — being able to point at the file and section the answer came from
- Build the instinct that confidence is not evidence
- Set up the vocabulary you'll need next for diagnosing grounding failures

---

## Step 1 — Pick One Source Document

Choose **one** document that has clear, factual content. It should be something you can actually open and read, not a whole website. Pick from this list (or bring your own that fits the spirit):

- An HR policy or employee handbook — many cities, counties, and universities publish theirs publicly
- A product troubleshooting manual or user guide — manufacturer support pages or ManualsLib
- Software documentation for an app or library you use — official docs site or a GitHub README
- A government safety regulation or standard — OSHA, FDA, EPA, or NIH guidance
- A local government ordinance or municipal code — city or county website
- A sports league or recreational rule book — NCAA, USTA, NFL, FINA, etc.
- A public company annual report or 10-K — SEC EDGAR or company investor pages
- A nonprofit's bylaws or annual report

Download it (PDF is easiest) or copy the URL. You only need one document. Don't agonize over the pick — any of these will produce an interesting comparison.

---

## Step 2 — Load It Into NotebookLM

Go to **notebooklm.google.com** and sign in with a Google account.

Click **Create new notebook** (or **New**, depending on what you see). When prompted for a source, upload the PDF or paste the URL. Wait for NotebookLM to finish processing — you'll see the document appear in the sources panel on the left.

That's it. NotebookLM is now restricted to answering from that one file. Anything it says should be traceable back to a section of your document.

---

## Step 3 — Write Three Questions

Before you ask anything, write down three questions about your source:

1. **A question the source clearly answers.** Something a careful reader could find by skimming the document. Example for an employee handbook: "How many vacation days do new employees get in their first year?"

2. **A question the source partially answers.** Something the document touches but doesn't fully resolve. Example: "What happens to my unused vacation days if I leave mid-year?"

3. **A question the source does NOT answer.** Something plausible-sounding but outside the document's scope. Example: "What is the median tenure of employees at this company?"

Write all three down before you ask any of them. The point is to control the experiment.

---

## Step 4 — Ask NotebookLM

In your notebook, paste each question into the chat and submit. For each answer, capture:

- The text of NotebookLM's response
- Any citations it shows (numbered markers, source snippets, page references)
- What it says or refuses to say when the source can't help

NotebookLM will usually attach little citation markers you can click to see the exact passage it pulled from. Click at least one. That's the "custody" piece — you can verify the answer came from somewhere real.

---

## Step 5 — Ask ChatGPT the Same Three Questions

Open a new tab. Go to **chat.openai.com** and sign in with a free account.

**Do not upload the source document.** Don't paste passages from it either. You want ChatGPT working from whatever it already knows.

Start a new chat. Ask the same three questions, in the same order, with the same wording. Capture each answer.

> Note: If ChatGPT asks clarifying questions, answer briefly and keep going. If it refuses one of the questions outright, capture the refusal as the answer.

---

## Step 6 — Fill The Comparison Table

On one page (digital or paper), build a table with these columns:

| Question | Grounded answer (NotebookLM) | Ungrounded answer (ChatGPT) | Which was right | How you'd tell |
|---|---|---|---|---|

Fill one row per question. For the last column, be concrete: "I clicked the citation and the answer matched the policy," or "ChatGPT named a specific dollar amount that doesn't appear anywhere in the document."

You don't need full sentences in each cell. A phrase is fine. The point is to see all three rows next to each other on one page.

---

## Deliverable

1. The one-page comparison table — all three rows filled.
2. **One sentence** at the bottom of the page describing what you noticed about confidence vs. correctness in the two answers.

Bring both to the debrief (or post them in the discussion thread if you're working async).

---

## Reflection Questions

Answer these before the debrief — even one line each is fine:

1. For the question the source clearly answered: did both tools get it right? If yes, what was the meaningful difference between the two answers — even though both were "correct"?

2. For the question the source did NOT answer: what did each tool do? Did either one make something up? Did either one refuse? Which behavior is safer, and why?

3. Look at the most confident-sounding answer in your whole table. Was it the most correct one? If those two don't match, what does that tell you about how you should read AI answers in general?

4. Imagine you're the person who has to defend one of these answers to a skeptical boss, client, or auditor. Which tool's answer could you defend, and what specifically would you point at?

---

## Why This Matters

Most people decide whether to trust an AI answer based on how the answer *sounds*. Fluent, specific, confident — must be right. This is the single most dangerous habit in agentic AI.

A grounded answer can be wrong too. But when it is, you can find out — because the answer points at the file. An ungrounded answer that's wrong leaves no trail. There's nothing to audit, nothing to correct, no one to call.

The rest of Module 4 is about building agents that keep custody of their sources, and about spotting the specific ways that custody breaks down. You just felt the difference. Now we name the failure modes.
