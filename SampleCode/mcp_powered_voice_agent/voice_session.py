"""Realtime WebSocket session: mic capture, speaker playback, MCP Postgres, UI event queue."""

from __future__ import annotations

import asyncio
import os
import queue
import threading
from typing import Any

import numpy as np
import sounddevice as sd
from dotenv import load_dotenv

from agents.mcp import MCPServerStdio
from agents.realtime import (
    RealtimeAgent,
    RealtimePlaybackTracker,
    RealtimeRunner,
    RealtimeSession,
    RealtimeSessionEvent,
)
from agents.realtime.items import (
    AssistantMessageItem,
    RealtimeToolCallItem,
    UserMessageItem,
)
from agents.realtime.model import RealtimeModelConfig

from agents_def import create_course_concierge

load_dotenv()

CHUNK_LENGTH_S = 0.04
SAMPLE_RATE = 24000
FORMAT = np.int16
CHANNELS = 1
ENERGY_THRESHOLD = 0.015
PREBUFFER_CHUNKS = 3
FADE_OUT_MS = 12
PLAYBACK_ECHO_MARGIN = 0.002


def _truncate_str(s: str, max_length: int) -> str:
    if len(s) > max_length:
        return s[:max_length] + "..."
    return s


def format_history_item(item: Any) -> str | None:
    """Turn a history item into a single human-readable line for the transcript pane."""
    if isinstance(item, UserMessageItem):
        parts: list[str] = []
        for block in item.content:
            t = getattr(block, "text", None)
            if t:
                parts.append(t)
        if parts:
            return "You: " + " ".join(parts)
        return None
    if isinstance(item, AssistantMessageItem):
        parts = []
        for block in item.content:
            if getattr(block, "type", None) == "text":
                tx = getattr(block, "text", None)
                if tx:
                    parts.append(tx)
        if parts:
            return "Assistant: " + " ".join(parts)
        return None
    if isinstance(item, RealtimeToolCallItem):
        out = item.output if item.output is not None else "(pending)"
        return f"Tool {item.name}: {_truncate_str(str(out), 500)}"
    return None


