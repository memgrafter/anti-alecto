---
url: https://github.com/ghostty-org/ghostty
title: 'ghostty-org/ghostty: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.'
scraped_at: '2026-04-12T07:31:25Z'
word_count: 1456
raw_file: raw/2026-04-12_ghostty-org-ghostty-ghostty-is-a-fast-feature-rich-and-cross-platform-terminal-e_6cec087e.txt
tldr: Ghostty is a cross-platform, GPU-accelerated terminal emulator that emphasizes native UI, strong standards compliance, and an embeddable terminal library (`libghostty`).
key_quote: Ghostty differentiates itself by being fast, feature-rich, and native. While there are many excellent terminal emulators available, they all force you to choose between speed, features, or native UIs. Ghostty provides all three.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mitchell Hashimoto
tools:
- Ghostty
- GitHub
- Sentry CLI
libraries:
- libghostty
- libghostty-vt
companies:
- Ghostty
- Sentry
tags:
- terminal-emulator
- cross-platform
- gpu-acceleration
- native-ui
- embeddable-library
---

### TL;DR
Ghostty is a cross-platform, GPU-accelerated terminal emulator that emphasizes native UI, strong standards compliance, and an embeddable terminal library (`libghostty`).

### Key Quote
“Ghostty differentiates itself by being fast, feature-rich, and native. While there are many excellent terminal emulators available, they all force you to choose between speed, features, or native UIs. Ghostty provides all three.”

### Summary
- **What it is**
  - Ghostty is a terminal emulator project with a main app plus a reusable core/library called **`libghostty`**.
  - It is presented as **fast, feature-rich, and cross-platform**, with **platform-native UI** and **GPU acceleration**.
  - The repository README links to **Download**, **Documentation**, **Contributing**, and **Developing** pages.

- **Core claims about Ghostty**
  - Ghostty aims to avoid the usual tradeoff between **speed**, **features**, and **native UI**.
  - It claims to be:
    - **standards-compliant** for common terminal control sequences
    - **competitive in performance** with the fastest terminals
    - rich in **windowing features**
    - highly **native** on each platform
    - a foundation for an embeddable terminal via **`libghostty`**

- **Standards-compliant terminal emulation**
  - Ghostty says it implements all regularly used control sequences and can run mainstream terminal programs without issue.
  - For legacy behavior, it references a **comprehensive xterm audit** and conformance test cases.
  - It also supports many modern features, including:
    - **Kitty graphics protocol**
    - **Kitty image protocol**
    - **clipboard sequences**
    - **synchronized rendering**
    - **light/dark mode notifications**
  - The project defines “standard” as:
    1. standards, if available
    2. xterm, if the feature exists
    3. other popular terminals

- **Performance**
  - Ghostty claims to be in the same performance class as other top terminal emulators.
  - The README says it is usually within a few percentage points of **Alacritty** on benchmarks, while being much faster than traditional terminals like **Terminal.app** and **iTerm**.
  - Performance is attributed to:
    - a **multi-threaded architecture**
    - dedicated **read**, **write**, and **render** threads per terminal
    - **OpenGL** rendering on Linux
    - **Metal** rendering on macOS
    - a heavily optimized parser using **CPU-specific SIMD instructions**

- **Windowing and UI**
  - The Mac and Linux GTK apps support:
    - **multi-window**
    - **tabbing**
    - **splits**
    - tab renaming and coloring
  - The project emphasizes that it does not aim for a lowest-common-denominator cross-platform experience.

- **Native platform experiences**
  - **macOS**
    - built as a **SwiftUI-based** application
    - includes real windowing, menu bars, and a settings GUI
    - uses **Metal** and **CoreText**
    - supports **AppleScript** and **Apple Shortcuts (AppIntents)**
  - **Linux**
    - built with **GTK**
    - integrates with **systemd** for features like:
      - always-on behavior
      - new windows in a single instance
      - cgroup isolation
  - The project’s goal is for Ghostty to feel built “for the platform first.”

- **`libghostty` embeddable terminal library**
  - Ghostty also serves as a **C-compatible library** for embedding terminal functionality in third-party apps.
  - It is described as **cross-platform** and **zero-dependency** in **C and Zig**.
  - The library is being split into smaller pieces, starting with **`libghostty-vt`**, focused on terminal sequence parsing and state.
  - `libghostty-vt` is described as:
    - available today for **Zig and C**
    - compatible with **macOS, Linux, Windows, and WebAssembly**
    - **extremely stable** in functionality
    - but with **API signatures still in flux**
  - The README points to:
    - the `example` directory for small C/Zig examples
    - **Ghostling** as a complete example project
    - **awesome-libghostty** for related projects/resources
    - a **Doxygen** site for C API docs

- **Future direction**
  - The project is considering **Ghostty-only terminal control sequences**.
  - It says the team has not implemented these yet, partly because they want to avoid fragmenting the terminal ecosystem.
  - The idea is to push terminal capabilities forward if standards remain stagnant.

- **Crash reports**
  - Ghostty includes a built-in crash reporter that saves reports locally to:
    - `$XDG_STATE_HOME/ghostty/crash`
    - or `~/.local/state` if `XDG_STATE_HOME` is unset
  - Crash reports are **not automatically sent off the machine**.
  - Reports are generated the **next time Ghostty starts after a crash**.
  - Users can list reports with:
    - `ghostty +crash-report`
  - Reports use:
    - the **`.ghosttycrash`** extension
    - **Sentry envelope format**
  - To send a report to the Ghostty project, the README gives a `sentry-cli send-envelope --raw <path to ghostty crash>` command using a provided DSN.
  - Warning: crash reports may contain **sensitive information** because they include the full stack memory of each thread at crash time.

### Assessment
This is a high-value repository README with **high durability** for the broad concepts it covers, but **medium durability** for version-specific claims, roadmap status, and implementation details like `libghostty-vt`, platform integrations, and crash-reporting behavior. The content type is **mixed**: it functions as both a project overview/reference and a promotional announcement-style README, with many claims that are self-asserted rather than independently verified. The document is **high-density** and quite specific, especially around architecture, supported protocols, platform features, and crash-report handling. Its originality is best described as **primary source** for the project’s own positioning and design claims. It is most useful as a **refer-back** reference rather than a one-time skim, especially if you want to confirm what Ghostty claims to support or to find exact details like `ghostty +crash-report`, `.ghosttycrash`, or the Sentry envelope format. Scrape quality appears **good** for the README content provided; this capture includes the major sections and no obvious code blocks or sections appear missing, though it is still a README rather than the full linked docs.
