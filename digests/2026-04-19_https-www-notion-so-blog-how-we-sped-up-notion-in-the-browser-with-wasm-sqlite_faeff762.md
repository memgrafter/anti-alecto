---
url: https://www.notion.so/blog/how-we-sped-up-notion-in-the-browser-with-wasm-sqlite
title: https://www.notion.so/blog/how-we-sped-up-notion-in-the-browser-with-wasm-sqlite
scraped_at: '2026-04-19T21:19:44Z'
word_count: 2110
raw_file: raw/2026-04-19_https-www-notion-so-blog-how-we-sped-up-notion-in-the-browser-with-wasm-sqlite_faeff762.txt
tldr: Notion describes how it sped up browser page navigation by 20% using WASM SQLite with OPFS, eventually shipping a SharedWorker-based architecture that avoids corruption and cross-tab contention while preserving caching across tabs.
key_quote: Using SQLite improved page navigation times by 20 percent in all modern browsers.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Roy Hashimoto
tools:
- Webpack
- Web Workers
- SharedWorker
- Service Workers
- Web Lock
- Comlink
libraries:
- sqlite3
companies:
- Notion
tags:
- browser-performance
- webassembly
- sqlite
- opfs
- web-workers
---

### TL;DR
Notion describes how it sped up browser page navigation by 20% using WASM SQLite with OPFS, eventually shipping a SharedWorker-based architecture that avoids corruption and cross-tab contention while preserving caching across tabs.

### Key Quote
"Using SQLite improved page navigation times by 20 percent in all modern browsers."

### Summary
- Notion had already used SQLite client-side caching to speed up its Mac, Windows, and mobile apps, and extended the same idea to the web browser.
- The browser implementation uses:
  - **SQLite compiled to WebAssembly**
  - **OPFS (Origin Private File System)** for persistence
  - **Web Workers** to keep database work off the main thread
  - **Comlink** to simplify message passing between main thread and worker
- Their final architecture:
  - Each tab gets its own dedicated Web Worker.
  - Only one tab is allowed to be the **active tab** at a time.
  - A **SharedWorker** coordinates which tab is active.
  - Queries from any tab are routed through the SharedWorker to the active tab’s worker.
  - This allows multiple tabs to benefit from caching without multiple simultaneous writers corrupting the DB.
  - Tab liveness is detected using an “infinitely-open” Web Lock.
- Performance impact:
  - **20% faster page navigation** overall in modern browsers.
  - Larger wins in slower network regions:
    - **28% faster in Australia**
    - **31% faster in China**
    - **33% faster in India**
- Why the simpler approach failed:
  - **Cross-origin isolation** would have been required for one OPFS variant, but Notion depends on many third-party scripts and iframes, making this impractical.
  - A first attempt caused **database corruption** for some users, producing wrong page data and inconsistent rows.
  - The alternative OPFS variant avoided corruption but only worked in **one tab at a time**, which was unacceptable for a multi-tab product.
- Their chosen solution:
  - Use **OPFS SyncAccessHandle Pool VFS** because it avoids the cross-origin-isolation requirement.
  - Wrap it in the SharedWorker/multi-tab architecture so all tabs still get caching.
- Regressions they had to fix:
  - **Initial page load got slower** because the WASM SQLite library download blocked startup.
    - Fix: load SQLite asynchronously so it does not block the page load.
    - After this, initial load returned to parity with control.
  - **Slow devices regressed at the 95th percentile**
    - Some devices read disk slower than the API.
    - Fix: race SQLite vs API and use whichever returns first for navigation clicks.
- Conclusion / lessons:
  - OPFS concurrency handling is not graceful by default; applications must design around it.
  - Web Workers, SharedWorkers, and Service Workers have different roles and can be combined.
  - Cross-origin isolation is still difficult for complex apps with third-party dependencies.
  - The final rollout delivered the navigation speedup without corruption issues or other metric regressions.

### Assessment
This is a high-density technical engineering post with medium-to-high durability: the specific APIs and browser constraints may age, but the architectural lessons about concurrency, worker coordination, and performance tradeoffs will remain useful. It is a mixed content type, but primarily a tutorial/technical case study with some announcement elements. The originality is strong and appears to be a primary-source engineering writeup from Notion, not a synthesis. It is best used as a refer-back or deep-study reference if you are evaluating browser-side persistence, WASM SQLite, OPFS, or multi-tab coordination patterns. Scrape quality looks good: the main narrative, metrics, and conclusions are present, though code snippets, figures, and any embedded diagrams are not included.
