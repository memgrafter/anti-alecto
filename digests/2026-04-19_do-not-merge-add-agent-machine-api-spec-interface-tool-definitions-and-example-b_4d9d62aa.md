---
url: https://github.com/memgrafter/flatagents/pull/8
title: '[do not merge] Add Agent Machine API: spec interface, tool definitions, and example by memgrafter · Pull Request #8 · memgrafter/flatagents'
scraped_at: '2026-04-19T07:12:48Z'
word_count: 5512
raw_file: raw/2026-04-19_do-not-merge-add-agent-machine-api-spec-interface-tool-definitions-and-example-b_4d9d62aa.txt
tldr: This pull request adds a cross-SDK “Machine API” that lets an agent in a `tool_loop` control its own FlatMachine runtime through standard function-call tools like launching child machines, inspecting checkpoints, reading/writing context, and sending signals.
key_quote: “An agent running inside a tool_loop state can call these operations to introspect its own runtime, launch child machines, inspect their state, and coordinate via signals — all without SDK-specific code.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Claude
tools: []
libraries: []
companies:
- Anthropic
tags:
- agents
- machine-orchestration
- tool-calling
- yaml-schema
- sdk-design
---

### TL;DR
This pull request adds a cross-SDK “Machine API” that lets an agent in a `tool_loop` control its own FlatMachine runtime through standard function-call tools like launching child machines, inspecting checkpoints, reading/writing context, and sending signals.

### Key Quote
“An agent running inside a tool_loop state can call these operations to introspect its own runtime, launch child machines, inspect their state, and coordinate via signals — all without SDK-specific code.”

### Summary
- **What changed**
  - Introduces a new `MachineAPI` interface in `flatagents-runtime.d.ts`.
  - Adds `machine_api?: MachineAPI` to `SDKRuntimeWrapper`.
  - Documents the pattern in `MACHINES.md`.

- **Core idea**
  - An agent in a `tool_loop` can act as an orchestrator over its own runtime.
  - It can:
    - `contextRead()` / `contextWrite()` its own machine context
    - `runtimeInfo()` discover available machines and agents
    - `launch()` child machines fire-and-forget
    - `invoke()` child machines and wait for results
    - `status()` poll launched executions
    - `inspect()` inspect checkpoints and runtime state
    - `signalSend()` wake paused machines through channels

- **Cross-SDK design**
  - Tool schemas are defined in **YAML** so the same tool contract survives across Python, JS, Rust, Go, Java, and C/C++.
  - Each SDK is expected to implement `MachineAPIToolProvider` against its own runtime primitives.

- **Tool set defined**
  - `context_read`
  - `context_write`
  - `runtime_info`
  - `machine_launch`
  - `machine_invoke`
  - `machine_status`
  - `machine_inspect`
  - `signal_send`

- **Example added**
  - A full working example lives in `sdk/examples/agent_machine_api/`.
  - It includes:
    - an **orchestrator** agent
    - an **echo** target machine
    - a **writer-critic** target machine that loops until a tagline scores at least 8 or hits max rounds

- **Example machine behavior**
  - `orchestrator-machine` has a `tool_loop` with:
    - `max_turns: 20`
    - `max_tool_calls: 50`
    - `max_cost: 5.00`
    - `tool_timeout: 120`
    - `total_timeout: 600`
  - It exposes `echo` and `writer_critic` as launchable child machines.
  - Context tracks:
    - `task`
    - `launched_machines`
    - `results`

- **Python reference implementation**
  - `hooks.py` wires the tool provider into the machine runtime.
  - `tools.py` implements the Machine API over FlatMachine internals.
  - `main.py` is a runnable entry point with REPL and single-task modes.
  - The implementation uses internal runtime fields like:
    - `_machine._invoker`
    - `_machine.result_backend`
    - `_machine.persistence`
    - `_machine._signal_backend`

- **Notable implementation details**
  - `machine_launch` appends launched execution IDs to `context.launched_machines`.
  - `machine_invoke` stores completed outputs in `context.results`.
  - `machine_status` checks the result backend first, then falls back to the latest checkpoint snapshot.
  - `machine_inspect` returns a fuller snapshot, truncating large tool-loop chains for readability.
  - `signal_send` requires a configured signal backend.

### Assessment
This is a **mixed** technical/reference + implementation pull request with high durability at the design level but medium durability in the concrete API surface, since it is tied to `spec_version: "2.0.0"` and internal runtime details that may evolve. The content is **dense** and fairly rich in specifics: exact tool names, YAML schemas, config files, execution flow, and Python reference code are all included. It appears to be **primary source** material from the repository, not commentary or synthesis. As a reference, it is best used **refer-back** rather than deep-study unless you want to implement or extend the pattern. Scrape quality is **good**: the patch content, docs, and example files are present, though any behavior depending on omitted surrounding repo context or runtime internals may still require the full repository to verify.
