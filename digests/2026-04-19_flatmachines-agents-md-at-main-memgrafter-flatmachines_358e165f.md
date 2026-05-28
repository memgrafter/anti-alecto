---
url: https://github.com/memgrafter/flatmachines/blob/main/AGENTS.md
title: flatmachines/AGENTS.md at main · memgrafter/flatmachines
scraped_at: '2026-04-19T07:55:43Z'
word_count: 1055
raw_file: raw/2026-04-19_flatmachines-agents-md-at-main-memgrafter-flatmachines_358e165f.txt
tldr: This document is a compact reference for the FlatAgents/FlatMachines ecosystem, defining how to build single-call agents versus state-machine orchestrations, how model profiles and OAuth backends resolve, and the hard rules for portable, non-fragile LLM pipelines.
key_quote: “**Never truncate** LLM inputs/outputs silently.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- git
libraries:
- flatagents
- flatmachines
companies:
- Anthropic
- Cerebras
tags:
- llm-orchestration
- state-machines
- model-profiles
- oauth-backends
- persistence
---

### TL;DR
This document is a compact reference for the FlatAgents/FlatMachines ecosystem, defining how to build single-call agents versus state-machine orchestrations, how model profiles and OAuth backends resolve, and the hard rules for portable, non-fragile LLM pipelines.

### Key Quote
“**Never truncate** LLM inputs/outputs silently.”

### Summary
- **Purpose and scope**
  - LLM-optimized reference (`<1000 tokens`) for `flatagent.d.ts`, `flatmachine.d.ts`, and `profiles.d.ts`.
  - States that **all specs and SDKs use lockstep versioning**.

- **Core concepts**
  - **FlatAgent** = one LLM call with model, prompts, and output schema; no orchestration.
  - **FlatMachine** = state machine that orchestrates agents with states, transitions, loops, retries, and error handling.
  - Usage guide:
    - Single LLM call → FlatAgent
    - Multi-step / branching / retry / errors → FlatMachine
    - Parallel execution → `machine: [a, b, c]`
    - Dynamic parallelism → `foreach`
    - Background tasks → `launch`

- **Model profiles**
  - Profiles are defined in `profiles.yml` with `spec: flatprofiles` and version `2.7.0`.
  - Example profiles:
    - `fast`: Cerebras `zai-glm-4.6`, temperature `0.6`
    - `smart`: Anthropic `claude-3-opus-20240229`
  - A model can be referenced by:
    - profile name string (`"fast"`)
    - profile override object (`{ profile: "fast", temperature: 0.9 }`)
    - direct provider/name object (`{ provider: x, name: y }`)
  - Resolution order: **default → profile → overrides → override**.

- **OAuth backends for Codex / Copilot**
  - `backend: codex` and `backend: copilot` are **explicit-only** and never auto-detected.
  - Backend precedence:
    1. constructor `backend`
    2. resolved `model.backend`
    3. auto-detect (only for `litellm/aisuite`)
  - OAuth settings come from the resolved model config, whether from inline config or profile.
  - Auth file precedence is listed separately for Codex and Copilot, with environment variable fallbacks and default paths.
  - Token handling includes:
    - pre-request refresh on expiry
    - one reread of the auth store for cross-process refresh
    - fallback refresh + retry on `401/403`
  - Retries apply to `429/500/502/503/504` with exponential backoff and **no jitter**.

- **Agent references**
  - `data.agents` can point to:
    - a string path to a flatagent config
    - an inline `spec: flatagent` config
    - a typed adapter reference (`flatagent`, `smolagents`, `pi-agent`)

- **LLM I/O and formatting rules**
  - Default handoffs between LLM stages should be **plain text/Markdown**.
  - Avoid JSON/Jinja-shaped model-to-model output unless a strict schema or boundary requires it.
  - Reasons given: JSON/Jinja handoffs increase parse fragility and token overhead.
  - Keep `input` and `output_to_context` mappings explicit and shallow.
  - Heavy transforms should happen only at boundary actions like final save/write steps.
  - Preserve full source text across stages; do not silently truncate.
  - Jinja used in config must be portable across SDKs:
    - use property access, comparisons, simple conditionals
    - avoid Python-specific features like `.items()`, `|tojson`, `len()`, `isinstance()`, list comprehensions
  - Every transform must have a one-line justification or be removed.

