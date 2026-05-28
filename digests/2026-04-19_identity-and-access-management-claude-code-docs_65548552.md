---
url: https://code.claude.com/docs/en/iam
title: Identity and Access Management - Claude Code Docs
scraped_at: '2026-04-19T03:59:28Z'
word_count: 1400
raw_file: raw/2026-04-19_identity-and-access-management-claude-code-docs_65548552.txt
tldr: Claude Code’s authentication docs explain how to log in as an individual or team, how enterprise and cloud-provider setups work, where credentials are stored, and which credential source takes precedence when multiple are present.
key_quote: “Claude Code supports multiple authentication methods depending on your setup.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- claude
libraries: []
companies:
- Anthropic
tags:
- authentication
- identity-access-management
- credential-management
- cli-tools
- enterprise-software
---

### TL;DR
Claude Code’s authentication docs explain how to log in as an individual or team, how enterprise and cloud-provider setups work, where credentials are stored, and which credential source takes precedence when multiple are present.

### Key Quote
“Claude Code supports multiple authentication methods depending on your setup.”

### Summary
- **Purpose of the page**
  - Explains how to authenticate Claude Code for **individual users, teams, organizations, and CI/scripts**.
  - Covers login flow, team setup options, credential storage, precedence rules, and long-lived token generation.

- **Logging in to Claude Code**
  - After installing Claude Code, run `claude` in the terminal.
  - First launch opens a browser for login.
  - If the browser doesn’t open, press `c` to copy the login URL.
  - If prompted with a login code, paste it into the terminal at `Paste code here if prompted`.
  - Supported account types:
    - **Claude Pro or Max**: sign in with a Claude.ai account
    - **Claude for Teams or Enterprise**: sign in with the invited team account
    - **Claude Console**: sign in with Console credentials after invitation
    - **Cloud providers**: use env vars for **Amazon Bedrock**, **Google Vertex AI**, or **Microsoft Foundry**
  - Logout/re-authenticate with `/logout`.

- **Team and organization authentication options**
  - Recommended path for most teams: **Claude for Teams or Enterprise**
  - Other supported org setups:
    - **Claude Console**
    - **Amazon Bedrock**
    - **Google Vertex AI**
    - **Microsoft Foundry**

- **Claude for Teams / Enterprise**
  - Positioned as the “best experience” for organizations using Claude Code.
  - Shared benefits:
    - Access to **Claude Code** and **Claude on the web**
    - **Centralized billing**
    - **Team management**
  - Differences:
    - **Claude for Teams**
      - Self-service
      - Collaboration features
      - Admin tools and billing management
      - Best for smaller teams
    - **Claude for Enterprise**
      - Adds **SSO**
      - **Domain capture**
      - **Role-based permissions**
      - **Compliance API**
      - **Managed policy settings**
      - Best for larger orgs with security/compliance needs
  - Setup steps:
    1. Subscribe/contact sales
    2. Invite team members from admin dashboard
    3. Members install Claude Code and log in with Claude.ai accounts

- **Claude Console authentication**
  - Meant for organizations preferring **API-based billing**.
  - Setup steps:
    1. Create or use a Claude Console account
    2. Add users via:
       - Console invite path: `Settings -> Members -> Invite`
       - Or **SSO**
    3. Assign roles:
       - **Claude Code** role: can only create Claude Code API keys
       - **Developer** role: can create any API key
    4. Users:
       - Accept invite
       - Check system requirements
       - Install Claude Code
       - Log in with Console credentials

- **Cloud provider authentication**
  - For teams using:
    - **Amazon Bedrock**
    - **Google Vertex AI**
    - **Microsoft Foundry**
  - Steps:
    1. Follow the provider-specific setup docs
    2. Distribute required environment variables and credential-generation instructions
    3. Install Claude Code
  - No browser login is needed in this path.

