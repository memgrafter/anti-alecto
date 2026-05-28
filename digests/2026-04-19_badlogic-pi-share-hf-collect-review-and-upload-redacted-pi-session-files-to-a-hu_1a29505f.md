---
url: https://github.com/badlogic/pi-share-hf
title: 'badlogic/pi-share-hf: Collect, review, and upload redacted pi session files to a Hugging Face dataset'
scraped_at: '2026-04-19T07:17:45Z'
word_count: 1417
raw_file: raw/2026-04-19_badlogic-pi-share-hf-collect-review-and-upload-redacted-pi-session-files-to-a-hu_1a29505f.txt
tldr: pi-share-hf is a CLI that incrementally collects `pi` coding-agent sessions from one OSS project, redacts exact secrets, blocks deny-listed or TruffleHog-flagged content, runs LLM review, and uploads only approved sessions to a Hugging Face dataset.
key_quote: Any TruffleHog finding blocks the session automatically.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
tools:
- pi-share-hf
- pi
- TruffleHog
- huggingface-cli
libraries: []
companies:
- Hugging Face
tags:
- cli-tools
- data-publishing
- secret-redaction
- llm-review
- hugging-face
---

### TL;DR
`pi-share-hf` is a CLI that incrementally collects `pi` coding-agent sessions from one OSS project, redacts exact secrets, blocks deny-listed or TruffleHog-flagged content, runs LLM review, and uploads only approved sessions to a Hugging Face dataset.

### Key Quote
“Any TruffleHog finding blocks the session automatically.”

### Summary
- **Purpose:** Publish public datasets of `pi` agent traces from a single open-source project to Hugging Face, while avoiding repeated reprocessing by keeping a local workspace cache.
- **Core pipeline:**
  1. Collect `pi` session files for a project
  2. Redact exact secrets from env files and `--secret` inputs
  3. Reject sessions matching user-provided `--deny` regexes
  4. Scan redacted output with TruffleHog
  5. Run LLM-based review on remaining sessions
  6. Upload only sessions that pass all checks
- **Incremental behavior:** Repeated runs only process changed or new sessions; the workspace stores state so you can run it over time without redoing everything.
- **Supported input:** `pi` coding agent session files in the session format documented in `pi-mono`.
- **Install requirements:**
  - `npm install -g pi-share-hf`
  - `npm install -g @mariozechner/pi-coding-agent`
  - TruffleHog installed separately (`brew install trufflehog` on macOS, upstream instructions on Linux/Windows)
  - Hugging Face write token via `HF_TOKEN` or `~/.cache/huggingface/token`
- **Typical workflow in an OSS project:**
  - Add `.pi/hf-sessions/` to `.gitignore`
  - Run `pi-share-hf init --repo ...`
  - Run `pi-share-hf collect` with secrets/deny lists and optional LLM provider/model settings
  - Inspect with `list --uploadable`, `grep`, and images folder if enabled
  - Manually reject anything suspicious
  - Run `pi-share-hf upload` or `upload --dry-run`
- **Redaction model:** Only exact secret values are removed, sourced from:
  - `--env-file` (default `~/.zshrc`)
  - `--secret <file>` with one secret per line
  - `--secret <literal>`
  This is intentional: exact matching is high precision, while TruffleHog handles broader secret detection afterward.
- **TruffleHog behavior:** Scans the **redacted** session, not the raw session. Any finding—`verified`, `unverified`, or `unknown`—blocks upload. Per-session reports are stored under `.pi/hf-sessions/reports/`.
- **LLM review behavior:** The model sees project context files plus a plain-text transcript of the redacted session and returns fields like:
  - `about_project: yes | no | mixed`
  - `shareable: yes | no | manual_review`
  - `missed_sensitive_data: yes | no | maybe`
  - plus flagged parts and summary
  Review sidecars live in `.pi/hf-sessions/review/`.
- **Upload rules:** Only sessions that pass deterministic checks, TruffleHog, and LLM review are uploaded; manually rejected sessions, missing reviews, failed reviews, or unchanged remote items are skipped.
- **Commands covered:**
  - `init` — create workspace and map it to a Hugging Face dataset repo
  - `collect` — gather sessions, redact, scan, review
  - `review` — rerun only LLM review on already-redacted sessions
  - `reject` — mark sessions or extracted images as never uploadable
  - `list` — inspect workspace sessions
  - `grep` — search only uploadable sessions
  - `upload` — push approved sessions and update remote manifest
- **Workspace structure:** Includes local and remote manifests, redacted public candidates, private reports, review chunks, extracted images, and `reject.txt`.
- **Dataset output:** Uploaded files are redacted `*.jsonl` sessions plus `manifest.jsonl`.
- **Developer note:** `npm run check` is the main development command.

### Assessment
This is a **mixed** technical/reference README with tutorial elements. Durability is **medium**: the workflow concepts are fairly stable, but the exact CLI flags, defaults, dependencies, and Hugging Face/TruffleHog behavior are version-sensitive and could change. Density is **high** because it packs install steps, operational workflow, redaction/review logic, command docs, and workspace layout into one page. It is a **primary source** for this tool’s intended behavior and usage, not commentary. Best used as **refer-back** reference when setting up or operating the pipeline, though the quick-start sections also support a one-time skim. Scrape quality looks **good**: the README content appears complete, including command examples, option lists, workspace layout, and example report JSON; no obvious code blocks or sections seem missing.
