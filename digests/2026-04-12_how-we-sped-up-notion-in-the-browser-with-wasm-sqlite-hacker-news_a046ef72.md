---
url: https://news.ycombinator.com/item?id=40949489
title: How we sped up Notion in the browser with WASM SQLite | Hacker News
scraped_at: '2026-04-12T10:41:39Z'
word_count: 5385
raw_file: raw/2026-04-12_how-we-sped-up-notion-in-the-browser-with-wasm-sqlite-hacker-news_a046ef72.txt
tldr: This Hacker News thread debates Notion’s use of WASM SQLite in the browser, arguing that local SQLite can dramatically reduce latency and cloud costs, but also exposing tradeoffs around startup time, browser file/storage APIs, multi-tab concurrency, and whether web apps should rely more on local databases at all.
key_quote: “Using SQLite improved page navigation times by 20 percent in all modern browsers.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Roy Hashimoto
- Gleb
tools:
- SQLite
- WASM
- LocalStorage
- IndexedDB
- OPFS
- DuckDB
- Ollama
- Dexie
- Capacitor
- Electron
- PostgreSQL
- RDS
libraries:
- sqldelight
companies:
- Notion
- AWS
- Firefox
- Chrome
- Safari
- Webkit
- Mozilla
- Coda
- OpenAI
tags:
- browser-storage
- sqlite
- wasm
- local-first
- web-apps
---

### TL;DR
This Hacker News thread debates Notion’s use of WASM SQLite in the browser, arguing that local SQLite can dramatically reduce latency and cloud costs, but also exposing tradeoffs around startup time, browser file/storage APIs, multi-tab concurrency, and whether web apps should rely more on local databases at all.

### Key Quote
“Using SQLite improved page navigation times by 20 percent in all modern browsers.”

### Summary
- The thread centers on a Notion performance post about speeding up browser-based Notion by moving database work into **SQLite compiled to WebAssembly (WASM)**.
- A major theme is the appeal of **local-first databases**:
  - A commenter says scanning a **30–100 MiB SQLite DB** locally on an SSD can happen in milliseconds.
  - Another side project, **“cluttr,”** uses WASM SQLite in-browser to clean up screenshots, add OCR search, and even use **Ollama** vision models locally.
- The thread repeatedly contrasts **browser-local storage** with **cloud/database infrastructure**:
  - Cloud IOPS are described as expensive and often overkill for many workloads.
  - Several commenters argue that **network latency**, **CPU limits**, and **real workload constraints** matter more than raw IOPS.
  - Others counter that cloud storage brings major benefits: redundancy, automatic scaling, easy recovery, and decoupled storage/compute.
- There is a detailed discussion of **Notion’s architecture and storage layers**:
  - Notion staff explain they used **LocalStorage**, then **IndexedDB**, then **SQLite** for native apps, and that the browser version’s SQLite cache is **optional**.
  - Reasons for moving away from LocalStorage:
    - **10 MB limit**
    - write loss with multiple tabs
    - synchronous deletion causing UI lag
  - Reasons IndexedDB underperformed:
    - high per-row overhead
    - browser variability
    - contention on large workspaces and multiple tabs
    - hard-to-debug reliability issues
- Several comments discuss why **SQLite in the browser** is attractive but still awkward:
  - Startup can be slow because the **WASM binary must load and initialize**.
  - **OPFS (Origin Private File System)** and related APIs are criticized for poor concurrency behavior and awkward tooling.
  - Some users wish browsers would simply expose “real files,” while others note browsers need sandboxing and cross-platform abstraction.
- There’s a broader philosophical debate about **web apps vs desktop apps**:
  - Some users say modern SaaS has pushed too much into the browser.
  - Others argue customers prefer web apps because installation and admin permissions are friction.
  - Notion is repeatedly described as having become slower and more bloated over time, especially compared with its earlier, simpler version.
- The thread also includes skepticism and caveats:
  - Some commenters say the **20% navigation improvement** may be partly due to caching strategy changes, not just SQLite itself.
  - Others note **SQLite is not fully SQL-92 compliant**, and using it as a browser standard would have been controversial.
  - There are concerns about **multi-tab coordination**, **browser bugs**, **Safari limitations**, and **production debugging**.
- Positive takeaways:
  - WASM SQLite is seen as a real, production-proven option for some workloads.
  - It can enable more **offline-capable**, **client-heavy**, and **server-light** apps.
  - Notion’s experience is presented as evidence that browser-based local databases are becoming viable, even if the implementation is still messy.

### Assessment
This is a **mixed** thread with a high density of practical details, but it is not a single coherent article so much as a long discussion around the Notion performance post. **Durability is medium**: the architectural arguments about local databases, latency, IndexedDB, OPFS, and browser-vs-desktop tradeoffs will remain relevant, but specific browser support, performance claims, and Notion’s implementation details are version- and platform-sensitive. The content type is **mixed** (technical discussion, opinion, and partial first-hand experience). It is mostly a blend of **commentary** and some **primary-source-like disclosures** from a Notion employee, rather than a formal tutorial or research piece. As a reference, it is best used **refer-back** for understanding browser SQLite tradeoffs, Notion’s storage evolution, and the broader argument about local-first web apps. **Scrape quality is good** for text discussion, but there are no images or code blocks here, and the thread is fragmented because it includes many comments rather than a polished article.
