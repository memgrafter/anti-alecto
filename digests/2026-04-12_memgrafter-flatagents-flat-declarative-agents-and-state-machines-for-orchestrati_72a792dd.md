---
url: https://github.com/memgrafter/flatagents
title: 'memgrafter/flatagents: Flat, declarative agents and state machines for orchestrating LLMs.'
scraped_at: '2026-04-12T07:28:49Z'
word_count: 885
raw_file: raw/2026-04-12_memgrafter-flatagents-flat-declarative-agents-and-state-machines-for-orchestrati_72a792dd.txt
tldr: You write YAML that describes states, transitions, and agents; the runtime handles retries, parallelism, checkpointing, error recovery, and distributed workers.
key_quote: Your Python code stays small.
durability: medium
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
- litellm
companies:
- GitHub
- OpenAI
tags:
- llm-orchestration
- state-machines
- yaml-config
- agent-frameworks
- distributed-systems
---

### TL;DR
FlatMachines/flatagents is a YAML-driven framework for orchestrating LLM agents as state machines, with built-in retries, checkpointing, persistence, parallelism, and distributed workers, though the repo warns it’s still a “product of its times” and recommends the Python SDK first.

### Key Quote
“Your Python code stays small.”

### Summary
- **What this repository is**
  - A GitHub repo for **memgrafter/flatagents** / **FlatMachines**: “flat, declarative agents and state machines for orchestrating LLMs.”
  - The core idea is to define **agents, states, transitions, and orchestration behavior in YAML**, while the runtime handles execution concerns.
  - It supports **checkpoint/restore, persistence, retries, parallelism, error recovery, and distributed workers**.
  - The repo explicitly warns: **“Caveat emptor”** and says to **prefer the Python SDK for now**, not JS or Rust.

- **Main design philosophy**
  - Agent behavior is controlled by editing **YAML config**, rather than refactoring Python code.
  - The runtime manages:
    - retries and backoff
    - error routing
    - state transitions
    - parallelism
    - distributed execution
  - It positions itself as **“batteries included”** for orchestration.

- **Quick start / usage**
  - Recommended entry point: the **`helloworld` example** in `sdk/examples/helloworld/python`.
  - Basic run flow:
    - set `OPENAI_API_KEY`
    - run `./run.sh`
  - For a fresh project:
    - `pip install flatmachines[flatagents] flatagents[litellm]`
  - The demo uses **three YAML files**:
    - `profiles.yml` for model catalog
    - `agent.yml` for a single LLM call
    - `machine.yml` for orchestration

- **Example configuration structure**
  - `profiles.yml`
    - defines model profiles like `fast` and `quality`
    - uses OpenAI models such as `gpt-5-mini` and `gpt-5`
    - allows a default profile and optional override
  - `agent.yml`
    - defines a `flatagent`
    - uses `profile: fast`
    - instructs the model to output exactly one character
    - references inputs like `{{ input.target }}` and `{{ input.current }}`
  - `machine.yml`
    - defines a `flatmachine`
    - keeps `context.target` and `context.current`
    - uses states:
      - `start` (initial)
      - `build_char` (agent execution with retry/backoff)
      - `append_char` (action)
      - `done` (final)
    - routes based on comparisons like whether the current string matches the target
    - captures agent output into context fields such as `expected_char` and `last_output`

- **Python runtime example**
  - `run.py` shows how to:
    - configure logging
    - create a custom `HelloWorldHooks` class extending `LoggingHooks`
    - mutate context in `on_action` when `append_char` runs
    - register hooks with `HooksRegistry`
    - create a `FlatMachine` from `config/machine.yml`
    - execute it with `input={"target": "Hello, World!"}`
  - The example logs the final result and success flag.

- **Versioning**
  - The project uses **lockstep versioning**: one version number applies across the entire repository and its SDKs/specs.

- **Examples listed**
  - The repo advertises many runnable examples under `./sdk/examples`, including:
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
  - These examples suggest the framework targets both **agent workflows** and more general **machine/orchestration patterns**.

- **Specs and source of truth**
  - TypeScript definitions are the authoritative schema:
    - `flatagent.d.ts`
    - `flatmachine.d.ts`
    - `profiles.d.ts`
    - `flatagents-runtime.d.ts`
  - `flatagents-runtime.d.ts` defines backend configuration categories such as:
    - persistence
    - locking
    - results
    - registration
    - work
    - signal
    - trigger
  - Allowed backend values include combinations like:
    - `memory`, `local`, `sqlite`, `redis`, `postgres`, `s3`, `dynamodb`
    - trigger values `none`, `file`, `socket`

- **SDK status**
  - Python agents: `pip install flatagents[litellm]` — **Stable**
  - Python machines: `pip install flatmachines[flatagents]` — **Stable**
  - JavaScript SDK: `sdk/js` — **In progress**

- **Logging and metrics**
  - Logging setup example:
    - `from flatmachines import setup_logging`
    - `setup_logging(level="INFO")`
  - Environment variables include:
    - `FLATAGENTS_LOG_LEVEL`
    - `FLATAGENTS_LOG_FORMAT`
    - `FLATAGENTS_METRICS_ENABLED`
    - `OTEL_METRICS_EXPORTER`
  - Metrics are described as OpenTelemetry-based, with console or OTLP export.

### Assessment
This is a **mixed reference/tutorial** repository with fairly high informational density because it combines a product overview, setup instructions, schema references, runtime contract details, and a catalog of examples. Durability is **medium**: the conceptual model of YAML-driven LLM orchestration is fairly stable, but several details are tied to current SDK status, versioning, and specific model names like `gpt-5-mini` and `gpt-5`, which may age quickly. Content originality is **primary source** for the project’s own design and API, though it also functions as a documentation hub. It’s best used as **refer-back** material if you plan to adopt the framework or need to locate the example or schema that matches a particular orchestration pattern. Scrape quality is **good**: the major sections, code blocks, examples, and spec summaries are present, though any deeper implementation details, linked example contents, or file-level nuances are not included here.
