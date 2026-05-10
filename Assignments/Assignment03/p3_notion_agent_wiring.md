# P3 — Notion Agent: Wired and Autonomous

**Worth:** 15% of final grade  
**Assigned:** End of Module 5  
**Due:** Before Module 7  
**Platform required:** Notion — [notion.com](https://www.notion.com) (Plus plan — 14-day trial, or free with .edu email)  
**Submission:** One PDF or Word document uploaded to Blackboard + live proof in the class Slack channel

---

## Overview

In P1 you planned an agent. In P2 you gave it a voice. In P3 you give it hands.

Specifically: you will build a Notion agent that does something useful for your actual work, connects to the class Slack channel as a live output channel, runs autonomously on a schedule without you manually triggering it, and can be called by name from Slack by anyone in the class. By the time this assignment is done, your agent will be a persistent, autonomous worker — not a demo you run once and close.

This is the pattern that appears in real enterprise deployments: an agent with a defined knowledge base, a scheduled task queue, external write access, and a public endpoint others can invoke. You are building all four pieces.

The proof of completion is visible to everyone — including the instructor — in the class Slack channel. If your agent posted, it worked.

---

## What You Need Before You Start

- A Notion account on the Plus plan. Use your .edu email at [notion.com](https://www.notion.com) for a free Plus plan, or start the 14-day trial if you prefer. The 14-day window is enough for the assignment.
- The class Slack workspace invite link (provided by your instructor before this assignment opens).
- Two to three Notion pages or a small database relevant to your work — policies, project notes, a task list, meeting notes, anything your agent would realistically draw from. You will build this during Part 1 if you do not have it already.
- 60–90 minutes of focused work time. This assignment has more moving parts than P1 or P2. Set aside a single block rather than splitting it across short sessions — the wiring steps build on each other.

**If something looks different from what this document describes:** Notion updates its interface frequently. Take a screenshot and ask your AI assistant: *"I'm in Notion trying to [do X]. Here's what my screen looks like — where do I find it?"* Using AI to navigate a changing interface is a legitimate skill in this field.

---

## Part 1 — Agent Design Document

Write this before opening Notion's agent builder. The design document is what separates a thoughtful deployment from clicking around until something posts to Slack.

### 1a — Define Your Agent's Job

Answer these four questions in writing. One to three sentences each.

**What is this agent's one job?**  
Be specific. Not "help me stay organized" — that is a product pitch, not an agent definition. Something like: *"Every weekday morning, this agent reads my Project Status database, identifies any items marked Blocked or Overdue, and posts a one-paragraph summary to the class Slack channel."*

**What Notion content will it use?**  
List the specific pages or databases you are giving it access to. If they do not exist yet, you will create them in Part 2 before building the agent. Two to three sources is enough.

**What will it post to Slack, and when?**  
Describe the output: what does the Slack message contain, and what triggers it — a schedule, an event in Notion, or an @mention from Slack?

**How does this connect to your actual work?**  
This agent should be doing something you could plausibly use after the course ends. Name the role or context. A student who works in operations and builds an agent that summarizes open tickets is doing something different from a student who works in sales and builds one that surfaces stale leads. Both are valid — but they should reflect real work, not placeholder content.

---

### 1b — Trigger Design

Your agent will use at least one trigger. Choose your trigger types and explain why you chose them. You may use more than one.

| Trigger type | Your plan for this trigger |
|---|---|
| **Recurring schedule** (daily, weekly, etc.) | |
| **Notion event** (page created, property updated, etc.) | |
| **Slack @mention** (someone calls the agent by name in Slack) | |

At minimum, your agent must have the **recurring schedule** trigger and the **Slack @mention** trigger active. The recurring trigger makes it autonomous. The @mention trigger makes it callable by your classmates — which is required for Part 4.

---

## Part 2 — Build Your Notion Foundation

Before the agent can do anything useful, it needs content to work with. If your Notion workspace already has relevant pages or databases, you can use those. If not, build a lightweight version now.

### Step 1 — Create or Identify Your Knowledge Base

Create at least one Notion database or a set of organized pages that represent the context your agent will draw from. This does not need to be large — a database with 8–10 records, or three focused pages, is enough.

**What makes useful agent content in Notion:**
- Concrete, factual information — not vague aspirational language
- Consistent structure — if it is a database, fill in the properties consistently
- Written the way you actually talk about the work — terminology should match how you and your colleagues describe things

Take a screenshot of this database or page set. You will include it in your submission.

### Step 2 — Create a Task Queue Database

This is the mechanism that makes your agent autonomous. You will build a small database called whatever makes sense for your context — something like *Daily Briefs*, *Agent Runs*, or *Weekly Reports*. Each time a new record is created in this database, it can carry a specific task prompt to your agent.

Create the database with at minimum these two fields:
- **Title** — the name and date of each run
- **Status** — to track what has been done

You do not need to populate it yet — you will set up the recurring template in Part 3.

---

## Part 3 — Build and Wire the Agent

### Step 1 — Create the Agent

1. Go to the **Agents** section in your Notion sidebar and select **+ New Agent**.
2. Choose **Create from scratch** or start from the **Task Triage** template — whichever fits your job definition from Part 1a.
3. Write your agent instructions. Use the job definition from Part 1a as your guide. Be specific about: what content it reads, what it produces, and what the Slack post should contain.

**Instruction-writing tip:** Write to the agent the same way you would write a task delegation email to a capable colleague who does not know your business yet. Spell out what "done" looks like.

### Step 2 — Grant Access to Your Content

In the agent's **Tools and access** settings:

1. Add the specific pages and databases you identified in Part 1a. Grant **Can view** access to knowledge sources the agent should read from. Grant **Can edit content** access to the Task Queue database from Part 2 — the agent will need to write status updates there.
2. Leave **web access** off unless your agent's job specifically requires it. Narrower access produces more predictable behavior.

Screenshot the Tools and access panel with your configured permissions. Include this in your submission.

### Step 3 — Connect Slack

1. In the agent's **Tools and access** panel, find Slack and select **Connect**.
2. Authorize Notion to access your Slack account. When prompted, use the same email address you used to join the class Slack workspace.
3. Select the class Slack channel as the channel your agent can post to.

Once connected, post a test message manually from the agent's Chat tab to confirm the connection works. Take a screenshot of that first test message appearing in Slack. Include it in your submission.

### Step 4 — Configure Triggers

In the agent's **Settings → Triggers** panel, add both of the following:

**Trigger 1 — Recurring schedule**  
Set a recurring schedule that makes sense for your agent's job. Daily at 7am is a reasonable default if you are unsure. Confirm the next scheduled run time is visible and correct.

**Trigger 2 — Slack @mention**  
Add a Slack trigger and set the event type to **"The Custom Agent mentioned in a message"**. Select the class Slack channel.

> **Note for the instructor to set up before students begin:** The Slack workspace admin must enable *Allow all members to create user groups* in Slack settings before the @mention trigger will work. This is a one-time workspace setting.

Screenshot your Triggers panel showing both triggers active. Include this in your submission.

### Step 5 — Set Up the Recurring Template

This step is what makes your agent autonomous rather than just automated. Instead of relying on the agent's built-in schedule to run the same instructions every time, you will create a recurring Notion template that delivers a specific task prompt to your agent each run — giving you a clean, auditable log of every run and the flexibility to change what the agent does without rewriting its standing instructions.

1. Open the Task Queue database you created in Part 2.
2. Click the **New** dropdown in the top right → **Templates**.
3. Create a new template. Name it something like *Daily Brief @Today*. The `@Today` tag automatically dates each new page with the current date — you never rename anything manually.
4. Inside the template body, write the specific task prompt you want your agent to receive each time this template runs. This should match the job you defined in Part 1a. For example:

   > *Hey @[your agent name], write today's status brief. Pull any items marked Blocked or Overdue from the Project Status database. Write a two-paragraph summary — first paragraph is the blockers, second paragraph is what is on track. Post to Slack when done.*

5. @mention your agent at the end of the prompt inside the template. This fires the agent when the new page is created.

   > **Important:** After you finish writing the template and mentioning the agent, immediately open the agent settings and pause any active triggers — otherwise the agent fires right now on the half-built template and may overwrite it. Resume the triggers when you are done.

6. Set the template to **Recur** on your chosen schedule (click the template name → Duplicate → set cadence). Confirm the small blue recurring icon appears next to the template name. If you do not see it, the schedule did not save — try again.

Screenshot the recurring template with the blue icon visible. Include this in your submission.

---

## Part 4 — Cross-Agent Interaction

This is the part of the assignment that you cannot do alone.

Every student in this class has built a Notion agent connected to the class Slack channel, with an @mention trigger active. That means the class Slack channel is now a live environment where multiple agents coexist and can be invoked by anyone.

Do both of the following before submitting:

### 4a — Call a Classmate's Agent

Find out the name of at least one classmate's Notion agent (coordinate in Slack or in class). In the class Slack channel, @mention their agent with a short, specific request that is relevant to what their agent does.

Document:
- Which agent you called and what you asked
- What the agent responded in Slack (paste or screenshot)
- Whether the response made sense given what you know about their agent's design

### 4b — Receive a Call

Your agent will be @mentioned by at least one classmate during the assignment window. Check your agent's **Activity** tab after the submission deadline passes to see the run log.

Document:
- What trigger fired (the Slack @mention)
- What the agent did in response (visible in the Activity log)
- Whether the agent's response was appropriate for the request it received

If no classmate called your agent before you submit, document that outcome honestly and describe what you would expect to happen based on your trigger configuration.

---

## Part 5 — Reflection

Answer both questions in two to four sentences each. Specific answers graded higher than general ones.

**1. What did the cross-agent interaction reveal that running your own agent alone did not?**

Think about what happened when your agent received a request from someone who did not design it and does not know its instructions. Did it behave the way you intended? What assumptions did you build into it that only became visible when someone else tried to use it?

**2. The recurring template system gives you a task queue and an audit log. What does the audit log change about how you would govern this agent if it were deployed at work?**

Consider: who would need to see the Activity tab? What would you look for in the run history? Would you feel comfortable letting this agent run unsupervised for two weeks — and if not, what specifically would you add before you would?

---

## Submission Requirements

Your submission is a single PDF or Word document uploaded to Blackboard. The class Slack channel serves as your primary proof of completion — if your agent posted, that is visible to the instructor without you submitting anything additionally.

The document must contain, in order:

1. **Agent Design Document** — job definition, content list, trigger plan (Part 1)
2. **Screenshot** of your Notion knowledge base or pages showing the content you gave the agent access to (Part 2)
3. **Screenshot** of the agent's Tools and access panel showing configured permissions (Part 3, Step 2)
4. **Screenshot** of the first test message in the class Slack channel (Part 3, Step 3)
5. **Screenshot** of the Triggers panel showing both triggers active (Part 3, Step 4)
6. **Screenshot** of the recurring template with the blue recurring icon visible (Part 3, Step 5)
7. **Cross-agent interaction documentation** — both 4a and 4b (Part 4)
8. **Reflection** — both questions answered (Part 5)

---

## Grading Rubric

| Section | Points | What earns full credit |
|---------|--------|----------------------|
| Agent Design Document | 20 | Job definition is specific and work-relevant; content sources named; trigger plan explains choices — not just what, but why |
| Notion Build | 20 | Knowledge base or pages exist and are substantive; Task Queue database created; agent instructions are specific and match the design document |
| Slack Connection and Triggers | 20 | Test message screenshot shows agent posted to class channel; both triggers configured and visible in screenshot; recurring template screenshot shows blue icon |
| Cross-Agent Interaction | 25 | 4a documented with the call made, response received, and honest assessment; 4b documented from Activity log or honestly noted if not triggered; both show the student engaged with the shared environment, not just their own setup |
| Reflection | 15 | Both questions answered with specifics from actual experience — not generic statements about agents in general |
| **Total** | **100** | |

---

## A Note on "It Didn't Work"

The most common failure mode in this assignment is a trigger that was configured but did not fire, or a Slack message that never arrived. Before assuming the platform is broken, check in this order:

1. Is the Slack integration authorized with the same email you used to join the class workspace?
2. Is the agent published and not paused?
3. For the recurring template — is the blue recurring icon visible next to the template name? If not, the schedule did not save.
4. For the @mention trigger — did the Slack workspace admin enable user groups? (Ask your instructor if unsure.)

If something genuinely does not work after checking these, document what you tried and what happened. An honest failure write-up that shows methodical debugging is graded more favorably than a submission that ignores the problem.

---

## Resources

- [Notion Custom Agents — Help Center](https://www.notion.com/help/custom-agents)
- [Notion Agents overview page](https://www.notion.com/product/agents)
- [Rundown AI guide — Use This Hidden Feature to Make Your Notion Agents Autonomous](https://app.therundown.ai/guides/use-this-hidden-feature-to-make-your-notion-agents-autonomous) — the recurring template technique used in Part 3, Step 5
- M05 pre-recorded demo — instructor walkthrough of the full wiring sequence
- M05 lesson slides — MCP, tool access, permission scoping, blast radius
