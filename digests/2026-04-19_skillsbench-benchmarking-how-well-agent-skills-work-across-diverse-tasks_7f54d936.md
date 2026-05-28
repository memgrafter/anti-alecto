---
url: https://arxiv.org/html/2602.12670v1
title: 'SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks'
scraped_at: '2026-04-19T07:06:16Z'
word_count: 12797
raw_file: raw/2026-04-19_skillsbench-benchmarking-how-well-agent-skills-work-across-diverse-tasks_7f54d936.txt
tldr: SkillsBench is a new benchmark showing that curated Agent Skills substantially improve LLM-agent performance across 84 containerized tasks, but gains vary by domain, are often harmed by overly long Skill docs, and cannot be replicated reliably by self-generated Skills.
key_quote: Curated Skills raise average pass rate by 16.2 percentage points(pp), but effects vary widely by domain ... and 16 of 84 tasks show negative deltas.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
- Google
- OpenAI
- Hake
- Merrill
- Sutton
- Sumers
- Yao
- Liu
- Jimenez
- Zhou
- Xie
- Koh
- Trivedi
- Yang
- Chan
- Zhuo
- Mattson
- Chiang
- Srivastava
- Lewis
- Schick
- Qin
- Shinn
- Madaan
- Wang
- Wei
- Zhu
- Yao
- Khattab
- Brown
- Chowdhery
- Touvron
- Ouyang
tools:
- Claude Code
- Gemini CLI
- Codex CLI
- Harbor
- GPTZero
- pytest
- Docker
- Gemini 3 Flash
- Gemini 3 Pro
- GPT-5.2
libraries:
- openpyxl
- scipy
- pandas
- OR-Tools
companies:
- Anthropic
- Google
- OpenAI
tags:
- llm-agents
- benchmarks
- agent-skills
- evaluation
- containerized-tasks
---

### TL;DR
SkillsBench is a new benchmark showing that curated Agent Skills substantially improve LLM-agent performance across 84 containerized tasks, but gains vary by domain, are often harmed by overly long Skill docs, and cannot be replicated reliably by self-generated Skills.

### Key Quote
“Curated Skills raise average pass rate by 16.2 percentage points(pp), but effects vary widely by domain ... and 16 of 84 tasks show negative deltas.”

### Summary
- **What SkillsBench is**
  - A benchmark for evaluating **Agent Skills**: structured procedural packages added at inference time.
  - Built around **84 evaluated tasks across 11 domains** (from **86 total tasks**, with **2 excluded**).
  - Uses **deterministic verifiers**, full trajectory logging, and paired evaluation under:
    - **No Skills**
    - **Curated Skills**
    - **Self-generated Skills**

- **Core claim**
  - Curated Skills help a lot on average, but not uniformly:
    - **+16.2 percentage points** average pass-rate improvement across **7 model-harness configurations**
    - **16 of 84 tasks** get worse with Skills
  - Self-generated Skills do **not** help on average:
    - **–1.3 pp** average vs. no-Skills baseline

- **Benchmark design**
  - Built on the **Harbor** container benchmark framework.
  - Each task includes:
    - **instruction**
    - **Dockerized environment**
    - **reference solution**
    - **deterministic verifier**
  - Emphasis on preventing leakage:
    - human-written instructions
    - Skills must be **general procedural guidance**, not task-specific answers
    - CI checks plus leakage audits
  - Tasks were contributed by **105 contributors** from academia and industry:
    - **322 candidate tasks**
    - **86 final tasks**
    - **26.7% acceptance rate**

- **What counts as a Skill**
  - Procedural, reusable, task-class guidance
  - Structured as **SKILL.md** plus optional resources/scripts/examples
  - Portable across agent harnesses
  - Explicitly excludes:
    - system prompts
    - few-shot examples
    - RAG retrievals
    - tool docs

- **Experimental setup**
  - **7 model-harness configurations**
  - **7,308 valid trajectories**
  - Models:
    - GPT-5.2
    - Claude Opus 4.5
    - Claude Opus 4.6
    - Claude Sonnet 4.5
    - Claude Haiku 4.5
    - Gemini 3 Pro
    - Gemini 3 Flash
  - Harnesses:
    - Claude Code
    - Gemini CLI
    - Codex CLI
  - All runs used **temperature 0**

