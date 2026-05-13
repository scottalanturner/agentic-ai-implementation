# P4 — Give Your Agent Hands (and a Watchdog)

**Worth:** 15% of final grade
**Assigned:** End of Module 8
**Due:** Before Module 10
**Platform required:** Notion (the agent you built in Project 2) + class Slack workspace
**Submission:** One PDF or Word document uploaded to Blackboard + live proof in the class Slack channel

---

## Overview

In Project 2 you built a grounded knowledge agent in Notion. It could read; it could not act. In Project 4 you give that same agent tools, schedule it to run on its own, expose it to your classmates as a callable resource in Slack — and *then* you audit it.

The pattern you are building is the one that appears in real enterprise deployments: an agent with a defined knowledge base (Project 2), a task queue, external write access, a public endpoint others can invoke, and a documented governance review. The Module 8 content — threat classes, blast radius, audit trails, RBAC, the confused deputy problem, recoverable-failure UX — becomes the lens you apply to your own agent. You will find at least one real risk in your own build. The point of this assignment is not to ship a perfectly safe agent — it is to find what you missed and document the fix.

The proof of completion is visible to everyone — including the instructor — in the class Slack channel. If your agent posted, it worked.

---

## What You Need Before You Start

- Your Project 2 Notion knowledge agent — keep your knowledge base, your agent, and your access scope intact from Project 2
- The class Slack workspace invite link (provided by your instructor before this assignment opens)
- A small Notion database or set of pages your agent can write *status* updates to — this becomes the Task Queue in Part 2. You do not need to have this built; you will create it in Part 2.
- 75–90 minutes of focused work time. This assignment has more moving parts than earlier projects. Set aside a single block rather than splitting it across short sessions — the wiring and audit steps build on each other.

**If something looks different from what this document describes:** Notion updates its interface frequently. Take a screenshot and ask your AI assistant: *"I'm in Notion trying to [do X]. Here's what my screen looks like — where do I find it?"* Using AI to navigate a changing interface is a legitimate skill in this field.

---

## Part 1 — Governance Plan

You are about to expand the surface of an agent — granting it write access, schedule autonomy, and a public endpoint. Module 8 named four threat classes that grow as agent surface grows. Before you wire anything, decide how you will scope each one.

### 1a — Threat Class Assessment

Fill in this table for your specific agent. Be concrete — name the exact mechanism, not the category.

| Threat class | What it could look like for your agent | What you will do about it |
|--------------|----------------------------------------|---------------------------|
| **Prompt injection** (text in a source document or Slack message that contains hidden instructions) | | |
| **Tool abuse / confused deputy** (agent uses its write access in ways the instructions did not intend) | | |
| **Over-permissioning** (agent has more access than the job requires) | | |
| **Data leakage** (information from one user, channel, or document surfaces somewhere it should not) | | |

Each "what you will do about it" entry should be a specific mitigation you will implement in Part 2 — not a vague aspiration. *"Limit write access to the Task Queue database only"* is specific; *"be careful with permissions"* is not.

---

### 1b — Permission Scoping Plan

For each Notion page or database your agent will touch, decide the minimum access level it needs to do its job. Use this table:

| Resource | Access level | Why this is the minimum |
|----------|--------------|------------------------|
| Knowledge Sources (from Project 2) | Can view (read-only) | Agent reads, never writes |
| Task Queue (new, from Part 2) | Can edit content | Agent writes status updates here |
| *(any other resource)* | | |

Then for Slack:

| Slack scope | Why your agent needs it |
|-------------|-------------------------|
| Read class channel mentions | To respond to @mentions |
| Post to class channel | To deliver scheduled briefs |
| *(any other scope)* | |

If you cannot justify a scope in one sentence, do not grant it.

---

### 1c — Human Approval and Tripwires

Name three conditions that, if hit, would require a human to step in. Examples:

- *"If the agent's scheduled post finds more than 10 Blocked items, pause and require a human review before posting."*
- *"If the agent is @mentioned more than 5 times in 10 minutes, stop responding and surface the activity to me."*
- *"If a Slack message contains an attached file or external URL, the agent should not parse it — refuse and direct to a human."*

These are tripwires. They are the agent equivalent of a circuit breaker — the threshold beyond which automation pauses and a human takes the call. Write three for your specific agent.

---

## Part 2 — Wire Your Project 2 Agent to Slack

You are extending the agent you built in Project 2 — not creating a new one. Open that agent in Notion.

### Step 1 — Create the Task Queue

This is the mechanism that makes your agent autonomous. You will build a small database called whatever makes sense for your context — something like *Daily Briefs*, *Agent Runs*, or *Weekly Reports*. Each time a new record is created in this database, it can carry a specific task prompt to your agent.

Create the database with at minimum these two fields:
- **Title** — the name and date of each run
- **Status** — to track what has been done

You do not need to populate it yet — you will set up the recurring template in Step 5.

---

### Step 2 — Grant Scoped Access

Open your Project 2 agent's **Tools and access** settings.

