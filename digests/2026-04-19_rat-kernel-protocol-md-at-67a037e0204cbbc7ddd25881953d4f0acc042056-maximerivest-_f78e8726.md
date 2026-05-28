---
url: https://github.com/MaximeRivest/rat/blob/67a037e0204cbbc7ddd25881953d4f0acc042056/KERNEL-PROTOCOL.md?plain=1#L1
title: rat/KERNEL-PROTOCOL.md at 67a037e0204cbbc7ddd25881953d4f0acc042056 · MaximeRivest/rat
scraped_at: '2026-04-19T07:26:42Z'
word_count: 2496
raw_file: raw/2026-04-19_rat-kernel-protocol-md-at-67a037e0204cbbc7ddd25881953d4f0acc042056-maximerivest-_f78e8726.txt
tldr: 'This document specifies the `rat` kernel protocol: a JSON-lines stdin/stdout contract for language runtimes that supports `ping`, `run`, inspection, completion, status, input, streaming messages, and pushed `event`s, with `rat serve` acting as the host and MCP bridge.'
key_quote: If you can read stdin and write stdout in JSON, you can be a rat kernel.
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Maxime Rivest
tools:
- rat
- tmux
- IPython
libraries:
- Node
companies: []
tags:
- language-runtime
- json-protocol
- repl-architecture
- stdin-stdout
- mcp
---

### TL;DR
This document specifies the `rat` kernel protocol: a JSON-lines stdin/stdout contract for language runtimes that supports `ping`, `run`, inspection, completion, status, input, streaming messages, and pushed `event`s, with `rat serve` acting as the host and MCP bridge.

### Key Quote
"If you can read stdin and write stdout in JSON, you can be a rat kernel."

### Summary
- Defines a **rat kernel** as a **RAPL**: **Read, Act, Perceive, Loop** — a runtime that acts on the external world and perceives results, rather than evaluating only local memory like a REPL.
- The kernel protocol is **JSON Lines over stdin/stdout**:
  - **stdin →** requests from Go to the kernel
  - **stdout ←** responses and pushed messages from the kernel
  - **stderr** is for diagnostics only
  - each line is one complete JSON object
- The protocol is used for:
  - built-in Go-backed kernels such as `internal/python`
  - generic runtimes loaded from `runtime.yaml` via `internal/generic/runtime.go`
  - in both cases, `rat serve` hosts the kernel subprocess and exposes it through MCP

**Lifecycle**
- Go starts the kernel subprocess
- Sends `{"op": "ping"}` at startup
- Kernel responds `{"ok": true}`
- Normal interaction begins
- On shutdown, Go sends `{"op": "shutdown"}` and the kernel exits

**Request ops from Go to kernel**
- `ping`: startup health check
- `run`: execute code while preserving state across calls
  - example response includes `success`, `output`, `error`, and optional `vars`
  - if the last statement is an expression, the kernel should emit its `repr` in `output`
- `look_overview`: list user-visible variables in a preformatted `text` block
- `look_at`: inspect a specific symbol with free-form formatted details
- `complete`: return up to 50 completions as `label  kind`
- `status`: report `idle`, `busy`, or `waiting_for_input`
- `input`: deliver text to a kernel blocked on user input
- `shutdown`: clean exit, no response expected

**Streaming messages during `run`**
- `output_chunk`: partial stdout while code is still running
- `input_request`: kernel is waiting for stdin
- `input_delivered`: input was received and execution resumed

**Events**
- Kernels can push `{"op": "event", ...}` at any time, even while idle
- This is meant for external-world runtimes like:
  - Slack / email / Discord messages
  - price alerts
  - background progress updates
  - connection errors
- Common event types described:
  - `message`
  - `progress`
  - `alert`
  - `error`
- Events are written to the activity log as event records and can be forwarded to clients later

**REPL frontend guidance**
- The protocol is the runtime side; the frontend side should preserve the language’s **native REPL UX** where possible
- Frontends should redirect only execution, completion, inspection, and control to the kernel
- The document maps frontend actions to host/kernel ops:
  - `execute(code)` → `run`
  - `complete(code, cursor)` → `complete`
  - `inspect(at)` → `look_at`
  - `status()` → `status`
  - `interrupt()` → host cancel path
  - `exit()` → exit frontend only, not the kernel
- The kernel is the source of truth for:
  - namespace
  - execution count
  - completion context
  - inspection results
  - busy/waiting state
- The host owns subprocess lifecycle, restart/shutdown policy, MCP exposure, and transport adaptation
- The frontend owns terminal rendering, keybindings, prompt editing, and redraw state

**Three frontend patterns**
- **Pattern A: attach to real session** via `tmux`  
  - good when there are no hooks
  - simple but scraped terminal output is fragile
- **Pattern B: hook native eval**  
  - best option for Python/Node/Julia/R when hooks exist
  - gives clean structured responses and preserves native UX
- **Pattern C: thin wrapper**
  - fallback when there are no hooks and no `tmux`
  - works but offers poor human UX

**Why structured output matters**
- The doc argues against always using `tmux` because scraped terminal text is less reliable than structured JSON
- Example contrast:
  - heuristic cleanup of terminal output vs.
  - machine-readable JSON like `{"success": true, "output": "...", "vars": 3}`

**Writing a kernel**
- Minimal kernel steps:
  1. read lines from stdin
  2. parse JSON
  3. dispatch on `op`
  4. write JSON response to stdout
  5. preserve state across calls
- For custom runtimes:
  - `runtime.yaml` declares detection and startup info
  - `rat serve` loads config
  - `internal/generic/runtime.go` starts the kernel script
  - the frontend talks to `rat serve`, not directly to the subprocess
- Includes a minimal Python example showing handlers for `ping`, `run`, `look_overview`, `look_at`, `complete`, `status`, and `shutdown`

### Assessment
This is a **high-durability** technical reference/specification: it’s tied to the `rat` architecture, but the underlying ideas—JSON-line process protocols, host/kernel separation, streaming, and event-driven runtimes—are broadly reusable. The content type is **reference / technical / mixed**, with a strong implementation focus rather than opinion. Density is **high**: it contains concrete ops, example payloads, lifecycle rules, frontend architecture, and a minimal Python kernel. Originality is best described as **primary source** for the `rat` protocol design, not a synthesis or commentary piece. It’s best used as a **refer-back** document for implementation and protocol compliance, though it can also be skimmed once to understand the architecture. Scrape quality is **good**: the page appears complete, with code blocks, tables, and section structure present, and no obvious truncation or missing sections.
