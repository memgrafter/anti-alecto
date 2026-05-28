---
url: https://github.com/memgrafter/flatagents/graphs/traffic
title: Traffic · memgrafter/flatagents
scraped_at: '2026-04-17T05:30:29Z'
word_count: 885
raw_file: raw/2026-04-17_traffic-memgrafter-flatagents_d659f7ff.txt
tldr: This is a GitHub traffic page for `memgrafter/flatagents`, but the captured content mostly shows the repository’s README for “FlatMachines,” a YAML-driven agent orchestration system with Python SDK examples, specs, and runtime features.
key_quote: Orchestrate agents with a peer network of state machines. Supports checkpoint/restore, persistence, and more.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- GitHub
libraries:
- flatagents
- flatmachines
- litellm
companies:
- OpenAI
- GitHub
tags:
- agent-orchestration
- state-machines
- yaml
- python-sdk
- llm-infrastructure
---

### TL;DR
This is a GitHub **traffic page** for `memgrafter/flatagents`, but the captured content mostly shows the repository’s README for “FlatMachines,” a YAML-driven agent orchestration system with Python SDK examples, specs, and runtime features.

### Key Quote
“Orchestrate agents with a peer network of state machines. Supports checkpoint/restore, persistence, and more.”

### Summary
- **URL/page context:** The URL is `https://github.com/memgrafter/flatagents/graphs/traffic`, which should normally show GitHub traffic analytics such as views, clones, referrers, and popular content.  
- **What was captured instead:** The provided content is largely the repository landing/README content for **FlatMachines / flatagents**, not the actual traffic graph data.
- **Project overview:**
  - FlatMachines is an orchestration system for agents using **state machines**.
  - It emphasizes **checkpoint/restore**, **persistence**, **retries**, **parallelism**, **error recovery**, and **distributed workers**.
  - The repo notes: “Prefer the Python SDK for now, not yet JS or Rust.”
  - For machine readers, it points to **`AGENTS.md`** as a compact reference.
- **Core programming model:**
  - Users write **YAML** to define:
    - `profiles.yml` for model catalog and defaults
    - `agent.yml` for a single LLM agent
    - `machine.yml` for orchestration/state transitions
  - The runtime manages:
    - retries
    - error routing
    - state
    - parallelism
    - checkpointing
- **Quick start details:**
  - Example install:
    - `pip install flatmachines[flatagents] flatagents[litellm]`
  - Example demo path:
    - `sdk/examples/helloworld/python`
    - run via `./run.sh`
  - The sample configuration uses model profiles like `fast` and `quality` with OpenAI models such as `gpt-5-mini` and `gpt-5`.
- **Example machine behavior:**
  - The sample machine builds a target string **one character at a time**.
  - It retries when the agent output is empty.
  - A hook (`HelloWorldHooks`) appends the character to context when `append_char` runs.
- **Repository structure highlights:**
  - Many runnable examples are listed under `./sdk/examples`, including:
    - `helloworld`
    - `writer_critic`
    - `parallelism`
    - `error_handling`
    - `human-in-the-loop`
    - `distributed_worker`
    - `coding_agent_cli`
    - `research_paper_analysis`
    - `multi_paper_synthesizer`
    - and more
- **Specs and versioning:**
  - TypeScript definition files are the source of truth:
    - `flatagent.d.ts`
    - `flatmachine.d.ts`
    - `profiles.d.ts`
    - `flatagents-runtime.d.ts`
  - The repo uses **lockstep versioning** across specs and SDKs.
- **Runtime/backend configuration:**
  - Supported backend categories include persistence, locking, results, registration, work, signal, and trigger.
  - Example allowed values are listed, such as `memory`, `sqlite`, `redis`, `postgres`, `s3`, `dynamodb`, and `file/socket` for triggers.
- **SDK status:**
  - Python agents SDK: stable
  - Python machines SDK: stable
  - JavaScript SDK: in progress
- **Logging and metrics:**
  - Shows how to enable logging with `setup_logging(level="INFO")`
  - Documents environment variables for log level, format, and OpenTelemetry metrics

### Assessment
**Durability:** Medium. The GitHub traffic page itself would be time-sensitive and frequently changing, but the captured text is mostly a README for a repo that appears more durable as a software reference. The content includes versioned specs (`2.6.0`) and current model examples (`gpt-5`, `gpt-5-mini`), which may age quickly. **Content type:** mixed, but primarily reference/tutorial with a traffic-page mismatch. **Density:** high, because the README excerpt is packed with config examples, install commands, and repo structure. **Originality:** primary source for the repository’s own documentation, though the actual traffic analytics are missing. **Reference style:** refer-back if you’re evaluating the project or learning the YAML/state-machine approach; skim-once if you only needed traffic stats, because those are not present here. **Scrape quality:** partial. The capture does **not include the actual GitHub traffic data** (views/clones/referrers), so this appears to be an incomplete or incorrect page scrape for the URL.
