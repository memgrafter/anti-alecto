---
url: https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/#3-agent-architecture-discovery
title: 'optimize_anything: A Universal API for Optimizing any Text Parameter - GEPA'
scraped_at: '2026-04-19T07:34:40Z'
word_count: 15662
raw_file: raw/2026-04-19_optimize-anything-a-universal-api-for-optimizing-any-text-parameter-gepa_0872c758.txt
tldr: GEPA’s new `optimize_anything` API treats any text-serializable artifact—prompts, code, agent architectures, scheduling policies, even SVGs—as an optimization target, and uses diagnostic feedback plus Pareto search to outperform domain-specific tools across multiple benchmarks.
key_quote: “if your artifact is text and its performance can be measured, you can optimize it.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
- AlphaEvolve
- OpenEvolve
- ShinkaEvolve
- Optuna
libraries:
- GEPA
- gemini-3-flash-preview
- gpt-4.1-mini
- cairosvg
- networkx
- torch
- scipy
- cma
- sklearn
companies:
- GEPA
- Google
- Anthropic
- OpenAI
- Amazon Web Services
- GCP
- Azure
tags:
- llm-optimization
- prompt-engineering
- agent-architectures
- cuda-kernels
- cloud-optimization
---

### TL;DR
GEPA’s new `optimize_anything` API treats any text-serializable artifact—prompts, code, agent architectures, scheduling policies, even SVGs—as an optimization target, and uses diagnostic feedback plus Pareto search to outperform domain-specific tools across multiple benchmarks.

### Key Quote
“if your artifact is text and its performance can be measured, you can optimize it.”

### Summary
- **What the post announces**
  - Introduces `optimize_anything`, a declarative API for optimizing any artifact representable as text.
  - It extends GEPA (Genetic-Pareto), previously a prompt optimizer, to a broader “optimize text artifacts” framework.
  - Core promise: user specifies **what** to optimize and **how to measure it**; the system handles **search, reflection, candidate selection, and strategy**.
  - The post claims it matches or beats domain-specific tools across several tasks.

- **Main API idea**
  - Minimal interface:
    - `seed_candidate` or an `objective` description
    - `evaluator(candidate) -> score (+ diagnostic side info)`
  - `oa.log()` acts like `print()` but routes text to the LLM proposer as **Actionable Side Information (ASI)**.
  - Evaluators can return structured diagnostics: text, dicts, multi-objective scores, and even images via `gepa.Image`.

- **Three optimization modes unified under one API**
  - **Single-task search**: one artifact solves one hard problem; no dataset required.
    - Example: circle packing.
    - This is the mode used by earlier frameworks like AlphaEvolve/OpenEvolve.
  - **Multi-task search**: optimize across a batch of related tasks so improvements transfer.
    - Example: CUDA kernel generation across multiple KernelBench problems.
    - Claimed to outperform single-task optimization in cross-transfer settings.
  - **Generalization**: learn a text artifact that performs well on held-out validation examples.
    - Example: prompt optimization, agent architecture discovery, cloud policy learning.
    - This is the GEPA-style mode most associated with prompt optimization.

- **Why the authors say it works better**
  - **ASI** gives the proposer rich feedback instead of a single scalar.
    - Used for compiler errors, runtime traces, rendered images, spot-availability timelines, etc.
    - The point is to let the LLM behave more like an engineer diagnosing a system than blind evolution.
  - **Pareto-efficient search**
    - Keeps candidates that are best on *some* metric/aspect, not just the best average score.
    - Helps preserve specialized improvements that would be lost by averaging.
  - **Minibatched reflection**
    - Reflection steps show only a subset of examples/metrics at a time.
    - Encourages focused fixes rather than trying to solve everything at once.

- **SVG demo**
  - Optimizes SVG code for “a pelican riding a bicycle” starting from a blank canvas.
  - The evaluator renders SVG to PNG, scores it with a VLM, and returns the rendered image as ASI.
  - Result: improved anatomy, composition, background elements, and overall visual sophistication.
  - Emphasizes that it optimizes the **SVG source code itself**, not a prompt that generates SVG.

