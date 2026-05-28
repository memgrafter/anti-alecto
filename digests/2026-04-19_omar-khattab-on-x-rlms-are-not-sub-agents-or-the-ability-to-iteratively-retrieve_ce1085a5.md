---
url: https://x.com/lateinteraction/status/2022725370152190215
title: 'Omar Khattab on X: "RLMs are not sub-agents or the ability to iteratively retrieve context. I know because I trained multi-hop models for reasoning &amp; retrieval in 2020, including compaction.* RLMs are the simplest/purest scaffold that understands its own prompts via recursion, not via attention." / X'
scraped_at: '2026-04-19T08:08:47Z'
word_count: 270
raw_file: raw/2026-04-19_omar-khattab-on-x-rlms-are-not-sub-agents-or-the-ability-to-iteratively-retrieve_ce1085a5.txt
tldr: Omar Khattab argues that “RLMs” are fundamentally about recursive self-access to a model’s own conversation/horizon via code and repeated LLM launches, not about ordinary sub-agents or iterative context retrieval.
key_quote: “RLMs are the simplest/purest scaffold that understands its own prompts via recursion, not via attention.”
durability: high
content_type: opinion
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Omar Khattab
tools:
- X
libraries: []
companies: []
tags:
- recursive-reasoning
- retrieval-augmented-generation
- multi-hop-reasoning
- llm-agents
- context-management
---

### TL;DR
Omar Khattab argues that “RLMs” are fundamentally about recursive self-access to a model’s own conversation/horizon via code and repeated LLM launches, not about ordinary sub-agents or iterative context retrieval.

### Key Quote
“RLMs are the simplest/purest scaffold that understands its own prompts via recursion, not via attention.”

### Summary
- The post draws a sharp distinction between **RLMs** and **sub-agent/tool-call workflows**.
- Khattab says RLMs are **not** merely:
  - sub-agents,
  - iterative retrieval of context,
  - or standard tool-using systems that delegate sub-tasks.
- His core claim: a model should be able to **symbolically and recursively access its own conversation with the user and its own horizon**.
- He argues the model should only understand long context by **writing code that launches LLMs**, then composing those outputs into the final answer.
- He emphasizes that the number of LLM launches may be **linear or even superlinear in context size**, rather than just a small fixed number of sub-tasks.
- He notes that this is not as strange as it sounds because **attention is already quadratic** in context length.
- He says he finds the usual “sub-agents” framing **boring** and conceptually different:
  - sub-agents = prompt-based tool calls for delegation,
  - RLMs = recursion over the model’s own context and horizon.
- The post includes a footnote referencing his earlier work:
  - **“Robust Multi-Hop Reasoning at Scale via Condensed Retrieval”**
  - arXived **Jan 2, 2021**
  - described as a system that could do many reasoning steps, retrieve from a large corpus, compact/condense context, and iterate further.

### Assessment
This is a **high-durability** conceptual/opinion post with strong technical framing, though it is also clearly a **commentary** rather than a full technical explanation. The density is **medium-high**: it contains specific distinctions, a historical reference to a 2021 paper, and an explicit definition of what the author thinks RLMs are and are not. It appears to be **original commentary** from Omar Khattab, not a synthesis. It is best used as a **refer-back** reference for understanding the author’s terminology and stance. **Scrape quality is partial**: the text of the post is captured, but the broader thread context, replies, and any embedded media are not included.
