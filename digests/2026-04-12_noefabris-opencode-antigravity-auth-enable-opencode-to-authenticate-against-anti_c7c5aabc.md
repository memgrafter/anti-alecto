---
url: https://github.com/NoeFabris/opencode-antigravity-auth
title: 'NoeFabris/opencode-antigravity-auth: Enable Opencode to authenticate against Antigravity (Google''s IDE) via OAuth so you can use Antigravity rate limits and access models like gemini-3-pro and claude-opus-4-5-thinking with your Google credentials.'
scraped_at: '2026-04-12T07:25:45Z'
word_count: 2891
raw_file: raw/2026-04-12_noefabris-opencode-antigravity-auth-enable-opencode-to-authenticate-against-anti_c7c5aabc.txt
tldr: A GitHub README for an unofficial OpenCode plugin that uses Google OAuth to access Antigravity and Gemini CLI quotas, with multi-account rotation, model routing, and extensive troubleshooting—while explicitly warning that it may violate Google’s Terms of Service and risk account bans.
key_quote: Using this plugin (and any proxy for antgravity) violate Google's Terms of Service.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- NoeFabris
- jenslys
tools:
- OpenCode
- Antigravity
- Gemini CLI
- oh-my-opencode
- dcp
libraries: []
companies:
- Google
tags:
- oauth
- cli-tools
- model-routing
- multi-account
- troubleshooting
---

### TL;DR
A GitHub README for an unofficial OpenCode plugin that uses Google OAuth to access Antigravity and Gemini CLI quotas, with multi-account rotation, model routing, and extensive troubleshooting—while explicitly warning that it may violate Google’s Terms of Service and risk account bans.

### Key Quote
“Using this plugin (and any proxy for antgravity) violate Google's Terms of Service.”

### Summary
- **What it is**
  - `opencode-antigravity-auth` is an OpenCode plugin that authenticates with Google via OAuth to use Antigravity-based access and Gemini CLI quotas.
  - It is presented as a way to use models like `gemini-3.1-pro`, `gemini-3-flash`, `claude-opus-4-6-thinking`, and `claude-sonnet-4-6` with Google credentials.

- **Main benefits claimed**
  - Access to **Claude Opus 4.6 / Sonnet 4.6** and **Gemini 3.1 Pro/Flash** via OAuth.
  - **Multi-account support** with automatic rotation when an account is rate-limited.
  - **Dual quota system**: Antigravity and Gemini CLI quotas.
  - **Thinking model support** with configurable budgets/levels.
  - **Google Search grounding** for Gemini models.
  - **Auto-recovery** from session/tool failures.
  - Compatibility with other OpenCode plugins like **oh-my-opencode** and **dcp**.

- **Major warning / risk**
  - The README includes a strong Terms of Service warning:
    - It says use of the plugin or any proxy for Antigravity violates Google’s Terms of Service.
    - It claims some users reported Google accounts being banned or shadow-banned.
  - The project is explicitly unofficial and not endorsed by Google.

- **Installation**
  - Add the plugin to `~/.config/opencode/opencode.json`:
    ```json
    { "plugin": ["opencode-antigravity-auth@latest"] }
    ```
  - Optional bleeding-edge version:
    - `opencode-antigravity-auth@beta`
  - Authenticate with:
    ```bash
    opencode auth login
    ```
  - Then configure models either automatically through the login flow or manually by copying the provided model config into `opencode.json`.
  - Example usage:
    ```bash
    opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
    ```

- **Model routing and naming**
  - The README distinguishes between:
    - **Antigravity quota** models, including:
      - `antigravity-gemini-3-pro`
      - `antigravity-gemini-3.1-pro`
      - `antigravity-gemini-3-flash`
      - `antigravity-claude-sonnet-4-6`
      - `antigravity-claude-opus-4-6-thinking`
    - **Gemini CLI quota** models, including:
      - `gemini-2.5-flash`
      - `gemini-2.5-pro`
      - `gemini-3-flash-preview`
      - `gemini-3-pro-preview`
      - `gemini-3.1-pro-preview`
      - `gemini-3.1-pro-preview-customtools`
  - Default behavior:
    - Gemini models route to Antigravity quota first.
    - If `cli_first: true`, Gemini CLI quota is used first.
    - When one quota pool is exhausted, the plugin falls back to the other.
  - Claude and image models always use Antigravity.
  - The README provides a full copy-paste JSON configuration with context/output limits, modalities, and variant settings.

