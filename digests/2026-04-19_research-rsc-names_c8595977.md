---
url: https://research.swtch.com/names
title: 'research!rsc: Names'
scraped_at: '2026-04-19T07:38:03Z'
word_count: 856
raw_file: raw/2026-04-19_research-rsc-names_c8595977.txt
tldr: Russ Cox argues that variable names should be as long as their scope and meaning require, but no longer, because short, precise names can communicate more efficiently than verbose ones.
key_quote: Make every name tell.
durability: high
content_type: opinion
density: medium
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Russ Cox
- Barry Kelly
- Rob Kohr
- David
- Ilyia Kaushansky
- dmolony
- Justin Lilly
- David Andersen
- Kai
- J
tools: []
libraries: []
companies: []
tags:
- programming-style
- naming-conventions
- code-readability
- software-design
- code-review
---

### TL;DR
Russ Cox argues that variable names should be as long as their scope and meaning require, but no longer, because short, precise names can communicate more efficiently than verbose ones.

### Key Quote
“Make every name tell.”

### Summary
- **Topic:** A brief essay on programming-style naming philosophy, posted by Russ Cox on February 4, 2010.
- **Core thesis:** The length of a name should not exceed its information content.
  - For **local variables**, short names like `i` can be as informative as `index` or `idx` and are faster to read.
  - For **paired indices**, `i` and `j` are better than `i1` and `i2` because they are easier to distinguish when scanning code.
  - For **global names**, more information is needed because they appear in more contexts.
- **Main argument:** Long names are not automatically better; they can be inefficient if they contain more words than needed to convey meaning.
- **Important nuance added in comments and author reply:**
  - The amount of descriptive detail should scale with the **scope** in which the variable is used.
  - Once the needed information level is chosen, prefer the **highest-density** name available: the shortest name that is still accurate and readable.
- **Example given by Cox:**
  - `getParametersAsNamedValuePairArray` is criticized as verbose and partly inaccurate.
  - Cox argues that `params()` or `parameters()` would be better, and if more specificity is needed, `queryParams()` adds useful information without unnecessary length.
- **Commentary/discussion themes:**
  - Some commenters object that short names like `j` are unreadable without context.
  - Another commenter argues editor support reduces the cost of longer names.
  - One reply reframes the issue as a balance between brevity and context visibility.
  - Cox responds directly: scope determines needed descriptiveness, and shorter high-density names are preferable when equally clear.

### Assessment
This is a short **opinion** piece with some practical programming guidance. Its **durability is high** because it discusses a timeless software design principle rather than a version-specific technique, though it reflects coding debates common in 2010. The **density is medium**: the article itself is brief, but the comment thread adds a few useful clarifications and examples. It is the author’s **primary source** for this naming philosophy, not a synthesis. This is best used as a **refer-back** reference for style discussions or code review reasoning. **Scrape quality is partial**: the main post and comment thread are present, but the page format is flattened and may not preserve the original site structure or links cleanly.
