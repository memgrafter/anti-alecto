---
url: https://arxiv.org/abs/2604.01658v1
title: '[2604.01658v1] CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery'
scraped_at: '2026-04-19T07:24:14Z'
word_count: 369
raw_file: raw/2026-04-19_2604-01658v1-coral-towards-autonomous-multi-agent-evolution-for-open-ended-disco_c0606a31.txt
tldr: CORAL is an arXiv paper introducing an autonomous multi-agent evolution framework for open-ended discovery, claiming state-of-the-art results on 10 tasks by replacing fixed heuristics with long-running agents, shared persistent memory, and asynchronous collaboration.
key_quote: “CORAL, the first framework for autonomous multi-agent evolution on open-ended problems.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Anthropic
tools: []
libraries: []
companies:
- arXiv
- Anthropic
tags:
- artificial-intelligence
- multi-agent-systems
- evolutionary-search
- open-ended-discovery
- llm-agents
---

### TL;DR
CORAL is an arXiv paper introducing an autonomous multi-agent evolution framework for open-ended discovery, claiming state-of-the-art results on 10 tasks by replacing fixed heuristics with long-running agents, shared persistent memory, and asynchronous collaboration.

### Key Quote
“CORAL, the first framework for autonomous multi-agent evolution on open-ended problems.”

### Summary
- **Paper type:** Research / technical paper in computer science / AI.
- **Problem addressed:**
  - Open-ended discovery needs sustained search and accumulating knowledge over long runs.
  - Existing LLM-based evolution methods still depend on **fixed heuristics** and **hard-coded exploration rules**, which limit autonomy.
- **What CORAL is:**
  - A framework for **autonomous multi-agent evolution**.
  - Designed to let agents **explore, reflect, and collaborate** over time rather than being tightly scripted.
- **Core system ideas:**
  - **Shared persistent memory** so agents can reuse knowledge across sessions.
  - **Asynchronous multi-agent execution** so agents can work in parallel and interact without rigid coordination.
  - **Heartbeat-based interventions** to monitor and intervene in long-running agent processes.
- **Safety / engineering safeguards:**
  - **Isolated workspaces**
  - **Evaluator separation**
  - **Resource management**
  - **Agent session and health management**
- **Evaluation claims:**
  - Tested on **diverse mathematical, algorithmic, and systems optimization tasks**.
  - Reports **new state-of-the-art results on 10 tasks**.
  - Claims **3–10× higher improvement rates** with **far fewer evaluations** than fixed evolutionary search baselines.
  - On **Anthropic’s kernel engineering task**, four co-evolving agents improved the best known score from **1363 to 1103 cycles**.
- **Mechanistic findings:**
  - The authors say the performance gains come from:
    - **knowledge reuse**
    - **multi-agent exploration**
    - **communication between agents**
- **Main takeaway:**
  - The paper argues that increasing agent autonomy and enabling persistent multi-agent evolution can meaningfully improve open-ended discovery.
- **Availability:**
  - The abstract states that **code is available** via the paper’s linked URL.

### Assessment
This is a **technical research paper** with **high durability** in terms of the broader idea (autonomous multi-agent evolution for open-ended discovery), but the specific results are **medium-durability** because they depend on current benchmarks, task sets, and LLM/system implementations as of **Submitted on 2 Apr 2026**. The content is **dense** and mostly **primary-source** reporting of the authors’ own framework, experiments, and claims. It is best used as a **deep-study** reference if you are interested in agent architectures, evolutionary search, or open-ended optimization. Scrape quality is **partial**: the abstract and metadata are present, but the full paper, figures, methods details, and code are not included here.
