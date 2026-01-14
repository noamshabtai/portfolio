---
layout: default
---

# Signal Processing Development & Testing Services

Building Scalable Python Platforms with TDD Frameworks and Long-Term Support

---

## About

I provide professional Python-based development and testing services for signal processing applications. My expertise lies in building scalable platforms with comprehensive Test-Driven Development (TDD) frameworks and providing long-term support that ensures your systems remain maintainable and reliable.

I help organizations transform their signal processing algorithms into production-ready, scalable platforms with robust testing infrastructure and modern development practices.

---

## Services I Offer

- **Custom Python Infrastructure:** Building scalable platforms tailored for signal processing applications

- **TDD Framework Development:** Establishing comprehensive testing frameworks that ensure code quality and accelerate development cycles

- **Long-Term Platform Support:** Providing ongoing maintenance, updates, and knowledge transfer to your team

- **Real-Time Processing Systems:** Production-ready frameworks with live streaming and data processing capabilities

- **Algorithm Implementation:** Transforming research algorithms into production-ready, tested code

- **Modular Architecture Design:** Scalable systems with clean separation of concerns and reusable components

---

## Portfolio Demonstration

**Example Project:** Real-Time Signal Processing Framework with Spatial Audio Application

To demonstrate the quality and depth of services I provide, I have built a complete, production-ready signal processing infrastructure. This framework provides general-purpose components for any signal processing application, with spatial audio implemented as an example use case showcasing the platform's capabilities.

The infrastructure demonstrates how modular, scalable platforms enable rapid development of signal processing applications while maintaining high code quality and testability.

### Core Infrastructure Components

- **System Architecture**: Base system class providing module connection and execution framework - applicable to any signal processing pipeline

- **Buffer Management**: Sophisticated input/output buffer handling for streaming data in real-time applications

- **Activator Pattern**: Abstract base class with both file-based and real-time callback implementations for flexible deployment across different use cases

- **STFT Processing Module**: Modular Short-Time Fourier Transform with separate Analysis and Synthesis classes, perfect reconstruction, and configurable overlap ratios (2x, 4x, custom)

### Example Application: Spatial Audio

Built on top of the general infrastructure to demonstrate real-world usage:

- **Spatial Audio System**: HRTF-based binaural rendering for immersive 3D audio with quaternion-based head orientation tracking

- **Real-Time GUI Demo**: Tkinter-based interface with live azimuth/elevation control and per-channel gain management

This example shows how the infrastructure enables rapid development of complex signal processing applications while maintaining code quality and testability.

### Development Quality

- **Comprehensive Testing**: 100+ tests across all modules using pytest with YAML-based parametrization

- **CI/CD Integration**: GitHub Actions with automated testing on all pull requests, branch protection requiring passing tests

- **Modern Development Practices**: Pre-commit hooks, type hints throughout, Python 3.12+, uv package management

- **Modular Design**: Clean separation of concerns with multiple interdependent packages in a monorepo structure

- **Production-Ready**: Real-time processing capabilities, perfect reconstruction guarantees, configurable parameters

### Platform Capabilities

**General Infrastructure:**
- Frequency-domain processing with configurable STFT pipeline
- Real-time streaming with callback-based architecture
- File-based processing for offline analysis
- Modular design allowing easy addition of new processing modules

**Example Application (Spatial Audio):**
- Multiple virtual sound sources at configurable 3D positions (azimuth/elevation)
- Input: CH channels (mono sources) → Output: Binauralized stereo
- Real-time streaming with PyAudio integration
- File I/O supporting .wav and .bin formats

**Source Code & Documentation:** [github.com/noamshabtai/portfolio](https://github.com/noamshabtai/portfolio)

The complete framework is open-source, demonstrating transparency and code quality. Technical documentation and architecture notes are included in the repository.

---

## Get in Touch

If you're interested in building scalable signal processing platforms for your organization, I welcome the opportunity to discuss how my services can support your needs.

Whether you need custom infrastructure development, TDD frameworks, or long-term platform support, I can help transform your signal processing requirements into production-ready solutions.

### Contact Information

- **Email:** [shabtai.noam@gmail.com](mailto:shabtai.noam@gmail.com)
- **LinkedIn:** [linkedin.com/in/noam-shabtai-80836717](https://www.linkedin.com/in/noam-shabtai-80836717/)
- **GitHub:** [github.com/noamshabtai](https://github.com/noamshabtai)

---

© 2025 Signal Processing Development & Testing. All Rights Reserved.
