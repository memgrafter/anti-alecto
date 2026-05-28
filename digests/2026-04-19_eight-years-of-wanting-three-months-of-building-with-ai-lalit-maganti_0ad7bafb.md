---
url: https://lalitm.com/post/building-syntaqlite-ai/
title: Eight years of wanting, three months of building with AI - Lalit Maganti
scraped_at: '2026-04-19T07:19:32Z'
word_count: 3949
raw_file: raw/2026-04-19_eight-years-of-wanting-three-months-of-building-with-ai-lalit-maganti_0ad7bafb.txt
tldr: AI coding agents made it possible to build and ship syntaqlite—a serious SQLite devtools project in three months—but also caused a month of “vibe-coding” sprawl, forcing a full rewrite and teaching that AI is great for implementation but weak at design.
key_quote: AI is an incredible force multiplier for implementation, but it’s a dangerous substitute for design.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Lalit Maganti
tools:
- Aider
- Roo Code
- Claude Code
- syntaqlite
libraries: []
companies:
- Google
- Perfetto
tags:
- ai-assisted-development
- software-design
- sqlite
- developer-tools
- refactoring
---

### TL;DR
Lalit Maganti argues that AI coding agents made it possible to build and ship `syntaqlite`—a serious SQLite devtools project in three months—but also caused a month of “vibe-coding” sprawl, forcing a full rewrite and teaching that AI is great for implementation but weak at design.

### Key Quote
> “AI is an incredible force multiplier for implementation, but it’s a dangerous substitute for design.”

### Summary
- **Context / motivation**
  - The author spent **eight years** wanting better devtools for **SQLite**.
  - He works on **PerfettoSQL**, a SQLite-like language used internally at Google with about **100K lines** of code, and wanted tools like:
    - formatters
    - linters
    - editor extensions
  - Existing open-source SQLite tools were not reliable, fast, or flexible enough.

- **Why the project was hard**
  - The goal was to parse **SQLite exactly**, not approximately.
  - SQLite has:
    - **no formal specification**
    - **no stable parser API**
    - an implementation that does **not build a parse tree**
  - The only viable route was to extract and adapt relevant parts of SQLite’s C source.
  - The grammar is huge: **more than 400 rules**.
  - The work also required:
    - tests
    - debugging
    - user bug fixes
    - maintaining broad compatibility for any SQLite user, not just Perfetto

- **How AI changed the project**
  - The author had used coding agents since early 2025:
    - **Aider**
    - **Roo Code**
    - **Claude Code** since July
  - He stress-tested a maximalist approach: could he build it mostly with **Claude Code on the Max plan (£200/month)**?
  - In **January**, he delegated almost everything to Claude and got a functional prototype:
    - parser in **C**
    - extraction scripts in **Python**
    - formatter
    - support for SQLite + PerfettoSQL extensions
    - web playground
  - But the codebase became **“complete spaghetti”**:
    - fragile
    - scattered
    - hard to understand
    - some files grew to **thousands of lines**
  - The prototype was abandoned, though it proved the concept and produced **500+ tests**.

- **The rewrite**
  - He restarted from scratch and moved much of the project to **Rust**.
  - Reasons:
    - C would be awkward for higher-level components like a validator and language server
    - Rust unified extraction and runtime better than splitting logic between C and Python
  - He changed his role:
    - took full ownership of decisions
    - used AI more like **“autocomplete on steroids”**
    - enforced opinionated design up front
    - reviewed every change
    - added scaffolding: linting, validation, non-trivial testing
  - Core features landed in **February**.
  - Final work—tests, editor extensions, packaging, docs—led to a **0.1 launch in mid-March**.

- **Where AI helped most**
  - **Overcoming inertia**
    - AI turned vague anxiety into concrete tasks.
    - It reduced the barrier to starting by giving something tangible to inspect and replace.
  - **Writing obvious code faster**
    - Good for functions/classes with clear requirements.
    - Produced consistent, standard code and often better documentation than the author would have written.
  - **Refactoring**
    - AI was especially useful when constantly reshaping the codebase.
    - The author says the lesson from the failed first attempt was that **refactoring must be continuous** when using AI-generated code.
  - **Teaching assistant**
    - Helped learn **Wadler-Lindig pretty printing**.
    - Helped bridge unfamiliar domains like:
      - Rust tooling
      - editor extension APIs
    - Useful for reorienting after time away from the project.
  - **Making the project more complete**
    - AI made “nice-to-have but important” features cheap enough to include:
      - editor extensions
      - Python bindings
      - WASM playground
      - docs site
      - multi-ecosystem packaging
    - Freed mental energy for UX:
      - error messages
      - formatter defaults
      - CLI flags

- **Where AI hurt**
  - **Addictive / slot-machine behavior**
    - Prompting created a “just one more try” loop.
    - The sunk-cost fallacy made him keep using AI even when it was ill-suited.
  - **Tiredness feedback loop**
    - When tired, prompts got worse, output got worse, and the cycle degraded productivity.
  - **Losing touch with the codebase**
    - He sometimes lost the detailed mental model of the system.
    - That made communication with the agent degrade into vague descriptions like “change the thing which does Bar.”
    - He compared this to being a manager who doesn’t understand the code.
  - **Slow corrosion of judgment**
    - Cheap refactoring encouraged deferring design decisions.
    - That procrastination made the code harder to reason about.
  - **False confidence from tests**
    - AI made it easy to generate **500+ tests**, but tests could not foresee every future edge case.
    - Several cases revealed that the architecture itself was wrong and needed rework.
  - **AI has no sense of time**
    - It lacks historical memory of why decisions were made or reversed.
    - It cannot naturally preserve institutional knowledge.
    - Documentation can help, but drafting and auditing it is still costly.
    - Context pollution makes it hard to know which past design choices matter elsewhere.

- **Core pattern: when AI works vs. when it doesn’t**
  - **Best case:** tasks the author already understood deeply
    - e.g. parser rule generation
    - He could review results quickly and correct them immediately
  - **Good but careful:** tasks he could describe but not yet fully understand
    - e.g. learning Wadler-Lindig for formatting
    - AI helped him learn while staying engaged
  - **Worst case:** tasks where he didn’t yet know what he wanted
    - especially architecture
    - AI could lead him down dead ends that felt productive but later collapsed
  - He argues AI is weak at **design**, especially when there is no objectively checkable answer.
  - Example: the **public API** was hard to get right because there is no test for “pleasant to use.”
  - He uses a **relativity** analogy:
    - local pieces of code can be correct
    - but global architecture can still be wrong

- **Conclusion**
  - The project would not exist without AI, and it completed far more than he could likely have done alone.
  - But the journey was not smooth:
    - one month lost to vibe-coding
    - a total rewrite
    - real cost from misunderstanding the codebase
  - Final takeaway:
    - **AI is excellent for implementation**
    - **AI is dangerous as a substitute for design**
    - He wants more honest, detailed accounts of real software built with AI—not just toy demos

### Assessment
This is a **mixed** first-person **commentary/opinion** piece with substantial reflective and practical detail, so its durability is **medium**: the specific AI tools, timing, pricing (£200/month Max plan), and project state are time-bound, but the broader lessons about AI-assisted software development, refactoring, and design are likely to remain relevant. The density is **high**, with many concrete examples, names, counts, and process details; it’s clearly **original work** rather than synthesis, since it draws from the author’s own journal, transcripts, and commit history. Best used as a **refer-back** reference if you want lessons on using coding agents for a real project, not as a skim-once announcement. Scrape quality appears **good**: the main text is captured end-to-end, including quoted claims and section structure, though any images, footnotes, or linked evidence are not present in the provided content.
