---
url: https://memgrafter.github.io/blog/2026/02/08/llm-coding-research-loop.html
title: 'Autocatalysis: LLM Research Digestion Loop'
scraped_at: '2026-04-12T07:43:37Z'
word_count: 513
raw_file: raw/2026-04-12_autocatalysis-llm-research-digestion-loop_8f6b607d.txt
tldr: A personal note on using LLMs and agentic workflows to digest the flood of recent ML papers, build a “coding assistant” term cloud, and recursively improve research questions—while arguing that the process is expensive, only partly validated, and better described as “autocatalysis” than a flywheel.
key_quote: 'Spolier alert: it’s too expensive and doesn’t work'
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- gpt-5.3-codex
- pi
- Speech Central
libraries: []
companies: []
tags:
- llm-research
- agentic-workflows
- research-evaluation
- machine-learning
- knowledge-management
---

### TL;DR
A personal note on using LLMs and agentic workflows to digest the flood of recent ML papers, build a “coding assistant” term cloud, and recursively improve research questions—while arguing that the process is expensive, only partly validated, and better described as “autocatalysis” than a flywheel.

### Key Quote
“Spolier alert: it’s too expensive and doesn’t work”

### Summary
- The post frames the problem as information overload in ML research: around **120 machine-learning-adjacent arXiv papers per day**, which the author says “only a machine can get through.”
- It introduces **autocatalysis** as the metaphor:
  - In chemistry, an autocatalytic reaction is one where a product also catalyzes the same reaction.
  - The author extends the idea to a **research digestion loop**: outputs from one pass of analysis help generate better inputs for the next pass, making the system partially self-sustaining.
- The author’s research workflow is described as a loop:
  - **Process papers** through agentic workflows and a research discovery pipeline, storing papers in an analysis repo.
  - **Ask questions** using **gpt-5.3-codex** in a “pi coding agent” to orient to the landscape.
  - **Listen and learn** by pasting digests or detailed analysis into **Speech Central** for deeper understanding.
  - **Rinse and repeat**: use improved understanding to ask better questions, reimplement agent workflows, and keep feeding the loop.
- A concrete use case is building a **term cloud** around **“coding assistant”**:
  - The author is feeding terms back into the corpus to identify the **top X papers for LLM coding (from 2025 onward)**.
  - The expectation is that the corpus and term cloud will improve search and retrieval results over time.
- The post includes a section on **judge agents** and what the author has learned:
  - **Scoring is unreliable** on its own; it only helps when compared against other outputs.
  - Very low scores can still be useful as a signal for **layout or format nonconformance**, not for factual quality.
  - **Weaker models can be good judges or routers**.
  - **Nonconforming output should be discarded**, not usually repaired, because format failures often indicate deeper problems.
- The author says they have **not yet directly analyzed judge capabilities with the coding agent**, so this is a planned next step.
- A small but notable observation: even without fully developed multi-agent workflows, the author was surprised that **codex-5.3(high) in pi** generated a **PNG file**, which they call “unplanned capabilities.”
- The post also comments on naming:
  - The author originally wanted to call the post **“LLM Research Flywheel”** but rejected that analogy.
  - They argue a flywheel is a misleading metaphor because it only stores/recycles energy you already put in; it does not inherently accelerate progress.
  - They prefer the **autocatalysis** framing because it better captures the self-reinforcing nature of the workflow.
- Tone-wise, this is a **personal, reflective, experimental note** rather than a polished technical report or tutorial.
- The post points readers to **LM Council documents** for a more detailed analysis of similar topics.

### Assessment
This is a **mixed** personal/technical commentary with medium-to-high durability: the specific tools, model names, and “2026/02/08” context make it somewhat time-bound, but the underlying ideas about research digestion loops, agent workflows, and judge reliability are broadly reusable. It is **medium-density** and reads like an exploratory field note rather than a formal tutorial or research paper. The piece appears to be **primary-source commentary** from the author’s own experiments and opinions, not a synthesis of external work. It’s best used as **refer-back** material if you’re interested in agentic research workflows, evaluation/judge agents, or the autocatalysis metaphor. **Scrape quality is good** for the text shown: the main sections and quoted snippets are present, though any embedded images or linked documents (like the “lm council documents” or the referenced PNG) are not included here.
