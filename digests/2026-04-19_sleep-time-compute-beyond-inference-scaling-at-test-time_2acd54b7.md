---
url: https://arxiv.org/html/2504.13171v1
title: 'Sleep-time Compute: Beyond Inference Scaling at Test-time'
scraped_at: '2026-04-19T08:36:35Z'
word_count: 6323
raw_file: raw/2026-04-19_sleep-time-compute-beyond-inference-scaling-at-test-time_2acd54b7.txt
tldr: 'This paper proposes sleep-time compute: pre-reasoning over persistent context before a user query arrives, then reusing that offline work to cut test-time latency/cost and improve accuracy on stateful reasoning and agentic SWE benchmarks.'
key_quote: we introduce sleep-time compute, which allows models to “think” offline about contexts before queries are presented
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- OpenAI
- DeepSeek-AI
- Claude Sonnet 3.7 Extended Thinking
- Llama2-70B
- gpt-4o-mini
- gpt-4o
- o1
- o3-mini
- DeepSeek-R1
tools:
- rethink_memory
- finish_rethinking
libraries: []
companies:
- OpenAI
- Anthropic
- DeepSeek
- Letta
- Aider-AI
- ComfyUI
tags:
- test-time-compute
- llm-inference
- stateful-reasoning
- benchmark-design
- software-engineering-agents
---

### TL;DR
This paper proposes **sleep-time compute**: pre-reasoning over persistent context before a user query arrives, then reusing that offline work to cut test-time latency/cost and improve accuracy on stateful reasoning and agentic SWE benchmarks.

### Key Quote
"we introduce sleep-time compute, which allows models to “think” offline about contexts before queries are presented"

### Summary
- **Core idea**
  - The authors argue that standard test-time scaling assumes stateless prompts, which forces LLMs to recompute similar inferences for every query.
  - Their proposal, **sleep-time compute**, moves some inference earlier: while the model is idle, it rewrites/re-represents the available context into a form that will be more useful later at test time.
  - This is especially intended for **stateful settings** such as:
    - document question answering
    - coding assistants over a shared repository
    - conversational assistants with ongoing history

- **How sleep-time compute works**
  - At sleep-time, the model sees **context** but not the next query.
  - It produces a new context containing inferences, likely questions, or reorganized information that may help answer future user queries.
  - At test-time, the user query is answered using this rewritten context, reducing the amount of reasoning needed then.
  - The paper implements this with function calling via:
    - `rethink_memory`
    - `finish_rethinking`
  - The model may call `rethink_memory` up to **10 times**.

- **Benchmarks / datasets**
  - The paper introduces **Stateful GSM-Symbolic** and **Stateful AIME** by splitting existing math reasoning problems into:
    - a **context**
    - a **question**
  - **Stateful GSM-Symbolic**
    - Derived from GSM-Symbolic P1 and P2, which build on GSM8K with added clauses.
    - P1: **5000 examples**
    - P2: **2500 examples**
  - **Stateful AIME**
    - **60 questions** from **AIME 2024 and 2025**
    - The paper manually handles edge cases where the question is not in the last sentence and strips figure latex that could leak answers.
  - **Multi-Query GSM-Symbolic**
    - A new amortization dataset where one context has multiple related queries.
    - Generated using **o3-mini** to synthesize additional question-answer pairs from existing context-question pairs.

- **Models and baselines**
  - On GSM-Symbolic:
    - **GPT-4o-mini**
    - **GPT-4o**
  - On AIME:
    - **OpenAI o1**
    - **OpenAI o3-mini**
    - **Claude Sonnet 3.7 Extended Thinking**
    - **DeepSeek-R1**
  - Baselines include:
    - standard test-time compute
    - a **context-only baseline** that tries to guess the most likely next question from context alone

- **Main results**
  - Sleep-time compute gives a **Pareto improvement** over standard test-time compute:
    - less test-time compute for the same accuracy
    - or higher accuracy for the same budget
  - Scaling sleep-time compute further improves results:
    - up to **13%** better on **Stateful GSM-Symbolic**
    - up to **18%** better on **Stateful AIME**
  - On parallel scaling comparisons, sleep-time compute is reported to outperform **pass@k** at the same test-time token budget.
  - For **Multi-Query GSM-Symbolic**, amortizing sleep-time reasoning across multiple questions reduces average cost per query, but the exact numeric reduction is **missing in the provided scrape / paper text**.

- **When it helps most**
  - The paper measures how predictable a query is from context using a **Llama2-70B base model log-probability** proxy.
  - Sleep-time compute works best when the query is **more predictable from the context**.
  - In less predictable or unrelated settings, the benefit is smaller, and standard test-time scaling may be preferable.

- **Agentic SWE case study**
  - The paper introduces **SWE-Features**, a benchmark for feature-implementation tasks in repositories.
  - It uses PRs that modify at least **3 files** and filters them to keep feature-oriented, self-contained tasks.
  - Repositories and counts:
    - **Aider-AI/aider**: **18 PRs**
    - **comfyanonymous/ComfyUI**: **15 PRs**
    - Total: **33 examples**
  - Evaluation is based on the **F1 score** between predicted modified files and ground-truth modified files.
  - Result pattern matches the math tasks:
    - sleep-time compute helps at lower test-time budgets
    - high test-time budgets can favor plain test-time compute

- **Discussion / limitations**
  - The method depends on the ability to **predict the likely query** from context.
  - It currently assumes a clean split into sleep-time and test-time, which is simpler than many real workflows with multiple interaction rounds and evolving context.
  - The authors frame sleep-time compute as a kind of **representation learning over natural language tokens**.
  - They also speculate about using it for **synthetic data generation** or amortizing expensive precomputation.

### Assessment
This is a **high-durability** research paper with a **mixed** content type: mainly **research/technical** plus some benchmark and systems design discussion. It is **high-density** and largely **primary source** material, so it is useful for deep-study rather than casual skim. For **Recall**, it clearly remembers the core framing: offline reasoning over persistent context to reduce later test-time cost. For **Decide**, it is worth re-reading if you work on LLM inference efficiency, agent workflows, or stateful prompting, but less necessary if you only care about generic test-time scaling. For **Evaluate**, the ideas are likely durable, but the claims are tied to specific model APIs, benchmarks, and 2024–2025 systems, so some implementation details will age. For **Find**, the paper is identifiable by its exact title, the new benchmark names (**Stateful GSM-Symbolic**, **Stateful AIME**, **Multi-Query GSM-Symbolic**, **SWE-Features**), and the GitHub release at `letta-ai/sleep-time-compute`. **Scrape quality is partial**: the main narrative is present, but some numbers are missing in the abstract/text (notably the average cost-per-query reduction), and several appendix sections are only partially rendered.
