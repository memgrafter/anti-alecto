---
url: https://www.reddit.com/r/rust/comments/1sm4qsm/ssh_latesh_clubhouse_for_devs_take_a_break_chat/?share_id=Yg8oLqEHDigh-bnbSgIor
title: 'ssh late.sh - Clubhouse for Devs. Take a break, chat, chill, listen to music and play some games! :) My first serious, source-available, rust project! : rust'
scraped_at: '2026-04-19T22:00:44Z'
word_count: 2131
raw_file: raw/2026-04-19_ssh-late-sh-clubhouse-for-devs-take-a-break-chat-chill-listen-to-music-and-play-_1ed0d5fa.txt
tldr: A Rust dev posts late.sh, an SSH-based “clubhouse for devs” with chat, games, music, and a bonsai streak system, and the thread largely praises it while debating IPv6 connectivity, AI-assisted coding, and the project’s source-available FSL-1.1-MIT licensing.
key_quote: “ssh late.sh That's all, no passwords. no OAuth, no accounts, your ssh key is your identity.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Bl4ckBe4rIt
- iamasuitama
- nafatsari
- Tiny_Cow_3971
- deanominecraft
- haakon
- SleeplessSloth79
- kabocha_
- dschramm_at
tools:
- ssh
- russh
- ratatui
- axum
- testcontainers
- OpenSSH
libraries: []
companies:
- Postgres
tags:
- rust
- ssh
- terminal-app
- developer-community
- source-available-license
---

### TL;DR
A Rust dev posts **late.sh**, an SSH-based “clubhouse for devs” with chat, games, music, and a bonsai streak system, and the thread largely praises it while debating IPv6 connectivity, AI-assisted coding, and the project’s source-available FSL-1.1-MIT licensing.

### Key Quote
“ssh late.sh That's all, no passwords. no OAuth, no accounts, your ssh key is your identity.”

### Summary
- **What the project is**
  - `late.sh` is a cozy social app for developers accessed primarily over SSH.
  - It combines:
    - chat and direct messages
    - multiple rooms
    - music listening/control
    - games and leaderboards
    - badges and streaks
    - a “bonsai” ASCII plant that grows with daily use and withers if streaks are lost
  - Landing page: `https://late.sh`
  - Code: `https://github.com/mpiorowski/late-sh`

- **Tech stack and implementation**
  - Rust workspace with 4 crates
  - Uses `russh` for SSH server functionality
  - `ratatui` for terminal UI
  - `axum` for HTTP/WebSocket side
  - Postgres
  - `testcontainers` for integration tests

- **Access and identity model**
  - No passwords, OAuth, or accounts.
  - SSH key is the identity.
  - Users connect via `ssh late.sh`.
  - Music has two access modes because SSH cannot stream audio directly:
    - CLI companion app: recommended, includes audio visualizer
    - Web mode: browser-based playback/control

- **Features mentioned**
  - Games: 2048, tetris, sudoku, nonograms, minesweeper, solitaire
  - Social tools: chat, DMs, multiline input, reply/mention support, room creation
  - Content/news sharing: links, YouTube, Twitter, etc. get processed and shared
  - Community mechanics: voting for next coding-music session, badges, streaks
  - Audio visualizer synced to beats in terminal

- **Author’s takeaways from building it in Rust**
  - `russh` render-loop backpressure was a real issue; a short timeout on `handle.data` (50ms) was needed so slow clients wouldn’t block everyone.
  - Music synchronization required paired-client WebSocket state sync and a token-keyed registry using `mpsc` channels.
  - `ratatui` worked comfortably with a 15 fps render loop.
  - The author explicitly wanted an audio visualizer and had to engineer around SSH’s limitations.

- **License / openness**
  - License is **FSL-1.1-MIT**
  - Source-available now, converts to MIT after 2 years
  - The author says this was intentional to protect the initial network/community from being split off too early

- **Top comment (verbatim):** “This is not how you create a valuable startup. You're not supposed to encourage, let alone enable, real people to connect with eachother!!”
- **Top commenter:** `u/iamasuitama`
- **Thread topics:**
  - whether this is a playful anti-startup / pro-community project
  - SSH identity and key-based login
  - IPv6 connection failures and `ssh -4 late.sh`
  - whether the project is AI-assisted or “hand made”
  - concerns about the future-license / source-available model

- **Discussion highlights**
  - Many commenters reacted positively and said the project is cool, cozy, or nostalgic.
  - Several users had connection issues related to IPv6; the fix was often `ssh -4 late.sh`.
  - One user asked for transparency on whether the project was vibe-coded, AI-assisted, or hand-made; the author answered **AI assisted**.
  - A permissions/publickey issue was resolved by generating an SSH key first.
  - Some discussion focused on the license: the MIT license becomes effective after two years.
  - One commenter raised a security concern about music-control paths becoming a future attack surface; the author said they were hardening paths in response.

### Assessment
This is a high-density, discussion-heavy Reddit thread centered on a niche Rust project launch, so it has **medium durability**: the core ideas about SSH-based community apps and Rust implementation lessons will remain useful, but specific details like the repository state, connectivity bugs, and licensing terms may age. The content is a **mixed** blend of announcement, technical notes, and social thread commentary, with the original post being the primary source and the comments adding live feedback. The thread is **dense** in practical specifics—stack, commands, features, failure modes, and design tradeoffs—making it good for quick reference and later comparison, though not a deep technical tutorial. Scrape quality is **good**: the main post, prominent comments, nested replies, and key implementation/usage details are present, with no obvious missing sections beyond any images or external context not included in the text capture.
