# Activity: MCP Server Evaluation — Find, Read, and Assess

**Module 5 | Estimated time: 15 minutes | Solo activity**

---

## What This Activity Is About

Before an organization connects an MCP server to an AI agent, someone needs to do the work of reading it carefully and asking hard questions. That person might be you — whether you're a manager, an analyst, an IT liaison, or a consultant.

In this activity, you'll browse a real directory of MCP servers, pick one that's relevant to a context you know, and write a short but structured risk assessment of what that connection would actually mean.

---

## Learning Objectives

By the end of this activity, you will be able to:

- Find and read an MCP server listing to understand what capabilities it exposes
- Identify what data or systems an agent would gain access to through that server
- Describe the potential consequences if that access were misused or went wrong
- Articulate the conditions under which you'd recommend connecting a server

---

## Materials Needed

- A web browser
- Access to **[mcp.so](https://mcp.so)** — a free, public directory of MCP servers. No account required.
- Something to write in (a document, a notes app, anything)

---

## Background: What Is an MCP Server Listing?

The site [mcp.so](https://mcp.so) catalogs MCP servers that developers have published. Each listing typically includes:

- **Name** — what the server is called
- **Description** — what it connects to and what it does
- **Tools** — specific actions the server makes available to an agent (e.g., "create issue," "send message," "read file")

Think of each listing as the resume of a capability you might give to an AI agent. Your job is to read that resume critically.

---

## Step-by-Step Instructions

### Step 1 — Pick a context (2 minutes)

Choose one of the following as your frame for this activity:

- A job you currently hold or have held
- An internship or volunteer role
- A student organization, club, or campus department
- A company or organization you've researched or know well

Write down: **What is the main business function or workflow you want to explore?**

Examples: customer support, project management, software development, HR recruiting, financial reporting, marketing campaigns.

### Step 2 — Browse mcp.so (5 minutes)

1. Go to **[https://mcp.so](https://mcp.so)** in your browser.
2. Use the search bar at the top to search for a tool or platform relevant to your chosen business function.
   - Try search terms like: `slack`, `github`, `salesforce`, `google sheets`, `jira`, `notion`, `hubspot`, or the name of any tool your context uses.
3. Click on one server listing that looks relevant.
4. Read the full listing — pay close attention to:
   - The **description** (what does this connect to?)
   - The **tools list** (what specific actions can an agent take?)
   - Any **permissions or scopes** mentioned

### Step 3 — Write your risk assessment (8 minutes)

Write a structured paragraph of **150–200 words** that answers all four of these questions:

1. **Access:** What does this server give an agent access to? Be specific — list the systems, data types, or actions involved.
2. **Data exposure:** What data would leave the organization if this server were connected? Think about what gets sent to the AI model as context.
3. **Blast radius:** What's the worst realistic outcome if the agent is confused, manipulated, or given a bad instruction while connected to this server? What could go wrong, and how bad could it get?
4. **Go / No-go conditions:** What would need to be true before you'd recommend connecting this server? Think about: scope limits, approval workflows, audit logging, reversibility of actions.

Your paragraph should read as professional analysis — the kind of thing you'd send to a manager or include in a vendor review.

---

## Worked Example

Here is an example of a completed assessment for the **Slack MCP server**, to show you the level of analysis expected. Your paragraph does not need to look exactly like this — but it should be similarly specific and grounded.

---

**Server evaluated:** Slack MCP Server  
**Context:** Internal communications at a mid-size company

> The Slack MCP server gives an AI agent the ability to read messages from channels, send messages, create channels, and look up user profiles. That means an agent connected to Slack has access to potentially sensitive internal conversations — including discussions about personnel, strategy, clients, and finances — depending on which channels it can read. Any content from those channels that the agent references becomes part of the context sent to the underlying language model, which may be hosted outside the organization's environment. The worst-case blast radius includes: an agent posting a confusing or incorrect message to a public channel at scale, leaking a private conversation by referencing it in a response to the wrong person, or being manipulated through a malicious message in a channel it monitors (prompt injection). Before I'd recommend connecting this server, I'd want to see: channel-level access controls (not org-wide read access), message-send limited to designated channels only, full audit logging of every action, and a clear human review step before any message goes out to more than one person.

---

## What to Do With Your Assessment

Hold on to this paragraph. You may be asked to share it during class discussion or submit it as part of a module check-in.

If you want to go further: pick a second server from a different category (e.g., a file storage server if you evaluated a messaging server) and note how the risk profile changes.

---

*Activity for Module 5 — ISYS 398U Agentic AI Implementation | University of Richmond SPCS*
