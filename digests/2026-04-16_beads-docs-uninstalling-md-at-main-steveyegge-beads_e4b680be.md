---
url: https://github.com/steveyegge/beads/blob/main/docs/UNINSTALLING.md
title: beads/docs/UNINSTALLING.md at main · steveyegge/beads
scraped_at: '2026-04-16T03:53:53Z'
word_count: 618
raw_file: raw/2026-04-16_beads-docs-uninstalling-md-at-main-steveyegge-beads_e4b680be.txt
tldr: A step-by-step guide for fully uninstalling Beads from a Git repository, including hooks, Git config, `.gitattributes`, `.beads/`, sync worktrees, and optionally the `bd` binary.
key_quote: '"Warning:** This permanently deletes all issue data."'
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- bd
libraries: []
companies: []
tags:
- git
- uninstallation
- command-line
- version-control
- data-removal
---

### TL;DR
A step-by-step guide for fully uninstalling Beads from a Git repository, including hooks, Git config, `.gitattributes`, `.beads/`, sync worktrees, and optionally the `bd` binary.

### Key Quote
"Warning:** This permanently deletes all issue data."

### Summary
- This document explains how to completely remove Beads from a repository and clean up related tooling.
- **Quick uninstall sequence from repo root:**
  - Stop any running Dolt server: `bd dolt stop 2>/dev/null || true`
  - Delete Beads-installed Git hooks:
    - `.git/hooks/pre-commit`
    - `.git/hooks/prepare-commit-msg`
    - `.git/hooks/post-merge`
    - `.git/hooks/pre-push`
    - `.git/hooks/post-checkout`
  - Unset Beads-related Git config:
    - `beads.role`
    - `merge.beads.driver`
    - `merge.beads.name`
  - Remove `.gitattributes` if it only contains Beads config, or edit out the Beads line.
  - Delete the `.beads` directory: `rm -rf .beads`
  - Delete sync worktrees if present: `rm -rf .git/beads-worktrees`
- **Detailed cleanup notes:**
  - The guide identifies what each installed hook does:
    - `pre-commit` runs Beads pre-commit checks
    - `prepare-commit-msg` adds Beads metadata to commit messages
    - `post-merge` imports changes after merges
    - `pre-push` syncs before pushing
    - `post-checkout` imports after branch switches
  - If you had pre-existing hooks, it suggests checking for `.backup` files and restoring them if needed.
- **What `.beads/` may contain:**
  - `dolt/` database directory
  - `dolt/sql-server.pid` and `dolt/sql-server.log` for server mode
  - `issues.jsonl` legacy issue data
  - `config.yaml`, `metadata.json`
  - `deletions.jsonl`
  - `README.md`
- **Data-loss warning:**
  - Removing `.beads/` permanently deletes issue data.
  - The doc suggests backing up first with:
    - `bd export -o ~/beads-backup-$(date +%Y%m%d).jsonl`
- **Optional follow-up:**
  - If `.beads/` was tracked, commit and push its removal with:
    - `git add -A`
    - `git commit -m "Remove beads issue tracking"`
    - `git push`
- **Uninstalling the `bd` binary:**
  - If installed via `go install`, remove it with `rm $(which bd)` or `rm ~/go/bin/bd`
  - If installed manually, delete it from wherever it was placed, e.g. `/usr/local/bin/bd`
- **Verification checklist:**
  - `which bd` should no longer find Beads
  - `.beads/` should not exist
  - `.git/hooks/` should not contain Beads hooks
  - `git config --get merge.beads.driver` should return nothing
  - `.gitattributes` should be absent or contain no Beads line
- **Reinstalling later:**
  - Run `bd init` to recreate `.beads/`, reinstall hooks, and restore the merge driver

### Assessment
This is a **reference** document with a **high** durability for the general uninstallation workflow, though some commands are tied to the current Beads/Dolt setup and could change if the project evolves. The content is mostly **fact/reference** with a little tutorial structure, and it is **dense** with concrete commands, file paths, and cleanup steps. It reads like a **primary source** documentation page rather than commentary or synthesis. Best used as a **refer-back** guide when actually uninstalling Beads, since the exact sequence and verification commands are the main value. Scrape quality looks **good**: the structure, code blocks, tables, warnings, and reinstall notes are all present.
