# OpenCode on Ambit

A persistent [OpenCode](https://opencode.ai) workspace that runs in the cloud and follows you across devices. 

You can start a coding session on your laptop, then continue on your phone — same workspace, same state, nothing to sync.

## Why This Exists

OpenCode is an agent-driven IDE that's normally tied to whatever machine you run it on. When you close your laptop, your session disappears.

This template runs OpenCode on [Ambit](https://github.com/ToxicPine/ambit) as a persistent web workspace on your private network. Your session survives reboots, you can access it from any of your devices using the browser (connection via Tailscale), and it stays invisible to the public internet.

**You get seamless mobile and desktop handoff.** This gives you a real development environment that moves with you instead of being stuck on your hardware, i.e. terminal sessions stay alive when you close the tab and conversations with agents continue where you left off. 

You can start debugging on your laptop, close the browser, and pick it up on your phone to find the same terminals, same context, and same work in progress waiting for you.

## What You Get

- **OpenCode Web UI** at `http://<name>.<network>` — accessible from any device on your Tailscale network
- **Automatic Suspend/Resume** — the machine suspends when idle and wakes on the next HTTP request, so you only pay for what you use
- **Pre-Configured Environment** — git, node, bun, deno, gh, tmux, vim, curl, and more, all declaratively configured
- **Self-Orchestation Plugin** pre-installed — OpenClaw-style self-orchestration built into your OpenCode instance
- **Customizable** — edit `home.nix` to add packages, change shell config, or add programs, then run `rebuild`

## Setup

You can deploy OpenCode to [Ambit](https://github.com/ToxicPine/ambit), which wraps Fly.io.

```bash
npx skills add ToxicPine/ambit-skills --skill ambit-cli  # optional, but helpful for AI agents
npx @cardelli/ambit create lab
npx @cardelli/ambit deploy my-ide.lab --template ToxicPine/ambit-templates/opencode
```

Open `http://my-ide.lab` on any device on your Tailscale network.

## Bonus: Cloud Browser on Your Private Network

You can deploy Playwright, and even computer-use agents, using [Chromatic](../chromatic/) on the same Ambit network.

```bash
npx @cardelli/ambit deploy my-browser.lab --template ToxicPine/ambit-templates/chromatic
```

Normally, running computer-use agents to automatically debug software against a local dev server from the cloud means setting up ngrok or Cloudflare tunnels, which is frustrating and comes with security risk. With Chromatic on Ambit, the cloud browser can access `http://localhost:3000` in your Ambit OpenCode, or even your local dev device, without any fuss.

## Default Specs (Configurable)

| | |
|---|---|
| CPU | 2x shared |
| Memory | 2 GB |
| Disk | 16 GB persistent volume |
| Auto stop | Suspend when idle |
| Auto start | Wake on HTTP request |

## Files

```
system.nix   — entrypoint, daemons, system packages
home.nix     — user packages and shell config (edit this)
users.nix    — user accounts
fly.toml     — Fly.io deployment config
flake.nix    — Nix flake wiring (you shouldn't need to touch this)
lib/         — plumbing (entrypoint, image builder, setup scripts)
```

> For details on the Nix image builder, daemon system, reload behaviour, and flake layout, see [TECHNICAL.md](./TECHNICAL.md).
