---
url: https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code
title: 'Haskell for all: A sufficiently detailed spec is code'
scraped_at: '2026-04-19T06:59:42Z'
word_count: 2172
raw_file: raw/2026-04-19_haskell-for-all-a-sufficiently-detailed-spec-is-code_16de7d85.txt
tldr: The post argues that “specification-first” agentic coding is misleading because a sufficiently precise spec becomes code-like, while vague specs produce slop and unreliable implementations.
key_quote: Specifications were never meant to be time-saving devices.
durability: high
content_type: opinion
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Dijkstra
- Borges
- Claude Code
- OpenAI
tools:
- Claude Code
libraries: []
companies:
- OpenAI
tags:
- agentic-coding
- software-specification
- code-generation
- programming-languages
- ai-ethics
---

### TL;DR
The post argues that “specification-first” agentic coding is misleading because a sufficiently precise spec becomes code-like, while vague specs produce slop and unreliable implementations.

### Key Quote
“Specifications were never meant to be time-saving devices.”

### Summary
- The author says the post expands on a comic-strip idea: if a specification is detailed enough to generate working code, it starts to resemble code itself.
- Main target: claims by “agentic coding” advocates that engineers can write specs and have agents produce the implementation.
- Two misconceptions identified:
  - **Misconception 1:** specifications are simpler than code.
  - **Misconception 2:** specification writing is necessarily more thoughtful than coding.
- The post uses **OpenAI’s Symphony** project as the central example:
  - Symphony claims to be generated from a `SPEC.md`.
  - The author argues the “spec” is really a mix of pseudocode, schema dumps, and near-code.
  - Examples cited include:
    - prose dumps of database schema
    - prose dumps of control logic and retry logic
    - “cheat sheet” sections added to help a coding agent
    - outright code-like “Reference Algorithms”
- The author argues that to make a spec precise enough for reliable code generation, it must be transformed into something like code or highly formalized English.
- A quoted passage from **Dijkstra** is used to support the idea that “narrow interfaces” and precision are necessary, and that verbal precision does not actually simplify the task.
- The author reports a practical test:
  - Asked **Claude Code** to implement Symphony in **Haskell**
  - Result: multiple bugs, fixes required via prompting, and a case where the agent spun silently without progress on a sample Linear ticket: **“Create a new blank repository”**
- The post claims this flakiness is not unique:
  - Even **YAML** is highly detailed, widely used, and tested, yet many implementations still fail full conformance.
- A second major argument: the Symphony spec itself looks like **AI-generated slop**
  - It is verbose, incoherent in places, and seems optimized for implementation speed rather than clarity.
  - The author cites a section about a `linear_graphql` extension as especially representative of this style.
- The conclusion:
  - Specifications are not time-saving substitutes for coding.
  - If the goal is speed, writing code directly is often better than inserting a spec layer.
  - Bad or unclear specs cannot reliably be “filled in” by coding agents; this is just **garbage in, garbage out**.

### Assessment
This is a **high-durability** opinion essay with strong commentary and some concrete technical examples, but it is clearly tied to the current wave of **agentic coding** discourse, so parts may age as tools and workflows evolve. The content type is **opinion/mixed**, with a dense argumentative structure and several quoted excerpts from Symphony, Dijkstra, and Borges. It appears to be **primary commentary** rather than neutral synthesis. It is best used as **refer-back** material if you want the argument against spec-first agentic coding, especially the “specs become code-like” critique. Scrape quality looks **good**: the post includes many textual excerpts, footnotes, and section headings, though any formatting nuance from the original page may be missing.
