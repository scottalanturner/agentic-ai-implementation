import "dotenv/config";
import cors from "cors";
import express from "express";
import type OpenAI from "openai";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { randomUUID } from "node:crypto";
import { initLogger } from "braintrust";
import { WhileLoopAgent } from "./agent.js";
import { getAllTools } from "./tools.js";
import { insertCaptureRow } from "./capture-dataset.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/** If the user message starts with `/capture`, strip it for the model and save this turn to a Braintrust dataset after success. */
const CAPTURE_PREFIX = /^\/capture\s*/i;

const SYSTEM_PROMPT = `You are a litigation paralegal assistant at a mid-size firm (mock demo). You help with docket lookups, deadlines, e-filing status checks, and preliminary conflict screening.

Rules:
- Use the provided tools whenever the user asks for matter-specific facts, dates, filings, or conflicts. Do not invent matter ids, dates, or filing statuses.
- After tool results, summarize in plain English for a busy paralegal.
- Never claim this is real legal advice or a real conflict clearance; say data is from the practice demo system when relevant.
- If the user is vague (e.g. "the container case"), use search_matters first.`;

if (!process.env.BRAINTRUST_API_KEY) {
  console.warn(
    "[paralegal demo] BRAINTRUST_API_KEY is missing — tracing will fail until you add it to .env",
  );
}

initLogger({
  projectName: process.env.BRAINTRUST_PROJECT_NAME ?? "ISYS398U-ParalegalDemo",
  apiKey: process.env.BRAINTRUST_API_KEY,
});

const agent = new WhileLoopAgent({
  tools: getAllTools(),
});

type Turn =
  | OpenAI.Chat.ChatCompletionUserMessageParam
  | OpenAI.Chat.ChatCompletionAssistantMessageParam;

const sessions = new Map<string, Turn[]>();

const app = express();
app.use(cors());
app.use(express.json({ limit: "1mb" }));
app.use(express.static(path.join(__dirname, "../public")));

app.post("/api/chat", async (req, res) => {
  try {
    const rawMessage = req.body?.message;
    const sessionId =
      typeof req.body?.sessionId === "string" && req.body.sessionId.length > 0
        ? req.body.sessionId
        : randomUUID();

    if (typeof rawMessage !== "string" || !rawMessage.trim()) {
      res.status(400).json({ error: "message (non-empty string) required" });
      return;
    }

    const trimmed = rawMessage.trim();
    const captureRequested = CAPTURE_PREFIX.test(trimmed);
    const messageForModel = captureRequested
      ? trimmed.replace(CAPTURE_PREFIX, "").trim()
      : trimmed;

    if (captureRequested && !messageForModel) {
      res.status(400).json({
        error:
          "After /capture, add your question on the same line (e.g. /capture What is the status of EF-88402?).",
      });
      return;
    }

    const history = sessions.get(sessionId) ?? [];
    history.push({ role: "user", content: messageForModel });

    const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [
      { role: "system", content: SYSTEM_PROMPT },
      ...history,
    ];

    const reply = await agent.run(messages);
    history.push({ role: "assistant", content: reply });
    sessions.set(sessionId, history);

    let captured = false;
    let captureRecordId: string | null = null;
    let captureError: string | null = null;
    if (captureRequested) {
      try {
        captureRecordId = await insertCaptureRow({
          userMessageForModel: messageForModel,
          userMessageRaw: trimmed,
          assistantReply: reply,
          sessionId,
        });
        captured = captureRecordId !== null;
        if (!captured) {
          captureError =
            "Dataset capture skipped (set BRAINTRUST_API_KEY, or check server logs for initDataset errors).";
        }
      } catch (err) {
        captureError = err instanceof Error ? err.message : String(err);
        console.error("[capture] insert failed:", err);
      }
    }

    res.json({
      reply,
      sessionId,
      captured,
      captureRecordId: captureRecordId ?? undefined,
      captureDataset:
        process.env.BRAINTRUST_CAPTURE_DATASET ?? "live-captures",
      captureError: captureError ?? undefined,
    });
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e);
    console.error(e);
    res.status(500).json({ error: msg });
  }
});

const port = Number(process.env.PORT) || 3847;
app.listen(port, () => {
  console.log(
    `Paralegal demo: http://localhost:${port}\nBraintrust project: ${process.env.BRAINTRUST_PROJECT_NAME ?? "ISYS398U-ParalegalDemo"}`,
  );
});
