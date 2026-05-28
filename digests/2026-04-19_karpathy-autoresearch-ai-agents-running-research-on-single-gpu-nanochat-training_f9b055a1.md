---
url: https://github.com/karpathy/autoresearch
title: 'karpathy/autoresearch: AI agents running research on single-GPU nanochat training automatically'
scraped_at: '2026-04-19T07:29:03Z'
word_count: 1223
raw_file: raw/2026-04-19_karpathy-autoresearch-ai-agents-running-research-on-single-gpu-nanochat-training_f9b055a1.txt
tldr: autoresearch is a Karpathy repo for running a single-GPU, 5-minute autonomous LLM-training experiment loop where an AI agent edits train.py, measures val_bpb, and iterates overnight toward better nanochat results.
key_quote: “give an AI agent a small but real LLM training setup and let it experiment autonomously overnight.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- karpathy
tools:
- uv
- Claude
- Codex
libraries:
- PyTorch
companies:
- GitHub
- NVIDIA
tags:
- autonomous-agents
- llm-training
- research-automation
- gpu-computing
- machine-learning-workflow
---

### TL;DR
`autoresearch` is a Karpathy repo for running a single-GPU, 5-minute autonomous LLM-training experiment loop where an AI agent edits `train.py`, measures `val_bpb`, and iterates overnight toward better nanochat results.

### Key Quote
“give an AI agent a small but real LLM training setup and let it experiment autonomously overnight.”

### Summary
- **What this repo is**
  - A minimal “autonomous research” setup built around a simplified single-GPU version of [nanochat](https://github.com/karpathy/nanochat).
  - The user’s role is less “edit Python as a researcher” and more “write `program.md` instructions for the AI agent.”
  - The repo is framed as a story about the beginning of fully autonomous AI research, with a tongue-in-cheek forward-looking introduction dated **March 2026**.

- **Core workflow**
  - An AI agent:
    - reads `program.md`
    - edits `train.py`
    - runs a training experiment for **exactly 5 minutes**
    - checks whether the result improved
    - keeps or discards changes
    - repeats
  - The goal is to wake up to a log of experiments and, ideally, a better model.
  - The evaluation metric is **`val_bpb`** (validation bits per byte), where **lower is better** and the metric is **vocab-size-independent**.

- **Main files**
  - **`prepare.py`**
    - fixed constants
    - one-time data prep
    - downloads training data
    - trains a BPE tokenizer
    - runtime utilities like dataloader and evaluation
    - explicitly **not modified**
  - **`train.py`**
    - the only file the agent edits
    - contains the GPT model, optimizer (**Muon + AdamW**), and training loop
    - all model/hyperparameter choices are fair game
  - **`program.md`**
    - baseline instructions for the agent
    - edited by the human to improve the “research org code”

- **Quick start**
  - Requires:
    - a **single NVIDIA GPU** (tested on **H100**)
    - **Python 3.10+**
    - **uv**
  - Setup commands:
    - `curl -LsSf https://astral.sh/uv/install.sh | sh`
    - `uv sync`
    - `uv run prepare.py`
    - `uv run train.py`
  - If that works, the setup is ready for autonomous research mode.

- **How to use an agent**
  - Run Claude/Codex/etc. in the repo with permissions disabled.
  - Prompt it to inspect `program.md` and start a new experiment.
  - The repo describes `program.md` as a lightweight “skill.”

- **Design choices**
  - **Single file to modify**
    - keeps scope manageable
    - makes diffs easier to review
  - **Fixed time budget**
    - every run is 5 minutes regardless of platform
    - author claims this enables about **12 experiments/hour** and **~100 while you sleep**
    - advantage: experiments are directly comparable on the same platform
    - downside: results are not comparable across different compute platforms
  - **Self-contained**
    - no distributed training
    - no complex configs
    - only PyTorch plus a few small packages

- **Platform support and smaller-compute advice**
  - Current repo requires a **single NVIDIA GPU**
  - The author says CPU/MPS/etc. support is possible but would bloat the code
  - For smaller machines (e.g. MacBooks), the README suggests using forks or adapting parameters:
    - use **TinyStories**
    - reduce `vocab_size` (e.g. 8192 → 4096/2048/1024/256)
    - reduce `MAX_SEQ_LEN` in `prepare.py`
    - possibly increase `DEVICE_BATCH_SIZE`
    - reduce `EVAL_TOKENS`
    - lower `DEPTH` in `train.py` (default **8**)
    - use `WINDOW_PATTERN = "L"` instead of `"SSSL"`
    - reduce `TOTAL_BATCH_SIZE` substantially, keeping it a power of 2

- **Notable forks**
  - `miolini/autoresearch-macos` — MacOS
  - `trevin-creator/autoresearch-mlx` — MacOS
  - `jsegov/autoresearch-win-rtx` — Windows
  - `andyluo7/autoresearch` — AMD

- **License**
  - **MIT**

### Assessment
This is a **mixed** repo README/announcement with tutorial and reference elements. Durability is **medium**: the conceptual framing of autonomous experiment loops is durable, but the concrete setup is tied to current repo structure, GPU assumptions, and likely evolving agent tooling. Density is **medium-high** because it packs a lot of implementation and operational detail into a short README, especially around file roles, metrics, and platform tuning. Originality is mostly **primary source** since it describes Karpathy’s own repo and design intent, though it also references external tweets and forks. It’s best used as a **refer-back** reference for setup, workflow, and repo structure, not deep-study. Scrape quality looks **good**: the main sections, commands, file roles, platform notes, and fork links are present, with no obvious missing code blocks or major omitted sections.
