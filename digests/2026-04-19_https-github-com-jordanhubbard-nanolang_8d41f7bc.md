---
url: https://github.com/jordanhubbard/nanolang
title: https://github.com/jordanhubbard/nanolang
scraped_at: '2026-04-19T21:20:11Z'
word_count: 2170
raw_file: raw/2026-04-19_https-github-com-jordanhubbard-nanolang_8d41f7bc.txt
tldr: NanoLang is a self-hosting, formally proved programming language that compiles to C or several backends, requires per-function `shadow` tests, and ships with a NanoISA VM, IDE tooling, and Coq proofs of core semantics.
key_quote: I am a minimal programming language designed for machines to write and humans to read.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- jordanhubbard
- Jordan Hubbard
- Sir Reginald von Fluffington III
tools:
- Coq
- Rocq Prover
- CodeMirror 6
- VS Code
- Language Server Protocol
- Debug Adapter Protocol
libraries: []
companies:
- GitHub
tags:
- programming-language
- formal-verification
- compiler
- virtual-machine
- developer-tools
---

### TL;DR
NanoLang is a self-hosting, formally proved programming language that compiles to C or several backends, requires per-function `shadow` tests, and ships with a NanoISA VM, IDE tooling, and Coq proofs of core semantics.

### Key Quote
> "I am a minimal programming language designed for machines to write and humans to read."

### Summary
- **What it is**
  - NanoLang is a minimal programming language project by `jordanhubbard`.
  - The README is written in the language’s first person voice and frames the language as machine-friendly, human-readable, and unambiguous.
  - It emphasizes formal proof, mandatory testing, and self-hosting/bootstrap status.

- **Core claims**
  - Core semantics are mechanically proved in Coq “using zero axioms.”
  - The language requires tests: every `fn` must be paired with a `shadow` test block, or compilation fails.
  - It transpiles to C for native performance and also supports a custom virtual machine, NanoISA.

- **Quick start / basic usage**
  - Clone and build:
    - `git clone https://github.com/jordanhubbard/nanolang.git`
    - `cd nanolang`
    - `make build`
  - Example compile/run:
    - `./bin/nanoc hello.nano -o hello`
    - `./hello`
  - BSD note: use `gmake` instead of `make`.

- **Language features highlighted**
  - **Type system and inference**
    - Hindley-Milner inference.
    - Optional annotations when types are inferable.
    - Immutable-by-default variables with `mut` for mutation.
  - **Syntax**
    - Both prefix and infix notation are supported.
    - Prefix calls are described as unambiguous.
    - Supports f-strings like `f"Hello, {name}!"`.
    - Pipeline syntax: `x |> f |> g`.
  - **Control flow and data types**
    - `if`, `match`, guards, or-patterns, wildcard `_`, exhaustiveness checking.
    - Structs, enums, generics, unions/variants, records.
  - **Effects and async**
    - Typed, resumable algebraic effects via `effect`, `perform`, `handle`.
    - `async fn` / `await` are lowered to a CPS state machine at compile time.
  - **Memory**
    - Automatic memory management via reference counting (“ARC”).
  - **Interop**
    - C interop is supported through modules, with isolation of calls in a separate process.
  - **Optimization**
    - Automatic profiling/optimization loop.
    - Constant folding and dead-code elimination on the AST before code generation.

- **NanoISA VM**
  - NanoLang includes a stack-based VM called NanoISA as an alternative to C transpilation.
  - VM-related tooling:
    - `./bin/nano_virt hello.nano --run`
    - `./bin/nano_virt hello.nano -o hello`
    - `./bin/nano_virt hello.nano --emit-nvm -o hello.nvm`
    - `./bin/nano_vm hello.nvm`
    - `./bin/nano_vm --isolate-ffi hello.nvm`
  - Architecture claims:
    - 178 opcodes.
    - Separate-process FFI isolation (`nano_cop`) so crashes don’t take down the main runtime.
    - VM daemon (`nano_vmd`) for faster startup/persistent service use.
    - Reference-counted GC / deterministic resource release.
    - Trap model separating computation from I/O.

- **Formal verification**
  - The proved subset includes:
    - integers, booleans, strings
    - arrays, records, variants
    - pattern matching, closures, recursion, mutable variables
  - Claimed theorems/properties:
    - type soundness
    - progress
    - determinism
    - semantic equivalence between big-step and small-step semantics
  - Proof build command:
    - `cd formal/ && make`
  - Requires Rocq Prover >= 9.0.

- **Tooling and ecosystem**
  - Language Server: `bin/nanolang-lsp`
    - hover, go-to-definition, completion, diagnostics
  - Debug Adapter: `bin/nanolang-dap`
    - breakpoints, stepping, variable inspection
  - VS Code extension in `editors/vscode/`
  - Web playground with CodeMirror 6 and live evaluation.
  - Example browser and SDL2-based launcher for demos/games.

- **Compilation targets**
  - Default native C output.
  - WebAssembly with source maps and optional Ed25519 signing/verification.
  - LLVM IR, PTX/CUDA, and RISC-V assembly.
  - Documentation extraction from triple-slash comments (`--doc-md`).

- **Build/test commands**
  - `make build`
  - `make lsp`
  - `make dap`
  - `make vm`
  - `make test`
  - `make test-vm`
  - `make test-quick`
  - `make examples`

- **Platform support**
  - Fully supported on:
    - Ubuntu 22.04+ (x86_64, ARM64)
    - macOS 14+ (Apple Silicon)
    - FreeBSD
  - Windows via WSL2 with Ubuntu.

- **Machine/LLM-oriented docs**
  - `MEMORY.md` as a training reference for idioms.
  - `spec.json` as a machine-readable formal specification.

- **Tone / history section**
  - The final section is intentionally humorous and fictionalized, “The Totally True and Not At All Embellished History of NanoLang.”
  - It narrates the origin story with a cat, Sir Reginald von Fluffington III, and a mock-serious account of ambiguity, formal verification, and self-hosting.
  - It reinforces the project’s themes: anti-ambiguity, mandatory tests, proofs, and self-compilation.
  - It also claims, jokingly, that the language has been used in production by exactly one person: its author.

### Assessment
This is a high-durability reference-style project README with mixed content: mostly factual documentation, but also heavy promotional framing and a humorous narrative appendix. It is dense with implementation claims, commands, and feature lists, so it’s high-density and useful for quick recall or deciding whether to inspect the full docs. The originality is primarily a first-party project README and documentation bundle rather than synthesis. It’s best used as a refer-back source for commands, feature claims, and architecture overviews. Scrape quality looks good overall: the main README content, code examples, commands, and the full whimsical history section are present, though this capture cannot verify linked files, source code, or any diagrams/images beyond the text shown.