class _AudioIO:
    """Callback-based playback with barge-in, adapted from openai-agents-python/examples/realtime/cli/demo.py."""

    def __init__(self, playback_tracker: RealtimePlaybackTracker) -> None:
        self.playback_tracker = playback_tracker
        self.output_queue: queue.Queue[Any] = queue.Queue(maxsize=0)
        self.interrupt_event = threading.Event()
        self.current_audio_chunk: tuple[np.ndarray[Any, Any], str, int] | None = None
        self.chunk_position = 0
        self.prebuffering = True
        self.prebuffer_target_chunks = PREBUFFER_CHUNKS
        self.fading = False
        self.fade_total_samples = 0
        self.fade_done_samples = 0
        self.fade_samples = int(SAMPLE_RATE * (FADE_OUT_MS / 1000.0))
        self.playback_rms = 0.0
        self.audio_player: sd.OutputStream | None = None

    def _update_playback_rms(self, samples: np.ndarray[Any, Any]) -> None:
        sample_rms = self._compute_rms(samples)
        self.playback_rms = 0.9 * self.playback_rms + 0.1 * sample_rms

    @staticmethod
    def _compute_rms(samples: np.ndarray[Any, Any]) -> float:
        if samples.size == 0:
            return 0.0
        x = samples.astype(np.float32) / 32768.0
        return float(np.sqrt(np.mean(x * x)))

    def _output_callback(self, outdata, frames: int, time, status) -> None:
        if status:
            print(f"Output callback status: {status}")

        if self.interrupt_event.is_set():
            outdata.fill(0)
            if self.current_audio_chunk is None:
                while not self.output_queue.empty():
                    try:
                        self.output_queue.get_nowait()
                    except queue.Empty:
                        break
                self.prebuffering = True
                self.interrupt_event.clear()
                return

            if not self.fading:
                self.fading = True
                self.fade_done_samples = 0
                remaining_in_chunk = len(self.current_audio_chunk[0]) - self.chunk_position
                self.fade_total_samples = min(self.fade_samples, max(0, remaining_in_chunk))

            samples, item_id, content_index = self.current_audio_chunk
            samples_filled = 0
            while (
                samples_filled < len(outdata) and self.fade_done_samples < self.fade_total_samples
            ):
                remaining_output = len(outdata) - samples_filled
                remaining_fade = self.fade_total_samples - self.fade_done_samples
                n = min(remaining_output, remaining_fade)

                src = samples[self.chunk_position : self.chunk_position + n].astype(np.float32)
                idx = np.arange(
                    self.fade_done_samples, self.fade_done_samples + n, dtype=np.float32
                )
                gain = 1.0 - (idx / float(self.fade_total_samples))
                ramped = np.clip(src * gain, -32768.0, 32767.0).astype(np.int16)
                outdata[samples_filled : samples_filled + n, 0] = ramped
                self._update_playback_rms(ramped)
                try:
                    self.playback_tracker.on_play_bytes(
                        item_id=item_id, item_content_index=content_index, bytes=ramped.tobytes()
                    )
                except Exception:
                    pass

                samples_filled += n
                self.chunk_position += n
                self.fade_done_samples += n

            if self.fade_done_samples >= self.fade_total_samples:
                self.current_audio_chunk = None
                self.chunk_position = 0
                while not self.output_queue.empty():
                    try:
                        self.output_queue.get_nowait()
                    except queue.Empty:
                        break
                self.fading = False
                self.prebuffering = True
                self.interrupt_event.clear()
            return

        outdata.fill(0)
        samples_filled = 0

        while samples_filled < len(outdata):
            if self.current_audio_chunk is None:
                try:
                    if (
                        self.prebuffering
                        and self.output_queue.qsize() < self.prebuffer_target_chunks
                    ):
                        break
                    self.prebuffering = False
                    self.current_audio_chunk = self.output_queue.get_nowait()
                    self.chunk_position = 0
                except queue.Empty:
                    break

            remaining_output = len(outdata) - samples_filled
            samples, item_id, content_index = self.current_audio_chunk
            remaining_chunk = len(samples) - self.chunk_position
            samples_to_copy = min(remaining_output, remaining_chunk)

            if samples_to_copy > 0:
                chunk_data = samples[self.chunk_position : self.chunk_position + samples_to_copy]
                outdata[samples_filled : samples_filled + samples_to_copy, 0] = chunk_data
                self._update_playback_rms(chunk_data)
                samples_filled += samples_to_copy
                self.chunk_position += samples_to_copy
                try:
                    self.playback_tracker.on_play_bytes(
                        item_id=item_id,
                        item_content_index=content_index,
                        bytes=chunk_data.tobytes(),
                    )
                except Exception:
                    pass

            if self.chunk_position >= len(samples):
                self.current_audio_chunk = None
                self.chunk_position = 0

    def start_player(self) -> None:
        chunk_size = int(SAMPLE_RATE * CHUNK_LENGTH_S)
        self.audio_player = sd.OutputStream(
            channels=CHANNELS,
            samplerate=SAMPLE_RATE,
            dtype=FORMAT,
            callback=self._output_callback,
            blocksize=chunk_size,
        )
        self.audio_player.start()

    def stop_player(self) -> None:
        if self.audio_player and self.audio_player.active:
            self.audio_player.stop()
        if self.audio_player:
            self.audio_player.close()
            self.audio_player = None


def _emit(
    ui_queue: queue.Queue[dict[str, Any]] | None, payload: dict[str, Any]
) -> None:
    if ui_queue is not None:
        try:
            ui_queue.put_nowait(payload)
        except Exception:
            pass


async def _forward_event(
    event: RealtimeSessionEvent,
    audio_io: _AudioIO,
    ui_queue: queue.Queue[dict[str, Any]] | None,
) -> None:
    try:
        if event.type == "agent_start":
            ag: RealtimeAgent = event.agent
            _emit(ui_queue, {"type": "agent", "name": ag.name})
            _emit(ui_queue, {"type": "status", "text": f"Agent: {ag.name}"})
        elif event.type == "handoff":
            _emit(
                ui_queue,
                {
                    "type": "status",
                    "text": f"Handoff: {event.from_agent.name} -> {event.to_agent.name}",
                },
            )
            _emit(ui_queue, {"type": "agent", "name": event.to_agent.name})
        elif event.type == "tool_start":
            _emit(
                ui_queue,
                {"type": "status", "text": f"Tool: {event.tool.name}"},
            )
        elif event.type == "tool_end":
            _emit(
                ui_queue,
                {"type": "status", "text": f"Tool done: {event.tool.name}"},
            )
        elif event.type == "audio":
            _emit(ui_queue, {"type": "speaking", "value": True})
            np_audio = np.frombuffer(event.audio.data, dtype=np.int16)
            audio_io.output_queue.put_nowait((np_audio, event.item_id, event.content_index))
        elif event.type == "audio_end":
            _emit(ui_queue, {"type": "speaking", "value": False})
        elif event.type == "audio_interrupted":
            _emit(ui_queue, {"type": "speaking", "value": False})
            audio_io.prebuffering = True
            audio_io.interrupt_event.set()
        elif event.type == "history_added":
            line = format_history_item(event.item)
            if line:
                _emit(ui_queue, {"type": "transcript", "line": line})
        elif event.type == "error":
            _emit(ui_queue, {"type": "error", "message": str(event.error)})
    except Exception as e:
        _emit(ui_queue, {"type": "error", "message": str(e)})


