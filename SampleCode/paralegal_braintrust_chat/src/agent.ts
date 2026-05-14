import OpenAI from "openai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
import { traced, wrapOpenAI } from "braintrust";
import type { Tool } from "./tools.js";
import { computeAutomatedRunScores } from "./run-scores.js";

export interface AgentOptions {
  model?: string;
  maxIterations?: number;
  tools: Tool[];
}

export class WhileLoopAgent {
  private client: OpenAI;
  private tools: Map<string, Tool>;
  private model: string;
  private maxIterations: number;

  constructor(options: AgentOptions) {
    this.client = wrapOpenAI(
      new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
      }),
    );
    this.tools = new Map(options.tools.map((t) => [t.name, t]));
    this.model = options.model ?? process.env.OPENAI_MODEL ?? "gpt-4o-mini";
    this.maxIterations = options.maxIterations ?? 12;
  }

  private formatToolsForOpenAI(): OpenAI.Chat.ChatCompletionTool[] {
    return Array.from(this.tools.values()).map((tool) => ({
      type: "function" as const,
      function: {
        name: tool.name,
        description: tool.description,
        parameters: zodToJsonSchema(tool.parameters as z.ZodType, {
          target: "openApi3",
        }) as Record<string, unknown>,
      },
    }));
  }

  /**
   * Full message list including system as first message (see Braintrust AgentWhileLoop cookbook).
   */
  async run(messages: OpenAI.Chat.ChatCompletionMessageParam[]): Promise<string> {
    return traced(
      async (span) => {
        span.log({ input: messages });

        const working = [...messages];
        let iterations = 0;
        let done = false;

        while (!done && iterations < this.maxIterations) {
          const iterationNum = iterations + 1;

          await traced(
            async (iterationSpan) => {
              iterationSpan.log({ input: working });

              const response = await this.client.chat.completions.create({
                model: this.model,
                messages: working,
                tools: this.formatToolsForOpenAI(),
                tool_choice: "auto",
              });

              const message = response.choices[0]?.message;
              if (!message) {
                iterationSpan.log({ error: "empty_choices" });
                done = true;
                return;
              }

              working.push(message);
              iterationSpan.log({ output: message });

              if (message.tool_calls?.length) {
                const toolResults = await Promise.all(
                  message.tool_calls.map((toolCall) => {
                    if (toolCall.type !== "function") {
                      return Promise.resolve({
                        role: "tool" as const,
                        tool_call_id: toolCall.id,
                        content: "Unsupported tool call type in demo.",
                      });
                    }
                    const fn = toolCall.function;
                    return traced(
                      async (toolSpan) => {
                        const tool = this.tools.get(fn.name);
                        if (!tool) {
                          const err = `Error: tool ${fn.name} not found`;
                          toolSpan.log({ error: err });
                          return {
                            role: "tool" as const,
                            tool_call_id: toolCall.id,
                            content: err,
                          };
                        }
                        try {
                          const args = JSON.parse(fn.arguments || "{}") as unknown;
                          toolSpan.log({ input: args });
                          const result = await tool.execute(args);
                          toolSpan.log({ output: result });
                          return {
                            role: "tool" as const,
                            tool_call_id: toolCall.id,
                            content: result,
                          };
                        } catch (err) {
                          const msg = err instanceof Error ? err.message : String(err);
                          toolSpan.log({ error: msg });
                          return {
                            role: "tool" as const,
                            tool_call_id: toolCall.id,
                            content: `Error executing tool: ${msg}`,
                          };
                        }
                      },
                      {
                        name: fn.name,
                        type: "tool",
                        event: {
                          metadata: {
                            tool_name: fn.name,
                            tool_call_id: toolCall.id,
                          },
                        },
                      },
                    );
                  }),
                );
                working.push(...toolResults);
              } else if (message.content) {
                done = true;
              }
            },
            {
              name: `iteration_${iterationNum}`,
              type: "task",
              event: {
                metadata: { iteration: iterationNum },
              },
            },
          );

          iterations++;
        }

        const last = working[working.length - 1];
        if (last?.role === "assistant" && last.content) {
          const content =
            typeof last.content === "string"
              ? last.content
              : last.content.map((p) => ("text" in p ? p.text : "")).join("");
          span.log({
            output: content,
            metrics: { total_iterations: iterations },
          });
          const scores = computeAutomatedRunScores(
            working,
            iterations,
            this.maxIterations,
          );
          span.logFeedback({
            scores,
            comment:
              "Automated rules-based scores for class demo (see README: Evaluation foundation).",
          });
          return content;
        }

        const fallback =
          "The agent stopped without a final text reply (iteration or model limit).";
        span.log({
          output: fallback,
          metrics: { total_iterations: iterations, max_iterations_reached: 1 },
        });
        const scores = computeAutomatedRunScores(
          working,
          iterations,
          this.maxIterations,
        );
        span.logFeedback({
          scores,
          comment:
            "Automated rules-based scores for class demo (see README: Evaluation foundation).",
        });
        return fallback;
      },
      { name: "paralegal_agent_run", type: "task" },
    );
  }
}
