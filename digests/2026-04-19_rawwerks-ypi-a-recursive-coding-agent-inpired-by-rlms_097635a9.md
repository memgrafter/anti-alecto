---
url: https://github.com/rawwerks/ypi
title: 'rawwerks/ypi: A recursive coding agent inpired by RLMs'
scraped_at: '2026-04-19T07:28:22Z'
word_count: 1337
raw_file: raw/2026-04-19_rawwerks-ypi-a-recursive-coding-agent-inpired-by-rlms_097635a9.txt
tldr: ypi is a recursive coding agent built on Pi that lets the agent call itself via `rlm_query`, using separate `jj` workspaces, guardrails, and a system prompt to safely decompose and edit code.
key_quote: “`ypi` is Pi that can call itself.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- jj
- bash
- grep
- sed
- cat
- npm
- npx
- bunx
- curl
- git
libraries: []
companies:
- Pi
tags:
- recursive-agents
- code-generation
- developer-tools
- llm-architecture
- version-control
---

### TL;DR
`ypi` is a recursive coding agent built on Pi that lets the agent call itself via `rlm_query`, using separate `jj` workspaces, guardrails, and a system prompt to safely decompose and edit code.

### Key Quote
“`ypi` is Pi that can call itself.”

### Summary
- **What it is**
  - `ypi` is a recursive coding agent “inspired by Recursive Language Models (RLMs)” and built on [Pi](https://github.com/badlogic/pi-mono).
  - The name comes from the **Y combinator** in lambda calculus, emphasizing recursion.
  - It adds one function, **`rlm_query`**, plus a system prompt that teaches Pi to recursively delegate work.

- **Core mechanism**
  - Pi already has a **bash REPL**; `ypi` treats that as the execution environment.
  - A child agent is spawned with the same prompt/tools, enabling recursion:
    - **Depth 0**: root agent with `bash` + `rlm_query`
    - **Depth 1+**: child agents get their own isolated **`jj` workspace**
    - **Max depth** is bounded; the leaf can operate without further recursion
  - Child agents return patches or edits that the parent can absorb via `jj squash`.

- **Why the author says it works**
  - **Self-similarity**: every depth uses the same agent/prompt/tools; no special planner/scout roles.
  - **Self-hosting**: the system prompt contains the source of `rlm_query`, so the agent is effectively modifying its own recursion machinery.
  - **Bounded recursion**: termination is enforced with guardrails like depth limit, call limit, budget, timeout, and PATH scrubbing.
  - **Symbolic access**: data lives in files (`$CONTEXT`, `$RLM_PROMPT_FILE`) so the agent can use shell tools like `grep`, `sed`, and `cat` instead of relying on token memory.

- **Installation and usage**
  - Install options:
    - `npm install -g ypi`
    - `npx ypi "What does this repo do?"`
    - `bunx ypi "What does this repo do?"`
    - `curl -fsSL https://raw.githubusercontent.com/rawwerks/ypi/master/install.sh | bash`
    - manual clone + submodule init + `PATH` export
  - Run modes:
    - `ypi` for interactive use
    - `ypi "Refactor the error handling in this repo"` for one-shot use
    - model/provider can be changed, e.g. `ypi --provider anthropic --model claude-sonnet-4-5-20250929 ...`

- **Architecture compared to Python RLM**
  - `SYSTEM_PROMPT.md` corresponds to `RLM_SYSTEM_PROMPT`
  - `$CONTEXT` file + bash correspond to Python RLM’s context
  - `rlm_query "prompt"` corresponds to `llm_query("prompt")`

- **Guardrails / configuration**
  - `RLM_BUDGET=0.50` — total budget cap
  - `RLM_TIMEOUT=60` — wall-clock limit
  - `RLM_MAX_CALLS=20` — max recursive calls
  - `RLM_CHILD_MODEL=haiku` — cheaper sub-call model
  - `RLM_MAX_DEPTH=3` — recursion depth limit
  - `RLM_JJ=0` — disable workspace isolation
  - `RLM_JSON=0` — disable JSON mode / cost tracking
  - `PI_TRACE_FILE=/tmp/trace.log` — log calls, timing, cost
  - Cost can be queried with:
    - `rlm_cost`
    - `rlm_cost --json`

- **Pi compatibility notes**
  - Uses Pi’s native session history directory; child sessions share the same store with trace-encoded filenames.
  - Extensions are passed through unless disabled with `RLM_EXTENSIONS=0`.
  - System prompt is assembled into a temp file and passed via `--system-prompt` rather than inlining.
  - Child calls run non-interactively with `-p`.
  - Uses `--session` only when `RLM_SESSION_DIR` is set; otherwise `--no-session`.
  - Does not hardcode provider/model defaults unless the user sets `RLM_PROVIDER` or `RLM_MODEL`.

- **Repo structure**
  - `ypi` — launcher
  - `rlm_query` — recursive sub-call function
  - `SYSTEM_PROMPT.md` — recursion instructions
  - `AGENTS.md` — meta-instructions
  - `tests/` — unit, guardrail, and end-to-end tests
  - `pi-mono/` — Pi submodule
  - `README.md`

- **Version control / workflow**
  - The project uses **`jj`** instead of Git directly.
  - Commands like `jj status`, `jj describe`, `jj new`, `jj bookmark set master`, and `jj git push` are recommended.
  - It explicitly says: **never use `git add/commit/push` directly**.

- **Testing**
  - `make test-fast` — unit + guardrails
  - `make test-extensions` — extension compatibility
  - `make pre-push-checks` — local/CI gate
  - `make test-e2e` — real LLM calls, costs money
  - `make test` — all tests
  - `make install-hooks` — install push hooks
  - `make release-preflight`, `make land` — release/landing helpers
  - `make ci-status N=15`, `make ci-last-failure` — CI inspection helpers
  - The README warns that any change to `rlm_query` should be wrapped with `make test-fast` before and after, because it is a live dependency of the agent itself.

- **Development history**
  - The repo describes four attempts:
    1. Tool-use REPL with Pi’s `completeWithTools()` / ReAct loop
    2. Python bridge between Pi and Python RLM
    3. Pi extension with custom provider/search tools
    4. **Current approach**: bash-based RLM using `rlm_query` + `SYSTEM_PROMPT.md`
  - The author claims the final design is simpler because Pi’s bash tool already functions as the REPL.

- **Related projects**
  - Pi coding agent
  - Recursive Language Models (RLM)
  - `rlm-cli` (Python RLM CLI)

### Assessment
This is a **mixed** technical/reference README with tutorial elements. Durability is **medium**: the recursive-agent concept is fairly durable, but the concrete commands, model names, tests, and Pi compatibility details will age with the project and its dependencies. Density is **high** because it contains architecture, usage, guardrails, repo layout, testing, and workflow instructions in one place. Originality is **primary source** since it describes the project’s own design and implementation choices rather than summarizing others. Reference style is **refer-back**: useful for setup, implementation, and maintenance details, especially if working on the repo or evaluating the architecture. Scrape quality is **good**: the README content appears intact, including tables, code blocks, and section structure, with no obvious missing portions.
