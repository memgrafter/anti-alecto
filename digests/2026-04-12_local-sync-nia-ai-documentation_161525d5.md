---
url: https://docs.trynia.ai/local-sync
title: Local Sync - Nia AI Documentation
scraped_at: '2026-04-12T07:30:57Z'
word_count: 901
raw_file: raw/2026-04-12_local-sync-nia-ai-documentation_161525d5.txt
tldr: Nia AI’s Local Sync docs explain how to privately index local folders and databases via a CLI daemon, with commands for adding sources, monitoring sync, controlling updates, and searching synced content from the terminal or web app.
key_quote: “Local folders are private to your account. They’re searched separately from public repositories and documentation.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- nia
libraries: []
companies:
- Nia AI
tags:
- local-sync
- cli
- data-indexing
- privacy
- synchronization
---

### TL;DR
Nia AI’s Local Sync docs explain how to privately index local folders and databases via a CLI daemon, with commands for adding sources, monitoring sync, controlling updates, and searching synced content from the terminal or web app.

### Key Quote
“Local folders are private to your account. They’re searched separately from public repositories and documentation.”

### Summary
- **What Local Sync is**
  - A privacy-first sync feature for Nia AI that lets you add **local folders or databases** to your account.
  - Local sources are **kept separate from public repositories and documentation**.
  - The CLI can **auto-detect known database paths** such as **iMessage** and browser history databases.

- **Getting started / setup flow**
  - **Add a source**: sync a local folder or database.
  - **Start syncing**: run the sync daemon, which watches files and syncs incrementally in real time.
  - The daemon uses native filesystem events in watch mode and also has fallback polling.

- **Core CLI commands**
  - `nia` — starts the sync daemon in watch mode by default
  - `nia login` / `nia logout` — browser-based OAuth login and credential clearing
  - `nia status` / `nia status --json` — show configured sources and sync state
  - `nia once` — run a one-time sync and exit
  - `nia add <path>` — add a source
  - `nia link <ID> <path>` — link a cloud source to a local path
  - `nia remove <ID>` — remove a source
  - `nia upgrade` — check and install updates

- **Search and query from the terminal**
  - Search indexed sources directly in the CLI.
  - Useful flags:
    - `-l, --local-folder` — restrict search to specific local folders by ID prefix or display name
    - `--sources` — show source snippets used to generate answers
    - `--markdown/--no-markdown` — toggle Markdown rendering
    - `--stream/--no-stream` — toggle streaming output
    - `-j, --json` — output raw JSON
    - `-n, --limit` — limit source snippets shown

- **Monitoring and debugging**
  - `nia info <ID>` — detailed source info, including chunk count, last sync, and errors
  - `nia logs` / `nia logs <ID>` — sync logs globally or per source
  - `nia logs --tail` — live log tailing
  - `nia logs --errors` — only error logs
  - `nia diff` / `nia diff <ID>` — dry-run sync preview without uploading
  - `nia doctor` — diagnostics for auth, API, and disk access
  - `nia whoami` — current authenticated user
  - `nia version` / `nia version --check` — CLI version and update check

- **Sync control**
  - `nia pause <ID>` — pause continuous sync for a source
  - `nia resume <ID>` — resume sync
  - `nia resync <ID>` — force a full resync
  - `nia resync --all` — force full resync for all sources

- **Daemon mode behavior**
  - Running `nia` with no arguments starts the daemon.
  - Daemon features:
    - watches for file changes using native filesystem events
    - syncs changes within seconds
    - periodically refreshes source lists from the web UI
    - auto-discovers new folders matching unlinked sources
    - sends heartbeats to indicate it is online
  - Daemon flags:
    - `--watch/--poll` — real-time watching vs interval polling
    - `-f, --fallback 600` — fallback sync interval in seconds
    - `-r, --refresh 30` — how often to check for new web UI sources

- **Supported data sources**
  - **Chat and messages**
    - iMessage: `~/Library/Messages/chat.db`
    - Telegram: JSON exports and ZIP files
  - **Browser history**
    - Safari: `~/Library/Safari/History.db`
    - Chrome / Brave / Edge
    - Firefox
  - **Databases**
    - Generic SQLite databases
    - Tables are auto-extracted into searchable text
  - **Folders**
    - Regular folders containing text files, code, notes, and documentation

- **Virtual file format for extracted data**
  - Nia converts database content into virtual text files for semantic search.
  - Examples:
    - iMessage → `messages/{contact}/{date}_{row_id}_{direction}.txt`
    - Safari/Chrome/Firefox → `history/{domain}/{date}_{id}.txt`
    - Telegram → `telegram/{chat_name}/{date}_{msg_id}.txt`

- **Web UI integration**
  - Sync sources can also be managed in the web app at **app.trynia.ai**
  - Navigate to **Settings → Local Sync**
  - From there you can view sync status, add/remove sources, and configure intervals

- **Sync intervals**
  - `5m` — every 5 minutes
  - `hourly` — every hour
  - `6h` — every 6 hours
  - `daily` — once per day

- **How local folders are searched**
  - Once synced, local folders become searchable via MCP tools.
  - Search uses a `local_folders` parameter in `search()` to include them.
  - Again, local folders are described as private and searched separately from public content.

- **Configuration**
  - Environment variable:
    - `NIA_API_URL` — defaults to `https://api.trynia.ai`
  - Credentials are stored in:
    - `~/.nia-sync/config.json`
    - with secure permissions `0600`

- **Limits**
  - Max files per folder: **5,000**
  - Max total upload size: **100 MB per folder**
  - Max individual file size: **5 MB**
  - Max database size: **1 GB**
  - Max rows per table: **100,000**

- **Security**
  - The system automatically applies **350+ exclusion patterns** to avoid syncing sensitive files.
  - Exclusions include:
    - credentials and secrets: `.env`, `.pem`, `.key`, SSH keys, `*credentials*`, `*secrets*`, `*token*`
    - version control: `.git`, `.svn`
    - dependencies: `node_modules`, `venv`, `__pycache__`
    - build outputs: `dist/`, `build/`, `.next/`

### Assessment
This is a **reference** document with high practical density, focused on CLI usage, sync behavior, supported sources, limits, and security exclusions. Its **durability is medium** because the concepts of local sync, daemon-based watching, and private indexing are broadly useful, but the exact command set, limits, URLs, and defaults are product/version-specific and may change. The content is a **mixed** primary-source product doc, not commentary, and is best used as a **refer-back** resource when setting up or troubleshooting Nia Local Sync. Scrape quality is **partial**: it captured most of the structure and command tables, but some sections are visibly compressed or missing formatting details, especially around “Quick Install,” “Web Integration,” and “Configuration Management” headings where explanatory text appears truncated.
