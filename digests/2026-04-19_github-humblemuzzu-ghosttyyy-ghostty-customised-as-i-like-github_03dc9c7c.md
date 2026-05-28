---
url: https://github.com/humblemuzzu/ghosttyyy/
title: 'GitHub - humblemuzzu/ghosttyyy: Ghostty customised as i like · GitHub'
scraped_at: '2026-04-19T07:33:25Z'
word_count: 4861
raw_file: raw/2026-04-19_github-humblemuzzu-ghosttyyy-ghostty-customised-as-i-like-github_03dc9c7c.txt
tldr: ghosttyyy is a macOS-focused repo that installs a customized Ghostty terminal with 10 live-switchable dark themes, 11 developer fonts, cursor/opacity tweaks, and a separate `pi-setup/` portable agent environment with custom extensions, skills, prompts, and tools.
key_quote: “Scroll through themes and fonts and watch your terminal change **in real-time**. Press Enter to keep it, Esc to revert.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mitchell Hashimoto
- Mario Zechner
- Sarah Drasner
tools:
- Ghostty
- Homebrew
- fzf
- pi
- llama.cpp
- tmux
- Chrome DevTools Protocol
libraries: []
companies:
- GitHub
- Vercel
- Microsoft
- JetBrains
- Ghostty
tags:
- terminal-customization
- macos
- coding-agents
- configuration
- developer-workflows
---

### TL;DR
`ghosttyyy` is a macOS-focused repo that installs a customized Ghostty terminal with 10 live-switchable dark themes, 11 developer fonts, cursor/opacity tweaks, and a separate `pi-setup/` portable agent environment with custom extensions, skills, prompts, and tools.

### Key Quote
“Scroll through themes and fonts and watch your terminal change **in real-time**. Press Enter to keep it, Esc to revert.”

### Summary
- This is a GitHub repo for a highly customized personal terminal and coding-agent setup, split into:
  - **Part 1: Ghostty Terminal Setup**
  - **Part 2: Pi Coding Agent Setup**
- The README emphasizes aesthetics plus workflow:
  - **10 dark Ghostty themes**
  - **11 developer fonts**
  - **3 cursor styles** × **2 blink modes**
  - **live preview** while browsing options
  - one-command installation via `./install.sh`
- Core Ghostty commands:
  - `gg` = master config hub
  - `gt` = theme switcher with live preview
  - `gf` = font switcher with live preview
  - `gc` = cursor switcher with live preview
- Installation requirements for Ghostty setup:
  - **macOS** (tested on macOS 14+)
  - **Ghostty** installed
  - **Homebrew**
  - `fzf` is installed by the script
- Important macOS caveat:
  - live preview depends on sending `⌘+Shift+,` to Ghostty
  - this needs **Accessibility permissions** for Ghostty and the terminal app used to run the install
- File layout and install destinations are made explicit:
  - `config` → `~/Library/Application Support/com.mitchellh.ghostty/config`
  - `themes/*` → `~/.config/ghostty/themes/`
  - `scripts/*` → `~/.local/bin/`
- The README warns about a common gotcha:
  - Ghostty looks for themes in `~/.config/ghostty/themes/`, **not** in the app support directory
- Theme set:
  - `midnight-code`
  - `catppuccin-macchiato`
  - `dracula-pro`
  - `vesper`
  - `kanagawa`
  - `rosepine`
  - `gruvbox-dark`
  - `nord-frost`
  - `opencode`
  - `synthwave`
- Font set includes:
  - JetBrains Mono, Geist Mono, Fira Code, Cascadia Code, Monaspace variants, Victor Mono, Maple Mono, Commit Mono, Iosevka
- Cursor styles include:
  - bar/block/underline, each with blink or static variants
- Opacity/blur defaults:
  - `background-opacity = 0.92`
  - `background-blur = 20`
- Manual config editing is supported and hot-reloadable with `⌘+Shift+,`
- Custom themes can be added by creating a new file in `~/.config/ghostty/themes/` and setting `theme = my-theme`
- The `pi-setup/` half of the repo is a portable backup of a custom **pi** coding-agent environment:
  - custom TUI
  - extensions
  - multi-agent system
  - skills
  - themes
  - prompts
  - config
- The README’s counts are internally inconsistent in places:
  - it says **11 extensions** in the intro/file tree, but later enumerates more extension files and categories
  - it says **17 skills** in one place, but the file tree shows **16 config skills + 1 pi-level skill**
- Pi setup installation:
  - `cd pi-setup`
  - `chmod +x install.sh`
  - `./install.sh`
  - it backs up existing config, copies files to `~/.pi/agent/` and `~/.config/agents/skills/`, installs npm dependencies, and installs 6 community packages
- Community packages listed:
  - `pi-web-access`
  - `pi-context`
  - `pi-powerline-footer`
  - `pi-anycopy`
  - `pi-token-burden`
  - `lsp-pi`
- Major extension categories described:
  - **editor**: bordered editor UI, bigger prompt area, activity spinner, session/model/context labels
  - **btw.ts**: side conversations via `/btw`
  - **handoff.ts**: replaces compaction with LLM-generated handoffs
  - **session-name.ts**: auto-names sessions
  - **session-breakdown.ts**: usage analytics dashboard
  - **system-prompt.ts**: injects the Amp system prompt every turn
  - **tool-harness.ts**: restricts tools for sub-agents
  - **notify.ts**: desktop notifications
  - **todos.ts**: markdown-backed todo manager
  - **command-palette**: VS Code-like command palette
  - **local-model.ts**: local llama.cpp server manager
  - **md-export.ts**: exports sessions to Markdown
  - **tools/**: replacement tool suite for file ops, search, web, GitHub, sub-agents, session tools, and more
- The prompt/agent system is a major part of the repo:
  - main system prompt: `prompt.amp.system.md`
  - sub-agents: Oracle, Finder, Librarian
  - code review and handoff prompt files are also included
- Skills are treated as loadable workflows or policies:
  - git workflow, review standards, spawning/coordination, tmux, investigation, documentation, writing style, Amp voice, remember, rounds, spar, report, shepherd, nexus-fix, chrome-cdp, handoff
- Settings shown in `settings.json`:
  - `theme: "gruvbox"`
  - `defaultProvider: "anthropic"`
  - `defaultModel: "claude-opus-4-6"`
  - `defaultThinkingLevel: "high"`
  - compaction disabled
  - quiet startup enabled
  - double escape shows tree
  - steering/follow-up mode set to `all`
- Safety rails in `permissions.json`:
  - blocks `git add -A` / `git add .`
  - blocks `git push --force`
  - blocks `rm`
  - otherwise allows tool calls
- Troubleshooting and uninstall sections provide practical recovery steps:
  - fix theme path issues
  - grant Accessibility permissions
  - handle bash compatibility notes
  - restore backups created by installers
  - remove Ghostty files, aliases, and pi backups if needed
- License is **MIT**

### Assessment
**Durability:** medium. The Ghostty customization ideas are fairly reusable, but many concrete details are tied to current app behavior, macOS permissions, Ghostty config paths, and the repo’s specific toolchain. **Content type:** mixed, with tutorial-heavy installation docs, reference sections, and a project showcase. **Density:** high; the README is packed with exact commands, file paths, feature lists, and configuration examples. **Originality:** primarily a first-party project README and reference implementation, not a synthesis. **Reference style:** refer-back, especially if you want the exact install commands, paths, aliases, or repo structure; it’s also useful for skim-once if you only want the gist. **Scrape quality:** good overall, but the source itself is internally inconsistent about extension and skill counts, so the summary should be read as reflecting those inconsistencies rather than resolving them.
