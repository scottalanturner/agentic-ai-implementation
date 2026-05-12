# Image Prompt Conventions — ISYS 398U

A standard for prompt-writing across all modules so the first round of images is usable without rework. Establishes when to generate an image, when not to, what text appears on the image, and how to write the prompt.

---

## Why this changes

The existing approach in Modules 2 and 3 produces large, beautiful, text-free illustrations. The problem is what students see: an image with no anchor — a desk, a calculator, a gavel — and no way to tell what concept the slide is teaching until the instructor narrates it. That puts every slide's weight on the instructor's voice.

The fix is not "more text" — it's **the right amount of text in the right places**, rendered in the same colored-pencil sketch style so the visual identity holds. Some slides keep visuals as the main event. Some slides become text-only (with sketch-style framing). Reflection slides become sketches that *replace* the bullet UI, with the prompt rendered into the art.

---

## Visual identity (every slide)

These hold across every image in every module.

- **Style:** colored-pencil sketch on a solid white background
- **Aspect:** widescreen 16:9
- **Color palette:** muted, restrained — warm earth tones with one or two accent colors per image
- **Text inside an image:** always hand-lettered in the same sketch style as the art — never typeset, never sharp serif/sans-serif
- **Mood:** warm, considered, professional. No clip-art energy, no whimsy, no startup-illustration look

---

## The five slide categories

Every slide fits one of these. The category determines the prompt rules and where text lives.

### 1. Text-only slides

**When:** Learning Objectives (top of module), Key Takeaways (end of module). Any slide whose entire content is a numbered or bulleted list students need to *read*.

**Treatment:** Native PowerPoint text — no image generation. The visual identity is preserved by a sketch-style border element (a hand-drawn rule, a corner doodle) that the tooling adds as a template. The text itself is typeset for readability.

**Lesson-file marker:** No `[Image prompt: ...]` block. The tooling already skips image generation when no prompt is present.

### 2. Title slides

**When:** Module title slide at the top of every module.

**Treatment:** Full-bleed sketch with the module title and number rendered as **hand-lettered text inside the image**. One iconic visual element that captures the module's theme (Module 3's gavel was the right idea — just needs the title rendered into the sketch).

**Text in image:** Module number, module title, course code. Optionally a one-line subtitle. Nothing more.

### 3. Sketch reflection slides

**When:** Any `### SLIDE: Reflect — [topic]` slide.

**Treatment:** A colored-pencil sketch *that includes the reflection prompt as part of the composition* — the prompt is rendered into the image, not laid on top of it. The visual element (a thinking figure, a notebook with a pencil, a desk lamp) frames the prompt. Replaces the existing blockquote-with-bullets UI entirely.

**Text in image:** The full reflection prompt (typically 25–50 words). The "60-second solo" cue can be a hand-lettered note in a corner. Bullet sub-points should be hand-lettered with simple bullet dots.

**Why this works:** Reflection slides are quiet moments — students read and think. The sketch frames the prompt visually so the slide isn't just an ugly text block, while the prompt remains the focal content.

### 4. Concept illustration slides

**When:** The majority of teaching slides — opener, customer stories, four-stages, grounding ladder, hallucinated citations, etc. Any slide whose primary job is to illustrate a single concept the instructor will narrate.

**Treatment:** A colored-pencil sketch that illustrates the concept, with **one short anchor phrase rendered in hand-lettering inside the image**. The phrase is the headline a student should retain — usually drawn from the slide's bold lead line or one of the talking-point key terms.

**Text in image (rules):**
- Slide title (rendered hand-lettered at top or as part of the composition)
- One anchor phrase (1–8 words) drawn from the slide's bold lead or a key talking-point term
- Optional: 2–4 short labels on parts of the illustration (e.g., labeling the four stages of the pipeline)
- **Never:** full sentences over 10 words, paragraphs, bullet lists in the image

**Examples of anchor phrases:**
- For Opener — the "two answers" problem: *Confidence without custody*
- For Act 1 — Ungrounded: *The model knows the words. It doesn't know your world.*
- For Hallucinated citations: *The citation that doesn't exist*
- For Customer story — Asana: *Grounding attaches to artifacts*

