#!/usr/bin/env python3
"""Open the Course Concierge in your browser (FastAPI + Realtime Agents SDK, no Tkinter)."""

from __future__ import annotations

import threading
import time
import webbrowser

import uvicorn

from web_server import app as fastapi_app

HOST = "127.0.0.1"
PORT = 8765


def main() -> None:
    def serve() -> None:
        uvicorn.run(
            fastapi_app,
            host=HOST,
            port=PORT,
            ws_max_size=16 * 1024 * 1024,
            log_level="info",
        )

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    time.sleep(0.45)
    url = f"http://{HOST}:{PORT}/"
    print(f"Course Concierge — opening {url}")
    webbrowser.open(url)
    try:
        thread.join()
    except KeyboardInterrupt:
        print("Shutting down.")


if __name__ == "__main__":
    main()
