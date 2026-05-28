---
url: https://github.com/memgrafter/flatmachines
title: 'memgrafter/flatmachines: Orchestrate agents with a peer network of state machines. Supports checkpoint/restore, persistence, and more. BYO cli, or agent, or use flatagents with API. Batteries included.'
scraped_at: '2026-04-19T08:07:40Z'
word_count: 906
raw_file: raw/2026-04-19_memgrafter-flatmachines-orchestrate-agents-with-a-peer-network-of-state-machines_674a8c9e.txt
tldr: FlatMachines is a Python-first orchestration framework for LLM/agent workflows where you define state machines, agents, transitions, retries, and checkpointing in YAML, then run them through a small runtime.
key_quote: Your Python code stays small.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- FlatMachine
- HooksRegistry
- LoggingHooks
- setup_logging
- get_logger
libraries:
- flatagents
- litellm
companies:
- OpenAI
- GitHub
tags:
- agent-orchestration
- state-machines
- yaml-config
- llm-workflows
- checkpointing
---

### TL;DR
FlatMachines is a Python-first orchestration framework for LLM/agent workflows where you define state machines, agents, transitions, retries, and checkpointing in YAML, then run them through a small runtime.

### Key Quote
“Your Python code stays small.”

### Summary
- **What it is**
  - An open-source repo for **orchestrating agents with a peer network of state machines**.
  - Emphasizes **checkpoint/restore, persistence, retries, parallelism, error recovery, and distributed workers**.
  - Supports **BYO CLI or agent**, or using **flatagents with API**.
  - The repo warns that it is “a product of its times” and recommends the **Python SDK** for now; **JS and Rust are not yet preferred**.

- **Core workflow**
  - You describe behavior in **YAML config files** rather than hard-coding workflow logic:
    - `profiles.yml` for **model catalog / profiles**
    - `agent.yml` for a **single LLM call**
    - `machine.yml` for **orchestration**
  - The runtime handles:
    - retries and backoff
    - error routing
    - state management
    - transitions between states
    - checkpointing and recovery
    - distributed execution patterns

- **Quick start / hello world example**
  - Fastest path:
    - set `OPENAI_API_KEY`
    - run `sdk/examples/helloworld/python/run.sh`
  - For a new project:
    - install with:
      - `pip install flatmachines[flatagents] flatagents[litellm]`
  - The example shows a machine that:
    - starts with a target string
    - calls an agent to produce the next character
    - checks whether the output matches the expected char
    - appends the char via a hook
    - loops until the target is complete
  - The Python example uses:
    - `FlatMachine`
    - `HooksRegistry`
    - `LoggingHooks`
    - `setup_logging`
    - `get_logger`
  - `HelloWorldHooks.on_action()` appends the produced character to `context["current"]` when the `append_char` action fires.

- **YAML config details**
  - `profiles.yml`
    - defines profiles such as:
      - `fast`: `openai`, `gpt-5-mini`, `max_tokens: 2048`
      - `quality`: `openai`, `gpt-5`, `max_tokens: 4096`
    - supports a default profile and optional override
  - `agent.yml`
    - declares a `flatagent` named `hello-world-agent`
    - uses profile `fast`
    - system prompt instructs the agent to output exactly one character
    - user prompt injects `input.target` and `input.current`
  - `machine.yml`
    - declares a `flatmachine` named `hello-world-loop`
    - keeps `context.target` and `context.current`
    - defines states:
      - `start` → initial state
      - `build_char` → agent-driven state with retry/backoff
      - `append_char` → action state
      - `done` → final state
    - retry config includes:
      - `retry_on_empty: true`
      - backoffs: `[2, 8, 16, 35]`
      - `jitter: 0.1`
    - uses templating like `{{ context.current }}` and `{{ input.target }}`

- **Examples**
  - The repo includes many runnable examples in `./sdk/examples`, including:
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
  - Each example is mapped to a concrete orchestration pattern such as feedback loops, parallelism, human approval, worker pools, synthesis, or reinforcement learning.

- **Specs and versioning**
  - The repo states that **TypeScript definitions are the source of truth**:
    - `flatagent.d.ts`
    - `flatmachine.d.ts`
    - `profiles.d.ts`
    - `flatagents-runtime.d.ts`
  - It uses **lockstep versioning** across specs and SDKs, meaning a single version number applies to the whole repository.

- **Runtime backend options**
  - `BackendConfig` supports these categories:
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
  - JavaScript SDK in `sdk/js` — **In progress**

- **Logging and metrics**
  - Logging can be set up via:
    - `from flatmachines import setup_logging`
    - `setup_logging(level="INFO")`
  - Environment variables documented:
    - `FLATAGENTS_LOG_LEVEL` default `INFO`
    - `FLATAGENTS_LOG_FORMAT` default `standard`
    - `FLATAGENTS_METRICS_ENABLED` default `true`
    - `OTEL_METRICS_EXPORTER` default `console`

- **Notable limitations / caveats**
  - The repo explicitly says it is a **“product of its times”** and warns “Caveat emptor.”
  - It recommends **Python over JS/Rust** at this stage.
  - Because this is a GitHub README-style overview, it is more of a **project reference and onboarding document** than a deep technical specification.

### Assessment
This is a **mixed** reference/tutorial-style repository README with a high density of concrete implementation details, config schemas, example names, commands, and runtime backend options. Durability is **medium** because the architectural ideas—state-machine orchestration for agents, YAML-driven workflows, retries, checkpointing—are fairly durable, but many specifics are tied to current SDK status, version `2.7.0`, and named models like `gpt-5-mini` / `gpt-5`. The content is primarily a **primary source** project overview and docs, not commentary. It is best used **refer-back** for setup, config shape, and feature lookup, though the quick-start sections are also suitable for a one-time skim. Scrape quality is **good**: the README structure, code blocks, tables, and example list are preserved, and no obvious major sections appear missing.