### 5. Table / data slides

**When:** Modes table, grounding failures table, three-layer memory, any slide whose content is a table or labeled structure where rows, columns, or alignment carries meaning.

**Treatment:** A two-step pipeline. The table is rendered locally to a clean PNG (deterministic, exact), then sent to OpenAI's image edit API with a stylization prompt that says "re-render in colored-pencil sketch style, preserve all text and structure." The colored-pencil version becomes the slide image. This is the only reliable way to get sketch-style tables — pure text-to-image loses rows, drops cells, and invents text.

**Workflow (3 steps):**

1. **Local render.** The build script parses the markdown table, renders it to PNG using a deterministic local renderer (HTML + headless-browser screenshot is most reliable; matplotlib also works for simple tables). Output: `slide_NN_table.png` with crisp, readable, but visually plain table.
2. **Stylize via OpenAI image edit.** The script calls `client.images.edit(image=open(slide_NN_table.png), prompt=...)` with a prompt that asks the model to redraw the table in the colored-pencil sketch style while preserving the text and grid structure exactly. Output: `slide_NN.png` — sketch-style table.
3. **Drop into PPTX.** Same slide layout as concept slides — full-bleed image, no PPT-native table on the slide.

**Stylization prompt template (image edit):**

> *Redraw this table in colored-pencil sketch style on a solid white background. Preserve every word, every row, and every column exactly as shown. Hand-letter all text in the same casual pencil style throughout. Replace the rigid table borders with loose, slightly-imperfect hand-drawn pencil lines. Keep the layout, alignment, and structure unchanged — only the visual aesthetic changes. Muted earth-tone palette with one accent color.*

**Risks worth knowing:**

- Image models can still distort small text on tables with many cells. Verify text fidelity on every generated table. If the model drops a row or rewrites a word, regenerate or fall back to a stricter local-render-only path with hand-drawn fonts.
- Tables with five or more columns are the highest risk. Three to four columns generally hold up well.
- The model occasionally adds decorative flourishes the prompt didn't ask for. Iterating once or twice is normal.

**Lesson-file marker:** Tables are detected by the existing markdown table syntax — no separate prompt block needed. The build script switches to the table-render-then-stylize pipeline automatically when it sees a table in a slide section.

**The same pattern extends to structurally-anchored concept slides** (Four stages, Grounding ladder, Three-layer memory) — render a clean structural skeleton locally, then stylize via image edit. This eliminates the "the model drew six stages instead of four" failure mode. Worth considering as a phase-two extension after tables are working.

---

## Prompt-writing rules (when generating an image)

Use these for both title slides (category 2), reflection slides (category 3), and concept illustration slides (category 4).

**Required prompt elements, in this order:**

1. **Aspect and style** — *"Widescreen 16:9, sketched with colored pencils on a solid white background."*
2. **Scene** — what the illustration shows. Concrete objects and posture, not abstract concepts. ("A wooden desk with a single document under a lamp" beats "an illustration of grounding.")
3. **Text to render** — explicit: *"Hand-lettered title 'Customer story — Asana' across the top in casual marker style. The phrase 'Grounding attaches to artifacts' written in pencil along the bottom right."* List every text element you want, where it goes, and its style.
4. **Composition cue** — what's the focal point, where does the eye land first
5. **Mood** — one or two adjectives. Calm, considered, deliberate, uneasy, decisive, warm, etc.

**Rules of thumb:**

- Image-generation models can render short phrases reliably but stumble on long text. Keep each text element under 10 words.
- Always say *"hand-lettered"* — not "text", not "typed". The lettering should look drawn, not printed.
- Quote phrases use rendered quotation marks (the generator handles them fine).
- The white background is critical for the sketch identity. Always state it explicitly.
- If a slide has a key number or stat, render it (e.g., *"the number 80% written large in the upper-right corner in pencil"*).

**What to avoid in prompts:**

