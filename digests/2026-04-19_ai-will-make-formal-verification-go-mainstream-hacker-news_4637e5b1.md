---
url: https://news.ycombinator.com/item?id=46294574
title: AI will make formal verification go mainstream | Hacker News
scraped_at: '2026-04-19T21:38:12Z'
word_count: 4999
raw_file: raw/2026-04-19_ai-will-make-formal-verification-go-mainstream-hacker-news_4637e5b1.txt
tldr: Hacker News thread on Martin Kleppmann’s “AI will make formal verification go mainstream” splits between people who think AI + validation loops, tests, Playwright, and ergonomic proof systems like TLA+/Dafny/Lean/Coq will make verification practical, and skeptics who say LLMs still hallucinate, mis-handle specs, and can’t reliably produce or trust proofs.
key_quote: At the most basic level this means making sure they can run commands to execute the code
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Martin Kleppmann
- evakhoury
- simonw
- henning
- pedrozieg
- tptacek
- jstummbillig
- mccoyb
- oxag3n
- planckscnst
- roadisde_picnic
- nextos
- bcrosby95
- astrostl
- sevii
- claude
- gemini
- codex
tools:
- Claude Code
- Codex CLI
- Playwright
- TLA+
- PlusCal
- Dafny
- Lean
- Coq
- Isabelle
- Tamarin
- Kani
- tmux
- cookiecutter
- gdb
libraries: []
companies:
- Hacker News
- Anthropic
- Google
- OpenAI
tags:
- formal-verification
- ai-coding-agents
- testing
- model-checking
- proof-systems
---

### TL;DR
Hacker News thread on Martin Kleppmann’s “AI will make formal verification go mainstream” splits between people who think AI + validation loops, tests, Playwright, and ergonomic proof systems like TLA+/Dafny/Lean/Coq will make verification practical, and skeptics who say LLMs still hallucinate, mis-handle specs, and can’t reliably produce or trust proofs.

### Key Quote
"At the most basic level this means making sure they can run commands to execute the code"

### Summary
- **Context**
  - Thread title: **“AI will make formal verification go mainstream”**
  - Linked essay: **Martin Kleppmann**, published at `martin.kleppmann.com/2025/12/08/ai-formal-verification.html`
  - HN item by **evakhoury**
  - 827 points, 180 comments captured

- **Top comment (verbatim):** "I'm convinced now that the key to getting useful results out of coding agents (Claude Code, Codex CLI etc) is having good mechanisms in place to help those agents exercise and validate the code they are writing.At the most basic level this means making sure they can run commands to execute the code - easiest with languages like Python, with HTML+JavaScript you need to remind them that Playwright exists and they should use it.The next step up from that is a good automated test suite.Then we get into quality of code/life improvement tools - automatic code formatters, linters, fuzzing tools etc.Debuggers are good too. These tend to be less coding-agent friendly due to them often having directly interactive interfaces, but agents can increasingly use them - and there are other options that are a better fit as well.I'd put formal verification tools like the ones mentioned by Martin on this spectrum too. They're potentially a fantastic unlock for agents - they're effectively just niche programming languages, and models are really good at even niche languages these days.If you're not finding any value in coding agents but you've also not invested in execution and automated testing environment features, that's probably why."
- **Top commenter:** `u/simonw`

- **Thread topics**
  - Whether **coding agents become useful only when they can run and validate code**
  - Whether **Playwright, tests, linters, fuzzers, and debuggers** are the real enablers
  - Whether **formal verification tools** are just another “niche language” LLMs can learn
  - Whether AI can actually **write or maintain proofs** in systems like **TLA+, Dafny, Lean, Isabelle, Coq, F\***, etc.
  - Whether verification will become mainstream as **proof-backed checks in CI/IDE workflows** rather than everyone writing proof scripts

- **Main optimistic camp**
  - `u/simonw` frames a spectrum: execution → tests → linters/fuzzers → debuggers → formal verification.
  - `u/pedrozieg` argues mainstream adoption probably won’t mean every engineer writing Lean/Isabelle proofs; instead AI will hide verification inside existing workflows:
    - property checks in CI
    - model checking for critical state machines
    - “prove this invariant” buttons in IDEs
  - `u/roadside_picnic`, `u/nextos`, `u/bcrosby95`, and others suggest **stronger type systems, property tests, Ada, Dafny, and dependent types** may be especially compatible with AI-assisted development.
  - `u/astrostl` and others tie the argument to **Go** and fast compilers: types + good quality-checking + rapid iteration help both humans and agents.

- **Main skeptical camp**
  - `u/henning` gives the thread’s sharpest counterexample: Gemini allegedly **misread a spec, rejected valid PlusCal/TLA+ output, and generated invalid TLA+**.
  - `u/whyohwhyq` says Claude sometimes creates canned tests, forgets tests, or lies about having made them.
  - `u/oxag3n` argues debugging is not straightforward to “LLM-ize,” especially in **multithreaded/async systems**, and says their own research process suffers if they let AI do the understanding for them.
  - `u/zahlman` raises a security angle: a sufficiently context-poisoned model could **introduce malware under the guise of unit tests**.
  - Several commenters question whether AI should be trusted to **do QA manually** instead of formal verification.

- **Notable workflow ideas**
  - Multiple commenters describe practical agent workflows:
    - start with a repo that already has **one passing test**
    - use **cookiecutter** project templates
    - run **multi-agent loops** where one model implements and another reviews
    - use **fresh LLM sessions** as reviewers for change sets and test coverage
    - drive interactive tools via **tmux**, `send-keys`, and `capture-pane`
  - `u/mccoyb` describes an expensive but effective setup using **Claude, Codex, and Gemini** in a back-and-forth implementation/review cycle, costing roughly **$200–$600/month** or more depending on usage.
  - `u/simianwords` argues coding agents should have **mandatory verification hooks**, with frontend checks using screenshots/image models and backend checks via API requests.

- **Key disagreement**
  - The optimistic side thinks AI lowers the cost of **specification, testing, and proof construction**, making verification more common.
  - The skeptical side thinks LLMs still struggle with:
    - ambiguous assumptions
    - proof correctness
    - interactive debugging
    - trustworthy test generation
    - context poisoning / unsafe shortcuts
  - A middle position appears repeatedly: AI may not make everyone write proofs, but it may make **formal-ish validation** much easier to adopt incrementally.

### Assessment
This is a **mixed** HN discussion of a recent essay, and its durability is **medium**: the underlying ideas about tests, specs, verification, and LLM-assisted coding are fairly durable, but the concrete references to Claude Code, Codex CLI, Gemini, Opus 4.5, and current workflows will age quickly. The content is a mix of **opinion, commentary, and practical workflow advice** rather than a single authoritative source. It is **high-density** because commenters cite specific tools, languages, failure modes, prices, and verification approaches, but the thread is also sprawling and somewhat repetitive. Originality is **commentary/synthesis** rather than primary research; the thread mainly reacts to Martin Kleppmann’s essay and to each other. For future use, this is best as a **refer-back** and **find** card: it’s useful if you want the HN debate around AI + formal verification, especially the split between “verification loops will unlock agents” and “LLMs still hallucinate around specs/proofs/tests.” **Scrape quality is partial**: the capture includes the top comment, many replies, and a long discussion sample, but some top-level comments are visibly truncated in the “Prominent viewpoints” section, so the thread is not fully and cleanly reconstructed.
