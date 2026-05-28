---
url: https://mitchellh.com/writing/building-block-economy
title: The Building Block Economy – Mitchell Hashimoto
scraped_at: '2026-04-19T08:04:11Z'
word_count: 1213
raw_file: raw/2026-04-19_the-building-block-economy-mitchell-hashimoto_a8fee151.txt
tldr: Mitchell Hashimoto argues that software adoption is increasingly driven by “building blocks” — high-quality components and libraries that AI and humans can assemble into many downstream apps — which lowers the bar for shipping, expands ecosystems, and shifts mainline products toward being stable, purposeful cores with outsourced R&D around them.
key_quote: “the shift has already happened. We’re living in it.”
durability: medium
content_type: opinion
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mitchell Hashimoto
tools:
- Ghostty
- libghostty
- Next.js
- Tailwind
libraries: []
companies: []
tags:
- software-ecosystems
- ai-agents
- open-source
- product-strategy
- modular-software
---

### TL;DR
Mitchell Hashimoto argues that software adoption is increasingly driven by “building blocks” — high-quality components and libraries that AI and humans can assemble into many downstream apps — which lowers the bar for shipping, expands ecosystems, and shifts mainline products toward being stable, purposeful cores with outsourced R&D around them.

### Key Quote
“the shift has already happened. We’re living in it.”

### Summary
- **Core thesis:** The most effective path to broad software adoption is shifting from polished “mainline apps” to **building blocks** that others can combine, fork, and customize.
- **Concrete examples from the author:**
  - **Ghostty in 18 months:** “one million daily macOS update checks.”
  - **libghostty in 2 months:** “multiple millions of daily users.”
  - Other examples mentioned: **Pi Mono, Next.js, Tailwind**.
- **Why the author says this is happening now:**
  - The “factory of today is **agentic**” — i.e. AI agents can rapidly assemble software from existing components.
  - AI is especially good at **gluing together high-quality, well-documented, proven components**, even if it is only okay at building everything from scratch.
  - Humans have always preferred reusable primitives, but the barrier to understanding and assembling them has now dropped significantly.
- **Positive effects of the building-block economy:**
  - **Lower quality bar for downstream artifacts:** small audience tools can ship faster and with looser constraints than a mass-market app.
  - **Greater awareness of niche use cases:** specialized communities can find and adopt building blocks that fit them.
  - **Lower maintenance burden for maintainers:** easier to say no to feature requests because the project is part of the means of production.
  - **R&D gets outsourced:** maintainers can observe experiments and cherry-pick proven ideas back into mainline software.
- **Negative effects acknowledged:**
  - Security vulnerabilities
  - Instability
  - Reduced understanding of how “load-bearing systems” actually work
- **Impact on mainline software:**
  - Mainline apps are not disappearing.
  - Instead, they may become **more stable, more purposeful, and more focused** because:
    - a larger and more diverse user base stabilizes the core
    - ecosystem experimentation supplies ideas and proofs of concept
  - The author expects many users will still prefer polished, well-supported applications rather than personalized “slop software.”
- **Commercialization concern:**
  - The author says **closed-source/commercial software appears disadvantaged** because agents tend to prefer **open and free software** over commercial alternatives.
  - He cites this as an “objective truth” at the time of writing, based on experiments from independent research labs.
  - He explicitly avoids making strong claims about the commercial future because he says he is not currently building a commercializable product and doesn’t want to overstate certainty.
- **Author’s stance:**
  - This is a personal reflection, written **by hand without AI assistance**.
  - The tone is confident about the shift itself, cautious about commercialization, and pragmatic rather than ideological.
- **Bottom line:** The article says the software world has already moved into an era where **modular, reusable building blocks** — often amplified by AI agents — are the primary drivers of adoption, experimentation, and ecosystem growth.

### Assessment
This is a **mixed** opinion/essay with some factual examples and trend claims rather than a technical tutorial. Durability is **medium**: the broad idea of modular ecosystems and reuse is likely lasting, but the discussion is tied to the current AI-agent wave and specific products like Ghostty, so parts may age quickly. Density is **medium-high** because it packs several concrete examples and claims into a relatively short essay. Originality is **primary source** commentary: it’s Mitchell Hashimoto’s own viewpoint and experience, not an aggregation. Best used as **refer-back** material for remembering the author’s framing of “building blocks” and the implications for software/product strategy. Scrape quality is **good** overall: the main text and footnotes are present, though any formatting nuances from the original page may be simplified.
