---
url: https://raw.works/ypi-a-recursive-coding-agent/
title: 'RAW.works - ypi: a recursive coding agent'
scraped_at: '2026-04-19T07:28:38Z'
word_count: 602
raw_file: raw/2026-04-19_raw-works-ypi-a-recursive-coding-agent_f0595bc5.txt
tldr: The post describes ypi, a recursive coding agent built on Pi that adds a single rlm_query function plus a system prompt to let the model self-delegate work across nested child processes with isolated jj workspaces.
key_quote: Pi already has a bash REPL. I added one function — rlm_query — and a system prompt that teaches Pi to use it recursively.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Pi
- jj
- bash
- rlm_query
- bunx
- npm
libraries: []
companies:
- RAW.works
- github.com/rawwerks/ypi
tags:
- recursive-agents
- llm-tools
- code-generation
- software-architecture
- developer-tools
---

### TL;DR
The post describes **ypi**, a recursive coding agent built on Pi that adds a single `rlm_query` function plus a system prompt to let the model self-delegate work across nested child processes with isolated `jj` workspaces.

### Key Quote
“Pi already has a bash REPL. I added one function — rlm_query — and a system prompt that teaches Pi to use it recursively.”

### Summary
- **What ypi is**
  - ypi is a “recursive coding agent” described as **Pi that can call itself**.
  - The name references the **Y combinator** from lambda calculus, a fixed-point combinator associated with recursion.
  - It was inspired by **Recursive Language Models (RLM)**, which use an LLM with a code REPL and a `llm_query()` function to recursively break down problems and write code.

- **Core design**
  - Pi already has a **bash REPL**.
  - ypi adds:
    - a single function: **`rlm_query`**
    - a **system prompt** that instructs Pi to use recursion
  - Each child process gets its own **`jj` workspace** for file isolation.
  - The parent reviews work with **`jj diff`** and merges it with **`jj squash --from <child-change>`**.

- **Recursive structure**
  - **Depth 0 (root)**: full Pi with `bash + rlm_query`, default workspace
  - **Depth 1 (child)**: full Pi with `bash + rlm_query`, but in its own isolated `jj` workspace
  - **Depth 2 (leaf)**: full Pi with `bash`, but **no `rlm_query`** to cap recursion
  - Child agents can themselves call `rlm_query`, enabling nested decomposition.

- **Architecture mapping to Python RLM**
  - The post explicitly maps ypi’s pieces to the Python RLM library:
    - System prompt: `RLM_SYSTEM_PROMPT` → `SYSTEM_PROMPT.md`
    - Context / REPL: Python context variable → `$CONTEXT` file + bash
    - Sub-call function: `llm_query("prompt")` → `rlm_query "prompt"`
  - The author’s key insight is that **Pi’s bash tool is the REPL**, so `rlm_query` is effectively the recursive query mechanism without needing a separate bridge.

- **Guardrails / limits**
  - The author warns recursive agents can quickly burn API budget, so ypi includes controls:
    - `RLM_BUDGET=0.50` — max total spend
    - `RLM_TIMEOUT=60` — wall-clock time limit
    - `RLM_MAX_CALLS=20` — max `rlm_query` calls
    - `RLM_CHILD_MODEL=haiku` — cheaper model for child calls
    - `RLM_MAX_DEPTH=3` — recursion depth cap
    - `PI_TRACE_FILE=/tmp/trace.log` — logs calls, timing, and cost
  - The agent can inspect its own usage:
    - `rlm_cost`
    - `rlm_cost --json`

- **Development path**
  - The author says ypi went through four approaches before settling on the current bash-based design:
    1. **Tool-use REPL** — Pi’s `completeWithTools()` ReAct loop; achieved **77.6% on LongMemEval**
    2. **Python bridge** — HTTP server between Pi and Python RLM; too complex
    3. **Pi extension** — custom provider with search tools; not true recursion
    4. **Bash RLM** — `rlm_query` + `SYSTEM_PROMPT.md`; described as the version that stuck

- **How to try it**
  - Install via script:
    - `curl -fsSL https://raw.githubusercontent.com/rawwerks/ypi/master/install.sh | bash`
  - Install via npm/bun:
    - `npm install -g ypi`
    - `ypi "What does this repo do?"`
    - `bunx ypi "Refactor the error handling in this repo"`
  - The code is on **github.com/rawwerks/ypi** and is built on Pi, inspired by RLM.

### Assessment
This is a **mixed technical/project write-up** with a strong tutorial and architecture explanation component. Durability is **medium**: the conceptual pattern of recursive agent design is fairly durable, but the specific tooling (`Pi`, `jj`, environment variables like `RLM_*`, and install commands) is version- and project-specific. Density is **medium-high** because it includes concrete architecture, depth behavior, guardrails, command examples, and a development history. Originality is **primary source** since it appears to be the author’s own project description and design rationale, not an aggregation. It is best used as a **refer-back** reference if you care about the recursion pattern, implementation tradeoffs, or install commands; the scrape quality is **good** overall, with the main content, tables, and commands preserved.
