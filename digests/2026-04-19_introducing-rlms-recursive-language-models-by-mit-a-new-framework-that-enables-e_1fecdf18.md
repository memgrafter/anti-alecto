---
url: https://www.reddit.com/r/LocalLLaMA/comments/1q3i75u/introducing_rlms_recursive_language_models_by_mit/
title: 'Introducing RLMs (Recursive Language Models) by MIT - A new framework that enables efficient OOC (Out Of Context-window) computing LLMs - The beginning of AGI?? : LocalLLaMA'
scraped_at: '2026-04-19T21:34:39Z'
word_count: 2488
raw_file: raw/2026-04-19_introducing-rlms-recursive-language-models-by-mit-a-new-framework-that-enables-e_1fecdf18.txt
tldr: Reddit thread on MIT’s “Recursive Language Models” paper, with top commenter u/-p-e-w- arguing it’s mostly a trivial agent-style prompt-inspection trick rather than a novel step toward AGI.
key_quote: Instead of feeding the entire long prompt directly into the model, an RLM loads the prompt into a Python REPL (Read-Eval-Print Loop) environment.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: good
people:
- u/madSaiyanUltra_9789
- u/-p-e-w-
- u/SlowFail2433
- u/fuutott
- u/Royal_District9201
- u/ahmealy_
- u/ttkciar
- u/Specialist_Laugh_231
- u/Alex_L1nk
- u/str0ma
tools:
- Python REPL
- GPT-5
- Qwen
- Claude Code
- Windsurf
- Ollama
libraries: []
companies:
- MIT
tags:
- long-context
- llm-agents
- context-window
- recursive-reasoning
- ai-research
---

### TL;DR
Reddit thread on MIT’s “Recursive Language Models” paper, with top commenter **u/-p-e-w-** arguing it’s mostly a trivial agent-style prompt-inspection trick rather than a novel step toward AGI.

### Key Quote
“Instead of feeding the entire long prompt directly into the model, an RLM loads the prompt into a Python REPL (Read-Eval-Print Loop) environment.”

### Summary
- **Top comment (verbatim):** “Instead of feeding the entire long prompt directly into the model, an RLM loads the prompt into a Python REPL (Read-Eval-Print Loop) environment. This is a trivial idea that probably tens of thousands of people have had, and I’ve seen multiple vibe coded projects implementing some variation of it on this sub alone. It’s basically “agents for prompt inspection”.”
- **Top commenter:** `u/-p-e-w-`
- **Thread topics:**
  - Whether MIT’s RLM is actually novel or just a repackaging of common agent patterns
  - Long-context scaling beyond native context windows using recursive sub-calls and external code
  - Comparisons to RAG, summary agents, CodeAct, and coding agents like Claude Code/Windsurf
  - Whether the paper’s results imply an “end of context rot” or are just a practical workaround
  - Interest in latent-space versions of the idea versus tool-based recursion

- **Original post’s claim:** RLMs use an external Python REPL plus recursive self-calls to let an LLM handle arbitrarily long prompts by decomposing, inspecting, and manipulating context outside the fixed window.
- **Paper results as described by the poster:**
  - Handles up to **10M+ tokens**, far beyond base context limits like GPT-5’s **128k**
  - Reportedly outperforms baselines on **BrowseComp+**, **OOLONG**, and **CodeQA**
  - Supposedly reduces “context rot” and can be **cost-comparable or cheaper** than direct base-model use
- **Main reaction in comments:** most high-scoring replies say the approach is **not especially novel** and is already common in agentic/coding workflows.
  - `u/-p-e-w-` calls it “agents for prompt inspection.”
  - `u/SlowFail2433` says it’s correct but not novel.
  - `u/fuutott` says it’s already deployed in production with main coding agents.
  - `u/Royal_District9201` criticizes the paper as “paradigm summarization” with hype around AGI.
- **Nuanced counterpoint from the OP:** the paper’s contribution is framed as **systematic evaluation**, **10M-token scaling**, and **cost-effectiveness**, even if the core idea is familiar.
- **Technical disagreement in-thread:** some users interpret the method as basically regex/RAG-like chunking, while the OP emphasizes recursive sub-calls, code execution, and model-driven filtering rather than just static search.
- **Broader idea discussed:** several commenters want the same capability implemented **in latent space** to avoid tool-call overhead.

### Assessment
Durability is **medium**: the core concept—recursive decomposition and externalized context handling—should remain relevant, but the specifics are tied to current agent frameworks, benchmark sets, and model limits. The content type is **mixed**: primarily a **social thread** discussing a research paper, with opinion and some technical explanation. Density is **medium**: the OP includes benchmark-style claims and concrete comparisons, but much of the value comes from the debate in the comments rather than deep technical detail. Originality is **commentary/synthesis**, not a primary source; it summarizes a paper and community reactions. This is best used as **skim-once** or **refer-back** material if you want the community’s take on RLMs and whether they’re genuinely new. Scrape quality is **good** overall: it captures the OP, prominent comments, and discussion sample, though the actual paper, image, and linked media are not included beyond references.
