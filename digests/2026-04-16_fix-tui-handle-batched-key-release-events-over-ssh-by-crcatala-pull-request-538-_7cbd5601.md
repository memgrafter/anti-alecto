---
url: https://github.com/badlogic/pi-mono/pull/538#issuecomment-3720734306
title: 'fix(tui): handle batched key release events over SSH by crcatala · Pull Request #538 · badlogic/pi-mono'
scraped_at: '2026-04-16T03:52:36Z'
word_count: 1838
raw_file: raw/2026-04-16_fix-tui-handle-batched-key-release-events-over-ssh-by-crcatala-pull-request-538-_7cbd5601.txt
tldr: This patch fixes TUI key handling so batched Kitty protocol release events received over SSH no longer cause valid key presses in the same chunk to be discarded.
key_quote: 'Fix: Add filterKeyReleases() that uses regex to remove only release sequences while preserving press events in batched input.'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- cc-vps
- crcatala
tools: []
libraries: []
companies:
- github
tags:
- terminal-input
- keyboard-events
- ssh
- tui
- kitty-protocol
---

### TL;DR
This patch fixes TUI key handling so batched Kitty protocol release events received over SSH no longer cause valid key presses in the same chunk to be discarded.

### Key Quote
"Fix: Add filterKeyReleases() that uses regex to remove only release sequences while preserving press events in batched input."

### Summary
- The patch addresses a bug in `packages/tui` where `isKeyRelease()` could incorrectly treat a whole input batch as a release if **any** event in the chunk was a release.
- The comment explains the trigger: **“The recent Kitty protocol flag 2 addition caused key presses to be dropped when batched with release events (common over SSH).”**
- The fix introduces `filterKeyReleases(data)` in `packages/tui/src/keys.ts`:
  - removes Kitty protocol release sequences using regex
  - preserves non-release input
- `packages/tui/src/tui.ts` is updated so focused components receive filtered input unless they opt in to key releases:
  - imports `filterKeyReleases` instead of `isKeyRelease`
  - replaces the old all-or-nothing `isKeyRelease(data)` drop check
  - skips forwarding input only when filtering leaves an empty string
- `packages/tui/src/index.ts` now exports `filterKeyReleases`.
- `packages/tui/CHANGELOG.md` adds:
  - an “Added” entry for `filterKeyReleases(data)`
  - a “Fixed” entry noting key presses are no longer dropped when batched with release events over SSH
- A new test file, `packages/tui/test/keys.test.ts`, adds coverage for:
  - `isKeyRelease`
  - `isKeyRepeat`
  - `filterKeyReleases`
  - `matchesKey`
  - `parseKey`
  - Kitty protocol sequences
  - legacy terminal input handling
- The test suite explicitly includes SSH-style batched input cases like:
  - `\x1b[97u\x1b[97;1:3u`
  - mixed press/release batches for multiple keys
  - arrow, Home/End, and functional key sequences

### Assessment
This is a high-value, narrow technical patch with **medium durability**: the core bug pattern around batched terminal input over SSH is likely to remain relevant, but the exact Kitty protocol details and implementation are version-sensitive. The content type is **mixed**—mostly a small code change with accompanying changelog and tests. Density is **high**, because the diff includes the bug description, API change, integration change, and a large test file. Originality is **primary source**, since this is the patch itself rather than commentary or aggregation. For later use, this is best as **refer-back** material: useful if you need to confirm the bug, the new `filterKeyReleases()` API, or the affected files (`keys.ts`, `tui.ts`, `index.ts`, `keys.test.ts`). Scrape quality looks **good** for the patch text and diff content shown here; it captures the key files and the full added test file, though the broader PR discussion beyond this comment is not present.
