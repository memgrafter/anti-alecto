---
url: https://github.com/humanlayer/12-factor-agents?tab=readme-ov-file
title: 'humanlayer/12-factor-agents: What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?'
scraped_at: '2026-04-19T08:06:41Z'
word_count: 1763
raw_file: raw/2026-04-19_humanlayer-12-factor-agents-what-are-the-principles-we-can-use-to-build-llm-powe_197e504b.txt
tldr: A GitHub README proposing “12-factor agents” as a set of practical design principles for building production-ready LLM applications, arguing that most useful agent systems are mostly deterministic software with LLMs used at specific control points.
key_quote: the fastest way I've seen for builders to get high-quality AI software in the hands of customers is to take small, modular concepts from agent building, and incorporate them into their existing product
durability: high
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Dex
- Dexhorthy
- Ian Butler
- Tnm
- Hellovai
- Stantonk
- Allison
- Pfbyjy
- A-Churchill
tools:
- npx/uvx create-12-factor-agent
libraries:
- crewai
- langchain
- smolagents
- langgraph
- griptape
companies:
- HumanLayer
- Airflow
- Prefect
- Dagster
- Inngest
- Windmill
- Anthropic
- MIT
tags:
- llm-agents
- prompt-engineering
- software-architecture
- production-systems
- context-management
---

### TL;DR
A GitHub README proposing “12-factor agents” as a set of practical design principles for building production-ready LLM applications, arguing that most useful agent systems are mostly deterministic software with LLMs used at specific control points.

### Key Quote
“the fastest way I've seen for builders to get high-quality AI software in the hands of customers is to take small, modular concepts from agent building, and incorporate them into their existing product”

### Summary
- This is a **README / manifesto-style guide** for the project **humanlayer/12-factor-agents**, framed as an analogue to **12 Factor Apps** for AI agents.
- The author, Dex, says he has:
  - worked on AI agents for a while,
  - tried many frameworks (from lightweight to “production grade”),
  - spoken with many technical founders,
  - and found that most customer-facing “agents” in production are not fully agentic, but rather **mostly deterministic software with LLM steps inserted strategically**.
- Main thesis:
  - The common “prompt + tools + loop until done” agent pattern is not enough for production quality.
  - Instead, builders should use **small, modular, software-engineering-friendly principles** to make LLM-powered systems reliable, scalable, and maintainable.
  - The author prefers **incremental integration into existing products** over greenfield framework rewrites.

- The README presents a **12-factor list** of linked essays:
  1. **Natural Language to Tool Calls**
  2. **Own your prompts**
  3. **Own your context window**
  4. **Tools are just structured outputs**
  5. **Unify execution state and business state**
  6. **Launch/Pause/Resume with simple APIs**
  7. **Contact humans with tool calls**
  8. **Own your control flow**
  9. **Compact Errors into Context Window**
  10. **Small, Focused Agents**
  11. **Trigger from anywhere, meet users where they are**
  12. **Make your agent a stateless reducer**
- There is also an **honorable mention / Factor 13**:
  - **Pre-fetch all the context you might need**

- The README includes a short conceptual history:
  - software as directed graphs / flow charts,
  - DAG orchestrators like **Airflow, Prefect, Dagster, Inngest, Windmill**,
  - then the promise of agents as a way to “throw the DAG away” and let an LLM choose the path dynamically.
- It then shows a simple agent loop:
  - LLM decides next step in structured JSON,
  - deterministic code executes the tool,
  - result is appended to the context window,
  - repeat until the model says “done.”
- The author argues this loop often fails to deliver the reliability needed for real customer-facing features, and that many teams get stuck around **70–80% quality** before having to rethink the architecture.
- The README emphasizes that this is **not an anti-framework rant**:
  - it explicitly says the project is not a dig at frameworks or their builders,
  - it acknowledges frameworks have accelerated the AI ecosystem,
  - but argues that **deep control** and **modular adoption** may be better for teams shipping real products.
- The page also includes:
  - links to a talk from the **AI Engineer World’s Fair**,
  - a note that the source is public and contributions are welcome,
  - a list of related resources and references,
  - contributors,
  - and licensing information.

### Assessment
This is a **mixed** content type, mostly **opinion/commentary with reference-like structure**, backed by practical engineering heuristics rather than formal research. Durability is **medium to high**: the specific AI-agent ecosystem and cited frameworks may age quickly, but the underlying principles about control flow, state, prompts, and production reliability are likely to remain useful. Density is **medium**—it’s fairly packed with named factors, examples, and links, though the README itself is more of a roadmap than a deep technical treatise. Originality is **primary source** in the sense that it presents the author’s own framework and perspective, though it also synthesizes ideas from many other sources. Reference style is **refer-back**: best used as an index into the individual factor essays rather than a one-time read. Scrape quality is **good**: the main README structure, links, quoted sections, and license/contributor information are present, though image-heavy visuals and linked subpages are only referenced, not fully captured.
