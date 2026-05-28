---
url: https://alexzhang13.github.io/blog/2025/rlm/
title: Recursive Language Models | Alex L. Zhang
scraped_at: '2026-04-12T07:36:59Z'
word_count: 4171
raw_file: raw/2026-04-12_recursive-language-models-alex-l-zhang_a389da53.txt
tldr: 'Alex Zhang’s post introduces Recursive Language Models (RLMs): a wrapper/inference strategy that lets an LLM recursively call itself or smaller LLMs inside a REPL-like environment to process extremely long contexts, with early results showing strong gains on long-context benchmarks like OOLONG and BrowseComp-Plus.'
key_quote: “RLMs are designed based on the principle that fundamentally, LMs should decide how to break down a problem to be digestible for an LM.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Alex Zhang
- Omar Khattab
- Tim Kraska
- Noah Ziems
- Jacob Li
- Diane Tchuindjo
- James Moore
- Jason Mohoney
- Amadou Ngom
- Ziniu Wu
- Jack Cook
tools:
- GPT-5
- GPT-5-mini
- Python REPL
- Jupyter Notebook
- BM25
- ReAct
libraries: []
companies:
- MIT OASYS
- MIT DSG
- Laude Institute
tags:
- long-context
- llm-inference
- recursive-reasoning
- agents
- benchmark-evaluation
---

### TL;DR
Alex Zhang’s post introduces Recursive Language Models (RLMs): a wrapper/inference strategy that lets an LLM recursively call itself or smaller LLMs inside a REPL-like environment to process extremely long contexts, with early results showing strong gains on long-context benchmarks like OOLONG and BrowseComp-Plus.

### Key Quote
“RLMs are designed based on the principle that fundamentally, LMs should decide how to break down a problem to be digestible for an LM.”

### Summary
- **What RLMs are**
  - A **recursive inference strategy** for language models.
  - The user experiences it like a normal model call, e.g. `rlm.completion(messages)` as a drop-in replacement for `gpt5.completion(messages)`.
  - Under the hood, the root model only sees the query and interacts with an **environment** that stores the full prompt/context.
  - The environment in this post is a **Python REPL / notebook** where the context is stored as a variable in memory.

- **Core idea**
  - Instead of forcing one model call to ingest a massive context, the root LM can:
    - inspect small parts of the context,
    - partition or grep through it,
    - launch recursive sub-calls to the same or another LM,
    - and then synthesize a final answer.
  - The authors frame this as a way to address **“context rot”**: performance degradation as contexts become long and messy.

- **Why they think it matters**
  - It offers a way to scale **test-time compute** without requiring a single model call to handle the full long context.
  - The choice of how to decompose the context is left to the model itself, rather than hard-coded by the system designer.
  - They suggest this could become the next step after **CoT-style reasoning** and **ReAct-style agents**.

- **Implementation details**
  - The specific setup described uses **GPT-5 or GPT-5-mini** as the root LM in a Python REPL environment.
  - The root LM can:
    - directly output `FINAL(answer)`,
    - or construct an answer in a variable and return it via `FINAL_VAR(final_ans_var)`.
  - The context can be treated programmatically as a Python variable, which the model can inspect, transform, chunk, and query recursively.
  - The environment is flexible in principle; they argue REPL/code is a good instantiation.

- **Observed behaviors / strategies**
  - The blog highlights several patterns the RLM learns to use:
    - **Peeking**: inspect a small slice of the context first.
    - **Grepping**: use regex/keyword search to narrow candidates.
    - **Partition + Map**: split context into chunks and recursively label/process them.
    - **Summarization**: summarize subsets for higher-level reasoning.
    - **Long-input, long-output** handling: programmatically process very long sequences or outputs.
  - The authors emphasize these are **interpretable trajectories** of the system.

