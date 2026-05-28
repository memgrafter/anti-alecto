---
url: https://github.com/sanowl/Drag-and-Drop-LLMs-Zero-Shot-Prompt-to-Weights
title: sanowl/Drag-and-Drop-LLMs-Zero-Shot-Prompt-to-Weights
scraped_at: '2026-04-12T09:42:47Z'
word_count: 1091
raw_file: raw/2026-04-12_sanowl-drag-and-drop-llms-zero-shot-prompt-to-weights_4caef1ee.txt
tldr: A GitHub repository for a 2025 MIT-licensed PyTorch project that claims to adapt LLMs in a zero-shot way by generating LoRA weights from text prompts via a cascaded hyper-convolutional decoder.
key_quote: “zero-shot adaptation of Large Language Models through prompt-to-weights generation using cascaded hyper-convolutional decoders.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Zhiyuan Liang
- Dongwen Tang
- Yuhao Zhou
- Xuanlei Zhao
- Mingjia Shi
- Wangbo Zhao
- Zekai Li
- Peihao Wang
- Konstantin Schürholt
- Damian Borth
- Michael M. Bronstein
- Yang You
- Zhangyang Wang
- Kai Wang
tools:
- PyTorch
- Git
- Qwen/Qwen2.5-0.5B
- sentence-transformers/all-MiniLM-L6-v2
libraries:
- Sentence-BERT
- LoRA
companies: []
tags:
- large-language-models
- lora
- prompt-to-weights
- zero-shot-learning
- hypernetworks
---

### TL;DR
A GitHub repository for a 2025 MIT-licensed PyTorch project that claims to adapt LLMs in a zero-shot way by generating LoRA weights from text prompts via a cascaded hyper-convolutional decoder.

### Key Quote
“zero-shot adaptation of Large Language Models through prompt-to-weights generation using cascaded hyper-convolutional decoders.”

### Summary
- This repository presents **Drag-and-Drop LLMs: Zero-Shot Prompt to Weights**, a modular implementation of a system that generates **LoRA (Low-Rank Adaptation) parameters directly from text prompts** rather than fine-tuning the base model in the usual way.
- The core pipeline described is:
  - **SentenceBERTEncoder** converts prompts into semantic embeddings.
  - **CascadedHyperConvolutionalDecoder** maps embeddings into parameter space.
  - **QwenLoRALayer** applies the generated low-rank adaptation weights.
  - **DragAndDropLLM** orchestrates the full process.
- The README emphasizes:
  - **Zero-shot adaptation**
  - **Modular architecture**
  - **YAML-based configuration**
  - **Command-line scripts** for training, evaluation, and inference
- Installation is standard Python:
  - `git clone ...`
  - `pip install -r requirements.txt`
  - verify with `python test_installation.py`
- A troubleshooting section lists expected files under `dnd_llm/models/` and suggests import tests if the model folder is missing.
- Quick-start examples show:
  - initializing with a foundation model like **`Qwen/Qwen2.5-0.5B`**
  - using **`sentence-transformers/all-MiniLM-L6-v2`** as the text encoder
  - training with `DnDTrainer`
  - generating parameters from prompts with `model(prompts)`
  - applying them via `model.apply_parameters(...)`
- Training and evaluation examples use scripts such as:
  - `python scripts/train.py --config configs/default.yaml`
  - `python scripts/evaluate.py --checkpoint ./outputs/final_model.pth --task all`
  - `python scripts/inference.py --checkpoint ... --prompts ... --output generated_weights.pth`
- The project structure is laid out in detail, including:
  - `dnd_llm/models/`
  - `dnd_llm/training/`
  - `dnd_llm/evaluation/`
  - `scripts/`
  - `configs/`
  - `tests/`
- Supported tasks claimed include:
  - **Common sense reasoning**: ARC-e, OBQA, PIQA, HellaSwag, BoolQ, WinoGrande
  - **Code generation**: HumanEval and related benchmarks
  - **Mathematical reasoning**: gsm8K, MATH
  - **Cross-domain transfer**
- The citation block points to an **arXiv 2025** paper:
  - `arXiv:2506.16406`
  - authors include **Zhiyuan Liang, Dongwen Tang, Yuhao Zhou, Xuanlei Zhao, Mingjia Shi, Wangbo Zhao, Zekai Li, Peihao Wang, Konstantin Schürholt, Damian Borth, Michael M. Bronstein, Yang You, Zhangyang Wang, Kai Wang**
- License is **MIT**.

### Assessment
This is a **reference/tutorial/mixed** repository README with moderate-to-high durability: the conceptual framing around LoRA, hypernetworks, and prompt-conditioned adaptation should remain relevant, but the specifics are tied to the repository’s current codebase, cited 2025 arXiv paper, and particular model names like Qwen2.5 and MiniLM. The content density is **high** because it includes architecture claims, usage snippets, scripts, configuration notes, and a full project tree. Originality is **primary source** in the sense that it describes the repository’s own system, though it also markets the paper and cites its authorship. It is best used as **refer-back** material for setup, commands, and architecture confirmation rather than deep study, unless you want the paper itself. Scrape quality appears **good**: the README content is captured broadly and includes code blocks, structure, and citation text, though of course images/badges and any hidden repository files are not included.
