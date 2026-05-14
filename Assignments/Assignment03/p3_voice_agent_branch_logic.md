# Project 3 — Voice Agent with Branch Logic

**Platform required:** ElevenLabs — [elevenlabs.io](https://elevenlabs.io) (free account)
**Submission:** A folder in your course GitHub repository — README write-up, screenshots, and your agent share link (see [Submission Requirements](#submission-requirements))

---

## Overview

In Project 1 you planned an agent and stress-tested it on paper. In Project 2 you gave it a memory grounded in source documents. In Project 3 you give it a voice — and a hand.

This is not a chatbot with audio added. A voice agent reasons about what the user needs, routes the conversation to the right knowledge and instructions for that specific situation, and hands off to a human when it reaches the edge of its competence. The routing is not vague ("the agent can answer many types of questions") — it is explicit: each branch has its own knowledge or tools, its own instructions, and a defined condition for entering and exiting it.

You will build three branches. One of them — the Order Lookup branch — is powered by a **tool**: a webhook that reaches out to a live system and pulls back real-time data, the same pattern you studied in Module 5. Another is grounded in your own documents. The third is your escalation path.

You will use your Project 1 Agent Card as the starting point. The same task, the same constraints, the same escalation trigger — now running as a voice conversation in ElevenLabs, with the ability to *act*, not just talk.

---

## What You Need Before You Start

- Your Project 1 Agent Card (you will adapt it, not replace it)
- A free ElevenLabs account — [elevenlabs.io/sign-up](https://elevenlabs.io/sign-up). No credit card required. If asked for Google Drive access during setup, decline — you do not need it.
- One to two real documents from your workplace or your agent's domain — policies, FAQs, product sheets, onboarding guides, or any content your agent would realistically draw from. You need at least one for your Branch 2 (your own domain branch). If you used real documents in Project 2, you can reuse them here.
- 60–75 minutes of focused work time
- A way to capture screenshots — built-in OS shortcuts work fine

**Watch this first — ElevenLabs' own walkthrough of webhook tools:**

- [Add Real-Time Data to Your Agent — Server Webhook Tools Explained](https://www.youtube.com/watch?v=pB33QxKN8P8&t=139s) — about 10 minutes. This is the exact technique you will use in Part 3 to wire up the Order Lookup tool. ElevenLabs embeds this same video in their own documentation.

**ElevenLabs documentation you will want open:**

- [ElevenLabs Agents overview](https://elevenlabs.io/docs/eleven-agents/overview)
- [Knowledge base setup](https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base)
- [Server tools — how an agent calls an external API](https://elevenlabs.io/docs/eleven-agents/customization/tools/server-tools)

**Navigation tip:** ElevenLabs changes its interface regularly. If a menu item or button is not where this document says it is, take a screenshot of your screen and ask Claude or ChatGPT: *"I'm in ElevenLabs trying to [do X]. Here's what my screen looks like — where do I find it?"* This is a legitimate skill in a field where tools update weekly.

---

## Part 1 — Voice Agent Design Document

Before touching ElevenLabs, write your design document. This is the planning artifact that drives everything you build in Parts 2 through 5.

### 1a — Adapt Your Project 1 Agent Card for Voice

Review your Project 1 Agent Card. Three things change when an agent operates by voice:

**Tone becomes conversational.** System prompt instructions that read well as text often sound robotic when spoken. Rewrite your Role and Task sections in plain, spoken English — shorter sentences, no bullet points in the spoken output, natural acknowledgment of what the user just said.

**Inputs become dynamic.** In a text agent, the user submits a complete request. In a voice agent, the conversation unfolds — the agent often needs to ask a follow-up question before it knows which branch to route to. Build that into your Task steps.

**Escalation becomes an audible handoff.** The escalation trigger from your Agent Card still fires — but now the agent must speak the handoff clearly. Revise your escalation trigger language to sound like something a real person would say out loud.

Write the revised version of your Agent Card with these three adaptations noted. You do not need to rewrite every section — only the sections that change for voice.

---

### 1b — Define Your Three Branches

Your agent has three branches. Each branch is a distinct conversation path with its own instructions and a clear condition for entering and exiting it. Two of the three are defined for you:

- **Branch 1 — Order Lookup.** Powered by a tool, not a document. When a customer asks about an order, this branch collects the order ID, calls a webhook to look up the order, and reads back what the customer ordered. Every student builds this same branch against the same test API — you will wire it up in Part 3.
- **Branch 2 — Your Domain Branch.** This is the branch that comes from your own Project 1 agent. It is grounded in a knowledge base document you provide. This is where your agent's real subject-matter lives.
- **Branch 3 — Escalation.** This fires when the user's need exceeds what Branches 1 and 2 can handle. It corresponds directly to the escalation trigger in your Project 1 Agent Card. It needs a clear spoken handoff message and an exit — no knowledge base, no tool.

Fill in this table:

| Field | Branch 1 — Order Lookup | Branch 2 — Your Domain | Branch 3 — Escalation |
|-------|-------------------------|------------------------|-----------------------|
| **Branch name** | Order Lookup | | Escalation |
| **Entry condition** — what does the user say or ask that routes them here? | Customer asks about the status or contents of an order, or gives an order number | | |
| **Powered by** — knowledge base, tool, or neither? | The Order Lookup webhook tool | A knowledge base document | Neither — spoken handoff only |
| **Instructions** — what specific behavior applies only in this branch? | | | |
| **Exit condition** — how does this branch end? (Resolved / Escalated / Return to router) | | | |

**What makes Branch 2 a good branch?** It should be meaningfully different from Branch 1 — different knowledge, different tone, different stakes. A good test: your Branch 2 should be something your Project 1 agent was actually designed to do.

---

### 1c — Router Design

Write a two to three sentence description of how the router (the entry node) works. What does the agent say first? What question does it ask or listen for to determine which branch to route to? What happens if the user's request is ambiguous?

The router does not need to be complex. One greeting, one routing question, three possible paths.

---

## Part 2 — Build the Voice Agent in ElevenLabs

### Step 1 — Create Your Agent

1. Go to [elevenlabs.io](https://elevenlabs.io) and sign in.
2. In the left navigation, find **Agents** (may also appear as **Conversational AI** depending on your interface version).
3. Click **Create agent** or **New agent**. Choose a blank template.
4. Give your agent a name that matches its purpose.
5. In the **System prompt** or **Agent instructions** field, paste your adapted voice SOP from Part 1a. This is the agent's global instructions — the router logic and shared constraints live here.

---

### Step 2 — Build Your Branch 2 Knowledge Base

ElevenLabs lets you attach knowledge base documents directly to your agent. Each document you add becomes a source the agent can retrieve from during a conversation.

1. Find the **Knowledge base** section in your agent settings. ([Documentation](https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base))
2. Add your Branch 2 document — this can be a file upload, a URL, or text pasted directly.
3. Name the knowledge base entry clearly — you will reference it in your Branch 2 instructions.

Branch 1 is powered by a tool, not a document — you will add that in Part 3. Branch 3 needs neither.

**What makes a good knowledge base document for a voice agent?**

- Clear, factual prose — not tables, not heavy formatting, not scanned PDFs if avoidable
- Focused on one topic — a 2-page policy document works better than a 20-page handbook
- Written in the language your users actually use — if they call it "PTO" not "annual leave," the document should too
- Real content from your actual workplace works best — the retrieval failure modes appear when the document is ambiguous or incomplete, and that is where the learning is

---

### Step 3 — Encode Branch Logic in Your System Prompt

ElevenLabs' conversation flow builder may or may not be available on the free tier depending on your interface version. Either way, the most reliable method for this assignment is to encode your branch logic directly in the system prompt. Here is a structure that works:

```
ROUTING LOGIC:
When the user asks about an order or gives an order number, follow Branch 1 (Order Lookup).
When the user's request is about [Branch 2 topic], follow Branch 2 instructions.
When [escalation condition from your Agent Card], follow Branch 3 instructions.
If you cannot determine which branch applies, ask one clarifying question before proceeding.

BRANCH 1 — Order Lookup:
When the user wants to check an order, ask for their order ID if they have not already given it.
Once you have the order ID, call the lookup_order tool.
Read back what the customer ordered in plain, conversational language.
If the tool returns no match, do not invent an order — say you could not find it and follow Branch 3.
Exit when: the order contents have been read back, or no match was found.

BRANCH 2 — [Branch name]:
[Specific instructions for this path. Reference the knowledge base document by name if possible.]
[Tone, format, constraints specific to this branch.]
Exit when: [resolved / user confirms / escalation needed]

BRANCH 3 — Escalation:
[Exact spoken handoff message.]
[Do not attempt to resolve — hand off immediately.]
Exit when: handoff is delivered
```

Write your actual branch instructions into this structure and paste it into your system prompt, below your agent's global role and context.

You will not be able to fully test Branch 1 until you add the tool in Part 3 — write the routing and Branch 1 instructions now, wire the tool next.

---

### Step 4 — Set the Voice

In the **Voice** section, choose any voice from the free library. Pick one that matches your agent's context — a customer service agent sounds different from an internal HR assistant.

---

## Part 3 — Add the Order Lookup Tool (Webhook)

This is the part that turns your agent from something that talks into something that *acts*. A **tool** lets your agent reach a live external system and pull back real-time data mid-conversation — the pattern from Module 5. You will add one webhook tool that looks up a customer's order.

Every student wires up the same tool against the same test API. It will not perfectly match every agent's domain — that is intentional. Standardizing one branch lets you focus on the mechanics of tool-calling, and lets the tool be graded consistently across the class.

**Watch first:** [Add Real-Time Data to Your Agent — Server Webhook Tools Explained](https://www.youtube.com/watch?v=pB33QxKN8P8&t=139s). It walks through exactly the steps below.

### Step 1 — Add the Webhook Tool

1. In your agent settings, on the **Agent** tab, find **Tools** → **Add Tool**.
2. Select **Webhook** as the Tool Type.
3. Configure it with these values:

| Field | Value |
|-------|-------|
| Name | `lookup_order` |
| Description | Looks up a customer's order by its order ID and returns what they ordered. Call this when the user asks about the status or contents of an order. |
| Method | GET |
| URL | `https://www.scottalanturner.com/api/order?order_id={order_id}` |

4. Add **one parameter**, with value type **LLM Prompt**:

| Data Type | Identifier | Description |
|-----------|------------|-------------|
| string | `order_id` | The customer's order ID — a four-digit number the customer reads aloud, for example 1001. |

5. **Authentication:** none. This is a public test endpoint — leave the authentication and headers empty.
6. Save the tool.

The `{order_id}` in the URL is a placeholder. ElevenLabs fills it in at call time with whatever order number the agent collected from the customer.

### Step 2 — Tell Your Agent How to Use the Tool

A tool that exists is not a tool that gets used. Your system prompt has to tell the agent *when* to call it and *what to do* with the answer. Confirm your Branch 1 instructions (from Part 2, Step 3) tell the agent to:

- Ask for the order ID if the customer has not given one
- Call `lookup_order` once it has the order ID
- Read back what the customer ordered, conversationally
- If no order is found, *not* invent one — say so and follow Branch 3

### Step 3 — Test the Tool

The valid test order IDs are **1001 through 1006**. Each one returns a real (test) order.

1. Open your agent's **Test** or **Try it** panel.
2. Say something like: *"I want to check on my order."* Confirm the agent asks for your order ID.
3. Give it a valid ID — pick any from 1001 to 1006. **Confirm the agent calls the tool and tells you what was ordered.**
4. Start again and give it an invalid ID — try `9999`. Confirm the agent does *not* invent an order; it should say it could not find that order and hand off.

Take a screenshot of the tool configuration panel, and a screenshot showing a successful tool call (the agent reporting the order contents).

---

## Part 4 — Publish and Run Structured Test Conversations

### Step 1 — Get Your Share Link

1. Look for a **Share**, **Publish**, or **Deploy** option in your agent settings.
2. Copy the agent's shareable URL. This link lets anyone talk to your agent in a browser without an ElevenLabs account.
3. Test the share link yourself before submitting — open it in a new browser tab and confirm it loads.

This link is a required part of your submission. If the link does not work at grading time, the build portion of your grade cannot be assessed.

### Step 2 — Run the Test Conversations

Run one structured test conversation per branch — three minimum. For each conversation, document:

- **Branch being tested**
- **What you said** — your opening message and any follow-up inputs, written out exactly
- **What the agent said** — paste or closely paraphrase the agent's responses
- **Did it route correctly?** — did the agent go to the right branch based on your input?
- **Did the knowledge base or tool activate?** — did the agent use the correct document or call the correct tool, or did it answer from general knowledge?
- **Did the branch exit correctly?** — did the conversation end (or escalate) as designed?
- **Pass or Fail** — and one sentence diagnosis

#### Test Conversation 1 — Branch 1 (Order Lookup)

Open your share link. Ask about an order and provide a valid order ID (1001–1006). Confirm the agent calls the tool and reads back what was ordered. Transcribe it.

#### Test Conversation 2 — Branch 2 (Your Domain)

Start a new conversation. Say something that should trigger your Branch 2 entry condition. Confirm the agent uses your knowledge base document. Let it run to exit. Transcribe it.

#### Test Conversation 3 — Escalation (Branch 3)

Start a new conversation. Say something that should trigger your escalation condition. Confirm the agent routes to Branch 3 and delivers the handoff message rather than attempting to resolve the request itself. Transcribe it.

#### Bonus Test — Routing Ambiguity

If you have time, run a fourth test where your opening message is genuinely ambiguous — it could belong to Branch 1 or Branch 2. Does the agent ask a clarifying question, or does it guess? Document the result. No pass/fail required — just honest observation.

---

## Part 5 — Voice and Tool Failure Analysis

After completing your test conversations, answer these three questions in two to four sentences each.

**1. What changed — and what broke — when you moved from a text agent (Project 2) to a voice agent (Project 3)?**

Be specific. Did the escalation trigger sound different when spoken? Did the branch routing feel natural or mechanical? Did the knowledge base perform differently than expected? Apply at least one voice-specific metric from Module 7 (word error rate, end-of-turn latency, hallucinated-name rate, refusal precision, or confirmation compliance) and name what you would measure if you had a dashboard.

**2. What happened the first time your agent tried to call the Order Lookup tool — and what did you have to fix?**

Tool calls rarely work on the first try. Did the agent fail to collect the order ID? Call the tool with the wrong value? Get a response and not know what to do with it? Describe the gap between your first attempt and a working tool call, and name what specifically closed it — the tool description, the parameter description, or your Branch 1 system-prompt instructions.

**3. Your Branch 3 is your last line of defense. After testing, do you trust it?**

Did the escalation fire when it should? Did it fire when it should not have — for example, on an invalid order ID? If you heard your agent deliver the Branch 3 handoff message to a real customer or colleague, would it sound professional and clear? What is the one thing you would change?

---

## Submission Requirements

Submit your work **in a folder in your course GitHub repository** — the same workflow you used for Project 1. Everything graders need must be reachable from that folder. Do not attach files to Blackboard; submit the link to the GitHub folder.

Your folder must contain:

1. **`README.md`** — your full write-up, in this order:
   - **Agent share link** — paste the URL at the very top so it is easy to find
   - **Voice Agent Design Document** — adapted Agent Card, branch table, router description (Part 1)
   - **Three test conversation transcripts** — with routing assessment, knowledge-base/tool check, and pass/fail diagnosis (Part 4)
   - **Voice and tool failure analysis** — all three questions answered (Part 5)
2. **Screenshots** — committed to the same folder (or a `screenshots/` subfolder) and referenced from your `README.md`:
   - Your agent's system prompt showing the branch logic
   - Your Branch 2 knowledge base
   - The `lookup_order` tool configuration panel
   - A successful tool call — the agent reporting an order's contents

Example folder layout:

```text
assignments/p3-voice-agent/
├── README.md
└── screenshots/
    ├── system-prompt.png
    ├── knowledge-base.png
    ├── tool-config.png
    └── tool-call-success.png
```

Commit and push your folder, then submit the **URL to that folder** on GitHub.

**Grading rubric:** see [rubric.md](rubric.md).

---

## A Note on Knowledge Base and Tool Quality

The most common reason a voice agent fails to retrieve correctly is not a platform problem — it is a document problem. If your knowledge base document is a dense 40-page handbook, the agent will retrieve the wrong section or nothing at all. If it is a clear, focused, 1–3 page document written in plain language, retrieval works reliably. If your agent gives generic answers instead of answers from your document, check the document first — not the system prompt.

The same logic applies to your tool. The most common reason a tool does not fire — or fires with the wrong value — is a vague name or a vague description. `lookup_order` with a plain-language description of when to call it and what `order_id` looks like will work far more reliably than a tool the agent has to guess about. Name things clearly, describe them in plain language, and the agent will use them correctly.
