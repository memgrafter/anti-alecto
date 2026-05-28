---
url: https://www.npmjs.com/package/@memgrafter/flatagents
title: '@memgrafter/flatagents - npm'
scraped_at: '2026-04-12T07:39:19Z'
word_count: 783
raw_file: raw/2026-04-12_memgrafter-flatagents-npm_31d556a5.txt
tldr: A compact npm reference for the `@memgrafter/flatagents` ecosystem that defines FlatAgents (single-call LLM agents) and FlatMachines (state-machine orchestration), including profiles, backend selection, state fields, signaling, persistence, hooks, distributed workers, and SDK install notes.
key_quote: 'FlatAgent: Single LLM call. Model + prompts + output schema. No orchestration.'
durability: high
content_type: reference
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people: []
tools:
- npm
- SSE
- SQLite
- launchd
- systemd
libraries:
- '@memgrafter/flatagents'
- flatagents
- flatmachines
- litellm
- aisuite
companies:
- Anthropic
- Cerebras
- DynamoDB
tags:
- llm-agents
- state-machines
- workflow-orchestration
- signal-handling
- persistence
---

### TL;DR
A compact npm reference for the `@memgrafter/flatagents` ecosystem that defines FlatAgents (single-call LLM agents) and FlatMachines (state-machine orchestration), including profiles, backend selection, state fields, signaling, persistence, hooks, distributed workers, and SDK install notes.

### Key Quote
"FlatAgent: Single LLM call. Model + prompts + output schema. No orchestration."

### Summary
- This package is presented as a **FlatAgents + FlatMachines reference**, optimized to stay under 1000 tokens and pointing readers to `flatagent.d.ts`, `flatmachine.d.ts`, and `profiles.d.ts` for schemas.
- **Versioning** is lockstep across specs and SDKs.

#### Core concepts
- **FlatAgent**:
  - A single LLM call.
  - Includes model, prompts, and output schema.
  - No orchestration.
- **FlatMachine**:
  - A state machine that orchestrates agents.
  - Supports states, transitions, conditions, loops, and error handling.
- Guidance:
  - Single LLM call → `FlatAgent`
  - Multi-step / branching / retry / errors → `FlatMachine`
  - Parallel execution → `machine: [a, b, c]`
  - Dynamic parallelism → `foreach`
  - Background tasks → `launch`

#### Model profiles
- Agents can reference profiles by name through `profiles.yml`.
- Example profiles:
  - `fast`: `provider: cerebras`, `name: zai-glm-4.6`, `temperature: 0.6`
  - `smart`: `provider: anthropic`, `name: claude-3-opus-20240229`
- `default` can be set to a profile, with `override` forcing all models.
- Agent model field can be:
  - `"fast"`
  - `{ profile: "fast", temperature: 0.9 }`
  - `{ provider: x, name: y }`
- Resolution order: **default → profile → overrides → override**

#### Codex backend behavior
- `backend: codex` is **explicit-only** and never auto-detected.
- Backend precedence:
  1. constructor backend
  2. resolved model.backend
  3. auto-detect (`litellm` / `aisuite` only)
- OAuth settings are taken from the resolved model config, whether the model came from inline agent config or from a profile.
- Auth file precedence:
  1. `oauth.auth_file`
  2. legacy `codex_auth_file`
  3. legacy `auth.auth_file`
  4. `FLATAGENTS_CODEX_AUTH_FILE`
  5. `~/.pi/agent/auth.json`
- Token handling:
  - refresh before request when expired
  - if refresh fails, re-read auth store once for cross-process refresh
  - fallback refresh + retry on `401/403`
- Transport:
  - SSE only
  - retries on `429/500/502/503/504`
  - exponential backoff, no jitter

#### Agent references
- `data.agents` values may be:
  - string path to a flatagent config
  - inline flatagent config (`spec: flatagent`)
  - typed adapter ref:
    - `{ type: "flatagent" | "smolagents" | "pi-agent", ref?: "...", config?: {...} }`

#### State fields
- `type`: `initial` (entry) or `final` (exit + output)
- `agent`: agent to call
- `machine`: machine(s), either string or array for parallel
- `foreach`: array expression for dynamic parallelism, with `item` as variable and `key` as result key
- `launch` / `launch_input`: fire-and-forget machines
- `input`: map input to agent/machine
- `output_to_context`: map `output.*` to `context.*`
- `execution`: retry/parallel/mdap settings
- `on_error`: state name or typed mapping
- `transitions`: conditional transitions, with last unconditioned transition as default
- `mode`: `settled` (all) or `any` (first) for parallel
- `wait_for`: external signal channel, as a Jinja2 template
- `timeout`: seconds, with `0` meaning forever