- **Case studies and reported results**
  1. **Agent skills / Claude Code**
     - Generalization mode.
     - Repository-specific skills improved resolve rates from **24% to 93%** on one repo and **55% to 82%** on another.
     - Claimed to transfer to Claude Code with near-perfect pass rates and **47% faster** resolution.
  2. **Cloud algorithms**
     - Generalization mode.
     - **CloudCast** broadcast routing: **40.2% cost savings**.
     - **Can’t Be Late** scheduling: **7.8% cost savings**.
     - Claimed to beat ADRS leaderboard / expert heuristics.
  3. **ARC-AGI agent architecture**
     - Generalization mode where the whole agent is the artifact.
     - Seed is a **10-line** agent; evolved into a **170+ line** or **300+ line** multi-stage system depending on the section.
     - Claimed improvement from **32.5% to 89.5%** on ARC-AGI v1 public test accuracy.
     - The learned pipeline includes analyst → developer → validator → optimizer, plus fallback logic.
  4. **AIME prompt optimization**
     - Generalization mode.
     - A system prompt for `gpt-4.1-mini` improved from **46.67% to 60.00%** on AIME 2025.
     - Prompt learned explicit problem-solving discipline and theorem-justified reasoning.
  5. **CUDA kernels / KernelBench**
     - Multi-task search.
     - Shared prompt optimization across multiple kernel problems.
     - Example artifact shown for LayerNorm, with **3.32x speedup** using float4 vectorization, warp shuffles, and a two-pass design.
  6. **Circle packing (n=26)**
     - Single-task search.
     - Starting from a concentric-ring heuristic, GEPA evolved a much larger optimizer.
     - Claimed score **2.63598+**, beating AlphaEvolve’s **2.6358**.
     - The evolved solution is extremely complex and combines LPs, duals, L-BFGS-B, SLP, CMA-ES, multiple seeds, and evolutionary exploration.
  7. **Blackbox mathematical optimization / EvalSet**
     - Single-task search.
     - Learns a solver tailored to each problem, matching or beating Optuna on the 56-problem benchmark.
     - The discussion highlights weaknesses of fixed pipelines like TPE/CMA-ES on deceptive or discontinuous landscapes.

- **Appendix / implementation notes**
  - Shows detailed code walkthroughs for the case studies.
  - Explains evaluator patterns:
    - sandboxing code
    - caching generated programs
    - returning detailed side info
    - extracting warm-starts from prior evaluations
  - Notes a `capture_stdio=True` option that turns `print()` debugging into ASI automatically.
  - Mentions backend-agnostic design: GEPA currently powers the API, but other optimizers could be swapped in.

- **Overall thesis**
  - The post argues that many problems across software, systems, ML, and creative generation can be reframed as **text artifact optimization**.
  - The distinctive combination is:
    - declarative API
    - rich diagnostic feedback
    - Pareto frontier search
    - support for single-task, multi-task, and generalization modes
  - The article is also a broad product/tech showcase, since many of the results are presented as performance claims across benchmarks.

### Assessment
This is a **mixed** content piece with a strong **announcement** core, plus tutorial-style API documentation and many embedded case-study writeups. Durability is **medium**: the conceptual framing of optimizing text artifacts and using diagnostic feedback is fairly durable, but the specific benchmarks, model names, version strings, dates, and claimed results are tied to current systems and will age quickly. Density is **high** because it packs API design, code examples, benchmarks, and multiple detailed application sections into one long post. Originality is mostly **primary source**: it presents the authors’ own API, examples, and reported results rather than summarizing others. It is best used as **refer-back** material if you need the API shape, the three optimization modes, or the concrete case-study claims. Scrape quality is **good** overall: the content includes extensive text and code, though the formatting is somewhat flattened and some visual/demo elements are only described rather than rendered.
