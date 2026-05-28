---
url: https://moglang.org
title: https://moglang.org
scraped_at: '2026-04-19T21:17:19Z'
word_count: 41252
raw_file: raw/2026-04-19_https-moglang-org_0ad17736.txt
tldr: Mog is a small, statically typed, compiled embedded language for AI agents that emphasizes capability-based security, native-speed plugins/hooks, and LLM-friendly syntax over general-purpose language features.
key_quote: '> "What if an AI agent could modify itself quickly, easily, and safely? Mog is a programming language designed for exactly this."'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: partial
people:
- Jeffrey Emanuel
- Simon Willison
- Claude Opus 4.6
- Kimi k2.5
- GLM-4.7
tools:
- cargo
- mogc
- rqbe
- dlopen
- llm
- dspy
libraries: []
companies:
- Voltropy
- QBE
- Lua
- Rust
tags:
- programming-languages
- capability-based-security
- embedded-systems
- ai-agents
- static-typing
---

### TL;DR
Mog is a small, statically typed, compiled embedded language for AI agents that emphasizes capability-based security, native-speed plugins/hooks, and LLM-friendly syntax over general-purpose language features.

### Key Quote
> "What if an AI agent could modify itself quickly, easily, and safely? Mog is a programming language designed for exactly this."

### Summary
- **What Mog is**
  - A programming language designed for AI agents to write their own code, scripts, hooks, and plugins.
  - Inspired by statically typed Lua: embedded, minimal, compiled, and meant to be easy for LLMs to generate.
  - Full spec is claimed to fit in **3200 tokens**.

- **Core design goals**
  - **Safety:** guest code can only call host-provided capabilities; no raw I/O/syscalls/memory access.
  - **Low latency:** compiled to native code, no interpreter/JIT/process startup overhead.
  - **LLM-friendliness:** syntax is intentionally familiar to TypeScript/Rust/Go with some Python-like ergonomics.
  - **Small surface area:** no generics beyond a few built-in parameterized types, no macros, no classes, no exceptions, no threads/locks.

- **Security model**
  - Uses a **capability system**: the host explicitly grants functions (e.g. `fs`, `process`, `http`, custom capabilities).
  - Scripts declare `requires` and `optional` capabilities; the host validates them before execution.
  - Capability access is the only way for Mog code to do I/O or interact with the outside world.
  - The compiler/runtime can enforce memory limits, cooperative interrupts, and stack overflow protection.
  - Security is **not yet audited**; the site explicitly says to treat it as unverified for untrusted third-party code.

- **Implementation/toolchain**
  - Compiler is written in **safe Rust**.
  - Uses **QBE** via a Rust implementation (`rqbe`) for code generation.
  - Produces native binaries, shared libraries (`.so`/`.dylib`) for plugins, and embedded runtime code.
  - The project is MIT licensed and hosted at `github.com/voltropy/mog`.

- **Language shape**
  - **Statically typed** with explicit type annotations in function signatures.
  - **No implicit coercion**; conversions are explicit (`as`, `str()`, parsing functions).
  - **No operator precedence**; grouping must be made explicit with parentheses.
  - **Mutable by default**: `:=` creates a binding, `=` reassigns.
  - Supports:
    - `if / else`, `while`, `for`, `break`, `continue`, `match`
    - functions and closures
    - structs
    - arrays, maps, SoA
    - `Result<T>` and `?T`
    - `async / await`, `spawn`, `all()`, `race()`
    - tensors with fixed dtypes

- **Compilation and runtime modes**
  - Standalone compiled executable for learning/testing.
  - Embedded host mode, where the host compiles and runs Mog code inside its VM.
  - Plugin mode, where `.mog` files compile to shared libraries loaded at runtime.
  - Plugin exports are `pub` functions; hosts can sandbox plugin capabilities at load time.

- **Chapter-by-chapter content**
  - **Ch. 1–5:** basics: program structure, variables, types/operators, control flow, functions, closures.
  - **Ch. 6–9:** strings, structs, collections, SoA performance layout.
  - **Ch. 10–11:** explicit error handling (`Result`, optionals, `?`, `try/catch`) and async programming (`await`, `spawn`, `all`, `race`).
  - **Ch. 12–14:** modules/packages, capabilities, embedding API in Rust/C, resource limits, interrupt handling, guard-page stack protection.
  - **Ch. 15:** tensors as data containers for ML/host compute; supports `f16`, `bf16`, `f32`, `f64`.
  - **Ch. 16:** advanced topics and omissions: type aliases, `with` blocks, GC, rqbe backend, SoA, and what Mog intentionally does not include.
  - **Ch. 17:** cookbook examples demonstrating real programs.

- **Notable constraints / omissions**
  - No classes, inheritance, traits, macros, exceptions, raw pointers, manual memory management, or standalone runtime.
  - No built-in file/network I/O; all such functionality must come from the host.
  - No user-defined generics; no operator overloading.
  - No null values; use optionals instead.

- **Examples and use cases emphasized**
  - Agent hooks (post-compaction, tool-result monitoring)
  - Safe shell-ish scripting via host-filtered capabilities
  - HTTP fetchers with retry/backoff
  - FFT and tensor manipulation
  - Matrix multiplication, validation chains, word counting, tree traversal
  - Async pipelines that fetch, process, and write data
  - Game-server NPC scripting via constrained capabilities

- **Assessment of the language positioning**
  - Mog is positioned as a niche language for **agentic self-modification and safe embedding**, not as a general-purpose systems language.
  - The pitch is that it solves a real gap: letting AI-written code inherit the same permissions and safety boundaries as the agent that produced it.
  - It reads more like a design manifesto plus a full draft language guide than a finished production language spec.

### Assessment
Durability is **medium**: the core ideas around embedded scripting, capability-based security, and native compilation are fairly timeless, but the concrete implementation details, performance claims, and AI-agent framing may age quickly. Content type is **mixed**: part announcement/positioning essay, part reference/docs, part tutorial/manual. Density is **high** because it includes a very large amount of syntax, examples, and design rationale. Originality is mostly **primary source** (the project’s own language guide and rationale), not synthesis. Reference style is **deep-study** if you want to understand or use Mog, but **skim-once** if you only need the concept. Scrape quality is **partial but strong**: the text appears very complete and includes many chapters and examples, but any diagrams, formatting nuances, and interactive elements from the site are necessarily missing.
