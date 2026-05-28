---
url: https://news.ycombinator.com/item?id=47317616
title: Two Years of Emacs Solo | Hacker News
scraped_at: '2026-04-19T21:40:44Z'
word_count: 6211
raw_file: raw/2026-04-19_two-years-of-emacs-solo-hacker-news_a2e6f62b.txt
tldr: A sprawling Hacker News discussion around “Two Years of Emacs Solo” centers on the idea that celadevra_ praises an Emacs setup that avoids external packages and backup-file clutter, argues it’s a sane and maintainable way to own your editor, while many commenters debate defaults, package management, GUI usability, Elisp, and whether Emacs is best understood as a hackable environment rather than just a text editor.
key_quote: That means the code is sketchy sometimes, sure, but it's in my control. I wrote it, I understand it, and when it breaks, I know exactly where to look.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people:
- celadevra_
- Rahul
- Claude
tools:
- emacs
- emacs-nox
- tramp
- which-key
- doom-emacs
- gptel
- eglot
- lsp-mode
- xref
- wgrep
- magit
libraries:
- diff-hl
- ace-window
- olivetti
- doom-modeline
- exec-path-from-shell
- eldoc-box
- rainbow-delimiters
- sudo-edit
companies:
- GNU
- ELPA
- NonGNU ELPA
- Ubuntu
- Debian
- Codeberg
tags:
- emacs
- editor-customization
- lisp
- package-management
- gui-vs-keyboard
---

### TL;DR
A sprawling Hacker News discussion around **“Two Years of Emacs Solo”** centers on the idea that **celadevra_** praises an Emacs setup that avoids external packages and backup-file clutter, argues it’s a sane and maintainable way to own your editor, while many commenters debate defaults, package management, GUI usability, Elisp, and whether Emacs is best understood as a hackable environment rather than just a text editor.

### Key Quote
> “That means the code is sketchy sometimes, sure, but it's in my control. I wrote it, I understand it, and when it breaks, I know exactly where to look.”

### Summary
- **Top comment (verbatim):** “> — Sensible file handling: backups and auto-saves in a cache/ directory, recentf for recent files, clean buffer naming with uniquify”
- **Top commenter:** `celadevra_`
- **Thread topics:**
  - Emacs backup/autosave defaults and whether they’re “bad” or just configurable
  - Emacs Solo’s “no external packages” philosophy and hand-rolled Elisp
  - Emacs in containers/VMs via `emacs-nox` and TRAMP
  - GUI discoverability vs keyboard-driven workflows in Emacs/Vim
  - Whether Emacs’ design makes it especially good for LLM-assisted workflows

- The thread is about a blog post describing **two years of running Emacs “solo”**:
  - The author prefers a **self-contained Emacs configuration** with no external packages, or at least minimal reliance on them.
  - They emphasize **controlling the whole stack**: if something breaks, they know where to look.
  - A major practical theme is **file hygiene**:
    - backups/autosaves are moved out of working directories
    - recent file tracking is used
    - buffers are given cleaner names with `uniquify`
  - The author’s stance is that Emacs is already strong out of the box, and that a small amount of carefully written Elisp can cover many common needs.

- A big portion of the thread is a **debate over defaults**:
  - Some users find Emacs’ default backup behavior annoying, especially in places like `/etc/nginx/sites-enabled/`, where backup files can be problematic.
  - Others point out:
    - `foo~` is Emacs’ default backup style, not `~foo`
    - editing symlink-managed config directories is often the real mistake
    - centralizing backups is a common and sensible customization
  - There’s broad agreement that Emacs’ defaults can be improved for some workflows, but disagreement about whether changing them globally would break long-established user expectations.

- Many comments focus on **self-sufficiency vs package ecosystems**:
  - Some users say building your own small tools helps you truly understand the system.
  - Others argue that **reading existing packages** is just as important as writing your own, and that relying on open-source packages is normal and productive.
  - The post itself notes that Emacs Solo was **influenced by many packages** even though it does not install them directly:
    - `diff-hl`
    - `ace-window`
    - `olivetti`
    - `doom-modeline`
    - `exec-path-from-shell`
    - `eldoc-box`
    - `rainbow-delimiters`
    - `sudo-edit`
    - and others

- The thread also turns into a discussion of **Emacs package infrastructure and stability**:
  - Some commenters describe freezing package versions alongside Emacs releases to keep configurations reproducible.
  - Another reply clarifies the distinction between:
    - **GNU ELPA**: tied to the FSF copyright assignment process
    - **NonGNU ELPA**: does not have that assignment restriction
  - There’s skepticism about dependency churn, mirrors failing, and maintenance overhead in large Emacs configs.

- A substantial side discussion is about **using Emacs in terminals, containers, and VMs**:
  - `emacs-nox` is praised as a good out-of-the-box editor in constrained environments.
  - TRAMP is recommended for editing local and remote files, including with `sudo`.
  - Users mention trying to reduce friction around backups, locks, and accidental commit of lock files like `.#filename.txt`.

- The thread contains a recurring **GUI vs keyboard** argument:
  - Some users say they want a GUI that behaves like Emacs/Vim power-user setups.
  - Others argue that Emacs is already a GUI app, and its discoverability can be improved with tools like:
    - `which-key`
    - command palettes via `M-x`
    - menus and context menus
  - The counterpoint is that Emacs’ power comes from **dense keybinding-based interaction**, and turning that into a conventional GUI would dilute what makes it effective.
  - Several people note that using the mouse is still possible, but the ecosystem is more optimized for keyboard-first workflows.

- There’s also a long reflection on **why Emacs is Lisp-based**:
  - Commenters explain that Emacs is less about “text editing features” and more about being a **dynamic, inspectable, extensible environment**.
  - Lisp is defended as a practical fit for:
    - incremental evaluation
    - code-as-data
    - runtime customization
    - “everything is a buffer” style architecture
  - A few comments contrast Emacs Lisp with Common Lisp and argue that Elisp is more practical today for editor scripting, even if CL is more powerful in some respects.

- The author later appears in the thread, thanking people and noting:
  - the post reached **#1** for a few hours
  - the server struggled under the traffic
  - they appreciate the responses, even if they can’t reply to all of them

- The thread also surfaces **practical Emacs snippets and tools**:
  - a custom Elisp function to export `xref` results into a grep-like buffer so `wgrep` can edit them
  - mention of `eglot` vs `lsp-mode` for C++
  - `gptel` and LLM tooling inside Emacs
  - the idea that LLMs may be especially useful for generating Elisp and navigating Emacs’ documentation

- Overall, the conversation splits into a few broad camps:
  - **Admiration**: Emacs Solo is beautiful, disciplined, and inspiring
  - **Pragmatism**: it’s good, but too much work for many users
  - **Customization advocates**: Emacs is at its best when you own your config
  - **Skeptics/GUI users**: keyboard-heavy, deeply customized workflows are impressive but not broadly ergonomic

### Assessment
This is a **mixed-content Hacker News discussion thread** with high density and good long-term value for anyone interested in Emacs, editor philosophy, or highly customized workflows. Durability is **medium to high**: the social arguments are timeless, but specific details about Emacs releases, ELPA, `emacs-nox`, `eglot`, `xref`, and current LLM tooling will age. The content is mostly **commentary/opinion** with some embedded technical guidance and a few concrete code/config snippets; originality is **mixed** because it includes the author’s participation plus many reactions and side discussions. It’s best used as a **refer-back** or **deep-study** reference if you care about Emacs customization, package policy, or editor philosophy. Scrape quality is **good** overall: the thread text is rich and includes many comments, though it lacks full page structure, timestamps, and any non-text context from the original HN page.
