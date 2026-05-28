---
url: https://github.com/googleworkspace/cli
title: 'googleworkspace/cli: Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.'
scraped_at: '2026-04-19T07:13:06Z'
word_count: 2657
raw_file: raw/2026-04-19_googleworkspace-cli-google-workspace-cli-one-command-line-tool-for-drive-gmail-c_d752d525.txt
tldr: gws is an actively developed, unofficial Google Workspace CLI that dynamically discovers API surfaces at runtime, supports structured JSON output, and includes many built-in helper commands plus AI agent skills.
key_quote: gws doesn't ship a static list of commands. It reads Google's own Discovery Service at runtime and builds its entire command surface dynamically.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- gws
- gcloud
- npm
- nix
- brew
- gemini
- OpenClaw
- jq
libraries:
- dotenvy
companies:
- Google
- Google Workspace
- GitHub
tags:
- command-line-tools
- google-workspace
- api-clients
- authentication
- developer-tools
---

### TL;DR
`gws` is an actively developed, unofficial Google Workspace CLI that dynamically discovers API surfaces at runtime, supports structured JSON output, and includes many built-in helper commands plus AI agent skills.

### Key Quote
> "gws doesn't ship a static list of commands. It reads Google's own Discovery Service at runtime and builds its entire command surface dynamically."

### Summary
- **What it is**
  - A command-line tool named **`gws`** for interacting with **Google Workspace APIs**: Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more.
  - Built for both **humans and AI agents**.
  - Explicitly states it is **not an officially supported Google product**.

- **Core design**
  - Does **not** have a static command list.
  - Uses Google’s **Discovery Service** at runtime to generate its command surface dynamically.
  - Automatically picks up new API endpoints/methods when Google adds them.
  - Outputs **structured JSON** for successes, errors, and metadata.

- **Why use it**
  - For humans:
    - Avoids hand-writing `curl` against REST docs.
    - Gives `--help` on resources.
    - Supports `--dry-run`.
    - Supports auto-pagination.
  - For AI agents:
    - Structured JSON responses make it easier for LLM-based agents to use.
    - Comes with **40+ agent skills** and broader mention of **100+ Skill files** plus 50 curated recipes.

- **Installation options**
  - Recommended: download a pre-built binary from **GitHub Releases**.
  - Via npm:
    ```bash
    npm install -g @googleworkspace/cli
    ```
  - Build from source:
    ```bash
    cargo install --git https://github.com/googleworkspace/cli --locked
    ```
  - Nix:
    ```bash
    nix run github:googleworkspace/cli
    ```
  - Homebrew:
    ```bash
    brew install googleworkspace-cli
    ```

- **Prerequisites**
  - **Node.js 18+** for npm installation.
  - A **Google Cloud project** for OAuth credentials.
  - A **Google account** with Workspace access.

- **Quick start**
  - Typical flow:
    ```bash
    gws auth setup
    gws auth login
    gws drive files list --params '{"pageSize": 5}'
    ```

- **Authentication model**
  - Supports several auth paths:
    - Interactive local desktop login via `gws auth setup` / `gws auth login`
    - Manual OAuth setup in Google Cloud Console
    - Pre-obtained access token via `GOOGLE_WORKSPACE_CLI_TOKEN`
    - Credentials file via `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`
    - Service account server-to-server use
    - Exported credentials for CI/headless environments
  - Credentials are encrypted at rest using **AES-256-GCM** with keyring support, or a file-based fallback.
  - Important warning: if the OAuth app is in **testing mode**, Google limits consent to about **25 scopes**, so the `recommended` preset with **85+ scopes** can fail.

- **Agent skills / integrations**
  - Includes many **Agent Skills** (`SKILL.md` files) for API-specific and workflow-specific tasks.
  - Installation examples are provided using `npx skills add`.
  - Has setup notes for **OpenClaw**.
  - Includes a **Gemini CLI extension**:
    ```bash
    gemini extensions install https://github.com/googleworkspace/cli
    ```
  - The extension lets Gemini CLI use `gws` commands and skills while inheriting authenticated terminal credentials.

