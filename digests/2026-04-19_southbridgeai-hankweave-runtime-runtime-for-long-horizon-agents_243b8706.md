---
url: https://github.com/SouthBridgeAI/hankweave-runtime
title: 'SouthBridgeAI/hankweave-runtime: Runtime for long-horizon agents'
scraped_at: '2026-04-19T07:51:28Z'
word_count: 3045
raw_file: raw/2026-04-19_southbridgeai-hankweave-runtime-runtime-for-long-horizon-agents_243b8706.txt
tldr: Hankweave is a TypeScript runtime for running long-horizon, headless AI “hanks” with strong emphasis on reproducibility, event logging, checkpoints, sentinels, and debuggability across existing agent harnesses like Claude Code, Codex, Gemini CLI, Pi, and OpenCode.
key_quote: “Single-threaded, headless-first, data agent runtime focused on maintainability, repairability, and long-horizon execution.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- SouthBridgeAI
- Southbridge
tools:
- bunx
- Claude Code
- Codex
- Gemini CLI
- Pi
- OpenCode
- npx
- Bun
libraries: []
companies:
- SouthBridgeAI
- Southbridge
tags:
- agent-runtime
- long-horizon-ai
- reproducibility
- event-logging
- checkpoints
---

### TL;DR
Hankweave is a TypeScript runtime for running long-horizon, headless AI “hanks” with strong emphasis on reproducibility, event logging, checkpoints, sentinels, and debuggability across existing agent harnesses like Claude Code, Codex, Gemini CLI, Pi, and OpenCode.

### Key Quote
“Single-threaded, headless-first, data agent runtime focused on maintainability, repairability, and long-horizon execution.”

### Summary
- **What it is**
  - `hankweave` is an **Apache 2.0** open-source runtime from **SouthBridgeAI**.
  - It is a **server/orchestrator** for long-running agent workflows called **hanks**.
  - It is written entirely in **TypeScript** and launched with `bunx hankweave`.

- **Core design goals**
  - Built for **brownfield AI engineering**: systems that are easier to maintain, debug, repair, and hand off.
  - Optimized for **long-horizon execution** rather than interactive “chatty” agent use.
  - Explicitly **not a coding agent** and **not a framework**; it is an opinionated runtime layer.

- **Main runtime features**
  - **Preflight checks**: validate API keys, models, file paths, rig configs, and schemas before execution starts.
  - **Sentinels**: real-time monitors on the event stream that detect drift, laziness, convention violations, cost spikes, and other failure modes.
  - **Looping**: repeat complex tasks with budget-aware termination and reliability-oriented repetition.
  - **Budgets**: authors and operators can set cost, time, and token limits; the runtime resolves competing constraints.
  - **Harness abstraction**: works with multiple agent harnesses such as:
    - Claude Code
    - Codex
    - Gemini CLI
    - Pi
    - OpenCode
  - **Rigs**: deterministic workspace/code loading so the same codon runs the same way.
  - **Checkpointing and rollbacks**: git snapshots at codon boundaries for recovery and alternate approaches.
  - **Structured event journal**: every tool call and decision is traceable.
  - **File-based prompts**: prompts are self-documenting with templates, comments, and frontmatter.

- **How it works**
  - A hank consists of:
    - **prompts**
    - **codons**
    - **rigs**
    - **sentinels**
    - **context boundaries**
    - **file tracking**
  - Inputs to the runtime are:
    - the **hank** itself
    - **runtime config** (API keys, model settings)
    - **data** mounted read-only
  - Hankweave orchestrates the chosen harnesses and streams events out over **WebSocket** to consumers.
  - Consumers can include:
    - included basic CLI
    - data pipelines
    - CI systems
    - custom UIs

- **Opinionated choices**
  - **Single agentic thread**: no parallel agent execution; one agent at a time to keep behavior understandable.
  - **Simple tools, used well**: file edits, scripting, shell commands; no MCPs or “skill trees.”
  - **Non-interactive**: designed for programmatic or agentic management, not human back-and-forth chat.
  - The philosophy is that reproducibility and inspectability are more valuable than interactive convenience.

- **Background and motivation**
  - Built at **Southbridge** after they encountered runs that were too complex to manage manually:
    - thousands of tool calls
    - hundreds of invocations
    - runs lasting **18+ hours**
  - Existing tools were seen as insufficient for either long-horizon execution or debugging after complexity grows.
  - It is reportedly used internally to:
    - migrate writing across platforms
    - do extensive planning for new features
    - auto-build shims as harnesses change
    - support partner work in research and codebooks

- **Sentinels**
  - Sentinels are highlighted as a key differentiator.
  - They observe the event stream in parallel and can:
    - trigger guardrails
    - write live documentation
    - track cost
    - detect drift
  - The docs argue LLMs work better as **noticers** than as direct evaluators.

- **Workflow and terminology**
  - **CCEPL-driven development**: develop interactively in a coding agent, then freeze working behavior into a codon for autonomous execution.
  - **Codons** are reusable units; they communicate through files, not shared memory.
  - **Continuation mode** defaults to `"fresh"` to keep handoffs explicit.
  - Data is mounted read-only at `read_only_data_source/` and referenced with `<%DATA_DIR%>`.

- **Costs and scale**
  - Costs vary widely by hank and model.
  - Example figures:
    - complex planning hank: roughly **$10–15 per run** on frontier models
    - simpler hanks: **pennies**
  - The docs recommend prototyping with cheaper models like **Haiku** and using:
    - `--max-cost 0.50 -m haiku`
  - Per-codon cost/token tracking and budget controls are part of the system.

- **Supported harnesses**
  - Five ship with Hankweave:
    - Claude Code
    - Gemini CLI
    - Codex
    - Pi
    - OpenCode
  - Multiple harnesses can be mixed in one hank.
  - The system can also build shims for new harnesses if they expose required capabilities.

- **Compatibility and deployment**
  - Can run **locally** or **air-gapped**.
  - Because it is orchestrated through configured harnesses, it can work with open-source models too.
  - Designed for atomic execution on temporary GPU instances rather than always-on infrastructure.

- **Caveats and limitations**
  - The project is explicitly described as a **research snapshot** and may break backward compatibility.
  - It is **opinionated** and likely to evolve.
  - The docs discourage expecting it to behave like Claude Code or a generic framework.
  - There is a Windows/Bun issue noted:
    - older Bun versions may silently fail when `bunx hankweave` hands off to Node
    - fixes: upgrade Bun, use `bunx --bun hankweave`, or use `npx hankweave`

- **Likely use case**
  - Best suited for people building **long-running, inspectable, reproducible AI workflows** where maintenance and debugging matter more than interactive agent exploration.

### Assessment
Durability is **medium**: the architectural ideas around long-horizon, inspectable agent execution are relatively durable, but many details are tied to specific harnesses, Bun/npm behavior, and current project status. Content type is **mixed** with strong **reference/tutorial** and **opinion** components, because it explains the system, its philosophy, and practical usage patterns. Density is **high**: the page is packed with concrete terms, commands, runtime features, FAQs, and design claims. Originality is **primary source** since this is the project’s own repository README describing its architecture and intent. Reference style is **refer-back** for the feature set, terminology, and workflow, though some sections are also worth a deep read if you’re evaluating whether to adopt it. Scrape quality is **good**: the main README content, FAQs, and warnings are present, though linked docs, demos, and any deeper code/examples are not included here.
