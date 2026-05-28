---
url: https://github.com/robbintt/flatagents/blob/a7cc6aa0109fae47beac7d822f478d3a69366fcf/SDK_COMMON_SPEC_PLAN.md
title: flatagents/SDK_COMMON_SPEC_PLAN.md at a7cc6aa0109fae47beac7d822f478d3a69366fcf · robbintt/flatagents
scraped_at: '2026-04-16T03:54:09Z'
word_count: 3832
raw_file: raw/2026-04-16_flatagents-sdk-common-spec-plan-md-at-a7cc6aa0109fae47beac7d822f478d3a69366fcf-r_d6920933.txt
tldr: A planning document for version 0.7.7 of FlatAgents’ cross-language SDK spec that defines common runtime interfaces, distributed execution requirements, WASM constraints, and an ACL2-based formal verification plan.
key_quote: 'Purpose: Define common requirements for FlatAgents SDK implementations across languages and runtimes.'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- wasm-bindgen
- Kubernetes
- Redis
- Consul
- PostgreSQL
- S3
- IndexedDB
- LocalStorage
- OpenTelemetry
libraries:
- ACL2
- Jinja2
- Hypothesis
- fast-check
- CEL
companies:
- FlatAgents
- Cloudflare
- Vercel
- AWS
- GCP
- Azure
tags:
- distributed-systems
- sdk-design
- wasm
- formal-verification
- state-machines
---

### TL;DR
A planning document for version 0.7.7 of FlatAgents’ cross-language SDK spec that defines common runtime interfaces, distributed execution requirements, WASM constraints, and an ACL2-based formal verification plan.

### Key Quote
“Purpose: Define common requirements for FlatAgents SDK implementations across languages and runtimes.”

### Summary
- **Document type:** Planning/specification for a shared SDK standard across Python, JavaScript, and Rust/WASM.
- **Spec version:** `0.7.7`; status is explicitly **“Planning Document.”**
- **Main goal:** Make FlatAgents SDKs behave consistently across runtimes and deployment environments, including:
  - Python, JavaScript, Rust/WASM
  - Kubernetes pods/jobs
  - cloud functions
  - ECS
  - edge runtimes
  - browser environments

#### Core spec files identified as source of truth
- `flatagent.d.ts` — agent configuration schema
- `flatmachine.d.ts` — machine orchestration schema
- `profiles.d.ts` — model profile configuration
- `flatagents-runtime.d.ts` — runtime interfaces, still only an initial draft

#### Required runtime interfaces
- **ExecutionLock**
  - Prevents concurrent execution of the same machine instance
  - Required implementations:
    - `NoOpLock` — MUST
    - `LocalFileLock` — SHOULD
    - `RedisLock` — MAY
    - `ConsulLock` — MAY
  - Formal note: lock acquisition modeled as a boolean predicate with a mutual exclusion invariant

- **PersistenceBackend**
  - Stores durable checkpoints / snapshots
  - Required implementations:
    - `MemoryBackend` — MUST
    - `LocalFileBackend` — SHOULD
    - `RedisBackend`, `PostgresBackend`, `S3Backend` — MAY
  - Interface:
    - `save(key, snapshot)` atomic
    - `load(key)`
    - `delete(key)`
    - `list(prefix)` deterministic lexicographic order

- **ResultBackend**
  - URI-addressed inter-machine communication via `flatagents://{execution_id}/{path}`
  - Paths:
    - `/checkpoint` for resume state
    - `/result` for final output
  - Required implementations:
    - `InMemoryResultBackend` — MUST
    - `RedisResultBackend` — MAY
  - Interface:
    - `write(uri, data)` with notify-blocked-readers semantics
    - `read(uri, {block, timeout})`
    - `exists(uri)`
    - `delete(uri)`

- **ExecutionConfig**
  - Execution types required:
    - `default` — single call, no retry
    - `retry` — backoff with jitter
    - `parallel` — N samples, return all successes
    - `mdap_voting` — multi-sample consensus mode
  - Formal notes mention monotonic backoff, bounded jitter, and k-margin consensus

