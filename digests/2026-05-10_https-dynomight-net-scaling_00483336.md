---
url: https://dynomight.net/scaling/
title: https://dynomight.net/scaling/
scraped_at: '2026-05-10T04:26:47Z'
word_count: 7542
raw_file: raw/2026-05-10_https-dynomight-net-scaling_00483336.txt
tldr: 'Dynomight argues that LLM scaling laws make AI progress more predictable than an “outside view” suggests: more data and compute should keep improving models, but current data quality, available text, and compute costs may become the real bottlenecks before “near-human” performance.'
key_quote: there is no apparent barrier to LLMs continuing to improve substantially from where they are now.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Dynomight
- Andrew Conner
- Tristan Homsi
- Damian Bogunowicz
- Kaplan
- Hoffman
- Gopher
- Chinchilla
- PaLM
- GPT-2
- GPT-3
- GPT-4
- LLaMA
- BigBench
tools: []
libraries: []
companies:
- OpenAI
- Common Crawl
- Google
- Amazon
- Facebook
- WhatsApp
- WeChat
- ArXiv
- Library of Congress
tags:
- ai-scaling
- large-language-models
- scaling-laws
- compute
- data-quality
---

### TL;DR
Dynomight argues that LLM scaling laws make AI progress more predictable than an “outside view” suggests: more data and compute should keep improving models, but current data quality, available text, and compute costs may become the real bottlenecks before “near-human” performance.

### Key Quote
“there is no apparent barrier to LLMs continuing to improve substantially from where they are now.”

### Summary
- **What the post is doing**
  - Presents a “first-principles” argument about AI scaling using empirical scaling laws.
  - Tries to estimate how far language models can improve from:
    - more parameters
    - more training tokens
    - more compute
  - Focuses on whether those gains translate into more “intelligence,” not just lower loss.

- **Core framework**
  - Uses **cross-entropy / log loss** as the main measurable proxy for LLM quality.
  - Argues that loss correlates with broader benchmark performance, citing **BigBench** as an example.
  - The key empirical claim: for certain model families trained on the same dataset, lower loss seems to correspond to better benchmark performance.

- **Scaling law discussed**
  - Cites the Chinchilla-style form where loss is predicted mainly by:
    - **N** = number of parameters
    - **D** = number of training tokens
  - The post emphasizes the decomposition into:
    - **model error** from too few parameters
    - **data error** from too little data
    - **irreducible error** that cannot be eliminated
  - Notes a simple compute relationship:
    - **FLOPs ≈ 6ND**
  - Main implication:
    - current models are often **data-limited**, not just parameter-limited
    - compute should often be spent on **more tokens**, not just bigger models

- **Evidence and examples**
  - Compares major models with estimated parameters/data/compute:
    - GPT-2
    - GPT-3
    - Gopher
    - Chinchilla
    - PaLM
  - Concludes that:
    - GPT-3, Gopher, and PaLM likely spent too much on parameters relative to data
    - Chinchilla is closer to the compute-optimal regime
  - Suggests that some current model-building behavior already reflects this:
    - LLaMA reportedly follows the “smaller model, more data” trend
    - rumored GPT-4 training may also reflect this pattern

- **How much better can models get from more data?**
  - The post estimates large gains are still possible if training data grows by **10x, 100x, or more**.
  - It explores rough token counts available from different sources:
    - internet
    - books
    - Wikipedia
    - scientific papers
    - Twitter
    - text messages
    - YouTube transcripts
    - a “panopticon” surveillance scenario
  - Main conclusion:
    - there may be enough text for substantial scaling, but getting **10¹⁵–10¹⁶ useful tokens** is hard
    - the biggest uncertainty is how much of the internet is actually **usable after filtering**

- **How much better can models get from more compute?**
  - The post argues that compute scaling alone faces strong diminishing returns unless data scales too.
  - It estimates:
    - current frontier training runs are around **10²⁴ FLOPs**
    - much better performance could require **10²⁷ to 10³⁰ FLOPs**
  - Notes that:
    - this is enormously expensive
    - even a lot more compute might only be affordable for rich organizations or nation-states
    - training costs are still declining over time, but not fast enough to make “infinite scale” easy

- **What might be wrong with this whole picture**
  - The post is careful to list major uncertainties:
    - the scaling law itself may break at much larger scale
    - the relationship between **loss** and **useful intelligence** may be weaker than assumed
    - **data quality** may matter as much as quantity
    - **fine-tuning / specialization** may become more important than base-model scaling
    - **multimodal training** or data-generation techniques might change the picture
  - It stresses that extrapolating from current data is risky.

- **Bottom-line conclusion**
  - There is **no obvious hard stop** for LLM improvement yet.
  - More scale should still help in the near term.
  - The main constraints are likely to be:
    - usable data availability
    - compute cost
    - diminishing returns
    - uncertainty about whether present scaling laws continue to hold
  - The author’s overall stance is cautiously optimistic about continued progress, but skeptical of simplistic “scale is all you need” slogans.

- **Appendix material**
  - A long appendix estimates token counts for:
    - Common Crawl / internet
    - Twitter
    - books
    - YouTube
    - scientific papers
    - Wikipedia
    - text messages
    - panopticon-style speech capture
  - Also includes a “compute optimal models” appendix explaining how to choose parameters vs. data for a fixed compute budget.

### Assessment
This is a high-density, mixed opinion/technical essay that tries to synthesize empirical scaling-law results into a practical forecast for AI progress. Its durability is medium: the core ideas about compute/data tradeoffs and scaling behavior are broadly useful, but many specific numbers, model examples, and benchmark references are tied to mid-2023 conditions and will age quickly. The piece is original commentary rather than a primary research paper, though it relies heavily on cited empirical work (especially Kaplan, Chinchilla, and related sources). It works best as a refer-back reference for the author’s overall argument and the rough token/compute estimates, not as a deep-study source. Scrape quality is good overall: the text appears substantially complete, including the appendix content and major tables/estimates, though the formatting of equations and some figures is lost, which matters for the exact mathematical presentation.
