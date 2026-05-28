---
url: https://github.com/OlaProeis/Ferrite
title: 'OlaProeis/Ferrite: A fast, lightweight text editor for Markdown, JSON, YAML, and TOML files. Built with Rust and egui for a native, responsive experience.'
scraped_at: '2026-04-12T07:28:13Z'
word_count: 3531
raw_file: raw/2026-04-12_olaproeis-ferrite-a-fast-lightweight-text-editor-for-markdown-json-yaml-and-toml_cce03fd7.txt
tldr: Ferrite is a Rust + egui desktop editor for Markdown and structured text files, with rich Markdown preview/editing, workspace and terminal features, broad packaging support, and explicit notes about platform limitations and AI-assisted development.
key_quote: Ferrite is a fast, lightweight text editor for Markdown, JSON, YAML, and TOML files.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Claude
- Anthropic
- Cursor
- Task Master
- SignPath Foundation
- liuxiaopai-ai
- blizzard007dev
- wolverin0
- abcd-ca
- SteelCrab
tools:
- egui
- eframe
- Cargo
- Cursor
- Task Master
- Weblate
- GitHub Releases
libraries:
- ropey
- comrak
- syntect
- two-face
- git2
- portable-pty
- vte
- encoding_rs
- chardetng
- clap
- rfd
- arboard
- notify
- csv
- font-kit
companies:
- GitHub
- Anthropic
- Weblate
- SignPath Foundation
- SignPath.io
tags:
- text-editors
- markdown
- rust
- desktop-apps
- developer-tools
---

### TL;DR
Ferrite is a Rust + egui desktop editor for Markdown and structured text files, with rich Markdown preview/editing, workspace and terminal features, broad packaging support, and explicit notes about platform limitations and AI-assisted development.

### Key Quote
"Ferrite is a fast, lightweight text editor for Markdown, JSON, YAML, and TOML files."

### Summary
- **What it is**
  - Ferrite is a cross-platform text editor focused on **Markdown, JSON, CSV, YAML, and TOML**.
  - Built with **Rust 1.70+** and **egui/eframe 0.28** for a native GUI.
  - Official site: **getferrite.dev**; source and releases are on GitHub.

- **Platform status and caveats**
  - Actively developed and tested on **Windows** and **Linux**.
  - **macOS support is experimental**.
  - Windows releases are **digitally signed starting with v0.2.6.1** to reduce SmartScreen warnings and antivirus false positives.
  - Ferrite claims it does **not** access passwords, browser data, or make unsolicited network connections; the only network use described is manual update checking.

- **Notable release highlights**
  - The README flags **v0.2.7** as latest in the screenshots section, with:
    - **Wikilinks** and **backlinks panel**
    - **Vim mode**
    - **Welcome page**
    - **GitHub-style callouts**
    - **Ctrl+Scroll zoom**
    - Better selection retention after formatting
    - **Frontmatter editor**
    - Image rendering in preview
    - Format toolbar and side panel toggles
    - **Nix/NixOS flake support**
    - New packaging: **.deb**, **.rpm**, and macOS **.app**
    - **Single-instance** file opening
  - Also mentions **v0.2.6** improvements like a custom editor engine with **virtual scrolling**, multi-cursor editing, code folding, and IME/CJK input improvements.

- **Core editor features**
  - **Markdown editing**
    - WYSIWYG-style editing with live preview
    - Split view and raw text modes
    - Click-to-edit formatting
  - **Structured file support**
    - Native handling for JSON/YAML/TOML tree views
    - CSV/TSV table viewer
    - Inline editing and path copying
  - **Editing productivity**
    - Find/replace with regex
    - Go to line
    - Undo/redo per tab
    - Multi-cursor editing
    - Duplicate line, move line up/down
    - Smart paste for links
    - Auto-close brackets/quotes
    - Snippets like `;date` and `;time`
    - Auto-save
    - Optional line numbers, line width limits, custom fonts, shortcut rebinding

- **Markdown and document tooling**
  - Supports **raw**, **rendered**, and **split** view modes.
  - Includes:
    - **Table of contents generation/update**
    - **Document outline and statistics**
    - Export to HTML or copy as HTML
    - Formatting toolbar
    - Frontmatter editing
  - Mermaid diagrams are rendered natively for **11 diagram types**:
    - Flowchart, sequence, pie, state, mindmap, class, ER, git graph, gantt, timeline, user journey
  - README notes Mermaid support is good but may differ from mermaid.js on complex diagrams.

