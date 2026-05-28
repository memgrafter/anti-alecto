---
url: https://deepwiki.com/karpathy/nanochat
title: karpathy/nanochat | DeepWiki
scraped_at: '2026-04-19T06:48:23Z'
word_count: 1185
raw_file: raw/2026-04-19_karpathy-nanochat-deepwiki_bdb43264.txt
tldr: nanochat is Karpathy’s minimal, full-stack LLM training system that can train, align, evaluate, and deploy a GPT-2-capability model on a single GPU node using a “single complexity dial” based on transformer depth.
key_quote: the --depth argument (number of transformer layers) automatically determines all other hyperparameters to produce compute-optimal models
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: partial
people:
- Andrej Karpathy
tools:
- scripts/chat_cli.py
- scripts/chat_web.py
- scripts/tok_train.py
- scripts/base_train.py
- scripts/chat_sft.py
- scripts/chat_rl.py
- scripts/base_eval.py
- scripts/chat_eval.py
- runs/speedrun.sh
- torchao
libraries:
- Flash Attention 3
companies:
- NVIDIA
tags:
- large-language-models
- model-training
- scaling-laws
- llm-evaluation
- gpu-training
---

### TL;DR
nanochat is Karpathy’s minimal, full-stack LLM training system that can train, align, evaluate, and deploy a GPT-2-capability model on a single GPU node using a “single complexity dial” based on transformer depth.

### Key Quote
“the --depth argument (number of transformer layers) automatically determines all other hyperparameters to produce compute-optimal models”

### Summary
- **What it is**
  - A minimal experimental harness for training large language models from scratch.
  - Designed to cover the full LLM lifecycle: tokenization, pretraining, supervised fine-tuning (SFT), reinforcement learning (RL), evaluation, and deployment.
  - Intended to be readable, hackable, and small, with no configuration objects or heavy framework abstractions.

- **Main value proposition**
  - Runs on a single GPU node, typically **8xH100 or 8xA100**.
  - Claims low cost for GPT-2-capability training: about **1.65–1.8 hours** and roughly **$40–$50**, compared with **$43,000 in 2019**.
  - Lets you interact with the trained model through:
    - `scripts/chat_cli.py`
    - `scripts/chat_web.py`

- **Pipeline / stages**
  - **Tokenization**: `scripts/tok_train.py` → `tokenizer.model`
    - Trains a BPE tokenizer with **32,768 vocab**.
  - **Base pretraining**: `scripts/base_train.py` → base checkpoint
    - Trains a transformer from scratch using scaling laws.
  - **SFT**: `scripts/chat_sft.py` → chat checkpoint
    - Adapts the base model using **SmolTalk / MMLU / GSM8K**.
  - **RL**: `scripts/chat_rl.py` → aligned checkpoint
    - Optional alignment stage using **GRPO / SimPO**.
  - **Evaluation**: `scripts/base_eval.py`, `scripts/chat_eval.py`
    - Measures **CORE score**, **val_bpb**, and task accuracy.
  - **Inference / deployment**: `scripts/chat_cli.py`, `scripts/chat_web.py`
    - Provides interactive chat with streaming API.

- **Core design philosophy: “single complexity dial”**
  - The user mainly chooses `--depth` (number of transformer layers).
  - That one choice determines other hyperparameters automatically, including:
    - model width (`n_embd`)
    - number of attention heads (`n_head`)
    - learning rates
    - training horizon / total tokens
    - batch size
    - weight decay and Muon momentum schedules
  - Implemented via scaling-law formulas in `scripts/base_train.py`.
  - Goal: produce **compute-optimal models** and avoid tedious hyperparameter tuning.
  - Principle: improvements should work across all depths, not just one favored scale.

- **Depth-to-capability examples**
  - **12 layers** → GPT-1 scale → ~**124M params** → ~**5 min**
  - **16 layers** → intermediate → ~**220M params** → ~**15 min**
  - **20 layers** → approaching GPT-2 → ~**343M params** → ~**45 min**
  - **24–26 layers** → GPT-2 → ~**475M–600M params** → ~**1.65–1.8 hours**

