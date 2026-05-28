---
url: https://arxiv.org/abs/2603.28052
title: '[2603.28052] Meta-Harness: End-to-End Optimization of Model Harnesses'
scraped_at: '2026-04-19T08:44:09Z'
word_count: 355
raw_file: raw/2026-04-19_2603-28052-meta-harness-end-to-end-optimization-of-model-harnesses_cdec6dc7.txt
tldr: Meta-Harness is an outer-loop system that automatically searches and optimizes LLM “harness” code—what to store, retrieve, and show the model—and reports gains on classification, math reasoning, and coding benchmarks.
key_quote: '“the harness: the code that determines what information to store, retrieve, and present to the model.”'
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies: []
tags:
- large-language-models
- prompt-engineering
- automated-optimization
- retrieval-augmented-generation
- benchmark-evaluation
---

### TL;DR
Meta-Harness is an outer-loop system that automatically searches and optimizes LLM “harness” code—what to store, retrieve, and show the model—and reports gains on classification, math reasoning, and coding benchmarks.

### Key Quote
“the harness: the code that determines what information to store, retrieve, and present to the model.”

### Summary
- **What the paper is about**
  - The paper argues that LLM performance depends not just on model weights, but also on the surrounding **harness**: the code layer that controls memory, retrieval, and context presentation.
  - It says current harnesses are mostly designed by hand, and that existing text optimizers are not well suited because they compress feedback too aggressively.

- **Core idea: Meta-Harness**
  - Meta-Harness is an **outer-loop optimization system** that searches over **harness code** for LLM applications.
  - It uses an **agentic proposer** that can access:
    - the **source code**
    - **scores**
    - **execution traces** of prior candidates
  - This information is made available through a **filesystem**, letting the proposer build on prior attempts more richly than standard text-only optimization loops.

- **Reported results**
  - **Online text classification**
    - Improves over a state-of-the-art context management system by **7.7 points**
    - Uses **4x fewer context tokens**
  - **Retrieval-augmented math reasoning**
    - A single discovered harness improves accuracy on **200 IMO-level problems**
    - Average gain of **4.7 points** across **five held-out models**
  - **Agentic coding**
    - Discovered harnesses beat the best **hand-engineered baselines** on **TerminalBench-2**

- **Main takeaway**
  - The authors claim that giving the optimizer **richer access to prior experience** enables automated harness engineering.
  - The paper’s broader point is that LLM systems can improve substantially by optimizing the surrounding software structure, not only the model itself.

- **What this page is**
  - This is the **arXiv abstract/metadata page**, not the full paper.
  - It includes title, submission date (**30 Mar 2026**), abstract, and arXiv navigation links, but no methods, experiments, or implementation details beyond the abstract.

### Assessment
This is a **research** item with **high durability** in its core framing—optimizing the harness around LLMs is a general concept—but the specific results are tied to the reported benchmarks and current system design, so the empirical claims may age as models and benchmarks change. The content is **dense** for an abstract: it includes the system name, mechanism, and quantitative results. It is a **primary source** at the abstract level, though still only a summary rather than full paper evidence. Best used as a **refer-back** reference if you want to remember the paper’s thesis and headline results; if you need methodology, ablations, or implementation details, you’ll need the PDF. **Scrape quality is good** for the abstract page, but partial in the sense that only the abstract and page metadata were captured, not the full article.
