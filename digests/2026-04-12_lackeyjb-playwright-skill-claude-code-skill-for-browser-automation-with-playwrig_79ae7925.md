---
url: https://github.com/lackeyjb/playwright-skill
title: 'lackeyjb/playwright-skill: Claude Code Skill for browser automation with Playwright. Model-invoked - Claude autonomously writes and executes custom automation for testing and validation.'
scraped_at: '2026-04-12T09:38:49Z'
word_count: 1067
raw_file: raw/2026-04-12_lackeyjb-playwright-skill-claude-code-skill-for-browser-automation-with-playwrig_79ae7925.txt
tldr: A Claude Code plugin/skill that lets Claude autonomously generate and run custom Playwright browser automation, with visible browser execution by default and installable either as a plugin or as a standalone skill.
key_quote: Claude autonomously decides when to use this skill based on your browser automation needs, loading only the minimal information required for your specific task.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- playwright
- claude code
libraries: []
companies:
- Claude
- GitHub
tags:
- browser-automation
- playwright
- claude-code
- testing
- developer-tools
---

### TL;DR
A Claude Code plugin/skill that lets Claude autonomously generate and run custom Playwright browser automation, with visible browser execution by default and installable either as a plugin or as a standalone skill.

### Key Quote
“Claude autonomously decides when to use this skill based on your browser automation needs, loading only the minimal information required for your specific task.”

### Summary
- **What it is**
  - A **Claude Skill** for **general-purpose browser automation** using **Playwright**.
  - Also packaged as a **Claude Code Plugin** for easier installation, updates, and team distribution.
  - The repo says it is “Made using Claude Code.”

- **Core idea**
  - Claude does **not** rely on prebuilt scripts; it **writes custom Playwright code on the fly** for each task.
  - Intended for anything from:
    - simple page testing
    - multi-step workflows
    - visual testing
    - validation tasks
    - interaction testing

- **Feature highlights**
  - **Any Automation Task**: custom code per request.
  - **Visible Browser by Default**: `headless: false` unless overridden.
  - **Zero Module Resolution Errors**: uses a “universal executor” to avoid module issues.
  - **Progressive Disclosure**: short `SKILL.md`, with `API_REFERENCE.md` loaded only when needed.
  - **Safe Cleanup**: temp file handling is designed to avoid race conditions.
  - **Comprehensive Helpers**: optional utility functions for common actions.

- **Installation paths**
  - **Recommended: Plugin installation**
    - Add marketplace:
      - `/plugin marketplace add lackeyjb/playwright-skill`
    - Install plugin:
      - `/plugin install playwright-skill@playwright-skill`
    - Then run:
      - `cd ~/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill`
      - `npm run setup`
  - **Standalone skill installation**
    - Clone repo to a temp directory, copy only `skills/playwright-skill` into:
      - `~/.claude/skills/` for global use, or
      - `.claude/skills/` inside a project
    - Run:
      - `npm run setup`
    - Delete the temp clone afterward.
  - **Release download**
    - Download from GitHub Releases, extract, copy the inner `skills/playwright-skill/` folder, then run `npm run setup`.

- **How it works**
  1. User describes a browser task.
  2. Claude writes custom Playwright code.
  3. `run.js` executes it with proper module resolution.
  4. Browser opens visibly by default and runs the automation.
  5. Results come back with **console output** and **screenshots**.

- **Default configuration**
  - **Headless:** `false`
  - **Slow Motion:** `100ms`
  - **Timeout:** `30s`
  - **Screenshots:** saved to `/tmp/`

- **Project structure**
  - Plugin metadata in `.claude-plugin/`
  - Actual skill under `skills/playwright-skill/`
  - Key files include:
    - `SKILL.md`
    - `run.js`
    - `package.json`
    - `lib/helpers.js`
    - `API_REFERENCE.md`
  - Also includes `README.md`, `CONTRIBUTING.md`, and `LICENSE`

- **Advanced documentation**
  - `API_REFERENCE.md` is meant to be loaded for deeper Playwright topics such as:
    - selectors
    - network interception
    - authentication
    - visual regression testing
    - mobile emulation
    - performance testing
    - debugging

- **Dependencies**
  - Node.js
  - Playwright
  - Chromium
  - All are installed via `npm run setup`

- **Troubleshooting notes**
  - If Playwright is missing, run `npm run setup`
  - If module errors happen, automation should go through `run.js`
  - If the browser doesn’t open, ensure `headless: false`
  - To install all browsers, run `npm run install-all-browsers`

- **Compatibility / positioning**
  - The project says it implements the **open Agent Skills specification** and is compatible across agent platforms.
  - It links to the Agent Skills spec and Claude documentation for skills, plugins, and marketplaces.

### Assessment
This is a **tutorial/reference/mixed** repository README with fairly high practical value and moderate-to-high durability, though some installation details are tied to current Claude Code/plugin workflows and may change over time. The content is **dense** and mostly **reference-style**, focused on setup, usage, and structure rather than deep theory. It is primarily **primary source** documentation for the project itself, not a synthesis of others’ work. Best used as a **refer-back** resource when installing or operating the skill, especially for the exact commands, defaults, and folder layout. Scrape quality looks **good** overall: the README content is intact, including commands, structure, and troubleshooting, though no code from `run.js`, `SKILL.md`, or `API_REFERENCE.md` is included beyond descriptions.
