# Activity: Version a Prompt in GitHub (No Command Line)

**Module 10 | Solo activity**

---

## What This Activity Is About

In Module 10 you heard that shipped agents need **operations** discipline — including a way to see *what changed* when a prompt stops behaving the way you expect. Professional teams often keep prompts in **version control** so every edit is dated, labeled, and reversible.

This activity uses **GitHub** the same way many beginners do: entirely in the **web browser**. You will not install software. You will not type cryptic commands. You will:

1. Write a prompt in a simple text file on your computer  
2. Put that file on GitHub in a small **project folder** GitHub calls a *repository*  
3. Write a second, improved version of the same prompt on your computer  
4. Update the file on GitHub so GitHub stores **both versions** and shows you the history  

When you are done, you will have seen **versioning** with your own eyes — not as an abstract IT concept, but as “I changed the instructions, and the system remembers the before and after.”

---

## Learning Objectives

By the end of this activity, you will be able to:

- Explain in plain language what a **repository** and a **commit** are on GitHub  
- Store a text prompt on GitHub and give it a clear **commit message**  
- Create a **second version** of the same prompt and upload it as an update, not a brand-new mystery file  
- Open GitHub’s **history** view for a file and identify which change came first and which came second  

---

## A Tiny Vocabulary (Read This Once)

You do not need to become a programmer for this lab. You only need four ideas:

| Term | Plain-language meaning |
|------|-------------------------|
| **GitHub** | A website where you can store files for a project, track changes over time, and share a link with an instructor or teammate. |
| **Repository (“repo”)** | One project’s folder on GitHub. It holds your files. Think “one binder for this assignment.” |
| **Commit** | A saved snapshot of your files at a moment in time. Every commit has a **message** you write — a short note to your future self, e.g. “First draft of intake prompt.” |
| **Version history** | GitHub’s list of commits for a file. You can open an older version to see what it used to say. |

---

## What You Need

- A **computer** (laptop or desktop is easiest; a tablet can work but small screens are fiddly)  
- A **web browser** (Chrome, Safari, Edge, or Firefox)  
- A way to create a **plain text file** on your machine:  
  - **Mac:** TextEdit → Format → Make Plain Text, then save as `my_agent_prompt.txt`  
  - **Windows:** Notepad → Save as `my_agent_prompt.txt` (type the name in quotes if Windows tries to add `.docx`)  
  - **Google Docs / Word:** only if you export or save as **plain text (.txt)** — not required if you use Notepad/TextEdit  
