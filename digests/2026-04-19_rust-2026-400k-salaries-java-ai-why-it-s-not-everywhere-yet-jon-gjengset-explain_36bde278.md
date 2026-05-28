---
url: https://www.youtube.com/watch?v=nOSxuaDgl3s
title: 'Rust 2026: $400K Salaries, Java, AI & Why It''s Not Everywhere (Yet) — Jon Gjengset Explains - YouTube'
scraped_at: '2026-04-19T07:50:10Z'
word_count: 14745
raw_file: raw/2026-04-19_rust-2026-400k-salaries-java-ai-why-it-s-not-everywhere-yet-jon-gjengset-explain_36bde278.txt
tldr: Jon Gjengset argues that Rust’s appeal comes from its safety-plus-performance design, but broad adoption is slowed by migration cost, ecosystem maturity, and existing-language momentum—not by Rust’s learning curve alone.
key_quote: “Rust gives you the headache up front.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Jon Gjengset
- Graydon Hoare
- Niko Matsakis
tools:
- Cargo
- Neovim
- RustRover
- clap
- ONNX Runtime
- Candle
- Axum
libraries:
- CXX
- NumPy
- SciPy
companies:
- AWS
- Meta
- Google
- Amazon
- Helsing
- Discord
tags:
- rust
- programming-languages
- software-engineering
- ai
- developer-tools
---

### TL;DR
Jon Gjengset argues that Rust’s appeal comes from its safety-plus-performance design, but broad adoption is slowed by migration cost, ecosystem maturity, and existing-language momentum—not by Rust’s learning curve alone.

### Key Quote
“Rust gives you the headache up front.”

### Summary
- **Format / topic:** Interview with Jon Gjengset about Rust adoption, Rust vs. Go/C++/Java, AI, crypto, Europe vs. US work culture, and his move to Helsing.
- **Why Rust exists / what it offers:**
  - Rust tries to combine **safety, performance, and ergonomics** without the usual tradeoff of sacrificing speed for a runtime/GC.
  - Gjengset frames Rust as giving more guarantees at **compile time**, especially around memory safety and concurrency.
- **His background and Rust origin story:**
  - At MIT he found a very collaborative, curiosity-driven environment.
  - He used Rust for the **second prototype** of a research database after initially writing the first draft in Go.
  - After the **Rust 1.0 announcement**, he switched because the codebase was highly concurrent and he wanted to try the language.
- **Why Rust is admired but not everywhere:**
  - Rust has been the **most admired language on Stack Overflow for 9 years in a row**, but only about **12–14%** of developers use it.
  - Main barriers:
    - **Migration/switching cost** in existing companies
    - Existing codebases and teams already centered on other languages
    - Need for training and hiring
    - Ecosystem maturity for some niches
  - He sees adoption as **slow but real**, citing companies like **AWS** and **Meta**.
- **Rust at AWS:**
  - He worked on the **Rust build system** for Amazon/AWS.
  - His work included:
    - Supporting internal Rust builds
    - Security tracking / provenance integration
    - IDE support
    - Better debug/build/test logs
    - Making Cargo-like workflows usable internally
  - He says the push for Rust often came from **teams requesting it**, not from top-down mandate.
  - Java remained common because AWS already had deep Java infrastructure and tooling; Kotlin was also growing.
- **Where Rust fits best today:**
  - **Embedded development** (e.g. ESP32-class work, where choices are often C/C++/Rust)
  - **Command-line tools**, helped by the `clap` crate
  - **Safety-critical systems**:
    - defense
    - automotive
    - space operations
  - He also mentions Rust use in **cryptography**, where safety matters a lot.
- **Rust vs. Go / C++ / Java:**
  - **Go:** Rust is “better than Go cuz it has types.”
    - His critique of Go is that it ignored decades of programming-language research.
    - Rust gives more expressive types and stronger guarantees.
  - **C++:** Rust is strongest where **concurrency safety** matters.
    - C++ already has RAII and some memory-management benefits, but Rust adds stronger static protection.
    - Rust is especially attractive when code must avoid concurrency bugs.
  - **Java/Kotlin:** Rust can improve **tail latency** and startup behavior because there’s no GC/runtime overhead.
- **Borrow checker and learning Rust:**
  - He says the borrow checker is hard, but useful.
  - His view: good C/C++ programmers already have a kind of **mental borrow checker**.
  - Rust makes that explicit, which can make programmers better in other languages too.
  - Error messages are one of Rust’s biggest strengths because they help users build the right mental model.