async def run_voice_session(
    stop_event: threading.Event,
    ui_queue: queue.Queue[dict[str, Any]] | None = None,
) -> None:
    """Run one realtime call until ``stop_event`` is set (End in the UI)."""
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        _emit(ui_queue, {"type": "error", "message": "OPENAI_API_KEY is not set."})
        return
    if not os.environ.get("SYLLABUS_VECTOR_STORE_ID"):
        _emit(
            ui_queue,
            {
                "type": "error",
                "message": "SYLLABUS_VECTOR_STORE_ID is not set. Run python ingest.py and update .env.",
            },
        )
        return
    db_url = os.environ.get("DATABASE_URL", "").strip()
    if not db_url:
        _emit(
            ui_queue,
            {"type": "error", "message": "DATABASE_URL is not set (local Postgres / Supabase)."},
        )
        return

    _emit(ui_queue, {"type": "status", "text": "Connecting..."})

    playback_tracker = RealtimePlaybackTracker()
    audio_io = _AudioIO(playback_tracker)

    postgres = MCPServerStdio(
        name="course_postgres",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-postgres", db_url],
        },
        cache_tools_list=True,
    )

    try:
        audio_io.start_player()
        async with postgres:
            starting_agent = create_course_concierge(postgres)
            runner = RealtimeRunner(starting_agent)

            # Input transcription is off (null): native realtime audio, no separate STT model.
            model_config: RealtimeModelConfig = {
                "playback_tracker": playback_tracker,
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

            session = await runner.run(model_config=model_config)
            async with session:
                _emit(ui_queue, {"type": "status", "text": "Listening — speak naturally."})

                read_size = int(SAMPLE_RATE * CHUNK_LENGTH_S)
                mic_stream = sd.InputStream(
                    channels=CHANNELS,
                    samplerate=SAMPLE_RATE,
                    dtype=FORMAT,
                )
                mic_stream.start()
                recording = True

                async def capture_audio() -> None:
                    nonlocal recording
                    try:
                        while recording and not stop_event.is_set():
                            if mic_stream.read_available < read_size:
                                await asyncio.sleep(0.01)
                                continue
                            data, _ = mic_stream.read(read_size)
                            audio_bytes = data.tobytes()

                            assistant_playing = (
                                audio_io.current_audio_chunk is not None
                                or not audio_io.output_queue.empty()
                            )
                            if assistant_playing:
                                samples = data.reshape(-1)
                                mic_rms = audio_io._compute_rms(samples)
                                playback_gate = max(
                                    ENERGY_THRESHOLD,
                                    audio_io.playback_rms * 0.6 + PLAYBACK_ECHO_MARGIN,
                                )
                                if mic_rms >= playback_gate:
                                    audio_io.interrupt_event.set()
                                    await session.send_audio(audio_bytes)
                                else:
                                    await session.send_audio(audio_bytes)
                            else:
                                await session.send_audio(audio_bytes)
                            await asyncio.sleep(0)
                    finally:
                        recording = False
                        if mic_stream.active:
                            mic_stream.stop()
                        mic_stream.close()
                        await session.close()

                cap_task = asyncio.create_task(capture_audio())

                try:
                    async for event in session:
                        if stop_event.is_set():
                            break
                        await _forward_event(event, audio_io, ui_queue)
                finally:
                    recording = False
                    cap_task.cancel()
                    try:
                        await cap_task
                    except asyncio.CancelledError:
                        pass
    finally:
        audio_io.stop_player()
        _emit(ui_queue, {"type": "speaking", "value": False})
        _emit(ui_queue, {"type": "status", "text": "Idle"})
        _emit(ui_queue, {"type": "call_ended"})


def run_voice_session_thread(
    stop_event: threading.Event,
    ui_queue: queue.Queue[dict[str, Any]] | None = None,
) -> None:
    """Entry point for a background thread: runs ``asyncio.run(run_voice_session(...))``."""

    asyncio.run(run_voice_session(stop_event, ui_queue=ui_queue))