- **Time-to-GPT-2 leaderboard**
  - The main benchmark is wall-clock time to train a model that exceeds GPT-2’s **CORE score of 0.256525** on an **8xH100** node.
  - Metrics tracked:
    - **Time**: wall-clock training time excluding evaluation/logging
    - **val_bpb**: validation bits-per-byte, vocabulary-size invariant
    - **CORE**: centered accuracy across **22 ICL tasks** from the DCLM paper
  - Recent entries listed:
    - **#4**: **2.02 hours**, `val_bpb 0.71854`, `CORE 0.2571`, NVIDIA ClimbMix dataset, **Mar 4 2026**, commit `324e69c`
    - **#5**: **1.80 hours**, `val_bpb 0.71808`, `CORE 0.2690`, Autoresearch round 1, **Mar 9 2026**, commit `6ed7d1d`
    - **#6**: **1.65 hours**, `val_bpb 0.71800`, `CORE 0.2626`, Autoresearch round 2, **Mar 14 2026**, commit `a825e63`
  - To participate, the wiki says to run `runs/speedrun.sh`, verify `core_metric > 0.256525`, and submit a PR with improved `total_training_time`.

- **Architecture / modules**
  - `gpt.py`
    - `GPT`, `GPTConfig`, `CausalSelfAttention`
    - Transformer architecture with Flash Attention 3, sliding windows, rotary embeddings
  - `engine.py`
    - `Engine`, `generate`, `generate_batch`
    - Inference engine with KV cache, sampling, and tool use (calculator)
  - `dataloader.py`
    - `make_dataloader`, `parquets_iter_batched`
    - BOS-aligned BestFit packing and distributed data loading for ClimbMix
  - `dataset.py`
    - `download_file`, `Dataset`
    - Manages parquet files for **ClimbMix-400B**
  - `tokenizer.py`
    - `Tokenizer`, `train_tokenizer`
    - BPE tokenizer wrapper with **32,768 vocab**
  - `optim.py`
    - `MuonAdamW`, `DistMuonAdamW`
    - Hybrid optimizer: Muon for 2D matrices, AdamW for embeddings/scalars
  - `checkpoint_manager.py`
    - `save_checkpoint`, `load_checkpoint`
    - Checkpoint I/O with backward compatibility and rank-aware saving
  - `common.py`
    - `compute_init`, `COMPUTE_DTYPE`
    - DDP setup, device management, explicit precision system

- **Precision / hardware support**
  - nanochat uses an explicit precision system instead of PyTorch autocast.
  - `COMPUTE_DTYPE` is auto-detected:
    - **CUDA SM 80+ (A100, H100)** → `bfloat16`
    - **CUDA SM < 80 (V100, T4)** → `float32` by default; `float16` via `NANOCHAT_DTYPE=float16`
    - **CPU / MPS** → `float32`
  - Optional **FP8** training is available with `--fp8` on Hopper+ GPUs, using `torchao` tensorwise FP8 scaling.

- **Other notable design choices**
  - No autocast; explicit `COMPUTE_DTYPE` and custom `Linear` casting logic.
  - Dataset switched from **FineWeb-EDU** to **NVIDIA ClimbMix 400B**, reportedly reducing GPT-2 speedrun time by **27%** (from **2h46m** to about **2h**).
  - Uses **Flash Attention 3** with fallback to standard SDPA for older hardware or non-FA3 paths.
  - Default **logit softcap = 20**, tuned from d24 scale experiments to improve validation loss.

### Assessment
This is a **reference** page describing a current ML codebase and its design philosophy, with strong practical specificity but also some time-sensitive details like hardware assumptions, benchmark results, commit hashes, and 2026 leaderboard entries. Durability is **medium** because the core ideas—minimal full-stack training, scaling-law-driven hyperparameter selection, and a single depth dial—are relatively durable, but the leaderboard and performance numbers will age quickly. Content type is **mixed**: part overview/reference, part technical documentation, part project status update. Density is **high**, with many concrete scripts, module names, metrics, and architectural choices packed in. Originality is mostly **synthesis** of the repository’s README and dev docs rather than a primary research paper or purely opinionated commentary. This is best used as a **refer-back** resource for deciding whether to dive into the repo and for locating the right scripts or subsystems. Scrape quality is **partial**: the summary captures major text sections, but the page references diagrams and deeper subsections that are not fully visible here, so some visual or section-level details may be missing.
