---
url: https://github.com/astrskai/astrsk
title: 'astrskai/astrsk: Pushing the boundaries of AI storytelling'
scraped_at: '2026-04-16T05:46:20Z'
word_count: 999
raw_file: raw/2026-04-16_astrskai-astrsk-pushing-the-boundaries-of-ai-storytelling_4eaf27bd.txt
tldr: astrskai/astrsk is a README for a local-first, cross-platform AI storytelling app that emphasizes customizable agents, a visual flow editor, PWA/Electron builds, and self-hosting guidance.
key_quote: Advanced AI agents • Customizable response formatting • Flexible prompt editing • Immersive roleplaying
durability: medium
content_type: mixed
density: medium-high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- React
- Vite
- Tailwind CSS
- TanStack Router
- TanStack Query
- Zustand
- shadcn/ui
- Electron
- PGlite
- Vercel AI SDK
- Drizzle ORM
- pnpm
libraries: []
companies:
- astrsk.ai
- OpenAI
- Anthropic
- Google AI
- DeepSeek
- Ollama
- xAI
tags:
- ai-storytelling
- local-first
- pwa
- electron
- self-hosting
---

### TL;DR
`astrskai/astrsk` is a README for a local-first, cross-platform AI storytelling app that emphasizes customizable agents, a visual flow editor, PWA/Electron builds, and self-hosting guidance.

### Key Quote
“Advanced AI agents • Customizable response formatting • Flexible prompt editing • Immersive roleplaying”

### Summary
- **What this repository is**
  - GitHub repo: `astrskai/astrsk`
  - Product positioning: “Pushing the boundaries of AI storytelling”
  - The README frames it as an AI storytelling / roleplaying app with configurable agents and prompt formatting.

- **Core features claimed**
  - **Complete AI Agent Control**
    - Custom prompts, output schemas, and response formatting
    - Import character cards v2/v3 or create agents from scratch
    - Supports 10+ AI providers, including OpenAI, Anthropic, Google AI, DeepSeek, Ollama, and xAI
  - **Visual Flow (AI agent workflow) Editor**
    - Drag-and-drop conversation flow design
    - Conditional branching is listed as “coming soon”
    - Real-time prompt preview and testing with actual roleplay sessions
  - **100% Local-First**
    - Data stored locally on the device
    - No account required, no data collection
    - Export and backup supported
  - **True Cross-Platform**
    - Progressive Web App for browser-based use
    - Native desktop apps for Windows, macOS, and Linux are listed as “coming soon”
    - Offline support via PWA is claimed

- **Tech stack / implementation**
  - Frontend: React, TypeScript, Vite, Tailwind CSS
  - Database: PGlite, described as PostgreSQL compiled to WebAssembly
  - AI integration: Vercel AI SDK with multiple providers
  - State/routing/UI: TanStack Router, TanStack Query, Zustand, shadcn/ui
  - Desktop: Electron wrapper with auto-updater
  - Project structure separates `apps/pwa`, `apps/electron`, and `packages/design-system`

- **Installation and development**
  - Releases are distributed as:
    - Windows: `astrsk-X.Y.Z.exe`
    - Mac: `astrsk-X.Y.Z.dmg`
    - Linux: `astrsk-X.Y.Z.AppImage` (not tested)
  - Development prerequisites:
    - Node.js v22+
    - pnpm v10+
  - Main scripts:
    - `pnpm install`
    - `pnpm dev:pwa`
    - `pnpm build:pwa`
    - `pnpm dev:electron`
    - `pnpm build:electron`

- **Self-hosting notes**
  - The README explains that PWA features rely on secure contexts because of OPFS, PGlite, and service workers.
  - For LAN/self-hosted access, it instructs users to:
    - install `@vitejs/plugin-basic-ssl` with  
      `pnpm --filter pwa add -D @vitejs/plugin-basic-ssl`
    - add `basicSsl()` to `apps/pwa/vite.config.ts`
    - set `server: { host: true }`
  - It shows the dev server then serving HTTPS network addresses, e.g. `https://172.30.1.34:5173/`
  - It warns that Chrome may require proceeding through the self-signed certificate warning.

- **References and links**
  - Website: `astrsk.ai`
  - Docs: `docs.astrsk.ai`
  - Discord, Reddit `r/astrsk_ai`, X `@astrskai`, LinkedIn, Medium are all listed
  - License: **AGPL-v3**

### Assessment
This is a **mixed** README and product landing page with some setup/documentation content. Durability is **medium**: the concepts of local-first AI apps, PWA, Electron, and self-hosting are fairly durable, but the exact tech versions, release assets, and “coming soon” items can go stale quickly. Density is **medium-high** because it packs features, stack, structure, install commands, and self-hosting instructions into one page, though it is still promotional in tone. Originality is mainly **primary source** since it describes the project from the maintainers’ perspective rather than summarizing others. Reference style is **refer-back** if you need install/self-hosting commands or the repo’s feature list; otherwise it also works as a **skim-once** product overview. Scrape quality is **partial**: the text captured the README content well, but the header image, logo, and demo video thumbnail are not meaningfully represented here, and those visuals may affect how the project is interpreted. For finding this page later, the most distinctive identifiers are the exact repo name `astrskai/astrsk`, the release asset names `astrsk-X.Y.Z.exe`, `astrsk-X.Y.Z.dmg`, `astrsk-X.Y.Z.AppImage`, and the self-hosting SSL step using `@vitejs/plugin-basic-ssl`.
