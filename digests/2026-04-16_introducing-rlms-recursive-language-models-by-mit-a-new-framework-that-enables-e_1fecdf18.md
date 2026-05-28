---
url: https://www.reddit.com/r/LocalLLaMA/comments/1q3i75u/introducing_rlms_recursive_language_models_by_mit/
title: 'Introducing RLMs (Recursive Language Models) by MIT - A new framework that enables efficient OOC (Out Of Context-window) computing LLMs - The beginning of AGI?? : LocalLLaMA'
scraped_at: '2026-04-16T06:30:24Z'
word_count: 2488
raw_file: raw/2026-04-16_introducing-rlms-recursive-language-models-by-mit-a-new-framework-that-enables-e_1fecdf18.txt
tldr: A Reddit thread about MIT’s “Recursive Language Models” paper argues that LLMs can surpass fixed context limits by using a Python REPL-style external environment for recursive sub-calls, but commenters mostly debate whether this is a real breakthrough or just a formalized version of common agentic prompting and search patterns.
key_quote: Instead of feeding the entire long prompt directly into the model, an RLM loads the prompt into a Python REPL (Read-Eval-Print Loop) environment.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- madSaiyanUltra_9789
- p-e-w
- martinerous
- ahmealy_
- SlowFail2433
- ttkciar
- Specialist_Laugh_231
- Alex_L1nk
- str0ma
- Royal_District9201
- sammy_samster
- Primary-Formal-1140
- Open-Noise-4386
tools:
- Python REPL
- CodeAct
- Claude Code
- Ollama
- grep
libraries: []
companies:
- MIT
- OpenAI
- Anthropic
- Ollama
- Windsurf
tags:
- long-context
- llm-agents
- recursive-reasoning
- context-window
- ai-research
---

### TL;DR
A Reddit thread about MIT’s “Recursive Language Models” paper argues that LLMs can surpass fixed context limits by using a Python REPL-style external environment for recursive sub-calls, but commenters mostly debate whether this is a real breakthrough or just a formalized version of common agentic prompting and search patterns.

### Key Quote
“Instead of feeding the entire long prompt directly into the model, an RLM loads the prompt into a Python REPL (Read-Eval-Print Loop) environment.”

### Summary
- **What the post is about**
  - The OP introduces an MIT arXiv paper, **“Recursive Language Models (RLMs)”** (`arXiv:2512.24601`), and frames it as a framework for **out-of-context-window (OOC)** computation.
  - The core pitch: instead of cramming a huge prompt into the model’s context window, the prompt is loaded into an **external Python REPL environment**, where the model can inspect, recurse, and manipulate state programmatically.

- **OP’s claimed mechanism**
  - The model can:
    - **peek and decompose** a long prompt,
    - **invoke itself recursively** on sub-tasks,
    - **use code** to store intermediate results and stitch together answers.
  - The OP describes this as a way to manage context far beyond the model’s native limit.

- **OP’s claimed results**
  - The thread says the paper reports scaling to **10M+ tokens**.
  - The OP specifically claims:
    - up to **two orders of magnitude beyond** the base model’s context window,
    - better performance than base models and baselines like **summary agents** and **CodeAct**,
    - less performance loss from **context rot**,
    - cost per query that is comparable to or cheaper than direct base-model use.
  - Benchmarks named in the OP include **BrowseComp+**, **OOLONG**, and **CodeQA**.
  - The OP also claims an improvement of about **~91.3% absolute value** relative to the base model, and around **~40% / ~20%** versus **CodeAct-agent** and **summary-agent** respectively on **BrowseComp+ (1K)**.

- **OP’s interpretation**
  - The OP argues this suggests LLMs are more capable than current deployments allow and could become far more economically useful with enough software scaffolding.
  - They frame it as potentially relevant to “the beginning of AGI,” though this is presented as speculation and a question to the thread, not as a paper claim.

- **Main skeptical response from commenters**
  - Several commenters say the idea is **not novel**:
    - one calls it “a trivial idea” and basically **“agents for prompt inspection”**;
    - others say this is already common in agentic systems and coding agents.
  - The strongest repeated theme is that the paper may be **real but not especially original**.

- **Nuanced praise / practical angle**
  - Some commenters think the paper is useful because it provides:
    - systematic evaluation,
    - a formalized way to handle large contexts,
    - evidence that these patterns work at scale.
  - One commenter notes the challenge is preserving the **big picture** across subtasks, and another compares the idea to manually decomposing tasks into subtasks.
  - A linked implementation, **Ollama-RLM-Analyzer**, is mentioned as an RLM-inspired tool for local LLMs that uses **chunking** and browser-stored state.

- **Specific tools and examples mentioned in discussion**
  - **CodeAct** is used as a baseline comparator in the OP.
  - **Claude Code** is mentioned by commenters as an existing example of similar recursive agent behavior.
  - **Windsurf** is mentioned as combining multiple search techniques, including regex, for large codebases.
  - A commenter links a simpler **Medium explanation** and another links a **webcomic/video** of the paper.

- **A recurring dispute in the thread**
  - Is this a genuinely new model architecture or just a cleaner name for established agent workflows?
  - Are the gains due to a new conceptual advance, or just better orchestration, search, and chunking?
  - Can the method really be called a path toward AGI, or is that just hype?

- **Overall tone of the thread**
  - The post is less a neutral paper summary and more a **novelty-vs-practicality debate**.
  - The OP is enthusiastic and interprets the paper as a major step toward long-running, economically useful AI.
  - The comment section is mostly skeptical but acknowledges that the technique may still be useful in practice, especially for long-context retrieval and decomposition.

### Assessment
This is a **mixed** Reddit thread: part paper announcement, part commentary, part skepticism-driven discussion. **Durability: medium** — the underlying idea of recursive/tool-using agents is likely to remain relevant, but the specific claims, benchmarks, and hype are tied to a particular paper and current agent ecosystem. **Content type: mixed** (announcement + commentary + technical discussion). **Density: medium-high** because the OP includes concrete benchmark names, comparative claims, and numbers, while the comments add practical counterpoints and examples like **Claude Code**, **Windsurf**, and **CodeAct**. **Originality: commentary/synthesis** — this is not a primary source paper itself but a Reddit discussion reacting to one, with the OP also paraphrasing and interpreting the MIT paper. **Reference style: refer-back** if you want to recall the debate, benchmark names, or community reaction; **skimming once** is enough if you only want the headline. **Scrape quality: good** — the thread title, OP, and a substantial sample of comments are included, though the screenshot/image content itself is not readable here and the full comment tree is not fully captured.
