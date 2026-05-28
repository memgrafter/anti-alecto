---
url: https://github.com/arman-bd/guppylm
title: https://github.com/arman-bd/guppylm
scraped_at: '2026-04-19T20:06:28Z'
word_count: 1045
raw_file: raw/2026-04-19_https-github-com-arman-bd-guppylm_19d1df82.txt
tldr: GuppyLM is a tiny 8.7M-parameter transformer trained from scratch on 60K synthetic conversations to act like a lowercase, fish-like chatbot, with Colab notebooks, a Hugging Face model/dataset, and a browser demo.
key_quote: This project exists to show that training your own language model is not magic.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Colab
- Hugging Face
- WebAssembly
- ONNX
libraries:
- torch
- tokenizers
- datasets
companies: []
tags:
- large-language-models
- synthetic-data
- transformer-models
- model-training
- machine-learning-demos
---

### TL;DR
GuppyLM is a tiny 8.7M-parameter transformer trained from scratch on 60K synthetic conversations to act like a lowercase, fish-like chatbot, with Colab notebooks, a Hugging Face model/dataset, and a browser demo.

### Key Quote
> “This project exists to show that training your own language model is not magic.”

### Summary
- **What it is**
  - An intentionally small language model called **GuppyLM** that “talks like a small fish.”
  - Built to demonstrate that making a working LLM can be done with modest resources: **one Colab notebook, a T4 GPU, and about 5 minutes**.
  - The model is not meant to be broadly capable; it is designed around a narrow character/personality.

- **Behavior/personality**
  - Speaks in **short, lowercase sentences**.
  - Talks about **water, food, light, bubbles, tank life, temperature, and fish-like feelings**.
  - Does **not** handle human abstractions well; the README explicitly says it is **not trying** to understand money, phones, politics, etc.
  - Example outputs show a friendly, simple, somewhat silly tone.

- **Model details**
  - **8.7M parameters**
  - **6 layers**
  - **Hidden size: 384**
  - **6 attention heads**
  - **FFN size: 768 (ReLU)**
  - **Vocabulary: 4,096 BPE tokens**
  - **Max sequence length: 128 tokens**
  - **LayerNorm**, **learned positional embeddings**
  - **Weight-tied LM head**
  - Described as a **vanilla transformer** with no GQA, RoPE, SwiGLU, or early exit.

- **Training/data**
  - Trained from scratch on **60,000 synthetic conversations**.
  - Dataset split: **57K train / 3K test**.
  - **60 categories/topics** including greetings, feelings, food, weather, sleep, cats, jokes, love, memory, time, and more.
  - Data generation uses **template composition** with randomized components; the README claims this yields about **16K unique outputs from ~60 templates**.

- **How to use it**
  - **Browser demo**: runs locally in the browser using **WebAssembly** and a **quantized ONNX model (~10 MB)**.
  - **Colab chat notebook**: downloads the pre-trained model from Hugging Face and lets you chat.
  - **Colab training notebook**: set runtime to **T4 GPU**, run all cells to download data, train tokenizer, train model, and test it.
  - **Local chat**:
    - `pip install torch tokenizers`
    - `python -m guppylm chat`
    - Single prompt mode is also supported:
      - `python -m guppylm chat --prompt "tell me a joke"`

- **Repository structure**
  - Core code lives in:
    - `config.py` — hyperparameters
    - `model.py` — transformer model
    - `dataset.py` — loading/batching
    - `train.py` — training loop with cosine LR and AMP
    - `generate_data.py` — synthetic conversation generation
    - `prepare_data.py` — data prep and tokenizer training
    - `inference.py` — chat interface
  - Tools include ONNX export, dataset publishing, and Colab notebook generation.
  - `docs/` contains the browser demo assets and downloadable model/tokenizer files.

- **Design rationale**
  - **No system prompt**: the same instruction was used during training, so the persona is “baked into the weights,” and omitting it at inference saves ~60 tokens.
  - **Single-turn only**: multi-turn chats degrade after turn 3–4 because of the **128-token context window**.
  - **Why a simple transformer**: the author argues advanced architecture tricks aren’t worth the added complexity at this tiny scale.
  - **Why synthetic data**: consistency of personality is easier to enforce with templated synthetic conversations than with messy real-world data.

- **Access/licensing**
  - Links to:
    - **Hugging Face dataset**: `arman-bd/guppylm-60k-generic`
    - **Hugging Face model**: `arman-bd/guppylm-9M`
    - **Colab notebooks**
    - **Browser demo**
  - Licensed under **MIT**.

### Assessment
This is a **mixed** content type: part project announcement, part technical reference, and part tutorial/README. Durability is **medium** because the conceptual ideas about tiny LLMs and synthetic data are fairly durable, but the specific model, dataset, notebook links, and performance claims are version- and project-specific. Density is **high**: the README packs architecture specs, dataset structure, usage instructions, and design rationale into a compact page. Originality is mostly **primary source**, since it documents the author’s own model, training setup, and demos. It’s best treated as **refer-back** material if you want to recall the architecture, commands, or project structure. Scrape quality appears **good**: the main README sections, commands, example outputs, and repository layout are present, with no obvious missing code blocks or major sections.
