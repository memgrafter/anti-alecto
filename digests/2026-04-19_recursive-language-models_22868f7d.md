---
url: https://arxiv.org/html/2512.24601v2
title: Recursive Language Models
scraped_at: '2026-04-19T08:35:24Z'
word_count: 11156
raw_file: raw/2026-04-19_recursive-language-models_22868f7d.txt
tldr: The paper introduces Recursive Language Models (RLMs), an inference-time scaffold that treats arbitrarily long prompts as an external environment and recursively calls the LLM on prompt slices, enabling much better long-context performance than vanilla LLMs, summarization agents, or retrieval/code-agent baselines.
key_quote: arbitrarily long user prompts should not be fed into the neural network (e.g., Transformer) directly but should instead be treated as part of the environment
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- GPT-5
- Qwen3-Coder-480B-A35B
- Qwen3-8B
- Noah Ziems
- Jacob Li
- James Moore
- Jack Cook
- Matej Sirovatka
- Ofir Press
- Sebastian Müller
- Simon Guo
- Zed Li
tools:
- Python REPL
- CodeAct
- ReAct
- BM25
- prime-rl
libraries: []
companies:
- Laude Institute
- Prime Intellect
- Modal Labs
- Anthropic
- OpenAI
- Qwen Team
- Fireworks AI
tags:
- long-context
- language-models
- recursive-reasoning
- llm-agents
- inference-time-scaling
---

### TL;DR
The paper introduces Recursive Language Models (RLMs), an inference-time scaffold that treats arbitrarily long prompts as an external environment and recursively calls the LLM on prompt slices, enabling much better long-context performance than vanilla LLMs, summarization agents, or retrieval/code-agent baselines.

### Key Quote
“arbitrarily long user prompts should not be fed into the neural network (e.g., Transformer) directly but should instead be treated as part of the environment”

### Summary
- **Core idea**
  - RLMs are a general-purpose inference paradigm for long-context processing.
  - Instead of stuffing the full prompt into the model context window, the prompt is stored externally in a persistent **Python REPL** environment.
  - The model gets constant-size metadata about the prompt and can:
    - inspect prompt slices,
    - decompose the input,
    - store intermediate variables,
    - and recursively invoke itself on sub-prompts.
  - Final answers are returned via a `Final` variable in the REPL, allowing effectively unbounded input/output length.

- **Why this is different from other scaffolds**
  - **Compared with summarization/compaction**:
    - Compaction assumes details can be forgotten; RLMs aim to preserve access by symbolic manipulation.
  - **Compared with retrieval/code agents**:
    - Those can fetch snippets, but still hit the base model’s context limit.
  - **Compared with self-delegation/sub-agent systems**:
    - RLMs emphasize **programmatic recursion**, not just verbalized subcalls, so loops and transformations over large inputs become feasible.

- **Evaluation setup**
  - Tested on two frontier models:
    - **GPT-5**
    - **Qwen3-Coder-480B-A35B**
  - Benchmarks/tasks:
    - **S-NIAH**: single needle-in-haystack retrieval
    - **BrowseComp-Plus (1K documents)**: multi-hop deep research over large offline document corpora
    - **OOLONG**: information aggregation / semantic transformation over long inputs
    - **OOLONG-Pairs**: synthetic quadratic-complexity pair reasoning task
    - **LongBench-v2 CodeQA**: code repository understanding
  - Baselines:
    - base LM
    - **CodeAct + BM25**
    - **CodeAct + sub-calls**
    - **Summary agent** (iterative context compaction)
    - **RLM with REPL**
    - **RLM with REPL, no sub-calls**

- **Main results**
  - RLMs scale to **10M+ token** regimes and outperform all other task-agnostic approaches on long-context tasks.
  - They often beat vanilla frontier LMs by **double-digit percentage gains** while keeping costs comparable.
  - On **BrowseComp-Plus (1K)**, RLM(GPT-5) nearly solves the benchmark and is far better than summarization or retrieval-based methods.
  - On **OOLONG-Pairs**, base models essentially fail, while RLMs achieve much stronger F1 scores, showing that recursion helps especially on **information-dense** tasks.
  - RLM performance degrades much more slowly with increasing context length than base LMs, especially when task complexity grows with input length.

- **Important ablation findings**
  - The **REPL / external prompt storage** is essential for handling long inputs.
  - **Recursive sub-calling** is especially important for dense tasks like OOLONG and OOLONG-Pairs.
  - Even without sub-calls, the RLM scaffold still beats many baselines because it can offload the prompt from the model window.
  - RLMs have **high variance in cost/runtime** because trajectory length depends on task difficulty.
  - Base LMs can still outperform RLMs on **small inputs**, so there is a tradeoff point where recursion is not worthwhile.

- **Native recursive model training**
  - The authors fine-tune **Qwen3-8B** into **RLM-Qwen3-8B**, described as the first natively recursive language model.
  - Training recipe:
    - distill from trajectories of **Qwen3-Coder-480B-A35B** acting as an RLM,
    - use **1,000 filtered trajectories** from unrelated domains,
    - train with a **Python REPL**-based RLM scaffold.
  - Result:
    - RLM-Qwen3-8B outperforms the base Qwen3-8B as an RLM on average,
    - and approaches **vanilla GPT-5** on three long-context tasks.

- **Observed behaviors in trajectories**
  - Models often:
    - chunk by newline or simple heuristics,
    - use regex/keyword searches to probe the prompt,
    - store partial results in variables,
    - stitch outputs from recursive calls into a final answer.
  - GPT-5 tends to be more conservative with subcalls.
  - Qwen3-Coder often overuses subcalls, sometimes making hundreds to thousands of them, and sometimes fails to return the computed answer correctly.

- **Limitations and future work**
  - Current experiments use **synchronous, sequential subcalls**, which makes RLMs slower than necessary.
  - Only **max recursion depth of one** was explored (subcalls are LMs, but not deeper recursive nesting).
  - The authors say more realistic and harder long-context tasks remain underexplored.
  - They suggest future work on:
    - asynchronous calls,
    - sandboxed REPLs,
    - deeper recursion,
    - hybrid symbolic recursion + neural attention,
    - better native RLM training at larger scale.

- **Paper’s overall claim**
  - RLMs are presented as a new inference-time axis for scaling LLMs:
    - not by increasing the context window directly,
    - but by letting the model recursively reason over the prompt as an external object.

### Assessment
This is a **research/technical** paper with high **density** and mostly **primary-source** content, since it reports a new method, benchmarks, ablations, and a small fine-tuning experiment. Its **durability** is medium: the conceptual framing of externalizing long prompts and recursive sub-calling should remain useful, but the exact results, model names, costs, and benchmark scores will age quickly as GPT-5, Qwen variants, and long-context baselines evolve. It is best used as a **deep-study** reference if you care about long-context agents, recursive tool-use, or inference-time scaling. The scrape quality is **good overall**: the paper text, tables, appendices, benchmark descriptions, and trajectory examples are present, though some table values appear partially garbled/missing in the extracted HTML and figures are not included.