- "Cinematic", "photorealistic", "3D render", "digital art" — these conflict with the colored-pencil identity
- Long instruction paragraphs about mood — the model loses focus
- Asking for diagrams with many labeled parts unless you list each label specifically
- Naming brand logos to be rendered (the generator handles brand names as text but not as logos reliably)

---

## Module 4 — slide categorization (proposed)

The 25 slides in `m04_make_your_agent_an_expert.md`:

| # | Slide title | Category |
|---|---|---|
| 1 | Title — Make Your Agent an Expert on Your Company | **Title** |
| 2 | Opener — the "two answers" problem | **Concept** |
| 3 | Act 1 — Ungrounded answer (what goes wrong) | **Concept** |
| 4 | Act 2 — Grounded answer (what changes) | **Concept** |
| 5 | Why HR is the example | **Concept** |
| 6 | The line to remember | **Concept** *(quote-driven; the line itself is the anchor)* |
| 7 | Customer story — Asana | **Concept** |
| 8 | Customer story — Notion | **Concept** |
| 9 | Customer story — HubSpot | **Concept** |
| 10 | Activity — Two Answers, Live | **Concept** *(activity slides treated as concept slides; the anchor is the activity name + tools)* |
| 11 | Reflect — your Project 1 Agent Card | **Sketch reflection** |
| 12 | What changes when documents are attached | **Table** |
| 13 | Three-layer memory | **Concept** *(three labeled icons in one image, one tagline per layer — see treatment note below)* |
| 14 | Layer 4 — Memory & Context Engineering | **Skip prompt** — image already exists in `images/` and will be inserted at PPTX assembly time |
| 15 | Reflect — memory layers | **Sketch reflection** |
| 16 | Four stages — chunk, embed, retrieve, generate | **Concept** *(four labeled stages in the illustration)* |
| 17 | Activity — Build Your Own Knowledge Agent | **Concept** |
| 18 | Grounding ladder | **Concept** *(four labeled rungs)* |
| 19 | Reflect — governance ownership | **Sketch reflection** |
| 20 | Grounding failures — the four ways RAG breaks | **Table** |
| 21 | Hallucinated citations — the one to watch | **Concept** |
| 22 | Wrong access — when the right answer is the wrong leak | **Concept** |
| 23 | Activity — Failure Detective: The Conflicting Syllabus | **Concept** |
| 24 | Activity — Build a Real Chatbot in Chatbase | **Concept** |
| 25 | Key takeaways — Module 4 | **Text-only** |

*(Learning Objectives also sit at the top of the lesson as a text-only slide; not currently numbered as a `### SLIDE:` entry — worth adding one explicitly if we want it in the deck.)*

**Treatment note — Three-layer memory (slide 13):** Concept slide with three labeled sketch icons across one image — *a library* for long-term memory, *a whiteboard* for working memory, *a signed form / ledger* for transactional memory. Each icon gets a short hand-lettered tagline beneath it:

- *Long-term memory: policies, CRM history, wikis*
- *Working memory: this conversation*
- *Transactional memory: IDs, approvals, ticket numbers*

No "durable, versioned, permissioned" extras — those become spoken talking points only.

**Summary of work this implies for Module 4:**

- **2 text-only slides** (Learning Objectives if added as a slide, Key Takeaways) — no image prompts needed
- **1 title slide** — sketch + module title rendered in image
- **3 sketch reflection slides** — sketch + reflection prompt rendered in image
- **2 table slides** (Modes table, Grounding failures table) — rendered locally via markdown → PDF → PNG, then stylized via OpenAI image edit
- **1 image-already-exists slide** (Layer 4) — skip prompt entirely; the existing image in `images/` gets inserted at PPTX assembly
- **15 concept illustration slides** — sketch + anchor phrase rendered in image (includes Three-layer memory, Four stages, Grounding ladder as labeled-parts variants, and the four activity slides)

---

## Example prompts (for buy-in)

Three worked examples to make the rules concrete. If these feel right, I'll write the rest of Module 4 in this style.

### Example A — Concept slide

