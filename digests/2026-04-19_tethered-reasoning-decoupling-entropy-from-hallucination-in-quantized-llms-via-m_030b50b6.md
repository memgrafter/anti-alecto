---
url: https://arxiv.org/html/2602.17691v1#abstract1
title: 'Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering'
scraped_at: '2026-04-19T08:10:38Z'
word_count: 5792
raw_file: raw/2026-04-19_tethered-reasoning-decoupling-entropy-from-hallucination-in-quantized-llms-via-m_030b50b6.txt
tldr: Helix is a proposed inference-time “manifold steering” method for quantized LLMs that uses a Unified Truth Score to keep activations near a truthfulness manifold, aiming to preserve high-temperature diversity while reducing hallucination on 4-bit Granite 4.0 H Small.
key_quote: high-temperature “hallucination” is primarily trajectory divergence rather than semantic collapse
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Craig Atkinson
tools:
- llama.cpp
libraries: []
companies:
- IBM
- Verificate Pty Ltd
tags:
- large-language-models
- quantization
- hallucination-mitigation
- inference-time-steering
- creative-generation
---

### TL;DR
Helix is a proposed inference-time “manifold steering” method for quantized LLMs that uses a Unified Truth Score to keep activations near a truthfulness manifold, aiming to preserve high-temperature diversity while reducing hallucination on 4-bit Granite 4.0 H Small.

### Key Quote
"high-temperature “hallucination” is primarily trajectory divergence rather than semantic collapse"

### Summary
- **What the paper claims**
  - Introduces **Helix**, a geometric framework for **decoupling output entropy from hallucination** in quantized LLMs.
  - Core idea: high-temperature failures are treated as **hidden-state trajectory divergence** from a **truthfulness manifold**, not simple semantic collapse.
  - Uses a **Unified Truth Score (UTS)** that combines:
    - token-level semantic entropy
    - Mahalanobis distance from the manifold
  - When UTS indicates divergence, Helix applies **graduated steering vectors** to redirect activations.
  - Steering affects only **0.2–2.5% of tokens**.

- **Main reported results**
  - On **4-bit quantized Granite 4.0 H Small** (**32B total / 9B active**, hybrid **Mamba-Transformer** / Mamba-2 + attention):
    - **GSM8K**: **91.80%** at one setting, exceeding the **87.27% full-precision baseline** by **4.53 pp**
    - **GSM8K** across temperature sweep: **88.84%** at the highest reported temperature, only **2.81 pp** degradation
    - **MMLU**: **72.49%** across **14,042 questions**, only **1.24 pp** degradation
    - **HumanEval**: **82.93%** to **76.83%**, a **6.10 pp** drop across temperatures
  - Claims that steering only the sparse Transformer attention layers (**10% of layers**) can correct drift in the Mamba-2 state-space components.
  - Cross-architecture validation on **Qwen3-30B-A3B MoE** is used to argue the effect generalizes.

- **Creative / high-temperature claim**
  - The paper argues high temperatures expose a **“High-Entropy Creative Reservoir”** rather than only causing degradation.
  - In creative ideation experiments:
    - **30 unique song concepts** across **11 temperatures**
    - **5–20% idea duplication** at high temperature vs **70–80%** at conservative settings
    - Claims **200%+ more unique concepts** using **Multi-Temperature Synthesis**
  - Cross-architecture result cited later: **Qwen3-30B-A3B** produced **46.7% higher unique concept generation** than Granite in the creative setup.

- **Method details worth remembering**
  - UTS is a **per-token** uncertainty signal.
  - The truthfulness manifold is built from prompts/responses drawn from:
    - **TruthfulQA**
    - **WikiText-103**
    - **GSM8K training set**
  - The system is implemented as a **C++ extension of llama.cpp**.
  - Quantization format mentioned: **Q4_K_M**.
  - Hardware: **NVIDIA A100-PCIE-40GB** on an academic HPC cluster.
  - Benchmarks:
    - **GSM8K**
    - **HumanEval**
    - **MMLU**
    - a songwriting / creative ideation task

- **Authors’ broader thesis**
  - Temperature is framed not as a simple quality-vs-diversity knob, but as a dimension that can be safely explored if activations are tethered to a structural manifold.
  - The authors claim Helix enables:
    - temperature-robust reasoning
    - real-time uncertainty telemetry
    - quantization recovery
    - higher-diversity generation without incoherence
  - They also position the method as useful for **resource-constrained deployment** and mention possible applications in product design, hypothesis generation, and creative work.

- **Limitations and caveats stated in the paper**
  - Evaluation is mainly on **Granite 4.0**, with one cross-validation model.
  - Creativity evaluation relies on **semantic similarity and LLM-based judging**.
  - The **High-Entropy Creative Reservoir** is presented as **preliminary / emergent**, not yet systematically characterized.
  - The implementation is **proprietary**; full code is not publicly released.
  - The paper notes a **conflict of interest**:
    - author **Craig Atkinson** is CEO/owner of **Verificate Pty Ltd**
    - and the **patent holder** for Helix
  - AI assistance was used in writing and experiments.

### Assessment
This is a **mixed** technical/research paper with strong **opinionated framing** layered over experimental claims. **Durability is medium** because the results depend on specific models, quantization settings, and 2025–2026 inference-time steering work, though the underlying ideas about entropy, uncertainty, and activation steering are more general. **Density is high**: it is packed with named models, benchmarks, percentages, and architectural claims. **Originality is primary-source** in the sense that it presents the authors’ own method and experiments, though it also situates itself against prior work. It’s best as a **refer-back** reference if you want the method, metrics, or claimed results; not just a skim-once note. **Scrape quality is partial**: the text is substantial, but equations and symbols are broken/missing in places, so some mathematical detail is not faithfully captured from the HTML scrape.
