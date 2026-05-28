---
url: https://news.ycombinator.com/item?id=47666024
title: 'Show HN: Ghost Pepper – Local hold-to-talk speech-to-text for macOS | Hacker News'
scraped_at: '2026-04-19T22:04:00Z'
word_count: 2949
raw_file: raw/2026-04-19_show-hn-ghost-pepper-local-hold-to-talk-speech-to-text-for-macos-hacker-news_613068c2.txt
tldr: Hacker News discussion of Ghost Pepper, a local-only, hold-to-talk speech-to-text app for macOS built by MattHart88, centered on privacy, model quality/speed comparisons (Whisper vs Parakeet vs Hex/Handy), and whether it meaningfully improves on existing local dictation tools.
key_quote: 100% open-source MIT license, would love feedback, PRs, and ideas on where to take it.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- MattHart88
- charlietran
- ipsum2
- goodroot
- konaraddi
- mathis
- hyperhello
- aristech
- guzík
- parhamn
- ericmcer
tools:
- Ghost Pepper
- Hex
- Handy
- Whisper
- Parakeet
- VoiceInk
- MacWhisper
- Glimpse
- Speech.framework
- Stream Deck
- yap dictate
libraries:
- whisper.cpp
- whisperkit
- faster-whisper
- FluidAudio
- parakeet-mlx
companies:
- OpenAI
- Apple
- Cohere
- Mozilla.ai
tags:
- speech-to-text
- macos
- local-ai
- privacy
- dictation
---

### TL;DR
Hacker News discussion of **Ghost Pepper**, a local-only, hold-to-talk speech-to-text app for macOS built by **MattHart88**, centered on privacy, model quality/speed comparisons (Whisper vs Parakeet vs Hex/Handy), and whether it meaningfully improves on existing local dictation tools.

### Key Quote
"100% open-source MIT license, would love feedback, PRs, and ideas on where to take it."

### Summary
- **What Ghost Pepper is**
  - A macOS **push-to-talk / hold-to-talk speech-to-text app**.
  - Built to keep **all models local**, so **no data leaves the computer**.
  - The author says they use it heavily for **coding and email** and are experimenting with it as a **voice interface for other agents**.
  - It is **open source** under the **MIT license**.
  - Project link: `https://github.com/matthartman/ghost-pepper`

- **Top comment (verbatim):** "Thank you for sharing, I appreciate the emphasis on local speed and privacy. As a current user of Hex (https://github.com/kitlangton/Hex (https://github.com/kitlangton/Hex)), which has similar goals, what are your thoughts on how they compare?"
- **Top commenter:** `u/charlietran`
- **Thread topics:**
  - Comparison to other local STT apps: **Hex**, **Handy**, **VoiceInk**, **MacWhisper**, **Glimpse**
  - **Model choice**: Whisper, **Parakeet v3**, Cohere Transcribe, faster-whisper
  - **Local privacy** vs speed/accuracy tradeoffs
  - **macOS-specific dictation/STT** alternatives and Apple’s built-in speech APIs
  - Feature requests: **video transcription**, **supported languages**, **custom corrections**, **hardware triggers** like foot pedals/Stream Decks

- **Main discussion themes**
  - Many commenters focus less on Ghost Pepper itself and more on the broader ecosystem of **local speech recognition tools**.
  - **Parakeet v3** gets repeatedly praised as **faster and more accurate than Whisper** when supported for a language.
  - Several users compare Ghost Pepper to:
    - **Hex**: similar local/privacy-oriented macOS dictation app
    - **Handy**: popular open-source local STT tool for Mac/Linux
    - **VoiceInk** / **MacWhisper**: other local dictation setups using Parakeet or Whisper
  - A recurring point is that **Whisper remains attractive** because it is reliable, supports many languages, and has multiple model sizes.
  - Some users point out that **Apple already has native dictation/STT APIs**, and wonder why third-party local apps need to exist at all.
  - Others highlight that **local apps still matter** because of privacy, custom workflows, and better UI/UX around push-to-talk.

- **Notable replies from the author**
  - On language support, MattHart88 says Ghost Pepper currently offers:
    - **Whisper small (multilingual)** — about **466 MB**, supports many languages
    - **Parakeet v3** — about **1.4 GB**, supports **25 languages** via FluidAudio
  - On transcription from a speech video, the author says it should work as long as the app’s microphone can hear the speaker.
  - On a microphone-permission bug, the author says the fix was merged and a **new version was up**.
  - On custom jargon and names, the author says the app’s **corrections feature** helps with most misspellings/jargon edge cases.

- **Practical/technical observations from the thread**
  - Some users report that **Parakeet** is excellent but can still have issues like repeated words, prompting discussion of **post-processing** or custom prompts.
  - There is interest in:
    - **Streaming dictation** that types as you speak
    - **automatic cleanup/post-processing**
    - **personalized models** tuned to a speaker’s voice and jargon
  - Hardware/workflow ideas include:
    - **Stream Deck** buttons
    - **foot pedals**
    - using local STT with **agents** and coding workflows

- **Tone / reception**
  - The thread is broadly positive and curious.
  - The main reaction is: **this is useful, but the space already has several strong local alternatives**, so differentiation matters.
  - The author gets encouragement, but also a lot of “how does it compare to X?” questions.

### Assessment
This is a **mixed** content item: part product announcement, part community comparison thread, and part technical workflow discussion. Durability is **medium** because the specific app, models, and macOS compatibility can go stale quickly, but the broader themes—local privacy-preserving dictation, push-to-talk UX, and model tradeoffs—will remain relevant longer. Content density is **medium-high** thanks to the many concrete comparisons, model names, and feature requests. Originality is **primary source plus commentary**: the launch post is original, while the thread mostly aggregates comparisons and user experiences. Reference style is **refer-back** if you’re tracking local STT tools or macOS dictation options. Scrape quality is **good** overall: it captured the launch text, the top comment, and many representative replies, though this is still a threaded capture rather than the full GitHub README or app UI details.
