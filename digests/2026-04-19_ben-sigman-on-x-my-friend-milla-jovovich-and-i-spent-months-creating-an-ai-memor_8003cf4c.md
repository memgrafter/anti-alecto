---
url: https://x.com/bensig/status/2041236952998171118?s=20
title: 'Ben Sigman on X: "My friend Milla Jovovich and I spent months creating an AI memory system with Claude. It just posted a perfect score on the standard benchmark - beating every product in the space, free or paid. It''s called MemPalace, and it works nothing like anything else out there. Instead https://t.co/trAUZyMHIe" / X'
scraped_at: '2026-04-19T07:20:45Z'
word_count: 319
raw_file: raw/2026-04-19_ben-sigman-on-x-my-friend-milla-jovovich-and-i-spent-months-creating-an-ai-memor_8003cf4c.txt
tldr: Ben Sigman is promoting MemPalace, a local-first open-source AI memory system built with Claude that claims perfect benchmark scores and uses a “palace” structure to organize personal context, but X’s community notes says some of the headline scores rely on reranking and targeted fixes.
key_quote: “Your memories never leave.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: skim-once
scrape_quality: partial
people:
- Ben Sigman
- Milla Jovovich
tools:
- Claude
libraries: []
companies: []
tags:
- ai-memory
- benchmark-claims
- local-first
- open-source
- personal-context
---

### TL;DR
Ben Sigman is promoting MemPalace, a local-first open-source AI memory system built with Claude that claims perfect benchmark scores and uses a “palace” structure to organize personal context, but X’s community notes says some of the headline scores rely on reranking and targeted fixes.

### Key Quote
“Your memories never leave.”

### Summary
- This is a promotional X post for **MemPalace**, described as an **AI memory system** created by Ben Sigman and Milla Jovovich using **Claude**.
- Core product claim: unlike cloud-based background agents, MemPalace **runs locally on the user’s machine** and “mines” conversations to build a structured memory model.
- The system organizes memory as a **“palace”** with:
  - **wings**
  - **halls**
  - **rooms**
  - The post says this structure mirrors how human memory works.
- Claimed user-facing benefits:
  - AI knows the user’s context before they type
  - Context for family/projects/preferences fits into about **120 tokens**
  - Semantic search across months of conversations finds answers quickly
  - **AAAK compression** is said to provide **30x lossless compression**
  - Contradiction detection flags wrong names, pronouns, and ages
- Benchmark claims in the post:
  - **100% recall on LongMemEval** — “first perfect score ever recorded,” **500/500 questions**
  - **92.9% on ConvoMem**, claimed to be more than **2x Mem0**
  - **100% on LoCoMo**, including temporal inference
- Distribution/licensing claims:
  - **No API key**
  - **No cloud**
  - **No subscription**
  - **One dependency**
  - **Runs locally**
  - **MIT License**
  - **100% Open Source**
  - GitHub: **github.com/milla-jovovich**
- A **community note** adds important caveats:
  - The claimed **100% LongMemEval** score used **targeted fixes for the 3 failing questions** and **LLM reranking**
  - Held-out score is stated as **98.4%**
  - The claimed **100% LoCoMo** score used **top-k=50** exceeding session count with reranking
  - “Honest top-10 no rerank” score is given as **88.9%**
- So the post is both a **product announcement** and a **benchmark-heavy marketing claim**, with some correction/context supplied by X users.

### Assessment
Durability is **medium**: the general idea of local-first personal AI memory and conversation retrieval is likely to stay relevant, but the specific benchmark numbers, model behavior, and product claims are tied to a particular release and may age quickly. Content type is **mixed** — mostly announcement/promotional, with technical claims and benchmark assertions. Density is **medium-high** because it packs in product features, architecture terms, benchmark scores, and licensing/distribution details into a short post. Originality is **primary source** for the author’s claims, though the community note introduces independent correction/context. Reference style is **skim-once** for most readers, or **refer-back** if tracking AI memory products/benchmarks. Scrape quality is **partial**: the main post text and community note were captured, but the linked image and any deeper thread replies are not included.
