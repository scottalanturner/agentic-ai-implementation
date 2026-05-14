# P2 — Knowledge Agent in Notion

**Platform required:** Notion — [notion.com](https://www.notion.com) (free tier is sufficient)
**Submission:** One PDF or Word document uploaded to Blackboard, including the screenshots described in [Submission Requirements](#submission-requirements) below

---

## Overview

In Project 1 you planned an agent on paper. In Project 2 you give it a memory.

A knowledge agent does one thing well: it answers questions from a defined set of source documents — and it knows when to say *"I don't have that information."* That second behavior is where most chatbots fail. They generate confident-sounding answers from general training data when they should be admitting they don't know. The hardest part of building a knowledge agent is not making it answer questions — it is making it refuse to answer the wrong ones.

You will use your Project 1 Agent Card as the starting point. Same role, same constraints, same escalation trigger — now backed by real source content that the agent can quote from.

This is also the first half of a two-stage build. In Project 4, you will extend this same agent with tools and governance. For now, focus on getting the knowledge layer right — if the agent cannot reliably answer from its sources or refuse when it should, no amount of tooling later will save it.

---

## What You Need Before You Start

- Your Project 1 Agent Card (you will adapt it, not replace it)
- A Notion account on the free tier — sign up at [notion.com](https://www.notion.com) if you don't already have one
- **Three to five real documents from your workplace or your agent's domain** — policies, FAQs, onboarding guides, product sheets, project notes, or anything the agent would realistically draw from. Real content beats placeholder content every time — the failure modes you will study in Part 3 only appear when documents are ambiguous or incomplete.
- A way to capture screenshots — built-in OS shortcuts work fine

**Notion documentation you will want open:**

- [Notion AI overview](https://www.notion.com/help/notion-ai) — what Notion's agent can do
- [Notion Q&A](https://www.notion.com/help/notion-ai-faqs) — how Notion's agent answers questions from your workspace

**Navigation tip:** Notion updates its interface frequently. If a menu item is not where this document says it is, take a screenshot and ask Claude or ChatGPT: *"I'm in Notion trying to [do X]. Here's what my screen looks like — where do I find it?"* This is a legitimate skill in a field where tools change often.

---

## Part 1 — Agent Design Document

Write this before opening Notion. The design document is what separates a thoughtful deployment from clicking around until the agent answers something.

### 1a — Adapt Your Project 1 Agent Card for Grounded Knowledge

Review your Project 1 Agent Card. Three things change when an agent is grounded in source documents:

**The Task becomes a retrieval task.** The agent does not produce answers from general knowledge — it produces answers *from your documents*. Rewrite your Task section to make that explicit: *"Answer the user's question using only the content in the attached sources. If the answer is not in the sources, say so."*

**Constraints become refusal criteria.** Your Project 1 Agent Card had constraints like *"do not make commitments above X amount."* Add a new category: refusal criteria — what kinds of questions should the agent refuse to answer because they are out of scope of the documents, even if it could plausibly guess?

**Escalation becomes an audit-friendly handoff.** When the agent escalates, it should explain *why* — naming the gap in its knowledge or the threshold that was exceeded — so the human picking up the handoff knows what the agent saw.

Write the revised version of your Agent Card with these three adaptations noted. You do not need to rewrite every section — only the sections that change for grounded knowledge.

---

### 1b — Define Your Knowledge Sources

Your agent must draw from at least three distinct knowledge sources. Each source is a separate document, page, database, or uploaded file in Notion. Fill in this table:

| Source | What it contains | When the agent should use it | When the agent should NOT use it |
|--------|-----------------|------------------------------|---------------------------------|
| **Source 1** | | | |
| **Source 2** | | | |
| **Source 3** | | | |
| **(Source 4 / 5 — optional)** | | | |

**What makes a useful knowledge source for a Notion agent?**

- **Clear, factual prose** — not tables, not heavy formatting, not scanned PDFs if avoidable
- **Focused on one topic** — a 2-page policy document works better than a 20-page handbook
- **Written in the language your users actually use** — if they call it "PTO" not "annual leave," the document should too
- **Real content from your actual workplace works best** — placeholder content masks the retrieval failure modes that are the point of this assignment

**Acceptable source types in Notion:** plain pages, sub-pages, databases, and uploaded files (PDF, DOCX, TXT, MD). Pick whichever matches the content's native shape.

The fourth column matters most. *"When the agent should NOT use this source"* is what defines the boundary of the agent's competence. An HR policy document should never be the source for an IT password reset question — but a poorly scoped agent will reach for whatever is nearest. Make the boundaries explicit.

---

### 1c — Refusal Criteria

Write three to five specific refusal criteria — phrased as conditions, not topics.

**Examples of weak refusal criteria** (do not use):

- "Refuse questions about HR" — too broad; what does that even mean?
- "Refuse anything risky" — risky to whom?

**Examples of strong refusal criteria** (good):

- *"Refuse any question whose answer requires information not present in the attached sources, and say so explicitly."*
- *"Refuse any request to commit to a specific date, amount, or person — those decisions belong to a human."*
- *"Refuse any question about a department whose policies are not in my sources, and direct the user to the appropriate team."*

Your refusal criteria should be testable. You should be able to write a question and know whether the agent should refuse it before you ever run the test.

---

## Part 2 — Build the Knowledge Agent in Notion

### Step 1 — Build Your Knowledge Base

If your Notion workspace already has the documents you defined in Part 1b, you can use those. If not, create them now.

1. In your Notion sidebar, create a new page titled *Knowledge Sources* (or whatever fits your context).
2. Inside that page, add a subpage for each source from Part 1b. Paste or type the source content into each subpage.
3. If a source is naturally a database (e.g., a product catalog, a list of FAQs), create it as a database. Otherwise, plain pages work fine. If a source is a PDF or Word document you already have, you can upload it as a file inside the page.

**Screenshot 1:** Take a screenshot of your Knowledge Sources page showing all subpages. Include it in your submission.

---

### Step 2 — Create the Agent

1. In your Notion sidebar, find the **Agents** section (location and label may vary slightly — look for the "agent" or "AI agent" entry point).
2. Create a new agent. If Notion offers a starting point, choose the blank/empty option so your configuration is visible and intentional.
3. Name your agent something that matches its purpose. *Policy Answer Bot* and *Onboarding Q&A* are descriptive; *My Cool Agent* is not.

---

### Step 3 — Attach Your Knowledge Sources

1. In the agent's settings, find the panel that controls what the agent can access (commonly labeled **Tools and access** or similar).
2. Add the **Knowledge Sources** page you built in Step 1.
3. Set the access level to **Can view** (read-only) — the agent should not be able to modify your source documents.
4. If your version of Notion offers a **Web search** toggle, set it to **off**. The agent should answer only from the knowledge sources you provided — not from the open web.
5. If your version of Notion shows a **Triggers** option, leave it empty. Triggers are for scheduled or event-driven runs — you will configure them in Project 4.

**Screenshot 2:** Take a screenshot of the access panel showing your knowledge sources attached with **Can view** (read-only) scope. Include it in your submission.

---

### Step 4 — Write the Agent Instructions

In the agent's instructions field (sometimes labeled **Custom instructions**, **Agent instructions**, or **System prompt**), paste the revised Agent Card content from Part 1a, followed by your refusal criteria from Part 1c.

**Structure that works:**

```
ROLE:
[From your Agent Card — who the agent is, who it serves]

TASK:
Answer the user's question using only the content in the attached Knowledge
Sources. If the answer is not in the sources, say so explicitly and recommend
the user [escalation path from your Agent Card].

CONSTRAINTS:
[From your Agent Card — what the agent can never commit to]

REFUSAL CRITERIA:
[Your three to five criteria from Part 1c]

WHEN YOU ANSWER:
- Quote or paraphrase the specific source you used
- If multiple sources apply, name them
- If the sources disagree, surface the conflict — do not pick one silently

WHEN YOU REFUSE:
- Name the gap clearly: "That question is not covered in my sources" — not "I don't know"
- Direct the user to [escalation path]
```

Save the agent.

**Screenshot 3:** Take a screenshot of the agent's instructions field showing your saved system prompt. Include it in your submission.

---

## Part 3 — Grounded Q&A Test

Run five test questions through your agent and document each. The mix matters:

- **Two in-scope questions** — answers are clearly in your sources
- **Two edge-case questions** — answers are partially in your sources, or require combining two sources, or sit near a boundary
- **One deliberately out-of-scope question** — the answer is *not* in your sources, and the agent should refuse

For each test, capture **a screenshot of the conversation in Notion** showing your question and the agent's full response — and document the test in this table:

| Field | Notes |
|-------|-------|
| **Question category** | In-scope / Edge case / Out-of-scope |
| **What you asked** | Exact wording |
| **What the agent answered** | Paste or closely paraphrase |
| **Did it cite a source?** | Yes / No / Partial — and which source |
| **Was the answer correct?** | Yes / No / Partial — and what was wrong if anything |
| **Did it refuse appropriately?** | For the out-of-scope question, did it admit the gap and direct to escalation? |
| **Pass / Fail** | One sentence diagnosis |

Place each screenshot directly below its corresponding table entry. The screenshot is the proof the conversation actually happened — without it, the test cannot be verified.

**One mandatory test:** the out-of-scope question. Your agent must refuse it cleanly. If it generates a confident-sounding answer from general knowledge, that is the failure mode the entire assignment exists to catch — and the most important thing for you to document and try to fix.

**Debugging tip:** If a response surprises you, check whether your knowledge source documents are clear and focused. The most common cause of a wrong answer is a messy source, not a broken agent.

---

## Part 4 — Grounding Failure Analysis

After completing your test conversations, answer these two questions in two to four sentences each. Specific answers from your actual test results are graded higher than general observations.

**1. What grounding failure did you see — and which Module 4 failure mode does it match?**

Module 4 named four grounding failures: *stale document*, *wrong chunk retrieved*, *hallucinated citation*, *conflicting sources*. Which one (or which combination) did your agent exhibit? If your agent passed all five tests, describe the failure mode you would expect to see first if you doubled the size of one of your source documents.

**2. The refusal behavior is the hardest part of a knowledge agent. After testing, do you trust your refusal criteria?**

Did the agent refuse the out-of-scope question? Did it refuse anything it should have answered? If you handed your agent to a manager who knew nothing about how it was built, would the refusals sound professional, or would they sound like the agent is broken? What is the one refusal criterion you would tighten or loosen?

---

## Submission Requirements

Your submission is a single PDF or Word document uploaded to Blackboard. The document must contain, in order:

1. **Agent Design Document** — adapted Agent Card, knowledge source table, refusal criteria (Part 1)
2. **Build screenshots** — three required:
    - **Screenshot 1:** Knowledge Sources page showing all subpages (Part 2, Step 1)
    - **Screenshot 2:** Access panel showing knowledge sources attached with **Can view** scope (Part 2, Step 3)
    - **Screenshot 3:** Agent instructions field showing your saved system prompt (Part 2, Step 4)
3. **Five test conversations** — each one documented in the table format **and** accompanied by a screenshot of the actual conversation in Notion (Part 3)
4. **Grounding failure analysis** — both questions answered (Part 4)

**Grading rubric:** see [rubric.md](rubric.md).

---

## A Note on Source Quality

The most common reason a knowledge agent gives bad answers is not the agent — it is the source. A 40-page handbook with embedded tables and inconsistent terminology will produce bad retrievals no matter how well you write the instructions. A 1–3 page focused document in plain language will produce reliable retrievals even with mediocre instructions.

If your agent gives a generic-sounding answer when it should be quoting your source, the first thing to check is the source itself — not the instructions. Rewrite the messy section, save, and test again.

---

## A Note on What Comes Next

Project 4 will extend this same agent with tools and a full governance audit. The agent you build here is the foundation for that work — keep your Notion workspace, your agent, and your sources intact between Projects 2 and 4. Do not delete your sources or your agent when you submit.

---

## Resources

- [Notion AI overview](https://www.notion.com/help/notion-ai)
- [Notion Q&A](https://www.notion.com/help/notion-ai-faqs)
- Your Project 1 Agent Card — required starting point for Part 1
- Module 4 lesson slides — RAG pipeline, document quality, grounding failure modes
