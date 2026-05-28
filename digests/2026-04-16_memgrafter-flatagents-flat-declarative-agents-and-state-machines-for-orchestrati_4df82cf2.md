---
url: https://github.com/memgrafter/flatagents/tree/main
title: 'memgrafter/flatagents: Flat, declarative agents and state machines for orchestrating LLMs.'
scraped_at: '2026-04-16T03:53:40Z'
word_count: 885
raw_file: raw/2026-04-16_memgrafter-flatagents-flat-declarative-agents-and-state-machines-for-orchestrati_4df82cf2.txt
tldr: You write YAML that describes states, transitions, and agents, while the runtime handles retries, parallelism, checkpointing, error recovery, and distributed workers.
key_quote: Your Python code stays small.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- flatagents
- flatmachines
- openai
libraries:
- litellm
companies:
- OpenAI
tags:
- llm-orchestration
- state-machines
- yaml-config
- agent-frameworks
- distributed-systems
---

### TL;DR
FlatAgents/FlatMachines is a YAML-driven orchestration framework for LLM agents and state machines, emphasizing retries, checkpointing, persistence, parallelism, and distributed execution with Python as the most mature SDK.

### Key Quote
"Your Python code stays small."

### Summary
- **What it is**
  - A repository for **FlatMachines** / **FlatAgents**, described as “flat, declarative agents and state machines for orchestrating LLMs.”
  - Core idea: define **states, transitions, agents, and profiles in YAML**, while the runtime handles orchestration concerns like retries, error recovery, persistence, and parallelism.
  - The repo explicitly warns it is “a product of its times” and says to **prefer the Python SDK for now**, not JS or Rust.

- **Main workflow**
  - You typically use **three config files**:
    - `profiles.yml` for model catalog/profile selection
    - `agent.yml` for a single LLM agent definition
    - `machine.yml` for orchestration/state machine logic
  - The provided hello-world example shows:
    - a profile named `fast` using `openai` `gpt-5-mini`
    - a higher-quality profile `quality` using `gpt-5`
    - an agent that outputs exactly one character
    - a machine that loops until a target string is built character by character
  - The runtime can:
    - retry on empty output
    - apply backoff and jitter
    - route transitions conditionally
    - map agent outputs into context fields
    - invoke hooks for custom actions

- **Example architecture demonstrated**
  - `machine.yml` defines:
    - `start` initial state
    - `build_char` agent-driven state
    - `append_char` action state
    - `done` final output state
  - `run.py` shows how to:
    - set up logging
    - register hooks via `HooksRegistry`
    - subclass `LoggingHooks`
    - mutate machine context in an action hook (`append_char`)
    - execute the machine asynchronously with `FlatMachine.execute(...)`
  - The example runs with:
    - `python run.py`
    - input target: `"Hello, World!"`
    - `max_agent_calls=20`

- **Versioning and spec model**
  - The repository uses **lockstep versioning**: one version number applies across the repo.
  - TypeScript definitions are the **source of truth** for schemas:
    - `flatagent.d.ts`
    - `flatmachine.d.ts`
    - `profiles.d.ts`
    - `flatagents-runtime.d.ts`
  - Runtime backend configuration categories include:
    - `persistence`, `locking`, `results`, `registration`, `work`, `signal`, `trigger`
  - Each category supports specific backend types such as `memory`, `sqlite`, `redis`, `postgres`, `s3`, `dynamodb`, `consul`, `file`, and `socket`.

- **Examples included**
  - The repo lists many runnable examples in `sdk/examples`, including:
    - `helloworld`
    - `writer_critic`
    - `parallelism`
    - `error_handling`
    - `human-in-the-loop`
    - `distributed_worker`
    - `coding_agent_cli`
    - `research_paper_analysis`
    - `multi_paper_synthesizer`
    - `support_triage_json`
    - `dynamic_agent`
    - `peering`
    - `rlm`
  - These examples indicate the framework is intended for:
    - feedback loops
    - multi-agent workflows
    - human approval steps
    - worker pools / queues
    - paper analysis and synthesis
    - self-optimization and reinforcement-learning-style loops

- **SDK status**
  - Python agents: `pip install flatagents[litellm]` — **Stable**
  - Python machines: `pip install flatmachines[flatagents]` — **Stable**
  - JavaScript SDK exists in `sdk/js` but is marked **In progress**

- **Logging and metrics**
  - Logging setup is exposed via:
    - `from flatmachines import setup_logging`
    - `setup_logging(level="INFO")`
  - Environment variables documented:
    - `FLATAGENTS_LOG_LEVEL`
    - `FLATAGENTS_LOG_FORMAT`
    - `FLATAGENTS_METRICS_ENABLED`
    - `OTEL_METRICS_EXPORTER`
  - Metrics support references OpenTelemetry.

- **Who this is for**
  - Developers building **LLM agent workflows**, especially those who want:
    - declarative config over imperative orchestration
    - stateful multi-step agent loops
    - persistence/checkpointing
    - distributed or parallel worker behavior
    - hooks for custom runtime behavior

### Assessment
This is a mixed but primarily **tutorial/reference** repository with fairly high practical density because it includes a concrete hello-world setup, config schemas, SDK install commands, backend capability lists, and an examples index. Its **durability is medium**: the architectural ideas around declarative state machines and agent orchestration are durable, but the specific versioning, package names, and model examples are tied to current ecosystem choices. The content is mostly **primary source** documentation from the repo maintainers, though the warning that the repo is “a product of its times” suggests a candid maturity signal. It is best used as a **refer-back** resource for setup, schema lookup, and example selection; the scrape quality is **good** overall, with code blocks, tables, and key sections preserved, though it’s limited to the top-level README content and does not include deeper implementation details or the linked files themselves.
