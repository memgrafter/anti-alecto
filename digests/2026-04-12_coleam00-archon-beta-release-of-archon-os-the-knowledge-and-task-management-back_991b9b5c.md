---
url: https://github.com/coleam00/Archon
title: 'coleam00/Archon: Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants.'
scraped_at: '2026-04-12T07:25:22Z'
word_count: 1722
raw_file: raw/2026-04-12_coleam00-archon-beta-release-of-archon-os-the-knowledge-and-task-management-back_991b9b5c.txt
tldr: Archon is a beta open-source workflow engine for AI coding agents that makes code changes repeatable by running YAML-defined pipelines for planning, implementation, validation, review, and PR creation.
key_quote: Archon fixes this. Encode your development process as a workflow.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- coleam00
tools:
- Bun
- Claude Code
- GitHub CLI
- GitHub Actions
- GitHub CLI
- GitHub
- Slack
- Telegram
- Discord
- Docker
- n8n
libraries: []
companies:
- GitHub
tags:
- ai-coding
- workflow-automation
- developer-tools
- open-source
- yaml
---

### TL;DR
Archon is a beta open-source workflow engine for AI coding agents that makes code changes repeatable by running YAML-defined pipelines for planning, implementation, validation, review, and PR creation.

### Key Quote
“Archon fixes this. Encode your development process as a workflow.”

### Summary
- **What it is**
  - Archon is described as “the first open-source harness builder for AI coding.”
  - It is a workflow engine for AI coding agents, aimed at making AI-assisted software development deterministic and repeatable.
  - The project positions itself as “like Dockerfiles did for infrastructure and GitHub Actions did for CI/CD.”

- **Core idea**
  - You define development processes as **YAML workflows** in `.archon/workflows/`.
  - Workflows can include:
    - planning
    - implementation
    - validation/tests
    - code review
    - approval gates
    - pull request creation
  - Archon combines:
    - **deterministic nodes** like bash scripts, tests, and git operations
    - **AI nodes** for planning, coding, and review
  - It emphasizes that the AI should only be used where it adds value, while the overall process remains controlled by the user.

- **Main benefits claimed**
  - **Repeatable**: same workflow sequence every run
  - **Isolated**: each run gets its own git worktree, enabling parallel work without conflicts
  - **Fire and forget**: users can start a workflow and return later to a finished PR
  - **Composable**: mix scripts/tests/git with AI steps
  - **Portable**: workflows work across CLI, Web UI, Slack, Telegram, and GitHub

- **Example workflow structure**
  - The README shows a YAML example with nodes:
    - `plan` → prompt to explore codebase and create an implementation plan
    - `implement` → depends on `plan`, runs in a loop until `ALL_TASKS_COMPLETE`, with fresh context each iteration
    - `run-tests` → bash command `bun run validate`
    - `review` → AI review against the plan
    - `approve` → human approval gate, interactive loop until `APPROVED`
    - `create-pr` → push changes and create a PR
  - This demonstrates the DAG-like workflow model and support for loops and human-in-the-loop checkpoints.

- **Workflow examples included**
  - The repo ships with **17 default workflows**, including:
    - `archon-assist`
    - `archon-fix-github-issue`
    - `archon-idea-to-pr`
    - `archon-plan-to-pr`
    - `archon-issue-review-full`
    - `archon-smart-pr-review`
    - `archon-comprehensive-pr-review`
    - `archon-create-issue`
    - `archon-validate-pr`
    - `archon-resolve-conflicts`
    - `archon-feature-development`
    - `archon-architect`
    - `archon-refactor-safely`
    - `archon-ralph-dag`
    - `archon-remotion-generate`
    - `archon-test-loop-dag`
    - `archon-piv-loop`
  - These are meant as starting points that users can copy and customize.

- **Setup / installation**
  - **Full setup**:
    - prerequisites: **Bun**, **Claude Code**, **GitHub CLI**
    - commands shown:
      - `git clone https://github.com/coleam00/Archon`
      - `cd Archon`
      - `bun install`
      - `claude`
      - then say: **“Set up Archon”**
  - **Quick install** for users who already have Claude Code:
    - macOS/Linux: `curl -fsSL https://archon.diy/install | bash`
    - Windows PowerShell: `irm https://archon.diy/install.ps1 | iex`
    - Homebrew: `brew install coleam00/archon/archon`
  - Important note: users should run **Claude Code from their target repo**, not from the Archon repo, because the setup wizard copies the Archon skill into the project.

- **Web UI**
  - Archon includes a web dashboard for:
    - chatting with the coding agent
    - running workflows
    - monitoring activity
  - Key UI sections:
    - **Chat**
    - **Dashboard**
    - **Workflow Builder**
    - **Workflow Execution**
  - It also acts as a monitoring hub for conversations and workflow events from multiple platforms.

- **Platforms / integrations**
  - The system supports:
    - Web UI
    - CLI
    - Telegram
    - Slack
    - GitHub Webhooks
    - Discord
  - Setup times are listed for some of these, suggesting remote control and notification use cases.

- **Architecture**
  - The README includes an architecture diagram with:
    - platform adapters
    - orchestrator for routing/context management
    - command handler
    - workflow executor
    - AI assistant clients (Claude / Codex)
    - SQLite / PostgreSQL backend
  - The database is said to use **7 tables** for:
    - codebases
    - conversations
    - sessions
    - workflow runs
    - isolation environments
    - messages
    - workflow events

- **Previous version**
  - The README notes that the original Python-based Archon (task management + RAG) is preserved on the `archive/v1-task-management-rag` branch.

- **Docs and support**
  - Full documentation is hosted at **archon.diy**
  - Documentation topics include:
    - getting started
    - CLI reference
    - workflow authoring
    - command authoring
    - configuration
    - AI assistant setup
    - deployment
    - architecture
    - troubleshooting

- **License and contribution**
  - Licensed under **MIT**
  - Contributions are welcome via GitHub issues and pull requests

### Assessment
This is a high-level project README for an open-source tool, so the content type is **mixed**: part product announcement, part reference, part setup tutorial. Durability is **medium** because the core workflow-engine concept is fairly stable, but installation commands, supported assistants, and setup details may change with versions and external tooling like Claude Code, Bun, and GitHub CLI. The density is **high**: it packs in positioning, examples, architecture, install steps, workflow inventory, and docs links. Originality is **primary source**, since it is the project’s own README and reflects the authors’ intended design and claims. It is best used as a **refer-back** reference when deciding whether to adopt the tool or locate setup/docs quickly. Scrape quality is **good** overall: the main README content appears intact, including the YAML example and architecture diagram as text, though any visual nuance from images or linked external docs is naturally not captured here.
