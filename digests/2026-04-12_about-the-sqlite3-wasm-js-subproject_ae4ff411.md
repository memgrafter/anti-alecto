---
url: https://sqlite.org/wasm/doc/tip/about.md
title: About the sqlite3 WASM/JS Subproject
scraped_at: '2026-04-12T09:41:47Z'
word_count: 1177
raw_file: raw/2026-04-12_about-the-sqlite3-wasm-js-subproject_ae4ff411.txt
tldr: The SQLite WASM/JS subproject aims to make SQLite a first-class browser/WebAssembly deliverable, with low-level, OO, worker-based, and Promise-based APIs plus client-side persistence support, while explicitly avoiding UTF-16 APIs and non-browser focus.
key_quote: the goal of making WASM builds of the library first-class members of the family of supported SQLite deliverables.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Alon Zakai
- James Long
- Roy Hashimoto
tools:
- Emscripten
- sql.js
- absurd-sql
- wa-sqlite
libraries: []
companies:
- SQLite
tags:
- webassembly
- sqlite
- browser-development
- client-side-storage
- javascript-api
---

### TL;DR
The SQLite WASM/JS subproject aims to make SQLite a first-class browser/WebAssembly deliverable, with low-level, OO, worker-based, and Promise-based APIs plus client-side persistence support, while explicitly avoiding UTF-16 APIs and non-browser focus.

### Key Quote
“the goal of making WASM builds of the library first-class members of the family of supported SQLite deliverables.”

### Summary
- This page is an **“About”** document for the SQLite **WASM/JS subproject**.
- It explains WebAssembly as:
  - a low-level language for cross-compilation,
  - suitable for running in browsers,
  - designed to interoperate with JavaScript and C with relatively little friction.
- It positions this SQLite effort as:
  - **officially associated** with the SQLite project,
  - building on prior community work dating back to **2012** (via `sql.js`),
  - intended to make WASM builds a **first-class** SQLite deliverable.

#### Specific goals
- Provide a **feature-complete wrapper** around the SQLite C API as far as WASM allows.
- Expose at least these APIs:
  1. **Low-level sqlite3 C-style API**
     - close to native usage
     - documented in `api-c-style.md`
  2. **Higher-level OO API**
     - more like `sql.js` / Node-style APIs
     - talks directly to the low-level API
     - must be used from the same thread
     - documented in `api-oo1.md`
  3. **Worker-based API**
     - communicates with the lower-level APIs through Worker messages
     - intended for main-thread use with SQLite running in a Worker
     - requires special handling because Workers are async and message-based
     - documented in `api-worker1.md`
  4. **Promise-based Worker API**
     - hides the cross-thread details from users
     - also referenced in `api-worker1.md`
- Support **persistent client-side storage** where possible:
  - **OPFS** (Origin-Private FileSystem)
  - very limited **`window.localStorage` / `window.sessionStorage`** backend (`kvvfs`)

#### Non-goals
- No current plans for **UTF-16-related SQLite APIs**
  - rationale: WASM/web is UTF-8-centric and UTF-16 bindings would add complexity without enough benefit
- Focus is **currently browser-only**
  - lower-level WASM may work elsewhere if required imports are available
  - JS API details prioritize browser clients
- No support for **old or niche platforms**
  - the project is aimed at **modern web platforms**
  - deprecated SQLite library options are omitted from the WASM interface

#### Attribution / influences
- **Emscripten**
  - described as the only full-featured WASM toolchain “as of this writing”
  - especially valued for POSIX file I/O emulation, which lets SQLite run with minimal modification
  - Emscripten developers helped with OPFS features
- **sql.js**
  - important stepping stone
  - helped demonstrate pointer handling and C callback bridging in JS
  - cited as likely the first published use of SQLite for the web
- **absurd-sql**
  - explored for persistent browser-side databases via IndexedDB
  - noted as interesting but not suitable for this project’s approach
- **wa-sqlite**
  - first project to publish an **OPFS** storage option for SQLite
  - ongoing SQLite VFS work inspired this project

### Assessment
This is a **reference** page with a clear project overview and design rationale. Durability is **medium-high**: the broad goals and architectural choices are fairly stable, but details like supported APIs, storage backends, and browser/runtime assumptions may evolve with SQLite/WASM releases. The content type is **mixed** (reference + explanatory overview), and the density is **medium**: it’s concise but fairly specific about goals, non-goals, APIs, and influences. Originality is **primary source** since it describes the project’s own intentions and acknowledges prior work. It’s best used **refer-back** rather than deep-study unless you’re evaluating whether the project’s scope matches your needs. Scrape quality is **good** overall: the main prose and structure are present, though this HTML capture includes site chrome, scripts, and metadata rather than a clean markdown-only source.
