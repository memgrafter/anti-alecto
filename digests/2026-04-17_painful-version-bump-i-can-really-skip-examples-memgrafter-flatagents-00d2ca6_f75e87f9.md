---
url: https://github.com/memgrafter/flatagents/commit/00d2ca6257ad529b2f5a0b6f8d759788fa1a44c2#diff-c14d0436e722e453e95d3602f7e37ea97c05e32f03cea34681760a69fcf7a100
title: painful version bump, i can really skip examples... · memgrafter/flatagents@00d2ca6
scraped_at: '2026-04-17T05:22:46Z'
word_count: 885
raw_file: raw/2026-04-17_painful-version-bump-i-can-really-skip-examples-memgrafter-flatagents-00d2ca6_f75e87f9.txt
tldr: You write YAML that describes states, transitions, and agents. The runtime handles retries, parallelism, checkpointing, error recovery, and distributed workers. Your Python code stays small.
key_quote: You write YAML that describes states, transitions, and agents. The runtime handles retries, parallelism, checkpointing, error recovery, and distributed workers.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries:
- flatmachines
- flatagents
- litellm
companies:
- FlatMachines
- FlatAgents
tags:
- agent-orchestration
- state-machines
- yaml-config
- checkpointing
- distributed-systems
---

### TL;DR
This README introduces FlatMachines/FlatAgents as a YAML-driven agent orchestration framework with checkpointing, retries, parallelism, distributed workers, and a set of runnable examples, while noting the Python SDK is the most mature path for now.

### Key Quote
“You write YAML that describes states, transitions, and agents. The runtime handles retries, parallelism, checkpointing, error recovery, and distributed workers.”

### Summary
- **What this is**
  - Project docs for **FlatMachines / FlatAgents**, described as orchestrating agents with a **peer network of state machines**.
  - Emphasizes **checkpoint/restore, persistence, distributed workers, error recovery, and batteries included**.
  - Says users can bring their own CLI or agent, or use FlatAgents via API.

- **Maturity / caveat**
  - Strong warning that the repo is “a product of its times.”
  - Explicitly recommends the **Python SDK** for now, and says **JS and Rust are not yet preferred**.
  - Points readers to `./sdk/examples/` to get started.
  - For machine readers, it references `AGENTS.md` as a compact reference.

- **Core idea**
  - The system is built around **YAML configs** that define:
    - **profiles.yml**: model catalog / model profiles
    - **agent.yml**: a single LLM agent
    - **machine.yml**: orchestration logic / state machine
  - The runtime handles the operational concerns:
    - retries
    - error routing
    - state
    - parallelism
    - checkpointing
    - distributed workers
  - The pitch is that you can change behavior by editing YAML rather than refactoring Python.

- **Quick start**
  - Fastest demo path:
    - set `OPENAI_API_KEY`
    - run the `helloworld` example from `sdk/examples/helloworld/python`
    - `./run.sh` sets up the venv, installs deps, and runs
  - For a fresh project, install:
    - `pip install flatmachines[flatagents] flatagents[litellm]`

- **Example configuration shown**
  - `profiles.yml`
    - defines `fast` and `quality` OpenAI profiles
    - `fast` uses `gpt-5-mini` with `max_tokens: 2048`
    - `quality` uses `gpt-5` with `max_tokens: 4096`
    - `default: fast`
    - optional `override: quality`
  - `agent.yml`
    - agent named `hello-world-agent`
    - uses model profile `fast`
    - system prompt instructs the model to output **exactly one character**, no explanation
    - user prompt passes in `target` and `current`
  - `machine.yml`
    - machine named `hello-world-loop`
    - context tracks `target` and `current`
    - defines one agent `builder`
    - uses `hello-world-hooks`
    - states:
      - `start`: initial state; if `current == target`, go to `done`, otherwise go to `build_char`
      - `build_char`: invokes the agent with retry/backoff settings (`backoffs: [2, 8, 16, 35]`, `jitter: 0.1`)
      - stores `expected_char` and `last_output` in context
      - transitions either to `append_char` when the output matches the expected char, or loops back to `build_char`
      - `append_char`: action-based state that appends a character via hook logic
      - `done`: final state returning `result` and `success: true`
  - `run.py`
    - sets up logging
    - registers `HelloWorldHooks`
    - hook `on_action` appends the first character from `last_output` when action is `append_char`
    - runs the machine with input `{"target": "Hello, World!"}` and `max_agent_calls=20`
    - logs result and success

- **Versioning**
  - States that **all specs and SDKs use lockstep versioning**: one version number applies across the whole repo.
  - The example configs use `spec_version: "2.6.0"`.

- **Examples catalog**
  - Lists runnable examples in `sdk/examples`, including:
    - `helloworld`
    - `writer_critic`
    - `parallelism`
    - `error_handling`
    - `human-in-the-loop`
    - `distributed_worker`
    - `coding_agent_cli`
    - `research_paper_analysis`
    - `multi_paper_synthesizer`
    - `character_card`
    - `support_triage_json`
    - `story_writer`
    - `dfss_deepsleep`
    - `dfss_pipeline`
    - `dynamic_agent`
    - `gepa_self_optimizer`
    - `listener_os`
    - `mdap`
    - `peering`
    - `rlm`
  - Each example is paired with a short description of the pattern it demonstrates.

- **Specs and source of truth**
  - Says **TypeScript definitions are the source of truth**.
  - Key schema files:
    - `flatagent.d.ts` — agent config schema
    - `flatmachine.d.ts` — machine config schema
    - `profiles.d.ts` — model profile schema
    - `flatagents-runtime.d.ts` — runtime interfaces and backend config contract
  - `BackendConfig` runtime categories and values are listed:
    - `persistence`: memory/local/sqlite/redis/postgres/s3/dynamodb
    - `locking`: none/local/sqlite/redis/consul/dynamodb
    - `results`: memory/redis/dynamodb
    - `registration`: memory/sqlite/redis/dynamodb
    - `work`: memory/sqlite/redis/dynamodb
    - `signal`: memory/sqlite/redis/dynamodb
    - `trigger`: none/file/socket

- **SDK status**
  - Python agent SDK: `pip install flatagents[litellm]` — **Stable**
  - Python machine SDK: `pip install flatmachines[flatagents]` — **Stable**
  - JavaScript SDK in `sdk/js` — **In progress**

- **Logging and metrics**
  - Shows how to enable logging with `setup_logging(level="INFO")`
  - Environment variables documented:
    - `FLATAGENTS_LOG_LEVEL` default `INFO`
    - `FLATAGENTS_LOG_FORMAT` default `standard`
    - `FLATAGENTS_METRICS_ENABLED` default `true`
    - `OTEL_METRICS_EXPORTER` default `console`, with `otlp` for production

### Assessment
Durability is **medium**: the architectural ideas around state-machine-based agent orchestration, retries, checkpoints, and human-in-the-loop workflows are fairly durable, but the document is tied to specific repo versions, SDK status, example paths, and model names like `gpt-5-mini` / `gpt-5`, which may age quickly. The content type is **mixed**—part reference, part tutorial, part product announcement. Density is **high** because it includes concrete YAML schemas, Python code, install commands, version numbers, backend options, and example catalogs. Originality is mainly **primary source** documentation from the project maintainers, not a synthesis. It is best used as **refer-back** material, especially when setting up configs or checking schema/API details. Scrape quality is **good** overall: the main README content, code blocks, tables, and example listings are present, though any linked files like `AGENTS.md` or the example directories themselves are not included here.
