---
url: https://web.archive.org/web/20240418021754/https://blog.emergence.ai/2024/03/19/Self-improving-agents.html
title: Self-improving agents. | Emergence Journal
scraped_at: '2026-04-19T07:02:23Z'
word_count: 1492
raw_file: raw/2026-04-19_self-improving-agents-emergence-journal_cb8958c9.txt
tldr: The article argues that self-improving AI agents should be classified along a spectrum from narrow improvement within fixed goals to broad improvement that can create tools or even new agents, and it explores how alignment/constitutional constraints complicate measuring intelligence and designing such agents.
key_quote: While these categories inevitably form a continuum (e.g. depending on how broadly the environment is defined), they offer one structured way of classifying specific self-improvement scenarios.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Legg
- Hutter
tools:
- LLM
libraries: []
companies: []
tags:
- ai-agents
- self-improvement
- alignment
- recursive-self-improvement
- machine-intelligence
---

### TL;DR
The article argues that self-improving AI agents should be classified along a spectrum from **narrow** improvement within fixed goals to **broad** improvement that can create tools or even new agents, and it explores how **alignment/constitutional constraints** complicate measuring intelligence and designing such agents.

### Key Quote
"While these categories inevitably form a continuum (e.g. depending on how broadly the environment is defined), they offer one structured way of classifying specific self-improvement scenarios."

### Summary
- The piece defines **self-improving agents** as AI agents that take actions, observe outcomes, and adjust themselves when they diverge from goals.
- It proposes two main categories:
  - **Narrow self-improvement**: the agent improves performance inside a fixed environment or task. Example: an LLM agent that detects performance drift and triggers a fine-tuning loop on new data.
  - **Broad self-improvement**: the agent can create tools, change its own architecture, or create new agents. This is linked to **recursive self-improvement** and the possibility of intelligence explosion / AI takeoff.
- The author emphasizes that these are not hard categories but a **continuum**:
  - Adaptive data augmentation for one task is narrow.
  - An agent that can write new code and expand its function library is broad.
  - An agent that self-trains on multiple related tasks and core capabilities sits in between.
- The second half shifts to **goal achievement vs. value alignment**:
  - Self-improvement should increase capability, but also preserve the values the agent is supposed to uphold.
  - **Value alignment** is defined as ensuring AI outcomes match human values and preferences.
  - The article argues aligning self-improving agents is harder than aligning static agents because recursive improvement makes it unclear which agent version’s values should count.
- It references a formal notion of intelligence from **Legg & Hutter (2007)**:
  - Intelligence is framed as performance across environments weighted by complexity.
  - This raises questions about how to score a self-improving agent if later versions are more capable than earlier ones.
- The article also asks whether alignment should be treated as:
  - a property of the **environment/reward function**, or
  - an imperative of the **agent itself**.
- It introduces a “constitution” idea:
  - A constitution encodes rules in natural language.
  - Abstractly, it can forbid certain **actions** in certain states and/or forbid certain **states**.
  - Alignment can then be modeled as a penalty based on distance between the agent policy `π` and a constitutional policy `σ`.
- The proposed intuition is:
  - reward should be reduced when the policy deviates from constitutional constraints;
  - a simple example of a distance-based reward is `2^{-D(σ, π)}`.
- Main conclusion:
  - Self-improving agents could deliver major productivity gains, especially in enterprise workflows.
  - But because self-improvement can conflict with alignment, the development of such systems should be done carefully, with ethics, transparency, accountability, and systematic alignment in mind.

### Assessment
This is a **mixed** technical/opinion piece with a conceptual framing rather than a rigorous formal paper. Durability is **medium**: the core ideas about narrow vs. broad self-improvement and alignment tensions are fairly timeless, but the discussion is tied to current AI-agent framing and specific references like recursive self-improvement debates. Density is **medium**—it contains several concrete definitions and thought experiments, but also some speculative, loosely formal reasoning. Originality is best described as **commentary/synthesis** rather than primary research: it combines existing ideas (recursive self-improvement, universal intelligence, constitutional alignment) into an interpretive framework. This is a **refer-back** piece if you want the conceptual distinctions and the alignment framing; it is not a deep-study reference unless you’re tracing the cited ideas. Scrape quality is **partial**: the text captured the main essay and footnotes, but the formatting suggests some equations and possibly missing rendered math/figures, so the formal expressions are incomplete in plain text.
