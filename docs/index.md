---
layout: default
---

<section class="card card--intro">
  <span class="eyebrow">About</span>
  <p class="lead">
    I'm <strong>Noam Shabtai</strong> — PhD from Ben-Gurion University (Prof. Boaz Rafaely),
    postdoctoral research at RWTH Aachen (Prof. Michael Vorländer). I specialize in
    <strong>array signal processing</strong>, <strong>real-time systems</strong>, and
    <strong>spectral analysis</strong>.
  </p>
  <p>
    This page presents independent engineering projects built the way I work:
    <strong>test-driven development</strong> and <strong>Clean Code</strong> first.
    Tests are written before the code; modules stay small, single-responsibility, and
    dependency-injected; names read as intent. Architecture and real-time processing
    follow from that discipline — not the other way around.
  </p>
</section>

<section class="card">
  <span class="eyebrow">Featured Project</span>
  <h2 class="card__title">Real-Time Signal Processing Framework</h2>
  <p class="card__subtitle">A modular Python framework for signal processing, with spatial audio as an example application.</p>

  <div class="badges">
    <span class="badge">Python 3.12+</span>
    <span class="badge">NumPy</span>
    <span class="badge">PyAudio</span>
    <span class="badge">HRTF / Binaural</span>
    <span class="badge">pytest</span>
    <span class="badge">GitHub Actions</span>
    <span class="badge">uv</span>
  </div>

  <h3 class="section-label">Architecture</h3>
  <div class="grid">
    <div class="tile"><span class="tile__icon">🧩</span><h4>Input Buffer</h4><p>Accumulates step-size chunks until a full window is ready.</p></div>
    <div class="tile"><span class="tile__icon">🔊</span><h4>Modules</h4><p>Independent processors (frequency or time domain): STFT Analysis, Spatial Audio, STFT Synthesis.</p></div>
    <div class="tile"><span class="tile__icon">⛓️</span><h4>System</h4><p>Runs each module's <code>execute()</code>, chaining one module's output into the next.</p></div>
    <div class="tile"><span class="tile__icon">▶️</span><h4>Activator</h4><p>Drives the system — <em>offline</em> (WAV/BIN batch) or <em>demo</em> (looping WAV → real-time PyAudio out).</p></div>
    <div class="tile"><span class="tile__icon">📊</span><h4>Analysis</h4><p>Runs an offline Activator once per case from a multi-case YAML, collecting per-case outputs.</p></div>
  </div>

  <h3 class="section-label">Example Application — Spatial Audio</h3>
  <ul class="feature-list">
    <li>HRTF-based binaural rendering with quaternion head-orientation tracking</li>
    <li>Tkinter GUI with live azimuth / elevation and per-channel gain</li>
  </ul>

  <h3 class="section-label">Try it <span class="muted">— Ubuntu, <a href="https://github.com/astral-sh/uv">uv</a>, headphones</span></h3>
  <div class="terminal">
    <div class="terminal__bar"><span></span><span></span><span></span></div>
<pre><code>git clone https://github.com/noamshabtai/signal-processing.git
cd signal-processing
./spatial-audio-demo/run_demo.sh</code></pre>
  </div>

  <h3 class="section-label">Test-Driven Development &amp; Clean Code</h3>
  <ul class="feature-list">
    <li><strong>TDD</strong> — behavior-driven pytest suite, parametrized from YAML case files, written test-first to drive the design</li>
    <li><strong>Clean Code</strong> — small single-responsibility modules, dependency injection, intention-revealing names, full type hints</li>
    <li>GitHub Actions CI/CD with branch protection — the suite gates every merge</li>
    <li>Pre-commit hooks, uv, monorepo structure</li>
  </ul>

  <a class="btn" href="https://github.com/noamshabtai/signal-processing">View source on GitHub →</a>
</section>

<section class="card card--contact" id="contact">
  <span class="eyebrow">Contact</span>
  <div class="contact-row">
    <button class="chip" type="button"
            onclick="navigator.clipboard.writeText('shabtai.noam@gmail.com');var l=this.querySelector('.chip__label');var o=l.textContent;l.textContent='Copied!';setTimeout(function(){l.textContent=o;},1200);"
            title="Click to copy">✉️ <span class="chip__label">shabtai.noam@gmail.com</span></button>
    <a class="chip" href="https://www.linkedin.com/in/noam-shabtai-80836717/">in LinkedIn</a>
    <a class="chip" href="https://github.com/noamshabtai">GitHub</a>
  </div>
</section>