- **MachineHooks**
  - Optional hooks supporting both sync and async behavior
  - Includes start/end hooks, state entry/exit hooks, transition hooks, error hooks, and action hooks

#### Distributed systems requirements
- Must support **fully stateless execution**
  - all state externalized to persistence
  - checkpoint/resume for interruptions
  - no in-memory state between invocations
- Defines a `MachineSnapshot` wire format with fields like:
  - `execution_id`
  - `machine_name`
  - `spec_version`
  - `current_state`
  - `context`
  - `step`
  - `created_at`
  - optional output, API call count, cost, parent execution ID, and pending launches
- Introduces an **outbox / launch intent pattern** for exactly-once launch semantics via `pending_launches`
- Specifies timeout and cancellation behavior
- Defines parallel execution modes:
  - `settled` — wait for all
  - `any` — return on first success

#### Rust/WASM-specific requirements
- Supported targets:
  - `wasm32-unknown-unknown` for browser / Cloudflare Workers
  - `wasm32-wasi` for Node.js / Deno / edge
  - native builds for CLI/server
- WASM constraints:
  - no filesystem for browser-targeted builds
  - no native threads; use async/await
  - browser binary size target under **500KB gzipped**
- WASM backend strategy includes:
  - `MemoryBackend`
  - `IndexedDBBackend`
  - `LocalStorageBackend`
  - `FetchBackend`
- JS/TS interop via `wasm-bindgen`, exporting `FlatAgent` and `FlatMachine` classes with Promise-based APIs

#### Formal verification / ACL2 section
- A major part of the document is an ACL2 verification plan.
- Proposes a `/verification/acl2/` repository layout with:
  - core state machine logic
  - theorem/proof files
  - refinement mappings to Python/JS/Rust SDKs
  - tests and counterexample generators
- Includes ACL2-style pseudocode for:
  - machine state
  - context operations
  - transition logic
  - simple expression evaluation
- Key properties to prove:
  - **progress**
  - **determinism**
  - **checkpoint consistency**
  - **mutual exclusion**
  - **exactly-once launch/outbox semantics**
- Also proposes:
  - property-based tests in Python/JS as executable spec bridges
  - CI/CD workflow that runs ACL2 proof certification and property tests

#### Cross-SDK compatibility checklist
- Tables mark Python and JavaScript as largely implemented (`✅`)
- Rust is mostly `TODO`
- Areas tracked:
  - configuration parsing
  - runtime interfaces
  - execution types
  - expression engines
- CEL support is only partial in JavaScript and TODO in Rust

#### Testing requirements
- A conformance test suite is planned in JSON format, meant to be runnable by any SDK
- Test categories:
  - agent tests
  - machine tests
  - parallel tests
  - persistence tests
  - expression tests
- Property-based tests should cover checkpoint/resume, expression determinism, transition totality, and error handler completeness

#### Roadmap
- Phase 1: finalize spec and generate JSON schema
- Phase 2: align Python and JS SDK behavior
- Phase 3: implement Rust/WASM runtime and browser backends
- Phase 4: add distributed Redis/cloud-function backends
- Phase 5: formal verification in ACL2

#### Open questions
- Full CEL support across JS/Rust
- hook serialization for distributed execution
- direct WASM LLM API calls vs host proxy
- standardized cost tracking
- common observability format, likely OpenTelemetry

#### Version/history
- Version history shows only:
  - `0.7.7` — “Initial SDK common spec plan”

### Assessment
This is a high-density **planning/reference** document with fairly high durability conceptually, though some parts are tied to current implementation choices and version-specific status. Its content is a **mixed** combination of spec, architecture plan, and verification strategy, with strong emphasis on formal methods and distributed runtime design. The originality is mainly **primary source**, since it appears to be the project’s own internal spec plan rather than commentary or aggregation. It is best used as a **refer-back** document: useful for checking intended requirements, interfaces, and roadmap decisions, but not as a final authoritative implementation spec because it is explicitly marked as a planning document and many items are still TODO/draft. Scrape quality is **good**: the content appears extensive and structurally complete, including code blocks, tables, and appendices, with no obvious missing major sections from the provided text.
