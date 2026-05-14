import { z } from "zod";
import {
  conflictCheck,
  getEfilingStatus,
  getMatterById,
  listEfilingsForMatter,
  searchMatters,
} from "./mock-store.js";

export interface Tool {
  name: string;
  description: string;
  parameters: z.ZodSchema;
  execute: (args: unknown) => Promise<string>;
}

const SearchMattersSchema = z.object({
  query: z
    .string()
    .describe(
      "Client name fragment, matter id (e.g. M-24087), or words from the case caption.",
    ),
});

const GetMatterCalendarSchema = z.object({
  matterId: z.string().describe("Matter id such as M-24087"),
});

const CheckEfilingSchema = z.object({
  submissionId: z
    .string()
    .optional()
    .describe("E-filing submission id, e.g. EF-88402"),
  matterId: z
    .string()
    .optional()
    .describe("If submissionId omitted, list recent filings for this matter."),
});

const ConflictCheckSchema = z.object({
  contactName: z.string().describe("Individual name to check"),
  organization: z
    .string()
    .optional()
    .describe("Company or firm name, if known"),
});

export const searchMattersTool: Tool = {
  name: "search_matters",
  description:
    "Search the firm's mock matter list by client, matter id, caption, or opposing counsel.",
  parameters: SearchMattersSchema,
  execute: async (raw) => {
    const { query } = SearchMattersSchema.parse(raw);
    const rows = searchMatters(query);
    if (rows.length === 0) {
      return `No matters matched "${query}". Try a shorter fragment or a matter id like M-24087.`;
    }
    return rows
      .map(
        (m) =>
          `${m.matterId} — ${m.caption}\n  Client: ${m.client}\n  Status: ${m.status}\n  Next: ${m.nextEvents.map((e) => `${e.date}: ${e.label}`).join("; ") || "none listed"}`,
      )
      .join("\n\n");
  },
};

export const getMatterCalendarTool: Tool = {
  name: "get_matter_calendar",
  description:
    "Return upcoming hearings/events and open deadlines for one matter from the mock docket system.",
  parameters: GetMatterCalendarSchema,
  execute: async (raw) => {
    const { matterId } = GetMatterCalendarSchema.parse(raw);
    const m = getMatterById(matterId);
    if (!m) {
      return `Unknown matter id "${matterId}". Use search_matters first.`;
    }
    const events = m.nextEvents
      .map((e) => `- ${e.date}: ${e.label}${e.location ? ` (${e.location})` : ""}`)
      .join("\n");
    const dlines = m.openDeadlines
      .map((d) => `- ${d.date}: ${d.description} — responsible: ${d.owner}`)
      .join("\n");
    return `Matter ${m.matterId} (${m.venue})\n\nUpcoming:\n${events || "(none)"}\n\nOpen deadlines:\n${dlines || "(none)"}`;
  },
};

export const checkEfilingTool: Tool = {
  name: "check_efiling_status",
  description:
    "Look up a mock CM/ECF-style submission status, or list filings for a matter.",
  parameters: CheckEfilingSchema,
  execute: async (raw) => {
    const { submissionId, matterId } = CheckEfilingSchema.parse(raw);
    if (submissionId) {
      const e = getEfilingStatus(submissionId);
      if (!e) {
        return `No submission "${submissionId}". Try EF-88321, EF-88402, or EF-88455 in the demo.`;
      }
      return `Submission ${e.submissionId} (${e.documentTitle})\nMatter: ${e.matterId}\nStatus: ${e.status}\nLast update: ${e.lastUpdate}${e.clerkNote ? `\nClerk note: ${e.clerkNote}` : ""}`;
    }
    if (matterId) {
      const list = listEfilingsForMatter(matterId);
      if (list.length === 0) {
        return `No e-filings on file for ${matterId} in the mock portal.`;
      }
      return list
        .map((e) => `${e.submissionId}: ${e.documentTitle} — ${e.status}`)
        .join("\n");
    }
    return "Provide either submissionId or matterId.";
  },
};

export const conflictCheckTool: Tool = {
  name: "conflict_check_contact",
  description:
    "Run a mock new-contact screen against an internal conflict index (not real clearance).",
  parameters: ConflictCheckSchema,
  execute: async (raw) => {
    const { contactName, organization } = ConflictCheckSchema.parse(raw);
    return conflictCheck(contactName, organization);
  },
};

export function getAllTools(): Tool[] {
  return [
    searchMattersTool,
    getMatterCalendarTool,
    checkEfilingTool,
    conflictCheckTool,
  ];
}
