---
url: https://blog.mariusvach.com/posts/gepa-sudoku-solver
title: Speeding up a Sudoku solver with GEPA `optimize_anything` - Marius Vach Blog
scraped_at: '2026-04-19T08:37:18Z'
word_count: 1677
raw_file: raw/2026-04-19_speeding-up-a-sudoku-solver-with-gepa-optimize-anything-marius-vach-blog_eb9223f8.txt
tldr: Marius Vach shows how GEPA’s new optimize_anything API can automatically improve a Python Sudoku solver, finding a bitmask/MRV/least-constraining-value version that scores 4.4× better than the numpy baseline after 8 iterations and 534 evaluator calls.
key_quote: You can truly optimize anything with it.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Marius Vach
- Lakshya Agrawal
- Arto Inkala
tools:
- GEPA
- optimize_anything
- DSPy
- Hugging Face
libraries:
- numpy
- pandas
companies: []
tags:
- sudoku
- optimization
- llm-workflows
- python
- prompt-optimization
---

### TL;DR
Marius Vach shows how GEPA’s new `optimize_anything` API can automatically improve a Python Sudoku solver, finding a bitmask/MRV/least-constraining-value version that scores 4.4× better than the numpy baseline after 8 iterations and 534 evaluator calls.

### Key Quote
“**You can truly optimize anything with it.**”

### Summary
- **What the post is about**
  - A February 21, 2026 blog post by Marius Vach describing a hands-on experiment with the newly released GEPA `optimize_anything` API.
  - The experiment uses GEPA to optimize a simple Sudoku solver originally written for clarity, not speed.

- **Why GEPA fits this use case**
  - GEPA takes:
    - a **seed artifact** (the initial solver code),
    - an **evaluation function**,
    - a **dataset**,
    - and optional natural-language objective/background context.
  - The post emphasizes that this new API makes optimization of text-based artifacts more streamlined and less tied to the broader DSPy stack.

- **Dataset and setup**
  - Uses the Hugging Face dataset **`sapientinc/sudoku-extreme`**.
  - Loads a parquet sample from the test set, then creates:
    - **170 training puzzles**
    - **81 validation puzzles**
  - Splits are stratified by difficulty (`rating`).
  - Adds **AI Escargot** manually to the validation set as an especially hard puzzle.
  - AI Escargot is identified as a puzzle by Finnish mathematician **Arto Inkala**.

- **Seed solver**
  - The original solver is a simple Python/Numpy implementation using:
    - **constraint propagation**
    - **naked singles**
    - **hidden singles**
    - **recursive backtracking**
  - The author explicitly says it was designed for educational clarity, not performance.

- **Evaluation function**
  - The evaluator:
    - executes candidate code with `exec(...)` in an isolated namespace,
    - checks for compile errors, missing `solve`, and runtime errors,
    - times the `solve()` call with `time.perf_counter()`,
    - returns a score plus diagnostic side information.
  - Scoring combines:
    - **85% speed**
    - **15% brevity**
  - Wrong answers receive score **0**, regardless of runtime.
  - Speed is scaled so roughly **10 ms = 0**, instant = 1.

- **Baseline behavior**
  - Example evaluations of the seed solver show:
    - one hard puzzle taking about **0.0106 s** with a near-zero time score,
    - another taking about **0.00184 s** with a much better time score.
  - The author notes this demonstrates GEPA’s separation of concerns: the evaluator is plain Python and independent of GEPA itself.

- **GEPA run**
  - GEPA is installed at version **0.1.0**.
  - The optimization call uses:
    - `GEPAConfig`
    - `EngineConfig(max_metric_calls=500)`
    - `ReflectionConfig(reflection_lm="openai/gpt-5.2")`
  - The objective is to maximize speed while preserving **100% correctness** for an 81-character puzzle string in / 81-character solution string out.

- **Results**
  - The run reports:
    - **8 iterations**
    - **534 evaluator calls**
    - **6 candidates explored**
  - Candidate table summary:
    - **0 (seed): 0.072**
    - **1: 0.269**
    - **2: 0.245**
    - **3 (best): 0.322**
    - **4: 0.238**
    - **5: 0.249**
  - The best candidate is described as **4.4× better** than the original solver on the scoring metric.

- **What GEPA discovered**
  - The best-performing solver moved away from numpy and toward:
    - **pure Python lists**
    - **9-bit bitmasks**
    - **trail-based undo** instead of copying the grid
    - **MRV** (minimum remaining values) heuristic
    - **least-constraining value** heuristic
    - **precomputed lookup tables** (`POPC`, `LOWDIG`, `DIGITS`)
  - The author notes that many very hard puzzles still score near zero because runtime exceeds the 10 ms cutoff in the scoring function.

- **Comparison against baseline**
  - On a sample puzzle, the optimized solver is shown to be about **an order of magnitude faster** than the baseline, though it has roughly **3× as many lines of code**.
  - The article includes a performance image (`/images/gepa_sudoku.webp`) and links to both the seed and optimized GitHub gists.

- **Author’s takeaway**
  - The post argues that the new GEPA API is a significant step forward because it can optimize **any text-based artifact**, not just prompts.
  - The author speculates about future uses such as:
    - optimizing **SQL queries**
    - optimizing **agent prompts/skill files**
    - minimizing token usage in task execution

### Assessment
This is a **mixed** technical blog post and experiment report, with a strong **tutorial/implementation** flavor and some commentary about GEPA’s broader implications. **Durability is medium**: the optimization pattern, evaluator design, and solver heuristics are broadly useful, but the specifics are tied to **GEPA 0.1.0**, **GPT-5.2**, a particular dataset, and the author’s February 2026 environment. **Density is high** because it includes concrete code, metrics, dataset splits, and comparison results. **Originality is primary source** in the sense that it reports the author’s own experiment and results rather than summarizing others. **Reference style** is **refer-back**: useful if you want to reproduce the setup, compare solver heuristics, or understand GEPA’s `optimize_anything` workflow. **Scrape quality is good** overall: the main narrative, code excerpts, metrics, and results are present, though full code blocks are truncated and the embedded performance image cannot be inspected from the scrape.
