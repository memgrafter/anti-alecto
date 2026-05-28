---
url: https://www.reddit.com/r/SillyTavernAI/comments/1q300mf/aventura_a_frontend_for_adventure_rp_and_creative/
title: 'Aventura | A frontend for adventure RP and creative writing : SillyTavernAI'
scraped_at: '2026-04-19T21:37:25Z'
word_count: 3342
raw_file: raw/2026-04-19_aventura-a-frontend-for-adventure-rp-and-creative-writing-sillytavernai_3506461d.txt
tldr: Reddit thread in r/SillyTavernAI announcing Aventura, a new alpha frontend for adventure RP/creative writing; top commenter says it looks incredible but wants more provider support beyond OpenRouter and likes the editable prompts.
key_quote: ST only being able to do singel-call gens has been one of the biggest limitations imo.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- AuYsI
- unkarelian
- AltpostingAndy
tools:
- SillyTavern
- OpenRouter
- KoboldCPP
- harper
- NanoGPT
libraries: []
companies:
- OpenRouter
- NanoGPT
tags:
- creative-writing
- roleplay
- frontend
- local-llm
- openrouter
---

### TL;DR
Reddit thread in r/SillyTavernAI announcing **Aventura**, a new alpha frontend for adventure RP/creative writing; top commenter **u/AltpostingAndy** says it looks incredible but wants more provider support beyond OpenRouter and likes the editable prompts.

### Key Quote
> “ST only being able to do singel-call gens has been one of the biggest limitations imo.”

### Summary
- **Top comment (verbatim):** "This looks incredible, I love that all of the prompts are easily viewable and editable. ST only being able to do singel-call gens has been one of the biggest limitations imo. Are there any plans to allow API endpoints other than openrouter?"
- **Top commenter:** `u/AltpostingAndy`
- **Thread topics:**
  - OpenRouter-first design vs. requests for **custom providers / OpenAI-compatible endpoints / local LLMs**
  - Feature feedback on **UI/UX**, screenshots, walkthroughs, imports, and mobile use
  - Bugs and rough edges: **POV inconsistency, text resize, Generate 3, hotkeys, context limit confusion**
  - Requests for **cloud sync**, **TTS**, **image support**, **translation**, and more control/customization
  - Comparisons to **SillyTavern**: Aventura is praised for automation and parallel requests, but seen as less flexible

- **What Aventura is:**
  - An **alpha release** of a frontend by `u/AuYsI` (`unkarelian`, maker of **timeline-memory** and **openvault**) for **adventure RP and creative writing**
  - Requires only an **OpenRouter API key** for the initial release; the author says everything is preconfigured

- **Why the author built it instead of using SillyTavern:**
  - Reported ST limitations included:
    - inability to run **several requests at the same time**
    - inability to run requests **in the background**
    - not returning **reasoning content** the way OpenRouter expects

- **Built-in features advertised by the author:**
  - **Tracker** for events, characters, plot points, inventory, etc.
  - **Multiple-choice options** for creative writing and adventure mode
  - **Long-term memory** using the same system as timeline-memory, but faster due to **parallel queries**
  - **Automatic lorebook management** in the background
  - **LLM-based lorebook retrieval** instead of embeddings
  - **Anti-slop automation** using an LLM rather than programmatic detection
  - **Setup wizard** for new scenarios with AI assistance
  - **Spell checker** using **harper**
  - **Lorebook classification** using LLMs
  - A **mobile app / .apk** for Android users
  - Mostly **automatic behavior**, including summarization triggered by context length

- **Models named in the release:**
  - **Grok 4/4.1 Fast**: classification, tracker, routes, slop tracking
  - **Deepseek v3.2**: setup wizard, creative writing options
  - **Minimax M2.1**: agentic tasks like timeline-fill and lorebook management
  - **GLM 4.7**: main narrative generations

- **Planned future features:**
  - Other providers
  - **TTS**
  - **Embedded images** in text
  - Later replies clarify the author is planning **OpenAI-compatible APIs**; NanoGPT and other provider support came up repeatedly

- **Author responses and clarifications:**
  - Said other providers will come, likely **NanoGPT first**
  - Said **OpenAI-compatible API** support is planned
  - Clarified the app’s **8k context** setting refers to **output context length**, not input
  - Said the latest version fixed the issue where pressing number keys could accidentally trigger multiple-choice responses
  - Mentioned a **Discord server** linked from the library page for feedback

- **Main praise in the thread:**
  - People liked the **editable prompts**, the **automation**, the **Android build**, and the fact that it feels like a smoother alternative for RP/story generation

- **Main criticism / concerns:**
  - Heavy reliance on **OpenRouter** in the initial version
  - Desire for **local LLM support** like KoboldCPP
  - Desire for more **customization knobs**
  - Some users reported **bugs** and **workflow friction**
  - Some want better **imports** from ST/CHUB, avatars/images, and device sync

### Assessment
This is a high-signal Reddit launch thread with lots of practical feedback, so it’s useful as both a product snapshot and a requirements backlog. **Durability: medium** — the core ideas (automated RP frontend, parallel calls, memory/lorebook orchestration) are durable, but the exact model/provider setup and alpha bugs will age quickly. **Content type: mixed** — mostly announcement plus community commentary and bug reports. **Density: medium-high** because the post lists concrete features, model choices, and limitations, while the replies add detailed user requirements. **Originality: primary source + commentary** — the OP is the author’s own announcement, with community reactions layered on top. **Reference style: refer-back** if you’re tracking Aventura’s evolution or comparing it to SillyTavern; otherwise skim-once. **Scrape quality: good** — the thread capture includes the original post, prominent comments, and a substantial discussion sample, though it likely omits the full 92-comment conversation and any screenshots/media that may have been attached.
