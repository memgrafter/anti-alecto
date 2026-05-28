---
url: https://github.com/nicobailon/pi-discord
title: 'nicobailon/pi-discord: Discord bot that routes mentions, DMs, and slash commands to persistent Pi sessions'
scraped_at: '2026-04-19T08:03:45Z'
word_count: 2088
raw_file: raw/2026-04-19_nicobailon-pi-discord-discord-bot-that-routes-mentions-dms-and-slash-commands-to_25997ea3.txt
tldr: pi-discord is a Pi extension that runs a detached Discord bot daemon so Pi can handle Discord mentions, DMs, and slash commands with persistent per-channel sessions, file uploads, reactions, and durable queue/journal state.
key_quote: Each channel gets its own persistent Pi session, so follow-up questions remember earlier conversation.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- discord
- pi
libraries: []
companies:
- GitHub
tags:
- discord-bot
- persistent-sessions
- daemon-processes
- queueing
- developer-tools
---

### TL;DR
`pi-discord` is a Pi extension that runs a detached Discord bot daemon so Pi can handle Discord mentions, DMs, and slash commands with persistent per-channel sessions, file uploads, reactions, and durable queue/journal state.

### Key Quote
“Each channel gets its own persistent Pi session, so follow-up questions remember earlier conversation.”

### Summary
- **What it is**
  - A GitHub project for a Discord bot extension called `pi-discord`.
  - It “brings Pi into your server” by routing Discord mentions, DMs, and slash commands into Pi sessions.
  - Uses a **detached daemon** so the bot stays connected independently of any interactive Pi session.

- **Core behavior**
  - Each Discord route is scoped by **guild/channel/thread IDs**.
  - Each route gets a **persistent Pi session**, so follow-up messages retain context.
  - The bot streams responses back into Discord and throttles message edits while the assistant is generating.
  - Operator control is exposed through Pi commands like `/discord start`, `/discord stop`, `/discord status`, and `/discord logs`.

- **Main features**
  - Discord-side commands:
    - `/pi ask text:"..."`
    - `/pi status`
    - `/pi stop`
    - `/pi reset`
  - Pi-side commands:
    - `/discord setup`
    - `/discord open-config`
    - `/discord sync-commands`
    - `/discord start`
    - `/discord stop`
    - `/discord status`
    - `/discord logs [lines]`
    - `/discord help`
  - Bot tools:
    - `discord_upload` for sending files back to Discord
    - `discord_react` for adding emoji reactions
  - Reacts to user emoji as passive context on the next turn.
  - Supports ambient context journaling for non-mention messages once a route exists.

- **Install and quick start**
  - Install with:
    ```bash
    pi install npm:pi-discord
    ```
  - Then restart Pi.
  - Typical setup flow:
    ```text
    /discord setup
    /discord start
    /discord status
    ```
  - Example usage in Discord:
    ```text
    /pi ask text:"Check the repo status and summarize"
    @your-bot inspect the latest error screenshot
    ```

- **Discord app setup requirements**
  - Create an app in the Discord Developer Portal.
  - Copy:
    - `Application ID`
    - bot `Token`
  - Enable **Message Content Intent** if you want mention-based prompting, ambient context, attachment ingestion, or natural chat behavior.
  - Invite bot with scopes:
    - `bot`
    - `applications.commands`
  - Recommended permissions include:
    - View Channels
    - Send Messages
    - Create Public Threads
    - Send Messages in Threads
    - Read Message History
    - Attach Files
    - Embed Links
  - Supports guild allowlisting via server IDs.

- **Config and runtime layout**
  - Runtime config file:
    - `~/.pi/agent/pi-discord/config.json`
  - Important config fields include:
    - `botToken`
    - `applicationId`
    - `allowedGuildIds`
    - `adminUserIds`
    - `dmAllowlistUserIds`
    - `commandName` (defaults to `pi`)
    - `registerCommandsGlobally`
    - `syncCommandsOnStart`
    - `workspaceMode`
    - `allowProjectExtensions`
    - `enableImageInput`
    - `enableDetailsThreads`
    - `globalConcurrency`
    - `queueLeaseMs`
    - `primaryFlushMs`
    - `defaultModel`
    - `defaultThinkingLevel`
  - Mutable runtime state is stored separately under:
    - `~/.pi/agent/pi-discord`
  - That directory contains logs, route journals, session files, attachments, and dedicated workspaces.

- **Routing and session model**
  - A route key is built from:
    - guild id or `dm`
    - channel id
    - optional thread id
  - Each route keeps:
    - manifest
    - durable queue
    - append-only journal
    - memory file
    - session storage
    - attachment folders
    - execution root
  - Sessions are created with `createAgentSession()` and run headlessly.
  - Raw Discord text is passed through with `expandPromptTemplates: false` so Discord commands remain literal unless explicitly handled.

- **Attachments and images**
  - Incoming attachments are downloaded before the run.
  - Images are passed to the model if supported; otherwise the file path is included in context.
  - Outbound files can be posted back to Discord via `discord_upload`.

- **Observability and recovery**
  - Logs are written to:
    - `~/.pi/agent/pi-discord/logs/daemon.log`
  - `/discord status` reports whether the daemon is running, its PID, route count, and active runs.
  - Durable queues use leased work items so abandoned jobs can be recovered after a crash.
  - On startup, the daemon recovers expired leases and backfills recent channel messages into journals.

- **Safety and access control**
  - DMs are deny-by-default unless the sender is in `dmAllowlistUserIds`.
  - Stop/reset controls are restricted to `adminUserIds`.
  - Project extensions are disabled by default because many assume interactive human supervision.
  - Route state is kept separate from the extension package so updates won’t overwrite runtime data.

- **Limitations**
  - No `launchd` or systemd service generation yet.
  - No UI for editing route overrides.
  - No full setup wizard beyond `/discord setup`.
  - Gateway-only; no webhook ingestion.
  - Some config fields exist for architectural reasons but are not fully exercised.

- **Development/testing**
  - Test commands:
    ```bash
    npm install
    npm test
    ```
  - Tests focus on config validation, recovery, route identity/init, persistence hardening, interaction scoping, daemon status handling, and authorization.

### Assessment
This is a high-density, practical reference/implementation document with medium-to-high durability: the architectural ideas around Discord routing, persistent sessions, durable queues, and journaling are fairly timeless, but the exact setup steps, Discord intents/permissions, and Pi commands are version- and product-specific. The content is mostly a **reference/tutorial mix** and appears to be **primary source** project documentation rather than commentary. It’s best used as a **refer-back** resource when setting up, debugging, or evaluating the extension. Scrape quality looks **good**: the text captures most major sections, commands, config fields, limitations, and troubleshooting notes, though embedded images and any repository code are not included.
