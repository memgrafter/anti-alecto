---
url: https://news.ycombinator.com/item?id=47203219#47239261
title: 'TorchLean: Formalizing Neural Networks in Lean | Hacker News'
scraped_at: '2026-04-19T21:46:08Z'
word_count: 914
raw_file: raw/2026-04-19_torchlean-formalizing-neural-networks-in-lean-hacker-news_82b93de1.txt
tldr: In this Hacker News thread on TorchLean / formalizing neural networks in Lean, the top commenter argues that quantum Fourier transform does not replace self-attention on classical LLMs, while the rest of the discussion ranges from formal verification of quantized attention and overflow bugs to confusion about floating-point, quantization, and whether “math insight” from Lean would help.
key_quote: No. The quantum Fourier transform is just a particular factorization of the QFT as run on a quantum computer. It's not any faster if you run it on a classical computer.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: skim-once
scrape_quality: partial
people: []
tools:
- Lean
- SageAttention
- QLoRA
libraries:
- PyTorch
companies: []
tags:
- neural-networks
- formal-verification
- quantization
- quantum-computing
- floating-point-arithmetic
---

### TL;DR
In this Hacker News thread on **TorchLean / formalizing neural networks in Lean**, the top commenter **`u/`(not shown in the scrape)** argues that **quantum Fourier transform does not replace self-attention on classical LLMs**, while the rest of the discussion ranges from formal verification of quantized attention and overflow bugs to confusion about floating-point, quantization, and whether “math insight” from Lean would help.

### Key Quote
> “No. The quantum Fourier transform is just a particular factorization of the QFT as run on a quantum computer. It's not any faster if you run it on a classical computer.”

### Summary
- **Top comment (verbatim):** “No. The quantum Fourier transform is just a particular factorization of the QFT as run on a quantum computer. It's not any faster if you run it on a classical computer. And to run (part of) LLMs would be more expensive on a quantum computer (because using arbitrary classical data with a quantum computer is expensive).”
- **Top commenter:** `u/` not visible in the provided scrape
- **Thread topics:**
  - Whether **FFT / QFT / IQFT** can substitute for **self-attention** in LLMs
  - Whether **quantum logic / probabilistic logic** is more appropriate for universal function approximation or physical simulation
  - Whether **formal verification in Lean** could help analyze attention and quantized arithmetic
  - **Quantization bugs and overflow**, including mention of **SageAttention**
  - Confusion around **floating-point representation**, infinity, and finite precision arithmetic

- The original question tries to connect **TorchLean** to a claim that self-attention can be replaced with FFT “for a loss in accuracy and a reduction in kWh,” and asks whether Lean formalisms can explain that or whether **QFT/IQFT** could similarly replace attention in LLMs.
- The first substantive reply rejects the quantum claim:
  - QFT is a quantum algorithm/factorization, not a classical speedup.
  - Using quantum computers for arbitrary classical LLM data is expensive.
- A later comment broadens into speculation about:
  - **quantum probabilistic logic**
  - **Constructor Theory counterfactuals**
  - “quantum embedding” of trained LLMs into qubit registers
  - whether programmable quantum circuits could outperform convolution/feed-forward methods
- Another major branch of the thread is about **formal verification for quantized neural networks**:
  - one commenter says Lean could help determine when **quantization overflows intermediate results**
  - cites **SageAttention (int8 quantized attention)** as a practical example where some models produce **black images** due to overflow
  - notes that current methods don’t clearly support training safely
- The thread then shifts into clarification about **quantized arithmetic vs IEEE floating point**:
  - one commenter links an arXiv paper on **integer quantization**
  - mentions **4-bit NormalFloat (NF)**, **quantile quantization**, **QLoRA**, and **float8 quantized fine-tuning**
  - another points out that all digital computers are quantized at some level
- The conversation ends in a back-and-forth about **finite precision and representable numbers**:
  - one user asks about infinity and whether it is “stored between 0-1”
  - replies explain that floating-point has **finite representable numbers**, with more density near zero
  - arithmetic on finite precision is **not associative**
  - another clarifies that real numbers themselves aren’t what computers store; computers store finite approximations

### Assessment
This is a **mixed social thread** with a strong technical slant and lots of side discussion rather than a single coherent argument. Its **durability is medium**: the high-level questions about formal verification, quantization overflow, and floating-point limits are durable, but the specific references to current tools like **SageAttention** and recent quantization methods are more time-sensitive. The content is **high-density but conversational**, with several speculative or confused exchanges mixed with a few concrete technical claims and citations. It is mostly **commentary/secondary discussion**, not a primary source of new research. Best used as a **skim-once / refer-back** item if you want the shape of the debate, not a rigorous reference. **Scrape quality is partial**: the thread content is captured only as a text excerpt, and the actual commenter handles, comment tree structure, and any linked context are incomplete or missing.
