---
url: https://factory.ai/news/evaluating-compression
title: Evaluating Compression
scraped_at: '2026-04-25T04:51:24Z'
word_count: 2632
raw_file: raw/2026-04-25_evaluating-compression_a1f67e2f.txt
tldr: Factory Research’s Dec. 16, 2025 post argues that for long-running coding-agent sessions, anchored iterative summarization preserves task-critical context better than OpenAI’s `/responses/compact` and Anthropic’s Claude context compression, even though it compresses slightly less.
key_quote: Compression ratio turned out to be the wrong metric entirely.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Factory Research
- Zheng
tools:
- GPT-5.2
- OpenAI /responses/compact
- Claude SDK
libraries: []
companies:
- Factory
- OpenAI
- Anthropic
tags:
- context-compression
- coding-agents
- summarization
- llm-evaluation
- software-engineering
---

### TL;DR
Factory Research’s Dec. 16, 2025 post argues that for long-running coding-agent sessions, anchored iterative summarization preserves task-critical context better than OpenAI’s `/responses/compact` and Anthropic’s Claude context compression, even though it compresses slightly less.

### Key Quote
"Compression ratio turned out to be the wrong metric entirely."

### Summary
- **What this post is about**
  - A research/evaluation writeup on how to measure whether context compression preserves what coding agents actually need to keep working.
  - The core claim: **structured, persistent summaries beat more opaque or regenerated compression methods** on real software-engineering sessions.

- **Problem framing**
  - Long agent sessions can grow to **millions of tokens**, far beyond model context windows.
  - The wrong goal is minimizing tokens per request; the better goal is minimizing **tokens per task**.
  - Over-compression can cause the agent to forget:
    - what files it touched
    - what errors it saw
    - what it already tried
    - what decision it made
  - That leads to re-reading files, repeated dead ends, and wasted tokens.

- **Their evaluation approach**
  - They reject standard summary metrics like **ROUGE** and embedding similarity as insufficient for agent usefulness.
  - Instead they use **probe-based evaluation**:
    - After compression, ask questions requiring details from the truncated history.
    - If the summary preserved the right info, the agent answers correctly.
  - Four probe types:
    - **Recall** — factual retention
    - **Artifact** — files modified / tracked
    - **Continuation** — what should happen next
    - **Decision** — what reasoning led to a prior choice

- **Grading method**
  - Responses are judged by **GPT-5.2** using six dimensions:
    - Accuracy
    - Context awareness
    - Artifact trail
    - Completeness
    - Continuity
    - Instruction following
  - Each dimension is scored **0–5** with detailed rubrics.
  - The judge is said to be blind to which compression method produced the response.

- **Why those dimensions matter for coding**
  - **Artifact trail**: coding agents must know which files were read/changed, or they risk inconsistent edits.
  - **Continuity**: if the agent can’t continue from current state, it wastes time re-fetching context.
  - **Context awareness**: summaries must capture the present task state, not just historical facts.
  - **Accuracy**: wrong paths, names, or error messages break editing workflows.
  - **Completeness**: multi-part requests need all parts handled.
  - **Instruction following**: constraints like “only modify auth” or “output JSON” must survive compression.

- **The three compression strategies compared**
  - **Factory: anchored iterative summarization**
    - Maintains a **persistent structured summary** with explicit sections such as:
      - session intent
      - file modifications
      - decisions made
      - next steps
    - Only the newly truncated span is summarized and merged into the existing summary.
    - Main advantage: structure forces preservation of important categories.
  - **OpenAI: `/responses/compact`**
    - Produces opaque compressed representations optimized for reconstruction fidelity.
    - Reported compression ratio: **99.3%**
    - Downside: not human-readable, so it’s impossible to inspect what was preserved.
  - **Anthropic: Claude SDK compression**
    - Produces structured summaries, usually **7–12k characters**, with sections for analysis, files, pending tasks, and current state.
    - Key difference: Anthropic **regenerates the full summary each time**, whereas Factory incrementally merges new info into a persistent summary.

- **Concrete example**
  - They describe a debugging session over **178 messages / 89,000 tokens** involving a **401 error on `/api/auth/login`**.
  - The work included:
    - reading auth controller
    - inspecting middleware
    - finding a misconfigured CORS policy
    - discovering an expired Redis connection in session storage
    - fixing Redis connection pooling
    - adding retry logic
    - fixing failing tests
  - Asked later what the original issue was:
    - **Factory** gave the most specific answer, including the endpoint and root cause.
    - **Anthropic** got the general problem but lost the endpoint detail.
    - **OpenAI** lost most technical specificity.
  - The post uses this to argue that structured summaries preserve the details that matter for continuation.

- **Results**
  - Evaluated on **36,611 messages** from production software-engineering sessions.
  - Overall scores:
    - **Factory: 3.70**
    - **Anthropic: 3.44**
    - **OpenAI: 3.35**
  - Factory outperformed OpenAI by **0.35** points overall and Anthropic by **0.26**.
  - Dimension highlights:
    - **Accuracy**: Factory 4.04, Anthropic 3.74, OpenAI 3.43
    - **Context awareness**: Factory 4.01, Anthropic 3.56, OpenAI 3.64
    - **Artifact trail**: weakest for all methods, ranging **2.19–2.45**
    - **Completeness / instruction following**: all were strong and close together
  - Compression ratios:
    - OpenAI: **99.3%**
    - Anthropic: **98.7%**
    - Factory: **98.6%**
  - The authors argue the small token savings of higher compression are not worth the loss in task-relevant context.

- **Main takeaways**
  - **Structure matters more than maximum compression**.
  - **Compression ratio is the wrong optimization target** if re-fetching context costs more later.
  - **Artifact tracking remains unsolved** across all methods; a dedicated file/artifact index may be needed.
  - **Probe-based evaluation** better reflects whether summaries help real agent workflows than lexical similarity metrics do.

- **Methodology details**
  - Data came from production coding sessions in real codebases from users who opted into a research program.
  - For each compression point, they generated **four probes** based on the truncated history.
  - All three methods were applied to the same prefixes.
  - Statistical claim: the observed differences were consistent across task types and session lengths.

- **Appendix**
  - The post includes the full **system prompt** and **rubrics** used for the LLM judge.
  - It spells out scoring guides for each criterion at 0, 3, and 5.
  - The grading process is formalized: score each criterion, compute dimension averages, then overall average.

### Assessment
This is a **high-durability mixed research/engineering article** with strong practical relevance for agent memory and context compression design. The content is **dense**, specific, and clearly grounded in an evaluation framework with numbers, methodology, and rubrics, though it is still a **primary-source company writeup** rather than an independent study. It is best used as a **refer-back** or **deep-study** reference if you care about coding agents, summarization quality, or benchmark design. Scrape quality looks **good**: the full article structure, results table, example, and appendix-style rubric content are present, with no obvious missing sections or code blocks.
