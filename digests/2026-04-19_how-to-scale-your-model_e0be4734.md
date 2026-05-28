---
url: https://jax-ml.github.io/scaling-book/
title: How To Scale Your Model
scraped_at: '2026-04-19T08:09:27Z'
word_count: 1395
raw_file: raw/2026-04-19_how-to-scale-your-model_e0be4734.txt
tldr: This is a draft book introduction to scaling LLMs on TPUs (and GPUs), focused on roofline analysis, hardware limits, and practical parallelism strategies for training and serving models like LLaMA 3.
key_quote: Training LLMs often feels like alchemy, but understanding and optimizing the performance of your models doesn't have to.
durability: high
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- James Bradbury
- Blake Hechtman
tools:
- JAX
- XLA
- TensorBoard
libraries: []
companies:
- NVIDIA
- LLaMA
tags:
- llm-scaling
- distributed-training
- tpus
- roofline-analysis
- transformer-models
---

### TL;DR
This is a draft book introduction to scaling LLMs on TPUs (and GPUs), focused on roofline analysis, hardware limits, and practical parallelism strategies for training and serving models like LLaMA 3.

### Key Quote
“Training LLMs often feels like alchemy, but understanding and optimizing the performance of your models doesn't have to.”

### Summary
- **What this book is about**
  - A “systems view” of LLMs on TPUs, with an added section on NVIDIA GPUs.
  - Aims to explain how models actually run on hardware, how chips communicate, and how to parallelize training/inference efficiently at scale.
  - Targets questions like:
    - “How expensive should this LLM be to train?”
    - “How much memory do I need to serve this model myself?”
    - “What’s an AllGather?”

- **Main thesis**
  - Scaling is about achieving near-linear throughput increase when adding chips.
  - This is called **strong scaling**.
  - Scaling breaks down when communication overhead grows larger than computation, making the system **communication bound**.
  - The book argues that a small set of principles can explain performance from one accelerator to tens of thousands.

- **Expected background**
  - Assumes familiarity with:
    - LLMs and the Transformer architecture
    - Basics of LLM training
    - Some JAX familiarity is helpful
  - Recommends background reading on the Transformer architecture and the original Transformer paper.

- **What readers should learn**
  - Estimate how close parts of a model are to theoretical optimum.
  - Choose between parallelism strategies at different scales.
  - Estimate training time and cost for large Transformer models.
  - Design algorithms that match hardware constraints.
  - Understand what limits current model performance from a hardware perspective.

- **Book structure**
  - **Part 1: Preliminaries**
    - Chapter 1: Roofline analysis — compute, communication, memory limits.
    - Chapter 2: How TPUs work.
    - Chapter 3: Sharded matrices and distributed matrix multiplication.
  - **Part 2: Transformers**
    - Chapter 4: Transformer math — FLOPs, parameter counts, KV cache size.
    - Chapter 5: Parallelizing Transformers for training.
    - Chapter 6: Training LLaMA 3 on TPUs — cost/time estimation.
    - Chapter 7: Transformer inference — latency, memory, disaggregated serving, KV caches.
    - Chapter 8: Serving LLaMA 3 on TPUs — cost and latency/throughput tradeoffs.
  - **Part 3: Practical Tutorials**
    - Chapter 9: Profiling TPU code with JAX/XLA and TensorBoard.
    - Chapter 10: Programming TPUs in JAX.
  - **Part 4: Conclusions and Bonus Content**
    - Chapter 11: Conclusions and further reading.
    - Chapter 12: How to think about GPUs — networking, rooflines, differences from TPUs.

- **Parallelism and optimization topics covered**
  - Core parallelism methods:
    - Data parallelism
    - Tensor parallelism
    - Pipeline parallelism
    - Expert parallelism
  - Memory-reduction techniques:
    - Rematerialization
    - Optimizer/model sharding (ZeRO)
    - Host offload
    - Gradient accumulation
  - Also discusses:
    - FSDP
    - Megatron sharding
    - Model sharding
    - Distributed inference and serving tradeoffs

- **Practical orientation**
  - The book is not just theory; it includes applied tutorials for:
    - LLaMA 3 training on TPUs
    - LLaMA 3 serving on TPUs
    - Profiling and debugging JAX/TPU code
    - Implementing parallelism in JAX

- **Audience and stance**
  - Written for researchers and engineers working on large models.
  - Suggests that model efficiency is now important even for “small” models, because they often run near hardware limits.
  - Encourages feedback and notes the book is still a draft.

- **Additional notes**
  - Says the first three chapters are preliminary and skippable if already familiar.
  - Says the final three parts may be the most practically useful.
  - Acknowledges James Bradbury and Blake Hechtman as sources of many ideas.

### Assessment
This is a **mixed** reference/tutorial introduction with a strong explanatory tone, and its durability is **high** because the core ideas—roofline analysis, strong scaling, communication bottlenecks, and Transformer parallelism—are broadly timeless even though some examples (like LLaMA 3, TPU v5e, and the new GPU section) are version- and platform-specific. The density is **medium to high**: it packs a lot of named concepts, chapter-level structure, and practical goals into a relatively compact introduction. It appears to be a **synthesis** rather than primary research, drawing together concepts from TPU/GPU systems, distributed training, and Transformer scaling into a coherent book. It is best used as a **refer-back** reference, especially if you want to revisit the book’s scope or locate a chapter on a specific topic. Scrape quality is **good**: the full table-of-contents style content and introductory framing are present, and there’s no obvious indication that code blocks or image-based material were missing.
