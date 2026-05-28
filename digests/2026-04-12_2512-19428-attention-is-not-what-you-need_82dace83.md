---
url: https://arxiv.org/abs/2512.19428
title: '[2512.19428] Attention Is Not What You Need'
scraped_at: '2026-04-12T07:35:20Z'
word_count: 468
raw_file: raw/2026-04-12_2512-19428-attention-is-not-what-you-need_82dace83.txt
tldr: This paper argues that explicit self-attention may not be necessary for strong sequence modeling, and proposes an attention-free Grassmann-manifold architecture that achieves competitive results on language modeling and NLI with linear sequence-length scaling.
key_quote: “explicit self-attention actually necessary for strong performance and reasoning?”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people: []
tools: []
libraries: []
companies: []
tags:
- sequence-modeling
- self-attention
- geometric-deep-learning
- language-modeling
- natural-language-inference
---

### TL;DR
This paper argues that explicit self-attention may not be necessary for strong sequence modeling, and proposes an attention-free Grassmann-manifold architecture that achieves competitive results on language modeling and NLI with linear sequence-length scaling.

### Key Quote
“explicit self-attention actually necessary for strong performance and reasoning?”

### Summary
- **What the paper asks**
  - Revisits a core sequence-modeling question: whether self-attention is truly necessary for performance and reasoning.
  - Frames standard multi-head attention as a kind of **tensor lifting**: hidden states are projected into a high-dimensional space of pairwise interactions.
  - Argues that while expressive, this becomes mathematically opaque after many layers, making it hard to describe with simple invariants.

- **Proposed alternative: Grassmann flows**
  - Introduces an **attention-free architecture** based on **Grassmann manifolds**.
  - The central module is a **Causal Grassmann layer**, which:
    1. **Linearly reduces token states**
    2. **Encodes local token pairs** as 2D subspaces on a Grassmann manifold using **Plücker coordinates**
    3. **Fuses geometric features** back into hidden states via **gated mixing**
  - The intended effect is that information moves through **controlled deformations of low-rank subspaces** across multi-scale local windows, rather than through an \(L \times L\) attention matrix.

- **Computational claim**
  - The paper says Grassmann mixing has **linear scaling in sequence length for fixed rank**.
  - This is presented as a more structured and interpretable alternative to dense attention.

- **Reported experiments**
  - **Wikitext-2 language modeling**
    - Purely Grassmann-based models with **13M to 18M parameters**
    - Achieve validation perplexities within roughly **10–15%** of size-matched Transformers
  - **SNLI natural language inference**
    - A **Grassmann-Plücker head** on top of **DistilBERT**
    - Slightly outperforms a Transformer head
    - Best validation/test accuracies:
      - Grassmann-Plücker: **0.8550 / 0.8538**
      - Transformer head: **0.8545 / 0.8511**

- **Stated takeaway**
  - The authors argue manifold-based designs may offer a more structured route to **geometric** and **invariant-based** interpretations of neural reasoning.
  - The paper positions itself as both a theoretical reframing of attention and an empirical exploration of an attention-free alternative.

### Assessment
This is a **mixed** research/technical paper with a strong theoretical pitch and some benchmark results. Its **durability is medium**: the geometric framing is likely to remain interesting, but the empirical claims are tied to specific models, datasets, and the state of sequence modeling research as of its **22 Dec 2025** submission date. The content is **high density**, packing conceptual claims, architecture details, complexity analysis, and benchmark numbers into a short abstract. It is **primary source** material, since it presents the authors’ own model and results rather than summarizing others. Best used as **deep-study** if you care about alternative sequence architectures, geometric deep learning, or attention replacements. Scrape quality is **good** for the abstract and metadata shown, but **partial** overall because only the abstract and surrounding page elements are captured; the full PDF, methods, proofs, and experimental details are not included.