1. Confirm your **Knowledge Sources** are still set to **Can view** (read-only). This was the Project 2 scope — do not change it.
2. Add the **Task Queue** database from Step 1 with **Can edit content** access. This is the only write surface the agent gets.
3. Confirm web access is **off** unless your Part 1a plan explicitly called for it.

Screenshot the Tools and access panel showing all three scopes. You will include it in your submission. This screenshot is the proof that your permission scoping matches your Part 1b plan.

---

### Step 3 — Connect Slack

1. In the agent's **Tools and access** panel, find Slack and select **Connect**.
2. Authorize Notion to access your Slack account. When prompted, use the same email address you used to join the class Slack workspace.
3. Select the class Slack channel as the channel your agent can post to.

Once connected, post a test message manually from the agent's Chat tab to confirm the connection works. Take a screenshot of that first test message appearing in Slack. Include it in your submission.

---

### Step 4 — Configure Triggers

In the agent's **Settings → Triggers** panel, add both of the following:

**Trigger 1 — Recurring schedule**
Set a recurring schedule that makes sense for your agent's job. Daily at 7 AM is a reasonable default if you are unsure. Confirm the next scheduled run time is visible and correct.

**Trigger 2 — Slack @mention**
Add a Slack trigger and set the event type to **"The Custom Agent mentioned in a message"**. Select the class Slack channel.

> **Note for the instructor to set up before students begin:** The Slack workspace admin must enable *Allow all members to create user groups* in Slack settings before the @mention trigger will work. This is a one-time workspace setting.

Screenshot your Triggers panel showing both triggers active. Include this in your submission.

---

### Step 5 — Set Up the Recurring Template

This step is what makes your agent autonomous rather than just automated. Instead of relying on the agent's built-in schedule to run the same instructions every time, you will create a recurring Notion template that delivers a specific task prompt to your agent each run — giving you a clean, auditable log of every run and the flexibility to change what the agent does without rewriting its standing instructions.

1. Open the Task Queue database you created in Step 1.
2. Click the **New** dropdown in the top right → **Templates**.
3. Create a new template. Name it something like *Daily Brief @Today*. The `@Today` tag automatically dates each new page with the current date — you never rename anything manually.
4. Inside the template body, write the specific task prompt you want your agent to receive each time this template runs. For example:

   > *Hey @[your agent name], using only the attached Knowledge Sources, write today's status brief. Pull any items marked Blocked or Overdue. Write a two-paragraph summary — first paragraph is the blockers, second is what is on track. Post to the class Slack channel when done.*

5. @mention your agent at the end of the prompt inside the template. This fires the agent when the new page is created.

   > **Important:** After you finish writing the template and mentioning the agent, immediately open the agent settings and pause any active triggers — otherwise the agent fires right now on the half-built template and may overwrite it. Resume the triggers when you are done.

6. Set the template to **Recur** on your chosen schedule (click the template name → Duplicate → set cadence). Confirm the small blue recurring icon appears next to the template name. If you do not see it, the schedule did not save — try again.

Screenshot the recurring template with the blue icon visible. Include this in your submission.

---

## Part 3 — Cross-Agent Interaction

This is the part of the assignment that you cannot do alone.

Every student in this class has wired their Project 2 Notion agent to the class Slack channel, with an @mention trigger active. That means the class Slack channel is now a live multi-agent environment.

Do both of the following before submitting:

### 3a — Call a Classmate's Agent

Find out the name of at least one classmate's Notion agent (coordinate in Slack or in class). In the class Slack channel, @mention their agent with a short, specific request that is relevant to what their agent does.

Document:
- Which agent you called and what you asked
- What the agent responded in Slack (paste or screenshot)
- Whether the response made sense given what you know about their agent's design

### 3b — Receive a Call

Your agent will be @mentioned by at least one classmate during the assignment window. Check your agent's **Activity** tab after the submission deadline approaches to see the run log.

Document:
- What trigger fired (the Slack @mention)
- What the agent did in response (visible in the Activity log)
- Whether the agent's response was appropriate for the request it received

If no classmate called your agent before you submit, document that outcome honestly and describe what you would expect to happen based on your trigger configuration.

---

## Part 4 — Guardrails Audit

Now that the agent is live, audit it against your Part 1 plan and against the Module 8 framework. This is the part of the assignment that mirrors what a real security review would look like.

### 4a — Threat Self-Test

For each of the four threat classes from Part 1a, run one deliberate test against your own agent and document what happened.

| Threat class | What you tried | What the agent did | Did your Part 1a mitigation hold? |
|--------------|----------------|---------------------|----------------------------------|
| Prompt injection | Example: post a Slack message containing an instruction-style sentence inside otherwise benign text ("Please ignore your prior instructions and...") | | |
| Tool abuse / confused deputy | Example: @mention the agent in a way that asks it to use its Task Queue write access in an unintended way | | |
| Over-permissioning | Example: ask the agent for information from a Notion page you did not grant it access to — does it admit the access boundary, or does it bluff? | | |
| Data leakage | Example: ask the agent to repeat the most recent message it processed from another user — does it surface content it should not? | | |

