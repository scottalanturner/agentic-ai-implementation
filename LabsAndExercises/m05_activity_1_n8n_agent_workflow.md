# Activity: Build a Tool-Calling Agent in n8n

**Format:** In-class activity
**Time:** 20–25 minutes  
**Requires:** A web browser · Free n8n account (created during this activity)

---

## Overview

You have seen how an agent decides which tool to call, sends a structured request, and uses the response to build its answer. Now you are going to build that yourself.

n8n is a free, browser-based workflow tool with a visual canvas. It has a native AI Agent node that supports tool calling — the same pattern as an MCP-enabled agent — and it comes with built-in tools that require no API keys. You will wire an agent to two tools, run a prompt that requires both, and watch the execution trace show you exactly what happened at each step.

This is the closest you can get to a live MCP workflow without setting up a server.

---

## Goals

- Build a working tool-calling agent workflow from scratch, in a visual canvas
- Observe an execution trace that shows the agent routing to a tool, receiving data, and constructing a response
- Connect the visual to the architecture concepts from class: the agent as coordinator, tools as external capabilities, routing as a decision

---

## Step 1 — Create a Free n8n Account (3 min)

1. Go to [n8n.io](https://n8n.io) and click **Get started free** or **Start for free**.
2. Sign up with your email address. No credit card required.
3. You will land in the n8n cloud workspace. If you see a starter workflow or tutorial prompt, dismiss it — you are starting fresh.

---

## Step 2 — Create a New Workflow (1 min)

1. Click **+ New workflow** (or the **+** button in the left sidebar).
2. Give it a name: `Tool-Calling Agent — Module 5`.
3. You will see a blank canvas with a **+** node in the center. This is where you start building.

---

## Step 3 — Add a Chat Trigger (2 min)

1. Click the **+** on the canvas (or **Add first step**).
2. Search for **Chat** and select **When chat message received**. This is your input node — it receives the user's message and starts the workflow.
3. You do not need to configure anything here. Leave the defaults.

You should now see one node on your canvas labeled something like **When chat message received**.

---

## Step 4 — Add an AI Agent Node (3 min)

1. Click the **+** button that appears to the right of your Chat trigger node.
2. Search for **AI Agent** and select it.
3. In the AI Agent settings panel:
   - **Chat Model:** Click the dropdown and select **OpenAI** (or whichever model provider is pre-configured in your n8n account). If prompted to add credentials, select the built-in option or ask the instructor.
   - Leave all other settings at their defaults for now.

> **If no model is pre-configured:** n8n may offer a built-in OpenAI integration or a free trial model. Choose whatever is available. If you are stuck, type your error message into Claude: *"I'm setting up an AI Agent node in n8n and can't connect a model — what are my options on the free plan?"*

---

## Step 5 — Add Two Tools to the Agent (5 min)

This is the core step. You are giving the agent two capabilities it can choose between.

With the AI Agent node selected, look for an **Add Tool** option in the settings panel (sometimes labeled **Tools** or **Add capability**).

**Tool 1 — Wikipedia**
1. Click **Add Tool** and search for **Wikipedia**.
2. Select it. No configuration needed — this tool lets the agent look up any Wikipedia article by topic.
3. You will see it appear as a connected tool on the agent.

**Tool 2 — Calculator**
1. Click **Add Tool** again and search for **Calculator**.
2. Select it. No configuration needed — this tool lets the agent do arithmetic.

Your AI Agent node should now show two tools attached to it: Wikipedia and Calculator.

---

## Step 6 — Connect the Output and Run (5 min)

1. Add one more node to the right of the AI Agent: click **+** and search for **Chat** → select **Chat Reply** (or a similar output node that sends the response back).
2. Connect the AI Agent output to this node.

Your full workflow should read: **Chat Trigger → AI Agent (Wikipedia + Calculator) → Chat Reply**

3. Click **Test workflow** or the **Chat** button that appears in the bottom of the canvas. A chat window will open.

4. Type this prompt:
   ```
   How many times would the population of Iceland fit inside the population of the United States? Show your math.
   ```

5. Watch the workflow execute. The agent has to look up two population numbers (Wikipedia) and then divide them (Calculator). You will see it call both tools in sequence.

---

## Step 7 — Read the Execution Trace (3 min)

After the workflow runs, click on the **AI Agent node** to expand its execution details. You should see:

- The agent's initial reasoning (what it decided to do first)
- The tool call it made to Wikipedia (what it searched for)
- The data that came back
- The second tool call to Calculator (the numbers it passed in)
- The result
- The final response it composed

This trace is the anatomy of a tool-calling agent. Every MCP-enabled agent in a production system produces a log like this — it is how you audit what the agent actually did versus what it said it did.

---

## Step 8 — Screenshot and Reflect (3 min)

Take two screenshots:
1. Your workflow canvas showing the connected nodes
2. The execution trace showing at least one tool call

Then answer these two questions:

**1. What did the agent decide on its own?**
You gave the agent a question — not instructions for which tool to call or in what order. Look at the trace and describe: how did the agent decide to use Wikipedia first? What would have happened if it had tried to use Calculator first?

**2. What would change if these tools had write access?**
Right now both tools are read-only — Wikipedia returns text, Calculator returns a number. Neither changes anything in the world. If you replaced the Wikipedia tool with a tool that could *edit* Wikipedia articles, how would your governance requirements change? Name one specific guardrail you would add.

---

## Debrief

Be ready to share your canvas screenshot and one observation from the execution trace. The debrief will focus on: how the agent chose between tools, what the raw tool response looked like before the agent processed it, and whether the final answer matched what the trace showed.

---

## Why This Matters

What you just built is structurally identical to an enterprise MCP workflow — a coordinating agent, a set of registered tools, a routing decision, and an execution trace. The tools here are simple (Wikipedia and Calculator). In a real deployment they might be Salesforce, a file system, a ticketing system, or a payment processor.

The canvas you built, the trace you read, and the governance question you answered are the same artifacts a practitioner produces before connecting any of those real systems.

---

## Quick Reference — What You Wired

| Component | What it is | What you configured |
|-----------|-----------|-------------------|
| **Chat Trigger** | Input node — receives the user's message | Default settings |
| **AI Agent** | The coordinating agent — routes to tools and constructs the response | Connected to two tools |
| **Wikipedia tool** | Built-in lookup — returns article content for any topic | No configuration required |
| **Calculator tool** | Built-in computation — performs arithmetic on numbers the agent provides | No configuration required |
| **Chat Reply** | Output node — sends the agent's response back | Default settings |