**Slide:** Opener — the "two answers" problem
**Anchor phrase to render:** *"Confidence without custody"*

Widescreen 16:9, sketched with colored pencils on a solid white background. Two nearly identical printed documents lying side by side on a wooden desk — same length, same clean formatting, same professional appearance. One has faint green checkmarks barely visible in the margins; the other has no marks. A single hand rests near the documents, hesitating between them. Hand-lettered title across the top in casual pencil style: **The "two answers" problem**. Beneath the documents in smaller hand-lettering: *Confidence without custody.* Composition close-in, slightly off-center, the pair of documents the clear focal point. Mood: uneasy — the danger of surfaces.

### Example B — Sketch reflection slide

**Slide:** Reflect — your Project 1 Agent Card
**Prompt text to render** (paraphrased onto the image, in 2–3 hand-lettered blocks):
- *Reflect — 60 seconds, solo*
- *Pull up your Agent Card from Project 1.*
- *Find one sentence you now disagree with.*
- *Was the mistake about scope, data, users, or success metrics?*

Widescreen 16:9, sketched with colored pencils on a solid white background. A small notebook open on a desk with a pencil resting across the page. The page is filled with hand-lettered text rendered in the same colored-pencil style. At the top in larger letters: **Reflect — 60 seconds, solo**. Below it in slightly smaller lettering: *Pull up your Agent Card from Project 1. Find one sentence you now disagree with. Was the mistake about scope, data, users, or success metrics?* A single coffee cup at the corner of the desk. Mood: quiet, considered, deliberate. No other text or imagery — the notebook page is the focal element.

### Example C — Concept slide with labeled parts

**Slide:** Four stages — chunk, embed, retrieve, generate
**Labels to render:** *Chunk · Embed · Retrieve · Generate*

Widescreen 16:9, sketched with colored pencils on a solid white background. Four numbered boxes arranged left to right with arrows between them, drawn in the loose colored-pencil style. Box 1: a stack of pages being cut into smaller pieces. Box 2: those pieces being placed onto a grid of coordinates. Box 3: a hand pulling a small subset of those coordinates out into a separate pile. Box 4: a document being written, with one of the retrieved pieces visible as a citation. Each box has its label hand-lettered above it in the same pencil style: *Chunk · Embed · Retrieve · Generate*. Hand-lettered title across the top: **The RAG pipeline — four stages**. Composition wide and orderly, left-to-right flow obvious. Mood: methodical, instructive.

---

## Resolutions (locked)

1. **Three-layer memory** — concept slide with three labeled icons + short tagline per layer. No second-level descriptors in the image. *Resolved.*
2. **Layer 4** — image already exists in the module's `images/` folder and gets inserted at PPTX assembly. No prompt written. *Resolved.*
3. **Activity slides** — concept slide treatment with the activity name and key action rendered in the image. *Resolved.*
4. **Tooling** — three changes required (see Tooling section below).

---

## Tooling changes required

The current `build_module_pptx.py` enforces "no text overlaid on images" and "all text in speaker notes." For the new conventions:

- **Text-only slides:** add a native PPT template with a small sketch-style border element. No image generation.
- **Reflection + concept slides:** keep full-bleed image; text is now rendered *in* the image, not overlaid by PPT.
- **Table slides:** new pipeline — `markdown table → PDF (pandoc + xelatex) → PNG (pdftoppm) → trim (ImageMagick) → stylize (OpenAI image edit)`. The final stylized PNG is inserted as a full-bleed image. **No Playwright, no HTML.** All four tools (pandoc, xelatex, pdftoppm, ImageMagick) are likely already on Scott's Mac via Homebrew; if not, they're one `brew install` away each.

The table pipeline is being built and tested as a standalone prototype first — `Application/ImageGen/test_table_render.py` — before integration into `build_module_pptx.py`. Once that prototype renders a clean PNG for a real Module 4 table, the OpenAI stylization step and the integration into the build script come next.

---

## Next step

Build and test the standalone table-render prototype on Module 4's "What changes when documents are attached" table. Show the output before integrating anything into the production tooling.
