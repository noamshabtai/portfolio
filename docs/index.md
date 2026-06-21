---
layout: default
---

# Noam Shabtai — Signal & Data Processing

Python frameworks for real-time signal and data processing.

---

## About

I am Noam Shabtai, with a PhD from Ben-Gurion University (Prof. Boaz Rafaely) and postdoctoral research at RWTH Aachen University (Prof. Michael Vorlaender), specializing in array signal processing, real-time systems, and spectral analysis.

This page presents independent engineering projects in Python architecture, test-driven development, and real-time processing.

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

### Quality
- 100+ pytest tests with YAML parametrization
- GitHub Actions CI/CD, branch protection
- Pre-commit hooks, type hints, uv, monorepo structure

**Source:** [github.com/noamshabtai/signal-processing](https://github.com/noamshabtai/signal-processing)

---

## Project: Data Processing Framework

Reuses the same patterns for data pipelines — a finance demo built on the activator pattern.

- **Data Fetcher**: stock data via yfinance
- **Feature Extraction**: trend extraction and FFT-based analysis on time series
- **Model**: PyTorch LSTM for sequence prediction
- **Reuse**: finance demo inherits from signal-processing's base_demo

**Source:** [github.com/noamshabtai/data-processing](https://github.com/noamshabtai/data-processing)

---

## Contact

- **Email:** [shabtai.noam@gmail.com](mailto:shabtai.noam@gmail.com)
- **LinkedIn:** [linkedin.com/in/noam-shabtai-80836717](https://www.linkedin.com/in/noam-shabtai-80836717/)
- **GitHub:** [github.com/noamshabtai](https://github.com/noamshabtai)

---

© 2025 Noam Shabtai
