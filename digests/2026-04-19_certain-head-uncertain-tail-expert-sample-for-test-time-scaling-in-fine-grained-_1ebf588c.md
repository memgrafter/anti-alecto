---
url: https://arxiv.org/html/2602.02443v1
title: 'Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE'
scraped_at: '2026-04-19T07:45:45Z'
word_count: 9008
raw_file: raw/2026-04-19_certain-head-uncertain-tail-expert-sample-for-test-time-scaling-in-fine-grained-_1ebf588c.txt
tldr: The paper argues that fine-grained MoE routing has a “certain head” of confidently selected experts and an “uncertain tail” of nearly interchangeable experts, and proposes Expert-Sample—a training-free inference method that keeps the head fixed while stochastically sampling the tail to boost multi-sample reasoning diversity and pass@n accuracy.
key_quote: “the router scores exhibit a certain head of high-confidence experts followed by an uncertain tail of low-confidence candidates.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Artetxe
- Brown
- Dai
- DeepSeek-AI
- Habib
- Irvine
- Jain
- Jiang
- Jin
- Kwon
- Ku
- Lu
- Merity
- Naik
- OpenAI
- Pipis
- Rein
- Team
- Wang
- Yang
- Yao
- Yan
- Zhang
- Zhou
tools:
- LightEval
- vLLM
libraries: []
companies:
- DeepSeek-AI
- GPT-OSS
- Qwen
- OpenAI
tags:
- mixture-of-experts
- test-time-scaling
- sampling
- reasoning
- inference
---

### TL;DR
The paper argues that fine-grained MoE routing has a “certain head” of confidently selected experts and an “uncertain tail” of nearly interchangeable experts, and proposes Expert-Sample—a training-free inference method that keeps the head fixed while stochastically sampling the tail to boost multi-sample reasoning diversity and pass@n accuracy.

### Key Quote
“the router scores exhibit a certain head of high-confidence experts followed by an uncertain tail of low-confidence candidates.”

### Summary
- **What the paper is about**
  - Introduces **Expert-Sample**, a **training-free, plug-and-play** test-time sampling method for **fine-grained MoE** models.
  - Goal: improve **test-time scaling** by generating more diverse candidates **without** the instability usually caused by high-temperature token sampling.
  - Core claim: routing scores in fine-grained MoE models show a **certain head / uncertain tail** pattern.

- **Main empirical finding**
  - When the number of activated experts is reduced:
    - **Greedy decoding accuracy stays stable**
    - **Multi-sample pass@n drops sharply**
  - Interpretation:
    - The **top few experts** are enough for deterministic reasoning.
    - The **lower-ranked selected experts** mainly contribute to **diversity** under sampling.
  - Router distributions across models/datasets show a sharp boundary:
    - A few high-confidence experts
    - A flatter tail of low-confidence, near-uniform candidates

- **Method: Expert-Sample**
  - At each MoE layer:
    1. **Keep the top-ranked experts deterministically** (“certain head”).
    2. **Sample remaining experts** from a candidate range in the uncertain tail using **temperature-scaled router logits** and **Gumbel-softmax sampling**.
    3. **Renormalize with original gating weights** for expert output aggregation.
  - No architecture changes, no retraining, and negligible overhead.
  - Designed to **complement token-level sampling**, not replace it.

- **Why it matters**
  - Token sampling faces the usual tradeoff:
    - Higher temperature = more diversity but less stability
    - Lower temperature = more stability but less exploration
  - Expert-Sample moves the diversity source **earlier** in the computation, at the **expert-routing level**, which preserves stability while increasing reasoning-path diversity.

- **Evaluation setup**
  - Models:
    - **Qwen3-30B-A3B-Instruct**
    - **GPT-OSS-20B**
    - **Ling-Lite-1.5**
    - **Qwen3-Next-80B-A3B-Instruct**
    - plus motivation experiments on **DeepSeek-V2-Lite-Chat**
  - Benchmarks:
    - **AIME-120**
    - **GPQA-Diamond**
    - **LiveCodeBench-V6-Lite**
    - plus **AIME 2024/2025, HMMT-2025, MATH-500-Hard**
  - Tools:
    - **LightEval 0.9.1**
    - **vLLM 0.10.2**
    - 8x NVIDIA A800-80G GPUs

- **Key results**
  - On **Qwen3-30B-A3B-Instruct** and **GPQA-Diamond**:
    - **pass@32** improves from **85.4% → 91.9%**
    - **accuracy with Best-of-N verification** improves from **59.1% → 62.6%**
  - Across 12 model-benchmark combinations:
    - average **pass@64** improvement of **4.32%** over normal-temperature token sampling
  - With verification:
    - average gains of **4.28%** over **Best-of-N**
    - average gains of **3.15%** over **Weighted Majority Voting**
  - On “hard” problems, Expert-Sample yields substantially higher reasoning diversity scores than token sampling and high-temperature sampling.

- **Stability vs diversity validation**
  - The paper separates problems into:
    - **Correct Set**: already reliably solvable
    - **Medium Set**: solvable with multiple attempts + verification
    - **Hard Set**: not solved by baseline sampling
  - Expert-Sample:
    - barely affects stability on the Correct Set
    - improves verified accuracy on the Medium Set
    - increases diversity and coverage on the Hard Set

- **Hyperparameter takeaway**
  - The method uses three knobs:
    - number of deterministically kept experts
    - sampling temperature
    - sampling range
  - Authors claim the method is **robust** and does **not require task-specific tuning**
  - Recommended defaults are given in the appendix; the main practical message is that:
    - keeping a small stable head is important
    - medium-to-high temperature works well
    - enlarging the tail candidate pool helps up to a point

- **Overhead**
  - Additional routing operations are claimed to be **negligible**
  - Throughput changes are mostly within **97%–103%** of baseline, i.e. near measurement noise

- **Limitations / trust notes**
  - This is a **research paper with empirical claims**, not a production report.
  - Results are tied to the specific models and benchmarks tested, especially recent MoE checkpoints.
  - Some formulas and symbols are mangled in the HTML scrape, but the narrative and tables are mostly intact.
  - The paper appears current for **2025-era models and checkpoints**, so relevance may fade as MoE routing and inference stacks evolve.

### Assessment
Durability is **medium**: the core idea—using routing-level stochasticity for test-time scaling in MoE—is likely to remain relevant, but the specific model names, checkpoints, and benchmark numbers are tied to recent 2025-era systems. Content type is **research / technical**. Density is **high**, with many concrete experiments, model names, benchmark results, and hyperparameter discussions. Originality is **primary source**, since it presents a new method and experiments rather than summarizing others’ work. Reference style is **deep-study** if you care about MoE inference or test-time scaling, and **refer-back** for the method and reported gains. Scrape quality is **partial**: the main text, tables, and appendix structure are present, but several equations, symbols, and some table formatting are broken or missing.