- Your **GitHub account** — [github.com](https://github.com)

---

## Before You Start: Pick a Prompt Topic

You will write a short **system-style prompt** — instructions that would tell an AI agent how to behave for one narrow job. Keep it **fictional and safe**: no real customer data, no real HR cases, no passwords.

**Example topics** (pick one or invent your own):

- A **front-desk triage** bot for a small veterinary clinic (what it should ask first, what it should never promise)  
- A **study-planning** helper for a student (how it should ask clarifying questions, what it should refuse to do, like taking exams for you)  
- A **meeting-notes** assistant for a student club (tone, format of summaries, what counts as a decision vs. a vague idea)

**Length:** roughly half a page — enough that “version 2” is a real improvement (clearer rules, clearer tone, or clearer “do not do this” list), not a single sentence.

---

## Step-by-Step Instructions

### Part A — Write version 1 in a text file

1. Open your plain-text editor (Notepad, TextEdit in plain text mode, or similar).  
2. Type your **first draft** prompt. At the very top, add one line you will keep in both versions, for example:  
   `VERSION: 1`  
   so you can always tell which draft you are looking at.  
3. Save the file on your computer as **`my_agent_prompt.txt`**.  
4. Close the file or leave it open — either is fine.

You have now done step **1** of the activity: a prompt in a **text file**.

---

### Part B — Put the file on GitHub

These steps happen **in the browser** on [github.com](https://github.com). GitHub’s buttons move around slightly over time; if a label does not match exactly, look for the same idea (e.g. “New” / “Add file” / “Upload”).

1. **Sign in** to GitHub.

2. **Create a new empty repository**  
   - Click your **profile picture** (top right) → **Your repositories** (or go to [github.com/new](https://github.com/new)).  
   - Click the green **New** button (or **New repository**).  
   - **Repository name:** something short and unique, e.g. `isys398u-m10-prompt-versioning` or `my-prompt-lab`.  
   - **Description (optional):** e.g. “Class lab — prompt versions.”  
   - Choose **Public** (easiest for turning in a link; if your instructor allows **Private**, you can use that and invite them as a collaborator — follow your syllabus).  
   - Leave **Add a README** unchecked for this lab — you want an **empty** repo so your first upload is clearly *your* file.  
   - Click **Create repository**.

3. **Upload your text file**  
   - GitHub shows an empty-repo page with suggestions. Find **uploading an existing file** or **Add file** → **Upload files**.  
   - Drag **`my_agent_prompt.txt`** from your computer into the browser, or use **choose your files**.  
   - Scroll down to **Commit changes**.  
   - In the **first box** (short summary), type a commit message such as:  
     `Add version 1 of agent prompt`  
   - In the **larger optional box**, you can add one sentence, e.g. “Initial draft for class activity.”  
   - Click **Commit changes** (or **Commit**).

4. **Confirm the file is there**  
   - You should see **`my_agent_prompt.txt`** listed in the file list.  
   - Click the filename. You should see the text of **version 1**.

You have now done step **2**: the prompt file **lives on GitHub** in your repository.

---

### Part C — Write version 2 on your computer

1. Open **`my_agent_prompt.txt`** again on your computer (same file name).  
2. Change the top line to:  
   `VERSION: 2`  
3. Improve the prompt in a way you could explain out loud, for example:  
   - Add a **“Never do this”** section  
   - Add **two example** user questions and ideal short replies  
   - Tighten vague words (“be helpful”) into **checkable** rules (“always ask X before suggesting Y”)  
4. Save the file (**Save** or **Cmd/Ctrl + S**).  

You have now done step **3**: a **new version** of the prompt, still named `my_agent_prompt.txt`.

---

### Part D — Update the same file on GitHub

You want **one** file on GitHub whose **history** shows version 1, then version 2 — not two different filenames unless your instructor says otherwise.

**Recommended path (simplest to understand):**

1. On GitHub, open your repository. Click **`my_agent_prompt.txt`**.  
2. Click the **pencil icon** — GitHub labels this **Edit** or “Edit this file.”  
3. **Select all** the old text in the browser, **delete** it, then open **`my_agent_prompt.txt`** on your computer, **copy all** the new text, and **paste** it into GitHub’s editor.  
4. Scroll down to **Commit changes**.  
5. Write a **new** commit message — different from version 1 — for example:  
   `Version 2 — clearer guardrails and examples`  
6. Click **Commit changes**.

**What just happened:** GitHub did **not** throw away version 1. It stored version 2 as the **new current** file and kept version 1 in the **history**.

---

### Part E — See the version history

1. While viewing **`my_agent_prompt.txt`** on GitHub, look for **History** (sometimes shown as a clock icon or “History” link near the top of the file view).  
2. Open **History**. You should see **at least two commits** — the one from Part B and the one from Part D.  
3. Click an older commit to see what the file **used to say**.  
4. (Optional) Explore **Compare** or diff views if GitHub offers them — you are looking at a **before/after** view of your own words.

This is the core lesson: **versioning** means you can answer “what did we tell the agent on Tuesday?” without guessing.

---

## If Something Goes Wrong

- **“I don’t see Upload files.”** Make sure you are **inside** your repository (you see the repo name at the top), not on your profile home page. Use **Add file** → **Upload files**.  
- **“I created a README by accident.”** You can still upload `my_agent_prompt.txt`; you will just have two files. That is fine.  
- **“I uploaded version 2 as a second file with a different name.”** You still learned upload — for full credit, either rename/consolidate with instructor guidance or repeat Parts B–D once with a single filename so **History** tells a clear story.  
- **“GitHub asks for two-factor authentication.”** Follow GitHub’s prompts; this is normal security, not you doing something wrong.  

---

## Connection to Module 10

Shipped agents drift, get “tweaked,” and break in subtle ways. Keeping prompts (and later, configuration) in a system with **dated commits** and **human-readable messages** is a basic **AgentOps** habit: you are not proving you are a developer; you are proving you can **run the agent like an operation**, not like a one-off chat.

---

*Activity for Module 10 — ISYS 398U Agentic AI Implementation | University of Richmond SPCS*
