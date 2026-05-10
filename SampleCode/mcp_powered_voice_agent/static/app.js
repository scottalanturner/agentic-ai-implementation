(() => {
  const callBtn = document.getElementById('callBtn');
  const muteBtn = document.getElementById('muteBtn');
  const statusEl = document.getElementById('status');
  const agentEl = document.getElementById('agent');
  const logEl = document.getElementById('log');
  const callCanvas = document.getElementById('callCanvas');

  let ws = null;
  let connected = false;
  let muted = false;
  let capturing = false;
  let sessionId = 's_' + Math.random().toString(36).slice(2, 11);

  let audioContext = null;
  let captureSource = null;
  let captureNode = null;
  let mediaStream = null;

  let playbackAudioContext = null;
  let playbackNode = null;
  let playbackInitPromise = null;
  const pendingPlayback = [];

  let pulsePhase = 0;
  let assistantSpeaking = false;
  let speakClearTimer = null;
  let rafId = 0;

  const CSS_W = 280;
  const CSS_H = 200;

  function log(line) {
    const t = new Date().toLocaleTimeString();
    logEl.textContent += `[${t}] ${line}\n`;
    logEl.scrollTop = logEl.scrollHeight;
  }

  function setStatus(s) {
    statusEl.textContent = s;
  }

  function setAgent(name) {
    agentEl.textContent = name || '—';
  }

  function wsUrl() {
    const proto = location.protocol === 'https:' ? 'wss:' : 'ws:';
    return `${proto}//${location.host}/ws/${sessionId}`;
  }

  /** Hi-DPI canvas so the “phone” draws crisply on Retina displays. */
  function resizeCanvas() {
    if (!callCanvas) return;
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    callCanvas.style.width = `${CSS_W}px`;
    callCanvas.style.height = `${CSS_H}px`;
    callCanvas.width = Math.round(CSS_W * dpr);
    callCanvas.height = Math.round(CSS_H * dpr);
    const ctx = callCanvas.getContext('2d');
    if (ctx) ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    paintPhone();
  }

  function paintPhone() {
    if (!callCanvas) return;
    const ctx = callCanvas.getContext('2d');
    if (!ctx) return;
    const w = CSS_W;
    const h = CSS_H;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, callCanvas.width, callCanvas.height);
    const dpr = callCanvas.width / w;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    ctx.fillStyle = '#eceff1';
    ctx.fillRect(0, 0, w, h);

    const cx = w / 2;
    const cy = h / 2 - 6;
    const r = 58;

    if (connected) {
      const pulse = 0.12 + 0.08 * Math.sin(pulsePhase);
      ctx.beginPath();
      ctx.arc(cx, cy, r + 14 + pulse * 10, 0, Math.PI * 2);
      ctx.strokeStyle = `rgba(198, 40, 40, ${0.25 + pulse})`;
      ctx.lineWidth = 3;
      ctx.stroke();
    }

    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 2);
    ctx.fillStyle = connected ? '#c62828' : '#2e7d32';
    ctx.strokeStyle = connected ? '#8e0000' : '#1b5e20';
    ctx.lineWidth = 3;
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#eceff1';
    ctx.strokeStyle = '#37474f';
    ctx.lineWidth = 2;
    const hx = cx - 20;
    const hy = cy - 28;
    ctx.fillRect(hx, hy, 40, 64);
    ctx.strokeRect(hx, hy, 40, 64);

    ctx.beginPath();
    ctx.arc(cx, hy + 6, 16, Math.PI, 0);
    ctx.fillStyle = '#eceff1';
    ctx.strokeStyle = '#37474f';
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#fff';
    ctx.font = '600 14px system-ui, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(connected ? 'On call' : 'Ready', cx, cy + 52);

    if (assistantSpeaking && connected) {
      ctx.fillStyle = 'rgba(255, 193, 7, 0.9)';
      ctx.beginPath();
      ctx.arc(cx + r - 8, cy - r + 12, 6, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function loopPaint() {
    pulsePhase += 0.08;
    paintPhone();
    if (connected) {
      rafId = requestAnimationFrame(loopPaint);
    }
  }

  function startPulseLoop() {
    cancelAnimationFrame(rafId);
    rafId = requestAnimationFrame(loopPaint);
  }

  function stopPulseLoop() {
    cancelAnimationFrame(rafId);
    rafId = 0;
    pulsePhase = 0;
    paintPhone();
  }

  function setSpeaking(on) {
    assistantSpeaking = on;
    if (speakClearTimer) clearTimeout(speakClearTimer);
    if (on) {
      speakClearTimer = setTimeout(() => {
        assistantSpeaking = false;
        paintPhone();
      }, 400);
    }
    paintPhone();
  }

  async function startCapture() {
    if (capturing) return;
    mediaStream = await navigator.mediaDevices.getUserMedia({
      audio: {
        sampleRate: 24000,
        channelCount: 1,
        echoCancellation: true,
        noiseSuppression: true,
      },
    });
    audioContext = new AudioContext({ sampleRate: 24000, latencyHint: 'interactive' });
    if (audioContext.state === 'suspended') {
      try {
        await audioContext.resume();
      } catch (_) {}
    }
    await audioContext.audioWorklet.addModule('/static/audio-recorder.worklet.js');
    captureSource = audioContext.createMediaStreamSource(mediaStream);
    captureNode = new AudioWorkletNode(audioContext, 'pcm-recorder');
    captureNode.port.onmessage = (ev) => {
      if (muted || !ws || ws.readyState !== WebSocket.OPEN) return;
      const buf = ev.data;
      if (!buf) return;
      const chunk = new Int16Array(buf);
      if (chunk.length === 0) return;
      ws.send(JSON.stringify({ type: 'audio', data: Array.from(chunk) }));
    };
    captureSource.connect(captureNode);
    captureNode.connect(audioContext.destination);
    capturing = true;
    updateMuteLabel();
  }

  function stopCapture() {
    capturing = false;
    if (captureSource) {
      try {
        captureSource.disconnect();
      } catch (_) {}
      captureSource = null;
    }
    if (captureNode) {
      captureNode.port.onmessage = null;
      try {
        captureNode.disconnect();
      } catch (_) {}
      captureNode = null;
    }
    if (audioContext) {
      audioContext.close();
      audioContext = null;
    }
    if (mediaStream) {
      mediaStream.getTracks().forEach((t) => t.stop());
      mediaStream = null;
    }
    updateMuteLabel();
  }

  async function ensurePlayback() {
    if (playbackNode) return;
    if (!playbackInitPromise) {
      playbackInitPromise = (async () => {
        playbackAudioContext = new AudioContext({
          sampleRate: 24000,
          latencyHint: 'interactive',
        });
        if (playbackAudioContext.state === 'suspended') {
          try {
            await playbackAudioContext.resume();
          } catch (_) {}
        }
        await playbackAudioContext.audioWorklet.addModule('/static/audio-playback.worklet.js');
        playbackNode = new AudioWorkletNode(playbackAudioContext, 'pcm-playback', {
          outputChannelCount: [1],
        });
        const fade = Math.floor(playbackAudioContext.sampleRate * 0.02);
        playbackNode.port.postMessage({ type: 'config', fadeSamples: fade });
        playbackNode.connect(playbackAudioContext.destination);
      })().catch((e) => {
        playbackInitPromise = null;
        throw e;
      });
    }
    await playbackInitPromise;
  }

  function flushPlayback() {
    if (!playbackNode) return;
    while (pendingPlayback.length) {
      const chunk = pendingPlayback.shift();
      if (!chunk || !chunk.length) continue;
      try {
        playbackNode.port.postMessage({ type: 'chunk', payload: chunk.buffer }, [chunk.buffer]);
      } catch (e) {
        console.error(e);
      }
    }
  }

  async function playAudio(b64) {
    if (!b64) return;
    setSpeaking(true);
    const bin = atob(b64);
    const bytes = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    const int16 = new Int16Array(bytes.buffer);
    if (!int16.length) return;
    pendingPlayback.push(int16);
    await ensurePlayback();
    flushPlayback();
  }

  function stopPlayback() {
    pendingPlayback.length = 0;
    if (playbackNode) {
      try {
        playbackNode.port.postMessage({ type: 'stop' });
      } catch (_) {}
    }
    setSpeaking(false);
  }

  function updateMuteLabel() {
    muteBtn.disabled = !connected;
    muteBtn.textContent = muted ? 'Muted (tap to unmute)' : 'Mute mic';
  }

  function updateCallButton() {
    if (connected) {
      callBtn.textContent = 'Hang up';
      callBtn.className = 'call out';
    } else {
      callBtn.textContent = 'Call in';
      callBtn.className = 'call in';
    }
    paintPhone();
  }

  async function connect() {
    callBtn.disabled = true;
    setStatus('Connecting…');
    sessionId = 's_' + Math.random().toString(36).slice(2, 11);
    ws = new WebSocket(wsUrl());
    ws.onopen = async () => {
      connected = true;
      updateCallButton();
      startPulseLoop();
      setStatus('Live — speak naturally');
      muteBtn.disabled = false;
      try {
        await startCapture();
      } catch (e) {
        log('Mic error: ' + e);
        setStatus('Microphone blocked or unavailable');
        disconnect();
      }
      callBtn.disabled = false;
    };
    ws.onmessage = (ev) => {
      let data;
      try {
        data = JSON.parse(ev.data);
      } catch {
        return;
      }
      handleEvent(data);
    };
    ws.onclose = () => {
      connected = false;
      stopPulseLoop();
      stopCapture();
      stopPlayback();
      updateCallButton();
      updateMuteLabel();
      setStatus('Idle');
      setAgent('—');
      callBtn.disabled = false;
    };
    ws.onerror = () => {
      log('WebSocket error');
    };
  }

  function disconnect() {
    if (ws) {
      ws.close();
      ws = null;
    }
    stopCapture();
    stopPlayback();
    connected = false;
    stopPulseLoop();
    updateCallButton();
  }

  function handleEvent(ev) {
    switch (ev.type) {
      case 'audio':
        playAudio(ev.audio);
        break;
      case 'audio_interrupted':
        stopPlayback();
        break;
      case 'audio_end':
        setSpeaking(false);
        break;
      case 'agent_start':
        setAgent(ev.agent);
        log(`Agent: ${ev.agent}`);
        break;
      case 'handoff':
        setAgent(ev.to);
        log(`Handoff ${ev.from} → ${ev.to}`);
        break;
      case 'tool_start':
        log(`Tool ▶ ${ev.tool}`);
        break;
      case 'tool_end':
        log(`Tool ✓ ${ev.tool}`);
        break;
      case 'tool_approval_required': {
        const preview = (ev.arguments || '').slice(0, 200);
        const ok = window.confirm(`Allow tool "${ev.tool}"?\n${preview}`);
        if (ws && ws.readyState === WebSocket.OPEN) {
          ws.send(
            JSON.stringify({
              type: 'tool_approval_decision',
              call_id: ev.call_id,
              approve: ok,
            })
          );
        }
        break;
      }
      case 'input_audio_timeout_triggered':
        if (ws && ws.readyState === WebSocket.OPEN) {
          ws.send(JSON.stringify({ type: 'commit_audio' }));
        }
        break;
      case 'error':
        log('Error: ' + (ev.error || JSON.stringify(ev)));
        setStatus('Error (see log)');
        break;
      default:
        break;
    }
  }

  function toggleCall() {
    if (connected) {
      disconnect();
    } else {
      connect();
    }
  }

  callBtn.addEventListener('click', toggleCall);

  if (callCanvas) {
    callCanvas.addEventListener('click', () => {
      toggleCall();
    });
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
  }

  muteBtn.addEventListener('click', () => {
    if (!connected) return;
    muted = !muted;
    updateMuteLabel();
  });

  updateCallButton();
  updateMuteLabel();
  setStatus('Idle — press Call in or tap the phone');
})();
