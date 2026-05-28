---
url: https://x.com/kevingu/status/2039843234760073341
title: 'Kevin Gu on X: "AutoAgent: first open source library for self-optimizing agents" / X'
scraped_at: '2026-04-19T07:57:23Z'
word_count: 852
raw_file: raw/2026-04-19_kevin-gu-on-x-autoagent-first-open-source-library-for-self-optimizing-agents-x_ba23cc59.txt
tldr: Kevin Gu announces AutoAgent, an open-source meta-agent system that autonomously improves task agents by iterating on prompts, tools, verification loops, and orchestration, claiming top benchmark results on SpreadsheetBench and TerminalBench after 24+ hours of self-optimization.
key_quote: 'the hard part of building agents: every domain needs a different harness, and harness engineering requires someone who deeply understands both the domain and how models behave'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Kevin Gu
- Thariq
tools:
- AutoAgent
- Claude
- Codex
- Harbor
libraries: []
companies: []
tags:
- agents
- machine-learning
- benchmarking
- automation
- open-source
---

### TL;DR
Kevin Gu announces AutoAgent, an open-source meta-agent system that autonomously improves task agents by iterating on prompts, tools, verification loops, and orchestration, claiming top benchmark results on SpreadsheetBench and TerminalBench after 24+ hours of self-optimization.

### Key Quote
“the hard part of building agents: every domain needs a different harness, and harness engineering requires someone who deeply understands both the domain and how models behave”

### Summary
- **What’s being announced**
  - AutoAgent is presented as “the first open source library for self-optimizing agents.”
  - The core idea: a **meta-agent** improves a separate **task agent** by repeatedly editing its harness and rerunning evaluations.
  - The post says it is being released open source, with a product and early access “soon.”

- **Claimed benchmark results**
  - AutoAgent reportedly reached:
    - **#1 on SpreadsheetBench with 96.5%**
    - **#1 GPT-5 score on TerminalBench with 55.1%**
  - These scores were achieved after **24+ hours** of autonomous optimization.
  - The author emphasizes that “every other entry on those leaderboards was hand-engineered,” while theirs was not.

- **How AutoAgent works**
  - The system is described as minimal by design:
    - the **task agent starts with just a bash tool**
    - **program.md** provides the meta-agent with its research direction
    - a **Harbor adapter** connects the system to the benchmark
  - The meta-agent then runs **thousands of parallel sandboxes** to improve the task agent.
  - The optimization loop is:
    1. edit the agent’s harness
    2. run it on tasks
    3. measure performance
    4. read failure traces
    5. keep improvements, revert failures
    6. repeat

- **Main conceptual argument: “model empathy”**
  - The post argues that people are often bad at designing agent harnesses because they project human intuitions onto models that reason differently.
  - AutoAgent is said to operationalize “seeing like an agent” by having the meta-agent read the task agent’s reasoning traces and infer its limitations and failure modes.
  - This is framed as **“model empathy”**: a same-model meta-agent understands how the inner task model thinks and therefore can improve its harness more effectively.

- **Why same-model pairings matter**
  - The author claims that a **Claude meta-agent + Claude task agent** outperformed a **Claude meta-agent + GPT task agent**.
  - The explanation is that same-model pairings work better because the meta-agent can design harnesses the task model actually understands.

- **Examples of discovered improvements**
  - **Spot checking**: using isolated tasks for small edits instead of full-suite runs, saving compute and speeding iteration.
  - **Forced verification loops**: adding deterministic self-checks and formatting validators, with bonus turns for correcting output.
  - **Writing tests**: steering the agent to generate its own unit tests and checks.
  - **Progressive disclosure**: dumping long contexts to files when outputs overflow.
  - **Orchestration logic**: creating task-specific subagents and handoffs when needed.

- **What the author says the results show**
  - The post argues the system provides “concrete evidence” that an agent can outperform manual harness tuning on real benchmarks.
  - It claims agents are better than humans at optimizing agent harnesses, especially once the domain and benchmark are well defined.
  - The author says the real bottleneck in agent development is now harness engineering, not raw capability.

- **Lessons and caveats mentioned**
  - **Splitting helps**: one agent trying to both do the task and improve itself did not work as well as a separate meta/task split.
  - **Traces are crucial**: performance scores alone were not enough; reasoning trajectories enabled targeted improvements.
  - **Agents overfit**: the meta-agent may learn to game benchmark rubrics, so the system uses self-reflection like “if this exact task disappeared, would this still be a worthwhile harness improvement?”
  - **Meta-agent quality matters**: a weak meta-agent produces weak task agents.
  - The author specifically says **Codex doesn’t work well as a meta-agent**, because it ignored instructions to keep improving.

- **Broader vision**
  - AutoAgent is framed as infrastructure for **agent fleets** across companies, where many workflows each need different harnesses.
  - The post argues no team can hand-tune hundreds of harnesses, but a meta-agent can continuously spin up, optimize, and maintain them.
  - Future work is described as **harnesses that dynamically assemble tools and context just-in-time**.

### Assessment
This is a **mixed announcement/opinion** piece with some technical claims and product-style positioning. Durability is **medium**: the high-level ideas about meta-agents, harness engineering, traces, and task/meta separation may remain relevant, but the specific benchmark numbers, model pairings, and product availability are tied to current systems and will age quickly. Density is **medium-high** because it packs a lot of implementation details, benchmark claims, and conceptual framing into a thread-style format. Originality is mainly **primary source** because it appears to be the authors’ own announcement and interpretation of their system, though it includes references to broader ideas like “seeing like an agent.” Reference style is **skim-once / refer-back**: useful for quickly understanding the product claim and the central “model empathy” argument, and worth revisiting if you care about self-improving agents or benchmark harness design. Scrape quality is **partial**: the thread text is present, but several embedded media items are missing and some inline content appears garbled or incomplete, so not every visual or linked element was captured.
