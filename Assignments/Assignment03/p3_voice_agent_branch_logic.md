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

### Step 1 — Create Your Agent and Write a Slim System Prompt

1. Go to [elevenlabs.io/app/agents](https://elevenlabs.io/app/agents) and sign in.
2. In the left navigation, under the **Agents** heading, click the **+** icon (tooltip: *Create an agent*).
3. A "New agent" modal appears with three options: **Personal Assistant**, **Business Agent**, and **Blank Agent**. Choose **Blank Agent**.
4. A second modal — "Complete your agent" — appears. Enter an **Agent Name** that matches your agent's purpose (50 character limit). Leave the *Chat only* and *Procedures* toggles off. Click **Create Agent**.
5. You land on the per-agent view. The left nav now shows agent-scoped items: **Agent**, **Workflow**, **Branches**, **Knowledge Base**, **Analysis**, **Tools**, **Widget**, **Settings**.
6. You are on the **Agent** tab by default. Find the **System prompt** field in the upper-left of the page. The default content reads "You are a helpful assistant." — select all of it and replace it with a *slim* shared-role prompt: who the agent is, the conversational tone you want everywhere, and any rules that apply across every branch (for example: never ask for passwords).

   **Do not put routing logic or per-branch instructions here.** Those go in individual workflow nodes in Step 3. A good system prompt at this stage is two to four sentences.

7. Just below the system prompt is a **First message** field — the line the agent speaks first. Keep it broad enough to cover every branch you plan to build (a security-only greeting will confuse callers who want an order lookup).

> **What's already configured for you:** on the right side of the Agent tab, ElevenLabs has pre-selected a voice (Eric — Smooth, Trustworthy) and an LLM (Gemini 2.5 Flash). You'll change the voice in Step 4. The LLM choice can stay as-is unless you have a reason to change it.

---

### Step 2 — Create Your Branch 2 Knowledge Base Document

You will *upload* the knowledge base document now and *attach* it to the right branch node in Step 3. Doing it in two steps mirrors how ElevenLabs is structured: documents live in a shared library, then individual nodes pull from them.

1. In the left navigation (per-agent view), click **Knowledge Base**. ([Documentation](https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base))
2. Click **Add document** in the top right. A dropdown appears with three buttons at the bottom: **Add URL**, **Add Files**, and **Create Text**. Pick the one that matches your source:
   - **Create Text** — paste your document content directly. Easiest path if your KB content is already written. You'll be prompted for a **Text Name** and **Text Content**.
   - **Add Files** — upload a `.txt`, `.md`, `.pdf`, or `.docx` file from your computer.
   - **Add URL** — point the agent at a public web page.
3. Name the knowledge base entry clearly — you'll reference it by name when you attach it to a node.
4. Click **Create Text** (or the equivalent confirm button for the option you picked). The document now appears in the per-agent Knowledge Base list.

Branch 1 is powered by a tool, not a document — you'll add that in Part 3. Branch 3 needs neither.

**What makes a good knowledge base document for a voice agent?**

- Clear, factual prose — not tables, not heavy formatting, not scanned PDFs if avoidable
- Focused on one topic — a 2-page policy document works better than a 20-page handbook
- Written in the language your users actually use — if they call it "PTO" not "annual leave," the document should too
- Real content from your actual workplace works best — the retrieval failure modes appear when the document is ambiguous or incomplete, and that is where the learning is

---

### Step 3 — Build the Branches Visually in the Workflow Builder

This is where the multi-agent shape becomes literal. You will build your three branches as discrete **Subagent nodes** on a canvas, connected to a router by labeled transition edges. Each Subagent has its own conversation goal, its own (optional) knowledge base, and its own (optional) tools. You will be able to *see* the branches in a single screenshot.

**Why not just put routing logic in the system prompt?** It works in a quick demo, but it is not how a real organization sets up a multi-agent system. A monolithic prompt collapses everything into prose and gives you nothing to point at when a branch misbehaves. Discrete nodes let you isolate a failure to a single subagent, change its prompt without touching the others, and reason about handoffs as edges rather than rules buried in paragraphs.

#### 3a — Start from a template

1. In the left navigation, click **Workflow**. You'll see an empty canvas with a single **Start** node.
2. Click the **Templates** button in the toolbar at the top of the canvas. A "Workflow Templates" dialog opens with four patterns. Click **Qualification Flow** — the one described as *"Route users to specialized support based on their needs."*
3. The canvas fills in with a five-node scaffold: **Start → Qualification Agent → (Technical Support, Billing Support) → End** (with an `End call condition` edge between each branch and its End node). You will reshape this into your three-branch agent.

> **Skip the template?** You can also add nodes manually by clicking a node, then clicking the **+** icon that appears below it. The dropdown offers **Subagent**, **Say** (alpha), **Update state**, **Agent transfer**, **Phone number transfer**, **Tool**, and **End**. For this assignment, every branch is a **Subagent** node and every leaf is an **End** node. The template just saves you a few clicks.

#### 3b — Configure the Router (the entry subagent)

Click the **Qualification Agent** node. The right-hand inspector panel opens with five tabs: **General**, **Knowledge Base**, **Tools**, **Tests**, **Edges**.

1. **Rename the node.** At the top of the inspector, click the node title and rename it to **Router** (or whatever name from your Part 1c router design).
2. **General tab → Conversation goal.** Write what the router does — *greet, listen, decide which branch, ask one clarifying question if ambiguous, do not try to answer the caller's question itself*. This replaces the routing logic that would have lived in the system prompt.
3. Leave **Voice**, **LLM**, **Eagerness**, and the other fields at their *Using default* settings unless you have a reason to change them.

#### 3c — Configure your two pre-built branch Subagents

Click the **Technical Support** node (the left child of the router). Rename it to your Branch 2 name (whatever you decided in Part 1b — for example, *IR Intake*). In the **General** tab, write the branch's **Conversation goal** — the per-node instructions for this subagent, the same content you would have written into "BRANCH 2 — [name]" in a system prompt.

Then click the **Knowledge Base** tab for this node:

1. Toggle **Inherit knowledge base** OFF. This isolates the node so it only sees what you explicitly attach.
2. Click **Add document** under *Additional knowledge base*. A document picker appears.
3. Select the document you uploaded in Step 2. The node card on the canvas will now show a small `+1` indicator at the bottom — that's your visual confirmation the KB is attached.

Now click the **Billing Support** node (the right child of the router). Rename it to **Order Lookup**. In **General → Conversation goal**, write what the Order Lookup subagent does (ask for ID, call the tool, read back, do not invent an order if not found). Leave the **Knowledge Base** tab alone for this node — Order Lookup is powered by a tool, not a document. The tool itself will be attached in Part 3.

#### 3d — Add the third branch: Escalation

The template only ships with two branches. Add the third yourself:

1. Click the **Router** node. A small **+** icon appears below it. Click the **+**.
2. Pick **Subagent** from the dropdown. A new node appears, connected to the router by an unconfigured edge.
3. Rename the new node to **Escalation**.
4. In **General → Conversation goal**, paste the exact spoken handoff line from your Part 1a, plus a short instruction: *Do not attempt to resolve. Do not give the caller a phone number or email.* Then end the call.
5. Click the **+** below the Escalation node and pick **End** to give the branch an exit.

You should now have a router with three outgoing edges, three branch subagents, and three End nodes. Click the **Rearrange nodes** icon in the toolbar (then **Vertical**) if the layout has gotten tangled — it auto-tidies the canvas.

#### 3e — Configure the transition edges

The edges between Router and the three branches are how the workflow decides which subagent fires. Click the **Technical issue** label on the edge to the Branch 2 node. The inspector shows:

- **Transition type:** *LLM Condition* (leave as-is)
- **Label:** the short tag shown on the canvas — rename this to match Branch 2 (for example, *Security incident*)
- **LLM condition:** a one-paragraph description of *when this edge should fire*. Write it as a description of caller intent, not as a rule (the LLM uses this to decide). Be explicit about what should NOT route here (for example: do not route here if the caller describes an active attack — that goes to Escalation).

Repeat for the **Billing issue** edge → rename and describe for Order Lookup, and for the new edge to Escalation → name it something like *Active attack or asks for human* and describe the conditions from your Part 1b escalation row.

For the **Escalation → End** edge, set a simple condition: *the handoff message has been delivered.* (ElevenLabs requires every transition to have a condition or a non-empty rule, even when the path is effectively unconditional.)

When all three edges and the End transition are configured, the red `Errors` indicator at the top of the page should disappear and you'll see `Draft` instead — that's the workflow saying it's structurally valid.

---

### Step 4 — Set the Voice

Return to the **Agent** tab (left nav). On the right side of that page is a **Voices** section showing the currently selected voice (default: *Eric — Smooth, Trustworthy*). Click the voice row to open the voice picker, then choose any voice from the free library. Pick one that matches your agent's context — a customer service agent sounds different from an internal HR assistant. (The voice is set at the agent level and inherited by every Subagent node, unless a specific node overrides it.)

---

## Part 3 — Add the Order Lookup Tool (Webhook)

This is the part that turns your agent from something that talks into something that *acts*. A **tool** lets your agent reach a live external system and pull back real-time data mid-conversation — the pattern from Module 5. You will add one webhook tool that looks up a customer's order.

Every student wires up the same tool against the same test API. It will not perfectly match every agent's domain — that is intentional. Standardizing one branch lets you focus on the mechanics of tool-calling, and lets the tool be graded consistently across the class.

**Watch first:** [Add Real-Time Data to Your Agent — Server Webhook Tools Explained](https://www.youtube.com/watch?v=pB33QxKN8P8&t=139s). It walks through exactly the steps below.

### Step 1 — Add the Webhook Tool

1. In the per-agent left navigation, click **Tools** (it's a top-level item, not buried inside the Agent tab).
2. Click **Add tool** in the top right. A dropdown opens with three buttons: **Add webhook tool**, **Add client tool**, **Add integration tool**. Click **Add webhook tool**.
3. A configuration panel slides in from the right. Fill in these top fields:

| Field | Value |
|-------|-------|
| Name | `lookup_order` |
| Description | Looks up a customer's order by its order ID and returns what they ordered. Call this when the user asks about the status or contents of an order. |
| Method | GET *(this is the default)* |
| URL | `https://www.scottalanturner.com/api/order?order_id={order_id}` |

4. As soon as you paste the URL, ElevenLabs detects the `{order_id}` placeholder and **auto-creates a Path parameter** for it. Scroll down to the **Path parameters** section and you'll see one row already filled in — Data type: `String`, Identifier: `order_id`, Value Type: `LLM Prompt`. You only need to add the **Description**:

| Field | Value |
|-------|-------|
| Description | The customer's order ID — a four-digit number the customer reads aloud, for example 1001. |

5. **Authentication:** none. This is a public test endpoint — leave Authentication empty (the field reads "Workspace has no auth connections" by default, which is fine). Leave Headers empty too.
6. Leave all the other fields (Response timeout, Disable interruptions, Pre-tool speech, Execution mode, Tool call sound, Query parameters) at their defaults.
7. Click **Add tool** at the bottom right of the panel to save.

The `{order_id}` in the URL is a placeholder. ElevenLabs fills it in at call time with whatever order number the agent collected from the customer.

> **Tip — "Edit as JSON":** If the form gets in your way, the bottom-left of the tool panel has an "Edit as JSON" toggle that lets you paste the entire tool config as one blob. For this assignment the form is easier, but it's good to know the option exists.

### Step 2 — Attach the Tool to the Order Lookup Node

In a workflow build, tools are not handed to the whole agent — they are scoped to the specific node that should be allowed to call them. This is part of what makes the multi-agent shape useful: the IR Intake subagent literally *cannot* call the order lookup tool, so it cannot wander into the wrong branch.

1. In the left navigation, click **Workflow** to return to the canvas.
2. Click the **Order Lookup** node to open its inspector.
3. Click the **Tools** tab in the inspector.
4. Toggle **Inherit tools** OFF (this prevents the node from getting any agent-level tools you didn't explicitly attach here).
5. Click **Add tool** under *Additional tools*. A dropdown appears with your workspace tools listed at the top — pick **lookup_order**.
6. The node card on the canvas now shows a wrench icon with `+1` at the bottom — that's the visual confirmation the tool is attached here and only here.

> **Why not just leave Inherit tools on?** Because then every branch — including IR Intake and Escalation — would silently have access to `lookup_order`. A confused security-incident caller saying *"can you check my order"* could pull the IR Intake branch into a tool call it shouldn't make. Tight scoping prevents that.

You also need to confirm the Order Lookup node's **Conversation goal** (from Step 3c in Part 2) tells the subagent to:

- Ask for the order ID if the customer has not given one
- Call `lookup_order` once it has the order ID
- Read back what the customer ordered, conversationally
- If no order is found, *not* invent one — say so and transition to Escalation

### Step 3 — Test the Tool

The valid test order IDs are **1001 through 1006**. Each one returns a real (test) order — the data is toy/STEM-kit themed.

1. The test panel is the **right sidebar of the agent builder** — it's always open. The "Inline / Widget" tabs at the top switch the view; "Inline" is fine for testing. There's a microphone icon for voice and a text input at the bottom labeled "Send a message to start a chat."
2. Type something like: *"I want to check on my order."* and press Enter. Confirm the agent asks for your order ID.
3. Give it a valid ID — pick any from 1001 to 1006. **Confirm the agent calls the tool and tells you what was ordered.**
4. Click **End chat** at the top of the test panel, then **+ New conversation** to start fresh. Give the agent an invalid ID — try `9999`. Confirm the agent does *not* invent an order; it should say it could not find that order and follow your escalation branch.

Take a screenshot of the tool configuration panel, and a screenshot showing a successful tool call (the agent reporting the order contents).

---

## Part 4 — Publish and Run Structured Test Conversations

### Step 1 — Publish and Get Your Share Link

ElevenLabs splits this into two actions: you have to **publish** the agent first, then construct the share URL. The two are not the same button.

1. **Publish.** Click **Publish** in the top right of the agent builder. A "Review Changes" diff modal appears showing what changed since the last published version. Optionally add a version description, then click **Publish** at the bottom right of the modal to confirm. The "Draft" badge at the top should disappear once publishing succeeds.
2. **Find your Agent ID.** Click the **⋯ (Agent actions)** menu at the very top right of the page (to the right of the Publish button). The dropdown's first row shows **Agent ID: agent_XXXXXXXXXXXXX...** — click the copy icon to copy it. (The "Share agent" option in this same menu is for sharing with workspace teammates, *not* for public sharing — don't confuse the two.)
3. **Construct the public share URL** by pasting the Agent ID into this template:

   ```text
   https://elevenlabs.io/app/talk-to?agent_id=YOUR_AGENT_ID_HERE
   ```

   That URL opens a no-sign-in page with a "Call AI agent" button and a "Switch to Chat" option in the top right. This is the link to submit.
4. **Test the share link before submitting** — open it in a new browser tab (or a private window so you're not logged in as yourself) and confirm it loads and the agent responds.

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
   - The **Workflow canvas** showing all three branches visible — router, three branch subagents, edges with labels, and the End nodes
   - Your **Branch 2 subagent's Knowledge Base tab** showing the attached document
   - Your **Order Lookup subagent's Tools tab** showing `lookup_order` attached
   - The **`lookup_order` tool configuration panel** (from the agent's Tools page) showing the URL, parameter, and description
   - A **successful tool call** — the agent reporting an order's contents during a test conversation

Example folder layout:

```text
assignments/p3-voice-agent/
├── README.md
└── screenshots/
    ├── workflow-canvas.png
    ├── branch2-knowledge-base.png
    ├── order-lookup-tool-attached.png
    ├── tool-config.png
    └── tool-call-success.png
```

Commit and push your folder, then submit the **URL to that folder** on GitHub.

**Grading rubric:** see [rubric.md](rubric.md).

---

## A Note on Knowledge Base and Tool Quality

The most common reason a voice agent fails to retrieve correctly is not a platform problem — it is a document problem. If your knowledge base document is a dense 40-page handbook, the agent will retrieve the wrong section or nothing at all. If it is a clear, focused, 1–3 page document written in plain language, retrieval works reliably. If your agent gives generic answers instead of answers from your document, check the document first — not the system prompt.

The same logic applies to your tool. The most common reason a tool does not fire — or fires with the wrong value — is a vague name or a vague description. `lookup_order` with a plain-language description of when to call it and what `order_id` looks like will work far more reliably than a tool the agent has to guess about. Name things clearly, describe them in plain language, and the agent will use them correctly.
