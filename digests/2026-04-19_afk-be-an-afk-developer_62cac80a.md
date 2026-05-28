---
url: https://afkdev.app/
title: AFK - Be an AFK Developer
scraped_at: '2026-04-19T08:14:24Z'
word_count: 298
raw_file: raw/2026-04-19_afk-be-an-afk-developer_62cac80a.txt
tldr: AFK is a remote desktop app for iOS and Android that lets you use your full Mac development environment from your phone, with low-latency WebRTC, end-to-end encryption, no account, and notifications for AI-agent task completion.
key_quote: Your full dev environment, from your pocket.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- Cursor
- Claude Code
- Codex
- Gemini CLI
- Windsurf
- Amp
- Aider
- OpenCode
- VS Code
- Xcode
- Terminal
- AFK Host
libraries: []
companies: []
tags:
- remote-desktop
- mobile-development
- webrtc
- developer-tools
- end-to-end-encryption
---

### TL;DR
AFK is a remote desktop app for iOS and Android that lets you use your full Mac development environment from your phone, with low-latency WebRTC, end-to-end encryption, no account, and notifications for AI-agent task completion.

### Key Quote
"Your full dev environment, from your pocket."

### Summary
- **What it is:** AFK is a remote desktop app for connecting a phone to a Mac, positioned specifically for “vibe coding” and mobile developer workflows.
- **Platforms:** Supports **iOS** and **Android**; works with **iPhone & iPad** and **Phone & Tablet**.
- **Core promise:** You can access your **full environment** rather than a limited sandbox or terminal-only interface.
- **What you can use it with:** The page explicitly names tools and environments including:
  - **Cursor**
  - **Claude Code**
  - **Codex**
  - **Gemini CLI**
  - **Windsurf**
  - **Amp**
  - **Aider**
  - **OpenCode**
  - **VS Code**
  - **Xcode**
  - **Terminal**
- **Not a sandbox:** AFK emphasizes that it is not a cloud sandbox and does not restrict you to terminal-only access. It provides access to the browser, simulator, databases, and running services on your Mac.
- **Connection model:** Uses **peer-to-peer WebRTC** so the phone connects directly to the Mac.
- **Privacy/security claims:**
  - Screen data and input never touch AFK’s servers.
  - Traffic is encrypted with **DTLS-SRTP**.
  - The signaling server only helps devices find each other.
  - **No account needed**; pairing uses a code and session keys stay on-device.
- **Open-source host:** The host component is open source, with a GitHub link mentioned.
- **AI-agent notifications:** AFK can ping your phone when an AI agent finishes a task or needs attention.
- **Setup flow:** The page shows a terminal example where you install a CLI from the AFK Host menu bar and run:
  - `afk setup`
- **Auto-detection:** It can detect coding tools on your system, including **Claude Code** and **Pi**.
- **Hooks/extensions:** Example setup output shows:
  - Claude Code hooks added to `~/.claude/settings.json`
  - Pi Coding Agent extension installed
- **Reliability behavior:** It claims “silent failure” behavior: if the host app isn’t running, it won’t block your agent.
- **Local-only CLI behavior:** The setup CLI uses a local socket and makes no network calls or API key requests.
- **Product framing:** The page ends with a “Product updates & new features” section header, suggesting it’s a product landing page with ongoing updates.

### Assessment
This is a **mixed** promotional/product page with some technical implementation details. **Durability is medium** because the underlying ideas—remote desktop, WebRTC, encryption, local pairing, mobile dev workflows—are fairly stable, but the specific supported tools, setup steps, and product claims may change as the app evolves. **Density is medium**: it’s concise but includes several concrete technical claims and setup details. **Originality is primary source** since it appears to be the product’s own landing page rather than commentary or aggregation. It’s best used as a **refer-back** reference if you want to confirm what AFK claims to do, how it positions itself against sandboxes/terminal tools, and what privacy model it advertises. **Scrape quality is partial**: the main landing-page copy is captured, but any deeper sections, images, demo content, or linked GitHub details are not present here.