#### Patterns and execution modes
- Execution types:
  - `default`
  - `retry` with backoffs and jitter
  - `parallel` with `n_samples`
  - `mdap_voting` with `k_margin` and `max_candidates`
- Transitions:
  - conditions like `"context.score >= 8"`
  - final transition without condition acts as default
- Loops:
  - transition to the same state
  - machine has a `max_steps` safety limit
- Error handling:
  - `on_error` can route to a single state or per error type
  - `context` receives `last_error` and `last_error_type`

#### Parallel, foreach, launch, and wait patterns
- Parallel machines:
  - `machine: [review_a, review_b]`
  - results keyed by machine name
  - `mode: settled` or `any`
- Foreach:
  - `foreach: "{{ context.items }}"`
  - `as: item`
  - `machine: processor`
- Launch / fire-and-forget:
  - `launch: background_task`
  - `launch_input: { data: "{{ context.data }}" }`
- Wait for signal:
  - machine pauses at a `wait_for` state
  - checkpoints are created with `waiting_channel`
  - process exits while nothing is running
  - later signal resumes the machine from checkpoint

#### Distributed worker pattern
- Built with hook actions such as `DistributedWorkerHooks` plus a `RegistrationBackend` and `WorkBackend`.
- Core machines:
  - **Checker**: `get_pool_state → calculate_spawn → spawn_workers`
  - **Worker**: `register_worker → claim_job → process → complete_job/fail_job → deregister_worker`
  - **Reaper**: `list_stale_workers → reap_stale_workers`
- `spawn_workers` expects `worker_config_path` in context, unless hooks resolve it.
- Custom queues can extend base hooks with extra actions.
- A sample context and state setup is shown, and the docs point to `sdk/examples/distributed_worker/` for a full example.

#### Signals and triggers
- Machines pause at `wait_for` states and checkpoint with a `waiting_channel`.
- External processes deliver signals that trigger resumption.
- Example flow:
  - `send("approval/task-001", {approved: true})`
  - writes to SQLite and touches a trigger file
  - launchd/systemd starts a dispatcher
  - dispatcher queries matching checkpoints
  - machine resumes with signal data as `output.*`
- Channel semantics:
  - **Addressed**: one waiter
  - **Broadcast**: multiple waiters, with dispatcher controlling limits
- Scale claim:
  - 10,000 waiting machines = 10,000 SQLite rows, with zero processes and zero memory
- Backends:
  - trigger: `none`, `file`, `socket`, or DynamoDB Streams implicitly
  - signal: `memory`, `sqlite`, `dynamodb`

#### Context variables
- Available variables:
  - `context.*` in all states
  - `input.*` initially
  - `output.*` in `output_to_context`
  - `item` / `as` in `foreach`

#### Hooks
- Supported lifecycle hooks:
  - `on_machine_start`
  - `on_machine_end`
  - `on_state_enter`
  - `on_state_exit`
  - `on_transition`
  - `on_error`
  - `on_action`
- Example hook behavior:
  - `on_action` can intercept actions like `"fetch"` and inject results into context

#### Persistence
- Persistence can be enabled with:
  - `backend: local`
  - `backend: memory`
  - `backend: sqlite`
- SQLite backend:
  - durable
  - single-file
  - no external dependencies
  - optional `db_path`, defaulting to `flatmachines.sqlite`
- It auto-selects `SQLiteLeaseLock` and `SQLiteConfigStore`, so no runner injection is needed.
- Machines can resume with `machine.execute(resume_from=execution_id)`.

#### SDKs
- Python:
  - `flatagents[litellm]` for agents
  - `flatmachines[flatagents]` for orchestration
- JavaScript:
  - one JS SDK under `sdk/js`
  - follows the same specs
  - not yet split into separate FlatAgents / FlatMachines packages

### Assessment
This is a high-density, reference-style package description with strong durability for the underlying architecture concepts, though some specifics like backend behavior, auth precedence, and SDK packaging are likely to change over time as the project evolves. The content type is mixed but mostly reference, with some tutorial-like configuration examples. It appears to be a synthesis/reference doc rather than original explanatory prose, and it’s best used as a refer-back resource when working with FlatAgents/FlatMachines schemas or runtime behavior. Scrape quality is good for a short package description: the main text and examples are captured, though this likely omits linked schema files and any deeper docs or code examples.
