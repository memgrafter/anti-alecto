---
url: https://news.ycombinator.com/item?id=38725953
title: When I open a large pdf on arxiv (100+ MB, not uncommon for ML papers focused on... | Hacker News
scraped_at: '2026-04-12T07:36:19Z'
word_count: 316
raw_file: raw/2026-04-12_when-i-open-a-large-pdf-on-arxiv-100-mb-not-uncommon-for-ml-papers-focused-on-ha_9d36001a.txt
tldr: A Hacker News thread explains why large arXiv PDFs can take 10+ seconds to show anything, with replies attributing the delay to PDF file structure, network/server slowness, and possibly PDF generation/caching on arXiv’s side.
key_quote: PDF-1.2 onwards supports linearized PDFs, and most PDF export tools have some way of enabling it (usually an option like "optimize for web").
durability: medium
content_type: mixed
density: medium
originality: synthesis
reference_style: skim-once
scrape_quality: partial
people: []
tools:
- Chrome
libraries: []
companies:
- arXiv
tags:
- pdf-rendering
- arxiv
- web-performance
- document-format
- machine-learning
---

### TL;DR
A Hacker News thread explains why large arXiv PDFs can take 10+ seconds to show anything, with replies attributing the delay to PDF file structure, network/server slowness, and possibly PDF generation/caching on arXiv’s side.

### Key Quote
“PDF-1.2 onwards supports linearized PDFs, and most PDF export tools have some way of enabling it (usually an option like "optimize for web").”

### Summary
- The original poster complains that opening very large arXiv PDFs, especially 100+ MB machine-learning papers, can take 10+ seconds before any content renders.
- They ask whether the delay is due to:
  - network transfer,
  - Chrome’s PDF rendering speed,
  - or a need for PDFs to be fully downloaded before rendering.
- They suggest that progressively rendered HTML would be a big improvement over the current experience.

- One reply explains a likely technical cause:
  - Standard PDFs often place the cross-reference table at the end of the file.
  - That means a viewer may need the full file before it can properly begin rendering.
  - PDF-1.2 and later support “linearized” PDFs, which are designed for faster web viewing.
  - Many PDF export tools have an “optimize for web” option to enable this.

- Other replies speculate that the bottleneck may be arXiv itself rather than the PDF format:
  - One person says the issue seems network-bound and that arXiv servers may be slow.
  - They mention arXiv theoretically supports caching servers, but they had trouble getting such a setup working.

- Another comment suggests the delay could include PDF generation time:
  - arXiv submissions are originally in LaTeX.
  - PDFs are automatically generated from the source.
  - This raises the possibility that some of the wait comes from conversion rather than serving a ready-made file.

- A final reply notes that arXiv probably caches PDFs so they are not regenerated on every request, but the commenter does not know how that caching works.

### Assessment
This is a short, mixed discussion thread rather than a definitive technical article. Durability is medium: the basic explanation about non-linearized PDFs and web rendering is fairly timeless, but the observations about arXiv performance and caching are tied to a specific service and may change over time. Content type is mixed, combining question, explanation, and speculation. Density is medium: there are only a few comments, but they contain specific technical claims like xref tables, PDF-1.2 linearization, and LaTeX-to-PDF generation. Originality is mostly commentary and crowd-sourced synthesis rather than primary source material. It’s best used as a skim-once or refer-back reference if you want a quick explanation for slow PDF startup behavior. Scrape quality is partial: the thread content appears truncated and there are no visible metadata, full comment context, or any linked technical details beyond the quoted discussion.
