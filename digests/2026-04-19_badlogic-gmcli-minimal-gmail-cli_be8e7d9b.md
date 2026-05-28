---
url: https://github.com/badlogic/gmcli
title: 'badlogic/gmcli: Minimal Gmail CLI'
scraped_at: '2026-04-19T08:28:23Z'
word_count: 673
raw_file: raw/2026-04-19_badlogic-gmcli-minimal-gmail-cli_be8e7d9b.txt
tldr: gmcli is a minimal Node.js command-line client for Gmail that supports account setup, search, thread viewing, label management, draft handling, sending mail, and generating Gmail thread URLs.
key_quote: Minimal Gmail CLI for searching, reading threads, managing labels, drafts, and sending emails.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- gmcli
libraries: []
companies:
- Google
tags:
- command-line-tools
- gmail
- email-management
- nodejs
- oauth
---

### TL;DR
`gmcli` is a minimal Node.js command-line client for Gmail that supports account setup, search, thread viewing, label management, draft handling, sending mail, and generating Gmail thread URLs.

### Key Quote
“Minimal Gmail CLI for searching, reading threads, managing labels, drafts, and sending emails.”

### Summary
- **What it is**
  - A Gmail CLI tool called `gmcli`.
  - Intended for basic Gmail operations from the terminal: search, inspect threads, manage labels, work with drafts, send emails, and create Gmail web URLs.
  - Published as `@mariozechner/gmcli`.

- **Install**
  - Global install via npm:
    ```bash
    npm install -g @mariozechner/gmcli
    ```

- **Setup requirements**
  - Requires Google Cloud Console OAuth2 credentials before adding accounts.
  - Setup steps:
    - Create or select a Google Cloud project
    - Enable the Gmail API
    - Set an app name in OAuth branding
    - Add test users for each Gmail account to use
    - Create an OAuth client of type **Desktop app**
    - Download the JSON credentials file
  - Then configure the CLI:
    ```bash
    gmcli accounts credentials ~/path/to/credentials.json
    gmcli accounts add you@gmail.com
    ```

- **Command structure**
  - General usage:
    ```bash
    gmcli accounts <action>
    gmcli <email> <command> [options]
    ```
  - The first form manages stored accounts; the second performs Gmail actions against a specific email account.

- **Accounts management**
  - `gmcli accounts credentials <file.json>` — set OAuth credentials once
  - `gmcli accounts list` — list configured accounts
  - `gmcli accounts add <email>` — add an account and open browser auth flow
  - `gmcli accounts add <email> --manual` — browserless flow using a pasted redirect URL
  - `gmcli accounts remove <email>` — remove an account

- **Search**
  - Searches Gmail threads using standard Gmail query syntax.
  - Returns thread metadata like thread ID, date, sender, subject, and labels.
  - Example syntax includes:
    - folders/state: `in:inbox`, `in:sent`, `in:drafts`, `in:trash`, `in:spam`
    - flags: `is:unread`, `is:starred`, `is:important`
    - participants: `from:...`, `to:...`
    - content/attachment filters: `subject:...`, `has:attachment`, `filename:pdf`
    - dates: `after:2024/01/01`, `before:2024/12/31`
    - labels: `label:Work`, `label:UNREAD`
  - Supports combining terms with spaces.
  - Example:
    ```bash
    gmcli you@gmail.com search "from:someone@example.com has:attachment"
    ```

- **Thread viewing**
  - Retrieves a full thread including all messages.
  - Shows:
    - `Message-ID`
    - headers
    - body
    - attachments
  - Can download attachments:
    ```bash
    gmcli <email> thread <threadId> --download
    ```
  - Downloaded attachments go to `~/.gmcli/attachments/`.

- **Labels**
  - List labels:
    ```bash
    gmcli <email> labels list
    ```
  - Modify labels on one or more thread IDs:
    ```bash
    gmcli <email> labels <threadIds...> [--add L] [--remove L]
    ```
  - Accepts either label names or IDs when modifying labels.
  - Notes system labels: `INBOX`, `UNREAD`, `STARRED`, `IMPORTANT`, `TRASH`, `SPAM`

- **Drafts**
  - List, view, download attachments from, delete, send, and create drafts.
  - Commands:
    - `drafts list`
    - `drafts get <draftId>`
    - `drafts get <draftId> --download`
    - `drafts delete <draftId>`
    - `drafts send <draftId>`
    - `drafts create --to ... --subject ... --body ...`
  - Draft creation supports:
    - `--cc`
    - `--bcc`
    - `--reply-to <messageId>` for threading / `In-Reply-To` and `References`
    - `--attach <file>` multiple times

- **Sending mail**
  - Send directly without creating a draft:
    ```bash
    gmcli <email> send --to <emails> --subject <s> --body <b> [options]
    ```
  - Uses the same recipient, CC/BCC, reply threading, and attachment options as draft creation.
  - Examples include sending a plain email or a reply with an attachment.

- **URL generation**
  - Generates canonical Gmail web URLs for thread IDs:
    ```bash
    gmcli <email> url <threadIds...>
    ```
  - Useful for opening the thread in Gmail regardless of browser account ordering.

- **Data storage**
  - Stores all local data in `~/.gmcli/`:
    - `credentials.json` — OAuth client credentials
    - `accounts.json` — account tokens
    - `attachments/` — downloaded attachments

- **Development and publishing**
  - Development commands:
    ```bash
    npm install
    npm run build
    npm run check
    ```
  - Publishing notes:
    - update version in `package.json` and `CHANGELOG.md`
    - `npm run build`
    - `npm publish --access public`
    - tag release and push tags

- **License**
  - MIT

### Assessment
This is a high-durability reference/documentation page for a small CLI tool, with medium-to-high density because it packs install steps, OAuth setup, command syntax, and examples into a concise format. It is a mix of reference and tutorial: mostly practical docs rather than opinion or commentary. The originality is primarily source documentation from the project itself, so it’s the authoritative place to confirm command names and options, though it will become stale if the CLI or Gmail API flows change. It’s best used as a refer-back reference when installing or using `gmcli`, not as deep-study material. Scrape quality is good: the core README content appears intact, including command examples and setup instructions, with no obvious missing sections beyond any GitHub UI elements not captured here.
