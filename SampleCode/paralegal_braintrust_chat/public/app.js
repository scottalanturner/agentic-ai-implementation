const logEl = document.getElementById("log");
const inputEl = document.getElementById("input");
const sendBtn = document.getElementById("send");
const errEl = document.getElementById("err");

let sessionId = "";

function append(role, text) {
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  const label = role === "user" ? "You" : "Assistant";
  div.innerHTML = `<strong>${label}</strong><br>${escapeHtml(text)}`;
  logEl.appendChild(div);
  logEl.scrollTop = logEl.scrollHeight;
}

function appendNote(text, variant = "ok") {
  const div = document.createElement("div");
  div.className = variant === "warn" ? "msg note warn" : "msg note";
  div.innerHTML = `<strong>Braintrust</strong><br>${escapeHtml(text)}`;
  logEl.appendChild(div);
  logEl.scrollTop = logEl.scrollHeight;
}

function escapeHtml(s) {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

async function send() {
  const message = inputEl.value.trim();
  if (!message) return;

  const wantedCapture = /^\/capture\b/i.test(message);

  errEl.textContent = "";
  append("user", message);
  inputEl.value = "";
  sendBtn.disabled = true;

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, sessionId: sessionId || undefined }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      throw new Error(data.error || res.statusText);
    }
    sessionId = data.sessionId || sessionId;
    append("bot", data.reply ?? "(no reply)");
    if (wantedCapture && data.captured && data.captureRecordId) {
      appendNote(
        `Saved this turn to dataset “${data.captureDataset}”. Record id: ${data.captureRecordId}. In Braintrust: open your project → Datasets → “${data.captureDataset}”.`,
      );
    } else if (wantedCapture && data.captureError) {
      appendNote(data.captureError, "warn");
    }
  } catch (e) {
    errEl.textContent = e instanceof Error ? e.message : String(e);
  } finally {
    sendBtn.disabled = false;
    inputEl.focus();
  }
}

sendBtn.addEventListener("click", send);
inputEl.addEventListener("keydown", (ev) => {
  if (ev.key === "Enter" && !ev.shiftKey) {
    ev.preventDefault();
    send();
  }
});
