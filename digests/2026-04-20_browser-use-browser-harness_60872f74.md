---
url: https://github.com/browser-use/browser-harness
title: browser-use/browser-harness
scraped_at: '2026-04-20T04:15:34Z'
word_count: 490
raw_file: raw/2026-04-20_browser-use-browser-harness_60872f74.txt
tldr: browser-use/browser-harness presents a minimal Chrome CDP-based browser automation harness that lets an LLM edit its own helper code mid-task, with setup, usage, remote-browser options, and an agent-generated skills workflow.
key_quote: One websocket to Chrome, nothing between.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
- Codex
- Chrome CDP
- browser-use
libraries: []
companies:
- browser-use
- GitHub
- Amazon
- LinkedIn
tags:
- browser-automation
- llm-agents
- cdp
- self-healing-systems
- developer-tools
---

### TL;DR
`browser-use/browser-harness` presents a minimal Chrome CDP-based browser automation harness that lets an LLM edit its own helper code mid-task, with setup, usage, remote-browser options, and an agent-generated skills workflow.

### Key Quote
"One websocket to Chrome, nothing between."

### Summary
- **What it is**
  - A GitHub repo for **Browser Harness**, described as the “simplest, thinnest, self-healing harness” for browser tasks.
  - It is built **directly on CDP** and aims to give an LLM “complete freedom” to perform browser automation.
  - The core idea is that the **agent can write missing functionality mid-task** instead of relying on a fixed framework.

- **Core concept / workflow**
  - Example flow shown in the README:
    - the agent wants to upload a file
    - `helpers.py → upload_file()` is missing
    - the agent edits the harness and adds the function
    - the file upload then succeeds
  - This is meant to illustrate the “self-healing” approach: gaps in tooling are filled during execution.

- **Setup instructions**
  - The repo provides a **setup prompt** intended to be pasted into **Claude Code or Codex**.
  - That prompt instructs the agent to:
    - read `install.md` first
    - connect the repo to the user’s real browser
    - then read `SKILL.md` for normal usage
    - always read `helpers.py`, since that’s where functions live
    - activate any setup/verification tab so the user can see the active browser tab
    - after installation, open the repository in the browser
    - if the user is logged into GitHub, ask whether to star the repo as a demo; only click if the user says yes
    - otherwise go to `browser-use.com`
  - The page also mentions a checkbox the user should tick so the agent can connect to the browser.

- **Remote browser support**
  - It offers **free remote browsers** for sub-agents or deployment.
  - Claimed free tier: **3 concurrent browsers, no card required**.
  - Two ways to get started:
    - grab an API key from `cloud.browser-use.com/new-api-key`
    - or let the agent sign up itself via `docs.browser-use.com/llms.txt`

- **Repository structure / components**
  - The README summarizes the codebase as roughly **592 lines of Python**:
    - `install.md` — first-time install and browser bootstrap
    - `SKILL.md` — day-to-day usage
    - `run.py` (~36 lines) — runs plain Python with helpers preloaded
    - `helpers.py` (~195 lines) — starting tool calls; the agent edits these
    - `admin.py` + `daemon.py` (~361 lines) — daemon bootstrap, CDP websocket, and socket bridge

- **Contributing / skills model**
  - The repo encourages contributors to add new **domain skills** under `domain-skills/` for recurring tasks and websites.
  - Example domains mentioned: **LinkedIn outreach, Amazon ordering, expenses filing**.
  - Important policy:
    - **Skills are written by the harness, not by you**
    - users should run tasks with the agent, and the harness will generate skills automatically when it learns non-obvious steps
    - contributors should open PRs with the generated `domain-skills/<site>/` folder
  - It also invites bug fixes, docs tweaks, and helper improvements.

- **Links / related reading**
  - The README links to:
    - a post on the **“bitter lesson”** for agent frameworks
    - a post about **web agents that actually learn**
  - It also points to existing skill folders such as `github/`, `linkedin/`, and `amazon/`.

### Assessment
This is a **mixed** content page combining product positioning, setup documentation, and contribution guidance. Durability is **medium**: the high-level “self-healing harness” idea may age well, but the setup instructions, file layout, and browser integration details are tied to the current repo state and tooling. The density is **medium**—there are concrete setup steps and architecture notes, but much of the page is promotional and conceptual. It appears to be **primary source** documentation from the project authors, so it’s the right place to verify how the tool is intended to work. As a reference, it’s best used **refer-back** for installation, repo structure, and the skill-generation model. Scrape quality is **good**: the README content and links are captured, though the image assets themselves are not viewable here.
