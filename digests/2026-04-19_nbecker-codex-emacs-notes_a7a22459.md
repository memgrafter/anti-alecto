---
url: https://github.com/nbecker/codex-emacs-notes?tab=readme-ov-file#using-terminal-coding-agents-from-emacs
title: nbecker/codex-emacs-notes
scraped_at: '2026-04-19T08:25:04Z'
word_count: 490
raw_file: raw/2026-04-19_nbecker-codex-emacs-notes_a7a22459.txt
tldr: This README describes a practical Emacs + `vterm` workflow for running terminal coding agents like Codex and Claude inside per-project `bubblewrap` sandboxes, with optional GPU passthrough and shared auth state.
key_quote: Authentication is shared, but operational state is isolated per repo.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- emacs
- vterm
- bubblewrap
- codex
- claude
libraries: []
companies: []
tags:
- emacs
- terminal-agents
- sandboxing
- bubblewrap
- developer-workflow
---

### TL;DR
This README describes a practical Emacs + `vterm` workflow for running terminal coding agents like Codex and Claude inside per-project `bubblewrap` sandboxes, with optional GPU passthrough and shared auth state.

### Key Quote
"Authentication is shared, but operational state is isolated per repo."

### Summary
- **What this repo is:** a small record of the setup the author found workable for using terminal coding agents from Emacs, primarily via `vterm`.
- **Scope:** explicitly not a full guide or product tutorial; it documents a personal workflow that has been tested with **Claude** and **Codex**, with Codex used more often in practice.
- **Why Emacs + `vterm`:**
  - lets the author stay in Emacs while using terminal-first agent CLIs
  - preserves normal Emacs editing, search, and window management
  - provides a real terminal rather than a shell emulation inside a standard buffer
  - makes it easy to move between source buffers and the agent session
- **Why sandboxing is used:** terminal coding agents need repo access to inspect and modify code, but the author does not want them running in the full login environment by default.
- **Sandbox requirements the author wanted:**
  - current project mounted read-write
  - private, project-local home directory
  - access to host-installed CLI tools
  - shared login/auth state across projects
  - project-local caches, history, and other agent state
- **`bub.sh`:**
  - launches a shell inside `bubblewrap`
  - binds `/workspace` to the current repo
  - binds `/home/sandbox` to a project-local `.bwrap-home`
  - mounts most of the host OS read-only
  - drops capabilities
  - shares Codex and Claude auth files from the real home directory
  - keeps other agent state local to the repo
  - typical use:
    ```bash
    cd my-repo
    bub.sh
    ```
  - after that, start the agent CLI inside the sandboxed shell
- **`bub-gpu.sh`:**
  - same basic setup as `bub.sh`
  - additionally binds NVIDIA device nodes into the sandbox
  - intended only for projects/tools that need GPU visibility
  - the plain wrapper is preferred when GPU access is unnecessary
- **Benefits the author highlights:**
  - stay inside Emacs
  - run the agent in a real terminal
  - keep writable state separate per repository
  - avoid recreating login/auth state for each project
- **Caveats and limitations:**
  - this is a convenience sandbox, not a formal security boundary
  - terminal focus and paste handling still matter
  - behavior may differ between Wayland and X11
  - GPU passthrough requires the separate wrapper
- **Files in the repo:** only two scripts are called out: `bub.sh` and `bub-gpu.sh`.

### Assessment
This is a **mixed** reference/tutorial note with a practical, firsthand workflow rather than a broad or authoritative guide. Durability is **medium**: the Emacs/vterm/bubblewrap pattern is broadly reusable, but the specifics depend on current agent CLIs, auth file locations, and Linux display/GPU behavior. Density is **medium**: it’s concise but contains concrete setup details, file names, mount behavior, and usage assumptions. Originality is **primary source** in the sense that it documents the author’s own setup and preferences, not an aggregation of docs. It is best used **refer-back** as a setup reminder or quick confirmation that this is the Emacs terminal-agent sandbox note. Scrape quality is **good**: the main README content and the referenced file names are present, though the actual script contents and any non-README repo details are not included.
