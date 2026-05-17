# Activity 1: Build a Tool-Calling Agent in n8n

**Module 5 · Pre-recorded class**
**Format:** Solo · self-paced
**Time:** 30–40 minutes (allow extra if it's your first time in n8n)
**Requires:** A web browser and an email address. No credit card. No prior coding experience.

---

## What you're building and why

In the lecture you saw how an agent decides which tool to call, sends a structured request, and uses the response to build its answer. This is the standard tool-calling pattern that sits underneath every MCP-enabled product.

In this activity you'll build that pattern yourself — visually — using **n8n**, a free browser-based workflow tool. The workflow will be a single coordinating agent wired to two tools (Wikipedia and a Calculator). You'll give it a question that requires both tools, then read the execution trace to see exactly which decisions the agent made on its own.

This is the closest you can get to a live MCP workflow without setting up a server.

> **A note about the UI.** n8n updates its interface every few weeks. Button labels and node names may shift slightly between when these instructions were written (May 2026) and when you complete the activity. If something in this document doesn't match what you see on screen, look for a button that does the same thing — the function is the same; the label may be different. The official tutorial at [docs.n8n.io/advanced-ai/intro-tutorial/](https://docs.n8n.io/advanced-ai/intro-tutorial/) is kept current — use it as a backup.

---

## Learning goals

By the end of this activity, you will be able to:

- Build a working tool-calling agent in a visual canvas, with no code
- Recognize the structural components of a tool-calling agent (trigger, agent, chat model, tools)
- Read an execution trace and identify the agent's routing decisions
- Connect what you built to the MCP architecture from the lecture

---

## Step 1 — Create a free n8n Cloud account (5 min)

1. Go to **[n8n.io](https://n8n.io)** in your browser.
2. Click **Get started** (or **Start free trial** — the button label varies).
3. Sign up with your email address. **No credit card required.** You'll get a 14-day Cloud trial.
4. Confirm your email, set a password, and answer the brief setup questions (you can pick "Personal" or any role — it doesn't affect the activity).
5. You'll land in your n8n Cloud workspace.

If you see a sample workflow, tutorial overlay, or welcome banner, close or dismiss it — you're starting from a blank canvas.

> **Why a Cloud account and not self-hosted?** n8n offers a free self-hosted version, but installing it requires Docker and a terminal. For this activity we want zero installation. The Cloud trial is fine for 14 days, which is more than enough.

---

## Step 2 — Claim your free AI credits (2 min) — **don't skip this**

This is the step that lets you finish the activity without buying anything.

When you land in your n8n workspace, look in the **left sidebar** for a banner that says something like **"Claim free AI credits"** or **"Get 100 free OpenAI credits"**. Click it and accept.

These credits let you use OpenAI's language model inside n8n **without needing your own OpenAI API key**. They're more than enough for this activity (each test run costs a fraction of a cent).

> **What is an "API key"?**
> An API key is a long random string that proves you're allowed to use a paid service like OpenAI. Normally you'd sign up at OpenAI, pay them with a credit card, and get a key. The free n8n credits skip that whole process — n8n pays OpenAI on your behalf for a small amount of usage.

> **If you don't see the banner:** look in the left sidebar under "Settings" or "Admin." Some accounts surface the credits in a slightly different spot. If you genuinely can't find it after two minutes of looking, jump to the **"What if I can't get free credits?"** section near the end of this document.

---

## Step 3 — Create a new workflow (1 min)

1. In the left sidebar, click **Workflows**.
2. Click **+ Create Workflow** (or the **+** icon near the top right).
3. At the top of the canvas, click the workflow's default name and rename it: **`Tool-Calling Agent — Module 5`**.

You should now see a blank canvas with a single button in the middle that says **Add first step** (or **+**).

---

## Step 4 — Add the Chat Trigger (2 min)

The trigger is the node that starts your workflow. For an agent that you'll chat with, you want a chat-based trigger.

1. Click **Add first step** (or the **+** in the middle of the canvas).
2. In the search box that appears on the right, type **`chat`**.
3. From the results, select **Chat Trigger** (you may also see it labeled **"When chat message received"** — same node, label varies by version).
4. Don't change any settings. Close the settings panel (X in the top right of the panel, or click outside it).

You should now have one node on your canvas labeled **Chat Trigger** (or **When chat message received**).

---

## Step 5 — Add the AI Agent node (2 min)

1. Click the **+** that appears to the right of your Chat Trigger node.
2. In the search box, type **`AI Agent`**.
3. Select the node called **AI Agent**.
4. The AI Agent's settings panel will open on the right. **Leave all the defaults for now** and close the panel.

You should now have two nodes connected by an arrow: **Chat Trigger → AI Agent**.

Now look closely at the **AI Agent** node. Below it (or attached to its underside, depending on the version) you'll see **three small "+" symbols labeled**:

- **Chat Model** — the language model the agent uses to think
- **Memory** — optional; lets the agent remember previous messages
- **Tool** — the external capabilities you'll attach

These three "+" symbols are how you attach **sub-nodes** to the AI Agent. The next three steps each click one of them.

---

## Step 6 — Attach the OpenAI Chat Model (5 min)

The Chat Model is the "brain" — the language model that decides what to do.

1. Click the **+** under the AI Agent labeled **Chat Model**.
2. In the search box, type **`OpenAI`**.
3. Select **OpenAI Chat Model**.
4. The settings panel will open. You'll see a field called **Credential to connect with** at the top.

### Setting up the credential

5. Click the **Credential to connect with** dropdown.
6. You should see an option called **"n8n free OpenAI API credits"** (or very similar wording — sometimes "n8n hosted credits"). **Select it.** This is the free-credits credential you claimed in Step 2.
7. Below the credential field, find **Model** and select **gpt-4o-mini** (or **gpt-4.1-mini**, or any "mini" or "nano" model that appears). These are the cheapest options and burn through fewer of your free credits.
8. Close the settings panel.

The OpenAI Chat Model sub-node should now appear attached to the AI Agent.

> **If the "n8n free OpenAI API credits" option isn't in the dropdown,** see the **"What if I can't get free credits?"** section near the end of this document.

> **What is a "credential" in n8n?**
> A credential is just stored authentication info — usually an API key — that tells n8n how to talk to an external service on your behalf. n8n stores the credential once and reuses it across all your workflows. The free credits option is a pre-configured credential that uses n8n's own API key under the hood.

---

## Step 7 — Attach the Wikipedia tool (2 min)

Tools are the external capabilities the agent can choose to use. The agent itself decides when to call which tool based on the user's request.

1. Click the **+** under the AI Agent labeled **Tool** (sometimes shown as **+ Tool**).
2. In the search box, type **`wikipedia`**.
3. Select **Wikipedia**.
4. No configuration needed. Close the settings panel.

You should now see a Wikipedia tool sub-node attached.

---

## Step 8 — Attach the Calculator tool (2 min)

1. Click the **+** under the AI Agent labeled **Tool** again (you can attach more than one tool — that's the point).
2. In the search box, type **`calculator`**.
3. Select **Calculator**.
4. No configuration needed. Close the settings panel.

Your full structure should now look like this:

```
Chat Trigger ──→ AI Agent
                 ├── Chat Model: OpenAI Chat Model
                 ├── Tool: Wikipedia
                 └── Tool: Calculator
```

You do **not** need to add a separate output node. The Chat Trigger has a built-in chat panel that will display the agent's response automatically.

---

## Step 9 — Save and test (5 min)

1. Click **Save** in the top right of the canvas (or press Cmd+S / Ctrl+S).

2. At the bottom of the canvas, find the **Chat** button (it may also appear as **"Open Chat"** or **"Test workflow"**). Click it. A chat panel will open at the bottom of the screen.

3. In the chat panel, paste this prompt exactly:

   ```
   How many times would the population of Iceland fit inside the population of the United States? Show your math step by step.
   ```

4. Press Enter. Watch the workflow run — you'll see colored indicators appear on the nodes as the agent works.

The agent has to do three things on its own:
- Decide it needs Iceland's population → call Wikipedia for "Iceland"
- Decide it needs the US's population → call Wikipedia for "United States"
- Decide it needs to divide them → call the Calculator

You typed none of that. The agent figured out the sequence.

5. After about 10–30 seconds, the agent's answer will appear in the chat panel. It should give you a number (roughly 800–1,000 times, depending on exactly which population figures Wikipedia returned) and show its arithmetic.

---

## Step 10 — Read the execution trace (5 min)

This is the most important step. The trace is what shows you what the agent actually did versus what it said it did.

1. Close the chat panel (X in the top right of the chat).
2. Click on the **AI Agent node** on the canvas. A details panel will open.
3. Click the tab or section labeled **Logs**, **Execution data**, or **Output** (varies by version — look for whichever shows the recent run's details).

You should be able to expand the steps and see:

- The agent's initial reasoning (what it decided to do first, in its own words)
- The first tool call — to Wikipedia — and the exact search term it chose
- The data Wikipedia returned (a chunk of article text)
- The second tool call — to Wikipedia again — for the other country
- The third tool call — to Calculator — with the exact expression it computed
- The result
- The final response the agent composed for you

Take a moment to scroll through this. **Every MCP-enabled agent in production produces a log like this.** It is how engineers audit what happened, why a tool was selected, and whether the final answer matched the underlying data.

---

## Step 11 — Reflect (5 min)


**Question 1 — What did the agent decide on its own?**

You gave the agent a question, not instructions. Look at your trace and describe: How did the agent decide to call Wikipedia first instead of Calculator? What information made that the right first move? What would have happened if it had tried Calculator first with no population numbers in hand?

**Question 2 — What would change if these tools could write, not just read?**

Wikipedia (in this version) and Calculator are both **read-only** — Wikipedia returns text, Calculator returns a number, neither changes anything in the world. If you replaced the Wikipedia tool with one that could **edit** Wikipedia articles, what would change about your governance requirements? Name one specific guardrail you would add before letting this same agent run with that more powerful tool. Tie your answer to the least-privilege checklist from the lecture.

---


## Troubleshooting — what to do if something doesn't work

This is a pre-recorded activity, so there's no instructor in the room. Here's how to unblock yourself.

### "I can't find the AI Agent node."
- Make sure you typed `AI Agent` (with the space). Some versions also list it as **Agent** or **LangChain Agent**.
- It's in the AI/LangChain category, sometimes shown under **Advanced AI** in the node menu.

### "The OpenAI credential dropdown doesn't show 'n8n free OpenAI API credits.'"
- This happens occasionally on new accounts. Try refreshing the page once.
- Check **Settings → Credentials** in the left sidebar. If you see a credential called **n8n free OpenAI API credits** there, it exists — go back to your node and select it. If you don't see it, see the next section.

### "What if I can't get free credits?"
You have three fallback options, in order of effort:

1. **Use Google's free Gemini tier.** Sign up at [aistudio.google.com](https://aistudio.google.com) → click **Get API key** → copy the key. In n8n, replace the **OpenAI Chat Model** sub-node with the **Google Gemini Chat Model** sub-node, and paste your key as the credential. Google's free tier is generous and works fine for this activity.

2. **Use your own OpenAI API key.** This requires a credit card. Go to [platform.openai.com](https://platform.openai.com) → **API keys** → **Create new secret key** → copy it. Add at least $5 of credit at **Billing**. In n8n, create a new OpenAI credential and paste your key. The activity uses pennies of credit.

3. **Skip the build, watch a recorded run.** If the technical setup is blocking you for more than 20 minutes, document what went wrong (a screenshot of the error helps), then watch the recorded walkthrough linked in the LMS module. You can still answer the two reflection questions based on the recorded trace.

### "My workflow ran but the agent's answer is empty or weird."
- Click on the AI Agent node and look at the **Logs**. If you see a quota or rate-limit error, your free credits may be exhausted — switch to one of the fallback options above.
- If the trace shows the tools were never called, check that you attached the tools to the **Tool** "+" slot, not the **Chat Model** slot. Each sub-node attaches to a specific slot.

### "Nothing happens when I click the Chat button."
- Make sure the workflow is **Saved** (top right).
- Make sure the Chat Trigger node is connected to the AI Agent (you should see an arrow between them).

### "The agent gives a wrong answer for the populations."
That's actually fine for this activity. The number Wikipedia returns can vary by article phrasing, and the agent's math depends on which numbers it extracted. **The point of the activity is the routing trace, not the population accuracy.** Your screenshot of the trace is what matters.

---

## Why this matters

What you just built is structurally identical to an enterprise MCP workflow:

- A coordinating agent
- A registered set of tools (manifest)
- A routing decision (the agent picked which tool, in which order)
- An execution trace (the audit log)

The tools you used are simple. In a real deployment they might be Salesforce, a file system, a ticketing platform, or a payment processor. The canvas you built, the credentials you wired, the trace you read, and the governance question you answered are the same artifacts a practitioner produces before connecting any of those real systems.

---

## Quick reference — what you wired

| Component | What it is | What you configured |
|-----------|-----------|---------------------|
| **Chat Trigger** | The starting node — receives a chat message and kicks off the workflow | Default settings |
| **AI Agent** | The coordinating agent — chooses tools and constructs the response | Default settings; sub-nodes attached |
| **OpenAI Chat Model** (sub-node) | The language model the agent uses to think | Free n8n credits credential + a mini model |
| **Wikipedia** (sub-node) | A tool that lets the agent look up any Wikipedia article | No configuration needed |
| **Calculator** (sub-node) | A tool that lets the agent do arithmetic on numbers it finds | No configuration needed |