- **Useful command examples**
  - List files:
    ```bash
    gws drive files list --params '{"pageSize": 10}'
    ```
  - Create a spreadsheet:
    ```bash
    gws sheets spreadsheets create --json '{"properties": {"title": "Q1 Budget"}}'
    ```
  - Send a Chat message:
    ```bash
    gws chat spaces messages create --params '{"parent": "spaces/xyz"}' --json '{"text": "Deploy complete."}' --dry-run
    ```
  - Inspect schema:
    ```bash
    gws schema drive.files.list
    ```
  - Stream paginated results:
    ```bash
    gws drive files list --params '{"pageSize": 100}' --page-all
    ```

- **Advanced usage**
  - Multipart upload support:
    ```bash
    gws drive files create --json '{"name": "report.pdf"}' --upload ./report.pdf
    ```
  - Pagination controls:
    - `--page-all`
    - `--page-limit <N>`
    - `--page-delay <MS>`
  - Sheets shell-escaping warning:
    - Use **single quotes** around values containing `!`.
  - Helper commands are prefixed with `+` to avoid collisions with generated method names:
    - Gmail: `+send`, `+reply`, `+reply-all`, `+forward`, `+triage`, `+watch`
    - Sheets: `+append`, `+read`
    - Docs: `+write`
    - Chat: `+send`
    - Drive: `+upload`
    - Calendar: `+insert`, `+agenda`
    - Workflow helpers: `+standup-report`, `+meeting-prep`, `+email-to-task`, `+weekly-digest`, `+file-announce`
    - Events: `+subscribe`, `+renew`
    - Model Armor: prompt/response sanitization and template creation
  - Time-aware helpers use the **Google account timezone** unless overridden.

- **Model Armor integration**
  - Can sanitize prompts or responses via Google Cloud **Model Armor**.
  - Configurable through:
    - `GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE`
    - `GOOGLE_WORKSPACE_CLI_SANITIZE_MODE` (`warn` or `block`)

- **Environment variables**
  - Key variables include:
    - `GOOGLE_WORKSPACE_CLI_TOKEN`
    - `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`
    - `GOOGLE_WORKSPACE_CLI_CLIENT_ID`
    - `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET`
    - `GOOGLE_WORKSPACE_CLI_CONFIG_DIR`
    - `GOOGLE_WORKSPACE_CLI_LOG`
    - `GOOGLE_WORKSPACE_CLI_LOG_FILE`
    - `GOOGLE_WORKSPACE_PROJECT_ID`
  - Supports `.env` files via `dotenvy`.

- **Exit codes**
  - Structured exit codes help scripts branch on failure type:
    - `0` success
    - `1` API error
    - `2` auth error
    - `3` validation error
    - `4` discovery error
    - `5` internal error

- **Architecture**
  - Two-phase parsing:
    1. Parse service name from `argv[1]`
    2. Fetch Discovery Document
    3. Build a `clap::Command` tree dynamically
    4. Re-parse arguments
    5. Authenticate and execute request
  - Discovery docs are cached for **24 hours**.

- **Troubleshooting highlights**
  - “Access blocked” or 403 during login usually means the OAuth app is in testing mode and the user is not added as a test user.
  - “Google hasn't verified this app” is expected in testing mode.
  - Too many scopes: pick only needed scopes.
  - `gcloud` not found: install it or use manual Cloud Console setup.
  - `redirect_uri_mismatch`: OAuth client should be a **Desktop app**.
  - `accessNotConfigured`: required Google API is not enabled in the GCP project; `gws` prints an enable link and suggests enabling the API.

- **Development**
  - Rust-based development workflow:
    - `cargo build`
    - `cargo clippy -- -D warnings`
    - `cargo test`
    - `./scripts/coverage.sh`
  - License: **Apache-2.0**

### Assessment
Durability is **medium**: the concepts behind a dynamically generated CLI for Google Workspace and the authentication patterns are broadly useful, but many details are tied to the current project state, APIs, scope limits, and install paths. Content type is **mixed**—mostly a **reference/docs** page with tutorial-style quick start and troubleshooting sections. Density is **high** because it packs installation, auth, architecture, environment variables, commands, and troubleshooting into one README. Originality is **primary source** since it documents the project itself. Reference style is **refer-back**: useful for installation, auth setup, and command syntax when actually using the tool. Scrape quality is **good**: the main README structure, examples, tables, and sections are present; no obvious major sections appear missing from the provided content.
