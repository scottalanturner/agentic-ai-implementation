# Optional Lab — Your Personal Recipe Agent

**Tools:** Telegram · n8n · OpenRouter  
**Cost:** $0  
**Coding required:** None  
**Time:** About 75–90 minutes (a little less if you already use Telegram)  
**Graded:** No — this is a bonus lab for students who want to build something they'll actually use

---

## What You're Building

You are going to build a bot that lives in Telegram — the free messaging app. Text it a list of whatever is in your fridge and pantry. Every morning at a time you choose, it will automatically send you a recipe based on what you have.

No app to install. No subscription. No code to write.

Here is the whole idea in one picture:

```
You text your bot a pantry list
        ↓
n8n saves the list
        ↓
Every morning at 7 a.m. — automatically:
n8n asks Llama AI: "what can I cook with this?"
        ↓
Your bot texts you the recipe
```

The part that makes this an *agent* rather than just a chatbot: step three happens on its own. You do not have to ask. It just shows up.

---

## The Four Pieces

| Piece | What it does | Cost |
|-------|-------------|------|
| **Telegram** | The app on your phone or computer — how you talk to the bot | Free |
| **OpenRouter** | Gives your bot access to Llama, a free AI model | Free |
| **n8n** | Connects everything together and runs the morning schedule | Free |
| **Your Telegram bot** | The bot account you'll create in Part 1 | Free |
| **The blueprint file** | A ready-made n8n workflow you'll import — no building from scratch | Free |

---

## Part 0 — Before You Start

Spend ten minutes on the setup below before you build anything. It will save you twenty minutes of confusion later.

### What you'll need

- A phone OR a computer (either one works for everything in this lab)
- A working internet connection
- An email address you can check (for the OpenRouter and n8n signups)
- A phone number that can receive a text message (Telegram uses this to make your account)

### Open a "Recipe Bot Notes" doc

During this lab you'll collect four pieces of information that you'll need to paste in later. If you lose any of them, parts of the lab won't work.

**Step 1.** Open a notes app — anything will do. Apple Notes, Google Docs, the Notes app on Windows, Microsoft Word, or even a plain text file all work fine.

**Step 2.** Make a new note called `Recipe Bot Notes`. Type these three lines into it, with a blank space after each colon. You'll fill in the blanks as you go.

```
Bot Token:
Telegram User ID:
OpenRouter API Key:
```

Keep this note open in a separate window or tab. You'll come back to it several times.

> **Keep this note private.** The Bot Token and the OpenRouter API Key are like passwords. Don't post them online or share them with anyone.

### Install Telegram and create an account

If you already use Telegram, skip to Part 1.

**Step 3.** Install Telegram on whichever device you want to use:

