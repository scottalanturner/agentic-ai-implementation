/** In-memory mock data for a small litigation practice (demo only). */

export type MatterStatus = "active" | "on_hold" | "closed";

export interface Matter {
  matterId: string;
  caption: string;
  client: string;
  venue: string;
  judge: string;
  opposingCounsel: string;
  status: MatterStatus;
  nextEvents: { date: string; label: string; location?: string }[];
  openDeadlines: { date: string; description: string; owner: string }[];
}

export interface EfilingSubmission {
  submissionId: string;
  matterId: string;
  documentTitle: string;
  status: "queued" | "submitted" | "accepted" | "rejected_needs_correction";
  lastUpdate: string;
  clerkNote?: string;
}

const MATTERS: Matter[] = [
  {
    matterId: "M-24087",
    caption: "Harbor Freight Logistics LLC v. Apex Container Corp.",
    client: "Harbor Freight Logistics LLC",
    venue: "U.S.D.C., N.D. Cal.",
    judge: "Hon. M. Patel",
    opposingCounsel: "Briggs & Vale LLP (R. Vale)",
    status: "active",
    nextEvents: [
      {
        date: "2026-05-28",
        label: "Case management conference",
        location: "Courtroom 4, Oakland",
      },
      { date: "2026-06-12", label: "Expert discovery cutoff" },
    ],
    openDeadlines: [
      {
        date: "2026-05-20",
        description: "Responses to RFP Set Two",
        owner: "Assoc. Chen",
      },
      {
        date: "2026-05-22",
        description: "Privilege log v2 to opposing counsel",
        owner: "Paralegal (you)",
      },
    ],
  },
  {
    matterId: "M-24102",
    caption: "In re: Sunset Retail Group — Subpoena compliance",
    client: "Sunset Retail Group",
    venue: "Cal. Super. Ct., L.A. County",
    judge: "Hon. L. Okonkwo",
    opposingCounsel: "In-house (General Counsel)",
    status: "active",
    nextEvents: [
      { date: "2026-05-18", label: "Deposition of D. Morales (10:00 a.m.)" },
    ],
    openDeadlines: [
      {
        date: "2026-05-16",
        description: "Third-party document production to subpoena issuer",
        owner: "Paralegal (you)",
      },
    ],
  },
];

const EFILINGS: EfilingSubmission[] = [
  {
    submissionId: "EF-88321",
    matterId: "M-24087",
    documentTitle: "Notice of appearance — local counsel",
    status: "accepted",
    lastUpdate: "2026-05-10T14:22:00Z",
  },
  {
    submissionId: "EF-88402",
    matterId: "M-24087",
    documentTitle: "Motion to compel — proposed order",
    status: "rejected_needs_correction",
    lastUpdate: "2026-05-12T09:05:00Z",
    clerkNote:
      "Certificate of service must list all parties including proposed intervenor.",
  },
  {
    submissionId: "EF-88455",
    matterId: "M-24102",
    documentTitle: "Notice of deposition (Morales)",
    status: "submitted",
    lastUpdate: "2026-05-13T16:40:00Z",
  },
];

const CONFLICT_INDEX: { name: string; org: string; linkedMatterId: string }[] =
  [
    {
      name: "Riley Vale",
      org: "Briggs & Vale LLP",
      linkedMatterId: "M-24087",
    },
    {
      name: "Dana Morales",
      org: "Sunset Retail Group",
      linkedMatterId: "M-24102",
    },
  ];

export function searchMatters(query: string): Matter[] {
  const q = query.trim().toLowerCase();
  if (!q) return MATTERS;
  return MATTERS.filter(
    (m) =>
      m.matterId.toLowerCase().includes(q) ||
      m.client.toLowerCase().includes(q) ||
      m.caption.toLowerCase().includes(q) ||
      m.opposingCounsel.toLowerCase().includes(q),
  );
}

export function getMatterById(matterId: string): Matter | undefined {
  return MATTERS.find((m) => m.matterId === matterId);
}

export function getEfilingStatus(submissionId: string): EfilingSubmission | undefined {
  return EFILINGS.find((e) => e.submissionId === submissionId);
}

export function listEfilingsForMatter(matterId: string): EfilingSubmission[] {
  return EFILINGS.filter((e) => e.matterId === matterId);
}

export function conflictCheck(contactName: string, organization?: string): string {
  const n = contactName.trim().toLowerCase();
  const o = (organization ?? "").trim().toLowerCase();
  const hits = CONFLICT_INDEX.filter((row) => {
    const nameHit = row.name.toLowerCase().includes(n) || n.includes(row.name.toLowerCase());
    const orgHit =
      !o ||
      row.org.toLowerCase().includes(o) ||
      o.includes(row.org.toLowerCase());
    return nameHit && orgHit;
  });
  if (hits.length === 0) {
    return `No conflict hits for "${contactName}"${organization ? ` / ${organization}` : ""} in the mock wall. (Demo data only — not real clearance.)`;
  }
  return hits
    .map(
      (h) =>
        `Potential relationship: ${h.name} (${h.org}) ↔ active matter ${h.linkedMatterId}. Flag for attorney review before engagement.`,
    )
    .join("\n");
}
