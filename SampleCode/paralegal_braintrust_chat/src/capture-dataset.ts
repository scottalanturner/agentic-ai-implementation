import { randomUUID } from "node:crypto";
import { initDataset, type Dataset } from "braintrust";

let captureDataset: Dataset | null | undefined;

/**
 * Lazily opens the Braintrust dataset used for `/capture` rows (same project as logs).
 */
export function getCaptureDataset(): Dataset | null {
  if (!process.env.BRAINTRUST_API_KEY) {
    return null;
  }
  if (captureDataset === undefined) {
    try {
      captureDataset = initDataset({
        project: process.env.BRAINTRUST_PROJECT_NAME ?? "ISYS398U-ParalegalDemo",
        dataset: process.env.BRAINTRUST_CAPTURE_DATASET ?? "live-captures",
        apiKey: process.env.BRAINTRUST_API_KEY,
        description: "Rows inserted from the paralegal demo when the user prefixes with /capture.",
      });
    } catch (e) {
      console.error("[capture] initDataset failed:", e);
      captureDataset = null;
    }
  }
  return captureDataset;
}

export type CaptureRowArgs = {
  userMessageForModel: string;
  userMessageRaw: string;
  assistantReply: string;
  sessionId: string;
};

export async function insertCaptureRow(args: CaptureRowArgs): Promise<string | null> {
  const ds = getCaptureDataset();
  if (!ds) {
    return null;
  }
  const id = randomUUID();
  ds.insert({
    id,
    input: {
      user_message: args.userMessageForModel,
      session_id: args.sessionId,
    },
    metadata: {
      assistant_reply: args.assistantReply,
      user_message_raw: args.userMessageRaw,
      source: "paralegal_demo_slash_capture",
      captured_at: new Date().toISOString(),
    },
    tags: ["demo", "slash-capture"],
  });
  await ds.flush();
  return id;
}