- **Cargo / tooling / compiler issues:**
  - He thinks **Cargo is excellent**, especially compared with package/build tooling in many other languages.
  - Still, there are real complaints:
    - **slow compile times**
    - **sub-par debugging**
    - **high disk usage**
  - He says these are valid concerns, but many fixes involve tradeoffs or fundamental compiler/build-system complexity.
- **Macros:**
  - He doesn’t think macros are broadly overused.
  - Procedural macros are powerful and useful for ergonomics, but they can add compile-time cost.
  - Some macro use reflects missing language features rather than gratuitous cleverness.
- **Rust and editor/workflow:**
  - He uses **Neovim**, not an IDE.
  - His workflow is terminal-centric: browser + terminal, with the editor inside the terminal.
  - He tried **RustRover** briefly but didn’t feel a need to switch.
- **Rust in CI/CD and mixed-language systems:**
  - Rust can fit modern pipelines, but sometimes you need extra tooling for:
    - JUnit-style test output
    - coverage
    - cross-compilation
  - Interop is generally good with:
    - **Python/Ruby** via native modules
    - **C/C++** via C ABI / crates like `CXX`
  - Java interop via JNI is possible but more painful.
- **What happens if Rust disappears:**
  - He thinks there is **no obvious replacement** that fully covers Rust’s combination of safety and performance.
  - Zig fills some unsafe systems niches; Swift has vendor-control concerns; Julia and others don’t quite match Rust’s safety-critical fit.
  - Personally, he would mainly lose the **Rust community**, which he values deeply.
- **AI skepticism:**
  - He says AI is **overhyped** because LLMs are good at pattern replication, not real understanding.
  - He doubts current models can robustly reason about deeper program structure, type systems, or underlying scientific models.
  - He thinks AI will automate many **repetitive or pattern-heavy tasks**:
    - WordPress templates
    - API glue code
    - boilerplate integrations
  - But he does **not** believe it will replace all software engineers.
  - He thinks Rust may be **harder for LLMs to generate correctly** because it requires understanding lifetimes and the borrow checker.
- **Rust + AI / machine learning:**
  - He thinks Rust is not ideal for **research/prototyping** in machine learning, where Python’s rapid iteration dominates.
  - Rust is more appropriate for **production** ML systems, especially where reliability matters.
  - He points to bridging tools like **ONNX Runtime** and **Candle**.
- **Personal/career and Europe vs. US:**
  - He moved from the US to Norway/Europe mainly because he dislikes aspects of US society, especially **health care**.
  - He says the US market is more remote-friendly and generally pays more.
  - He estimates:
    - senior Rust engineer in **Norway**: maybe around **150k** (currency implied by context; likely NOK-equivalent in the conversation)
    - senior Rust engineer at **Amazon/US market**: around **$400,000 total compensation**
  - He says the higher US pay does not outweigh the tradeoffs for him.
- **Helsing / defense work:**
  - He joined **Helsing**, a European defense AI company.
  - He says discomfort about defense is normal and expected.
  - He believes Rust fits the defense/safety-critical context well because type safety can prevent whole classes of bugs.
- **Community and influence:**
  - He says his personal brand helps make people curious about Helsing, but it doesn’t magically convert senior engineers into job switchers.
  - He sees Rust’s direction as broadly good and not overly controlled by corporations.
  - He emphasizes that Rust evolves through **RFCs, issue trackers, forums, Zulip, and team stewardship**, not vendor decree.
  - He thinks the Rust community would be a real loss if Rust disappeared.

### Assessment
This is a **mixed interview/commentary** with a strong technical core and a lot of opinionated but informed discussion. Durability is **medium-high**: the core ideas about Rust’s safety/performance tradeoffs, adoption friction, borrow checking, Cargo, and language interop will remain relevant, though specific salary figures, survey stats, and company examples may age. The density is **high**—it covers language design, compiler ergonomics, industry adoption, AI skepticism, salaries, geography, and defense use cases with many concrete examples. Originality is **primary source** because it’s Jon Gjengset speaking directly, not a rehash. Reference style is best as **refer-back** or **deep-study** if you care about Rust adoption, tooling, or language comparisons. Scrape quality is **good** overall: the main conversation is captured in text, though as a YouTube transcript it likely misses visual context, pacing, and any on-screen material.
