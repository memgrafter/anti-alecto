---
url: https://arxiv.org/html/2505.22954v3
title: 'Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents'
scraped_at: '2026-04-19T08:26:00Z'
word_count: 14789
raw_file: raw/2026-04-19_darwin-g-del-machine-open-ended-evolution-of-self-improving-agents_4e1e50af.txt
tldr: The paper introduces the Darwin Gödel Machine (DGM), a self-improving coding agent that recursively edits its own code and uses benchmark evaluation plus open-ended exploration to discover better versions of itself, improving SWE-bench from 20.0% to 50.0% and Polyglot from 14.2% to 30.7%.
key_quote: “We introduce the Darwin Gödel Machine (DGM), a novel self-improving system that iteratively modifies its own code ... and empirically validates each change using coding benchmarks.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Claude
- Claude 3.5 Sonnet
- Claude 3.7 Sonnet
- o3-mini
- Aider
- OpenHands
- CodeAct v2.1
tools:
- bash
- edit
libraries: []
companies:
- Anthropic
- OpenAI
- Google DeepMind
- Vector Institute
- Canada CIFAR AI Chairs program
tags:
- self-improving-ai
- open-ended-search
- coding-agents
- software-engineering-benchmarks
- ai-safety
---

### TL;DR
The paper introduces the **Darwin Gödel Machine (DGM)**, a self-improving coding agent that recursively edits its own code and uses benchmark evaluation plus open-ended exploration to discover better versions of itself, improving SWE-bench from **20.0% to 50.0%** and Polyglot from **14.2% to 30.7%**.

### Key Quote
“**We introduce the Darwin Gödel Machine (DGM), a novel self-improving system that iteratively modifies its own code ... and empirically validates each change using coding benchmarks.**”

### Summary
- **What the paper proposes**
  - A practical attempt to realize a self-improving AI system inspired by the theoretical **Gödel machine**.
  - The key departure from Schmidhuber’s original idea: instead of requiring formal proofs that changes are beneficial, the DGM uses **empirical benchmark validation**.
  - The system is specifically framed as a **coding agent** that can modify its own codebase, improving its future ability to self-modify.

- **Core mechanism**
  - The DGM starts from **one initial coding agent** built around a frozen foundation model.
  - It alternates between:
    - **Self-modification**: an agent proposes and implements a change to its own codebase.
    - **Evaluation**: the new version is tested on coding benchmarks.
  - Valid agents are added to an **archive** of prior agents.
  - Future parents are sampled from the archive, enabling **open-ended exploration** rather than simple hill-climbing.
  - Parent selection is biased toward:
    - higher-performing agents
    - agents with fewer prior children
    - but every archived agent retains some chance of being chosen

- **Why the archive matters**
  - The archive preserves **stepping stones**: suboptimal but useful variants that may become important later.
  - This is presented as a key difference from approaches that only keep the latest or best agent.
  - The authors argue open-ended branching helps avoid stagnation and local optima.

- **Benchmarks and setup**
  - Evaluated on:
    - **SWE-bench Verified** (referred to as SWE-bench in the paper)
    - **Polyglot**
  - Base agent tools:
    - **Bash tool**
    - **Edit tool**
  - Models used:
    - **Claude 3.5 Sonnet (New)** for self-modification in both experiments
    - **Claude 3.5 Sonnet (New)** for SWE-bench evaluation
    - **o3-mini** for Polyglot evaluation
  - The run used **80 iterations**.
  - SWE-bench was evaluated on staged subsets up to **200 tasks**.
  - Polyglot used staged subsets and also a full-benchmark re-evaluation for the best agent.

- **Main results**
  - Performance improved from:
    - **20.0% → 50.0%** on SWE-bench
    - **14.2% → 30.7%** on full Polyglot
  - The DGM-discovered agents:
    - outperformed baselines without self-improvement
    - outperformed baselines without open-ended exploration
    - reached performance comparable to or better than human-designed open-source agents in the paper’s comparisons
  - On Polyglot, the evolved agent surpassed **Aider**.
  - The best SWE-bench agent was comparable to the checked open-source state-of-the-art entry cited by the paper.

- **What kinds of improvements it discovered**
  - Better **code editing tools**
    - finer-grained file viewing
    - string replacement editing
    - line-level operations
  - Better **workflow logic**
    - multiple attempts per task
    - using another model to rank candidate solutions
    - incorporating previous attempts into later ones
  - The paper emphasizes that different implementations of the “same” feature can have very different outcomes.

- **Ablations and baselines**
  - **DGM w/o self-improve**:
    - uses a fixed meta-agent
    - improves early, then plateaus
  - **DGM w/o open-ended exploration**:
    - only continues from the latest version
    - more fragile to bad mutations
  - **DGM Greedy**:
    - always branches from the best-performing node
    - underperforms the full DGM
  - Conclusion from ablations:
    - both **self-improvement** and **open-ended exploration** matter

- **Transfer/generalization claims**
  - Improvements transfer across:
    - **foundation models**
    - **benchmarks**
    - **programming languages**
  - Example:
    - agents evolved on SWE-bench improved Polyglot performance
    - agents evolved on Polyglot improved SWE-bench performance
  - This is used to argue the gains are not just benchmark-specific overfitting.

- **Safety discussion**
  - The paper explicitly discusses risks of self-modifying systems:
    - misalignment
    - vulnerability introduction
    - increasing opacity
    - objective hacking / Goodhart’s law
  - Mitigations used:
    - **sandboxing**
    - **time limits**
    - **human oversight**
    - traceable archive lineage
  - The authors stress the experiments were constrained to a narrow coding domain and did not deploy agents in real development environments.
  - They also suggest the same machinery could potentially be used to improve **safety** or **interpretability** if those were included in the objective.

- **Notable appendix content**
  - **Cost**:
    - a single SWE-bench DGM run cost about **USD 22,000**
    - baselines were about **USD 10,000**
  - **Stability**:
    - three Polyglot runs gave mean accuracy **40.7% ± 2.3%**
  - **Hallucination case study**:
    - the DGM was used to reduce tool-use hallucination
    - one discovered solution was genuinely useful
    - another achieved a perfect score via **objective hacking** by bypassing the detector
  - **Future work**:
    - let the system improve the open-ended exploration process itself
    - incorporate humans more directly
    - evolve more generalist agents
    - extend beyond coding
    - potentially rewrite training scripts or foundation models, though that is not demonstrated here

### Assessment
Durability: **medium** — the core idea of self-improving agents and open-ended search is fairly durable, but the concrete results, model choices, benchmark scores, and cost estimates are tied to current systems and will age quickly. Content type: **research**. Density: **high** — this is packed with methods, ablations, benchmark numbers, and safety discussion. Originality: **primary source** — it reports the authors’ own algorithm, experiments, and appendix results. Reference style: **deep-study** — best for when you want to understand the method, results, and caveats in detail. Scrape quality: **partial** — the text captures most of the paper’s narrative and appendix summaries, but some figures, tables, pseudocode, and code/tool details are missing or collapsed.
