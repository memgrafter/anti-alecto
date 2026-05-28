---
url: https://github.com/kyutai-labs/pocket-tts
title: 'kyutai-labs/pocket-tts: A TTS that fits in your CPU (and pocket)'
scraped_at: '2026-04-19T08:14:39Z'
word_count: 1499
raw_file: raw/2026-04-19_kyutai-labs-pocket-tts-a-tts-that-fits-in-your-cpu-and-pocket_7bf176cb.txt
tldr: Pocket TTS is a lightweight, CPU-friendly text-to-speech system from Kyutai that supports streaming, voice cloning, multilingual speech, and both CLI/Python use with ~100M parameters and low latency.
key_quote: “Generating audio is just a pip install and a function call away.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Manu Orsini
- Simon Rouard
- Gabriel De Marmiesse
- Václav Volhejn
- Neil Zeghidour
- Alexandre Défossez
tools:
- uvx
- pocket-tts
- PyTorch
libraries:
- torch
- scipy
companies:
- Kyutai
tags:
- text-to-speech
- voice-cloning
- cpu-inference
- speech-synthesis
- streaming-audio
---

### TL;DR
Pocket TTS is a lightweight, CPU-friendly text-to-speech system from Kyutai that supports streaming, voice cloning, multilingual speech, and both CLI/Python use with ~100M parameters and low latency.

### Key Quote
“Generating audio is just a pip install and a function call away.”

### Summary
- **What it is**
  - A text-to-speech application designed to run efficiently on CPUs, avoiding the need for GPUs or web APIs.
  - Promoted as small enough to fit “in your CPU (and pocket).”
  - Model size: **100M parameters**.

- **Core capabilities**
  - Runs on **CPU only**; does **not** require GPU PyTorch.
  - Supports **audio streaming** with about **200ms** latency to first audio chunk.
  - Claims performance of about **6x real-time** on a **MacBook Air M4 CPU**, using **2 CPU cores**.
  - Supports **voice cloning** from a voice sample or a saved voice embedding.
  - Multilingual support: **English, French, German, Portuguese, Italian, Spanish**.
  - Can handle **infinitely long text inputs**.
  - Can run **client-side in the browser** via community implementations.

- **Compatibility / requirements**
  - Supports **Python 3.10, 3.11, 3.12, 3.13, 3.14**.
  - Requires **PyTorch 2.5+**.
  - Works without the GPU build of PyTorch.

- **Ways to try it**
  - **Web demo** at Kyutai’s site, no install needed.
  - **CLI**:
    - `uvx pocket-tts generate`
    - or `pocket-tts generate` after manual install
    - Outputs a WAV file `./tts_output.wav`
    - Supports `--voice`, `--text`, `--language`, and `--config`
  - **Local server**:
    - `uvx pocket-tts serve`
    - or `pocket-tts serve`
    - Serves a local web UI at `http://localhost:8000`
    - Keeps the model in memory between requests for faster repeated use
  - **Voice export**:
    - `export-voice` converts an audio sample into a fast-loading **safetensors** voice embedding

- **Python library usage**
  - Install with:
    - `pip install pocket-tts`
    - or `uv add pocket-tts`
  - Typical workflow:
    - `TTSModel.load_model()`
    - `get_state_for_audio_prompt(...)` to create voice state
    - `generate_audio(...)` to synthesize speech
  - Audio output is a **1D torch tensor containing PCM data**
  - `export_model_state(...)` can save voice state to `.safetensors` for faster reuse later

- **Pre-made voices / cloning notes**
  - Provides a catalog of named sample voices such as `alba`, `anna`, `azelma`, `bill_boerst`, `charles`, `jean`, `marius`, `vera`, etc.
  - Voice input can be:
    - a built-in voice name
    - a local `.wav` file
    - a Hugging Face voice file path
  - Recommends cleaning sample audio before cloning because the sample quality is reproduced in the generated voice.

- **Limitations / unsupported features**
  - No support yet for:
    - inserting silence directly in text for pauses
    - **int8 quantization**
  - Notes that GPU did not provide a speedup in their tests, likely due to batch size 1 and the model being very small.

- **Development / ecosystem**
  - Contributions are welcome; development instructions are in `CONTRIBUTING.md`.
  - Lists several **community browser or runtime ports**, including:
    - `wasm-pocket-tts`
    - `pocket-tts-onnx-export`
    - `pocket-tts-candle`
    - `jax-js`
  - Lists other alternative implementations such as:
    - `pocket-tts-mlx`
    - `pocket-tts-xn`
    - `PocketTTS.cpp`
    - `sherpa-onnx`
    - `pocket-tts-csharp`

- **Projects using Pocket TTS**
  - Examples include browser screen readers, Home Assistant/voice integrations, Unity integration, Discord bots, desktop apps, and OpenAI-compatible servers.

- **Policy / safety**
  - Explicitly prohibits harmful or deceptive use, especially:
    - voice impersonation without consent
    - misinformation/disinformation
    - fraudulent or privacy-invasive generated content

- **Authors**
  - Manu Orsini*, Simon Rouard*, Gabriel De Marmiesse*, Václav Volhejn, Neil Zeghidour, Alexandre Défossez
  - `*` indicates equal contribution

### Assessment
This is a **mixed** reference/announcement/documentation page with strong practical tutorial content. Durability is **medium**: the general concepts around CPU-based streaming TTS and voice cloning are durable, but compatibility claims, performance numbers, supported Python versions, and the listed voices/links may age quickly. Density is **high**, since it packs install commands, API examples, supported features, limitations, and ecosystem links into a compact README. Originality is **primary source**, as it is the project’s own documentation and product description. Reference style is **refer-back** for installation and API usage, and **skim-once** for the marketing-style overview. Scrape quality is **good**: the main README content, examples, feature lists, and link lists are present; however, external docs, images, and linked pages are not included in full here.
