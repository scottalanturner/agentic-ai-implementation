# Activity: Design Your Own Agent Workflow — With ChatGPT as Your Architect

**Module 5 | Estimated time: 25–35 minutes | Solo activity**

---

## What This Activity Is About

In this activity, you are going to do what a consultant or systems architect would do: sit down with an AI and work through what an agent workflow would actually look like for a real business task.

You're not building anything yet. You're designing — identifying which MCP servers would be involved, how agents would hand off work to each other, where a human needs to stay in the loop, and what could go wrong.

The output will be something you could realistically hand to a manager or drop into a project brief. It will include a workflow diagram (as an image you create in ChatGPT), a wiring guide, and governance notes — all produced collaboratively with ChatGPT.

---

## Learning Objectives

By the end of this activity, you will be able to:

- Describe a real business workflow in terms an AI agent can act on
- Identify which MCP servers or tool integrations a workflow would require
- Map out the roles of a coordinating agent, specialist agents, and human checkpoints
- Generate and review a workflow diagram as an image using ChatGPT
- Identify least-privilege, data exposure, and failure-handling considerations for an agent system

---

## Materials Needed

- A **ChatGPT account** — sign in or create an account at [ChatGPT](https://chatgpt.com). The free tier is sufficient for this activity.
- Something to write in for your reflection notes
- About 10 minutes of thought about your professional or organizational context before you start

---

## Background: What You're Actually Testing

When you run this prompt, ChatGPT will act as a workflow architect. It will ask you clarifying questions, make assumptions where you leave gaps, find relevant MCP servers, sketch an agent-to-agent design, help you visualize the workflow as an image, and flag governance concerns — all based on what you tell it about your context.

This is a realistic preview of how a practitioner might use an AI assistant in the early stages of an implementation project. The goal is not to get a perfect document. The goal is to see how the concepts from Module 5 — tool calls, MCP server selection, A2A handoffs, human checkpoints, least privilege — show up in a real design exercise.

Pay attention to:
- Which MCP servers ChatGPT recommends and why
- Where it places human-in-the-loop checkpoints
- What it flags as a permission risk
- Whether the workflow image matches your mental model of how the workflow would run

---

## Step-by-Step Instructions

### Step 1 — Prepare your context (5 minutes)

Before you open ChatGPT, decide on two things:

**Your role / organization:** You don't need to share anything confidential. Use a general description — your job title, the type of company or organization, and roughly what you do day to day. If you're a student and don't have a current job, use a past role, a student organization, or invent a plausible one (e.g., "Marketing coordinator at a mid-size regional nonprofit").

**Your business task:** Choose one realistic task that you think could benefit from an AI agent workflow. It should be something multi-step — not just "summarize a document," but something that touches more than one system or requires coordination. Examples:

- Drafting and routing a weekly project status report from data in multiple tools
- Reviewing job applications and scheduling first-round interviews
- Monitoring a product backlog and flagging items that have stalled
- Pulling together competitor pricing data and updating an internal tracker
- Reviewing client support tickets and escalating anything above a threshold

The more specific you are, the richer the output will be.

---

### Step 2 — Run the prompt (15–20 minutes)

Open a new conversation in [ChatGPT](https://chatgpt.com) and paste the full prompt below. Fill in the two bracketed sections before submitting.

---

> **Prompt — copy and paste this exactly, filling in your details:**

```
You are helping me design an agentic AI workflow using MCP servers and A2A-style agent communication.

My role / organization:
[Describe your job and workplace]

Business task:
[Invent or describe one realistic task that would benefit from an AI agent workflow]

Your job:

1. Clarify the workflow
Ask me up to 5 questions if needed. If I do not answer, make reasonable assumptions and state them.

2. Identify useful MCP servers
Find 3–5 MCP servers or tool integrations that could support this workflow. For each one, explain:
- What system it connects to
- What the agent would use it for
- What data it would read
- What action it might take
- What permission risks exist

3. Design the agent workflow
Create a workflow with:
- The human user
- The main coordinating agent
- Any specialist agents
- MCP servers/tools
- Any A2A handoffs between agents
- Human approval checkpoints

4. Create a workflow diagram
After you have described the workflow in text, use image generation in this chat to produce a single clear, business-friendly diagram image of the workflow (actors, agents, tools/MCP, handoffs, and human checkpoints). The image should align with the design above.

5. Document how it would be wired up
Explain, step by step:
- Which agent starts the process
- Which MCP server each agent calls
- What information moves between systems
- Where A2A handoffs happen
- Where the human reviews or approves
- What logs should be kept
- What should happen if something fails

6. Add governance notes
Include:
- Least-privilege permissions
- Sensitive data concerns
- Human-in-the-loop checkpoints
- Error/failure handling
- One metric for success
- One red flag that would stop deployment

Output format:
A. Use Case Summary
B. Assumptions
C. MCP Servers / Tool Integrations
D. Agent + A2A Design
E. Workflow Diagram (image — include the diagram image in this section)
F. Wiring Instructions
G. Governance / Guardrails
H. Success Metric
```

---

Answer any clarifying questions ChatGPT asks. If it makes assumptions you'd change, correct them. If the first pass at the diagram image looks off, tell it what's wrong and ask for a revised image — that back-and-forth is part of the learning.

---

### Step 3 — Review the output (5 minutes)

Once ChatGPT has produced the full A–H document (including the workflow image), read through it and write brief answers to these four reflection questions:

1. **MCP servers:** Which of the servers ChatGPT recommended surprised you? Which one would you be most hesitant to connect, and why?

2. **Workflow diagram:** Does the generated image match how you imagined the workflow? What's missing or different?

3. **Governance:** Look at the red flag ChatGPT identified. Do you agree with its choice? What would your red flag be?

4. **Real deployment:** If you were actually handed this design and told to implement it next quarter, what would be the first thing you'd need to verify before writing a line of code or making a single API connection?

---

## What to Submit

Save or copy the full A–H output ChatGPT produced (include the workflow image — e.g., download it from ChatGPT and attach it, or paste a link if your workflow allows), along with your four reflection answers. You may be asked to share during class discussion or submit both as a single document.


---

## A Note on the Workflow Image

ChatGPT can generate diagram-style images from your workflow description (look for image or “create an image” options in the interface, which may depend on your account and region). If the first image is too busy or misses a handoff, ask for a simpler version or a second image focused on one slice of the flow. Treat the image as a communication artifact for stakeholders, not as an executable specification — your text sections (especially wiring and governance) remain the source of truth.

---

*Activity for Module 5 — ISYS 398U Agentic AI Implementation | University of Richmond SPCS*
