---
url: https://news.ycombinator.com/item?id=47172664
title: Smartphone market forecast to decline this year due to memory shortage | Hacker News
scraped_at: '2026-04-19T21:58:10Z'
word_count: 14811
raw_file: raw/2026-04-19_smartphone-market-forecast-to-decline-this-year-due-to-memory-shortage-hacker-ne_99c55b14.txt
tldr: Hacker News thread on a report that smartphone market growth will decline because of DRAM/memory shortages, with the opening commenter arguing that device and app bloat—not hardware limits alone—are making modern phones, Safari tabs, and desktop-style web apps feel worse despite much faster chips.
key_quote: “Everything sucks and is way less fun than it used to be.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: skim-once
scrape_quality: partial
people: []
tools:
- Safari
- Electron
- Outlook
- YouTube
- Firefox
- Qt
- GTK
- Win32
- React
- Claude
- GrapheneOS
- LineageOS
- SmartTube
- yt-dlp
- ImGUI
- LibreWolf
- Waterfox
- Chromium
- uBlock Origin
libraries:
- Java
- Python
- JSX
companies:
- Apple
- Google
- Microsoft
- OpenAI
- Nintendo
- Samsung
- Xiaomi
- Anker
- Meta
- Qualcomm
- AYN
- Qt
- GNOME
- SAP
tags:
- smartphone-market
- memory-shortage
- software-bloat
- mobile-ux
- web-apps
---

### TL;DR
Hacker News thread on a report that smartphone market growth will decline because of DRAM/memory shortages, with the opening commenter arguing that device and app bloat—not hardware limits alone—are making modern phones, Safari tabs, and desktop-style web apps feel worse despite much faster chips.

### Key Quote
“Everything sucks and is way less fun than it used to be.”

### Summary
- **What the thread is about**
  - The discussion starts from a news item/headline: **“Smartphone market forecast to decline this year due to memory shortage”**.
  - The thread quickly broadens into a long argument about:
    - smartphone RAM/storage constraints
    - aggressive background process killing on iOS/Android
    - app and web bloat
    - whether browsers/Electron/web apps are the wrong platform for software
    - whether AI/datacenter demand is distorting the memory market
    - whether lower-end devices and consoles will be affected

- **Opening comment / top comment**
  - **Top comment (verbatim):** “Somehow, with 12GB of RAM, I can't get my iPhone 17 Pro to keep more than a few safari tabs open without having them refresh when I come back from an app or two, and it makes me want to throw my phone across the train (Where the internet often cuts out!).”
  - **Top commenter:** not available in the provided scrape
  - This opening complaint sets the tone: even with a high-end phone, the user experiences tab eviction, refreshes, and poor state retention.

