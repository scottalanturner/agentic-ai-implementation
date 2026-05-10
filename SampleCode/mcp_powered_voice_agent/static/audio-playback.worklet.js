class PCMPlaybackProcessor extends AudioWorkletProcessor {
  constructor(options) {
    super(options);
    this._queue = [];
    this._current = null;
    this._offset = 0;
    this.port.onmessage = (e) => {
      const m = e.data;
      if (!m || typeof m !== 'object') return;
      if (m.type === 'chunk' && m.payload) {
        this._queue.push(new Int16Array(m.payload));
      } else if (m.type === 'stop') {
        this._queue = [];
        this._current = null;
        this._offset = 0;
      } else if (m.type === 'config') {
        this._fadeSamples = m.fadeSamples | 0;
      }
    };
    this._fadeSamples = 0;
  }

  process(inputs, outputs) {
    const out = outputs[0][0];
    let w = 0;
    while (w < out.length) {
      if (!this._current || this._offset >= this._current.length) {
        if (this._queue.length === 0) {
          out.fill(0, w);
          if (w === 0 && !this._current) {
            this.port.postMessage({ type: 'drained' });
          }
          break;
        }
        this._current = this._queue.shift();
        this._offset = 0;
      }
      const n = Math.min(out.length - w, this._current.length - this._offset);
      for (let i = 0; i < n; i++) {
        out[w + i] = this._current[this._offset + i] / 32768;
      }
      this._offset += n;
      w += n;
    }
    return true;
  }
}

registerProcessor('pcm-playback', PCMPlaybackProcessor);
