---
url: https://x.com/alex_prompter/status/2043415890507731276
title: 'Alex Prompter on X: "Everyone assumes LLMs are the future of AI. The permanent foundation. The layer everything else gets built on. I’m not so sure. The historical parallel that fits best isn’t the one most people want to hear. LLMs are Edison’s DC power grid: → Genuinely revolutionary → https://t.co/35T3AyDWLA" / X'
scraped_at: '2026-04-19T08:01:40Z'
word_count: 1077
raw_file: raw/2026-04-19_alex-prompter-on-x-everyone-assumes-llms-are-the-future-of-ai-the-permanent-foun_d561b709.txt
tldr: 'Alex Prompter argues that LLMs are like Edison’s DC grid: revolutionary and useful but architecturally limited, so AI workers should focus on durable skills like systems thinking, evaluation, data literacy, workflow design, domain expertise, and clear problem definition rather than model-specific tricks.'
key_quote: Hallucination isn’t a bug. It’s the architecture.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Alex Prompter
- Yann LeCun
tools:
- RAG
- JEPA
- Mamba
companies:
- Meta
- AMI Labs
tags:
- llm-limitations
- ai-careers
- model-architecture
- ai-workflows
- prompt-engineering
---

### TL;DR
Alex Prompter argues that LLMs are like Edison’s DC grid: revolutionary and useful but architecturally limited, so AI workers should focus on durable skills like systems thinking, evaluation, data literacy, workflow design, domain expertise, and clear problem definition rather than model-specific tricks.

### Key Quote
“Hallucination isn’t a bug. It’s the architecture.”

### Summary
- The thread’s central thesis is that **LLMs are not the final foundation of AI**; they are a powerful but likely transitional architecture, similar to **Edison’s DC power grid** before AC replaced it.
- The author argues that LLMs are:
  - **commercially dominant**
  - **solving real problems now**
  - but **architecturally limited** in ways that can’t be fully patched
- A major claim is that **hallucination is structural**, not just a training-data or fact-checking issue:
  - the post says researchers have “formally proven” LLMs cannot learn all computable functions and will inevitably hallucinate in general problem-solving settings
  - it also says another paper links hallucinations to the model’s mathematical/logical structure
  - the author further claims hallucination may be tied to creativity, creating a tension between eliminating errors and preserving useful generative behavior
- The thread says the AI “AC power” replacement is already emerging through **non-LLM or post-transformer approaches**, including:
  - **Yann LeCun / JEPA**: learning latent representations rather than next-word prediction
  - **Mamba**: presented as a faster, linearly scaling alternative to Transformers
  - **hybrid transformer-SSM architectures**: described as already shipping and handling long contexts
- It frames current LLM product layers as **workarounds**, not intrinsic capabilities:
  - **Agents** because models can’t verify outputs well
  - **Tool use** because models can’t directly interact with the real world reliably
  - **Reasoning chains** because models don’t reason natively, in the author’s view
  - **RAG** because models can’t reliably recall facts
- The practical career advice is the most durable part of the thread:
  - **systems thinking** for breaking tasks into AI-executable steps
  - **evaluation and verification** for checking AI outputs
  - **data literacy** for understanding how to structure and clean data
  - **AI-augmented workflow design** instead of just prompt crafting
  - **domain expertise + AI fluency**
  - **clear problem definition** as a transferable skill across tools and future architectures
- The post explicitly says some things **do not transfer well**:
  - memorizing specific model quirks
  - platform-specific hacks
  - building identity around one product
  - treating “prompt engineer” as a permanent job identity
- Bottom line: the author is **not bearish on AI**; they are arguing the opposite — that **LLMs are valuable now, but the most important skills are architecture-agnostic and will survive whatever replaces Transformers**.

### Assessment
This is a **mixed opinion/commentary thread** with some technical claims and career advice. Its durability is **medium**: the broader DC-vs-AC analogy and the skills advice are fairly timeless, but many specifics are tied to the current AI landscape, named architectures, and rapidly changing benchmarks/funding claims. The density is **medium-high** because it packs in a lot of claims, analogies, and practical takeaways into a short thread, though many assertions are presented rhetorically rather than carefully evidenced. Originality is mainly **commentary**, not a primary technical source: it synthesizes existing ideas, cites papers and industry examples, and uses them to make a persuasive argument. As a reference, it’s best for **refer-back** use if you want the author’s framing on LLM limitations and transferable AI skills. Scrape quality is **partial**: the text capture includes the main thread content and a linked image placeholder, but it likely omits the image’s contents and does not provide the cited paper context or source links, so several technical claims should be treated as the author’s assertions rather than independently verified facts.
