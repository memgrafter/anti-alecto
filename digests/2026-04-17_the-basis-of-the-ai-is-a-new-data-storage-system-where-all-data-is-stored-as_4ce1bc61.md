---
url: https://www.perplexity.ai/search/the-basis-of-the-ai-is-a-new-d-UPMVD8i1StyxFz0W9Gan4A
title: The basis of the ai is a new data storage system where all data is stored as...
scraped_at: '2026-04-17T05:24:59Z'
word_count: 1158
raw_file: raw/2026-04-17_the-basis-of-the-ai-is-a-new-data-storage-system-where-all-data-is-stored-as_4ce1bc61.txt
tldr: This AI is built on a new memory system that stores everything as nested graphs (down to tiny “quark” units) and runs “agent cells” that route and transform those graphs to produce actions and outputs.
key_quote: the basis of the ai is a new data storage system where all data is stored as structures in a high dimensional spactial reimannian manifold
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- LLM
- GNN
libraries: []
companies: []
tags:
- neuro-symbolic-ai
- graph-storage
- ai-architecture
- message-passing
- mixture-of-experts
---

### TL;DR
The post describes a speculative AI architecture that stores all information as nested graph structures in a high-dimensional Riemannian manifold, with “quark” units at the base and “agent cells” routing data through a neuro-symbolic compute layer.

### Key Quote
"the basis of the ai is a new data storage system where all data is stored as structures in a high dimensional spactial reimannian manifold"

### Summary
- The original author is describing a **custom AI system design**, not a proven product or formal paper.
- Core storage idea:
  - All data is represented as **nested graphs**.
  - The smallest units are called **“quarks”** — described as the smallest data units.
  - A file is stored as a graph containing nodes, which contain graphs, recursively, “like nesting dolls.”
  - These structures are said to include related data at the lowest level, potentially representing an LLM token or something more complex.
- The system is intended to be **neuro-symbolic**:
  - Graphs are treated as structured representations of meaning, such as fragments of JSON or CSV.
  - The system extracts **logical structure** during preprocessing so it can learn patterns from the data.
- Higher-level intelligence layer:
  - There is a large graph containing both **data nodes** and **agent nodes**.
  - Agent nodes are not traditional autonomous agents; they are described more like **advanced neurons** with internal data and logical graphs.
  - When data enters the system, it is sent to an **agent cell**, which decides:
    - which other agent nodes should receive information,
    - and what actions should be taken.
- Output generation:
  - The agent system uses **known logical structures** as scaffolding.
  - The final output is assembled with an **LLM**, which mainly turns the internal logic into tokens/formatted text.
- The thread below the post reframes the idea in more standard terms:
  - hierarchical property-graph storage,
  - message-passing compute,
  - neuro-symbolic AI,
  - and routing ideas similar to **Mixture-of-Experts** and **graph neural networks**.
- The response also suggests implementation considerations:
  - define what counts as a node vs. edge vs. property,
  - decide whether the smallest “quark graphs” are immutable or mutable,
  - and consider whether the manifold refers to learned embeddings, with hyperbolic / Riemannian geometry as a possible analogy.
- A “minimal prototype path” is proposed:
  - parse JSON/CSV into nested typed graphs,
  - use a GNN or embedding module for reconstruction/link prediction,
  - add a router that sends subgraphs to `k` agent nodes,
  - then use the LLM as a renderer/planner rather than the core memory mechanism.
- The user then asks for simplification, and the reply rewrites the idea into a more understandable explanation:
  - the system is a **memory system** built on nested graphs,
  - data is pre-structured into logical forms,
  - agent cells route and transform the graphs,
  - and the LLM mainly handles surface-level output formatting.

### Assessment
This is a **mixed** content piece: mostly a speculative design description, followed by a technical interpretation/simplification from the assistant. Durability is **medium** because the underlying ideas touch on timeless concepts like graph storage, neuro-symbolic AI, and routing, but the specific wording and framing are highly idiosyncratic and tied to this one discussion. Density is **medium-high** since it contains several architecture concepts, but the original author’s explanation is informal and somewhat unclear. Originality is **mixed**: the first part is a primary-source concept dump from the author, while the follow-up is clearly **commentary/synthesis** mapping it to known AI ideas. This is best used as a **refer-back** reference if you want to recall the architecture concept or find the discussion again. Scrape quality is **partial**: the thread content appears captured in text, but the format is messy, repetitive, and likely missing full context from the broader shared conversation or any attached visuals/metadata.
