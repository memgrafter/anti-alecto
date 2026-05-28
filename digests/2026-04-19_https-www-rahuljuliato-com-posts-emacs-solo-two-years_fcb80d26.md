---
url: https://www.rahuljuliato.com/posts/emacs-solo-two-years
title: https://www.rahuljuliato.com/posts/emacs-solo-two-years
scraped_at: '2026-04-19T21:17:00Z'
word_count: 4023
raw_file: raw/2026-04-19_https-www-rahuljuliato-com-posts-emacs-solo-two-years_fcb80d26.txt
tldr: 'A two-year retrospective on Emacs Solo: the author refactored their no-external-packages Emacs config into a core `init.el` plus 35 self-written `lisp/` modules, and argues Emacs built-ins now cover far more than most users expect.'
key_quote: 'Emacs Solo started as a personal challenge: can I have a productive, modern Emacs setup without installing a single external package?'
durability: high
content_type: mixed
density: high
originality: primary
reference_style: deep-study
scrape_quality: good
people:
- Eli Zaretskii
- Yuan Fu
- Stéphane Marks
- João Távora
- David Wilson
- Prot
- Gopar
tools:
- Emacs
- Eglot
- ERC
- Gnus
- Icomplete
- Dired
- Eshell
- vc
- tab-bar-mode
- proced
- flymake
- flyspell
- Modus themes
- yt-dlp
- mpv
- Ollama
- Gemini
- Claude
- Docker
- Podman
- TRAMP
- cheat.sh
- gh
libraries: []
companies:
- GitHub
- GitLab
- MELPA
- ELPA
- Anthropic
- Google
- Open Source
tags:
- emacs
- elisp
- configuration
- package-free
- workflow
---

### TL;DR
A two-year retrospective on Emacs Solo: the author refactored their no-external-packages Emacs config into a core `init.el` plus 35 self-written `lisp/` modules, and argues Emacs built-ins now cover far more than most users expect.

### Key Quote
“Emacs Solo started as a personal challenge: can I have a productive, modern Emacs setup without installing a single external package?”

### Summary
- **What this post is**
  - A status report on **Emacs Solo** at its **two-year mark**
  - Focuses on a major refactor, a walkthrough of the built-in Emacs config, and a catalog of **35 self-contained extra modules**
  - The post is **text only**; screenshots and visual details live in the GitHub repo

- **Project rule**
  - Emacs Solo uses **no external packages**
  - Everything is either:
    - built into Emacs, or
    - written from scratch by the author in `lisp/`
  - Explicitly avoids `package-install`, `straight.el`, and `use-package :ensure t` targeting ELPA/MELPA

- **Why the author does this**
  - To learn what Emacs provides out of the box
  - To reduce breakage across releases
  - To avoid dependency/repository issues and upstream downtime
  - To keep full control over the config

- **Big architectural change: split into two layers**
  - **Layer 1: `init.el`**
    - Only configures **built-in Emacs packages/features**
    - Uses `use-package` with `:ensure nil`
    - Designed to be copy-paste friendly for other users
  - **Layer 2: `lisp/`**
    - Contains custom, standalone modules
    - Each module `provide`s/`require`s cleanly
    - Loaded from `init.el` with:
      - `(add-to-list 'load-path (expand-file-name "lisp" user-emacs-directory))`
      - `(require 'emacs-solo-themes)` etc.
    - Modules can be removed by commenting out `require` lines

- **Built-in Emacs config covered in `init.el`**
  - **General settings**
    - Keybindings like `M-o` for `other-window`, `M-j` for `duplicate-dwim`, `C-x ;` for `comment-line`, `C-x C-b` for `ibuffer`
    - New/coming Emacs 31 features: window layout commands, tree-sitter defaults, `delete-pair-push-mark`, `kill-region-dwim`, `ibuffer-human-readable-size`
    - File handling: backups/autosaves in `cache/`, `recentf`, `uniquify`
    - `C-z` disabled to avoid accidental terminal suspension
  - **Abbrev**
    - Custom placeholder-based abbrev expansion using markers like `###1###`, `###2###`, and `###@###`
  - **Auth-source**
    - Uses `~/.authinfo.gpg`
  - **Auto-revert**
    - Keeps buffers synced to on-disk changes
  - **Conf / compilation**
    - ANSI-colored compilation output
  - **Window / tab-bar**
    - Window tweaks and tab-based workspace management
  - **ERC / RCIRC**
    - IRC client setup, including logging, scroll behavior, match highlighting, and inline image support via an extra module
  - **Icomplete**
    - Uses built-in `icomplete-vertical-mode` instead of Vertico/Consult/Helm
    - Tuned with:
      - `(setq icomplete-delay-completions-threshold 0)`
      - `(setq icomplete-compute-delay 0)`
      - `(setq icomplete-show-matches-on-no-input t)`
      - `(setq icomplete-scroll t)`
    - Author says they’ve been upstreaming improvements to icomplete
  - **Dired / WDired**
    - Custom listing, openers (`open`, `xdg-open`), writable Dired editing
  - **Eshell**
    - Shared history across buffers
    - Toggleable prompt styles with `C-c t` and `C-c T`
    - History size of **100,000** with deduplication
  - **VC**
    - Strong emphasis on built-in version control workflow
    - Key commands include:
      - `C-x v D` / `C-x v =`
      - `C-c C-c`
      - `C-c C-e` for amend
      - `C-x v B` to browse remote repo in browser
      - `C-x C-g` to jump between modified/untracked files
    - Custom reflog viewer and current-hunk navigation
  - **Smerge / Diff / Ediff**
    - Merge and diff tools configured for sane window splits
  - **Eldoc / Eglot**
    - `eldoc-help-at-pt`, no event-buffer logging in Eglot
    - Custom LSP server programs including `rassumfrassum`
    - Keybindings under `C-c l`
  - **Flymake / Flyspell / Whitespace**
    - Diagnostics, spell checking, whitespace visibility
  - **Gnus / Man / Minibuffer / Newsticker / Org / Proced / Speedbar / Time / Webjump**
    - Various built-in tools configured for mail/news, docs, completion, feeds, process management, RSS, clocks, search, etc.
  - **Language modes**
    - Common Lisp with `inferior-lisp`
    - Tree-sitter and non-tree-sitter setups for Ruby, JS/TS, Bash, Rust, TOML, Markdown, YAML, Dockerfile, Go, etc.