- **Thread topics**
  - **Smartphone RAM and background-state loss**
    - Safari tabs reloading after app switching.
    - Photos, YouTube, Facebook, and other apps losing state.
    - iOS background-kill behavior versus Android/OEM “battery optimization.”
    - Whether phones should ask users what to kill instead of silently dropping apps.

  - **Memory shortage / DRAM pricing**
    - Some commenters treat the headline as a real industry constraint.
    - Others argue the shortage is not “natural” but driven by AI/datacenter demand, especially HBM and large-capacity server memory.
    - There’s disagreement over whether this is a temporary cycle or a structural shift that will keep low-end devices uneconomical.
    - One cited claim in the thread: memory prices may stabilize by mid-2027 but not return to prior levels, which would permanently pressure sub-$100 devices.

  - **App and OS bloat**
    - Repeated complaints that modern software squanders hardware gains.
    - Examples mentioned:
      - Windows 11/Outlook feeling sluggish on modern hardware
      - giant app updates from vendors like Xiaomi and Anker
      - iOS “Liquid Glass” and other UI-heavy layers
      - YouTube background behavior, smart downloads, and queue/state loss
    - Several commenters say performance problems are increasingly due to software choices, not insufficient silicon.

  - **Web apps, Electron, and “the browser as platform”**
    - A major sub-thread debates whether browsers are the right architecture for software.
    - One side says the web “won” because it’s easy to deploy and cross-platform.
    - Another side argues that web/Electron have created huge complexity, dependency sprawl, and poor UX.
    - There’s a recurring contrast between:
      - native GUI toolkits
      - browser-based apps
      - cross-platform frameworks
      - the difficulty of building software that feels native on each OS

  - **Platform tradeoffs and native UX**
    - Some commenters argue cross-platform software inevitably becomes mediocre because users on different platforms have different expectations.
    - Others say native toolkits also have serious portability and quality issues.
    - Gtk, Qt, Win32, Electron, and Java are all mentioned as examples in the broader debate.

  - **iOS-specific complaints**
    - Safari tab eviction and state loss
    - aggressive app suspension
    - lack of swap on iPhones
    - limited background execution
    - storage capacity complaints, especially 128 GB models
    - difficulty multitasking between Safari and other apps
    - frustration that even “system” apps don’t restore state reliably

  - **Android / Chinese phone / OEM behavior**
    - Some users contrast iPhone behavior with Android devices:
      - some say Android handles memory better on their hardware
      - others note Chinese phones often kill background apps aggressively
      - custom ROMs and ZRAM tuning are mentioned as ways to improve behavior
    - One commenter says a 6 GB Android phone can still feel fine if configured well.

  - **Game consoles and similar devices**
    - The thread speculates about whether a hypothetical **Switch 2 Lite** or similar cost-reduced device would be impacted by memory pricing.
    - Some note that Nintendo may be unable to reduce RAM after the fact because existing software expectations would break.
    - The broader point: memory-intensive consumer devices may become less attractive if DRAM stays expensive.

  - **AI as a driver of hardware scarcity**
    - A large part of the thread is skeptical of AI’s impact on the market.
    - Some commenters accuse OpenAI/AI infrastructure demand of consuming memory supply and crowding out consumer devices.
    - Others are more cautious, saying this may just be normal market behavior amplified by high demand.
    - There are also claims that AI hype is causing overinvestment, delayed consumer hardware, and secondary-market price spikes.

  - **Older phone nostalgia / hardware stagnation**
    - Multiple comments say older phones felt smoother, more predictable, or more enjoyable.
    - Some prefer hardware stagnation if it leads to better software and more robust devices.
    - Others welcome stagnation because it might finally force software teams to optimize.

- **Main opinion clusters**
  - **“Software got bloated; hardware gains were squandered.”**
    - This is the dominant sentiment in the thread.
    - Modern phones and apps are seen as resource-hungry, state-hostile, and too eager to refresh/reset.
  - **“The web won because deployment mattered more than elegance.”**
    - This cluster accepts browser-based apps as a pragmatic compromise.
    - It often argues the problem is implementation quality, not the web itself.
  - **“Cross-platform is the wrong goal.”**
    - A more purist camp argues good apps must be adapted to each OS, not flattened into one shared UI.
  - **“Memory shortage may actually force discipline.”**
    - A smaller but recurring view: constrained RAM could improve software quality by removing the option to brute-force problems with more hardware.
  - **“AI/datacenter demand is warping the market.”**
    - This is the thread’s most speculative angle.
    - Some think the shortage is artificial or at least magnified by AI capex; others think it’s simply the new reality.

- **What’s concrete and useful here**
  - The thread is less a clean analysis of the article and more a **mood board for modern software frustration**.
  - If you want:
    - **a sense of HN sentiment** about phone bloat, browser apps, or DRAM shortages: this is relevant.
    - **a disciplined summary of the original news item**: the thread is noisy and heavily digressive.
  - Specific recurring factual anchors in the discussion:
    - 12 GB iPhone/Safari tab reload complaints
    - Android/iOS background-kill behavior
    - concern about low-end phone viability under higher DRAM prices
    - speculation that AI demand is driving or distorting memory supply

### Assessment
This is a **mixed** HN social thread with lots of commentary, anecdote, and speculation layered on top of a real news hook. **Durability: medium** — the specific market forecast and DRAM pricing claims will age quickly, but the broader themes about software bloat, state loss, and cross-platform UI tradeoffs are evergreen. **Content type: mixed**. **Density: high** in the sense that there are many concrete examples, but the signal is diluted by repetition and tangents. **Originality: commentary/synthesis**, not a primary source; the thread mostly reacts to the headline and each other. **Reference style: skim-once to refer-back** — useful for recalling the range of arguments and the emotional tenor, less useful as a clean factual source. **Scrape quality: partial** — this is clearly a comment-thread scrape; the article text itself is absent, and the metadata for the opening/top comment author is missing, so attribution is incomplete even though the text of the opening comment is present.
