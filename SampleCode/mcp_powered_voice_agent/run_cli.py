#!/usr/bin/env python3
"""Headless entry point when Tkinter is not available (same voice session, logs to terminal)."""

from __future__ import annotations

import asyncio
import signal
import threading

from dotenv import load_dotenv

from voice_session import run_voice_session

load_dotenv()


def main() -> None:
    print("Course Concierge — CLI mode (Ctrl+C to hang up)")
    stop = threading.Event()

    def _sigint(_signum: int, _frame: object | None) -> None:
        print("\nHang-up signal received, closing session…")
        stop.set()

    signal.signal(signal.SIGINT, _sigint)

    asyncio.run(run_voice_session(stop))
    print("Goodbye.")


if __name__ == "__main__":
    main()