- **Main results**
  - Best raw performance with Skills:
    - **Gemini 3 Flash + Gemini CLI: 48.7% pass rate**
  - Largest improvement:
    - **Claude Opus 4.5 + Claude Code: +23.3 pp**
  - Self-generated Skills were weak or harmful:
    - only **Opus 4.6** showed a small gain (**+1.4 pp**)
    - Codex + GPT-5.2 dropped by **–5.6 pp**
  - Harness behavior matters:
    - Claude Code showed strong Skills usage
    - Codex often acknowledged Skills but solved independently
    - Gemini CLI sometimes had setup-time issues

- **Domain-level effects**
  - Biggest gains:
    - **Healthcare: +51.9 pp**
    - **Manufacturing: +41.9 pp**
    - **Cybersecurity: +23.2 pp**
  - Smaller gains:
    - **Software Engineering: +4.5 pp**
    - **Mathematics: +6.0 pp**
  - Interpretation:
    - Skills help most where specialized procedural knowledge is underrepresented in pretraining

- **Task-level effects**
  - Huge wins on some tasks:
    - **mario-coin-counting: +85.7 pp**
    - **sales-pivot-analysis: +85.7 pp**
    - **flood-risk-analysis: +77.1 pp**
    - **sec-financial-report: +75.0 pp**
  - Some tasks were hurt by Skills:
    - **taxonomy-tree-merge: –39.3 pp**
    - **energy-ac-optimal-power-flow: –14.3 pp**
    - **trend-anomaly-causal-inference: –12.9 pp**
  - Conclusion: Skills can add conflicting guidance or overhead on tasks where the model already has decent priors.

- **Skills design findings**
  - **2–3 Skills per task** performed best:
    - **+18.6 pp**
  - **4+ Skills** had much weaker gains:
    - **+5.9 pp**
  - Documentation length matters:
    - **Detailed** and **compact** Skills worked best
    - **Comprehensive** Skills actually hurt performance (**–2.9 pp**)
  - Takeaway: concise, focused procedural guidance outperforms exhaustive documentation

- **Model-scale implication**
  - Skills can partially substitute for model size:
    - smaller models with Skills can outperform larger models without them
  - Example:
    - **Claude Haiku 4.5 with Skills: 27.7%**
    - vs **11.0% without Skills**

- **Failure analysis**
  - Most failures were not “no output,” but **quality below threshold**:
    - **49.8%** of failures
  - Other major failure types:
    - **Agent timeout: 17.8%**
    - **Incomplete solution: 10.2%**
    - **No output produced: 7.9%**
  - Skills mainly reduced:
    - quality failures
    - incomplete solutions
  - Self-generated Skills increased failure and timeout rates relative to baseline

- **Important limitations**
  - Focused on **terminal-based, containerized tasks**
  - May not generalize to:
    - GUI agents
    - multi-agent systems
    - very long-horizon workflows
  - Gains may partly reflect “more context” rather than pure structure, though self-generated Skills results argue structure matters
  - Determinism is not perfect; contamination/leakage cannot be fully ruled out

- **Why this paper matters**
  - It reframes Skills as something that should be **evaluated directly**, not assumed helpful.
  - It argues for **paired benchmarks**: measure task performance both with and without augmentation.
  - It provides evidence that **Skill quality, concision, and harness integration** matter as much as the underlying model.

### Assessment
This is a **high-density research paper** with strong practical relevance and fairly high durability, though some implementation details are version-sensitive because it references current commercial models and agent harnesses. The content type is **mixed** but primarily **research/technical**: it presents a benchmark, experimental methodology, quantitative findings, and limitations. The originality is **primary source** rather than synthesis, since it introduces SkillsBench and reports new measurements across 7,308 trajectories. It is best used as **refer-back** material if you care about agent augmentation, benchmark design, or Skills usage; a full reread would be warranted for methodology, tables, and failure taxonomy. Scrape quality is **good**: the text includes the abstract, main sections, appendix material, tables, task list, and failure analysis, though some equations/formatting are partially mangled and a few tables appear line-broken.
