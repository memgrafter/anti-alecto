---
url: https://arxiv.org/html/2506.14728v1
title: 'AgentDistill: Training-Free Agent Distillation with Generalizable MCP Boxes'
scraped_at: '2026-04-12T07:38:58Z'
word_count: 5889
raw_file: raw/2026-04-12_agentdistill-training-free-agent-distillation-with-generalizable-mcp-boxes_339a478c.txt
tldr: AgentDistill proposes a training-free way to distill agent skills by extracting, abstracting, clustering, and consolidating teacher-generated Model–Context–Protocols (MCPs) into a reusable MCP-Box that student agents can mount at inference time without fine-tuning.
key_quote: No further gradient update is applied to student agent
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Jiahao Qiu
- Xinzhe Juan
- Yimin Wang
- Ling Yang
- Xuan Qi
- Tongcheng Zhang
- Jiacheng Guo
- Yifu Lu
- Zixin Yao
- Hongru Wang
- Shilong Liu
- Xun Jiang
- Liu Leqi
- Mengdi Wang
- Claude-Sonnet-4
- GPT-4o
- GPT-3.5-turbo
- Qwen3-8B
- LLaMA3.1-8B
tools:
- SmolAgents
- FastMCP
- OctoTools
libraries: []
companies:
- Princeton University
- University of Michigan
- Tsinghua University
- Shanghai Jiao Tong University
- Columbia University
- The Chinese University of Hong Kong
- University of Texas at Austin
- Anthropic
tags:
- agent-distillation
- model-context-protocol
- tool-use
- multimodal-reasoning
- benchmark-evaluation
---

### TL;DR
AgentDistill proposes a **training-free** way to distill agent skills by extracting, abstracting, clustering, and consolidating teacher-generated **Model–Context–Protocols (MCPs)** into a reusable **MCP-Box** that student agents can mount at inference time without fine-tuning.

### Key Quote
“**No further gradient update is applied to student agent**”

### Summary
- **What it is**
  - A new agent distillation framework called **AgentDistill**.
  - It transfers capabilities from a strong teacher agent (e.g. **Claude-Sonnet-4** / **GPT-4o**) to smaller student agents (e.g. **LLaMA3.1-8B**, **Qwen3-8B**, **GPT-3.5-turbo**) via **teacher-generated MCPs**.
  - The central idea is to distill teacher tool-use knowledge into a reusable **MCP-Box** rather than replaying long reasoning-action trajectories.

- **Why the authors think prior agent distillation is limited**
  - **Trajectory distillation** is expensive and tends to force students to imitate fixed sequences.
  - **Structure distillation** is more compact but can miss differences in student/teacher capability and tool constraints.
  - AgentDistill aims to be **lighter, more adaptable, and training-free**.

- **Core method**
  - The teacher agent generates **self-contained MCPs** during task solving.
  - These MCPs are:
    1. **Extracted** from successful teacher trajectories
    2. **Abstracted** into reusable, parameterized versions
    3. **Clustered** by functionality
    4. **Consolidated** into production-ready tools
  - The final output is an **MCP-Box**: a library of executable, FastMCP-compatible Python tools with functional labels.

- **How the student uses it**
  - The entire MCP-Box is mounted into the student agent’s tool interface at inference time.
  - There is **no retrieval, reranking, or parameter selection**.
  - The student remains frozen and simply decides:
    - whether to call a tool,
    - which MCP to use,
    - how to fill in arguments.
  - The claim is that this improves problem-solving without additional training.

- **Teacher/student architecture**
  - **Teacher agent**
    - Manager Agent
    - Basic Image Captioner
    - MCP Creation Module
  - **Student agent**
    - Manager Agent
    - Basic Image Captioner
    - Uses distilled MCP-Box directly
  - Teacher models include **Claude-Sonnet-4** for management and **GPT-4o** for MCP creation.

- **Benchmarks**
  - Evaluated on:
    - **PathVQA**: pathology visual question answering
    - **SLAKE**: medical multimodal VQA
    - **Game of 24**: arithmetic reasoning
  - They sample **100 validation examples** per dataset for MCP-box generation.

- **Main reported results**
  - Student agents improve consistently after MCP-Box integration.
  - Examples from the paper:
    - **PathVQA**
      - GPT-3.5-turbo: **45.7% → 52.7%**
      - Qwen3-8B: **53.0% → 55.3%**
      - LLaMA3.1-8B: **46.7% → 50.0%**
    - **SLAKE**
      - GPT-3.5-turbo: **61.0% → 68.3%**
      - Qwen3-8B: **61.0% → 67.7%**
      - LLaMA3.1-8B: **49.3% → 59.3%**
    - **Game of 24**
      - GPT-3.5-turbo: **34.3% → 82.7%**
      - Qwen3-8B: **72.7% → 79.7%**
      - LLaMA3.1-8B: **21.7% → 64.0%**
  - The biggest gains are on **Game of 24**, especially for weaker models.

- **Comparison to other systems**
  - The distilled MCP-Box helps student agents approach or sometimes match teacher performance.
  - Reported comparisons include **OctoTools** variants and the teacher agent.
  - The authors argue that MCP-based distillation can outperform retrieval-based tool pipelines.

- **Why the method may work**
  - The MCP-Box acts like an **external library of verified, parameterized protocols**.
  - It reduces low-level code generation burden.
  - It preserves high-level planning in the student while constraining tool use to a smaller, more reliable space.

- **Case study**
  - A **Brain MRI analysis** example shows how narrow teacher-generated protocols (e.g. detect bright areas, analyze left hemisphere) are consolidated into a more general tool with parameters like:
    - `region`
    - `analysis_mode`
    - threshold multipliers
  - The point is that the distilled tool generalizes across related medical scenarios without rewriting code.

- **Contribution claims**
  - **Training-free**: no fine-tuning of teacher or student.
  - **Reusable and modular**: distilled MCPs are abstracted and consolidated into an executable box.
  - **Generalizable**: improves performance on biomedical and math tasks and narrows the student-teacher gap.

### Assessment
This is a **mixed research/technical paper** with a clear method, experiments, and claims grounded in benchmark results. Its durability is **medium**: the general idea of protocol-based agent distillation may age well, but the specific implementation, model names, benchmarks, and MCP ecosystem are tied to a very current moment in agent tooling. The density is **high**, with many concrete methodological steps, model references, and numerical results packed into each section. Originality is best described as **primary source** because it presents a new framework and experimental evaluation, though it builds heavily on prior distillation and MCP-related work. It is most useful as **deep-study** material if you care about agent distillation, tool-use abstraction, or MCP-based systems. Scrape quality is **partial**: the main text is present and rich, but several equations are stripped, some tables are malformed, and some formatting artifacts/typos suggest the HTML scrape did not preserve everything cleanly.