- **State fields**
  - Documents the main machine state keys and what each does:
    - `type` (`initial` / `final`)
    - `agent`
    - `machine`
    - `foreach`
    - `launch` / `launch_input`
    - `input`
    - `output_to_context`
    - `execution`
    - `on_error`
    - `transitions`
    - `mode`
    - `wait_for`
    - `timeout`

- **Patterns**
  - Execution types:
    - `default`
    - `retry` with backoffs/jitter
    - `parallel` with `n_samples`
    - `mdap_voting` with `k_margin` and `max_candidates`
  - Transitions use conditions like `context.score >= 8`, with the last unconditional transition as default.
  - Loops are represented by transitions back to the same state, with `max_steps` as safety.
  - Error handling can be global or per-type; `context` gets `last_error` and `last_error_type`.
  - Examples included for:
    - parallel machines (`mode: settled` or `any`)
    - `foreach`
    - `launch`
    - `wait_for` approval/resume flow

- **Distributed worker pattern**
  - Describes building worker pools using hooks plus `RegistrationBackend` and `WorkBackend`.
  - Core machine roles:
    - **Checker**: `get_pool_state` → `calculate_spawn` → `spawn_workers`
    - **Worker**: register, claim job, process, complete/fail, deregister
    - **Reaper**: list and reap stale workers
  - Notes that `spawn_workers` expects `worker_config_path` in context unless hooks override resolution.
  - Points to `sdk/examples/distributed_worker/` for a full example.

- **Signals and triggers**
  - `wait_for` states checkpoint the machine and exit; no process remains running.
  - External signal delivery resumes machines via dispatcher and checkpoint lookup.
  - Explains addressed vs broadcast channels and notes that 10,000 waiting machines are just 10,000 SQLite rows, not active processes.
  - Trigger backends:
    - `none` (polling)
    - `file` (launchd/systemd)
    - `socket` (UDS, in-process)
    - DynamoDB Streams is implicit
  - Signal backends:
    - `memory`
    - `sqlite`
    - `dynamodb`

- **Context variables**
  - Clarifies where variables come from:
    - `context.*` everywhere
    - `input.*` in initial input
    - `output.*` in `output_to_context`
    - `item` / `as` in `foreach`

- **Hooks**
  - Lists lifecycle hooks:
    - `on_machine_start`
    - `on_machine_end`
    - `on_state_enter`
    - `on_state_exit`
    - `on_transition`
    - `on_error`
    - `on_action`
  - Includes a short Python example overriding `on_action`.

- **Persistence**
  - Persistence can be enabled with `local`, `memory`, or `sqlite`.
  - SQLite is emphasized as durable, single-file, and dependency-free.
  - Defaults to `flatmachines.sqlite` if `db_path` is omitted.
  - Auto-selects `SQLiteLeaseLock` and `SQLiteConfigStore`.
  - Resume is done with `machine.execute(resume_from=execution_id)`.

- **SDKs**
  - Python:
    - `flatagents` via `pip install flatagents[litellm]`
    - `flatmachines` via `pip install flatmachines[flatagents]`
  - JavaScript:
    - single SDK under `sdk/js`
    - same specs, not yet split into separate FlatAgents/FlatMachines packages

### Assessment
This is a high-density **reference** document with medium-to-high durability: the conceptual model and orchestration patterns are fairly timeless, but some details are version-sensitive (notably `spec_version: 2.7.0`, package names, backend behaviors, and specific model/profile examples). It is a **mixed** technical spec/reference rather than tutorial prose, and appears to be a **primary source** for the project’s conventions. It’s best used as a **refer-back** card for implementation details like state fields, backend precedence, persistence, and signal handling. Scrape quality looks **good** overall: the content is complete and structured, with code blocks and tables preserved, though any linked external files (`flatagent.d.ts`, `flatmachine.d.ts`, examples) are only referenced, not included.
