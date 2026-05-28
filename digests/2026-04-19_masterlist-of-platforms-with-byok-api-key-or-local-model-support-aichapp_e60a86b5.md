---
url: https://www.reddit.com/r/aichapp/comments/1pjydtm/masterlist_of_platforms_with_byok_api_key_or/
title: 'Masterlist of Platforms With BYOK (API Key) or Local Model Support : aichapp'
scraped_at: '2026-04-19T21:27:49Z'
word_count: 610
raw_file: raw/2026-04-19_masterlist-of-platforms-with-byok-api-key-or-local-model-support-aichapp_e60a86b5.txt
tldr: A Reddit resource post in r/aichapp by u/Exciting-Mall192 catalogs BYOK and local-model chat/story platforms, and the top reply from u/rakanssh endorses Hakawati as an interactive-fiction client that fills a niche for game-like local/BYOK apps.
key_quote: I'm a resource to help proxy users to find suitable platform for their needs.
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Exciting-Mall192
- rakanssh
- Forward_Reaction6744
tools:
- LM Studio
- KoboldCPP
- SillyTavern
- llama.cpp
- Oobabooga
- OpenRouter
libraries: []
companies:
- OpenAI
- Claude
- DeepSeek
- Anthropic
- Chutes
- Backyard AI
tags:
- byok
- local-models
- chat-platforms
- interactive-fiction
- roleplay
---

### TL;DR
A Reddit resource post in r/aichapp by u/Exciting-Mall192 catalogs BYOK and local-model chat/story platforms, and the top reply from u/rakanssh endorses Hakawati as an interactive-fiction client that fills a niche for game-like local/BYOK apps.

### Key Quote
“I'm a resource to help proxy users to find suitable platform for their needs.”

### Summary
- **Top comment (verbatim):** “I've been working on a client catered specifically towards interactive stories. Free/OSS. Still actively being developed but fully playable: [Hakawati.dev](http://Hakawati.dev) Also on [Itch.io](https://rakanssh.itch.io/hakawati) and [github](https://github.com/rakanssh/hakawati) Feel free to remove this comment if it's inappropriate, just noticed a lack of interactive fiction/game-y clients supporting local models/BYOK.”
- **Top commenter:** `u/rakanssh`
- **Thread topics:**
  - Master list of chat platforms that support **BYOK API keys**
  - Which apps support **local models** natively vs via **networked backends**
  - Mobile, desktop, and web clients for roleplay / interactive storytelling
  - Niche clients for **game-like / interactive fiction** use cases
  - Corrections and additions to the platform list, including beta/deprecated status

- The original post is explicitly framed as a **non-promotional resource** for “proxy users” who either:
  - bring their own API key, or
  - rely on local models.
- It defines the main categories:
  - **BYOK** = user supplies paid API keys from providers like OpenAI, Claude, DeepSeek, OpenRouter.
  - **Local (Native)** = model runs directly on the device, usually GGUF, with RAM/storage/CPU/battery cost.
  - **Local (Network)** = app connects to another device on the same network running the backend.
  - **Frontend UI** = only a UI; requires API or local backend.
  - **All-in-One** = includes its own local backend and may also support BYOK.

- The post then lists platforms in two sections:

  **Front-end UI / BYOK / network-local support**
  - **Agnaistic** — BYOK + local network, web
  - **Chattica** — BYOK + local network, Android; self-host only via LM Studio and KoboldCPP; iOS coming soon
  - **Chub AI** — BYOK, web/Android APK/iOS coming soon
  - **Duren AI** — BYOK, web
  - **Hakawati** — BYOK + local network, desktop app
  - **Janitor AI** — BYOK, web; iOS/Android coming soon
  - **Lettuce AI** — BYOK, Android APK; beta
  - **Loreblendr** — BYOK + local network, iOS; beta; supports MCP plugin
  - **MegaNova Chat** — BYOK, web; beta
  - **NeoTavern** — local network only, desktop/Android; rewritten frontend for SillyTavern
  - **OMate Chat** — BYOK, Android/iOS
  - **Risu AI** — BYOK + local network, web/desktop
  - **Saucepan AI** — BYOK, web; only supports OpenAI, DeepSeek, Anthropic, and Chutes
  - **School House AI** — BYOK, desktop app; Android coming soon; beta
  - **SillyTavern** — BYOK + local network, desktop and Android via Termux
  - **TavernAI** — local network only, desktop; older/deprecated legacy version of SillyTavern
  - **Tavo** — BYOK, Android/iOS
  - **WyvernChat** — BYOK, web; beta

  **All-in-One / local native support**
  - **Backyard AI** — local native only in desktop app; desktop is deprecated
  - **ChatterUI** — BYOK + local native + local network; Android APK
  - **Hammer AI** — BYOK + local native; desktop and web; web can run local models via WebGPU
  - **Layla** — local native only; APK lite is free; paid Android and iOS apps
  - **Maid** — BYOK + local native; Android
  - **PocketPal** — local native only; Android and iOS

- The author adds a specific correction about **Backyard AI**:
  - Android, iOS, and web versions rely on Backyard’s proprietary cloud service.
  - They **do not** support BYOK or local phone-side model execution.
  - Only the legacy desktop app supports local models.

- The thread’s discussion is small but supportive:
  - One top-level reply is just a short GIF reaction from `u/Forward_Reaction6744`.
  - `u/rakanssh` promotes **Hakawati** as a free/open-source client for interactive stories and local/BYOK use.
  - The original poster replies that they will add it to the list later.

### Assessment
This is a practical, fairly dense resource post with a moderate-to-high durability profile: the general distinctions between BYOK, local native, and networked backends are durable, but the platform list itself will age quickly as apps change beta status, pricing, and support. The content type is a mixed reference/social thread: mainly a curated reference list, with a small discussion layer. Originality is mostly synthesis/aggregation rather than primary research, though it adds useful categorization and a correction about Backyard AI. It’s best used as a skim-once or refer-back reference for checking which roleplay/chat clients support BYOK or local models. Scrape quality is good overall: the post content, table entries, and top comments are preserved, though the thread is short and there are no missing code blocks or images beyond the visible GIF reaction.
