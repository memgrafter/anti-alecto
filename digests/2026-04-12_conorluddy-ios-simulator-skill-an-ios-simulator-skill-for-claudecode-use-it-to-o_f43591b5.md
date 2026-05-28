---
url: https://github.com/conorluddy/ios-simulator-skill
title: 'conorluddy/ios-simulator-skill: An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude''s ability to build, run and interact with your apps, without using up any of the available token/context budget.'
scraped_at: '2026-04-12T09:38:33Z'
word_count: 1468
raw_file: raw/2026-04-12_conorluddy-ios-simulator-skill-an-ios-simulator-skill-for-claudecode-use-it-to-o_f43591b5.txt
tldr: A Claude Code Skill for iOS Simulator automation that uses semantic, accessibility-based scripts to build, launch, inspect, and interact with iOS apps with minimal token/context usage.
key_quote: “Skills don't load in any context.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- conorluddy
tools:
- Claude Code
- Xcode
- idb
- simctl
- jq
libraries:
- Pillow
companies:
- Facebook
tags:
- ios-automation
- accessibility
- claude-code
- simulator-testing
- developer-tools
---

### TL;DR
A Claude Code Skill for iOS Simulator automation that uses semantic, accessibility-based scripts to build, launch, inspect, and interact with iOS apps with minimal token/context usage.

### Key Quote
“Skills don't load in any context.”

### Summary
- This repository is presented as a **production-ready iOS Simulator automation skill for Claude Code**, with **21 scripts** aimed at both human developers and AI agents.
- It is described as a **Skill version of the author’s Xcode MCP** (`xc-mcp`), with the main value proposition being **avoiding the token/context overhead of active MCPs**.
- Important warning from the author: you should **copy the `ios-simulator-skill` directory into your Claude skills directory**, not install the entire repo as-is.

- **Core approach**
  - Avoids fragile coordinate-based tapping like `idb ui tap 320 400`.
  - Instead uses **semantic navigation via accessibility APIs**, e.g.:
    - `python scripts/navigator.py --find-text "Login" --tap`
  - Claims this makes it more robust across UI changes and screen sizes.

- **Highlighted features**
  - **21 production scripts** for building, testing, and automation
  - **Semantic navigation** by text, type, or ID
  - **Token optimized** with a claimed **96% reduction** vs raw tools
  - **Zero configuration** on macOS with Xcode
  - **Structured output** in JSON or formatted text
  - **Auto-UDID detection**
  - **Batch simulator operations**
  - **Accessibility/testing tooling** including WCAG checks, visual diffs, and audits
  - **CI/CD readiness** via JSON output and exit codes

- **Installation**
  - As a **Claude Code Skill**:
    - `git clone https://github.com/conorluddy/ios-simulator-skill.git ~/.claude/skills/ios-simulator-skill`
    - or project-local: `.claude/skills/ios-simulator-skill`
  - From release zip:
    - download from GitHub releases and unzip into the skills directory
  - Claude Code is expected to load the skill automatically after restart.

- **Prerequisites**
  - macOS 12+
  - Xcode Command Line Tools
  - Python 3
  - Optional: **IDB** (`brew tap facebook/fb && brew install idb-companion`) for interactive features
  - Optional: **Pillow** for `visual_diff.py`

- **Quick start workflow**
  - Run `sim_health_check.sh`
  - Launch app with `app_launcher.py --launch <bundle-id>`
  - Inspect the current UI with `screen_mapper.py`
  - Tap UI elements by semantic label using `navigator.py`
  - Enter text with `navigator.py --find-type TextField --enter-text ...`
  - Run `accessibility_audit.py`

- **Script categories**
  - **Build & Development**: `build_and_test.py`, `log_monitor.py`
  - **Navigation & Interaction**: `screen_mapper.py`, `navigator.py`, `gesture.py`, `keyboard.py`, `app_launcher.py`
  - **Testing & Analysis**: `accessibility_audit.py`, `visual_diff.py`, `test_recorder.py`, `app_state_capture.py`, `sim_health_check.sh`
  - **Advanced Testing & Permissions**: `clipboard.py`, `status_bar.py`, `push_notification.py`, `privacy_manager.py`
  - **Device Lifecycle**: `simctl_boot.py`, `simctl_shutdown.py`, `simctl_create.py`, `simctl_delete.py`, `simctl_erase.py`

- **Usage examples**
  - Login flow: launch app, map screen, fill fields, tap Login, check accessibility
  - Test documentation: record screenshots, accessibility trees, and markdown timing reports
  - Visual testing: capture baseline, compare screenshots
  - Permission testing: grant/revoke camera and location permissions
  - CI/CD lifecycle: create simulator, run build/tests, delete simulator afterward

- **Design principles emphasized**
  - **Semantic Navigation** over pixel coordinates
  - **Token Efficiency** with very short default outputs
  - **Accessibility-first** reliability
  - **Zero Configuration**
  - **Structured data**
  - **Auto-learning** of device preference

- **Documentation included**
  - `SKILL.md` for full reference
  - `CLAUDE.md` for architecture/dev guidance
  - `references/` for deep docs
  - `examples/` for workflows

- **Evaluation claims**
  - Tested with Claude Code evals
  - Iteration 1 results:
    - **With skill: 100% (3/3)**
    - **Without skill: 46% (~1.4/3)**
  - Evaluations focus on:
    1. Environment & discovery
    2. Build & navigate
    3. Test & capture

- **Troubleshooting**
  - Run the health check script for environment issues
  - Use `--help` on any script
  - Use `--verbose` if elements are not found

- **Contributing**
  - The author welcomes contributions but says review will be slow
  - Best path may be to **fork and customize**
  - Contributions should preserve token efficiency, accessibility focus, `--help`, `--json`, type hints, Black/Ruff compliance, and SKILL.md updates

### Assessment
Durability is **medium** because the underlying ideas—accessibility-based UI automation, semantic navigation, and token-efficient tool use—are fairly durable, but the implementation is tied to macOS, Xcode, Claude Code Skills, and current simulator tooling, so some details may age quickly. Content type is **mixed**, leaning tutorial/reference: it explains what the skill does, how to install it, how to use the scripts, and what the repository structure contains. Density is **high**, with many concrete commands, script names, feature claims, and workflow examples packed into a fairly short README. Originality is best classified as **primary source** for the project itself, though it also serves as promotional/architectural documentation rather than neutral technical analysis. Reference style is **refer-back**: useful to revisit when installing, choosing scripts, or checking supported capabilities, not something to memorize once. Scrape quality is **good** overall: the main README content appears intact, including code blocks, feature lists, and evaluation tables, though the summary is limited to the README and does not include the contents of linked files like SKILL.md, CLAUDE.md, or the references/examples directories.
