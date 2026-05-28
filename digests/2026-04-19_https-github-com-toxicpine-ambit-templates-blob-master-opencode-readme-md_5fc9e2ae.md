---
url: https://github.com/ToxicPine/ambit-templates/blob/master/opencode/README.md
title: https://github.com/ToxicPine/ambit-templates/blob/master/opencode/README.md
scraped_at: '2026-04-19T20:09:40Z'
word_count: 513
raw_file: raw/2026-04-19_https-github-com-toxicpine-ambit-templates-blob-master-opencode-readme-md_5fc9e2ae.txt
tldr: This README describes a template for running OpenCode as a persistent cloud workspace on Ambit/Fly.io, so your coding session survives device changes, idle suspend/resume, and stays accessible privately over Tailscale.
key_quote: Your session survives reboots, you can access it from any of your devices using the browser (connection via Tailscale), and it stays invisible to the public internet.
durability: medium
content_type: tutorial
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- ToxicPine
- cardelli
tools:
- OpenCode
- Ambit
- Fly.io
- Tailscale
- Chromatic
- Playwright
libraries:
- Nix
- tmux
- vim
- curl
- bun
- deno
- node
- git
companies: []
tags:
- cloud-development
- remote-workspaces
- devops
- browser-access
- private-network
---

### TL;DR
This README describes a template for running OpenCode as a persistent cloud workspace on Ambit/Fly.io, so your coding session survives device changes, idle suspend/resume, and stays accessible privately over Tailscale.

### Key Quote
“Your session survives reboots, you can access it from any of your devices using the browser (connection via Tailscale), and it stays invisible to the public internet.”

### Summary
- **What it is**
  - A template called **“OpenCode on Ambit”** for deploying a persistent **OpenCode** workspace in the cloud.
  - It is intended to behave like a development environment that follows you across devices, with the same session state available on laptop and phone.

- **Core value proposition**
  - OpenCode is normally tied to the machine it runs on; this template removes that limitation by hosting it on **Ambit** as a persistent web workspace.
  - The workspace:
    - survives reboots
    - is accessible from any device on the same **Tailscale** network
    - is not exposed to the public internet
    - preserves terminals, agent conversations, and work state across device handoff

- **What you get**
  - **OpenCode Web UI** at `http://<name>.<network>`
  - **Automatic suspend/resume**
    - machine suspends when idle
    - wakes on the next HTTP request
    - billed as “only pay for what you use”
  - **Pre-configured environment**
    - includes `git`, `node`, `bun`, `deno`, `gh`, `tmux`, `vim`, `curl`, and more
    - configured declaratively
  - **Self-Orchestation Plugin**
    - pre-installed
    - described as “OpenClaw-style self-orchestration”
  - **Customizability**
    - edit `home.nix` to add packages, shell config, or programs
    - run `rebuild` afterward

- **Setup / deployment**
  - Deploy to **Ambit**, which wraps **Fly.io**
  - Example commands:
    - `npx skills add ToxicPine/ambit-skills --skill ambit-cli`
    - `npx @cardelli/ambit create lab`
    - `npx @cardelli/ambit deploy my-ide.lab --template ToxicPine/ambit-templates/opencode`
  - Then access it in a browser at `http://my-ide.lab` on the Tailscale network

- **Bonus: cloud browser on the same private network**
  - Mentions deploying **Chromatic** on the same Ambit network for:
    - Playwright
    - computer-use agents
  - This is positioned as a safer alternative to using ngrok or Cloudflare tunnels for cloud browsers against local dev servers
  - Example:
    - `npx @cardelli/ambit deploy my-browser.lab --template ToxicPine/ambit-templates/chromatic`
  - Claims a cloud browser can access `http://localhost:3000` in the Ambit OpenCode environment, or even a local dev device, without extra tunnel setup

- **Default specs**
  - **CPU:** 2x shared
  - **Memory:** 2 GB
  - **Disk:** 16 GB persistent volume
  - **Auto stop:** suspend when idle
  - **Auto start:** wake on HTTP request

- **Repo/file structure**
  - `system.nix` — entrypoint, daemons, system packages
  - `home.nix` — user packages and shell config; the main customization point
  - `users.nix` — user accounts
  - `fly.toml` — Fly.io deployment config
  - `flake.nix` — Nix flake wiring
  - `lib/` — plumbing scripts and build/setup logic
  - Points readers to `TECHNICAL.md` for details on the image builder, daemon system, reload behavior, and flake layout

### Assessment
This is a **reference/tutorial** with a strong deployment-oriented focus and moderate marketing language. Durability is **medium**: the core idea of persistent remote dev environments is fairly stable, but the exact commands, template names, product names, and infrastructure references (Ambit, Fly.io, Tailscale, OpenCode, Chromatic) may change over time. Density is **medium**—it includes concrete setup commands, specs, and file names, but remains concise and promotional rather than deeply technical. Originality is mostly **primary source** in the sense that it documents this specific template and its workflow, though it also contains some product-positioning language. This is best used as a **refer-back** resource when deploying or modifying the template. **Scrape quality is good**: the README content appears intact, including commands, table, and file list, though the linked `TECHNICAL.md` and repository context are not included here.
