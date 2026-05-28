---
url: https://news.ycombinator.com/item?id=47312728
title: 'Show HN: The Mog Programming Language | Hacker News'
scraped_at: '2026-04-19T21:40:24Z'
word_count: 955
raw_file: raw/2026-04-19_show-hn-the-mog-programming-language-hacker-news_ebfde9c9.txt
tldr: Hacker News Show HN post by Ted introducing Mog, a small statically typed compiled embedded language designed for LLM-written plugins with capability-based permissions, native-code performance, and runtime self-modification without restarting the host agent.
key_quote: Mog is a statically typed, compiled, embedded language (think statically typed Lua) designed to be written by LLMs -- the full spec fits in 3,200 tokens.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Ted
tools:
- OpenClaw
- Bun
- OpenAI's Codex CLI
libraries:
- LLVM
- QBE
companies: []
tags:
- programming-languages
- llm-agents
- security-models
- embedded-systems
- compiler-design
---

### TL;DR
Hacker News Show HN post by Ted introducing **Mog**, a small statically typed compiled embedded language designed for LLM-written plugins with capability-based permissions, native-code performance, and runtime self-modification without restarting the host agent.

### Key Quote
“**Mog is a statically typed, compiled, embedded language (think statically typed Lua) designed to be written by LLMs -- the full spec fits in 3,200 tokens.**”

### Summary
- **Top comment (verbatim):** "Mog is a statically typed, compiled, embedded language (think statically typed Lua) designed to be written by LLMs -- the full spec fits in 3,200 tokens."
- **Top commenter:** `Ted`
- **Thread topics:**
  - Designing a programming language specifically for LLMs to generate reliably
  - Capability-based permissions for AI agent plugins and scripts
  - Compiling agent-written code into native plugins without restart
  - Safety model: preventing plugins from gaining syscalls/libc/memory access
  - Async integration, coroutine lowering, and host-controlled execution limits

- Ted describes **Mog** as an embedded language meant to be authored by AI agents/LLMs:
  - **Statically typed** and **compiled**
  - Intended to have a very small spec: **~3,200 tokens**
  - Similar in spirit to **statically typed Lua**, but narrower and safer for generated code

- Core design goals:
  - Make code generation easier for LLMs by reducing ambiguity and foot-guns
  - Keep the language small enough to fit in context
  - Prefer constrained expressiveness over generality

- Language restrictions chosen for LLM-friendliness:
  - **No operator precedence**; ambiguous expressions must be parenthesized
  - **No implicit type coercion**
  - Reduced support for **generics**
  - **No macros, metaprogramming, or syntactic abstraction**

- Security / permissions model:
  - Mog is designed around **capability-based permissions**
  - A Mog program cannot directly access:
    - syscalls
    - libc
    - raw memory
  - It can only:
    - call host-provided functions
    - allocate memory inside a host-provided arena
    - return values
  - This is meant to keep agent-written plugins from breaking host state or escaping permissions

- The host can inspect and control dangerous actions because the guest only reaches them through host-supplied functions:
  - Example: a guest-generated Mog program may be given a function to run a bash command
  - The host can still enforce session-level permissions when that function is called

- Performance / execution model:
  - Mog compiles to **native code**
  - Intended for **low-latency plugin execution**
  - No interpreter overhead, no JIT, no process startup cost
  - Compiler is written in **safe Rust**
  - Execution time limits are enforced with **cooperative interrupt polling**
    - Compiler inserts checks so the host can ask the guest to stop
    - Claimed overhead: about **10%** in very tight loops

- Self-modification / live loading:
  - An agent can generate Mog source, compile it, and **dlopen()** it into the host process
  - This allows **adding or changing behavior without restarting** the agent/session
  - Ted presents this as useful for situations where an agent needs to adapt quickly to user feedback

- Async and runtime integration:
  - Async support is built into Mog
  - Ted says it adapts **LLVM coroutine lowering** to a Rust port of **QBE**
  - The host library can integrate into an async event loop, tested with **Bun**

- Memory / stack design:
  - Mog uses a **stack inside the host-provided memory arena**, not the system stack
  - A **guard page** separates stack and heap
  - Claimed benefit: avoids stack overflow without runtime overhead

- Current limitations and future work:
  - Ted says Mog is **not yet batteries-included**
  - Missing or incomplete standard library pieces include:
    - JSON
    - CSV
    - SQLite
    - HTTP
  - He wants an `llm` library so Mog code can call models through the host with:
    - multi-model support
    - token budgeting
  - He also wants a more ergonomic plugin lifecycle and stronger host integration for agents like **OpenClaw** or **OpenAI’s Codex CLI**

### Assessment
This is a **mixed announcement/tutorial/reference** post with moderate density and strong original content from the project author. Durability is **medium**: the architectural ideas around capability-based embedded languages and LLM-oriented language design are fairly timeless, but the specifics of Mog’s implementation, tooling, and feature gaps will age quickly as the project evolves. The content is **primary source** and useful as a **refer-back** reference if you want to understand the language’s motivation, security model, and runtime design. Scrape quality is **good** in that the full text of the post is present, though it does not include the actual HN comment thread beyond the post itself, and there are no missing code blocks or images to worry about.
