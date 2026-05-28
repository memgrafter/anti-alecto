---
url: https://news.ycombinator.com/item?id=46684958
title: 'Nanolang: A tiny experimental language designed to be targeted by coding LLMs | Hacker News'
scraped_at: '2026-04-12T07:29:41Z'
word_count: 8745
raw_file: raw/2026-04-12_nanolang-a-tiny-experimental-language-designed-to-be-targeted-by-coding-llms-hac_fe8b7fb3.txt
tldr: A Hacker News thread debates whether programming languages should be redesigned for LLMs, with the original poster arguing for Nanolang/librdx as an AST- and CRDT-oriented “specification language” for AI-assisted coding, while commenters split between skepticism, practical tooling ideas, and support for simpler, more verifiable languages.
key_quote: “LLMs don’t need new languages, we do.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Jordan Hubbard
- Jonathan Edwards
- Claude
- Gemini
- Opus 4.5
- DeepSeek
- Rust
tools:
- Claude Code
- Cursor
- VS Code
- Autocomplete
- Automerge
- MPS
libraries:
- librdx
- toon
companies:
- JetBrains
- Nvidia
- FreeBSD
- Apple
- DeepSeek
tags:
- llm-assisted-coding
- programming-languages
- specification-languages
- ast-editing
- crdt
---

### TL;DR
A Hacker News thread debates whether programming languages should be redesigned for LLMs, with the original poster arguing for Nanolang/librdx as an AST- and CRDT-oriented “specification language” for AI-assisted coding, while commenters split between skepticism, practical tooling ideas, and support for simpler, more verifiable languages.

### Key Quote
“LLMs don’t need new languages, we do.”

### Summary
- **Topic of the thread:** Whether a new programming language should be designed specifically to make coding LLMs more effective, and whether that’s better than improving specs, tooling, or existing languages.
- **Original premise from the post:**
  - The author argues that the real need is not “new languages” but **new ways to create specifications**.
  - They propose a system where an LLM acts as a **pseudocode-to-code translator**, with humans writing the spec in a mixture of code-like syntax and natural language.
  - They also frame code generation as producing **diffs/modification instructions** against an existing codebase, rather than code snapshots.
- **Nanolang / librdx details mentioned in the discussion:**
  - The author links to **`https://github.com/gritzko/librdx`** and describes it as the foundation of their work.
  - It is presented as an **RDX tree CRDT** mapped to the **AST tree** of a program.
  - The intent is **conflictless merge**, overlay branches, and AST-level editing/merging, akin to a **CRDT DOM for the AST** rather than line-based diffs.
  - The author says it is more like **CRDT JSON DOM** than “JSON+”.
  - Nanolang is described later by the author as:
    - a **thought experiment**
    - a **Decorator Crab** / “Frankenstein” language that accreted features
    - using **prefix notation**
    - designed with LLM use in mind, not human ergonomics
- **Core arguments in favor of LLM-targeted languages/specs:**
  - LLMs can already translate pseudocode into code well.
  - A language or spec format that is more machine-friendly could reduce bugs by reducing ambiguity.
  - Some commenters argue that future code will be mostly AI-written, so languages should optimize for machine generation and verification.
  - Several people suggest **specification-first development**, where the spec and tests are the key artifacts.
  - One commenter argues that higher-level languages could let humans describe user-facing value, and the compiler/LLM would implement the details.
- **Core skepticism / counterarguments:**
  - Many commenters say **LLMs struggle less with syntax than with semantics, obscure APIs, and correctness**.
  - Some argue that if a language is close to existing languages, the benefit is trivial; if it’s too novel, the LLM will struggle without lots of examples.
  - Others say the biggest bottleneck is not code generation, but **auditing, testing, and verification** by humans.
  - Several commenters question whether a new language is worth it compared with:
    - better tooling
    - better compiler errors
    - stricter types
    - existing languages like Rust, Kotlin, Go, Haskell, OCaml, F#, Lisp variants
- **Practical points raised repeatedly:**
  - **Feedback loops matter**: compiler errors, linters, runtime tests, and trace/debug modes help LLMs correct themselves.
  - **LLMs can pick up syntax quickly** from a grammar, examples, or context, but deeper language idioms and semantic conventions are harder.
  - **Training-data scarcity** for a new language is a concern, but some commenters argue that long context, docs, examples, and tooling can compensate.
  - A few commenters mention that if a language is primarily for LLMs, it may not need to be maximally human-friendly.
- **Specific design ideas floated in the thread:**
  - A **terse programming language** that doubles as specification.
  - A language that supports **tests as first-class artifacts**.
  - A language that can be written in **words or code**, with syntax looseness but semantic rigor.
  - A **delta on top of a known language** (especially Python) so the LLM only needs a compact “skill” prompt.
  - A **hosted/fine-tuned language-specific LLM** as part of the language product.
  - A service where model providers let you **pay to include your language in training data**.
  - Use of **AST-to-AST transpilation** or a translation layer to reuse training from existing languages.
  - Ideas around **streaming code / live LLM interaction**, not just static code generation.
- **Examples and side discussions:**
  - JavaScript/Python/Kotlin/Rust/Haskell/OCaml/F# are used as comparison points.
  - One tangent explains **lambda functions** to someone coming from older imperative languages.
  - Another tangent discusses **Rust error handling**, arguing for more human-intent-friendly error context.
  - Another commenter discusses **s-expressions**, **Clojure**, **MPS**, **Subtext**, **Inform7**, **d2lang**, **BPMN**, **sourcemaps**, and **OpenSCAD** as related examples of higher-level or structured specs.
- **Status and maturity of Nanolang:**
  - The author explicitly says it is **experimental**, not a polished product.
  - They note that it is partly a **solo project** and partly a response to the current LLM era.
  - The author provides some examples of using Claude/agents with the language and says the compiler’s debugging/tracing support makes LLM iteration easier.

### Assessment
This is a **mixed** content thread: part announcement, part opinion/essay, part technical discussion, and part practical experimentation report. Durability is **medium**: the broad questions about specs, AST-level editing, and LLM-assisted coding are likely to stay relevant, but many specifics are tied to current LLM capabilities and the particular state of Nanolang/librdx. Density is **high** because the thread contains many concrete claims, design ideas, examples, and counterarguments, though it is also noisy and repetitive in places. Originality is mostly **commentary** with some **primary-source** elements from the project author describing Nanolang/librdx directly. Reference style is best as **refer-back** rather than deep-study: useful for recalling the debate and the project’s framing, but not a clean canonical spec. Scrape quality is **partial**: the thread text is extensive and includes many comments, but it is fragmented, repetitive, and clearly missing the structure of the original page and any linked code/docs beyond pasted excerpts.
