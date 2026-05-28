---
url: https://arxiv.org/abs/2601.20404
title: '[2601.20404] On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents'
scraped_at: '2026-04-19T07:05:25Z'
word_count: 401
raw_file: raw/2026-04-19_2601-20404-on-the-impact-of-agents-md-files-on-the-efficiency-of-ai-coding-agent_84a81906.txt
tldr: This arXiv paper reports that adding an `AGENTS.md` file to GitHub repositories makes AI coding agents run faster and use fewer output tokens, based on experiments across 10 repositories and 124 pull requests.
key_quote: the presence of AGENTS.md is associated with a lower median runtime (Δ 28.64%) and reduced output token consumption (Δ 16.58%), while maintaining a comparable task completion behavior.
durability: high
content_type: fact
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Jai Lulla
tools:
- Codex
- Claude Code
- AGENTS.md
companies:
- GitHub
tags:
- ai-coding-agents
- software-engineering
- repository-instructions
- token-usage
- agent-efficiency
---

### TL;DR
This arXiv paper reports that adding an `AGENTS.md` file to GitHub repositories makes AI coding agents run faster and use fewer output tokens, based on experiments across 10 repositories and 124 pull requests.

### Key Quote
“the presence of AGENTS.md is associated with a lower median runtime (Δ 28.64%) and reduced output token consumption (Δ 16.58%), while maintaining a comparable task completion behavior.”

### Summary
- **What the paper studies**
  - The impact of repository-level configuration files, specifically `AGENTS.md`, on the efficiency of AI coding agents.
  - Focuses on agents like **Codex** and **Claude Code** operating on **GitHub pull requests**.

- **Research question**
  - Whether having an `AGENTS.md` file changes:
    - **Wall-clock execution time**
    - **Token usage**
    - **Task completion behavior**

- **Method**
  - Analyzed **10 repositories** and **124 pull requests**.
  - Ran agents under **two conditions**:
    - **With** an `AGENTS.md` file
    - **Without** an `AGENTS.md` file
  - Measured:
    - Runtime
    - Output token consumption

- **Main findings**
  - `AGENTS.md` presence was associated with:
    - **28.64% lower median runtime**
    - **16.58% lower output token consumption**
  - Task completion behavior was **comparable** between the two conditions, suggesting the speed/token gains did not come at an obvious cost in success behavior.

- **Implications**
  - Suggests that repository-level instructions can materially improve how efficiently AI coding agents operate in practice.
  - The authors argue this has immediate relevance for:
    - Configuring AI agents
    - Deploying them in software workflows
  - They also propose a broader research agenda on how repo-level instructions shape agent behavior, efficiency, and integration into development.

- **Metadata / freshness**
  - Submitted **28 Jan 2026**, revised **30 Mar 2026**.
  - The paper is likely relevant to current AI coding-agent tooling, especially as `AGENTS.md` conventions evolve.

### Assessment
This is a **research** paper with **high** durability for the general idea that repository instructions can improve agent efficiency, though the exact numbers and agent/tooling context are tied to the 2026 state of Codex/Claude Code and may age as tools evolve. The content is **dense**, **primary source**, and best used as a **refer-back** reference rather than a one-time skim, since it reports a concrete experiment with clear quantitative results. Scrape quality is **good**: the abstract, submission history, and key metadata are present, but the full paper text, methods details, and any figures/tables are not included here.
