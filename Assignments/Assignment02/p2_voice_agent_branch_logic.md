# P2 — Voice Agent with Branch Logic

**Worth:** 15% of final grade  
**Assigned:** End of Module 4  
**Due:** Before Module 6  
**Platform required:** ElevenLabs — [elevenlabs.io](https://elevenlabs.io) (free account)  
**Submission:** One PDF or Word document + your ElevenLabs agent share link, uploaded to Blackboard

---

## Overview

In P1 you planned an agent and stress-tested it on paper. In P2 you build it — as a live, talking voice agent.

This is not a chatbot with audio added. A voice agent reasons about what the user needs, routes the conversation to the right knowledge and instructions for that specific situation, and hands off to a human when it reaches the edge of its competence. The routing is not vague ("the agent can answer many types of questions") — it is explicit: each branch has its own knowledge base, its own instructions, and a defined condition for entering and exiting it.

You will use your P1 Agent Card as the starting point. The same task, the same constraints, the same escalation trigger — now running as a voice conversation in ElevenLabs.

---

## What You Need Before You Start

- Your P1 Agent Card (you will adapt it, not replace it)
- A free ElevenLabs account — [elevenlabs.io/sign-up](https://elevenlabs.io/sign-up). No credit card required. If asked for Google Drive access during setup, decline — you do not need it.
- Two to three real documents from your workplace or your agent's domain — policies, FAQs, product sheets, onboarding guides, or any content the agent would realistically draw from. One document per branch.
- 30–40 minutes of focused work time

**ElevenLabs documentation you will want open:**
- [ElevenLabs Agents overview](https://elevenlabs.io/docs/eleven-agents/overview)
- [Knowledge base setup](https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base)
- [RAG — how ElevenLabs retrieves from your knowledge base during conversations](https://elevenlabs.io/docs/conversational-ai/customization/knowledge-base/rag)

**Navigation tip:** ElevenLabs changes its interface regularly. If a menu item or button is not where this document says it is, take a screenshot of your screen and ask Claude or ChatGPT: *"I'm in ElevenLabs trying to [do X]. Here's what my screen looks like — where do I find it?"* This is a legitimate skill in a field where tools update weekly.

---

## Part 1 — Voice Agent Design Document

Before touching ElevenLabs, write your design document. This is the planning artifact that drives everything you build in Parts 2 and 3.

### 1a — Adapt Your P1 Agent Card for Voice

Review your P1 Agent Card. Three things change when an agent operates by voice:

**Tone becomes conversational.** System prompt instructions that read well as text often sound robotic when spoken. Rewrite your Role and Task sections in plain, spoken English — shorter sentences, no bullet points in the spoken output, natural acknowledgment of what the user just said.

**Inputs become dynamic.** In a text agent, the user submits a complete request. In a voice agent, the conversation unfolds — the agent often needs to ask a follow-up question before it knows which branch to route to. Build that into your Task steps.

**Escalation becomes an audible handoff.** The escalation trigger from your Agent Card still fires — but now the agent must speak the handoff clearly. Revise your escalation trigger language to sound like something a real person would say out loud.

Write the revised version of your Agent Card with these three adaptations noted. You do not need to rewrite every section — only the sections that change for voice.

---

### 1b — Define Your Three Branches

Your agent must have at least three branches. Each branch is a distinct conversation path with its own knowledge source, its own instructions, and a clear condition for entering and exiting it.

For each branch, fill in this table:

| Field | Branch 1 | Branch 2 | Branch 3 (Escalation) |
|-------|----------|----------|-----------------------|
| **Branch name** | | | |
| **Entry condition** — what does the user say or ask that routes them here? | | | |
| **Knowledge base** — what document or content does this branch draw from? | | | |
| **Instructions** — what specific behavior applies only in this branch? | | | |
| **Exit condition** — how does this branch end? (Resolved / Escalated / Return to router) | | | |

**Branch 3 must be your escalation path.** It fires when the user's need exceeds what Branches 1 and 2 can handle. It should correspond directly to the escalation trigger in your P1 Agent Card. Branch 3 does not need a knowledge base — it needs a clear spoken handoff message and an exit.

**What makes a good branch split?**
The branches should differ meaningfully — different knowledge, different tone, different stakes. A good test: if you swapped the knowledge base documents between Branch 1 and Branch 2, the agent would break. If swapping them would not matter, the branches are not distinct enough.

---

### 1c — Router Design

Write a two to three sentence description of how the router (the entry node) works. What does the agent say first? What question does it ask or listen for to determine which branch to route to? What happens if the user's request is ambiguous?

The router does not need to be complex. One greeting, one routing question, three possible paths.

---

## Part 2 — Build in ElevenLabs

### Step 1 — Create Your Agent

1. Go to [elevenlabs.io](https://elevenlabs.io) and sign in.
2. In the left navigation, find **Agents** (may also appear as **Conversational AI** depending on your interface version).
3. Click **Create agent** or **New agent**. Choose a blank template.
4. Give your agent a name that matches its purpose.
5. In the **System prompt** or **Agent instructions** field, paste your adapted voice SOP from Part 1a. This is the agent's global instructions — the router logic and shared constraints live here.

---

### Step 2 — Build Your Knowledge Bases

ElevenLabs lets you attach knowledge base documents directly to your agent. Each document you add becomes a source the agent can retrieve from during a conversation.

1. Find the **Knowledge base** section in your agent settings. ([Documentation](https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base))
2. Add your Branch 1 document — this can be a file upload, a URL, or text pasted directly.
3. Add your Branch 2 document.
4. If Branch 3 has a reference document, add it as well. If Branch 3 is a pure escalation with no knowledge lookup, skip it.
5. Name each knowledge base entry clearly — you will reference them in your branch instructions.

**What makes a good knowledge base document for a voice agent?**
- Clear, factual prose — not tables, not heavy formatting, not scanned PDFs if avoidable
- Focused on one topic — a 2-page policy document works better than a 20-page handbook
- Written in the language your users actually use — if they call it "PTO" not "annual leave," the document should too
- Real content from your actual workplace works best — the RAG failure modes appear when the document is ambiguous or incomplete, and that is where the learning is

---

### Step 3 — Encode Branch Logic in Your System Prompt

ElevenLabs' conversation flow builder may or may not be available on the free tier depending on your interface version. Either way, the most reliable method for this assignment is to encode your branch logic directly in the system prompt. Here is a structure that works:

```
ROUTING LOGIC:
When the user's request is about [Branch 1 topic], follow Branch 1 instructions.
When the user's request is about [Branch 2 topic], follow Branch 2 instructions.
When [escalation condition from your Agent Card], follow Branch 3 instructions.
If you cannot determine which branch applies, ask one clarifying question before proceeding.

BRANCH 1 — [Branch name]:
[Specific instructions for this path. Reference the knowledge base document by name if possible.]
[Tone, format, constraints specific to this branch.]
Exit when: [resolved / user confirms / you have provided the answer]

BRANCH 2 — [Branch name]:
[Specific instructions for this path.]
[Tone, format, constraints specific to this branch.]
Exit when: [resolved / user confirms / escalation needed]

BRANCH 3 — Escalation:
[Exact spoken handoff message.]
[Do not attempt to resolve — hand off immediately.]
Exit when: handoff is delivered
```

Write your actual branch instructions into this structure and paste it into your system prompt, below your agent's global role and context.

---

### Step 4 — Set Voice and Test Settings

1. In the **Voice** section, choose any voice from the free library. Pick one that matches your agent's context — a customer service agent sounds different from an internal HR assistant.
2. Find the **Test** or **Try it** button — usually in the top right of the agent builder.
3. Run a quick sanity check: say something that should route to Branch 1 and confirm the agent responds appropriately. If it does not, adjust the system prompt routing logic and try again.

---

### Step 5 — Get Your Share Link

1. Look for a **Share**, **Publish**, or **Deploy** option in your agent settings.
2. Copy the agent's shareable URL. This link allows anyone to talk to your agent in a browser without an ElevenLabs account.
3. Test the share link yourself before submitting — open it in a new browser tab and confirm it loads.

This link is a required part of your submission. If the link does not work at grading time, the build portion of your grade cannot be assessed.

---

## Part 3 — Structured Test Conversations

Run one structured test conversation per branch — three conversations minimum. For each conversation, document:

- **Branch being tested**
- **What you said** — your opening message and any follow-up inputs, written out exactly
- **What the agent said** — paste or closely paraphrase the agent's responses
- **Did it route correctly?** — did the agent go to the right branch based on your input?
- **Did the knowledge base activate?** — did the agent use content from the correct document, or did it generate a response from general knowledge?
- **Did the branch exit correctly?** — did the conversation end (or escalate) as designed?
- **Pass or Fail** — and one sentence diagnosis

---

### Test Conversation 1 — Branch 1

Open your share link. Say something that should trigger your Branch 1 entry condition. Let the conversation run until the branch exits. Transcribe it.

---

### Test Conversation 2 — Branch 2

Start a new conversation. Say something that should trigger your Branch 2 entry condition. Let it run to exit. Transcribe it.

---

### Test Conversation 3 — Escalation (Branch 3)

Start a new conversation. Say something that should trigger your escalation condition. Confirm the agent routes to Branch 3 and delivers the handoff message rather than attempting to resolve the request itself. Transcribe it.

---

### Bonus Test — Routing Ambiguity

If you have time, run a fourth test where your opening message is genuinely ambiguous — it could belong to Branch 1 or Branch 2. Does the agent ask a clarifying question, or does it guess? Document the result. No pass/fail required — just honest observation.

---

## Part 4 — Voice-Specific Failure Analysis

After completing your test conversations, answer these two questions in two to four sentences each.

**1. What changed — and what broke — when you moved from a text agent (P1) to a voice agent (P2)?**

Be specific. Did the escalation trigger sound different when spoken? Did the branch routing feel natural or mechanical? Did the knowledge base perform differently than expected? This is not a general reflection on voice AI — it is about your specific agent.

**2. Your Branch 3 is your last line of defense. After testing, do you trust it?**

Did the escalation fire when it should? Did it fire when it should not have? If you heard your agent deliver the Branch 3 handoff message to a real customer or colleague, would it sound professional and clear? What is the one thing you would change?

---

## Submission Requirements

Your submission is a single PDF or Word document plus your agent share link. The document must contain, in order:

1. **Voice Agent Design Document** — adapted Agent Card, branch table, router description (Part 1)
2. **Screenshots** — at least two: (a) your agent's system prompt in ElevenLabs, (b) your knowledge base showing the documents you uploaded
3. **Agent Share Link** — paste the URL at the top of the document, before anything else, so it is easy to find
4. **Three test conversation transcripts** with routing assessment, KB check, and pass/fail (Part 3)
5. **Voice-specific failure analysis** — both questions answered (Part 4)

---

## Grading Rubric

| Section | Points | What earns full credit |
|---------|--------|----------------------|
| Voice Agent Design Document | 30 | Branch table complete with distinct entry/exit conditions; KB plan matches branches; router logic described; voice adaptations from P1 are specific and explained |
| ElevenLabs Build | 20 | Share link works at grading time; system prompt shows branch logic structure; knowledge base documents visible in screenshot; at least two distinct KB documents present |
| Test Conversations | 35 | All three branches tested; transcripts show routing working; KB activation noted; escalation branch documented; pass/fail diagnosis is specific |
| Voice Failure Analysis | 15 | Both questions answered with specifics from actual test results — not generic observations |
| **Total** | **100** | |

---

## A Note on Knowledge Base Quality

The most common reason voice agents fail to retrieve correctly is not a platform problem — it is a document problem. If your knowledge base document is a dense 40-page handbook, the agent will retrieve the wrong section or nothing at all. If it is a clear, focused, 1–3 page document written in plain language, retrieval works reliably.

If you find your agent giving generic answers instead of answers from your document, the first thing to check is the document itself — not the system prompt. Rewrite the messy parts, re-upload, and test again.

---

## Resources

- [ElevenLabs Agents overview](https://elevenlabs.io/docs/eleven-agents/overview)
- [Knowledge base documentation](https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base)
- [RAG in ElevenLabs](https://elevenlabs.io/docs/conversational-ai/customization/knowledge-base/rag)
- [Deploying enterprise knowledge to voice agents](https://elevenlabs.io/blog/deploying-enterprise-knowledge-to-voice-agents) — ElevenLabs blog post on knowledge base best practices
- [ElevenLabs free tier sign-up](https://elevenlabs.io/sign-up)
- Your P1 Agent Card — required starting point for Part 1
- M04 lesson slides — RAG pipeline, document quality, retrieval failure modes
- M07 lesson slides — voice agent design, spoken UX, IVR patterns
