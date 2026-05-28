---
url: https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html
title: https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html
scraped_at: '2026-04-19T21:15:47Z'
word_count: 3692
raw_file: raw/2026-04-19_https-leodemoura-github-io-blog-2026-02-28-when-ai-writes-the-worlds-software-ht_010e830c.txt
tldr: Leo de Moura argues that as AI rapidly writes more of the world’s software, the only scalable defense is machine-checked formal verification—especially Lean—so the future competitive advantage is not faster code generation but provably correct code.
key_quote: “AI is going to write a great deal of the world's software. It will advance mathematics, science, and engineering in ways we cannot yet anticipate. The question is whether anyone can prove the results correct.”
durability: medium
content_type: opinion
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Leo de Moura
- Andrej Karpathy
- Chris Lattner
- Kim Morrison
- Ilya Sergey
- Maryna Viazovska
libraries:
- Lean
- Mathlib
- zlib
companies:
- Code Metal
- Google
- Microsoft
- AWS
- Anthropic
- OpenSSL
- Harvard Business Review
- Google DeepMind
- ByteDance
- Mistral AI
- NUS
tags:
- formal-verification
- lean
- ai-generated-code
- software-engineering
- proof-assistants
---

### TL;DR
Leo de Moura argues that as AI rapidly writes more of the world’s software, the only scalable defense is machine-checked formal verification—especially Lean—so the future competitive advantage is not faster code generation but provably correct code.

### Key Quote
“AI is going to write a great deal of the world's software. It will advance mathematics, science, and engineering in ways we cannot yet anticipate. The question is whether anyone can prove the results correct.”

### Summary
- **Core thesis:** AI is already generating a large and growing share of software, but current review/testing practices do not scale to that pace; formal verification must become the default if critical software is to remain trustworthy.
- **Main concern:**  
  - Human review is weakening in the face of AI-generated code (“Accept All” behavior).
  - Testing and code review catch many bugs, but not all, and they provide confidence rather than guarantees.
  - The author argues this creates a widening “verification gap” as AI increases software output volume.
- **Risk framing:**  
  - One subtle bug can have enormous consequences, citing Heartbleed as an example of how a single defect in a widely used library can persist despite review.
  - AI also introduces a new supply-chain risk: poisoning training data or model APIs could inject subtle vulnerabilities across many systems.
  - The result is a systemic risk for critical infrastructure: crypto, finance, medical devices, defense, transportation, and cloud services.
- **Why proof over testing:**  
  - Testing, fuzzing, and property-based tests are useful, but proofs give guarantees over all inputs and states.
  - A proof can enforce properties testing cannot, such as constant-time behavior or correctness under all edge cases and interleavings.
  - The author emphasizes that AI can make proof-writing cheap enough to scale.
- **What the verification platform needs:**  
  - A **small trusted kernel** that mechanically checks proofs.
  - A **combined programming language + theorem prover** so code and proofs live in one system with no translation gap.
  - A **rich tactic framework** so AI gets structured feedback during proof search rather than a black-box yes/no result.
  - A **large formalized knowledge base** to build on.
  - **Deep extensibility** so users and AI can add domain-specific tooling.
  - **Open source / independent control**, since the verification layer must not be under the same vendor as the AI generating code.
- **Why Lean is central to the argument:**  
  - The essay presents Lean as the best current platform for AI-assisted formal verification.
  - It notes Lean’s role in AI math systems such as AlphaProof, Aristotle, SEED Prover, Axiom, Aleph, and Mistral AI.
  - It highlights **Mathlib** as a huge formalized mathematics library: over **200,000 theorems** and **750 contributors**.
  - It also cites real enterprise use: **AWS** verified Cedar, and **Microsoft** uses Lean for SymCrypt verification.
- **Concrete AI proof example (zlib):**  
  - At Lean FRO, an AI agent converted **zlib** to Lean with minimal human guidance and no special theorem-proving model.
  - The workflow:
    - AI wrote a clean Lean implementation.
    - It passed the existing test suite.
    - Key properties were stated and proved as theorems.
    - An optimized version is being developed and proved equivalent.
  - The key theorem shown is a machine-checked proof that compressing and then decompressing returns the original data:
    - `decompressSingle (compress data level) = .ok data`
- **Why this matters:**  
  - This suggests the main bottleneck is no longer AI capability but **platform readiness**: how good the verification system is at guiding AI and checking results.
  - The author argues AI-generated proofs about production software are now feasible.
- **Broader verification examples:**  
  - **Veil** at NUS combines model checking and full proof for distributed protocols.
  - The team verified **Rabia** and found an inconsistency in a prior formal verification.
  - AI systems have also formalized major mathematical results, including the **Prime Number Theorem** and the **E8 sphere packing** proof.
- **Economic and strategic claim:**  
  - Verification is framed not as a tax but as a catalyst.
  - If AI can generate verified software cheaply, industries like aerospace, automotive, medical devices, and cloud security could shrink qualification timelines from years to weeks or hours.
  - The productivity gap will widen between teams using strong verification tooling and those that don’t.
- **Vision of the “verified stack”:**  
  - The future stack should include verified versions of:
    - cryptography
    - core data structures and algorithms
    - compression
    - parsers and protocol implementations
    - storage engines like SQLite
    - compilers and runtimes
  - Each verified component becomes a permanent public good with public proofs that can be audited and reused.
- **Engineering philosophy shift:**  
  - Engineers will spend more time on specifications, models, invariants, and intended behavior.
  - The hard part becomes defining correctness, not implementing it.
  - The author argues this makes engineering more creative, not less.
- **Important caveat:**  
  - Formal specifications encode values as well as logic, so “correctness” is not purely technical.
  - Making specifications public and formal can improve auditability, but does not solve the underlying normative questions.
- **Closing message:**  
  - AI will write much of the world’s software.
  - The critical question is whether that software can be proven correct.
  - The post is both a warning about unverified AI code and a call to build an open, Lean-based verification infrastructure.

### Assessment
This is a high-density opinion/manifesto-style technical essay with a strong advocacy posture and a clear thesis: verification must scale with AI code generation. Durability is **medium-high** because the core ideas about proofs, specifications, and trusted kernels are timeless, but some examples and adoption claims are time-sensitive to 2026 and current Lean ecosystem momentum. It is highly original as a **commentary/argument** rather than a neutral reference, drawing on many examples, anecdotes, and ecosystem claims to support a single position. The piece is best used as **refer-back** material if you want the author’s full case for Lean and verified AI-generated software. Scrape quality appears **good**: the full article text is present, including the zlib theorem snippet and closing links, though any visual formatting, inline links, or embedded media are not relevant here.
