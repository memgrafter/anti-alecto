---
url: https://github.com/memgrafter/flatmachines/releases/tag/mk42_dev-0.1.0-20260418T183530Z-6c1b12681440
title: Release mk42_dev-0.1.0-20260418T183530Z-6c1b12681440 · memgrafter/flatmachines
scraped_at: '2026-04-19T08:05:44Z'
word_count: 906
raw_file: raw/2026-04-19_release-mk42-dev-0-1-0-20260418t183530z-6c1b12681440-memgrafter-flatmachines_a25df1be.txt
tldr: FlatMachines is a YAML-driven framework for orchestrating LLM agents as state machines, with built-in retries, parallelism, checkpointing, persistence, and distributed execution, with Python currently the recommended SDK.
key_quote: You write YAML that describes states, transitions, and agents. The runtime handles retries, parallelism, checkpointing, error recovery, and distributed workers.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- pi-mono
tools:
- flatmachines
- flatagents
- litellm
- OpenAI
companies:
- memgrafter
- GitHub
tags:
- llm-orchestration
- state-machines
- yaml-config
- agent-frameworks
- distributed-systems
---

### TL;DR
FlatMachines is a YAML-driven framework for orchestrating LLM agents as state machines, with built-in retries, parallelism, checkpointing, persistence, and distributed execution, with Python currently the recommended SDK.

### Key Quote
"You write YAML that describes states, transitions, and agents. The runtime handles retries, parallelism, checkpointing, error recovery, and distributed workers."

### Summary
- **What this release/page is**
  - GitHub release page for `memgrafter/flatmachines`, specifically tag `mk42_dev-0.1.0-20260418T183530Z-6c1b12681440`.
  - Describes **FlatMachines**, a framework for orchestrating agents with a **peer network of state machines**.
  - Positions the project as “batteries included” with support for **checkpoint/restore**, **persistence**, and distributed workers.

- **Core idea**
  - Users define workflows in **YAML** rather than hardcoding orchestration logic in Python.
  - The runtime manages:
    - retries
    - parallelism
    - checkpointing
    - error routing/recovery
    - distributed workers
  - The page emphasizes that behavior changes by editing YAML, not by refactoring Python code.

- **Caveats / positioning**
  - The page warns: “this repo is a product of its times. Caveat emptor.”
  - It recommends the **Python SDK** for now, and says **JS and Rust are not yet preferred/mature**.
  - For LLM/machine readers, it points to `AGENTS.md` as a compact reference.

- **Quick start**
  - Fastest path is to run the **helloworld** example:
    - `cd sdk/examples/helloworld/python`
    - `./run.sh`
  - For a fresh project, install:
    - `pip install flatmachines[flatagents] flatagents[litellm]`
  - The demo uses three config files:
    - `profiles.yml` — model catalog / profiles
    - `agent.yml` — single LLM call
    - `machine.yml` — orchestration graph

- **Example architecture shown**
  - `profiles.yml`
    - Defines `fast` and `quality` OpenAI profiles.
    - Sets `fast` as the default profile.
  - `agent.yml`
    - Defines a `hello-world-agent` using profile `fast`.
    - Prompts the model to return exactly one character.
  - `machine.yml`
    - Defines a `hello-world-loop` machine.
    - Uses states like `start`, `build_char`, `append_char`, `done`.
    - Includes retry behavior:
      - `retry_on_empty: true`
      - backoffs: `[2, 8, 16, 35]`
      - jitter: `0.1`
    - Uses templated input/output fields and conditional transitions.
  - `run.py`
    - Registers a `HelloWorldHooks` class.
    - On `append_char`, it appends the first character of `last_output` to `context["current"]`.
    - Executes the machine with input `{"target": "Hello, World!"}` and logs the result.

- **Versioning**
  - The repo uses **lockstep versioning**:
    - one version number applies across the whole repository and all specs/SDKs.

- **Examples**
  - The page lists many runnable examples under `./sdk/examples`, including:
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

- **Specs and schemas**
  - States that **TypeScript definitions are the source of truth**.
  - Lists schema files:
    - `flatagent.d.ts` — agent config schema
    - `flatmachine.d.ts` — machine config schema
    - `profiles.d.ts` — model profile schema
    - `flatagents-runtime.d.ts` — runtime interfaces and backend contract

- **Runtime backend options**
  - `BackendConfig` categories and allowed values include:
    - `persistence`: `memory`, `local`, `sqlite`, `redis`, `postgres`, `s3`, `dynamodb`
    - `locking`: `none`, `local`, `sqlite`, `redis`, `consul`, `dynamodb`
    - `results`: `memory`, `redis`, `dynamodb`
    - `registration`: `memory`, `sqlite`, `redis`, `dynamodb`
    - `work`: `memory`, `sqlite`, `redis`, `dynamodb`
    - `signal`: `memory`, `sqlite`, `redis`, `dynamodb`
    - `trigger`: `none`, `file`, `socket`

- **SDK status**
  - Python agents: `pip install flatagents[litellm]` — **Stable**
  - Python machines: `pip install flatmachines[flatagents]` — **Stable**
  - JavaScript SDK: `sdk/js` — **In progress**

- **Logging and metrics**
  - Logging can be configured with:
    - `from flatmachines import setup_logging`
    - `setup_logging(level="INFO")`
  - Environment variables documented:
    - `FLATAGENTS_LOG_LEVEL`
    - `FLATAGENTS_LOG_FORMAT`
    - `FLATAGENTS_METRICS_ENABLED`
    - `OTEL_METRICS_EXPORTER`

- **Acknowledgments**
  - Thanks `pi-mono` for example coding-agent prompts and OAuth flow examples for codex and copilot.

### Assessment
This is a **mixed reference/announcement** page with fairly high density because it combines positioning, install instructions, YAML examples, schema references, and backend capability lists in one place. Durability is **medium**: the conceptual model of YAML-orchestrated agent state machines is fairly durable, but the specific versioned package names, SDK status, example set, and backend options may change quickly. The content is mostly **primary source** documentation from the project itself, so it is useful for evaluating the intended design and current maturity, though the warning about being “a product of its times” suggests some caution. It is best used as a **refer-back** resource for setup and architecture, not deep study unless you want to adopt the framework. Scrape quality is **good**: the main text, examples, versioning notes, SDK table, and runtime/backend lists are present, though any linked files themselves were not included.
