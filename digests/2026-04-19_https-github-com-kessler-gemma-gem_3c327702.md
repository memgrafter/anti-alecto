---
url: https://github.com/kessler/gemma-gem
title: https://github.com/kessler/gemma-gem
scraped_at: '2026-04-19T20:06:43Z'
word_count: 547
raw_file: raw/2026-04-19_https-github-com-kessler-gemma-gem_3c327702.txt
tldr: Gemma Gem is a Chrome extension that runs Google’s Gemma 4 locally in the browser via WebGPU, letting you chat with pages and automate DOM actions without sending data to the cloud.
key_quote: “Your personal AI assistant living right inside the browser.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- chrome
- pnpm
- webgpu
- wxt
- '@huggingface/transformers'
- marked
libraries:
- '@huggingface/transformers'
- marked
companies:
- Google
tags:
- browser-automation
- local-ai
- chrome-extension
- webgpu
- privacy
---

### TL;DR
Gemma Gem is a Chrome extension that runs Google’s Gemma 4 locally in the browser via WebGPU, letting you chat with pages and automate DOM actions without sending data to the cloud.

### Key Quote
“Your personal AI assistant living right inside the browser.”

### Summary
- **What it is**
  - A browser-based AI assistant Chrome extension called **Gemma Gem**.
  - It runs **Google’s Gemma 4** entirely **on-device via WebGPU**.
  - The project emphasizes **privacy**: no API keys, no cloud, no data leaving the machine.

- **What it can do**
  - Read page content and answer questions about the current site.
  - Click buttons, fill forms, scroll pages, and run JavaScript.
  - Provide a chat UI anchored in the browser, accessible via a gem icon in the bottom-right corner.

- **Requirements**
  - **Chrome with WebGPU support**
  - About **500MB disk** for **E2B**
  - About **1.5GB disk** for **E4B**
  - Model files are cached after the first run.

- **Setup**
  - Install dependencies and build:
    - `pnpm install`
    - `pnpm build`
  - Load the extension from `chrome://extensions` using developer mode, from `.output/chrome-mv3-dev/`.

- **Usage flow**
  - Visit any page.
  - Click the gem icon to open chat.
  - Wait for model loading progress.
  - Ask questions or request actions on the page.

- **Architecture**
  - **Offscreen Document**
    - Hosts Gemma 4 using `@huggingface/transformers` + WebGPU.
    - Runs the agent loop.
    - Handles token streaming and inference.
  - **Service Worker**
    - Routes messages between content scripts and offscreen document.
    - Handles `take_screenshot` and `run_javascript`.
  - **Content Script**
    - Injects the gem icon and shadow DOM chat overlay.
    - Executes DOM tools like reading content, clicking, typing, and scrolling.

- **Available tools**
  - `read_page_content` — read page text/HTML or a CSS selector
  - `take_screenshot` — capture the visible page as PNG
  - `click_element` — click an element by CSS selector
  - `type_text` — type into an input by CSS selector
  - `scroll_page` — scroll up/down by pixels
  - `run_javascript` — execute JS in the page context with full DOM access

- **Settings**
  - Model selection between **Gemma 4 E2B (~500MB)** and **E4B (~1.5GB)**
  - Toggle **native thinking**
  - Set **max iterations** for tool-call loops
  - **Clear context** for the current page
  - **Disable on this site** per hostname

- **Development and debugging**
  - Development build:
    - `pnpm build`
  - Production build:
    - `pnpm build:prod`
  - Logs are prefixed with **`[Gemma Gem]`**
  - Useful inspection points:
    - service worker logs via `chrome://extensions`
    - offscreen document logs via `chrome://extensions`
    - content script logs in page DevTools
    - `chrome://inspect#other` for extension contexts
  - The offscreen document logs are highlighted as the most useful for model loading, prompts, token counts, raw output, and tool execution.

- **Tech stack**
  - **WXT** for the Chrome extension framework
  - **@huggingface/transformers** for browser ML inference
  - **marked** for Markdown rendering
  - Gemma 4 E2B/E4B ONNX models with **q4f16 quantization** and **128K context**

- **Additional note**
  - The `agent/` directory has **zero dependencies** and defines interfaces like `ModelBackend` and `ToolExecutor`, making it extractable as a standalone library.

### Assessment
This is a **mixed** reference-and-project README with high practical value for anyone wanting to install, understand, or modify the extension. Its **durability is medium**: the core ideas of local browser AI and extension architecture are fairly durable, but the specific model names, package choices, build commands, and Chrome/WebGPU requirements may age as the project evolves. The content is **dense** and mostly **primary-source** documentation, not commentary or synthesis. It works best as a **refer-back** reference for setup, architecture, and debugging, though it can be skimmed once to assess whether the project fits a privacy-preserving browser-agent use case. The scrape quality appears **good** overall: it includes the main README sections, tool table, commands, and notes, though embedded images are referenced but not viewable in the text capture.
