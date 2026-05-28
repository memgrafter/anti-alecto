---
url: https://github.com/badlogic/pi-mono/tree/main/packages/mom
title: pi-mono/packages/mom at main · badlogic/pi-mono
scraped_at: '2026-04-16T03:54:30Z'
word_count: 2961
raw_file: raw/2026-04-16_pi-mono-packages-mom-at-main-badlogic-pi-mono_1d041b13.txt
tldr: mom is a self-managing Slack bot/LLM agent that can run bash, edit files, install tools, and persist memory/workspaces per channel, with strong emphasis on Docker sandboxing and security risks.
key_quote: Mom is **self-managing**. She installs her own tools, programs CLI tools (aka "skills") she can use to help with your workflows and tasks, configures credentials, and maintains her workspace autonomously.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
tools:
- npm
- docker
- Slack
- Socket Mode
- tsx
libraries:
- pi-mom
- pi-coding-agent
companies:
- Slack
- Anthropic
tags:
- slack-bots
- llm-agents
- docker-sandboxing
- prompt-injection
- developer-tools
---

### TL;DR
`mom` is a self-managing Slack bot/LLM agent that can run bash, edit files, install tools, and persist memory/workspaces per channel, with strong emphasis on Docker sandboxing and security risks.

### Key Quote
“Mom is **self-managing**. She installs her own tools, programs CLI tools (aka "skills") she can use to help with your workflows and tasks, configures credentials, and maintains her workspace autonomously.”

### Summary
- **What it is**
  - `mom (Master Of Mischief)` is a Slack bot powered by an LLM.
  - It can execute bash commands, read/write files, and interact with a development environment.
  - It is designed to be **minimal** and **self-managing**, meaning it can install tools, create scripts, configure credentials, and maintain its own workspace.

- **Core features**
  - Slack integration via **Socket Mode**.
  - Full bash access for automation and environment control.
  - **Docker sandbox** support, recommended for isolation.
  - Persistent workspace in a single directory controlled by the user.
  - **Working memory** across sessions using memory files.
  - Ability to create workflow-specific CLI tools called **skills**.
  - Thread-based handling: concise main replies, detailed tool output in Slack threads.

- **Documentation links called out**
  - `docs/artifacts-server.md` — share HTML/JS visualizations publicly with live reload.
  - `docs/events.md` — reminders and periodic tasks.
  - `docs/sandbox.md` — Docker vs host security guidance.
  - `docs/slack-bot-minimal-guide.md` — minimal Slack integration setup.

- **Installation**
  - Install via npm:
    ```bash
    npm install @mariozechner/pi-mom
    ```

- **Slack app setup requirements**
  - Enable **Socket Mode**.
  - Create an app-level token with `connections:write` scope (`MOM_SLACK_APP_TOKEN`).
  - Add bot token scopes including:
    - `app_mentions:read`
    - `channels:history`
    - `channels:read`
    - `chat:write`
    - `files:read`
    - `files:write`
    - `groups:history`
    - `groups:read`
    - `im:history`
    - `im:read`
    - `im:write`
    - `users:read`
  - Subscribe to bot events:
    - `app_mention`
    - `message.channels`
    - `message.groups`
    - `message.im`
  - Enable Direct Messages in **App Home**.
  - Install the app and obtain the bot token (`MOM_SLACK_BOT_TOKEN`).
  - Add mom to channels where it should operate.

- **Quick start**
  - Set Slack and Anthropic credentials:
    ```bash
    export MOM_SLACK_APP_TOKEN=xapp-...
    export MOM_SLACK_BOT_TOKEN=xoxb-...
    export ANTHROPIC_API_KEY=sk-ant-...
    ```
  - Recommended Docker setup:
    ```bash
    docker run -d \
      --name mom-sandbox \
      -v $(pwd)/data:/workspace \
      alpine:latest \
      tail -f /dev/null
    ```
  - Run:
    ```bash
    mom --sandbox=docker:mom-sandbox ./data
    ```

- **CLI usage**
  - Basic form:
    ```bash
    mom [options] <working-directory>
    ```
  - Sandbox options:
    - `--sandbox=host` — run tools on host, not recommended
    - `--sandbox=docker:<name>` — run tools in a Docker container, recommended

