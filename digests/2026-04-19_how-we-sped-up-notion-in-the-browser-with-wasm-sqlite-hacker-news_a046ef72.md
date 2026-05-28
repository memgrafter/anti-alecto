---
url: https://news.ycombinator.com/item?id=40949489
title: How we sped up Notion in the browser with WASM SQLite | Hacker News
scraped_at: '2026-04-19T21:38:51Z'
word_count: 4403
raw_file: raw/2026-04-19_how-we-sped-up-notion-in-the-browser-with-wasm-sqlite-hacker-news_a046ef72.txt
tldr: Hacker News thread on Notion’s engineering post about speeding up the browser app with WASM SQLite, where the top comment simply punts readers to an earlier HN discussion and the broader thread debates whether browser SQLite/OPFS is production-ready, what browser APIs are missing, and whether Notion should instead expose real offline mode.
key_quote: There's a multiple readers and writers proposal [0].
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- jFriedensreich
- gnabgib
- nafey
- AlexErrant
- slightwinder
- bearjaws
- nikeee
- stpn
- jitl
- simonw
- compressedgas
- NewtonSpock
- NelsonMinar
- kevingadd
- fastball
- dbalatero
tools:
- WASM SQLite
- OPFS
- SharedWorker
- IndexedDB
- WebSQL
- Dexie
- DuckDB
- SQLite
libraries:
- wa-sqlite
- IDBMirrorVFS
companies:
- Notion
- Firefox
- Chrome
- WebKit
- AWS
- Ollama
- IndexedDB
tags:
- web-development
- browser-storage
- sqlite
- webassembly
- offline-mode
---

### TL;DR
Hacker News thread on Notion’s engineering post about speeding up the browser app with WASM SQLite, where the top comment simply punts readers to an earlier HN discussion and the broader thread debates whether browser SQLite/OPFS is production-ready, what browser APIs are missing, and whether Notion should instead expose real offline mode.

### Key Quote
"There's a multiple readers and writers proposal [0]."

### Summary
- **Source article discussed:** Notion’s blog post, **“How we sped up Notion in the browser with WASM SQLite”**.
- **Thread metadata:** HN item **40949489**, by **jFriedensreich**, **253 points**, **103 comments**, **22 top-level comments captured**.
- **Top comment (verbatim):** "Article title: How we sped up Notion in the browser with WASM SQLite Discussion (19 points, yesterday) https://news.ycombinator.com/item?id=40931957 (https://news.ycombinator.com/item?id=40931957)"
- **Top commenter:** `u/gnabgib`
- **Thread topics:**
  - whether the Notion post is evidence that **WASM SQLite is ready for production**
  - **OPFS / SharedWorker / concurrency** limitations in browser storage APIs
  - the long-running debate over **WebSQL vs IndexedDB vs browser-native SQLite**
  - why Notion still lacks a clear **offline mode** despite local SQL caching
  - performance and architecture tradeoffs of pushing database work into the client

- **Main thread reaction:** the HN comments are less about Notion itself and more about the implications of Notion’s approach for web app architecture.
- **Notion/WASM SQLite takeaway in the thread:**
  - Several commenters read the article as proof that **SQLite in WASM can work at scale**, but only with substantial engineering around persistence and browser quirks.
  - `u/jFriedensreich` says their own experience suggests Notion’s approach is “pretty much required” for production use, but also notes the stack still has “a LOT of ugly parts”:
    - tooling, support, and debugging for **OPFS**
    - practical reliance on **a single worker using sync APIs**
    - lack of a straightforward npm package that provides the full needed layer
- **Browser-platform debates:**
  - `u/nafey` argues it was a missed opportunity not to bundle SQLite into major browsers.
  - Replies point out this is essentially the old **WebSQL** debate:
    - `u/compressedgas` notes WebSQL already existed and was removed in favor of IndexedDB.
    - `u/simonw` argues browser-vendored SQLite would freeze everyone on an old SQLite version, whereas **SQLite compiled to WASM** avoids that problem.
  - `u/AlexErrant` highlights the **multiple readers and writers** proposal for OPFS, noting:
    - Firefox has a positive position
    - Chrome has implemented it
    - WebKit has ignored it
- **Concurrency / file-system API frustration:**
  - Multiple comments complain that the web has **too many partial filesystem abstractions** and none that feel like “real files.”
  - One branch argues browsers should just expose files more directly; others respond that sandboxing and OS differences make that hard.
- **Offline mode criticism:**
  - `u/slightwinder` complains that Notion has an actual SQL database on the client “as cache” but still no offline mode.
  - A reply from `u/jitl` says the WASM SQLite path is only an **optional cache** and Notion still works as before where the required browser APIs are missing; their mobile/native apps already use SQLite on a native thread.
- **Performance / local-first enthusiasm:**
  - `u/bearjaws` argues local SQLite is powerful because modern SSDs can scan **30–100 MiB** databases in milliseconds, and claims cloud IOPS can be absurdly expensive by comparison.
  - That comment leads into a long side discussion comparing **SQLite vs DuckDB**, browser SIMD, and whether browser-side databases can meaningfully replace server-side workloads.
- **IndexedDB comparison:**
  - A recurring theme is that IndexedDB is seen as:
    - awkward and verbose
    - slow or inconsistent across browsers
    - hard to debug
    - not a real SQL experience
  - One commenter says it is “the worst of both” because it is both async and still can block or behave badly depending on implementation.
- **Notion product criticism:**
  - Some comments drift into complaints that Notion remains sluggish in mobile/table views and that the company has prioritized AI and feature growth over UX polish.
  - Others note that Notion’s value may be more social/product-led than technically innovative.

### Assessment
This is a **mixed** content type: primarily a **social thread** reacting to a Notion engineering article, with some direct technical commentary from participants. Durability is **medium**: the specific Notion post and browser API references will age, but the underlying debates about SQLite in WASM, OPFS concurrency, and IndexedDB pain are fairly durable. Density is **medium-high** because the thread contains concrete implementation claims, browser API details, and real-world examples, but also a lot of digressive argument. Originality is mostly **commentary**, not primary research, though it includes one notable direct comment from a Notion-related participant about production constraints. Reference style is **skim-once to refer-back**: useful for remembering the exact debate and the cited browser API issues, not something that requires deep study unless you are building browser persistence. Scrape quality is **partial**: the thread metadata and many comment excerpts are captured, but the underlying Notion article itself is not included, and the comment set is noisy and repetitive; still, the capture is good enough to identify the discussion and its major fault lines.
