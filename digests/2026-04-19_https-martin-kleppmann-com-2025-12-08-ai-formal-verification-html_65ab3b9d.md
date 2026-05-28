---
url: https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html
title: https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html
scraped_at: '2026-04-19T21:19:56Z'
word_count: 973
raw_file: raw/2026-04-19_https-martin-kleppmann-com-2025-12-08-ai-formal-verification-html_65ab3b9d.txt
tldr: Martin Kleppmann argues that LLMs will make formal verification practical and mainstream by automating proof-writing, shifting software trust from human code review to machine-checked specifications and proofs.
key_quote: In fact, I would argue that writing proof scripts is one of the best applications for LLMs.
durability: medium
content_type: opinion
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Martin Kleppmann
tools:
- Rocq
- Isabelle
- Lean
- F*
- Agda
- seL4
- Harmonic's Aristotle
- DeepSeek-Prover-V2
companies:
- Harmonic
tags:
- formal-verification
- large-language-models
- software-engineering
- proof-assistants
- ai-assisted-coding
---

### TL;DR
Martin Kleppmann argues that LLMs will make formal verification practical and mainstream by automating proof-writing, shifting software trust from human code review to machine-checked specifications and proofs.

### Key Quote
“In fact, I would argue that writing proof scripts is one of the best applications for LLMs.”

### Summary
- **Core thesis:** AI will dramatically lower the cost of formal verification, turning it from a niche, PhD-heavy practice into a mainstream software engineering technique.
- **Why formal verification has been rare so far:**
  - Proof assistants / proof-oriented languages such as **Rocq, Isabelle, Lean, F\*, and Agda** let engineers prove code satisfies a formal spec.
  - Historically, the barrier has been **difficulty and labor**:
    - proof writing requires specialized expertise
    - it is slow and expensive
    - only a small number of people worldwide can do it well
  - Example given: the **seL4 microkernel** (as of 2009) had **8,700 lines of C**, but proving it correct took **20 person-years** and **200,000 lines of Isabelle code**.
- **Economic argument:**
  - For most software, the expected cost of bugs is still lower than the cost of formal verification.
  - Bugs are often an externality: developers don’t fully bear the cost, users do.
  - Even if developers did bear the cost, verification has been too hard and expensive to justify broadly.
- **Why AI changes the equation:**
  - LLM coding assistants are already getting good at writing **proof scripts**, not just implementation code.
  - Today a human expert still guides the process, but Kleppmann expects this to become **fully automated within a few years**.
  - Once proof generation is cheap, verification becomes economically viable for far more software.
- **Why AI increases the need for verification:**
  - Rather than human-reviewing AI-generated code, Kleppmann prefers having the AI **prove correctness**.
  - If AI can produce verified code, he would choose it over “handcrafted code” with its “artisanal bugs.”
- **Why proof scripts are a strong LLM use case:**
  - Hallucinated proof attempts don’t matter much because the **proof checker rejects invalid proofs**.
  - The checker is small and itself verified, making it difficult to sneak an incorrect proof through.
- **Remaining hard problem: specifications**
  - Automation shifts the bottleneck from proof-writing to **specification-writing**.
  - The main challenge becomes: are you specifying the *right* properties?
  - Formal specs still require human judgment and expertise, but are easier than hand-written proofs.
- **Spec-writing may also be AI-assisted:**
  - Kleppmann imagines AI helping translate between **natural language** and **formal specifications**.
  - He notes possible subtle meaning loss, but sees this as manageable.
- **Long-term vision:**
  - Developers could describe desired properties declaratively, then “vibe code” both implementation and proof.
  - In that world, people might stop inspecting generated code, just as they don’t inspect machine code emitted by compilers.
- **Conclusion:**
  - Formal verification is about to become much cheaper.
  - AI-generated code creates demand for machine-checked correctness.
  - The precision of verification complements the probabilistic nature of LLMs.
  - The main barrier may become **culture change**, not technology.

- **Updates noted by the author:**
  - A **September 2025 paper** coined **“vericoding”** for using LLMs to generate formally verified code and reports benchmark results across several languages.
  - The author mentions startups / systems reportedly improving at Lean proof writing: **Harmonic’s Aristotle, Logical Intelligence, and DeepSeek-Prover-V2**.

### Assessment
This is a **mixed opinion/forecast essay** grounded in technical facts and an economic argument. Its **durability is medium to high**: the core ideas about formal verification and AI-assisted proof generation are likely to remain relevant, though the specific state of tools and startups will age quickly. The piece is **dense** with concrete examples, named systems, and a clear causal chain, and it is clearly **commentary** rather than primary research. It’s best used as a **refer-back** reference for the argument that AI may make formal methods practical at scale. **Scrape quality is good**: the main article text and the update notes are present, though the linked references themselves are not expanded here.
