---
url: https://arxiv.org/abs/2502.20379
title: '[2502.20379] Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers'
scraped_at: '2026-04-12T07:37:30Z'
word_count: 372
raw_file: raw/2026-04-12_2502-20379-multi-agent-verification-scaling-test-time-compute-with-multiple-veri_e8b37eaf.txt
tldr: This arXiv paper proposes Multi-Agent Verification (MAV), a test-time compute approach that improves LLM outputs by using multiple verifiers—including prompted off-the-shelf LLMs called Aspect Verifiers—and shows that combining verifiers with best-of-n sampling (BoN-MAV) can outperform self-consistency and reward-model verification.
key_quote: 'we propose a novel scaling dimension for test-time compute: scaling the number of verifiers.'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools: []
libraries: []
companies: []
tags:
- large-language-models
- test-time-compute
- verification
- multi-agent-systems
- artificial-intelligence
---

### TL;DR
This arXiv paper proposes **Multi-Agent Verification (MAV)**, a test-time compute approach that improves LLM outputs by using **multiple verifiers**—including prompted off-the-shelf LLMs called **Aspect Verifiers**—and shows that combining verifiers with **best-of-n sampling (BoN-MAV)** can outperform self-consistency and reward-model verification.

### Key Quote
“we propose a novel scaling dimension for test-time compute: scaling the number of verifiers.”

### Summary
- **Paper title:** *Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers*
- **Field:** Computer Science > Artificial Intelligence
- **Submission date:** **27 Feb 2025**
- **Core idea:** Instead of only scaling model size or number of samples at test time, the authors argue for scaling the **number of verifiers** used to judge candidate outputs.
- **Main proposal: Multi-Agent Verification (MAV)**
  - A test-time compute paradigm that combines **multiple verifiers** to improve LLM performance.
  - The verifiers can be separate models or differently prompted agents that assess outputs from multiple angles.
- **Aspect Verifiers (AVs)**
  - The paper introduces **Aspect Verifiers** as a practical kind of verifier.
  - These are **off-the-shelf LLMs** prompted to check different aspects of an output.
  - They require **no additional training**, making them easy to compose into a verification system.
- **BoN-MAV algorithm**
  - The authors propose **BoN-MAV**, which combines **best-of-n sampling** with **multiple verifiers**.
  - This is presented as a simple multi-agent verification algorithm.
- **Reported behavior / claims**
  - BoN-MAV shows **stronger scaling patterns** than:
    - **self-consistency**
    - **reward model verification**
  - The paper reports **weak-to-strong generalization**, meaning combining weaker verifiers can still improve stronger LLMs.
  - It also reports **self-improvement**, where the same base model is used for both **generation and verification**.
- **Main conclusion**
  - The authors frame **scaling the number of verifiers** as a promising new dimension for improving language model performance at test time.

### Assessment
This is a **research** paper with **medium-to-high durability**: the specific results and benchmarks may age as models and evaluation methods change, but the underlying idea of scaling test-time verification is likely to remain relevant. The content is **dense** and fairly compact, typical of an arXiv abstract, and it reads as a **primary source** rather than commentary or synthesis. It is best used as a **refer-back** reference if you want the paper’s core claim, algorithm name, and headline contributions, though a full read would be needed to assess experimental details and limitations. **Scrape quality is partial**: only the abstract and arXiv page metadata are present, with no full paper text, figures, methods, or results tables.
