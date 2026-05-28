---
url: https://github.com/memgrafter/pi-pkm-mode-extension
title: 'memgrafter/pi-pkm-mode-extension: Personal knowledge management in pi.'
scraped_at: '2026-04-12T07:34:03Z'
word_count: 210
raw_file: raw/2026-04-12_memgrafter-pi-pkm-mode-extension-personal-knowledge-management-in-pi_d552fc1d.txt
tldr: A small `pi` extension that adds a personal knowledge management mode, with `/pkm` commands, optional startup behavior, and configurable storage path support.
key_quote: Personal knowledge management mode for **pi**.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
tools:
- pi
libraries: []
companies:
- memgrafter
tags:
- personal-knowledge-management
- developer-tools
- command-line
- github-repository
- configuration
---

### TL;DR
A small `pi` extension that adds a personal knowledge management mode, with `/pkm` commands, optional startup behavior, and configurable storage path support.

### Key Quote
“Personal knowledge management mode for **pi**.”

### Summary
- This GitHub repo is for **`pi-pkm-mode-extension`**, an extension that adds **personal knowledge management (PKM) mode** to **pi**.
- The quickstart says to:
  - Install pi with `npm install -g @mariozechner/pi-coding-agent`
  - Install the extension with `pi install git:github.com/memgrafter/pi-pkm-mode-extension`
  - Create a PKM folder such as `~/code/pkm`
  - Start pi with the extension loaded via `pi -e /path/to/pi-pkm-mode-extension/extensions/pi-pkm-mode.ts`
  - In pi, enable PKM with `/pkm on` or `/pkm`
  - Then prompt pi with something like: `Ask me my requirements and set up a personal knowledge management structure in ~/code/pkm.`
- Documented features:
  - `/pkm` toggle
  - `/pkm on|off|status`
  - `/pkm <text>` turns PKM mode on and immediately sends the supplied text
  - Optional startup flag: `--pkm`
  - If a PKM path is configured, the system prompt includes: `My pkm is stored in <path>`
- PKM path configuration:
  - Can be set in project settings at `.pi/settings.json`
  - Or globally at `~/.pi/agent/settings.json`
  - Example JSON:
    ```json
    {
      "pkm_path": "~/code/pkm"
    }
    ```
  - `pkm_path` takes precedence over `pkmPath`
  - Project settings override global settings
- The README also gives usage examples for:
  - **Local development**: running the extension directly with `pi -e ./extensions/pi-pkm-mode.ts`
  - **Absolute path usage**: `pi -e /Users/user/code/pi-pkm-mode-extension/extensions/pi-pkm-mode.ts`
  - **Package install**:
    - Unpinned install: `pi install git:github.com/memgrafter/pi-pkm-mode-extension`
    - Pinned install: `pi install git:github.com/memgrafter/pi-pkm-mode-extension@v0.1.0`
    - Project-local install: `pi install -l git:github.com/memgrafter/pi-pkm-mode-extension`

### Assessment
This is a practical **reference/tutorial** for installing and using a pi extension, and it’s fairly durable in terms of the general PKM workflow but medium durability overall because the commands, package names, and install syntax are tied to the current `pi` tool and this specific repository. The content is **mixed**: mostly tutorial/reference, with concrete setup instructions and configuration details. Density is **medium**—it’s short but specific, with commands, file paths, and settings precedence clearly listed. It appears to be **primary source** material from the project README rather than commentary or aggregation. It’s best used as a **refer-back** reference when installing, configuring, or reloading the extension. Scrape quality is **good**: the main README content, commands, and JSON example are present, with no obvious missing sections beyond the repo content not included here.