- **Credential management**
  - Claude Code stores credentials securely, with storage varying by OS:
    - **macOS**: encrypted **Keychain**
    - **Linux/Windows**: `~/.claude/.credentials.json`
    - If set, `$CLAUDE_CONFIG_DIR` changes the location
    - On Linux, file mode is `0600`
    - On Windows, it inherits user profile access controls
  - Supported auth types stored/handled:
    - Claude.ai credentials
    - Claude API credentials
    - Azure Auth
    - Bedrock Auth
    - Vertex Auth
  - `apiKeyHelper` can run a shell script to supply an API key.
  - Default refresh timing:
    - Recalled after **5 minutes** or on **HTTP 401**
    - Custom TTL via `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`
  - If `apiKeyHelper` takes **more than 10 seconds**, Claude Code shows a warning in the prompt bar.
  - Important limitation:
    - `apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` apply to **terminal CLI sessions only**
    - **Claude Desktop** and **remote sessions** use **OAuth exclusively** and do not read these env vars or call `apiKeyHelper`

- **Authentication precedence**
  - If multiple credentials exist, Claude Code uses them in this order:
    1. **Cloud provider credentials** when one of:
       - `CLAUDE_CODE_USE_BEDROCK`
       - `CLAUDE_CODE_USE_VERTEX`
       - `CLAUDE_CODE_USE_FOUNDRY`
    2. **`ANTHROPIC_AUTH_TOKEN`**
       - Sent as `Authorization: Bearer`
       - Useful for LLM gateways/proxies that use bearer tokens
    3. **`ANTHROPIC_API_KEY`**
       - Sent as `X-Api-Key`
       - For direct Anthropic API access
       - In interactive mode, user approves/declines once
       - In non-interactive mode (`-p`), it is always used if present
    4. **`apiKeyHelper`** output
       - Useful for dynamic/rotating credentials from a vault
    5. **`CLAUDE_CODE_OAUTH_TOKEN`**
       - A long-lived OAuth token from `claude setup-token`
       - Intended for CI/scripts without browser login
    6. **Subscription OAuth credentials from `/login`**
       - Default for Pro, Max, Team, Enterprise
  - Important caveat:
    - If you have a Claude subscription but also set `ANTHROPIC_API_KEY`, the API key takes precedence once approved.
    - This can break authentication if the key belongs to a disabled/expired org.
    - Suggested fix: `unset ANTHROPIC_API_KEY` and verify with `/status`.
  - Claude Code on the Web always uses subscription credentials.
  - `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` in the sandbox do not override web credentials.

- **Generating a long-lived token**
  - For CI pipelines or scripts without browser login:
    - Run:
      ```bash
      claude setup-token
      ```
  - The command performs OAuth authorization and prints a token to the terminal.
  - The token is **not saved automatically**; the user must copy it and set:
    ```bash
    export CLAUDE_CODE_OAUTH_TOKEN=your-token
    ```
  - Characteristics:
    - Works with **Claude subscription**
    - Requires **Pro, Max, Team, or Enterprise**
    - Scopes to **inference only**
    - Cannot establish **Remote Control** sessions
    - **Bare mode** does not read `CLAUDE_CODE_OAUTH_TOKEN`
    - For `--bare`, use `ANTHROPIC_API_KEY` or `apiKeyHelper` instead

### Assessment
This is a **reference**-style documentation page with high practical density and mostly durable guidance, though some specifics are version- and product-policy-dependent and may change over time. The content type is **mixed** but primarily **reference/tutorial**: it combines login instructions, team setup steps, credential storage details, and precedence rules. Originality is **primary source** because it documents Claude Code’s own authentication behavior and configuration. It’s best used as a **refer-back** resource, not a one-time skim, since it contains exact environment variables, command names, and precedence ordering that users may need later. Scrape quality is **good**: the page structure, headings, steps, and key technical details are present; however, visual elements and any interactive UI behavior are naturally absent, and the page title/header appears duplicated as “Authentication”/“Identity and Access Management,” which suggests the scrape captured the content but not the full site chrome perfectly.
