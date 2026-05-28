---
url: https://github.com/karpathy/nanochat/tree/master?tab=readme-ov-file
title: 'karpathy/nanochat: The best ChatGPT that $100 can buy.'
scraped_at: '2026-04-19T06:48:01Z'
word_count: 2364
raw_file: raw/2026-04-19_karpathy-nanochat-the-best-chatgpt-that-100-can-buy_08f8652f.txt
tldr: nanochat is Andrej Karpathy’s minimal, single-GPU-friendly LLM training harness that can take a compute-optimal GPT-style model from tokenization through pretraining, fine-tuning, evaluation, and a ChatGPT-like web UI, with a strong emphasis on speedrun-style benchmarking and under-$100 GPT-2-class training.
key_quote: nanochat is the simplest experimental harness for training LLMs.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Andrej Karpathy
- Alec Radford
- Sofie
tools:
- uv
- torchrun
- wandb
- DeepWiki
- Lambda
libraries:
- PyTorch
companies:
- GitHub
- OpenAI
- Hugging Face
- Lambda
tags:
- llm-training
- gpt-2
- machine-learning-infrastructure
- fine-tuning
- benchmark
---

### TL;DR
`nanochat` is Andrej Karpathy’s minimal, single-GPU-friendly LLM training harness that can take a compute-optimal GPT-style model from tokenization through pretraining, fine-tuning, evaluation, and a ChatGPT-like web UI, with a strong emphasis on speedrun-style benchmarking and under-$100 GPT-2-class training.

### Key Quote
“nanochat is the simplest experimental harness for training LLMs.”

### Summary
- **What it is**
  - A minimal, hackable repository for training and interacting with LLMs end-to-end.
  - Designed to run on a single GPU node, with a cohesive codebase rather than a full-featured framework.
  - Covers the full pipeline: tokenization, pretraining, finetuning, evaluation, inference, and a chat UI.

- **Core idea**
  - The project is built around one main complexity dial: `--depth` (number of transformer layers).
  - Other hyperparameters are derived automatically, including width, number of heads, learning rate adjustments, training horizon, and weight decay.
  - The goal is compute-optimal models across a “miniseries” of sizes, not highly customizable architectures.

- **GPT-2 speedrun / leaderboard**
  - The repo tracks “time to GPT-2,” meaning wall-clock time to reach GPT-2-grade capability as measured by the DCLM CORE score.
  - The reference script is `runs/speedrun.sh`.
  - Current leaderboard entries listed in the README include:
    - Original OpenAI GPT-2 checkpoint: `168 hours`, CORE `0.2565`
    - `d24 baseline, slightly overtrained`: `3.04` hours, val_bpb `0.74833`, CORE `0.2585`
    - `d26 slightly undertrained +fp8`: `2.91` hours, val_bpb `0.74504`, CORE `0.2578`
    - `bump total batch size to 1M tokens`: `2.76` hours, CORE `0.2602`
    - `change dataset to NVIDIA ClimbMix`: `2.02` hours, CORE `0.2571`
    - `autoresearch round 1`: `1.80` hours, CORE `0.2690`
    - `autoresearch round 2`: `1.65` hours, CORE `0.2626`
  - The README emphasizes that GPT-2 training that cost about `$43,000` in 2019 can now be done for about `$48` on an 8×H100 node, or closer to `$15` on a spot instance.

- **Getting started**
  - Dependency management uses `uv`.
  - Install options:
    - `uv sync --extra gpu`
    - `uv sync --extra cpu`
    - `uv sync --extra gpu --group dev`
  - Typical workflow:
    - Train with `bash runs/speedrun.sh`
    - Serve the chat UI with `python -m scripts.chat_web`
  - The README says the speedrun takes about `~3 hours` on an 8×H100 node.

