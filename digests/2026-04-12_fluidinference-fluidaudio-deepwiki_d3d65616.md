---
url: https://deepwiki.com/FluidInference/FluidAudio
title: FluidInference/FluidAudio | DeepWiki
scraped_at: '2026-04-12T10:42:44Z'
word_count: 805
raw_file: raw/2026-04-12_fluidinference-fluidaudio-deepwiki_d3d65616.txt
tldr: FluidAudio is a Swift 6 SDK for fully local, low-latency audio AI on Apple platforms, covering ASR, diarization, VAD, and TTS with CoreML/ANE optimization and a model-registry download-on-first-use workflow.
key_quote: “FluidAudio is a Swift SDK that enables fully local audio AI processing on macOS and iOS devices.”
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- CoreML
- HuggingFace
- Silero VAD
- Vocos
- Mimi
- Pyannote
- WeSpeaker
- VBx
- Sortformer
libraries: []
companies:
- FluidInference
- FluidAudio
tags:
- audio-ai
- swift
- apple-platforms
- speech-processing
- on-device-inference
---

### TL;DR
FluidAudio is a Swift 6 SDK for fully local, low-latency audio AI on Apple platforms, covering ASR, diarization, VAD, and TTS with CoreML/ANE optimization and a model-registry download-on-first-use workflow.

### Key Quote
“FluidAudio is a Swift SDK that enables fully local audio AI processing on macOS and iOS devices.”

### Summary
- **What it is**
  - A Swift SDK for **on-device audio AI** on **macOS 14+** and **iOS 17+**, targeting **Apple Silicon / arm64**.
  - Emphasizes **privacy**, **low latency**, and **no network dependency after initial model download**.

- **Core capabilities**
  - **ASR (Automatic Speech Recognition)**:
    - Uses **Parakeet TDT**, **Qwen3**, and **Nemotron** model families.
    - Supports **30+ languages** overall; specific examples include:
      - **Parakeet tdt-0.6b-v3 / eou-120m**: Token Duration Transducer, **25 European languages**
      - **Qwen3-ASR-0.6B**: encoder-decoder transformer, **30+ languages**
      - **Nemotron-Streaming-0.6B**: FastConformer RNNT, **English**
    - Modes include:
      - **Batch** transcription via `AsrManager`
      - **Streaming** transcription via `StreamingAsrManager`, `SlidingWindowAsrManager`, or `Qwen3StreamingManager`
      - **Post-processing** with `TextNormalizer` for inverse text normalization (ITN)
      - **Custom vocabulary / keyword boosting** via `CtcTokenizer` and `BpeTokenizer`
  - **Speaker diarization**:
    - Identifies **“who spoke when”**
    - Built from modular components like **Pyannote segmentation**, **WeSpeaker embeddings**, **VBx clustering**, and **end-to-end Sortformer**
  - **VAD (Voice Activity Detection)**:
    - Uses **Silero VAD**
    - Supports:
      - **Batch mode**: whole-file speech timestamp extraction
      - **Streaming mode**: real-time detection with **128 ms chunks** and **hysteresis**
  - **TTS (Text-to-Speech)**:
    - Two engines:
      - **KokoroTtsManager**: parallel synthesis, **Vocos** vocoder, full-generation latency, supports **SSML**, **custom lexicon**, and **IPA**, across **9 languages** (EN, ES, FR, HI, IT, JA, PT, ZH)
      - **PocketTtsManager**: autoregressive streaming, **Mimi** vocoder, about **80 ms to first audio**, supports **voice cloning** from **1–30 seconds**, English only

- **Architecture and design philosophy**
  - The SDK is organized as **modular Swift targets**, with `FluidAudio` as the main library product.
  - It uses a **registry-based model lifecycle**, downloading models from **HuggingFace on first use**.
  - It is designed for **entirely local inference after download**.
  - Heavy inference is optimized for **Apple Neural Engine (ANE)** via **CoreML**, explicitly avoiding **GPU/MPS**.
  - Notes a **FLOAT16 conversion** for newer TTS models like **Kokoro**, moving transformer and convolution layers to ANE and claiming a **1.67x speedup** for Kokoro.

- **Concurrency and safety**
  - The project follows **Swift 6 concurrency rules strictly**.
  - It avoids `@unchecked Sendable`.
  - Core managers are **actor-based** to prevent data races.
  - Utility types like `CtcTokenizer` and `BpeTokenizer` are marked **Sendable**.

- **Docs and layout**
  - The wiki points to major sections:
    - Getting Started
    - Core Library
    - Performance and Benchmarks
    - ASR custom pronunciation
    - CLI
    - TTS docs for Kokoro and SSML
  - The scraped content includes references to several source files and docs, but this page is still mostly an **overview/wiki index**, not a deep implementation guide.

### Assessment
This is a **mixed reference/overview** page with high utility for orientation but limited depth compared with the linked docs. Its **durability is medium to high**: the broad design patterns (local-first audio AI, ANE optimization, actor-based concurrency) are fairly stable, but model names, version requirements, and performance claims are tied to a specific project state. The content is **dense** and **fact-heavy**, but it is also clearly a **synthesis** assembled from README, CLAUDE.md, podspec, Package.swift, and other docs rather than a primary technical narrative. It is best used as a **refer-back** reference to confirm what FluidAudio includes, what platforms it supports, and which subdocs to read next. **Scrape quality is partial/good**: the overview and many specifics are captured, but the page shows “Loading...” artifacts and some sections look summarized rather than fully rendered, so code blocks, diagrams, or deeper section content may be missing.
