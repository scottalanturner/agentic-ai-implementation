"""FastAPI bridge: browser mic/speaker ↔ OpenAI Realtime Agents SDK (no input STT)."""

from __future__ import annotations

import asyncio
import base64
import json
import logging
import os
import struct
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from agents.mcp import MCPServerStdio
from agents.realtime import RealtimeRunner, RealtimeSession, RealtimeSessionEvent
from agents.realtime.items import RealtimeItem
from agents.realtime.model import RealtimeModelConfig
from agents.realtime.model_inputs import RealtimeModelSendRawMessage

from agents_def import create_course_concierge

load_dotenv()

logger = logging.getLogger(__name__)
STATIC_DIR = Path(__file__).resolve().parent / "static"


def _strip_transcript_fields(obj: Any) -> Any:
    """Remove transcript-bearing fields from payloads sent to the browser (no STT in UI)."""
    if isinstance(obj, dict):
        return {
            k: _strip_transcript_fields(v)
            for k, v in obj.items()
            if k not in ("transcript", "input_audio_transcription")
        }
    if isinstance(obj, list):
        return [_strip_transcript_fields(x) for x in obj]
    return obj


def _realtime_model_config() -> RealtimeModelConfig:
    return {
        "initial_model_settings": {
            "model_name": "gpt-realtime-1.5",
            "modalities": ["audio"],
            "audio": {
                "input": {
                    "format": "pcm16",
                    "transcription": None,
                    "turn_detection": {
                        "type": "semantic_vad",
                        "interrupt_response": True,
                        "create_response": True,
                    },
                },
                "output": {"format": "pcm16", "voice": "ash"},
            },
        },
    }


def _check_env() -> str | None:
    if not os.environ.get("OPENAI_API_KEY"):
        return "OPENAI_API_KEY is not set."
    if not os.environ.get("SYLLABUS_VECTOR_STORE_ID"):
        return "SYLLABUS_VECTOR_STORE_ID is not set. Run python ingest.py and update .env."
    if not os.environ.get("DATABASE_URL", "").strip():
        return "DATABASE_URL is not set."
    return None


def _sanitize_history_item(item: RealtimeItem) -> dict[str, Any]:
    item_dict = item.model_dump()
    content = item_dict.get("content")
    if isinstance(content, list):
        sanitized: list[Any] = []
        for part in content:
            if isinstance(part, dict):
                p = part.copy()
                if p.get("type") in {"audio", "input_audio"}:
                    p.pop("audio", None)
                p.pop("transcript", None)
                sanitized.append(p)
            else:
                sanitized.append(part)
        item_dict["content"] = sanitized
    return _strip_transcript_fields(item_dict)


async def _serialize_event(event: RealtimeSessionEvent) -> dict[str, Any]:
    base: dict[str, Any] = {"type": event.type}

    if event.type == "agent_start":
        base["agent"] = event.agent.name
    elif event.type == "agent_end":
        base["agent"] = event.agent.name
    elif event.type == "handoff":
        base["from"] = event.from_agent.name
        base["to"] = event.to_agent.name
    elif event.type == "tool_start":
        base["tool"] = event.tool.name
    elif event.type == "tool_end":
        base["tool"] = event.tool.name
        base["output"] = str(event.output)
    elif event.type == "tool_approval_required":
        base["tool"] = event.tool.name
        base["call_id"] = event.call_id
        base["arguments"] = event.arguments
        base["agent"] = event.agent.name
    elif event.type == "audio":
        base["audio"] = base64.b64encode(event.audio.data).decode("utf-8")
    elif event.type == "audio_interrupted":
        pass
    elif event.type == "audio_end":
        pass
    elif event.type == "history_updated":
        base["history"] = [_sanitize_history_item(i) for i in event.history]
    elif event.type == "history_added":
        try:
            base["item"] = _sanitize_history_item(event.item)
        except Exception:
            base["item"] = None
    elif event.type == "guardrail_tripped":
        base["guardrail_results"] = [{"name": r.guardrail.name} for r in event.guardrail_results]
    elif event.type == "raw_model_event":
        base["raw_model_event"] = {"type": event.data.type}
    elif event.type == "error":
        base["error"] = str(event.error) if hasattr(event, "error") else "Unknown error"
    elif event.type == "input_audio_timeout_triggered":
        pass
    else:
        base["note"] = "unhandled_event_shape"

    return _strip_transcript_fields(base)


async def _pump_session_to_ws(session: RealtimeSession, websocket: WebSocket) -> None:
    try:
        async for event in session:
            await websocket.send_text(json.dumps(await _serialize_event(event)))
    except Exception as e:
        logger.exception("Event pump failed: %s", e)


app = FastAPI(title="Course Concierge (Realtime)")


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.websocket("/ws/{session_id}")
async def voice_ws(websocket: WebSocket, session_id: str) -> None:
    await websocket.accept()
    err = _check_env()
    if err:
        await websocket.send_text(json.dumps({"type": "error", "error": err}))
        await websocket.close()
        return

    db_url = os.environ["DATABASE_URL"].strip()
    postgres = MCPServerStdio(
        name="course_postgres",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-postgres", db_url],
        },
        cache_tools_list=True,
    )

    try:
        async with postgres:
            starting_agent = create_course_concierge(postgres)
            runner = RealtimeRunner(starting_agent)
            session_context = await runner.run(model_config=_realtime_model_config())
            session = await session_context.__aenter__()
            pump: asyncio.Task[None] | None = None
            try:
                pump = asyncio.create_task(_pump_session_to_ws(session, websocket))
                while True:
                    raw = await websocket.receive_text()
                    msg = json.loads(raw)
                    mtype = msg.get("type")
                    if mtype == "audio":
                        int16_data = msg["data"]
                        audio_bytes = struct.pack(f"{len(int16_data)}h", *int16_data)
                        await session.send_audio(audio_bytes)
                    elif mtype == "commit_audio":
                        await session.model.send_event(
                            RealtimeModelSendRawMessage(message={"type": "input_audio_buffer.commit"})
                        )
                    elif mtype == "interrupt":
                        await session.interrupt()
                    elif mtype == "tool_approval_decision":
                        call_id = msg.get("call_id")
                        if not call_id:
                            continue
                        if msg.get("approve"):
                            await session.approve_tool_call(
                                call_id, always=bool(msg.get("always", False))
                            )
                        else:
                            await session.reject_tool_call(
                                call_id, always=bool(msg.get("always", False))
                            )
            finally:
                if pump:
                    pump.cancel()
                    try:
                        await pump
                    except asyncio.CancelledError:
                        pass
                await session_context.__aexit__(None, None, None)
    except WebSocketDisconnect:
        logger.info("Client disconnected session=%s", session_id)
    except Exception as e:
        logger.exception("Session error: %s", e)
        try:
            await websocket.send_text(json.dumps({"type": "error", "error": str(e)}))
        except Exception:
            pass


def create_app() -> FastAPI:
    return app
