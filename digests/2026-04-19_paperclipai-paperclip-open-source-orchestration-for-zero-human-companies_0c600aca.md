---
url: https://github.com/paperclipai/paperclip
title: 'paperclipai/paperclip: Open-source orchestration for zero-human companies'
scraped_at: '2026-04-19T07:00:07Z'
word_count: 1885
raw_file: raw/2026-04-19_paperclipai-paperclip-open-source-orchestration-for-zero-human-companies_0c600aca.txt
tldr: Paperclip is an MIT-licensed Node.js + React open-source control plane for orchestrating many AI agents as if they were a company, with org charts, budgets, governance, heartbeats, and audit trails.
key_quote: If OpenClaw is an _employee_, Paperclip is the _company_
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Node.js
- React
- pnpm
- Claude Code
- OpenClaw
- Cursor
- Codex
- Bash
- HTTP
- Tailscale
- Vercel
libraries: []
companies:
- Paperclip
- OpenClaw
- Claude
- Cursor
- Vercel
- Tailscale
tags:
- ai-agents
- orchestration
- autonomous-systems
- governance
- developer-tools
---

### TL;DR
Paperclip is an MIT-licensed Node.js + React open-source control plane for orchestrating many AI agents as if they were a company, with org charts, budgets, governance, heartbeats, and audit trails.

### Key Quote
“**If OpenClaw is an _employee_, Paperclip is the _company_**”

### Summary
- **What it is**
  - Paperclip is described as “open-source orchestration for zero-human companies.”
  - It is a **Node.js server and React UI** for coordinating AI agents that run business-like operations.
  - The project positions itself as a **company-level orchestration layer**, not an agent framework or chatbot.

- **Core idea**
  - You define a **company goal**, “hire” agents for roles like CEO, CTO, engineer, designer, or marketer, and then review/approve/run work from a dashboard.
  - It emphasizes that agents should be managed like an organization, with **org charts, budgets, governance, goal alignment, and coordination**.

- **Supported agent/runtime ecosystem**
  - Paperclip claims compatibility with “bring your own agent.”
  - Listed examples/works-with integrations include:
    - **OpenClaw**
    - **Claude Code**
    - **Codex**
    - **Cursor**
    - **Bash**
    - **HTTP**
  - The slogan is: “If it can receive a heartbeat, it’s hired.”

- **Who it’s for**
  - People building **autonomous AI companies**
  - Users coordinating **many agents** at once
  - People who need **persistent task tracking**, **cost controls**, and **24/7 autonomous agents**
  - People who want to manage these systems from a **mobile-friendly dashboard**

- **Main features**
  - **Bring Your Own Agent**: any runtime/provider can be slotted into the org chart
  - **Goal Alignment**: every task traces back to company mission
  - **Heartbeats**: agents wake on a schedule, check for work, and act
  - **Cost Control**: monthly budgets per agent; agents stop at their limit
  - **Multi-Company**: one deployment can host many isolated companies
  - **Ticket System**: threaded conversations, tool-call tracing, immutable audit log
  - **Governance**: approve hires, override strategy, pause/terminate agents
  - **Org Chart**: roles, hierarchies, reporting lines, job descriptions
  - **Mobile Ready**: manage from anywhere

- **Problems it claims to solve**
  - Keeping track of many Claude Code tabs/agents
  - Losing context after reboot
  - Manually reconstructing what agents are supposed to be doing
  - Disorganized agent configs and ad hoc coordination
  - Runaway token spend
  - Recurring jobs that need to be kicked off manually
  - Babysitting coding agents instead of assigning tasks and reviewing work

- **Why it says it’s special**
  - **Atomic execution** for task checkout and budget enforcement
  - **Persistent agent state** across heartbeats
  - **Runtime skill injection** without retraining
  - **Governance with rollback**
  - **Goal-aware execution** with full goal ancestry
  - **Portable company templates** with secret scrubbing and collision handling
  - **True multi-company isolation**

- **What it is not**
  - Not a chatbot
  - Not an agent framework
  - Not a workflow builder
  - Not a prompt manager
  - Not a single-agent tool
  - Not a code review tool

- **Quickstart / installation**
  - Simplest setup:
    ```bash
    npx paperclipai onboard --yes
    ```
  - Optional bind modes:
    ```bash
    npx paperclipai onboard --yes --bind lan
    npx paperclipai onboard --yes --bind tailnet
    ```
  - Manual install:
    ```bash
    git clone https://github.com/paperclipai/paperclip.git
    cd paperclip
    pnpm install
    pnpm dev
    ```
  - Default local API server: `http://localhost:3100`
  - Embedded PostgreSQL is created automatically
  - Requirements: **Node.js 20+**, **pnpm 9.15+**

- **Typical setup / deployment**
  - Local mode: single Node.js process with embedded Postgres and local file storage
  - Production: bring your own Postgres and deploy however you like
  - Mentions Tailscale for solo access and Vercel as an example later-stage deployment option

- **Development commands**
  - `pnpm dev` — full dev
  - `pnpm dev:once` — full dev without file watching
  - `pnpm dev:server` — server only
  - `pnpm build` — build all
  - `pnpm typecheck`
  - `pnpm test` — Vitest only
  - `pnpm test:e2e` — Playwright browser suite
  - `pnpm db:generate`, `pnpm db:migrate`
  - Notes that `pnpm test` does **not** run Playwright

- **Roadmap**
  - Completed items include:
    - Plugin system
    - OpenClaw/claw-style agent employees
    - companies.sh import/export
    - AGENTS.md configs
    - Skills Manager
    - Scheduled Routines
    - Better Budgeting
    - Agent Reviews and Approvals
  - Planned items include:
    - Multiple Human Users
    - Cloud/Sandbox agents
    - Artifacts & Work Products
    - Memory / Knowledge
    - Enforced Outcomes
    - Deep Planning
    - Work Queues
    - Self-Organization
    - Automatic Organizational Learning
    - CEO Chat
    - Cloud deployments
    - Desktop App

- **Telemetry**
  - Collects **anonymous usage telemetry** by default
  - Claims it does **not** collect personal info, issue content, prompts, file paths, or secrets
  - Private repo references are hashed with a per-install salt
  - Can be disabled via:
    - `PAPERCLIP_TELEMETRY_DISABLED=1`
    - `DO_NOT_TRACK=1`
    - `CI=true`
    - `telemetry.enabled: false`

### Assessment
This is a **mixed** content type, primarily a **reference/docs-style README** with strong marketing language and some tutorial/quickstart material. Durability is **medium** because the conceptual framing around agent orchestration and governance is fairly timeless, but installation commands, roadmap items, and product claims may change quickly. Density is **high**: it packs installation steps, feature claims, roadmap, telemetry policy, and positioning into a single README. Originality is mostly **primary source** from the maintainers, though it is also promotional in tone rather than neutral documentation. It is best used as **refer-back** material to quickly understand what the project is, whether it fits your needs, and how to install it; not deep-study. Scrape quality looks **good** overall, with the README text captured clearly, though images and the embedded video are present only as references and not directly viewable here.
