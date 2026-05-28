---
url: https://ameer-saleem.medium.com/how-does-multi-head-attention-improve-upon-one-larger-single-head-mechanism-674858597d36
title: How does multi-head attention improve upon one larger single-head mechanism? | by AmeerSaleem | Feb, 2026 | Medium
scraped_at: '2026-04-19T03:53:22Z'
word_count: 2086
raw_file: raw/2026-04-19_how-does-multi-head-attention-improve-upon-one-larger-single-head-mechanism-by-a_4f6424b7.txt
tldr: This article explains why Transformer multi-head attention uses several smaller parallel heads instead of one larger head, arguing that the design helps capture different relationships in text simultaneously while keeping compute roughly comparable to single-head attention.
key_quote: By running multiple heads at once, we allow the transformer the ability to pick up on many different patterns in the training data simultaneously.
durability: high
content_type: tutorial
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- AmeerSaleem
- Neural Foundry
tools: []
libraries: []
companies: []
tags:
- transformers
- attention-mechanisms
- deep-learning
- natural-language-processing
- sequence-models
---

### TL;DR
This article explains why Transformer multi-head attention uses several smaller parallel heads instead of one larger head, arguing that the design helps capture different relationships in text simultaneously while keeping compute roughly comparable to single-head attention.

### Key Quote
“By running multiple heads at once, we allow the transformer the ability to pick up on many different patterns in the training data simultaneously.”

### Summary
- **Context and scope**
  - This is a follow-up to the author’s previous article on **queries, keys, and values** in attention.
  - It focuses on:
    - **multi-head attention**
    - why attention is useful compared with older architectures like **LSTMs**
    - an extra mathematical note on the paper’s **√d_k normalization** footnote

- **What multi-head attention is**
  - The Transformer paper (“Attention is All You Need”, 2017) uses **h = 8** attention heads instead of one large attention mechanism.
  - Each head has its own **Query, Key, and Value** matrices.
  - For a sentence of length **n = 6**, the author describes this as producing **48 self-attention values total** across 8 heads.
  - The outputs of the heads are **concatenated** into one larger matrix.
  - The paper’s notation is slightly more explicit about weight matrices than the simplified explanation in the article.

- **Why multiple heads help**
  - The main benefit is that different heads can learn **different patterns at the same time**.
  - The article uses the example sentence **“you should subscribe to my substack”** and suggests separate heads might learn:
    - the call-to-action structure: “you… should… subscribe”
    - the referential relationship between **subscribe** and **substack**
    - ownership via **my**
    - part-of-speech-like distinctions
  - The author notes that in practice attention heads are a **black box**: there is no guarantee they will learn the exact patterns humans expect.
  - The article also notes that in a simple sentence, multiple heads might redundantly attend to the same patterns.

- **Comparison with LSTMs and older sequence models**
  - A key contrast is with **LSTMs** in seq2seq models, where each step depends on the previous cell’s output.
  - Because of these dependencies, LSTMs cannot process all parts of the pipeline in parallel.
  - Attention heads, by contrast, can be computed in parallel and their outputs combined afterward.

- **Compute and complexity claim**
  - The article states that self-attention has complexity **O(n² · d)**, while recurrent layers have complexity **O(n · d²)**.
  - Here:
    - **n** = sequence length
    - **d** = representation dimension
  - The author argues that because representation dimension is usually larger than sentence length, self-attention is often less computationally demanding in practice.
  - The article also says multi-head attention has **similar computational cost** to the original single-head approach.

- **Extra mathematical section: √d_k normalization**
  - The author responds to a comment about the paper’s footnote and tries to justify a claim about the dot product of random vectors **q** and **k**.
  - Assumptions used:
    - **q** and **k** are independent random vectors of dimension **d_k**
    - each has mean **0**
    - each has variance **1**
  - The goal is to show the dot product **q · k** has:
    - **mean 0**
    - **variance d_k**
  - The author sketches a derivation using:
    - linearity of expectation
    - independence of vector components
    - variance expansion into second moments
    - cancellation of off-diagonal terms through zero-mean/independence reasoning
  - The point is to motivate why scaling by **√d_k** helps normalize attention scores.

- **Overall takeaway**
  - Multi-head attention is presented as a practical way to let Transformers learn **multiple relationships in parallel**, instead of forcing a single attention mechanism to represent everything at once.
  - The article frames this as one of the reasons Transformers outperform older recurrent approaches on sequence tasks.

### Assessment
This is a **tutorial/mixed technical explanation** with moderate-to-high durability: the core Transformer ideas are stable, but the piece is tied to a specific paper discussion and to a 2026 publication date. It is fairly **dense** with concrete claims, equations, and complexity notation, though still written in an approachable, conversational style. The piece is **commentary/synthesis** rather than a primary source, since it explains and interprets the original 2017 Transformer paper rather than presenting new research. It’s best used as a **refer-back** reference if you want a readable refresher on multi-head attention and the author’s derivation of the √d_k footnote. **Scrape quality is partial**: the text is captured well, but the many embedded images/diagrams and any precise equations inside them are not fully available in the markdown, so some mathematical detail is missing.
