---
url: https://www.tobyord.com/writing/mostly-inference-scaling
title: https://www.tobyord.com/writing/mostly-inference-scaling
scraped_at: '2026-05-10T04:31:32Z'
word_count: 1653
raw_file: raw/2026-05-10_https-www-tobyord-com-writing-mostly-inference-scaling_43e5a765.txt
tldr: Toby Ord argues that the recent performance gains in Anthropic reasoning models are driven mostly by inference-scaling—letting the model spend far more tokens at answer time—rather than by the RL post-training itself, using Sonnet 3.7 vs. its Sonnet 3.5/“3.6” base model and benchmark trend lines to show the RL-only boost is smaller than the test-time compute boost.
key_quote: “In this case, the total performance boost is 34 percentage points with 82% of this coming from inference-scaling.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Toby Ord
- Anson Ho
- Arden Berg
tools: []
libraries: []
companies:
- Anthropic
- Epoch AI
tags:
- ai-inference
- reinforcement-learning
- benchmark-analysis
- test-time-compute
- ai-economics
---

### TL;DR
Toby Ord argues that the recent performance gains in Anthropic reasoning models are driven mostly by **inference-scaling**—letting the model spend far more tokens at answer time—rather than by the RL post-training itself, using Sonnet 3.7 vs. its Sonnet 3.5/“3.6” base model and benchmark trend lines to show the RL-only boost is smaller than the test-time compute boost.

### Key Quote
“In this case, the total performance boost is 34 percentage points with 82% of this coming from inference-scaling.”

### Summary
- **Article type:** technical/opinion essay analyzing benchmark data from reasoning models.
- **Date:** October 3, 2025.
- **Main thesis:** the apparent gains from RL-trained reasoning models are mostly not from RL improving the model at a fixed compute budget, but from RL enabling the model to use much longer chains of thought at inference time.

- Ord frames modern AI scaling as having shifted from:
  - **pre-training scale**: larger next-token-prediction training runs, which he says has stalled out
  - **post-training RL scale**: using reinforcement learning to improve chain-of-thought reasoning
  - **inference-scaling**: spending more compute every time the model answers a query

- He argues inference-scaling is the more important story because:
  - it increases cost on every deployment
  - major AI companies were already spending a lot on serving/inference
  - unlike training costs, higher per-query costs can’t be offset by volume in the same way

- **Data and setup:**
  - He follows Epoch AI’s Anson Ho and Arden Berg in using **Anthropic’s Sonnet 3.7** as the reasoning model.
  - He assumes the base model is **Anthropic’s October 2024 release of Sonnet 3.5** (which he notes is commonly called **Sonnet 3.6** by the community).
  - He uses the same Epoch AI dataset and looks at three benchmarks:
    - **MATH level 5**
    - **GPQA Diamond**
    - **OTIS Mock AIME**

- **Method:**
  - Plot benchmark performance against number of output tokens.
  - Fit the inference-scaling trend line from the RL-trained model.
  - Compare the base model’s score to that trend line.
  - Treat the gap as the “RL boost” at fixed compute.
  - Treat the additional gains from longer reasoning chains as inference-scaling.

- **Key findings:**
  - **MATH level 5**
    - RL boost: **6 percentage points**
    - inference-scaling boost: **28 percentage points**
    - total gain: **34 points**
    - about **82%** of the gain comes from inference-scaling
    - reasoning chains used can be up to **30x** longer, implying about **30x** more cost per query
  - **GPQA Diamond**
    - RL boost: **9 points**
    - inference-scaling boost: **15 points**
    - about **63%** from inference-scaling
    - requires **more than 10x** compute per answer
  - **OTIS Mock AIME**
    - RL boost: **4 points**
    - inference-scaling boost: **45 points**
    - about **92%** from inference-scaling
    - he notes the near-boundary nature of the scores may make a sigmoid fit more appropriate than a straight line, but the inference-scaling advantage still dominates

- **Interpretation:**
  - The core effect of RL post-training seems to be enabling longer, more useful reasoning traces.
  - The resulting capability gains are therefore often purchased by much higher inference costs.
  - This changes:
    - the business model
    - the risk profile
    - the policy/governance response

- **Caveats and future work:**
  - He says it would be useful to extend the analysis to other companies’ models.
  - He also says an important next step is to compare **different generations of reasoning models** to see how much RL shifts the trend line itself versus simply enabling more inference.
  - He notes this is hard to test with public models because non-RL improvements would inflate the apparent RL boost.

### Assessment
This is a **mixed technical-opinion** essay with a fairly durable core idea: the relationship between training-time improvements and test-time compute costs in reasoning models. The argument is **medium-to-high durability** because it depends on current model generations and specific Anthropic/Epoch data, but the broader inference-scaling framework should remain relevant. It is **high density**: it includes concrete model names, benchmark names, percentage-point deltas, and compute-cost implications. The piece is **original analysis/commentary** rather than a pure primary-source release, though it relies on public benchmark data. For later use, it is best as a **refer-back** item if you want the specific claim that most observed gains in these reasoning models come from inference-scaling rather than RL-at-fixed-compute. **Scrape quality is partial**: the article text is present, but the embedded charts are missing, and the page includes obvious site-template artifacts (“Contact Us” form text, placeholder address/phone/email), so the capture is not a clean page scrape.
