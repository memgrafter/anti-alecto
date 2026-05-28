---
url: https://x.com/mitchellh/status/2041566958681014418
title: 'Mitchell Hashimoto on X: "The Building Block Economy" / X'
scraped_at: '2026-04-19T07:30:11Z'
word_count: 1073
raw_file: raw/2026-04-19_mitchell-hashimoto-on-x-the-building-block-economy-x_ffb55855.txt
tldr: Mitchell Hashimoto argues that software is shifting from “mainline apps” to “building blocks” optimized for AI-assisted assembly, where open, well-documented components attract massive reuse, reduce maintainer burden, and reshape product strategy.
key_quote: “The factory of today is agentic.”
durability: medium
content_type: opinion
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Mitchell Hashimoto
tools:
- Ghostty
- libghostty
- Next.js
- Tailwind
- Pi Mono
libraries:
- libghostty
companies: []
tags:
- software-development
- artificial-intelligence
- open-source
- product-strategy
- modularity
---

### TL;DR
Mitchell Hashimoto argues that software is shifting from “mainline apps” to “building blocks” optimized for AI-assisted assembly, where open, well-documented components attract massive reuse, reduce maintainer burden, and reshape product strategy.

### Key Quote
“The factory of today is agentic.”

### Summary
- This X thread claims the dominant way to build software has changed: instead of focusing on one polished, all-purpose application, the winning pattern is to create **building blocks** that others can assemble into many products, forks, and integrations.
- Hashimoto uses **Ghostty** and **libghostty** as examples:
  - Ghostty reportedly reached **one million daily macOS update checks in 18 months**.
  - **libghostty** reached **multiple millions of daily users in 2 months**.
  - He notes Ghostty’s GUI app now has **more forks than ever before**, often with custom patches.
- He compares this pattern to other “building block” technologies such as **Pi Mono, Next.js, and Tailwind**.
- Central thesis: the “factory” of software creation is now **agentic**—AI is especially good at **gluing together proven, well-documented components** rather than inventing from scratch.
- He says the biggest change is not that humans stopped composing software from primitives, but that the **barrier to understanding and assembling components has dropped**, dramatically increasing the amount of software produced.
- He acknowledges downsides, especially:
  - **Security vulnerabilities**
  - **Instability**
  - **Shallow understanding of load-bearing systems**
- He then lays out the benefits of the building-block model:
  - **Lower quality bar for artifacts** aimed at small audiences, allowing faster shipping
  - **Greater awareness** because niche users discover the building block through usage
  - **Lower maintenance burden** because maintainers can more easily reject feature requests
  - **Outsourced R&D**, where others experiment and mainline projects can later cherry-pick the best ideas
- His own perspective has shifted toward intentionally creating **building blocks** and encouraging **forks/applications on top**, which he believes leads to:
  - a **happier community**
  - a **larger community**
  - **better mainline software**
- He argues that **mainline applications are not disappearing**; rather, they become:
  - more **stable** because they serve a larger and more diverse user base
  - more **purposeful** because their features are shaped by ecosystem experimentation
- On commercialization, he says **closed-source, commercial software is at a major disadvantage** in an agentic ecosystem, because AI systems tend to prefer **open and free software** over commercial alternatives.
- He explicitly avoids overclaiming here, saying he does **not** have a concrete answer for commercialization yet and is not speaking from direct experience with a commercializable product.
- The thread ends with the assertion that this shift has **already happened** and we are already living in it.
- Footnote context:
  - The Ghostty usage numbers are approximate because Ghostty does not have real user tracking; the macOS figure comes from aggregate update checks.
  - The post was **written by hand, without AI assistance**.

### Assessment
This is a high-level **opinion/commentary** thread with some anecdotal evidence and a few concrete usage numbers, so its **durability is medium**: the broad pattern about software modularity and AI-assisted composition may remain relevant, but the commercialization claims are tied to today’s AI ecosystem and may age quickly. It is **mixed** content—part essay, part product reflection, part industry prediction—and relatively **dense** with specific examples and claims. The originality is best described as **primary-source commentary** from a practitioner speaking from firsthand experience with Ghostty/libghostty, though it also synthesizes broader observations about software ecosystems and AI. It’s best used as **refer-back** material if you want the author’s framing of the “building block economy,” not as a neutral technical reference. **Scrape quality is partial**: the thread text is present, but some quoted/link-like fragments are missing or blank in the capture, and the footnotes suggest context that may not fully render here.
