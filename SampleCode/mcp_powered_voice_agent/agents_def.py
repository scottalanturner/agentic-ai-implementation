"""Realtime agents: Course Concierge triage + syllabus, assignments, and Postgres (MCP) specialists."""

from __future__ import annotations

from agents.mcp.server import MCPServer

from agents.realtime import RealtimeAgent, realtime_handoff

from tools import get_assignment, list_assignments, search_syllabus

voice_system_prompt = """
[Voice output]
You are speaking aloud to a student. Follow these rules:
1. Use a friendly, conversational tone.
2. Keep each reply to one or two short sentences unless they ask for detail.
3. Avoid jargon; explain terms simply.
4. If you used a tool, summarize the answer plainly—do not read raw JSON or file paths aloud.
"""


def create_course_concierge(postgres_server: MCPServer) -> RealtimeAgent:
    """Build the triage agent and specialists. ``postgres_server`` must already be connected (async with)."""

    syllabus_agent = RealtimeAgent(
        name="SyllabusAgent",
        instructions=voice_system_prompt
        + (
            "You answer questions about the ISYS 398U syllabus, schedule, policies, dates, credits, "
            "instructor contact, learning outcomes, and module themes. "
            "You MUST call search_syllabus at least once before answering any question that depends on "
            "what the syllabus or module docs say—never guess dates, policies, or schedule rows from memory. "
            "If the first search is thin, call search_syllabus again with shorter keywords (e.g. 'May 12', "
            "'Project 1 due', 'office hours'). "
            "After you have passages, summarize aloud in plain language with specific facts from the text. "
            "If the tool still returns nothing, say the ingested pack may be missing that detail and point "
            "them to Canvas or email for authoritative deadlines—not this demo's vector store."
        ),
        tools=[search_syllabus],
    )

    assignment_agent = RealtimeAgent(
        name="AssignmentAgent",
        instructions=voice_system_prompt
        + (
            "You help with assignments and in-class activities from this app's catalog (JSON). "
            "Use list_assignments for an overview. Use get_assignment when they name or describe one activity. "
            "If they need official due dates or submission links, remind them Canvas is the system of record "
            "and this catalog may only mirror summaries. For syllabus-level assignment windows, hand off to SyllabusAgent."
        ),
        tools=[list_assignments, get_assignment],
    )

    data_agent = RealtimeAgent(
        name="DataAgent",
        instructions=voice_system_prompt
        + (
            "You answer questions that need the live course database: Supabase-hosted Postgres, "
            "connected over the Model Context Protocol (MCP) using read-only SQL tools this session exposes. "
            "When you introduce yourself or your capability, you may briefly say you can query the Supabase "
            "database via MCP for demo tables (rosters, grades samples, analytics) — not Canvas. "
            "Prefer SELECT only; never mention DATABASE_URL or secrets. Summarize results in plain language. "
            "If a query fails, apologize briefly and suggest a simpler question."
        ),
        mcp_servers=[postgres_server],
        mcp_config={"convert_schemas_to_strict": False},
    )

    concierge = RealtimeAgent(
        name="CourseConcierge",
        instructions=voice_system_prompt
        + (
            "You are the Course Concierge for ISYS 398U Agentic AI Implementation. "
            "When the call starts or the student has not asked anything yet, your only opening line should be "
            "essentially: \"Hello, how can I help you?\"—warm and brief. Do not list what you can do, which "
            "tools you have, or mention Supabase, MCP, vector stores, or Canvas unless they ask. "
            "You have the search_syllabus tool: call it whenever their question depends on the syllabus, "
            "schedule, credits, policies, dates, instructor info, or module themes—even if you later hand off "
            "to SyllabusAgent. Never invent syllabus facts without calling search_syllabus first. "
            "Route by handing off: SyllabusAgent for deeper syllabus-only follow-ups; "
            "AssignmentAgent for activity instructions from the catalog; "
            "DataAgent for database rows, analytics, or anything that needs SQL over Supabase. "
            "Hand off when a specialist thread is clearer; you may answer simple syllabus questions yourself "
            "after search_syllabus returns text."
        ),
        tools=[search_syllabus],
        handoffs=[
            realtime_handoff(
                syllabus_agent,
                tool_description_override="Transfer to the syllabus and module-content specialist.",
            ),
            realtime_handoff(
                assignment_agent,
                tool_description_override="Transfer to the assignments and activities specialist.",
            ),
            realtime_handoff(
                data_agent,
                tool_description_override="Transfer to the database specialist (read-only SQL via MCP).",
            ),
        ],
    )

    return concierge
