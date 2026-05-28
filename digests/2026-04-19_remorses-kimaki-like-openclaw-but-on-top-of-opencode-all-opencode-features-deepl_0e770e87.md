---
url: https://github.com/remorses/kimaki
title: 'remorses/kimaki: like openclaw but on top of opencode. all opencode features deeply integrated inside Discord. each project is a channel. each session a thread'
scraped_at: '2026-04-19T08:03:32Z'
word_count: 1140
raw_file: raw/2026-04-19_remorses-kimaki-like-openclaw-but-on-top-of-opencode-all-opencode-features-deepl_0e770e87.txt
tldr: Kimaki is a Discord bot and CLI that turns Discord channels into OpenCode-powered coding sessions, letting you prompt an AI agent to edit and run code on your machine from inside threads.
key_quote: Think of it as texting your codebase.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Discord
- OpenCode
- Gemini API
libraries: []
companies:
- Discord
- Google
tags:
- discord-bot
- coding-agent
- cli-tools
- developer-workflow
- open-source-software
---

### TL;DR
Kimaki is a Discord bot and CLI that turns Discord channels into OpenCode-powered coding sessions, letting you prompt an AI agent to edit and run code on your machine from inside threads.

### Key Quote
“Think of it as texting your codebase.”

### Summary
- **What it is**
  - Kimaki is a Discord bot for controlling [OpenCode](https://opencode.ai) coding sessions from Discord.
  - Positioning: “Iron Man's Jarvis for coding agents, inside Discord.”
  - Each Discord **channel maps to a project directory** on your machine.
  - Each message creates a **thread** and starts an OpenCode session.

- **Core workflow**
  - Install and run with:
    ```bash
    npx -y kimaki@latest
    ```
  - The CLI handles setup interactively in about a minute.
  - Kimaki acts as the bridge between Discord and your local machine; keep the CLI running.

- **Setup modes**
  - **Gateway mode (default)**:
    - Uses Kimaki’s pre-built Discord bot.
    - No Discord Developer Portal setup required.
    - Recommended path; install via one link and authorize in your server.
  - **Self-hosted mode**:
    - Create your own Discord bot in the Discord Developer Portal.
    - Takes about 5–10 minutes.
    - Useful if you want full control over the bot identity.
  - Both modes behave the same after setup.

- **Main capabilities**
  - **Text messages**: send a prompt in a linked channel to start a session.
  - **File attachments**: images, code files, and other files are included in session context.
  - **Voice messages**:
    - Transcribed using Google’s Gemini API.
    - Uses the project’s file tree to better recognize function names and file paths.
    - Requires a Gemini API key during setup.
  - **Session management**:
    - Resume sessions.
    - Fork from any message.
    - Generate public URLs to share sessions.
  - **Message queue**:
    - `/queue <message>` queues follow-up messages while the agent is still responding.
    - Ending a message with `. queue` does the same.
  - **Memory**:
    - Reads `MEMORY.md` from the project root at session start.
    - The agent can update it to retain learnings, decisions, and context.
  - **Tool permissions**:
    - Shows Accept / Accept Always / Deny buttons for actions requiring approval.
    - Defaults can be customized in `opencode.json`.
    - References OpenCode permissions docs.

- **Slash commands**
  - `/session <prompt>` — start a new session
  - `/resume <session>` — resume a session
  - `/abort` — stop current session
  - `/add-project <project>` — create channels for an existing OpenCode project
  - `/create-new-project <name>` — create a new project folder and session
  - `/new-worktree <name>` — create a git worktree and start a session
  - `/merge-worktree` — merge worktree branch
  - `/model` — change model
  - `/agent` — change agent
  - `/share` — create a public URL
  - `/fork` — fork from a previous message
  - `/queue <message>` — queue a message
  - `/clear-queue` — clear queued messages
  - `/undo` — revert last assistant message and file changes
  - `/redo` — redo last undone message
  - `/screenshare` — share screen via VNC tunnel, auto-stops after 1 hour
  - `/screenshare-stop` — stop screen sharing
  - `/upgrade-and-restart` — upgrade Kimaki and restart
  - It also imports OpenCode project-specific commands, skills, and MCP prompts into Discord command form.

- **CLI commands**
  - `npx -y kimaki@latest` — start/setup bot
  - `npx -y kimaki project add [directory]` — add a project directory as a Discord channel
  - `npx -y kimaki send --channel <channel-id> --prompt "your prompt"` — start a session programmatically
  - `npx -y kimaki upgrade` — upgrade and restart
  - Mentions CI/automation docs for full `send` command reference, GitHub Actions, and scheduled tasks.

- **Access control**
  - Kimaki only processes messages from users with one of:
    - Server Owner
    - Manage Server permission
    - Administrator permission
    - A role named **“Kimaki”** (case-insensitive)
  - Recommended team setup: use the **Kimaki** role for trusted users.
  - A role named **“no-kimaki”** blocks specific users, even server owners.
  - Other bots are ignored by default unless given the Kimaki role.

- **Model and agent configuration**
  - Configure model in `opencode.json`, e.g.:
    ```json
    {
      "model": "anthropic/claude-sonnet-4-20250514"
    }
    ```
  - Model format is `provider/model-name`.
  - Examples include Anthropic Claude, OpenAI GPT-4o, and Google Gemini 2.5 Pro.
  - `/model` and `/agent` can override settings per channel/session.

- **Best practices**
  - Create a dedicated Discord server for agent activity.
  - Use the **Kimaki** role for access control in teams.
  - Send long prompts as file attachments due to Discord character limits.

- **Advanced docs linked**
  - Advanced Setup: multiple instances, multiple servers, architecture
  - CI & Automation: programmatic sessions, GitHub Actions, scheduled tasks, per-session permissions
  - Screen Sharing: browser-based screen sharing setup
  - Internals: SQLite, lock port, channel metadata, voice processing

### Assessment
This is a **mixed** technical product README/reference page with tutorial and docs elements. Durability is **medium**: the core idea of Discord-based coding-agent control is fairly durable, but many specifics are tied to current tooling, command names, model IDs, and OpenCode/Discord implementation details that may change. Density is **high** because it includes setup, features, commands, permissions, configuration, and operational guidance in a compact format. Originality is **primary source**: it appears to be the project’s own documentation and product description rather than a third-party summary. It is best used as **refer-back** material for setup, commands, and feature recall rather than deep study. Scrape quality is **good** overall: the main README content, code blocks, tables, and feature lists are present, though linked docs themselves and any repository assets/images are not included here.