- **Variants / thinking settings**
  - Example variant use:
    ```bash
    opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
    ```
  - Gemini variants map to different thinking levels like `minimal`, `low`, `medium`, and `high`.
  - Claude Opus 4.6 thinking variants use budgets such as:
    - `8192`
    - `32768`

- **Multi-account setup**
  - Users can add multiple Google accounts by running `opencode auth login` again.
  - The plugin can:
    - rotate accounts automatically
    - show quotas per account
    - enable/disable accounts
  - It recommends different strategies depending on account count:
    - `sticky` for one account
    - `hybrid` for 2–5 accounts
    - `round-robin` for 5+ accounts
  - `pid_offset_enabled: true` is recommended for parallel agents.

- **Configuration options**
  - Optional config file: `~/.config/opencode/antigravity.json`
  - Main behavior options include:
    - `keep_thinking`
    - `session_recovery`
    - `cli_first`
  - Quota/rate-limit controls include:
    - `soft_quota_threshold_percent`
    - `quota_refresh_interval_minutes`
    - `soft_quota_cache_ttl_minutes`
    - `scheduling_mode`
    - `max_cache_first_wait_seconds`
    - `failure_ttl_seconds`
  - App behavior options include:
    - `quiet_mode`
    - `debug`
    - `debug_tui`
    - `auto_update`
  - Environment variables are documented for custom config path and debug logging.

- **Troubleshooting coverage**
  - The README is unusually extensive in troubleshooting:
    - deleting `antigravity-accounts.json` and re-authenticating
    - Windows path handling
    - 403 permission denied errors tied to missing project IDs
    - “Model not found” fixes
    - Gemini 3 “Unknown name 'parameters'” errors
    - MCP schema compatibility issues
    - rate-limit cascade bugs
    - session recovery commands like `continue` and `/undo`
    - Safari OAuth callback issues
    - port conflicts
    - Docker/WSL2/remote development limitations
    - configuration typo: `plugin` vs `plugins`
    - migration of accounts between machines
  - It also documents interaction issues with:
    - `@tarquinen/opencode-dcp`
    - `oh-my-opencode`
    - other Google auth plugins

- **Documentation references**
  - The README points to separate docs for:
    - `docs/CONFIGURATION.md`
    - `docs/MULTI-ACCOUNT.md`
    - `docs/MODEL-VARIANTS.md`
    - `docs/TROUBLESHOOTING.md`
    - `docs/ARCHITECTURE.md`
    - `docs/ANTIGRAVITY_API_SPEC.md`

- **Overall tone and purpose**
  - This is primarily a **tool/plugin reference and setup guide**, with strong operational detail.
  - It reads like a practical install/configuration README aimed at users who want to run OpenCode with Google-authenticated model access, especially through multiple accounts and quota-routing strategies.

### Assessment
Durability is **medium**: the general ideas around OAuth-based auth, quota routing, and multi-account load balancing are reusable, but many details are tightly coupled to specific model names, quotas, bugs, and Google/OpenCode behavior that may change quickly. The content type is **mixed**, leaning heavily toward **reference** and **tutorial** rather than opinion. Density is **high** because it includes concrete commands, JSON config, model tables, error messages, and troubleshooting steps. Originality is mostly **primary source** for this plugin’s own setup, behavior, and claims, though it also contains some commentary and warnings. It is best used as a **refer-back** resource, especially for installation, configuration, and error diagnosis. Scrape quality appears **good**: the README content is largely intact, including code blocks, tables, and warning sections, though external linked docs and screenshots/badges are not actually fetched here.
