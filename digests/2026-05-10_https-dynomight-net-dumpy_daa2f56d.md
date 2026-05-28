---
url: https://dynomight.net/dumpy/
title: https://dynomight.net/dumpy/
scraped_at: '2026-05-10T04:28:15Z'
word_count: 7089
raw_file: raw/2026-05-10_https-dynomight-net-dumpy_daa2f56d.txt
tldr: Dynomight argues that NumPy makes high-dimensional array programming too mentally taxing, and proposes DumPy—a JAX-backed syntax that uses explicit loop-like indices and named mapped dimensions to preserve vectorization while eliminating broadcasting and shape-mashing confusion.
key_quote: Loops and indices are better.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Dynomight
tools:
- JAX
- NumPy
- PyTorch
- xarray
- uv
libraries:
- jax.vmap
- torch.vmap
companies:
- PyPI
tags:
- array-programming
- tensor-computation
- jax
- numpy
- gpu-computing
---

### TL;DR
Dynomight argues that NumPy makes high-dimensional array programming too mentally taxing, and proposes DumPy—a JAX-backed syntax that uses explicit loop-like indices and named mapped dimensions to preserve vectorization while eliminating broadcasting and shape-mashing confusion.

### Key Quote
"Loops and indices are better."

### Summary
- **What this is:** A long opinionated technical essay introducing **DumPy**, a prototype array-language wrapper built on top of **JAX**.
- **Core thesis:** For high-dimensional tensor work, the easiest notation is often **explicit loops and indices**; NumPy forces users to mentally track shape rules, broadcasting, axis order, and special-cased function behavior.
- **Motivation:** The author argues that:
  - NumPy is excellent for low-dimensional linear algebra.
  - For ≥3D arrays, the complexity of broadcasting and axis manipulation becomes hard to reason about.
  - Modern GPU-centric workflows already rely on compilation/vectorization, so Python loop speed is less important than clarity.
- **Main proposal: DumPy**
  - Users write code that looks like **loops with indices**, but it is **not actually executed as Python loops**.
  - Example pattern:
    - `Z = dp.Slot()`
    - `Z['i', 'j'] = Y['j', :] @ dp.linalg.solve(A['i', 'j', :, :], X['i', :])`
  - `dp.Range(...)` provides loop-like index scoping while still compiling to vectorized operations.
  - A mapped axis system turns string-labeled indices into hidden vectorized dimensions.
- **How it works internally:**
  - Indexing with a string or `dp.Range` creates a **mapped array**.
  - DumPy functions detect mapped dimensions and automatically vectorize over them.
  - `dp.Slot` is used to “unmap” results back to the desired output shape.
  - The underlying vectorization is delegated to **`jax.vmap`**.
- **What DumPy tries to remove from NumPy:**
  - **Broadcasting**: disallowed except for scalars or exactly matching shapes.
  - **Fancy/advanced indexing complexity**: heavily restricted.
  - **Implicit dimension dropping**: all dimensions must be indexed explicitly.
  - **Overloaded functions with confusing batch semantics**: functions like `solve` and `@` are simplified to work only on ≤2D arrays directly; higher-dimensional use is done through indices.
- **Examples compared across systems:**
  - Hilbert matrix construction
  - Batched covariance
  - Moving average
  - Complex indexing
  - Gaussian density evaluation
  - Multi-head self-attention
- **Comparative evaluation:**
  - The author assigns subjective “goodness” scores and concludes DumPy is “**96.93877% as good as loops**” by this made-up metric.
  - DumPy usually scores close to explicit loops and better than raw NumPy/JAX for readability on the showcased tasks.
- **Stance on alternatives:**
  - **APL-like languages:** acknowledged as powerful but still fundamentally involve dimension-mashing by position.
  - **Named-dimension systems like xarray:** promising, but the author says permanent names raise awkward questions for linear algebra (e.g. what should the dimension names be after `A.T @ A` or SVD?).
  - **Julia:** praised for fast loops, but the author’s main interest is GPU execution and clearer notation.
- **Prototype status:**
  - DumPy is presented as a **hacky single-file prototype (~700 lines)**, not intended for serious production use.
  - The author says it works with **`jax.jit`** and **`jax.grad`**.
  - There is also an update saying it became a real package on PyPI: **`dumpy-numpy`**.
  - Installation example:
    - `pip install dumpy-numpy`
    - or `uv run --with dumpy-numpy --with ipython ipython`
- **Bottom line:** The piece is a strong, humorous argument for making tensor programming feel more like writing explicit indexed math, while still compiling to efficient GPU-backed vectorization.

### Assessment
This is a mixed-content technical essay with a clear opinionated thesis and a prototype API demonstration. Durability is **medium**: the conceptual critique of NumPy and the readability argument are fairly timeless, but the concrete implementation details depend on current JAX/NumPy/GPU conventions and the specific DumPy package state. Content density is **high**, with many concrete examples, commands, and code snippets. Originality is **primary source/commentary** rather than synthesis, since it presents the author’s own framework and prototype. It’s best used as **refer-back** material if you care about array-language design, tensor notation, or JAX-style vectorization. Scrape quality is **good** overall: the article text, examples, and update are present, though formatting is messy and code blocks are flattened into inline text.
