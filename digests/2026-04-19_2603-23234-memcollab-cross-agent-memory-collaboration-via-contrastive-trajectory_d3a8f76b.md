---
url: https://arxiv.org/abs/2603.23234
title: '[2603.23234] MemCollab: Cross-Agent Memory Collaboration via Contrastive Trajectory Distillation'
scraped_at: '2026-04-19T08:27:15Z'
word_count: 379
raw_file: raw/2026-04-19_2603-23234-memcollab-cross-agent-memory-collaboration-via-contrastive-trajectory_d3a8f76b.txt
tldr: MemCollab proposes a shared memory system for heterogeneous LLM agents by distilling agent-agnostic reasoning constraints from contrasting trajectories, improving transfer across models on math and code tasks.
key_quote: can a single memory system be shared across different models?
durability: high
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
- agent-memory
- cross-agent-transfer
- retrieval
- code-generation
---

### TL;DR
MemCollab proposes a shared memory system for heterogeneous LLM agents by distilling agent-agnostic reasoning constraints from contrasting trajectories, improving transfer across models on math and code tasks.

### Key Quote
“can a single memory system be shared across different models?”

### Summary
- **Problem addressed**
  - LLM-based agents use memory to reuse past problem-solving experience.
  - Existing memory methods are usually **per-agent**, meaning the stored memory is tied to one model’s reasoning style.
  - In heterogeneous deployments, directly transferring memory between agents often **hurts performance** because the memory contains **agent-specific biases** as well as task knowledge.

- **Main idea: MemCollab**
  - The paper proposes **MemCollab**, a collaborative memory framework designed to build **agent-agnostic memory**.
  - It does this by **contrasting reasoning trajectories** from different agents solving the same task.
  - The contrastive process aims to:
    - **distill abstract reasoning constraints**
    - preserve **shared task-level invariants**
    - suppress **agent-specific artifacts**

- **Retrieval mechanism**
  - MemCollab also introduces a **task-aware retrieval mechanism**.
  - Memory access is conditioned on the **task category**, so only relevant constraints are retrieved at inference time.

- **Reported results**
  - Experiments were run on **mathematical reasoning** and **code generation** benchmarks.
  - The abstract claims MemCollab:
    - improves **accuracy**
    - improves **inference-time efficiency**
    - works across **diverse agents**
    - includes **cross-modal-family settings**

- **Implication**
  - The paper argues that collaboratively constructed memory can serve as a **shared reasoning resource** for different LLM-based agents, rather than being locked to one model’s style.

### Assessment
This is a **research** paper abstract with **high durability** in terms of conceptual relevance, since shared memory and cross-agent transfer are likely to remain important themes even as specific model versions change. The content is **dense** and fairly technical, but only at the abstract level, so it gives a strong high-level picture without methodological details. It appears to be a **primary source** rather than commentary or synthesis. For later use, this is best treated as a **refer-back** reference if you care about agent memory, retrieval, or transfer across heterogeneous LLM systems. **Scrape quality is partial**: the abstract and basic paper metadata are present, but the full paper, figures, equations, experiments, and implementation details are missing.
