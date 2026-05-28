---
url: https://pitchfork.jdx.dev/cli/
title: pitchfork
scraped_at: '2026-04-19T06:54:51Z'
word_count: 127
raw_file: raw/2026-04-19_pitchfork_c09da0f8.txt
tldr: pitchfork is a CLI tool (v2.6.0) whose documentation page is essentially a command reference listing all available subcommands for managing configs, proxies, boot behavior, process lifecycles, and a TUI.
key_quote: 'Usage: pitchfork <SUBCOMMAND>'
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pitchfork
libraries: []
companies: []
tags:
- cli
- command-reference
- service-management
- proxy-management
- supervisor
---

### TL;DR
`pitchfork` is a CLI tool (v2.6.0) whose documentation page is essentially a command reference listing all available subcommands for managing configs, proxies, boot behavior, process lifecycles, and a TUI.

### Key Quote
"Usage: pitchfork <SUBCOMMAND>"

### Summary
- This page is a **CLI reference** for `pitchfork`, version **2.6.0**.
- The top-level usage is:
  - `pitchfork <SUBCOMMAND>`
- Major command groups and notable commands:
  - **Shell integration**
    - `pitchfork activate <SHELL>`
    - `pitchfork completion <SHELL>`
  - **Boot management**
    - `pitchfork boot enable`
    - `pitchfork boot disable`
    - `pitchfork boot status`
  - **Configuration**
    - `pitchfork config <SUBCOMMAND>`
    - `pitchfork config add [FLAGS] <ID> [ARGS]…`
    - `pitchfork config remove <ID>`
  - **Service/control lifecycle**
    - `pitchfork enable <ID>`
    - `pitchfork disable <ID>`
    - `pitchfork start [FLAGS] <ID>…`
    - `pitchfork stop [-a --all] [ID]…`
    - `pitchfork restart [FLAGS] [ID]…`
    - `pitchfork status <ID>`
    - `pitchfork wait <ID>`
    - `pitchfork logs [FLAGS] [ID]…`
    - `pitchfork list [--hide-header]`
    - `pitchfork clean`
    - `pitchfork tui`
  - **Proxy management**
    - `pitchfork proxy <SUBCOMMAND>`
    - `pitchfork proxy trust [--cert <CERT>]`
    - `pitchfork proxy status`
    - `pitchfork proxy add [--dir <DIR>] [--daemon <DAEMON>] <SLUG>`
    - `pitchfork proxy remove <SLUG>`
  - **Supervisor**
    - `pitchfork supervisor <SUBCOMMAND>`
    - `pitchfork supervisor run [FLAGS]`
    - `pitchfork supervisor start [-f --force]`
    - `pitchfork supervisor status`
    - `pitchfork supervisor stop`
  - **Other**
    - `pitchfork mcp`
    - `pitchfork run [FLAGS] <ID> [-- RUN]…`
- The page does **not** explain what each command does in detail; it mainly serves as a navigational index for the CLI surface.
- The presence of `mcp`, `proxy`, and `supervisor` suggests `pitchfork` is likely used to orchestrate or manage local services/components, but the page itself only confirms the command names.

### Assessment
This is a **reference** page with **high durability** at the conceptual level but **medium durability** in practice because it is tied to **version 2.6.0** and command availability may change across releases. The content is **high-density** for a command listing but **low on explanation**, making it useful as a **refer-back** lookup rather than a deep-study resource. It appears to be a **primary source** CLI help/documentation page, and the scrape quality is **good** for the visible text, though it likely omits any richer command descriptions or examples that may exist deeper in the docs.
