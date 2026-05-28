---
url: https://x.com/HamelHusain/status/2033920254938886331
title: 'Hamel Husain on X: "One thing that makes me feel that code factory has not arrived yet is the following experiment: 1.Ask a LLM to do an in-depth rigorous review of your code 2. In a new thread, as same/different LLM to consider those review comments independently and address issues it agrees with" / X'
scraped_at: '2026-04-19T07:02:01Z'
word_count: 234
raw_file: raw/2026-04-19_hamel-husain-on-x-one-thing-that-makes-me-feel-that-code-factory-has-not-arrived_6aa5abb2.txt
tldr: Hamel Husain argues that “code factory” is not here yet because repeated LLM code reviews in separate threads keep finding new issues for a long time, suggesting autonomous “claude-take-the-wheel” coding is still unreliable.
key_quote: Keep repeating until no new concerns
durability: high
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: partial
people:
- Hamel Husain
tools: []
libraries: []
companies: []
tags:
- llm-coding
- code-review
- ai-agents
- software-development
- machine-learning
---

### TL;DR
Hamel Husain argues that “code factory” is not here yet because repeated LLM code reviews in separate threads keep finding new issues for a long time, suggesting autonomous “claude-take-the-wheel” coding is still unreliable.

### Key Quote
“Keep repeating until no new concerns”

### Summary
- **Main claim:** Hamel Husain says a simple experiment exposes a limitation in current LLM coding autonomy:
  1. Ask a LLM for an in-depth, rigorous review of your code.
  2. In a new thread, ask the same or another LLM to independently evaluate those review comments and fix the issues it agrees with.
  3. Repeat until no new concerns remain.
- **Observed result:** He says this loop “always goes on for a ridiculously long time,” implying LLM-generated code and reviews keep surfacing additional problems rather than converging quickly.
- **Interpretation:** This makes him doubt that fully autonomous “code factory” workflows are ready, especially the idea of “claude-take-the-wheel.”
- **Scope of the criticism:** He says this happens regardless of:
  - the harness used
  - how specific the specs are
- **Nuance:** He adds that LLMs work fine for “simple applications,” but at the limit their “cognitive dissonance” makes them hard to trust.
- **Alternative explanation offered:** He suggests either:
  - the autonomy idea is not ready, or
  - LLMs are RLHF’d to always find some kind of issue.
- **Context:** This is a short opinionated X post, not a detailed technical experiment writeup. It includes engagement metrics and a link to 69 replies, but the scraped content does not include the replies themselves.

### Assessment
This is a **high-durability opinion/commentary** piece with a **mixed** content type: it presents a practical test, an observed pattern, and an interpretation about LLM reliability. The post is **medium-density**—concise but specific enough to preserve the core argument and the proposed experiment. It is **original commentary** rather than a synthesis of external sources. Best used as a **skim-once** reference unless you’re tracking debates about autonomous coding agents, in which case it’s worth a **refer-back**. **Scrape quality is partial**: the main post text and metadata are captured, but the replies and any surrounding discussion are missing.
