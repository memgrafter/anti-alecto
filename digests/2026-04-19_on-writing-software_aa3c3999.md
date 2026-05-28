---
url: https://memgrafter.github.io/blog/2026/03/02/on-writing-software.html
title: On Writing Software
scraped_at: '2026-04-19T08:15:44Z'
word_count: 602
raw_file: raw/2026-04-19_on-writing-software_aa3c3999.txt
tldr: A personal essay on how the author’s software-writing workflow evolved from hand-coding with LLM help to mostly LLM-authored code, centered on Aider, Claude Code, and Pi, with a skeptical take on “innovative” tool ecosystems.
key_quote: Study the payout schedule carefully.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Aider
- Claude Code
- Pi
- flatagents+flatmachines
- AiderX Handlers
libraries: []
companies: []
tags:
- llm-coding
- ai-agents
- developer-tools
- software-workflow
- tool-use
---

### TL;DR
A personal essay on how the author’s software-writing workflow evolved from hand-coding with LLM help to mostly LLM-authored code, centered on Aider, Claude Code, and Pi, with a skeptical take on “innovative” tool ecosystems.

### Key Quote
“Study the payout schedule carefully.”

### Summary
- The author says writing software has changed dramatically over the past three years, and that they stopped writing 99% of code by hand in April 2025.
- That shift happened because:
  - they left a job that banned machine-generated code, and
  - LLM coding tools became capable enough to handle harder cases.

#### LLM coding progression
- **2023–2024**
  - The author prompted an LLM for a rough “form” of software.
  - They then manually wrote the actual software, using the form to reduce cognitive load.
  - They sometimes fixed the generated form and moved it into a file.
- **April 2025**
  - The author used **Aider**.
  - They manually ran shell `!commands` to give the LLM context.
  - They added whole files, and the LLM could add whole files to context via a repo map.
  - Aider had:
    - write
    - edit
    - whole-file read
    - human-managed bash
  - The author says it wrote **99% of the software** they built.
- **November 2025**
  - The author moved to **claude code**.
  - The model could access the shell directly through “agentic tool use.”
  - It could gather context faster and more precisely than the author.
  - The author dislikes closed ecosystems and left Claude Code.
- **December 2025**
  - The author wrote the first version of **flatagents+flatmachines**.
  - They describe it as spec-driven software for LLMs to code LLM workflows.
  - They frame it as their own agentic orchestrator, promising a separate post.
- **January 2026**
  - The author moved to **pi**.
  - Pi uses the same four tools as Aider, but all are managed by the LLM:
    - bash
    - read
    - write
    - edit
  - Human-run bash `!commands` are still possible, but used much less.
  - The author считает Pi more flexible and ergonomic, and possibly longer-lasting.

#### Main opinions and arguments
- The author thinks **Claude Code did not really innovate** on Aider’s core four tools.
- They are unsure whether Claude’s tool-use training changed tool use fundamentally.
- Their guess:
  - it probably made models more likely to use tools unprompted,
  - but not necessarily better at using tools overall.
- They say **Claude’s models are more reliable** at tool use than other models, except for **gpt-5.3-codex**.
- They view Claude Code CLI as full of attempted innovations, many of which were “mostly useless.”
- They argue that innovation has a cost:
  - time wasted,
  - uncertainty,
  - similarity to gambling in terms of uncertain payoff.
- They extend that skepticism to vibe coding and say to “study the payout schedule carefully.”

#### Speculative / forward-looking point
- The author wonders whether LLMs could use tools better if providers had not copied Claude Code’s approach.
- They mention having built early tools as **AiderX Handlers**, which non-tool-use LLMs could call successfully.
- They suggest an alternative future where:
  - models are **cut-to-fit** for each tool,
  - this could be **32x cheaper**,
  - it would save context window cost,
  - and could be more time-efficient and accessible to train.
- They also note that a **small language model (SLM)** could be instructed in natural language on how to use a tool and trained specifically for it.

### Assessment
This is a **mixed opinion/experience essay** with some tool-history commentary and light speculation about LLM agent design. Durability is **medium**: the general workflow observations about LLM-assisted coding may remain useful, but the specific tool references and version-era claims are tightly tied to **2025–2026** and may age quickly. Density is **medium-high** because it packs several concrete milestones, tool names, and judgments into a short post. Originality is **primary source** since it is the author’s own experience and viewpoint rather than a summary of others. It is best used as a **refer-back** piece if you want to track the author’s evolving workflow or compare LLM coding tools. Scrape quality is **good** for the captured text; it appears to include the full post content provided, with no obvious missing sections, code blocks, or images.
