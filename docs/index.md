---
layout: default
---

# Noam Shabtai — Signal & Data Processing

Python frameworks for real-time signal and data processing.

---

## About

I am Noam Shabtai, with a PhD from Ben-Gurion University (Prof. Boaz Rafaely) and postdoctoral research at RWTH Aachen University (Prof. Michael Vorlaender), specializing in array signal processing, real-time systems, and spectral analysis.

This page presents independent engineering projects built the way I work: **test-driven development** and **Clean Code** first. Tests are written before the code; modules stay small, single-responsibility, and dependency-injected; names read as intent. Architecture and real-time processing follow from that discipline, not the other way around.

---

## Project: Real-Time Signal Processing Framework

A modular Python framework for signal processing, with spatial audio as an example application.

### Architecture
- **Input Buffer**: accumulates step-size chunks until a full window is ready
- **Modules**: independent signal processors (frequency or time domain), e.g. STFT Analysis, Spatial Audio, STFT Synthesis
- **System**: runs each module's `execute()`, chaining one module's output into the next
- **Activator**: drives the system — *offline* (file-to-file WAV/BIN batch, one `.bin` + plot per tracked module) or *demo* (looping WAV input → real-time PyAudio output)
- **Analysis**: runs an offline Activator once per case from a multi-case YAML, collecting per-case outputs

### Example Application: Spatial Audio
- HRTF-based binaural rendering with quaternion head-orientation tracking
- Tkinter GUI with live azimuth/elevation and per-channel gain

**Try it** (Python 3.12+, [uv](https://github.com/astral-sh/uv), headphones):
```bash
git clone https://github.com/noamshabtai/signal-processing.git
./signal-processing/spatial-audio-demo/run_demo.sh
```

### Test-Driven Development & Clean Code
- **TDD**: 100+ pytest tests with YAML parametrization, written test-first to drive the design
- **Clean Code**: small single-responsibility modules, dependency injection, intention-revealing names, full type hints
- GitHub Actions CI/CD with branch protection — the suite gates every merge
- Pre-commit hooks, uv, monorepo structure

**Source:** [github.com/noamshabtai/signal-processing](https://github.com/noamshabtai/signal-processing)

---

## Contact

- **Email:** [shabtai.noam@gmail.com](mailto:shabtai.noam@gmail.com)
- **LinkedIn:** [linkedin.com/in/noam-shabtai-80836717](https://www.linkedin.com/in/noam-shabtai-80836717/)
- **GitHub:** [github.com/noamshabtai](https://github.com/noamshabtai)

---

© 2025 Noam Shabtai
