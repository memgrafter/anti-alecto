---
url: https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/
title: https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/
scraped_at: '2026-04-19T21:16:24Z'
word_count: 925
raw_file: raw/2026-04-19_https-martinalderson-com-posts-no-it-doesnt-cost-anthropic-5k-per-claude-code-us_a31c3c4b.txt
tldr: Anthropic’s “$5,000 per Claude Code user” figure is likely an API-pricing artifact, not its real inference cost, and average Claude Code users may be profitable or near break-even.
key_quote: No, it doesn't cost Anthropic $5k per Claude Code user
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Martin Alderson
- Anthropic
- Cursor
- OpenAI
- Forbes
tools:
- Claude Code
- OpenRouter
- DeepInfra
libraries: []
companies:
- Anthropic
- Cursor
- OpenRouter
- DeepInfra
- Alibaba Cloud
tags:
- ai-economics
- inference-costs
- api-pricing
- claude-code
- model-pricing
---

### TL;DR
Martin Alderson argues that Forbes’ “$5,000 per Claude Code user” figure is an API-pricing artifact, not Anthropic’s real inference cost, and that Anthropic is likely far more profitable on average Claude Code users than the headline suggests.

### Key Quote
“No, it doesn't cost Anthropic $5k per Claude Code user”

### Summary
- **Main thesis:** The widely shared claim that Anthropic loses about $5,000/month on a heavy Claude Code Max user confuses **retail API pricing** with **actual compute cost**.
- **Core distinction:**  
  - Anthropic’s API prices for **Opus 4.6** are cited as **$5/M input tokens** and **$25/M output tokens**.  
  - Those prices can make a heavy user look like they consume **$5,000/month worth of tokens**, but that is **not** the same as what Anthropic pays to serve them.
- **Comparison used to estimate actual cost:**  
  - The author points to **OpenRouter** pricing for large open-weight models as a proxy for serving costs.
  - Examples given:
    - **Qwen 3.5 397B-A17B**: **$0.39/M input**, **$2.34/M output**
    - **Kimi K2.5**: **$0.45/M input**, **$2.25/M output**
    - Cached-token comparison: **DeepInfra** charges **$0.07/M** cache reads for Kimi K2.5 vs Anthropic’s **$0.50/M**
  - The conclusion is that similar-scale models appear to be served at roughly **10x cheaper** prices than Anthropic’s API rates.
- **Implication for Anthropic’s cost basis:**  
  - If a heavy user looks like **$5,000/month** at API prices, the implied actual compute cost might be about **$500/month**.
  - That would mean the loss on the most extreme power users is closer to **$300/month** on a $200 plan, not **$4,800/month**.
- **Average users matter more than extremes:**  
  - The author notes Anthropic said **fewer than 5%** of subscribers were affected by weekly caps.
  - They also say their own Max 20x usage is about **50%** of the weekly token budget.
  - Their estimate: average usage may be **break-even or profitable** for Anthropic.
- **Who the $5,000 figure actually applies to:**  
  - The author argues the number is probably accurate for **Cursor**, because Cursor must pay Anthropic’s API-level prices (or close to them) to offer model access.
  - So the real economic strain is on **Cursor’s margins**, not Anthropic’s direct inference economics.
- **Broader argument:**  
  - Anthropic is still not necessarily profitable overall because training frontier models, researcher salaries, and compute commitments are enormous.
  - But the author argues **inference itself is not the main money sink**.
  - They call the “AI inference is a money pit” narrative misleading because it may help frontier labs justify large API markups and discourage competition.
- **Supporting note in footnotes:**  
  - A HN user example of **150M–200M tokens/day** is back-of-the-envelope converted to **$400–$600/day** in API-equivalent cost, aligning with the $5,000/month estimate.
  - Anthropic’s own `/cost` data is cited as showing the average Claude Code developer uses about **$6/day** in API-equivalent spend, with **90% under $12/day**, which the author says would translate to about **$18/month** in actual compute cost against a **$20–$200** subscription.

### Assessment
This is a **mixed opinion/analysis post** with a fairly high-density argument built from pricing comparisons and rough back-of-the-envelope math. Its **durability is medium**: the core conceptual distinction between API price and actual serving cost is lasting, but the specific model names, prices, and product tiers are tied to a particular moment in Anthropic/OpenRouter pricing. The piece is **commentary/synthesis**, not primary source research, though it does cite figures from Forbes, Anthropic, OpenRouter, DeepInfra, and Anthropic’s `/cost` command. It’s best used as a **refer-back** item if you want the argument and the pricing logic; the scrape quality is **good**, with the full text and footnotes present.
