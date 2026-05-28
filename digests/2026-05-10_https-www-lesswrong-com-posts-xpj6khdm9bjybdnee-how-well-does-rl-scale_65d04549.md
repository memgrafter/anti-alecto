---
url: https://www.lesswrong.com/posts/xpj6KhDM9bJybdnEe/how-well-does-rl-scale
title: https://www.lesswrong.com/posts/xpj6KhDM9bJybdnEe/how-well-does-rl-scale
scraped_at: '2026-05-10T04:30:56Z'
word_count: 7924
raw_file: raw/2026-05-10_https-www-lesswrong-com-posts-xpj6khdm9bjybdnee-how-well-does-rl-scale_65d04549.txt
tldr: Toby Ord argues that RL post-training for LLMs scales much worse than pre-training or inference scaling, so its main practical value is unlocking longer chains of thought rather than efficiently turning more training compute into more intelligence.
key_quote: “Now that RL-training is nearing its effective limit, we may have lost the ability to effectively turn more compute into more intelligence.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: partial
people:
- Toby Ord
- Daniel Kokotajlo
- Jacob Hilton
- Wei Dai
- Vladimir Nesov
- Stanislav Krym
tools: []
libraries: []
companies:
- OpenAI
- Anthropic
- xAI
- Google
tags:
- reinforcement-learning
- llm-scaling
- inference-scaling
- ai-governance
- ai-timelines
---

### TL;DR
Toby Ord argues that RL post-training for LLMs scales much worse than pre-training or inference scaling, so its main practical value is unlocking longer chains of thought rather than efficiently turning more training compute into more intelligence.

### Key Quote
“Now that RL-training is nearing its effective limit, we may have lost the ability to effectively turn more compute into more intelligence.”

### Summary
- **What the post argues**
  - RL-training for reasoning models appears to have a much worse compute-efficiency curve than inference scaling.
  - Ord distinguishes:
    - **RL-scaling**: spending more compute on RL training during post-training
    - **Inference-scaling**: spending more compute at deployment so the model thinks longer
  - His core claim is that RL’s biggest effect is not a direct boost at fixed token budget, but enabling models to use much longer chains of thought.

- **Evidence and scaling claims**
  - On OpenAI’s original o1 chart, Ord says the RL-scaling slope is about half the inference-scaling slope on a log x-axis.
  - He interprets this as:
    - **100x inference compute** often taking a model from roughly **20% to 80%** on reasoning benchmarks like AIME
    - **100x RL training compute** only moving performance from about **33% to 66%**
  - From this, he extrapolates that:
    - **10,000x RL compute** may be needed to get the same capability gain as **100x inference compute**
    - Roughly **1,000,000x RL compute** might be needed for a GPT-level jump comparable to **100x pre-training compute**
  - He cites later OpenAI charts around **o3** and **GPT-5** as consistent with the same pattern.

- **Why this matters economically**
  - Early RL gains were “cheap” because RL compute started from a tiny base relative to pre-training.
  - Once RL compute approaches or exceeds pre-training compute, the economics worsen sharply:
    - training cost rises a lot
    - but the resulting capability gain is still modest compared with inference scaling
  - He argues this makes further large RL scale-ups infeasible:
    - frontier labs may be near the point where RL is no longer a cheap lever
    - the next big gains may depend on inference scaling instead

- **Interpretation and implications**
  - Ord’s conclusion is not that RL becomes useless, but that:
    - RL is a poor way to convert compute into intelligence at large scale
    - its main legacy is enabling longer reasoning traces
  - He says this changes AI progress dynamics because inference scaling:
    - raises ongoing deployment costs
    - affects pricing, usage, governance, and safety differently from one-time training spend
  - He suggests compute scaling may now be less effective overall than many expected, which could lengthen timelines and alter strategy.

- **Comment/reply themes from the thread**
  - **Daniel Kokotajlo** argues Ord may be underestimating how much RL changes the plateau of the inference-scaling curve, and that RL can unlock new capability levels rather than merely substituting for longer inference.
  - **Toby Ord** replies that RL’s main importance is indeed enabling inference scaling, but he thinks that does not rescue RL as a cheap path to large capability gains.
  - **Jacob Hilton** questions whether Ord’s “worse slope” claim is really a mathematical effect of RL itself versus an artifact of episode length, information density, or data/overfitting dynamics.
  - **Wei Dai** shifts to a meta-point: it is worrying that highly capable philosophically trained AI-safety people are spending time on forecasting rather than direct safety work.
  - Other commenters discuss:
    - compute-optimal tradeoffs between pre-training and RL
    - whether RL can produce specialized skills or continual learning
    - whether longer contexts and more agentic scaffolding change the picture
    - whether public evidence is too thin to justify the strongest numerical extrapolations

### Assessment
This is an opinionated analytical post rather than a technical paper, but it is fairly dense and specific, with detailed comparisons across o1, o3, GPT-5, AIME, SWE-bench, GPQA Diamond, and Grok 4. Its durability is **medium**: the general argument about RL-vs-inference economics may remain useful, but the specific slope estimates, benchmark references, and compute numbers are tied to the 2025 frontier-model landscape and could age quickly. The content type is **mixed**: part data-driven commentary, part forecasting, part strategic interpretation. Originality is best described as **commentary/synthesis** rather than primary research; Ord is assembling public evidence into a strong thesis, not presenting new experimental results. As a reference, this is more **deep-study** than skim-once if you care about AI scaling debates, governance, or timelines. Scrape quality is **partial**: the text of the article and thread comments are present, but the cited charts/figures are not directly inspectable here, so some of the empirical support is only described rather than visible.