- **Benchmarks and results**
  - **OOLONG benchmark**
    - They focus on the `trec_coarse` split.
    - Queries involve distributional questions over thousands of rows, with user IDs and unlabeled instances.
    - They evaluate:
      - GPT-5
      - GPT-5-mini
      - RLM(GPT-5-mini)
      - RLM(GPT-5) without sub-calls
      - ReAct + GPT-5 + BM25
    - On contexts over **128k tokens** (about 100 queries), **RLM(GPT-5-mini)** reportedly:
      - outperforms GPT-5 and GPT-5-mini by **more than 33% raw score**,
      - roughly matches GPT-5 API cost per query,
      - and recursion contributes about **10%** of the gain.
    - They also report similar but somewhat degraded gains around **263k tokens**.

  - **BrowseComp-Plus retrieval-style experiments**
    - These involve multi-hop questions over large corpora where the answer exists in the provided documents.
    - They compare:
      - GPT-5
      - truncated GPT-5
      - GPT-5 + pre-query BM25
      - RLM(GPT-5)
      - RLM(GPT-5) without sub-calls
      - ReAct + GPT-5 + BM25
    - They test with **10, 50, 100, and 1000 documents**.
    - Reported result: **RLM(GPT-5)** is the only method that maintains **perfect performance at 1000 documents**, while base GPT-5 variants degrade as document count increases.
    - The no-recursion ablation still does well but worse than full RLM.
    - They note the results are preliminary and based on a subset of the dataset.

- **Long output / programmatic tasks**
  - They discuss tasks where the model must generate or transform long outputs, such as tracking long git diffs or producing complete results from histories.
  - On one example family (LoCoDiff), they say GPT-5 struggles badly beyond **75k tokens**.
  - RLMs sometimes solve these by **programmatically processing the sequence** rather than trying to reason in a single pass.

- **Limitations and caveats**
  - The implementation is **not optimized for speed**.
  - Recursive calls are **blocking** and do not use **prefix caching**.
  - Query time can range from **seconds to minutes** depending on recursion depth and partitioning.
  - They do **not** yet have strong guarantees on total API cost or runtime.
  - The BrowseComp-Plus results are explicitly described as **preliminary** and based on a **small subset**.

- **Positioning relative to prior work**
  - They distinguish RLMs from standard **agents**:
    - agents decompose by **task/problem**,
    - RLMs decompose by **context**.
  - They mention related ideas like **MemGPT**, **CodeAct**, **ROMA**, **THREAD**, and long-context architecture work such as **ALiBi** and **YaRN**.
  - They argue RLMs sidestep some of the need to directly “solve” context rot by avoiding huge single-pass context ingestion.
  - They also frame RLMs as a complement to systems and architecture work, not a replacement.

- **Broader thesis**
  - RLMs are presented as a new bet for long-context inference:
    - the model decides how to split and recurse,
    - the system exposes a structured environment for doing so,
    - and improvements in base model capability should directly improve RLM capability.
  - Their final stance is exploratory but optimistic: the authors think RLMs may be a powerful future paradigm for inference-time scaling.

- **References / links included in the post**
  - Full paper: `https://arxiv.org/abs/2512.24601v1`
  - Official codebase: `https://github.com/alexzhang13/rlm`
  - Minimal implementation: `https://github.com/alexzhang13/rlm-minimal`
  - Twitter/X summary: `https://x.com/a1zhang/status/1978469116542337259`
  - Citation is provided for the October 2025 blog post.

### Assessment
This is a **mixed** technical/research blog post with announcement-like elements, centered on a new inference framework and early benchmark results. Durability is **medium**: the core idea of recursive context decomposition may age well, but the specific claims, model names (GPT-5/GPT-5-mini), benchmark numbers, and GitHub links are tied to current-era models and an early research snapshot. The content is **high-density** and fairly specific, with concrete benchmark names, dataset splits, and performance claims, and it is clearly **primary source** material from the authors rather than synthesis or commentary. As a reference, it is best used **deep-study** if you want the method and evidence, or **refer-back** if you want to recall the main framing, results, and implementation links. **Scrape quality is good** overall: the post content, citations, and most sections are present, though the text appears partially duplicated in places and some figure/code/image elements referenced in the prose are not included.
