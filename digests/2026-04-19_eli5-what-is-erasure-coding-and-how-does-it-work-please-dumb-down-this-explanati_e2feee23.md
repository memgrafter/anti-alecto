---
url: https://www.reddit.com/r/explainlikeimfive/comments/qpgkb7/eli5_what_is_erasure_coding_and_how_does_it_work/
title: 'ELI5 what is erasure coding and how does it work. Please dumb down this explanation way down for me, I may have follow up questions because of the intricacies of the topic. : explainlikeimfive'
scraped_at: '2026-04-19T21:56:55Z'
word_count: 810
raw_file: raw/2026-04-19_eli5-what-is-erasure-coding-and-how-does-it-work-please-dumb-down-this-explanati_e2feee23.txt
tldr: A short r/explainlikeimfive thread explains erasure coding as redundancy for missing/unavailable data, using a coin-flip/walkie-talkie analogy and a CD/DVD/Blu-ray scratch example, with the top commenter arguing it’s about reconstructing lost pieces, not compressing data.
key_quote: Erasure coding is a form of error correction in data storage.
durability: low
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: partial
people:
- u/Koooooj
- u/Xelopheris
- u/[deleted]
tools: []
libraries: []
companies: []
tags:
- erasure-coding
- error-correction
- data-storage
- compression
- redundancy
---

### TL;DR
A short r/explainlikeimfive thread explains erasure coding as redundancy for missing/unavailable data, using a coin-flip/walkie-talkie analogy and a CD/DVD/Blu-ray scratch example, with the top commenter arguing it’s about reconstructing lost pieces, not compressing data.

### Key Quote
“Erasure coding is a form of error correction in data storage.”

### Summary
- **Top comment (verbatim):** “Let's say I need to flip a few coins, then tell you the entire sequence of coin flips. If I communicate even a single coin flip incorrectly then that counts as a failure.”
- **Top commenter:** `u/Koooooj`
- **Thread topics:**
  - What “erasure” means in erasure coding vs ordinary bit-flip errors
  - Why redundancy is added to recover missing data
  - Why erasure coding is **not** compression
  - Storage/media examples like scratched CDs/DVDs/Blu-rays
  - Whether the technique is about storage savings or data integrity

- The top reply uses a simple communication analogy:
  - A sender reads a sequence of coin flips over unreliable “cheap walkie-talkies.”
  - If a bit is garbled or missing, that’s treated as an **erasure**: the receiver knows a slot is missing, even if the exact value is unknown.
  - Instead of asking for the missing part again, you can send extra redundant information up front so the message can be reconstructed later.
- Another reply clarifies the core purpose:
  - **Erasure coding is not for storage savings.**
  - It always uses **more space** because it adds redundancy.
  - Its goal is **data integrity / recoverability** when pieces of data are unavailable.
- The discussion distinguishes erasure coding from compression:
  - Compression tries to store **fewer** bits than the original file.
  - Erasure coding stores **more** bits so the original can be recovered if some parts are lost.
  - The reply notes that compression works only because real files often contain patterns; random data generally does not compress well.
- A second top-level comment ties it to physical media:
  - Traditional error correction protects against **bit flips**.
  - Erasure coding protects against **missing sections** of data.
  - Example: a **giant gouge on a CD/DVD/Blu-ray** can destroy a localized area.
  - One strategy is to arrange data so that damage to any one physical region does not wipe out all the information needed to reconstruct a logical chunk.
- The thread is very short and mostly explanatory, with no major disagreement:
  - One line of questioning asks whether this is a kind of compression for “cold data.”
  - The answer rejects that framing and keeps the focus on redundancy and fault tolerance.
- Because the scrape is truncated in places, the first comment is only partially captured, so the thread’s explanation is clear but not fully complete.

### Assessment
This is a **low-durability** social thread: the concept of erasure coding is enduring, but the wording, examples, and thread context are tied to this specific Reddit exchange rather than a canonical technical source. It is a **mixed** content type, mostly a tutorial/explanatory discussion with a small amount of clarification and correction. **Density is medium**: the thread is short but uses memorable analogies and a few concrete contrasts (compression vs redundancy, bit flips vs erasures, scratched optical discs). It is **commentary/synthesis**, not a primary technical source. Best used as a **skim-once** or light **refer-back** reference for the intuitive analogy, not as a deep-study source. **Scrape quality is partial**: the top comment is truncated mid-sentence, so the capture does not preserve the full argument or exact closing details, and some discussion is summarized rather than fully shown.