- **Hardware and portability notes**
  - Works on 8×A100 too, but slower.
  - Can run on a single GPU by omitting `torchrun`, with roughly identical results but about `8x` longer runtime.
  - GPUs with less than `80GB` VRAM may require lowering `--device-batch-size`.
  - The code is mostly vanilla PyTorch and is intended to run on CUDA, CPU, MPS, XPU, etc., though not all paths are equally tested.

- **Research usage**
  - Two main experiment scripts are highlighted:
    - `runs/scaling_laws.sh`
    - `runs/miniseries.sh`
  - For quick iteration, the README suggests training a `12-layer` model:
    - `torchrun --standalone --nproc_per_node=8 -m scripts.base_train -- --depth=12 ...`
  - The main metrics to watch in wandb are:
    - `val_bpb`
    - `core_metric`
    - VRAM utilization
    - `train/mfu`
    - `train/tok_per_sec`
  - The README reiterates that `depth` controls the model family and should work consistently across sizes.

- **Precision / dtype design**
  - Does not use `torch.amp.autocast`; precision is controlled explicitly via a global `COMPUTE_DTYPE`.
  - Defaults depend on hardware:
    - CUDA SM80+ (A100/H100): `bfloat16`
    - CUDA SM<80: `float32` by default; `float16` possible via `NANOCHAT_DTYPE=float16`
    - CPU/MPS: `float32`
  - Model weights stay in fp32 for optimizer precision, while a custom `Linear` casts to compute dtype in forward passes.
  - Embeddings are stored directly in compute dtype to save memory.
  - `float16` training uses `GradScaler`; SFT supports it, RL currently does not.

- **Guides and docs**
  - The README points to several Discussions posts:
    - Feb 1 2026: “Beating GPT-2 for <<$100: the nanochat journey”
    - Jan 7 miniseries v1
    - “counting r in strawberry” guide for adding abilities
    - “infusing identity to your nanochat” guide for persona tuning
    - The original Oct 13 2025 nanochat post, now somewhat deprecated
  - The `dev/LEADERBOARD.md` file is referenced for interpreting/contributing to the leaderboard.

- **Repository structure**
  - The README includes a file tree showing:
    - `nanochat/` core modules like `gpt.py`, `engine.py`, `tokenizer.py`, `optim.py`, `core_eval.py`, `chat_ui` assets, etc.
    - `scripts/` for train/eval/chat/tokenizer workflows
    - `runs/` scripts for speedrun, CPU, miniseries, scaling laws
    - `tasks/` for evaluation tasks like ARC, GSM8K, MMLU, HumanEval-like coding, spelling, and custom JSONL conversations
    - `tests/` with `test_engine.py`
  - This makes it clear the repo is both a runnable system and a research sandbox.

- **Contribution philosophy**
  - The project aims to improve micro-model accessibility under `$1000` budgets, while keeping cognitive complexity low.
  - It explicitly avoids giant config objects and framework-style abstraction layers.
  - Current contribution focus is improving pretraining speed to beat GPT-2 faster.
  - PR policy requires disclosure of substantial LLM-generated contributions.

- **Acknowledgements / provenance**
  - Inspired by `nanoGPT` and `modded-nanoGPT`.
  - Thanks Hugging Face, Lambda, Alec Radford, and repository maintenance contributors.
  - The citation block identifies the project as a 2025 GitHub publication by Andrej Karpathy.
  - License is MIT.

### Assessment
This is a **high-durability** reference/documentation page with a **mixed** content type: partly tutorial, partly project overview, partly research/status report. It is **high-density** because it includes concrete commands, hardware requirements, metrics, costs, file structure, and design choices. It is primarily a **primary source** from the maintainer, so it’s useful for evaluating the repo’s current intent and workflow, though some parts are inherently time-sensitive—especially the leaderboard, costs, and dated discussion links. As a reference, it’s best for **refer-back** or **deep-study** depending on whether you want setup instructions or the repo’s design philosophy. The scrape quality looks **good**: the README content appears intact, including code blocks, tables, and the directory tree, though embedded images are present only as references and not inspectable here.
