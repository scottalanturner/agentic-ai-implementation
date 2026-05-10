# Activity: Wire Your Voice Agent to Slack via MCP

**Format:** In-class activity — solo  
**Time:** 20 minutes  
**Requires:** Your P2 ElevenLabs agent · ElevenLabs account (free) · Class Slack workspace (instructor provides link)

---

## Overview

You built a voice agent in P2. Right now it lives entirely inside ElevenLabs — it talks to users, routes to branches, escalates when needed, but nothing outside knows what happened. That is fine for a prototype. It is not fine for anything you would actually deploy at work.

In a real deployment, when your agent escalates — when a customer mentions a lawsuit, a safety issue, or a repeat contact — someone on your team needs to know immediately. Not by checking a dashboard. By getting a message in the tool they are already looking at: Slack.

This activity wires your existing P2 agent to the class Slack workspace so that when Branch 3 fires, a message posts automatically. You are not rebuilding anything — you are extending the agent you already have by attaching it to a real communication system. This is MCP in action: your agent's hands now reach outside ElevenLabs.

---

## Goals

- Experience MCP as a practitioner, not just as a concept — you are attaching a live integration, not reading about one
- See the difference between an agent that "works in a sandbox" and one that "does something in the world"
- Understand why the moment an agent can write to external systems, permission scope becomes a real security concern

---

## What the Instructor Has Set Up

Your instructor has created a class Slack workspace with one channel per student. Before this activity starts, you will receive:

- An invite link to join the class Slack workspace
- The name of your personal channel (e.g., `#firstname-lastname-agent`)
- The class Slack workspace URL

You do not need a Slack account — you can join the workspace with just your email address.

---

## Step 1 — Join the Class Slack Workspace (2 min)

1. Open the invite link your instructor shared.
2. Sign in or create a Slack account using your email address.
3. Find your personal channel in the left sidebar and confirm it is there.

Leave Slack open — you will check it at the end to verify the integration worked.

---

## Step 2 — Find the Slack Integration in ElevenLabs (3 min)

1. Go to [elevenlabs.io](https://elevenlabs.io) and open your P2 agent.
2. In your agent settings, look for an **Integrations** section. It may also appear under **Tools**, **Connections**, or **Deploy**. ([ElevenLabs integrations documentation](https://elevenlabs.io/agents/integrations))
3. Find the **Slack** integration. ([ElevenLabs Slack integration](https://elevenlabs.io/agents/integrations/slack))
4. Click it and follow the connection flow — you will need to authorize ElevenLabs to post to your Slack workspace.

**If you cannot find the Slack integration in your interface:** Take a screenshot of your screen and type this into Claude or ChatGPT: *"I'm in ElevenLabs trying to find the Slack integration for my Conversational AI agent. Here's what my screen looks like — where do I find it?"* This is the right way to navigate a platform that updates frequently.

---

## Step 3 — Configure What Posts to Slack (5 min)

Once the Slack connection is authorized, configure what gets sent and when:

**Channel:** Point the integration to your personal class channel (e.g., `#firstname-lastname-agent`).

**Trigger:** Set the integration to fire when your **escalation branch (Branch 3)** is reached. This is the integration's value — not every conversation posts to Slack, only the ones that need human attention.

Depending on your ElevenLabs interface, this may be configured as:
- A webhook trigger on conversation end with a condition
- A tool call your Branch 3 instructions invoke
- An integration-level setting for escalation events

If the trigger options are different from what you expect, configure the integration to post whenever Branch 3 language appears in the conversation — or, if easier, post at the end of every conversation as a fallback for this activity.

**Message content:** Configure the Slack message to include at minimum: the customer's stated issue (one line) and the reason for escalation.

---

## Step 4 — Test It (5 min)

1. Open your agent's share link in a new browser tab.
2. Start a conversation and say something that fires your Branch 3 escalation trigger — use the same input you tested in P2 Test Conversation 3.
3. After the agent delivers the escalation handoff message, switch to Slack.
4. Check your personal channel. A message should have arrived.

**If nothing arrives:** Check the integration settings — confirm the right channel is selected and the trigger condition is saved. Try triggering the agent again. If it still does not fire, ask the instructor.

---

## Step 5 — Screenshot and Reflect (5 min)

Take a screenshot of your Slack channel showing the message that arrived. Keep this — it may be useful for future assignments.

Then answer these two questions before the debrief:

**1. What is the blast radius of this integration?**

Your agent can now post to Slack. That is a narrow permission — post only. If the integration were misconfigured to allow your agent to *read* all channels, or *delete* messages, or *invite new members*, what could go wrong? Name one specific scenario.

**2. What would you add to the Slack message to make it actually useful for the person receiving it?**

Right now it probably says something basic. If you were the customer experience manager getting this message at 9pm, what additional information would you need to act on it without logging into ElevenLabs?

---

## Debrief

Be ready to share your Slack message with the class — either by screen share or describing what appeared. The debrief will focus on three things: what the message contained, what it was missing, and whether the trigger condition was specific enough to avoid noise in a real deployment.

---

## Why This Matters

The moment an agent can write to an external system — Slack, email, a CRM, a ticketing tool — it has hands. And hands can cause damage. What you just configured in 20 minutes is the same pattern enterprise teams spend weeks governing: which agent, under which conditions, can write what, to where, and who audits it.

The scoping question from the reflection — blast radius — is not hypothetical. It is a security review line item every time someone proposes adding a new MCP server or integration to a production agent.

---

## Quick Reference — What You Wired

| Component | What it is | What you configured |
|-----------|-----------|-------------------|
| **ElevenLabs agent** | Your P2 voice agent | The source — it initiates the Slack post |
| **Slack integration** | ElevenLabs native connector | The channel and trigger condition |
| **Your Slack channel** | `#firstname-lastname-agent` | The destination — where the message lands |
| **Trigger condition** | Branch 3 escalation | When the post fires — not on every conversation |
| **Message content** | Issue summary + escalation reason | What arrives in Slack |
