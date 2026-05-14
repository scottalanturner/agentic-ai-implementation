import type OpenAI from "openai";

/**
 * Cheap, deterministic "scores" for teaching (0–1). These are not legal judgments
 * or LLM-as-judge; they show how automated signals attach to a trace via
 * Braintrust `logFeedback` → `scores`.
 */
export function computeAutomatedRunScores(
  working: OpenAI.Chat.ChatCompletionMessageParam[],
  iterations: number,
  maxIterations: number,
): Record<string, number> {
  const toolMsgs = working.filter(
    (m): m is OpenAI.Chat.ChatCompletionToolMessageParam => m.role === "tool",
  );

  const usedTools = toolMsgs.length > 0 ? 1 : 0;

  const toolFailures = toolMsgs.filter(
    (m) =>
      typeof m.content === "string" &&
      (m.content.includes("Error executing tool") ||
        m.content.startsWith("Error: tool")),
  );
  const cleanToolExecution =
    toolMsgs.length === 0 ? 1 : toolFailures.length === 0 ? 1 : 0;

  const last = working[working.length - 1];
  let completedWithReply = 0;
  if (last?.role === "assistant" && last.content) {
    const text =
      typeof last.content === "string"
        ? last.content
        : last.content.map((p) => ("text" in p ? p.text : "")).join("");
    completedWithReply = text.trim().length > 0 ? 1 : 0;
  }

  const stoppedBeforeIterationCeiling = iterations < maxIterations ? 1 : 0;

  return {
    used_tools: usedTools,
    clean_tool_execution: cleanToolExecution,
    completed_with_assistant_reply: completedWithReply,
    stopped_before_iteration_ceiling: stoppedBeforeIterationCeiling,
  };
}
