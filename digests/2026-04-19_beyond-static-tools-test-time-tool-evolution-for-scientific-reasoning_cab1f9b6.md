---
url: https://arxiv.org/html/2601.07641v1#S7
title: 'Beyond Static Tools: Test-Time Tool Evolution for Scientific Reasoning'
scraped_at: '2026-04-19T07:15:51Z'
word_count: 9468
raw_file: raw/2026-04-19_beyond-static-tools-test-time-tool-evolution-for-scientific-reasoning_cab1f9b6.txt
tldr: The paper argues that scientific LLM agents should not rely on fixed tool libraries; instead, they should synthesize, verify, and evolve executable tools at test time, and it introduces the SciEvo benchmark plus experiments showing strong gains in accuracy and tool reuse.
key_quote: By transforming tools from fixed resources into problem-driven artifacts, TTE overcomes the rigidity and long-tail limitations of static tool libraries.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Jiaxuan Lu
- Ziyu Kong
- Yemin Wang
- Rong Fu
- Haiyuan Wan
- Cheng Yang
- Wenjie Lou
- Haoran Sun
- Lilong Wang
- Yankai Jiang
- Xiaosong Wang
- Xiao Sun
- Dongzhan Zhou
- Brown
- Miret
- Krishnan
- Yu
- Chen
- Nijkamp
- Schick
- Wan
- Yao
- Patil
- Qin
- Bran
- Wu
- Yang
- Zhang
- Jiang
- Qian
- Yuan
- Cai
- Wölflein
- Wang
- Sun
- Huang
- Hu
- Shang
- Reimers
- Gurevych
- Feng
- Alkhouli
- Basu
- Kate
- Peng
- Li
tools:
- GPT-4o
- Qwen2.5-7B-Instruct
- GPT-3.5-turbo
- GPT-4.1-nano
- bge-m3
- bge-reranker-v2-m3
- CodeBERT
- ReAct
- Toolformer
- Gorilla
- ToolLLM
- ChemCrow
- CheMatAgent
- ChemMAS
- HoneyComb
- SciEval
- SciBench
libraries: []
companies:
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- Xiamen University
- University of Macau
- Tsinghua University
- Hangzhou Dianzi University
- GitHub
- MIT
tags:
- scientific-reasoning
- tool-use
- llm-agents
- benchmark-design
- dynamic-tool-synthesis
---

### TL;DR
The paper argues that scientific LLM agents should not rely on fixed tool libraries; instead, they should synthesize, verify, and evolve executable tools at test time, and it introduces the SciEvo benchmark plus experiments showing strong gains in accuracy and tool reuse.

### Key Quote
“By transforming tools from fixed resources into problem-driven artifacts, TTE overcomes the rigidity and long-tail limitations of static tool libraries.”

### Summary
- **Main thesis**
  - Existing LLM tool-use systems assume a **static tool library**, but scientific reasoning needs **open-ended, domain-specific computational primitives** that may not exist in advance.
  - The paper proposes **Test-Time Tool Evolution (TTE)**: tools are **generated, validated, decomposed, deduplicated, and reused during inference** rather than selected from a frozen set.

- **What TTE is**
  - TTE turns agents from **tool selectors** into **tool creators**.
  - Two instantiations:
    - **TTE-Zero**: start from an **empty library** and evolve tools from scratch.
    - **TTE-Adapt**: start with a **source-domain library** and adapt it to a new domain.
  - Core loop:
    - **Structured Task Decomposition** into sub-goals
    - **Dynamic Tool Retrieval** from current library
    - **Generative Tool Synthesis** when no match exists
    - **Atomic Tool Refinement** to split tools into reusable “cell tools”
    - **Runtime Execution Engine** to solve the query

- **SciEvo benchmark**
  - The authors release **SciEvo**, a benchmark designed to evaluate both **scientific reasoning** and **tool evolution**.
  - Size:
    - **1,590 scientific reasoning tasks**
    - **925 evolved tools**
  - Domain coverage:
    - **Physics:** 499 tools
    - **Chemistry:** 192 tools
    - **Mathematics:** 171 tools
    - **Materials Science:** 63 tools
  - Tools were bootstrapped from seed datasets including **SciEval**, **SciBench**, and a proprietary materials-science dataset.
  - The benchmark is meant to test not just solving, but whether tools are **actually reusable primitives**.

- **Evaluation metrics**
  - Standard **Accuracy (Acc)** for final answers.
  - **Tool Reuse Rate (TRR)** at different thresholds to measure whether synthesized tools are reused or just one-off scripts.
  - For adaptation, they also split metrics into source-tool retention vs newly evolved-tool contribution.

- **Reported results**
  - TTE-Zero beats baselines on:
    - **SciBench:** 0.45 accuracy vs 0.37 (KTCE) and 0.34 (CheMatAgent)
    - **SciEvo:** 0.62 accuracy vs 0.56 (CheMatAgent) and 0.55 (KTCE)
  - Tool reuse on SciEvo is very high:
    - **TRR@1 = 0.99** for TTE-Zero
  - In cross-domain adaptation, **TTE-Adapt** outperforms “No Tool” and “Source Only” baselines in both Chemistry and Physics.
  - The paper argues that **sub-question decomposition** is crucial:
    - “S+Tools” (decomposed sub-questions) generally beats “Q+Tools” (original question retrieval).

- **Case studies**
  - **Molar mass estimation**:
    - Baselines fail due to unit mistakes or missing primitives.
    - TTE decomposes the task and synthesizes a missing tool for molar volume calculation.
  - **Electroplating stoichiometry**:
    - TTE evolves specific primitives like electron-mole calculation and area derivation to solve a multi-step physics/chemistry problem accurately.

- **Theoretical claims**
  - The appendix argues mathematically that:
    - **Atomic decomposition** should increase expected reuse over monolithic tools.
    - Larger libraries can cause a **“Tool Overload Phenomenon”**: more tools can hurt retrieval due to distractors and context interference.
    - With pruning, library growth converges to a stable equilibrium rather than growing without bound.

- **Limitations**
  - **Higher latency and compute cost** than static retrieval methods.
  - Performance depends on the base LLM’s **code-generation quality**; smaller models struggle.
  - **Safety risks** exist because the system can generate and execute arbitrary code at test time, so sandboxing and stronger verification are needed.

- **Broader impact / ethics**
  - The authors acknowledge dual-use risk, especially in chemistry/materials, and say they manually reviewed the released tools to exclude harmful ones.
  - Code and data are released under the **MIT License**.

### Assessment
This is a **research paper / technical proposal** with a mixed profile: it combines a new framework, benchmark design, experimental results, and theoretical analysis. Durability is **medium-high**: the core idea of dynamic tool evolution and the general critique of static tool libraries are likely to remain relevant, but the exact benchmark numbers, model choices (e.g. GPT-3.5-turbo, GPT-4o, Qwen2.5-7B), retrieval stack (bge-m3, bge-reranker-v2-m3), and released benchmark details are version- and time-sensitive. Density is **high**, with many concrete metrics, architecture components, datasets, and appendix-level formalism. Originality is primarily **primary source** rather than synthesis, since the paper presents its own framework, benchmark, and experiments. This is best treated as **deep-study** material if you care about scientific agents, tool use, or benchmark design, and **refer-back** material if you want the specific TTE architecture, SciEvo stats, or TRR metrics later. Scrape quality is **partial**: the text captures most sections and many tables, but several equations, symbols, and formatting elements are missing or garbled, and some table entries appear truncated.
