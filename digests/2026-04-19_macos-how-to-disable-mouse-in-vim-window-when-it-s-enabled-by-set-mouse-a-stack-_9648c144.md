---
url: https://stackoverflow.com/questions/43048243/how-to-disable-mouse-in-vim-window-when-its-enabled-by-set-mouse-a
title: macos - How to disable mouse in vim window when it's enabled by "set mouse = a"? - Stack Overflow
scraped_at: '2026-04-19T08:05:51Z'
word_count: 59
raw_file: raw/2026-04-19_macos-how-to-disable-mouse-in-vim-window-when-it-s-enabled-by-set-mouse-a-stack-_9648c144.txt
tldr: A Stack Overflow question asks how to temporarily disable Vim’s mouse support in macOS Terminal after enabling `set mouse=a`, because `set mouse=c` did not stop the mouse from affecting Vim while trying to select/copy text in the terminal.
key_quote: I'm using vim and I've set mouse=a in my .vimrc, so upon startup, vim supports mouse cursor. But some times I need to copy text from terminal, so I need to shut down mouse support in vim.
durability: low
content_type: mixed
density: low
originality: primary
reference_style: skim-once
scrape_quality: partial
people: []
tools:
- vim
- macOS Terminal
libraries: []
companies: []
tags:
- vim
- macos-terminal
- mouse-support
- terminal-usage
---

### TL;DR
A Stack Overflow question asks how to temporarily disable Vim’s mouse support in macOS Terminal after enabling `set mouse=a`, because `set mouse=c` did not stop the mouse from affecting Vim while trying to select/copy text in the terminal.

### Key Quote
“I'm using vim and I've set mouse=a in my .vimrc, so upon startup, vim supports mouse cursor. But some times I need to copy text from terminal, so I need to shut down mouse support in vim.”

### Summary
- This is a **question**, not an answer: the user wants a way to **disable mouse interaction in Vim** when mouse support has been enabled globally via `.vimrc`.
- The setup described:
  - Vim is configured with `set mouse=a`
  - Vim is running inside the **macOS Terminal**
  - The user sometimes wants to **use the mouse to select/copy text from the terminal**
- The problem:
  - The user tried `set mouse=c`
  - That did **not** appear to disable the mouse behavior in the terminal session
- Core ask:
  - Is there a way to **toggle off mouse support in Vim temporarily** without removing the global `.vimrc` setting?
- This is a practical Vim/macOS terminal behavior issue, likely about how Vim mouse modes interact with terminal selection/copying.

### Assessment
This is a **low-durability** technical support question because it depends on Vim behavior and terminal interaction on macOS, which can vary by version and environment. The content type is **question / tutorial-seeking** rather than a solution or explanation. It is **low-density**: only a brief problem statement with no code beyond the settings `set mouse=a` and `set mouse=c`. The source is a **primary source** in the sense that it’s the original user report, not a synthesis. It’s best used as a **skim-once** reference to identify the exact issue being searched for. **Scrape quality is partial**: only the question text is present, and the answer section is missing, so the full resolution is not included.