- **Authentication options for Anthropic**
  - Use `ANTHROPIC_API_KEY`, or
  - Use OAuth login through `npx @mariozechner/pi-coding-agent`, then `/login`, then link `auth.json` into `~/.pi/mom/auth.json`.

- **How it works**
  - Mom is a Node.js app that connects to Slack using Socket Mode.
  - Each Slack channel/DM added to mom gets its own directory and persistent state.
  - Incoming messages are appended to `log.jsonl`.
  - Attachments are saved in an `attachments/` folder.
  - On mention/DM, mom syncs unseen logs into `context.jsonl`, loads memory from `MEMORY.md`, and then responds with tools.
  - Tool outputs stay in `context.jsonl`; direct replies go to `log.jsonl`.
  - Older context is compacted when needed, but `log.jsonl` remains a searchable full history.

- **Tools available to mom**
  - `bash` — primary tool for shell commands.
  - `read` — read file contents.
  - `write` — create or overwrite files.
  - `edit` — surgical edits.
  - `attach` — send files back to Slack.

- **Workspace layout**
  - The data directory contains:
    - global `MEMORY.md`
    - `settings.json`
    - `skills/`
    - per-channel directories with:
      - `MEMORY.md`
      - `log.jsonl`
      - `context.jsonl`
      - `attachments/`
      - `scratch/`
      - `skills/`
  - This structure is the basis for persistent memory, tools, and logs.

- **Skills system**
  - Skills are custom CLI tools mom can create and use.
  - Each skill has:
    - `SKILL.md` with frontmatter (`name`, `description`)
    - supporting scripts/programs
  - A basic skills repository exists at `github.com/badlogic/pi-skills`, which can be cloned into `/workspace/skills/pi-skills`.

- **Events / scheduled wake-ups**
  - Mom can be triggered by JSON files in `data/events/`.
  - Event types:
    - `immediate` — triggers as soon as created
    - `one-shot` — runs once at a specified datetime
    - `periodic` — cron-based recurring schedules
  - Events can be used for reminders, inbox checks, webhooks, and recurring tasks.
  - Periodic jobs can emit `[SILENT]` to avoid posting noise.
  - Limits: max 5 queued events per channel.

- **Security considerations**
  - The README strongly emphasizes that mom is a **power tool** and can be abused.
  - Risks include:
    - direct prompt injection from Slack users
    - indirect prompt injection from fetched content
    - credential exfiltration
  - Anything mom can access may be leaked:
    - API keys
    - tool tokens
    - files in the data directory
    - SSH keys in host mode
  - Mitigations:
    - use dedicated bot accounts
    - scope credentials tightly
    - avoid production secrets
    - monitor tool calls and logs
    - prefer Docker mode
  - Docker protects the host, but **not** credentials inside the container.
  - Separate instances are recommended for different trust levels or teams.

- **Development / code structure**
  - Main files:
    - `src/main.ts` — CLI entry point
    - `src/agent.ts` — agent runner and tool execution
    - `src/slack.ts` — Slack integration and backfill
    - `src/context.ts` — session/context management
    - `src/store.ts` — persistence and attachment downloads
    - `src/log.ts` — logging
    - `src/sandbox.ts` — sandbox execution
    - `src/tools/` — tool implementations
  - Dev mode:
    - `npm run dev`
    - or `npx tsx --watch ...` in `packages/mom`

- **License**
  - MIT

### Assessment
This is a **mixed** reference/tutorial document with high practical density: it combines product overview, installation steps, operational architecture, workspace conventions, security warnings, and development notes. Durability is **medium** because the concepts of Slack bots, sandboxing, memory, and prompt injection are broadly useful, but specific commands, package names, and Slack setup details may change over time. The content appears to be a **primary source** README from the project itself, so it is good for authoritative setup/usage details, though some sections are intentionally promotional and security-focused rather than deeply technical. It’s best used as a **refer-back** reference when setting up or understanding the system, and potentially **deep-study** if you’re evaluating the architecture or security model. Scrape quality is **good**: the content looks complete, including installation, workflow, security, and development sections, with code blocks and structure preserved.