- **The 35 self-contained extra modules**
  - These are small standalone reimplementations of features usually supplied by external packages
  - The author describes them as “hacky reimplementations” that are intentionally small and understandable
  - Notable modules include:
    - `emacs-solo-themes`
      - Theme variants: **Catppuccin Mocha**, **Crafters** (default), **Matrix**, **GITS**
      - Built on Modus themes
    - `emacs-solo-mode-line`
      - Minimal custom mode line
    - `emacs-solo-movements`
      - Navigation/window movement helpers
    - `emacs-solo-formatter`
      - Format-on-save registry keyed by file extension
    - `emacs-solo-transparency`
      - Frame transparency for GUI and terminal
    - `emacs-solo-exec-path-from-shell`
      - Shell PATH syncing in ~20 lines
    - `emacs-solo-rainbow-delimiters`
      - Delimiter coloring
    - `emacs-solo-project-select`
      - Project switching on top of `project.el`
    - `emacs-solo-viper-extensions`
      - Vim-like text objects for built-in Viper
    - `emacs-solo-highlight-keywords`
      - Highlights TODO/FIXME/HACK/NOTE comments
    - `emacs-solo-gutter`
      - Diff indicators in buffers
    - `emacs-solo-ace-window`
      - Window switching with labels
    - `emacs-solo-olivetti`
      - Centered writing mode
    - `emacs-solo-0x0`
      - Uploads text/files to 0x0.st
    - `emacs-solo-sudo-edit`
      - Reopen files as root via TRAMP `/sudo::`
    - `emacs-solo-replace-as-diff`
      - Multi-file search/replace with diff preview
    - `emacs-solo-weather`
      - Weather from wttr.in
    - `emacs-solo-rate`
      - Crypto/fiat exchange rates
    - `emacs-solo-how-in`
      - Cheat.sh answers inside Emacs
    - `emacs-solo-ai`
      - AI assistant integration for **Ollama**, **Gemini**, **Claude**
    - `emacs-solo-dired-gutter`
      - Git status markers in Dired
    - `emacs-solo-dired-mpv`
      - Audio playback from Dired using mpv
    - `emacs-solo-icons` + `-dired` / `-eshell` / `-ibuffer`
      - Icon registry and display helpers
    - `emacs-solo-container`
      - Docker/Podman management UI
    - `emacs-solo-m3u`
      - Playlist viewer / radio player
    - `emacs-solo-clipboard`
      - Clipboard integration for terminal Emacs
    - `emacs-solo-eldoc-box`
      - Eldoc in a child frame
    - `emacs-solo-khard`
      - Khard contacts browser
    - `emacs-solo-flymake-eslint`
      - ESLint Flymake backend
    - `emacs-solo-erc-image`
      - Inline images in ERC
    - `emacs-solo-yt`
      - YouTube search/playback via `yt-dlp` and mpv
    - `emacs-solo-gh`
      - GitHub CLI interface using transient menus

- **Emacs 31 angle**
  - Many sections are annotated with `; EMACS-31`
  - The author expects some custom/polyfill code to become unnecessary as these land in stable Emacs
  - Examples:
    - window layout commands
    - tree-sitter grammar sources
    - `markdown-ts-mode`
    - icomplete improvements
    - `speedbar-window`
    - VC enhancements
    - ERC fixes
    - `native-comp-async-on-battery-power`
    - `world-clock-sort-order`

- **Main takeaways**
  - Emacs is more capable out of the box than many users assume
  - Built-in tools like `vc`, `icomplete-vertical-mode`, `tab-bar-mode`, and `proced` are presented as genuinely useful, not fallback options
  - Writing custom packages taught the author a lot about Elisp internals like overlays, process filters, `tabulated-list-mode`, transient menus, and child frames
  - Small modules under 200 lines are preferred over feature-bloated replacements
  - The author also emphasizes contributing upstream when a workaround points to a real Emacs improvement

- **Conclusion / repository**
  - The author concludes that a modern, productive, package-free Emacs setup is possible
  - They invite readers to check the repository:
    - **https://github.com/LionyxML/emacs-solo**
  - The article’s purpose is both to document the setup and to share reusable ideas/snippets

### Assessment
This is a high-durability, mixed opinion/tutorial/reference post with very high specificity: it catalogs a real Emacs configuration, concrete keybindings, module names, feature flags, and Emacs 31-forward-looking notes, so it’s useful both as a reference and as a signal of what built-in Emacs can do without third-party packages. The content is primarily original work from the author rather than synthesis, though it is heavily informed by package ecosystems the modules emulate. Accuracy is likely strong within the author’s own setup, but readers should treat some claims as personal workflow judgments rather than universal benchmarks. Scope is broad but coherent: it covers the refactor, the built-in core, the 35 modules, and lessons learned. The scrape quality is good: the post appears fully captured in text form, and the omission of screenshots is intentional rather than a missing-data problem.