- **Workspace and file management**
  - Can open folders as a **workspace**
  - Includes:
    - File tree
    - Quick switcher (`Ctrl+P`)
    - Search in files (`Ctrl+Shift+F`)
    - Session persistence
    - Git status indicators with auto-refresh

- **Terminal workspace**
  - Built-in terminal with multiple instances and shell choices:
    - PowerShell, CMD, WSL, bash
  - Supports:
    - Horizontal and vertical splits
    - Pane maximize
    - Layout persistence
    - Theming and transparency
    - Drag-and-drop tab reordering
  - README explicitly markets it as **AI-ready** with a “breathing” indicator when waiting for input.

- **Installation and packaging**
  - Prebuilt packages are available from GitHub Releases for:
    - **Windows**: MSI installer and portable ZIP
    - **Linux**: `.deb`, `.rpm`, `.tar.gz`
    - **macOS**: `.dmg` and `.tar.gz`
  - Also available on:
    - **AUR**
    - **Nix/NixOS flake**
    - Homebrew tap for macOS
  - The README gives platform-specific install commands and notes:
    - Windows portable mode stores data next to the executable
    - Linux packages register file associations
    - macOS Gatekeeper may show warnings because Ferrite is not notarized

- **Build from source**
  - Requires **Rust 1.70+**
  - Lists platform dependencies for Windows, Linux, and macOS
  - Standard build command:
    - `cargo build --release`
  - Optional macOS bundling:
    - `cargo install cargo-bundle`
    - `cargo bundle --release`

- **Usage and shortcuts**
  - CLI examples:
    - `ferrite path/to/file.md`
    - `ferrite path/to/folder/`
  - Key shortcuts include:
    - `Ctrl+N`, `Ctrl+O`, `Ctrl+S`
    - `Ctrl+P` quick switcher
    - `Ctrl+F` find
    - `Ctrl+G` go to line
    - `Ctrl+,` settings
  - More detailed shortcuts cover tab navigation, folding, formatting, and terminal pane control.

- **Configuration**
  - Settings cover appearance, editor behavior, and file handling.
  - Config locations:
    - Windows: `%APPDATA%\ferrite\`
    - Linux: `~/.config/ferrite/`
    - macOS: `~/Library/Application Support/ferrite/`
    - Windows portable: `portable/`
  - Workspace-specific settings live in `.ferrite/`.

- **Tech stack**
  - Core dependencies include:
    - **ropey** for text buffer
    - **comrak** for Markdown parsing
    - **syntect** and **two-face** for syntax highlighting
    - **git2** for git integration
    - **portable-pty** and **vte** for terminal emulation
    - **encoding_rs** and **chardetng** for encoding detection
    - **clap**, **rfd**, **arboard**, **notify**, **csv**, **font-kit**, and others

- **AI-assisted development**
  - The project claims the codebase is **100% AI-generated**.
  - Claude (Anthropic), via Cursor and MCP tools, wrote the Rust code, docs, and config.
  - The maintainer describes their role as product direction, testing, review, and orchestration.
  - The README says the workflow, prompts, and handover docs are public for transparency.

- **Community and contribution**
  - Translations are managed via **Weblate**.
  - Contribution instructions are provided with standard Rust tooling:
    - `cargo fmt`
    - `cargo clippy`
    - `cargo test`
    - `cargo build`
  - Acknowledgments mention contributors for Nix support, welcome page, terminal workspace, line editing features, and CJK rendering.

### Assessment
Ferrite’s README is a high-density project reference with a lot of installation, feature, and platform-specific detail, so it has **medium durability** overall: the general editor concept is stable, but version-specific highlights, packaging formats, and platform caveats will age as releases change. The content is a **mixed** blend of reference, tutorial, and announcement material, and it is fairly **high density** because it enumerates commands, shortcuts, dependencies, and release-specific claims. It is primarily a **primary source** for the project’s own capabilities and policies, making it useful as a trustworthy starting point, though some claims—especially performance and antivirus behavior—are self-reported. This is best used as a **refer-back** reference rather than deep study, since it helps confirm features, install steps, and platform support quickly. Scrape quality is **good**: the README content appears largely complete, including details, commands, tables, and expandable sections, though images/screenshots themselves are not captured beyond their references.
