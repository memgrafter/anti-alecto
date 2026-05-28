---
url: https://www.reddit.com/r/linuxmemes/comments/tszfjf/does_anyone_even_use_dash/
title: 'does anyone even use dash? : linuxmemes'
scraped_at: '2026-04-19T21:33:09Z'
word_count: 1261
raw_file: raw/2026-04-19_does-anyone-even-use-dash-linuxmemes_39cf8f19.txt
tldr: A Reddit meme thread about whether anyone uses `dash` turns into a shell-war mini-debate where u/raedr7n argues that plenty of people do because `dash` is Debian’s default `/bin/sh` and is faster/POSIX-compliant, while others split between `zsh`, `fish`, `bash`, and jokes about `csh` being “under the ocean floor.”
key_quote: Dash is a great `/bin/sh` shell because it's focussed purely on speed and POSIX compatibility.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: good
people:
- u/Nitrocellulose_404
- u/h4636oh
- u/raedr7n
- u/Dragonflame7155
- u/KasaneTeto_
- u/noob-nine
- u/DoorsXP
- u/WeirdAsQuantumWorld
- u/MagellanCl
- u/IAmTheMageKing
- u/TheOmegaCarrot
- u/SamSalvador440
- u/The_Dark_Byte
- u/GregTheHun
- u/avnothdmi
- u/chainbreaker1981
- u/LongerHV
- u/MFAFuckedMe
tools:
- dash
- bash
- zsh
- fish
- csh
- ksh
- tcsh
- pwsh
libraries: []
companies:
- Debian
- Apple
- Alpine
tags:
- shell
- linux
- debian
- posix
- scripting
---

### TL;DR
A Reddit meme thread about whether anyone uses `dash` turns into a shell-war mini-debate where **u/raedr7n** argues that plenty of people do because `dash` is Debian’s default `/bin/sh` and is faster/POSIX-compliant, while others split between `zsh`, `fish`, `bash`, and jokes about `csh` being “under the ocean floor.”

### Key Quote
> “Dash is a great `/bin/sh` shell because it's focussed purely on speed and POSIX compatibility.”

### Summary
- **Top comment (verbatim):** "i use zsh as my default shell but i have set the symlink for /bin/sh to dash"
- **Top commenter:** `u/h4636oh`
- **Thread topics:**
  - Whether anyone actually uses `dash` as a shell
  - The difference between an interactive login shell and `/bin/sh`
  - Debian’s use of `dash` for `/bin/sh`
  - Comparisons among `bash`, `zsh`, `fish`, `csh`, `ksh`, `tcsh`, and `pwsh`
  - Performance vs feature-rich shells

- The thread’s main joke question is whether `dash` is ever used, but the replies quickly clarify that it is widely used as a **non-interactive POSIX `/bin/sh`** implementation, especially on **Debian**.
- Multiple commenters explain the common setup:
  - **login/interactive shell**: often `bash`, `zsh`, or `fish`
  - **`/bin/sh`**: often symlinked to `dash` for scripts and speed
- A repeated point is that `dash` is not meant to be a fancy interactive shell; it is valued because it is:
  - **fast**
  - **POSIX-compliant**
  - suitable for system scripts
- There is some confusion in-thread from users realizing that:
  - they may “use bash” interactively
  - while their system’s `/bin/sh` actually points to `dash`
- The discussion includes a mini-debate over whether `dash`’s speed matters:
  - one side says Bash’s extra features are worth the slight overhead for interactive use
  - the other says `dash` can be significantly faster for scripts and avoids Bash startup/config overhead
- Shell preference banter dominates:
  - **zsh > bash** is stated by one commenter
  - **fish** gets praise for being pleasant even without extensions
  - **csh** gets dunked on humorously
  - there’s a side tangent into `ksh`, `tcsh`, `rc`, `eshell`, `pwsh`, and old-school shells
- A few concrete technical clarifications appear:
  - On Debian, **`/bin/sh` is a symlink to `dash`**
  - The **default user/login shell** may still be `bash`
  - `dash` is especially suited for scripts started via a shebang like `#!/bin/sh`
- The thread is mostly humor and shell tribalism, but it does contain a useful practical explanation of why `dash` exists and how it is used.

### Assessment
This has **medium durability** because the shell concepts are fairly timeless, but the exact distro defaults and the meme context are tied to a specific Reddit post from the time. The content is a **mixed** social thread: mostly opinion/jokes, with some genuine technical clarification. Density is **medium**: there are a lot of concrete examples and distinctions, but they’re embedded in conversational back-and-forth. Originality is mostly **commentary** rather than primary technical writing, though several comments provide accurate explanatory synthesis. This is best as a **skim-once** or light **refer-back** reference if you need the Debian `/bin/sh` vs login shell distinction. **Scrape quality is good**: the thread structure, prominent viewpoints, and discussion samples are captured clearly, though the original linked image is not included.
