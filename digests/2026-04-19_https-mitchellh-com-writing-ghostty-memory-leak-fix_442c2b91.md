---
url: https://mitchellh.com/writing/ghostty-memory-leak-fix
title: https://mitchellh.com/writing/ghostty-memory-leak-fix
scraped_at: '2026-04-19T21:20:26Z'
word_count: 1388
raw_file: raw/2026-04-19_https-mitchellh-com-writing-ghostty-memory-leak-fix_442c2b91.txt
tldr: Mitchell Hashimoto explains how Ghostty’s largest memory leak came from reusing oversized scrollback pages as if they were standard-sized, causing `munmap` to be skipped, and says the fix is merged for tip/nightly and will ship in Ghostty 1.3.
key_quote: “Eventually, we'd free the page under various circumstances ... and we would never call `munmap` on it.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mitchell Hashimoto
- '@grishy'
- Claude Code
- Mach
tools:
- Ghostty
- Claude Code
- Valgrind
- macOS Instruments
- mmap
- munmap
libraries:
- Zig
companies: []
tags:
- memory-management
- debugging
- terminal-emulators
- memory-leaks
- software-engineering
---

### TL;DR
Mitchell Hashimoto explains how Ghostty’s largest memory leak came from reusing oversized scrollback pages as if they were standard-sized, causing `munmap` to be skipped, and says the fix is merged for tip/nightly and will ship in Ghostty 1.3.

### Key Quote
“Eventually, we'd free the page under various circumstances ... and we would never call `munmap` on it.”

### Summary
- **What happened**
  - Ghostty users reported absurd memory growth, including one case of **37 GB after 10 days**.
  - The leak existed since at least **Ghostty 1.0**, but only recently began showing up at scale because **CLI workloads like Claude Code** started triggering the right conditions.
  - The fix is already **merged**, available in **tip/nightly**, and slated for the **1.3 release in March**.

- **How Ghostty stores terminal content**
  - Ghostty uses a **PageList**, a doubly-linked list of memory pages holding terminal content such as:
    - characters
    - styles
    - hyperlinks
  - Pages are allocated with **`mmap`**.
  - To avoid expensive repeated syscalls, Ghostty uses a **memory pool** for standard-sized pages.
  - If terminal content is unusually large or complex, Ghostty allocates a **non-standard page** directly via `mmap`, bypassing the pool.
  - Normal cleanup logic:
    - pages **<= standard size** → returned to the pool
    - pages **> standard size** → freed with **`munmap`**

- **The scrollback optimization that caused the bug**
  - Ghostty has a **scrollback limit** and prunes old pages when history gets too large.
  - To keep this fast in hot paths, Ghostty reuses the **oldest page as the newest page** instead of allocating and freeing repeatedly.
  - This optimization is normally fast and beneficial, because it avoids allocations and only does pointer/metadata work.

- **The actual bug**
  - During scrollback pruning, Ghostty would **resize metadata back to standard size** but **not resize the underlying allocation**.
  - That meant a page that was still backed by a **large non-standard `mmap` allocation** was now treated as if it were standard-sized.
  - Later, when the page was freed, Ghostty assumed it belonged to the pool and **never called `munmap`**, so the memory leaked.
  - The leak was especially severe because:
    - **Claude Code** produced many **multi-codepoint grapheme** outputs, forcing frequent non-standard pages.
    - It also used the **primary screen** and produced lots of **scrollback output**.
  - Mitchell explicitly says **Claude Code was not at fault**; it just exposed an existing bug.

- **The fix**
  - The chosen fix is simple: **never reuse non-standard pages**.
  - If pruning encounters a non-standard page:
    - destroy it properly with `munmap`
    - allocate a fresh standard-sized page from the pool
  - The key code path shown:
    - `if (first.data.memory.len > std_size) { self.destroyNode(first); break :prune; }`
  - Mitchell notes a more complex strategy could track non-standard-page usage over time, but the team prefers the current assumption that **standard pages are the common case**.

- **How the leak was diagnosed**
  - Mitchell added support for **virtual memory tags on macOS** via the Mach kernel.
  - This allowed PageList allocations to be tagged with a specific identifier and tracked in tooling.
  - On macOS, the tagged memory made it easy to:
    - isolate the leak
    - confirm PageList was the culprit
    - verify the fix by checking that the tagged memory was freed correctly

- **Preventing future leaks**
  - Ghostty already uses several leak-detection practices:
    - **Zig leak-detecting allocators** in debug builds and unit tests
    - **Valgrind** in CI across the unit test suite
    - **macOS Instruments** for GUI leak checks in Swift
    - **Valgrind** on GTK-related PRs
  - This leak escaped detection because it required a very specific runtime pattern that tests didn’t reproduce.
  - The merged PR includes a **new test** that reproduces the bug to prevent regressions.

- **Conclusion / broader takeaway**
  - This was Ghostty’s **largest known memory leak** and the only one confirmed by multiple users.
  - The post emphasizes that **reproduction is essential** for diagnosing memory leaks.
  - Mitchell thanks **@grishy** for providing a reliable reproduction and thanks the community for diagnostics and analysis.

### Assessment
This is a **mixed technical / debugging post** with high relevance for readers interested in terminal emulators, memory management, or real-world leak hunting. **Durability is medium**: the general debugging lessons, allocator design, and leak-analysis techniques are long-lived, but the specifics are tied to Ghostty’s implementation and the upcoming **1.3** release. The content is **high density** and **primary source**—it’s authored by Mitchell Hashimoto and includes the actual fix rationale plus code. It works best as a **refer-back** reference if you’re investigating Ghostty internals or memory leaks. **Scrape quality is good**: the main narrative, code snippet, and key details are present, though formatting is somewhat flattened and the footnotes/images (if any) are not included.
