---
url: https://news.ycombinator.com/item?id=46294574
title: AI will make formal verification go mainstream | Hacker News
scraped_at: '2026-04-12T10:41:00Z'
word_count: 28796
raw_file: raw/2026-04-12_ai-will-make-formal-verification-go-mainstream-hacker-news_4637e5b1.txt
tldr: This Hacker News thread argues that AI may make formal verification more practical, but the real bottleneck is still writing correct specifications and requirements—not generating proofs.
key_quote: '“the challenge will move to correctly defining the specification: that is, how do you know that the properties that were proved are actually the properties that you cared about?”'
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Peter Norvig
- Terence Tao
- Tudor
tools:
- TLA+
- Lean
- Rocq
- Coq
- Dafny
- Kani
- Verus
- Alloy
- Quint
- Apalache
- TLC
- Z3
- PRISM
- Storm
- Playwright
- Claude Code
- Codex CLI
- Google Antigravity
- Black
- Semgrep
libraries:
- Rust
- TypeScript
- Haskell
- Ada/SPARK
- Dafny
- Lean 4
companies:
- AWS
- Anthropic
- Google
- Harmonic
- HashiCorp
- OpenAI
- Microsoft
tags:
- formal-verification
- ai-assisted-programming
- specification
- proof-systems
- software-quality
---

### TL;DR
This Hacker News thread argues that AI may make formal verification more practical, but the real bottleneck is still writing correct specifications and requirements—not generating proofs.

### Key Quote
“the challenge will move to correctly defining the specification: that is, how do you know that the properties that were proved are actually the properties that you cared about?”

### Summary
- The thread starts from the claim that AI could make formal verification “mainstream,” then immediately splits into two big camps:
  - **Pro-automation**: LLMs can help write specs, proofs, tests, and verification harnesses much faster than humans.
  - **Skeptical**: most software failures come from unclear, changing, or implicit requirements, not from code that fails a precise formal spec.
- A recurring theme is that **formal verification is only as good as the spec**:
  - If the spec is wrong, incomplete, or stale, a formally verified program can still be “wrong” in practice.
  - Many commenters argue the hardest part is translating messy business intent into a stable formal model.
- Several comments point out that **formal methods already exist in limited mainstream forms**:
  - Type systems are framed as a lightweight form of verification.
  - Rust, TypeScript, Ada/SPARK, and similar tools are repeatedly mentioned as partial examples.
  - Property-based testing, contracts, linters, and static analysis are suggested as the more likely “mainstream” path than full theorem proving.
- A lot of the debate centers on **where formal verification is actually useful**:
  - Strong use cases: cryptography, compilers, kernels, safety-critical systems, smart contracts, protocols, and fixed-discipline infrastructure.
  - Weak use cases: GUI/business apps, constantly changing product requirements, ambiguous user-facing behavior, and distributed systems with lots of external state.
- Another major argument is that **LLMs may help most when paired with verification tools**, not by replacing them:
  - LLMs can generate tests, specs, proof sketches, and boilerplate.
  - Proof checkers and model checkers can reject invalid outputs, turning verification into a useful feedback loop.
  - Some commenters think this could make formal methods much more approachable for teams and agents.
- There’s also a strong counterpoint that **if AI becomes good enough to reliably prove software correct, it may also be good enough to eliminate the need for humans in the coding loop altogether**:
  - In that view, the AI would not just write proofs; it would also gather requirements, choose designs, and write the implementation directly.
  - So formal verification might not become “mainstream” as a human activity, even if machine use of it increases.
- The thread repeatedly returns to **tooling and ergonomics**:
  - Better workflows, test runners, browser automation, REPLs, and verification environments are seen as more immediately useful than raw model capability.
  - Several comments say the practical bottleneck is not code generation but **validation and assumption-checking**.
- There are multiple side discussions about:
  - TLA+, Lean, Rocq/Coq, Dafny, Kani, Verus, Alloy, and Quint
  - whether proofs are “turtles all the way down”
  - whether AI should help write tests first instead of proofs
  - whether strong typing and refactoring tools matter more than formal proof systems for everyday code

### Assessment
This is a **mixed discussion thread** with high informational density but uneven focus, so its durability is **medium**: the broad arguments about specs, verification, and AI-assisted development are durable, but many specific references to current models, pricing, and workflows will age quickly. The content type is best classified as **mixed**—mostly opinion and commentary, with some tutorial-like tool mentions and reference-style discussion of formal methods. Density is **high** because it contains many specific claims, examples, tools, and counterarguments in a compact thread format. Originality is mostly **commentary/synthesis**, not a primary source article: it aggregates reactions to the HN post and mixes expert anecdotes with speculation. Reference style is **refer-back**: useful when you want to revisit the debate over whether AI makes formal verification practical, especially the recurring point that spec-writing is the real bottleneck. Scrape quality is **partial**: the thread appears flattened and heavily interleaved, with repeated quotations, nested replies, and some fragmented attribution, so the main arguments are recoverable but the conversational structure is not cleanly preserved.