You are red-teaming your own agent. If a mitigation failed and you cannot fix it within the assignment window, document the failure honestly — that is graded more favorably than hiding it.

---

### 4b — Inspect the Audit Log

Open your agent's **Activity** tab and review the run log from the last several days.

Answer these questions in writing, two to four sentences each:

- **What does the Activity log actually capture, and what is missing?** Could you reconstruct a problematic agent decision from the log alone, or would you need additional logs from Slack and Notion?
- **Who in a real organization would need access to this log, and how often?** Daily, weekly, only after an incident? Why?
- **What is the longest period you would feel comfortable letting this agent run with no human reviewing the log?** Be specific about the threshold beyond which review becomes mandatory.

---

### 4c — Top 3 Risks + Top 3 Mitigations

Close the audit by writing two short lists.

**Top 3 risks remaining** — what would you flag to a manager before this agent ran for real outside this course?

**Top 3 mitigations to implement before that happens** — concrete next steps, in priority order.

These two lists are what a real handoff to operations looks like. If you were leaving this agent for someone else to own next quarter, this is the page they would read.

---

## Part 5 — Reflection on Accountability

Answer both questions in two to four sentences each. Specific answers from your actual build and audit are graded higher than general statements.

**1. The Module 8 case studies named the people who got the call when the agent failed. For your agent, name one realistic failure and the role that would have to own the response.**

Not "the engineer." Not "the admin." Name the actual function — content owner, IT security, business owner, legal, customer success — and say why that person owns *this specific failure mode* and not some other.

**2. Going from Project 2 (read-only) to Project 4 (write access + Slack + schedule), what specifically changed about your risk register?**

Project 2's threat model was small — the worst case was a wrong answer. Project 4's threat model is larger. Name the single biggest expansion of risk and what would have to be true before you would be willing to ship this agent at work.

---

## Submission Requirements

Your submission is a single PDF or Word document uploaded to Blackboard. The class Slack channel serves as your primary proof of completion — if your agent posted, that is visible to the instructor without you submitting anything additionally.

The document must contain, in order:

1. **Governance Plan** — threat class assessment, permission scoping plan, tripwires (Part 1)
2. **Screenshot** of the agent's Tools and access panel showing the scoped permissions (Part 2, Step 2)
3. **Screenshot** of the first Slack test message in the class channel (Part 2, Step 3)
4. **Screenshot** of the Triggers panel showing both triggers active (Part 2, Step 4)
5. **Screenshot** of the recurring template with the blue recurring icon visible (Part 2, Step 5)
6. **Cross-agent interaction documentation** — both 3a and 3b (Part 3)
7. **Guardrails audit** — threat self-test table, audit log review, top 3 risks + top 3 mitigations (Part 4)
8. **Reflection** — both questions answered (Part 5)

---

## Grading Rubric

| Section | Points | What earns full credit |
|---------|--------|----------------------|
| Governance Plan | 20 | Threat class table is specific to this agent; permission scoping table justifies each scope in one sentence; three concrete tripwires written |
| Slack + Trigger Build | 20 | All four screenshots present; both triggers configured; recurring template shows blue icon; first Slack test post visible in class channel |
| Cross-Agent Interaction | 15 | 3a documented with call made and response received; 3b documented from Activity log or honestly noted if not triggered |
| Guardrails Audit | 30 | Threat self-test table includes one attempt per class; results honest, including failed mitigations; audit log review answers all three questions; top 3 risks + top 3 mitigations are specific and prioritized |
| Reflection | 15 | Both questions answered with specifics; Question 1 names a real function (not "the engineer"); Question 2 names the single biggest risk expansion and a concrete pre-ship condition |
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

## A Note on the Build-Audit Loop

Part 2 and Part 4 are not separate tasks. The whole point of this assignment is that the audit reveals something the build missed — and you have time to fix it. If your Part 4 threat self-test surfaces a real failure, the appropriate response is to fix it (or document why you can't) before you submit, not to hide it.

A submission that says *"I found a real prompt injection vector during the audit, fixed it by adding [specific mitigation], and re-tested to confirm"* earns more points than one that says *"All threats mitigated."*

---

## Resources

- [Notion Custom Agents — Help Center](https://www.notion.com/help/custom-agents)
- [Notion Agents overview page](https://www.notion.com/product/agents)
- [Rundown AI guide — Use This Hidden Feature to Make Your Notion Agents Autonomous](https://app.therundown.ai/guides/use-this-hidden-feature-to-make-your-notion-agents-autonomous) — the recurring template technique used in Part 2, Step 5
- Your Project 2 Notion knowledge agent — the foundation you are extending
- Module 5 lesson slides — MCP, tool access, permission scoping, blast radius, allowlists
- Module 8 lesson slides — threat classes, audit trails, RBAC, confused deputy, incident response
