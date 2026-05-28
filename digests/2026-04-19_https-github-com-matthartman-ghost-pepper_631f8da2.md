---
url: https://github.com/matthartman/ghost-pepper
title: https://github.com/matthartman/ghost-pepper
scraped_at: '2026-04-19T20:07:03Z'
word_count: 812
raw_file: raw/2026-04-19_https-github-com-matthartman-ghost-pepper_631f8da2.txt
tldr: Ghost Pepper is a free, open-source macOS menu bar app that does fully local speech-to-text and meeting transcription on Apple Silicon, with local cleanup/summarization models and a strong privacy-first pitch.
key_quote: “100% private on-device voice models for speech-to-text and meeting transcription on macOS. No cloud APIs, no data leaves your machine.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- WhisperKit
- LLM.swift
- Hugging Face
- Sparkle
- FluidAudio
libraries: []
companies: []
tags:
- macos
- speech-to-text
- meeting-transcription
- privacy
- open-source-tools
---

### TL;DR
Ghost Pepper is a free, open-source macOS menu bar app that does fully local speech-to-text and meeting transcription on Apple Silicon, with local cleanup/summarization models and a strong privacy-first pitch.

### Key Quote
“100% private on-device voice models for speech-to-text and meeting transcription on macOS. No cloud APIs, no data leaves your machine.”

### Summary
- **What it is**
  - A macOS app called **Ghost Pepper** for voice dictation and meeting transcription.
  - Targets **macOS 14.0+** and **Apple Silicon (M1+)**.
  - Positioned as **100% local / private / free and open source**.

- **Core features**
  - **Hold Control to talk**: release the key to transcribe speech and paste text into any field.
  - **Meeting transcription**: records calls, creates notes, transcripts, and **AI-generated summaries** saved as Markdown.
  - Runs as a **menu bar app** with no dock icon and can **launch at login**.
  - Includes **smart cleanup** using a local LLM to remove filler words and handle self-corrections.
  - Lets users **customize the cleanup prompt**, mic selection, and feature toggles.

- **How it works**
  - Uses **open-source models** that are downloaded automatically and cached locally.
  - **Speech models** listed:
    - Whisper tiny.en — ~75 MB, fastest, English only
    - **Whisper small.en** (default) — ~466 MB, best accuracy, English only
    - Whisper small (multilingual) — ~466 MB
    - Parakeet v3 — ~1.4 GB, 25 languages, via **FluidAudio**
    - Qwen3-ASR 0.6B int8 — ~900 MB, 50+ languages, requires **macOS 15+**
  - **Cleanup models** listed:
    - **Qwen 3.5 0.8B** (default) — ~535 MB, very fast (~1–2s)
    - Qwen 3.5 2B — ~1.3 GB, fast (~4–5s)
    - Qwen 3.5 4B — ~2.8 GB, full quality (~5–7s)
  - Speech is powered by **WhisperKit**; cleanup by **LLM.swift**; models are served by **Hugging Face**.

- **Getting started**
  - Download the DMG from the latest GitHub release.
  - Open the DMG, drag Ghost Pepper to Applications.
  - Grant **Microphone** and **Accessibility** permissions.
  - Use **Control + speak** to transcribe.
  - If macOS shows an **“Apple could not verify”** Gatekeeper warning on Sequoia, go to **System Settings > Privacy & Security** and click **Open Anyway** once.
  - Can also be **built from source** by opening `GhostPepper.xcodeproj` in Xcode and building/running.

- **Permissions**
  - **Microphone**: record your voice.
  - **Accessibility**: global hotkey handling and simulated paste keystrokes.

- **Privacy claims / audit**
  - The README presents a privacy audit claiming all core features run locally.
  - It explicitly says there is:
    - no audio sent anywhere for speech-to-text
    - no cloud API for cleanup or summarization
    - local storage for transcripts and recordings
    - no analytics/telemetry SDKs like Firebase, Mixpanel, or Sentry
  - Optional cloud integrations exist but are **disabled by default** and require the user’s own API keys:
    - Zo AI chat
    - Trello integration
    - Granola meeting import

- **Enterprise / managed devices**
  - Notes that Accessibility permission usually requires admin access.
  - For managed devices, IT admins can pre-approve via **MDM/PPPC**.
  - Gives the bundle ID **`com.github.matthartman.ghostpepper`**, team ID **`BBVMGXR9AY`**, and Accessibility permission identifier **`com.apple.security.accessibility`**.

- **Miscellaneous**
  - Built with **WhisperKit**, **LLM.swift**, **Hugging Face**, and **Sparkle**.
  - Licensed under **MIT**.
  - “Ghost Pepper” name explanation: it’s spicy because it offers a free local alternative to apps that have raised major funding.

### Assessment
This is a **mixed** content piece: primarily a **tool/reference** README with some tutorial-style setup instructions and a marketing/privacy pitch. Durability is **medium** because the core concept of local on-device transcription is fairly stable, but the specific model list, macOS version requirements, and performance claims will age as dependencies evolve. Density is **high**: it includes concrete feature descriptions, model sizes, OS requirements, permissions, and enterprise deployment details. Originality is mainly **primary source** since it documents the project itself, though the privacy audit section is partly a curated internal verification claim. Reference style is **refer-back** if you’re considering installing, building, or evaluating its privacy posture. Scrape quality is **good** overall: the main README content appears intact, including tables and setup notes, though any linked files like the full audit document or release binary content are not included here.