- **On an iPhone or iPad:** Open the App Store, search for `Telegram`, and tap **Get**.
- **On an Android phone:** Open the Play Store, search for `Telegram`, and tap **Install**.
- **On a computer:** Go to [telegram.org](https://telegram.org) and click the download link for your computer (Windows, Mac, or Linux). Install the file it downloads.

**Step 4.** Open Telegram. Tap or click **Start Messaging**.

**Step 5.** Type your phone number (with the country code — for the US that's `+1`) and tap **Next**.

**Step 6.** Telegram will text you a 5-digit code. Type it into Telegram.

**Step 7.** Type a first name (a last name is optional). You can also add a profile photo if you want — it isn't needed for this lab.

You now have a Telegram account. The main screen — the one with the search bar at the top and a list of chats below it — is where you'll be doing everything in Part 1.

---

## Part 1 — Create Your Telegram Bot

Telegram lets anyone create a bot. You make one by chatting with a special account called **BotFather** — that's a built-in helper that exists only to create bots. This part takes about five minutes.

**Step 1.** Open Telegram. At the very top of the main screen there's a search bar (it has a magnifying glass icon). Tap or click in it and type `BotFather`.

**Step 2.** In the list of results, look for the one named **BotFather** with a **blue checkmark** next to the name. The blue checkmark means it's the real, official BotFather. Tap it. (If you see other results without the checkmark, ignore them.)

**Step 3.** A chat window will open. At the bottom you'll see a big blue **Start** button. Tap it. (If you don't see the button, type `/start` — that includes the slash — into the message box at the bottom and send it.)

**Step 4.** BotFather will reply with a long welcome message listing many commands. You only need one. In the message box at the bottom, type `/newbot` (with the slash) and send it.

**Step 5.** BotFather will ask: *"Alright, a new bot. How are we going to call it? Please choose a name for your bot."* This is the **display name** — the name that will show at the top of the chat with your bot. Type something simple like `My Recipe Bot` and send it.

**Step 6.** BotFather will then ask for a **username**. This is the unique ID for your bot. It has two rules:
- It must be all one word (no spaces)
- It must end with the word `bot`

Examples that work: `scotts_recipe_bot`, `myrecipes2026bot`, `kitchen_helper_bot`. If BotFather replies *"Sorry, this username is already taken,"* just try another one.

**Step 7.** Once your username is accepted, BotFather will send a message that includes a long code that looks like this:

```
7234567890:AAHabcdefghijklmnopqrstuvwxyz123
```

This is your **Bot Token**. Copy the whole code (tap and hold on a phone, or triple-click on a computer, then copy). Switch to your `Recipe Bot Notes` doc and paste it after `Bot Token:`. Save the note.

> **Important:** Keep your Bot Token private. Anyone who has it can send messages as your bot.

---

### Find your own Telegram User ID

Your bot also needs to know which Telegram account is *yours* so it can send you the morning recipe. Telegram gives every account a number. Here's how to find yours.

**Step 8.** Go back to the main Telegram screen and tap the search bar again. Type `userinfobot` and tap the result named **@userinfobot**. (This is another built-in helper. There is no blue checkmark on this one, but it's safe — it just tells you your account info.)

**Step 9.** Tap **Start** at the bottom (or send `/start`).

**Step 10.** It will instantly reply with a short message that includes a line that says `Id: 1234567890` (your number will be different). That number is your **Telegram User ID**.

**Step 11.** Copy the number and paste it into your `Recipe Bot Notes` doc after `Telegram User ID:`. Save the note.

You now have two of the four pieces filled in. Two to go.

---

## Part 2 — Get Your Free AI Key from OpenRouter

OpenRouter is a website that lets your projects use many different AI models, including a free version of one called Llama (made by Meta). You'll create an **API key** — think of it as a password that lets your bot use Llama.

**Step 1.** Open a web browser and go to [openrouter.ai](https://openrouter.ai). In the top-right corner of the page, click **Sign In**. Choose any sign-in option you like (Google works well — there's no cost, and you won't be charged for anything in this lab).

**Step 2.** Once you're signed in, look at the very top-right of the page. You'll see a small round circle — either your profile photo or a colored circle with your initial in it. Click on it. A small menu will drop down. Click **Keys** in that menu. (On some screens it may say **API Keys** instead. Either is the right one.)

**Step 3.** On the Keys page, click the button labeled **Create Key**. A small box will pop up asking for a name. Type `Recipe Bot` and click **Create**.

**Step 4.** A long code starting with `sk-or-` will appear on the screen. This is your **OpenRouter API Key**. Click the small copy icon next to it (or select the whole code and copy it).

**Step 5.** Switch to your `Recipe Bot Notes` doc and paste the key after `OpenRouter API Key:`. Save the note.

> **Copy it right now.** OpenRouter only shows this key one time. Once you close the box, you can't see it again — you'd have to create a new one.

That's all you need from OpenRouter. The specific AI model (`meta-llama/llama-3.3-70b-instruct:free`) is already baked into the blueprint file you'll import in Part 3 — no need to look it up.

Your notes doc should now have all three pieces filled in. You're done with account setup — the rest of the lab is wiring things together.

---

## Part 3 — Set Up n8n and Import the Blueprint

n8n (pronounced "n-eight-n") is a website where you build little automatic helpers without writing any code. The helpers are called **workflows**, and they're made up of **nodes** (small boxes that each do one job, connected by lines).

You're not going to build the workflow from scratch — that's a lot of clicking. Instead, you'll import a ready-made blueprint file that already has all the nodes and connections in place. Then you'll plug in your accounts and turn it on.

### Sign up for n8n

**Step 1.** Go to [n8n.cloud](https://n8n.cloud) in your browser. Click **Get started for free**.

**Step 2.** Fill in your email, make a password, and click the signup button. n8n may ask a couple of quick questions (what you do, what you'll use it for) — answer however you like; it doesn't affect the lab.

**Step 3.** n8n will set up your workspace. This takes about 30 seconds. When it's done, you'll land on the main n8n screen — usually a page titled **Personal** with a few buttons across the top.

> **A note about cost.** n8n Cloud gives you a 14-day free trial that includes everything you need for this lab. You can finish the lab in one sitting and never pay anything. After 14 days, n8n will ask you to choose a paid plan or stop using it.

### Download the blueprint file

**Step 4.** Find the file `recipe_bot_workflow.json` that came with this lab. (Your instructor will have shared it on Blackboard, in the same place you found this document.)

**Step 5.** Download it to your computer. Put it somewhere easy to find — your Desktop or Downloads folder is fine. **Don't open it** — it'll look like a wall of code. You just need it sitting on your computer so n8n can read it in the next step.

### Import the blueprint

**Step 6.** Back in the n8n tab in your browser, look at the top-right corner. You'll see a button (or a small menu indicated by three dots `...`) for creating things. Click the dropdown arrow next to **Create Workflow**.

**Step 7.** A small menu drops down. Choose **Import from File** (on some versions it says **Import workflow from file** or just **Import**).

**Step 8.** A file picker opens. Navigate to where you saved `recipe_bot_workflow.json`, click it, and click **Open**.

**Step 9.** A new workflow opens on the canvas. You should see **eight boxes (nodes)** arranged in two rows, connected by gray lines:

```
Top row (the pantry-saving path):
[When user texts the bot] → [Ask Llama to clean the pantry] → [Save the pantry] → [Reply to the user]

Bottom row (the morning recipe path):
[Every morning at 7am] → [Load the saved pantry] → [Ask Llama for a recipe] → [Send the morning recipe]
```

Some of the nodes will have a small red dot or warning triangle on them — that's normal. They're telling you they need credentials (accounts to connect to), which you'll add in Part 5. First, take a quick tour so you know what each box does.

**Step 10.** Click **Save** in the top-right corner of n8n. Give it a name like `Recipe Bot` if it asks.

---

## Part 4 — A Quick Tour of the Workflow

You don't have to change anything in this part — just read along and click each node to see how it's set up. Understanding what each box does will make Part 5 (plugging in your accounts) much easier.

### The two paths

Look at the canvas. There are two completely separate chains of boxes — they never touch. The **top row** runs whenever you text the bot. The **bottom row** runs by itself, every morning, on a schedule.

Both rows share the same pantry list (stored in n8n's memory). The top row writes to the list; the bottom row reads from it.

### Tour of the top row (the pantry-saving path)

Click each node to open its settings panel on the right. You don't need to change anything — just look.

**1. When user texts the bot** *(a Telegram Trigger)*
- This is the box that waits for you to send a message to your bot. As soon as a message arrives, the chain runs.

**2. Ask Llama to clean the pantry** *(an HTTP Request)*
- This box sends what you typed to OpenRouter. OpenRouter forwards it to the Llama AI model, with the instruction: *"Extract every food item as a simple list, one item per line."* Llama replies with a tidy list.

**3. Save the pantry** *(a Code node — a small piece of JavaScript)*
- This box takes Llama's clean list and tucks it away in the workflow's memory under the label `pantry`. The bottom row will look for this same label tomorrow morning.

**4. Reply to the user** *(a Telegram send)*
- This box sends you a confirmation message in Telegram showing the list it just saved.

### Tour of the bottom row (the morning recipe path)

**5. Every morning at 7am** *(a Schedule Trigger)*
- This box fires automatically at 7:00 a.m. every single day. **This is the agentic part of the bot** — nothing has to ask it. It just goes.

**6. Load the saved pantry** *(a Code node)*
- This box reaches into the workflow's memory and pulls out the pantry list that the top row saved.

**7. Ask Llama for a recipe** *(an HTTP Request)*
- This box sends the pantry list to Llama with a new instruction: *"You are a friendly home cook. Suggest one simple recipe I can make today using items from my pantry."*

**8. Send the morning recipe** *(a Telegram send)*
- This box sends Llama's recipe to you in Telegram.

That's the whole bot. Now to make it actually work, you need to give each Telegram node a way to log in to your bot, give each Llama node a way to log in to OpenRouter, and tell the morning-recipe sender which Telegram account to send to. That's Part 5.

---

## Part 5 — Plug in Your Accounts and Activate

There are three pieces of wiring to do, in this order:

1. Create your Telegram credential and attach it to all three Telegram nodes
2. Create your OpenRouter credential and attach it to both HTTP Request nodes
3. Type your Telegram User ID into the "Send the morning recipe" node
4. Connect Telegram to n8n (one URL visit, exactly like before)
5. Activate the workflow and test both paths

---

### Step 1 — Create your Telegram credential

You'll create this once, then pick it from a dropdown on each of the three Telegram nodes.

**Step 1.** Click the node **When user texts the bot** to open its settings panel on the right.

**Step 2.** The first field is **Credential to connect with**. It will say *"— None —"* or have a red warning. Click it, then click **+ Create new credential** at the bottom of the dropdown.

**Step 3.** A small popup appears with a field called **Access Token**. Switch to your `Recipe Bot Notes` doc, copy the **Bot Token** you saved in Part 1, and paste it into this field. Click **Save**. You should see a green checkmark and the words **Connection tested successfully**. Close the popup.

**Step 4.** Now click the node **Reply to the user**. In its **Credential to connect with** field, click the dropdown — your bot credential should already be listed (probably called *"Telegram account"*). Pick it. The red warning on this node should disappear.

**Step 5.** Click the node **Send the morning recipe** (the last one in the bottom row). Pick the same credential from its dropdown.

All three Telegram nodes now share the same bot credential.

---

### Step 2 — Create your OpenRouter credential

Same pattern — create it once, attach it to both HTTP Request nodes.

**Step 6.** Click the node **Ask Llama to clean the pantry**. In its settings panel, find the field called **Credential for Header Auth**. Click it, then click **+ Create new credential**.

**Step 7.** A popup opens with two fields:

- In the **Name** field, type exactly: `Authorization`
- In the **Value** field, type the word `Bearer` followed by ONE space, then paste your **OpenRouter API Key** from your notes doc. The whole thing should look like this (with your real key in place of the example):

```
Bearer sk-or-v1-abcdef1234567890yourkeyhere
```

The space between `Bearer` and `sk-or-...` is required. Click **Save**, then close the popup.

**Step 8.** Click the node **Ask Llama for a recipe** (in the bottom row). In its **Credential for Header Auth** field, pick the credential you just made. You do not need to create a new one — it'll appear in the dropdown.

Both Llama-calling nodes are now connected to your OpenRouter account.

---

### Step 3 — Tell the morning recipe where to send itself

**Step 9.** Click the node **Send the morning recipe**.

**Step 10.** Find the field called **Chat ID**. It currently has the placeholder text `PASTE_YOUR_TELEGRAM_USER_ID_HERE`. Delete that whole placeholder, then type your **Telegram User ID** from your notes doc (just the plain number, like `1234567890` — no quotes, no brackets, no equals sign).

> **Why a plain number here?** The other Telegram-sending node (**Reply to the user**) replies to whoever just sent the message — so it reads the chat ID out of the incoming message automatically. This one is different: there's no incoming message because the schedule woke it up, so you have to tell it exactly where to send the recipe.

**Step 11.** Click **Save** at the top of the screen to save your changes.

---

### Step 4 — Connect Telegram to n8n

Right now, your bot exists, n8n is wired up, but Telegram doesn't yet know to forward incoming messages to your n8n workflow. This step introduces them with one URL visit.

**Step 12.** Click the node **When user texts the bot**. At the top of the settings panel, just under the words "Telegram Trigger", there's a small section labeled **Webhook URLs**. Click **Test URL** to switch to **Production URL** — this is the URL that works when the workflow is Active. Click the copy icon next to the address that appears.

**Step 13.** Open a new browser tab. You're going to build a special web address (URL) in the address bar that combines your Bot Token and your n8n Webhook URL. Here's the template:

```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=<YOUR_N8N_WEBHOOK_URL>
```

Replace **both** parts in angle brackets — and **delete the angle brackets themselves**. A worked example: if your Bot Token is `7234567890:AAHabc` and your Webhook URL is `https://yourworkspace.app.n8n.cloud/webhook/abc123`, you would type:

```
https://api.telegram.org/bot7234567890:AAHabc/setWebhook?url=https://yourworkspace.app.n8n.cloud/webhook/abc123
```

Notice three things:
- The word `bot` runs right into the token with no space and no brackets
- The angle brackets `<` and `>` are gone
- The whole thing is one long line with no spaces

**Step 14.** Press **Enter**. You should see a reply like this in the browser:

```json
{"ok":true,"result":true,"description":"Webhook was set"}
```

If you see `"ok":true`, Telegram and n8n are now connected. If you see `"ok":false`, check that you replaced both pieces correctly and that you removed the brackets, then try again.

---

### Step 5 — Activate and test

**Step 15.** Back in n8n, look at the top of the screen near the workflow name. There's a toggle switch labeled **Inactive**. Click it to flip to **Active**. n8n may show a confirmation popup — click whatever the "yes, activate" button says.

**Step 16. Test the pantry-saving path.** Open Telegram, find your bot (search for the username you gave it in Part 1), and text it something like:

> *I've got a dozen eggs, some leftover rice, soy sauce, garlic, two carrots, and olive oil.*

Wait about 15 seconds. Your bot should reply with a checkmark message and a clean list. If it does — the top row works. If not, see **What Can Go Wrong** below.

**Step 17. Test the morning recipe path without waiting until 7 a.m.** Back in n8n, click the **Every morning at 7am** node. At the top of its settings panel, look for a button labeled **Execute Step** (older versions say **Execute Node** or **Test Step**). Click it. This pretends that the 7 a.m. alarm just went off and runs the whole bottom row right now.

Within about 30 seconds, a recipe should arrive in your Telegram. If it does — your entire bot works, and tomorrow at 7 a.m. it'll deliver a recipe on its own. 🎉

---

## What Can Go Wrong

### My bot doesn't reply when I text it

The most common cause is that Telegram isn't yet forwarding messages to n8n. To check, open a browser tab and put together a URL like this — replacing the angle-bracket part with your Bot Token (and removing the brackets too):

```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo
```

Press Enter. You should see a chunk of text that includes a line starting with `"url":` followed by your n8n Webhook URL. If the `url` line is empty (`"url":""`), the webhook never got set. Go back to **Step 12–14** in Part 5 (the "Connect Telegram to n8n" steps) and try again.

Also check that:
- The workflow is set to **Active** (not Inactive)
- The Telegram Trigger's Webhook URL is the **Production URL**, not the Test URL

### n8n shows a red box with an error on an HTTP Request node

Click the red box. A panel will open showing the error message. The two most common errors:

- **401 Unauthorized** — Your OpenRouter API Key is wrong, or you forgot the word `Bearer` (with one space after it) in front of the key. Click the HTTP Request node, open the Header Auth credential, and fix the **Value** field.
- **Model not found** — The free Llama model on OpenRouter may have been renamed. Visit [openrouter.ai/models](https://openrouter.ai/models), search for `llama`, find a current free version, and replace `meta-llama/llama-3.3-70b-instruct:free` in both HTTP Request nodes (the **JSON** body field on each) with the new Model ID.

### The morning recipe is generic — it doesn't seem to know my pantry

This usually means the morning path couldn't find a saved pantry. Two things to check:

1. **Did you text the bot a pantry first?** The morning path reads from memory — if you never saved anything, there's nothing to read. Text your bot a pantry list, wait for the confirmation, then re-test the morning path.
2. **Static data only persists between *active* runs.** n8n only saves the pantry to memory when the workflow runs in Active mode (triggered by a real Telegram message or schedule). If you tested using **Execute Step** manually, the save may not have stuck. Send your bot a real Telegram message instead.

### The bot replies but the list looks weird

Llama sometimes adds extra commentary, like *"Sure! Here's your list..."* before the items. You can tighten the prompt — click the **Ask Llama to clean the pantry** node, find the **JSON** body field, and edit the sentence that starts *"The user just told me..."*. The prompt is plain English — add something like *"Do not include any introduction or closing remarks — just the bare list."*

---

## (Optional) Add Voice Input

If you want to speak your pantry instead of typing it, you can add voice transcription using Groq — a free speech-to-text service.

**What changes:** You add two extra nodes to the top row of the workflow, between the **When user texts the bot** node and the **Ask Llama to clean the pantry** node. The first new node downloads the voice file from Telegram. The second sends it to Groq, which converts it to text. After that, everything flows to Llama exactly as before.

**To get started:**

1. Go to [console.groq.com](https://console.groq.com) and create a free account
2. Under **API Keys**, create a key and copy it
3. In your workflow's top row, add an **IF** node after the Telegram Trigger — set it to check whether `{{ $json.message.voice }}` exists (meaning: is this message a voice note or just text?)
4. On the "yes" path, add an **HTTP Request** node to download the audio file from Telegram, then another **HTTP Request** node to send it to Groq's transcription endpoint at `https://api.groq.com/openai/v1/audio/transcriptions`
5. The text that comes back from Groq flows into the **Ask Llama to clean the pantry** node the same way `$json.message.text` did before

A complete walkthrough for this step is in the n8n community forum — search for **"n8n Groq Whisper Telegram voice"**.

---

## Reflection

Not graded — but worth five minutes of thought.

> **The schedule trigger is what makes this an agent.** It acts without being asked. What else in your work could run on a schedule — checking something, summarizing something, sending a nudge — without you remembering to trigger it?

> **You saved state.** The pantry list persists from one session to the next. Most chatbots forget everything when the conversation ends. Where does that kind of memory matter in the agents you are thinking about building?
