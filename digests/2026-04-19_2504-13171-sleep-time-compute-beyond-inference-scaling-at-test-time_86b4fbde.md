---
url: https://arxiv.org/abs/2504.13171
title: '[2504.13171] Sleep-time Compute: Beyond Inference Scaling at Test-time'
scraped_at: '2026-04-19T08:35:50Z'
word_count: 411
raw_file: raw/2026-04-19_2504-13171-sleep-time-compute-beyond-inference-scaling-at-test-time_86b4fbde.txt
tldr: 'The paper proposes sleep-time compute: precomputing useful reasoning about a context before users ask questions, reducing test-time latency/cost while improving accuracy on modified reasoning benchmarks.'
key_quote: sleep-time compute, which allows models to "think" offline about contexts before queries are presented
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools: []
libraries: []
companies: []
tags:
- large-language-models
- inference-optimization
- test-time-compute
- reasoning-benchmarks
- ai-agents
---

### TL;DR
The paper proposes **sleep-time compute**: precomputing useful reasoning about a context before users ask questions, reducing test-time latency/cost while improving accuracy on modified reasoning benchmarks.

### Key Quote
“sleep-time compute, which allows models to ‘think’ offline about contexts before queries are presented”

### Summary
- **Problem addressed**
  - Test-time scaling improves LLM reasoning, but it increases **latency** and **inference cost**.
  - The paper asks whether some of that computation can be moved **before** the query arrives.

- **Main idea: sleep-time compute**
  - The model “thinks” **offline** about a context in advance.
  - It anticipates possible future queries and **pre-computes useful quantities**.
  - This precomputation is then reused when the actual query is presented, reducing work at test time.

- **Experiments / benchmarks**
  - The authors create modified versions of two reasoning tasks:
    - **Stateful GSM-Symbolic**
    - **Stateful AIME**
  - They also introduce **Multi-Query GSM-Symbolic**, which gives multiple related questions about the same context.

- **Reported results**
  - Sleep-time compute reduces the amount of **test-time compute needed for the same accuracy by about 5×** on both Stateful GSM-Symbolic and Stateful AIME.
  - By increasing sleep-time compute, accuracy improves by:
    - **up to 13%** on Stateful GSM-Symbolic
    - **up to 18%** on Stateful AIME
  - On **Multi-Query GSM-Symbolic**, amortizing sleep-time compute across related queries lowers the **average cost per query by 2.5×**.

- **Analysis**
  - The paper studies when this approach works best.
  - A key finding is that **predictability of the user query** is strongly correlated with how effective sleep-time compute is.
  - If likely future queries are easier to anticipate, the method helps more.

- **Case study**
  - The paper includes a case study applying sleep-time compute to a more realistic **agentic SWE** task, suggesting the approach may generalize beyond toy reasoning benchmarks.

- **What this is useful for**
  - If you want a current research idea about reducing LLM inference cost without giving up reasoning quality, this paper is directly relevant.
  - It is especially relevant for systems where:
    - the context is known in advance,
    - future queries are somewhat predictable,
    - multiple questions may be asked about the same context.

### Assessment
This is a **research** paper with **high durability** in the sense that the core idea—shifting computation from query time to precomputation time—is likely to remain relevant, though the exact results are tied to the submitted version and the specific benchmarks used. The content is **dense** and primarily **primary source** material rather than commentary or synthesis. It is best treated as **refer-back** reading: useful to revisit for the method, benchmark setup, and quantitative claims. Scrape quality is **good** for the abstract-level content shown here, but **partial** because only the abstract and page metadata are included, with no full paper text, figures, equations, or detailed method sections.
