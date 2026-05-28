---
url: https://www.reddit.com/r/linuxmemes/comments/tszfjf/does_anyone_even_use_dash/
title: 'does anyone even use dash? : linuxmemes'
scraped_at: '2026-04-17T05:23:21Z'
word_count: 1258
raw_file: raw/2026-04-17_does-anyone-even-use-dash-linuxmemes_39cf8f19.txt
tldr: A Linux memes thread asks whether anyone uses `dash`, and the replies explain that many people do—mostly as `/bin/sh` for fast, POSIX-compliant scripting, especially on Debian—while arguing about whether it makes sense as an interactive shell.
key_quote: Dash is a great `/bin/sh` shell because it's focussed purely on speed and POSIX compatibility.
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Nitrocellulose_404
- h4636oh
- raedr7n
- Dragonflame7155
- KasaneTeto_
- DoorsXP
- WeirdAsQuantumWorld
- Luke Smith
tools:
- dash
- zsh
- bash
- fish
- csh
- ksh
- tcsh
- eshell
- rc
- sash
- scsh
- pwsh
- cmd
libraries: []
companies:
- Debian
- Alpine
- macOS
tags:
- linux
- shell-scripting
- posix
- debian
- command-line
---

### TL;DR
A Linux memes thread asks whether anyone uses `dash`, and the replies explain that many people do—mostly as `/bin/sh` for fast, POSIX-compliant scripting, especially on Debian—while arguing about whether it makes sense as an interactive shell.

### Key Quote
“Dash is a great `/bin/sh` shell because it's focussed purely on speed and POSIX compatibility.”

### Summary
- The post is a r/linuxmemes thread titled **“does anyone even use dash?”** by **u/Nitrocellulose_404** with **829 score** and **124 comments**.
- The main consensus in the comments is that **dash is widely used as `/bin/sh`**, not usually as a person’s interactive login shell.
- Several users clarify an important distinction:
  - **Interactive shells**: people tend to prefer **zsh**, **bash**, or **fish** for usability features like completion and nicer UX.
  - **Script shells**: **dash** is valued because it is **fast** and **POSIX-compliant**.
- A recurring factual point is that on **Debian**, `/bin/sh` commonly points to **dash**, while the user’s default login shell may still be **bash**.
- One commenter notes:
  - `bash` must read multiple config files on startup, which adds overhead.
  - `dash` avoids that and can be **about 2x faster** in benchmarks, according to the thread’s claims.
- There is a side discussion about shell preferences:
  - Some users champion **zsh > bash**
  - Others like **fish**
  - One joke comment says **csh is “under the ocean floor”**
  - The thread branches into shell-genealogy humor involving **ksh, tcsh, rc, pwsh, cmd, Bourne shell, Thompson shell**, etc.
- A few practical points are mentioned:
  - If a script has a shebang like `#!/bin/sh`, it will run under whatever shell `/bin/sh` points to.
  - For POSIX shell scripts, that shell should be POSIX-compliant “to avoid a very bad time.”
  - One user says they use dash as their default shell because they are a **startx** user and launch **zsh** manually in Konsole.
  - Another says **Luke Smith** uses it.
- The thread includes some disagreement:
  - Some argue the time saved by dash is not worth losing bash features.
  - Others respond that dash is intended for a different job entirely, and that using it for scripts is the correct use case.
  - One commenter dismisses interactive dash users as “LARPing,” while others point out dash’s usefulness in **embedded applications**, **containers**, **VMs**, **cloud**, and **desktop** contexts.

### Assessment
This is a **mixed** social-thread discussion with a strong factual core about shell roles and common `/bin/sh` behavior on Debian, but it is wrapped in memes, preference wars, and some exaggeration. **Durability is medium**: the general concept of dash as a lightweight POSIX shell is stable, but distro defaults and shell ecosystems can change over time. **Density is medium** because the thread contains several concrete claims and clarifications, but much of it is conversational back-and-forth. **Originality is commentary** rather than primary source, since it reflects community opinion and informal explanations. It works best as a **refer-back** reference for remembering the distinction between `/bin/sh` and interactive shells. **Scrape quality is good**: the title, score, comment count, and a representative set of top comments and nested replies are present, though obviously images/memes are not included.
