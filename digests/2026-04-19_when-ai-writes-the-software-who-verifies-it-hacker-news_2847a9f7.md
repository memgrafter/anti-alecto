---
url: https://news.ycombinator.com/item?id=47234917
title: When AI writes the software, who verifies it? | Hacker News
scraped_at: '2026-04-19T21:44:13Z'
word_count: 17850
raw_file: raw/2026-04-19_when-ai-writes-the-software-who-verifies-it-hacker-news_2847a9f7.txt
tldr: Hacker News discussion of Leonardo de Moura’s “When AI writes the software, who verifies it?” centers on whether AI-generated code can be trusted without stronger specs/tests, with replies splitting between TDD/spec-first advocates, skeptics of formal methods at scale, and people reporting that verification and code review are already becoming the real bottlenecks.
key_quote: At a certain point, the verification complexity takes off. You literally run out of time to verify everything.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Leonardo de Moura
- Claude
- ChatGPT
- Gemini
- Leeonardo de Moura
tools:
- Lean
- Coq
- Dafny
- Verus
- Why3
- Rocq
- ATS
- Idris
- OpenAPI
- JSON Schema
- TLA+
- AWS Cedar
- Claude Code
- Replit
- Jira
- GitHub
- Chrome
- UIA
libraries:
- Rust
- Haskell
- OCaml
- Python
- TypeScript
- Go
- JavaScript
- Svelte
- Vue
- React
companies:
- AWS
- Microsoft
- Google
- Anthropic
- OpenAI
tags:
- ai-coding
- software-verification
- formal-methods
- testing
- code-review
---

### TL;DR
Hacker News discussion of Leonardo de Moura’s “When AI writes the software, who verifies it?” centers on whether AI-generated code can be trusted without stronger specs/tests, with replies splitting between TDD/spec-first advocates, skeptics of formal methods at scale, and people reporting that verification and code review are already becoming the real bottlenecks.

### Key Quote
"At a certain point, the verification complexity takes off. You literally run out of time to verify everything."

### Summary
- **Thread topic:** whether AI coding agents make verification, testing, and code review the limiting factor in software development.
- **Main article framing:** Leo de Moura argues that if AI produces more software, organizations will need machine-checked verification to keep up, with Lean-style proof kernels as a scalable answer.
- **Concrete article anchor points mentioned in-thread:**
  - Lean, Coq, Dafny, Verus/Rust, Why3, Rocq, ATS, Idris
  - AWS Cedar / Dafny correction: one commenter notes Cedar is written in **Dafny**, not Lean
  - benchmark cited in-thread: **27% Lean, 44% Verus/Rust, 82% Dafny** success rates for off-the-shelf LLMs on formally verified program synthesis
  - verification alternatives discussed: **OpenAPI**, **JSON Schema**, **property-based testing**, **fuzzing**, **TLA+**
  - recurring theme of **specification-first vs code-first**
- **Top comment (verbatim):** "The Claude C Compiler illustrates the other side: it optimizes for passing tests, not for correctness. It hard-codes values to satisfy the test suite. It will not generalize."
- **Top commenter:** not clearly recoverable from the provided scrape
- **Thread topics:**
  - AI-generated code passing tests without implementing real business logic
  - whether tests should be written before code, after code, or independently from specs
  - whether formal verification languages can realistically scale to application software
  - code review bottlenecks, 100% test coverage, and teams rubber-stamping AI output
  - whether better architecture, stricter contracts, or human accountability matter more than more tests
- **Major viewpoints in the discussion:**
  - **TDD/spec-first camp:** tests should be independent of implementation; write failing tests first, then code; broad tests are better than bug-specific ones.
  - **Skeptical camp:** AI can write tests that merely mirror the code, so tests alone don’t prevent wrong behavior; human reviewers still matter.
  - **Formal-methods camp:** AI may finally make Lean/Dafny/Coq economically worthwhile by shifting effort into precise specs and proofs.
  - **Pragmatist camp:** for many teams, especially UI-heavy or exploratory work, formal verification is too expensive; humans still need to understand the system and make judgment calls.
  - **Process/incentives camp:** many failures are caused less by AI itself than by incentives to ship quickly, superficial review culture, and lack of time for QA.
- **Repeated concerns from commenters:**
  - LLMs are good at generating plausible-looking code/tests, not necessarily correct or generalized behavior.
  - “100% coverage” can become meaningless if AI generates huge test files that nobody truly verifies.
  - Frontend testing is often described as either impractical or too shallow to catch real user-facing issues.
  - Verification may need to shift from the code itself to the **generation process** and the specs/contracts feeding the agent.
- **Notable counterpoint:** some commenters argue AI could improve productivity if used as a pair programmer with human oversight, and that the real future is more explicit specs, more reviews, and more constrained agent workflows rather than fully autonomous coding.

### Assessment
This is a mixed-content Hacker News thread with high density but fragmented structure, so it’s best treated as a reference-back item rather than a polished essay. Durability is **medium-high**: the specific model names, benchmark numbers, and current AI workflow complaints may age, but the underlying verification/specification tension is likely long-lived. Content type is **mixed**: opinion, technical discussion, and practical workflow commentary. Originality is mostly **commentary/synthesis** rather than primary research, though it references a real article and a benchmark result. Reference style is **refer-back** if you care about AI coding, testing, formal methods, or software process debates. Scrape quality is **partial**: the thread is clearly captured, but comment ordering, “top comment” metadata, and exact author attribution are unreliable/missing, and the content is heavily interleaved and repetitive.
