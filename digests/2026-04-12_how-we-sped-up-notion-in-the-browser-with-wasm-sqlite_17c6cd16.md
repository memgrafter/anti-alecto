---
url: https://www.notion.com/blog/how-we-sped-up-notion-in-the-browser-with-wasm-sqlite
title: How we sped up Notion in the browser with WASM SQLite
scraped_at: '2026-04-12T09:41:31Z'
word_count: 2110
raw_file: raw/2026-04-12_how-we-sped-up-notion-in-the-browser-with-wasm-sqlite_17c6cd16.txt
tldr: Notion sped up browser navigation by moving its client-side cache to WASM SQLite in OPFS, but only after building a SharedWorker-based architecture to avoid cross-tab corruption and cross-origin isolation limits.
key_quote: Using SQLite improved page navigation times by 20 percent in all modern browsers.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Roy Hashimoto
tools:
- Comlink
- Web Workers
- SharedWorker
- Web Locks
- Origin Trials
libraries:
- sqlite3
companies:
- Notion
tags:
- browser-performance
- wasm
- sqlite
- opfs
- web-workers
---

### TL;DR
Notion sped up browser navigation by moving its client-side cache to WASM SQLite in OPFS, but only after building a SharedWorker-based architecture to avoid cross-tab corruption and cross-origin isolation limits.

### Key Quote
“Using SQLite improved page navigation times by 20 percent in all modern browsers.”

### Summary
- **What Notion changed**
  - Notion had already used SQLite caching in its Mac/Windows desktop app and native mobile app.
  - This post explains how they brought the same performance improvement to the browser using a WebAssembly implementation of SQLite.

- **Measured impact**
  - Page navigation improved by **20%** overall in modern browsers.
  - Larger gains appeared where API latency was worse:
    - **28%** faster in Australia
    - **31%** faster in China
    - **33%** faster in India

- **Core browser technologies used**
  - **OPFS (Origin Private File System)** for persistent storage in the browser.
  - **Web Workers** to run SQLite off the main thread.
  - **Comlink** to simplify messaging between the main thread and workers.
  - **SharedWorker** to coordinate which tab is allowed to write to SQLite.
  - **Web Locks** to detect when a tab closes.

- **Final architecture**
  - Each tab gets its own dedicated Web Worker.
  - Only one tab is designated the **active tab**.
  - A **SharedWorker** routes SQLite queries to the active tab’s Worker.
  - This lets many tabs issue queries while ensuring only one tab writes at a time.
  - They used the **OPFS SyncAccessHandle Pool VFS** implementation, which works across major browsers.

- **Why simpler designs failed**
  - **Cross-origin isolation problem**
    - The `sqlite3_vfs` approach required cross-origin isolation.
    - That would have forced Notion to change headers and iframe behavior across many third-party dependencies.
    - They only partially tested this using **Origin Trials for SharedArrayBuffer** on Chrome and Edge.
  - **Database corruption**
    - With one Worker per tab writing directly, some users saw corrupted SQLite data.
    - Symptoms included wrong comments, wrong page previews, duplicate IDs, and data consistency errors.
    - The likely cause was poor concurrency handling with OPFS when multiple tabs wrote simultaneously.
  - **Single-tab limitation of the alternative**
    - The **OPFS SyncAccessHandle Pool VFS** variant avoided corruption and didn’t need cross-origin isolation.
    - But it could only run in one tab at a time, which didn’t fit Notion’s multi-tab use case.

- **Why they chose the shipped approach**
  - The SharedWorker routing design worked with both SQLite variants.
  - They ultimately shipped **OPFS SyncAccessHandle Pool VFS** because it avoided the cross-origin isolation requirement and could therefore work beyond Chrome and Edge.

- **Regressions they had to fix**
  - **Slower initial page load**
    - WASM SQLite was a few hundred KB and initially blocked page load.
    - They changed it to load **asynchronously**, making startup performance match the control group.
  - **Slow devices got worse**
    - Some slower devices, especially mobile phones, read from disk too slowly for cache access to always beat the API.
    - They fixed this by “racing” disk and API requests and using whichever returned first.
    - This restored the 95th percentile navigation performance.

- **Main lessons**
  - OPFS does not handle concurrency gracefully by default.
  - Web Workers, SharedWorkers, and Service Workers can be combined to solve different parts of the problem.
  - Full cross-origin isolation is still hard for complex apps with many third-party scripts.
  - The final result delivered the performance win without observable corruption issues.

### Assessment
This is a **mixed** technical case study and engineering retrospective with high practical value. Durability is **medium**: the architectural lessons around OPFS, workers, concurrency, and browser tradeoffs are likely to remain useful, but specific implementation constraints and browser support details may age. The content is **high-density** and fairly detailed, with concrete performance numbers, browser APIs, and failure modes. It is primarily a **primary source** from Notion’s engineering team, though it references an external GitHub discussion and prior mobile work. It’s best used as **deep-study** material if you’re designing browser-side persistence or multi-tab synchronization, and as a **refer-back** reference for the specific architecture and tradeoffs. Scrape quality appears **good**: the main article text, conclusions, and performance metrics are present, though any diagrams, code snippets, or embedded visuals are not included.
