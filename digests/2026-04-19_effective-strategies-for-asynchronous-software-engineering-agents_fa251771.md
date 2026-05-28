---
url: https://arxiv.org/html/2603.21489v1
title: Effective Strategies for Asynchronous Software Engineering Agents
scraped_at: '2026-04-19T08:26:52Z'
word_count: 8223
raw_file: raw/2026-04-19_effective-strategies-for-asynchronous-software-engineering-agents_fa251771.txt
tldr: This paper proposes CAID, a branch-and-merge multi-agent architecture for asynchronous software engineering, and reports +26.7% absolute on PaperBench and +14.3% on Commit0 over single-agent baselines by combining centralized dependency-aware delegation, isolated git worktrees, and test-gated merges.
key_quote: we show that branch-and-merge is central to effective multi-agent software engineering, and that SWE primitives provide the basis for implementing it.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Wang
- Zhao
- Starace
- Jimenez
- Yang
- Claude
- MiniMax
- Anthropic
- OpenAI
tools:
- git worktree
- git commit
- git merge
- asyncio
- OpenHands agent SDK
libraries: []
companies:
- OpenHands
- Fujitsu
tags:
- multi-agent-systems
- software-engineering
- git
- task-delegation
- benchmarks
---

### TL;DR
This paper proposes **CAID**, a branch-and-merge multi-agent architecture for asynchronous software engineering, and reports **+26.7% absolute on PaperBench** and **+14.3% on Commit0** over single-agent baselines by combining centralized dependency-aware delegation, isolated git worktrees, and test-gated merges.

### Key Quote
"we show that branch-and-merge is central to effective multi-agent software engineering, and that SWE primitives provide the basis for implementing it."

### Summary
- **Core thesis:** Long-horizon SWE tasks are not just a planning problem; they are also an **integration/coordination** problem. CAID is designed to make multi-agent collaboration work by importing software-engineering primitives into agent orchestration.
- **Main idea of CAID:**  
  - A **central manager** builds a dependency graph and delegates tasks only when dependencies are satisfied.
  - Multiple engineer agents work **concurrently**.
  - Each engineer uses an **isolated git worktree** so edits do not collide.
  - Changes are integrated through **git commit / git merge**, with conflicts surfaced explicitly.
  - Engineers must **self-verify** with executable tests before submission.
- **Named coordination framing:** The paper calls this paradigm **Centralized Asynchronous Isolated Delegation (CAID)** and argues that **branch-and-merge** is the key mechanism for shared-artifact collaboration.
- **SWE primitives mapped to coordination roles:**  
  - dependency graph → scheduling constraints  
  - git worktree → workspace isolation  
  - git commit / pull request → structured signaling  
  - git merge → output integration  
  - merge conflict resolution → conflict handling  
  - code review → verification  
  - asyncio parallel execution → concurrent execution  
  - event loop + await → coordination cycle  
  - git reset --hard HEAD → state synchronization
- **Benchmarks used:**  
  - **Commit0-Lite**: implement Python libraries from scratch, judged by unit tests.  
  - **PaperBench (Code-Dev protocol)**: reproduce a conference paper’s main contributions/results, judged by **gpt-5-mini**.
- **Reported headline gains (from the abstract):**  
  - **+26.7% absolute on PaperBench**
  - **+14.3% on Commit0**
- **Experimental setup:** Built on **OpenHands agent SDK v1.11.0** and evaluated with **GLM 4.7**, **MiniMax 2.5**, and **Claude-4.5-Sonnet**.
- **What the main results say:**  
  - CAID consistently outperforms the single-agent baseline across both benchmarks and all three models.
  - The paper emphasizes that the advantage comes from **changing the execution method**, not changing the model.
- **Strategic finding:** A “single-agent first, multi-agent later” fallback strategy is inefficient; the paper argues it is better to use coordinated multi-agent execution **from the outset**.
- **Ablation/analysis highlights:**  
  - **Worktree isolation matters**: soft isolation helps sometimes, but physical isolation via git worktrees is more stable, especially on the more open-ended PaperBench.
  - **More engineers is not always better**: performance does not increase monotonically; too much parallelism creates integration overhead and conflicts.
  - **Delegation quality matters**: assigning the wrong dependency (e.g., missing a critical file like `autodiff.py`) can dramatically hurt performance.
  - **Verification style trades off with speed**: heavier manager review improves pass rate but increases runtime; engineer self-verification is a middle ground.
- **Limitations noted by the authors:** CAID improves success rates but adds cost/runtime overhead, depends on the manager’s decomposition quality, and is currently evaluated only on software-engineering benchmarks with version-control and test infrastructure.

### Assessment
This is a **research/technical** paper with a strong **mixed** component because it combines system design, benchmark evaluation, and analysis of coordination patterns. **Durability: medium-high** — the specific benchmark numbers and model versions will age, but the architectural lessons about isolation, dependency-aware delegation, and merge-based coordination are likely to remain useful. **Density: high** — it is packed with implementation details, benchmark names, configuration choices, and quantitative results. **Originality: primary source** — this is the authors’ own proposal and experiments, not a secondary summary. **Reference style: deep-study** if you care about multi-agent SWE systems; otherwise it is still good for **refer-back** when designing agent orchestration or comparing isolation strategies. **Scrape quality: partial** — the HTML extraction captured the narrative and many tables, but some equations/tables are visibly broken or partially missing formatting, and several numeric placeholders are malformed; the quoted text is therefore safest when taken from clearly preserved prose rather than reconstructed table text.
