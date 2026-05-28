---
url: https://github.com/zeflq/pi-reviewer
title: zeflq/pi-reviewer
scraped_at: '2026-04-19T06:54:09Z'
word_count: 1393
raw_file: raw/2026-04-19_zeflq-pi-reviewer_f35a34ef.txt
tldr: pi-reviewer is an AI-powered pull request review tool for the `pi` agent that can run locally, over SSH, in a browser UI, or automatically in GitHub Actions, with configurable severity filtering and project-specific review conventions.
key_quote: “AI-powered PR reviewer using the pi agent — model-agnostic, works with any provider.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- github-actions
- gh
- tibdex/github-app-token
libraries: []
companies:
- GitHub
- Anthropic
- OpenAI
tags:
- code-review
- pull-requests
- github-actions
- developer-tools
- ai-agents
---

### TL;DR
`pi-reviewer` is an AI-powered pull request review tool for the `pi` agent that can run locally, over SSH, in a browser UI, or automatically in GitHub Actions, with configurable severity filtering and project-specific review conventions.

### Key Quote
“AI-powered PR reviewer using the pi agent — model-agnostic, works with any provider.”

### Summary
- `pi-reviewer` is a `pi` extension and GitHub Action that reviews code diffs and returns structured findings grouped by severity: `critical`, `warn`, and `info`.
- It supports multiple workflows:
  - **Local mode**: `/review`, `/review --branch dev`, `/review --pr 42`, `/review --diff HEAD~1`
  - **SSH mode**: `/review --ssh` for remote machines via an SSH extension
  - **UI mode**: `/review --ui` to inspect findings in a browser and decide per comment
  - **CI mode**: runs on every PR through GitHub Actions and posts review comments
- The tool is **model-agnostic** and works with any provider through `pi`, with examples mentioning Anthropic and OpenAI.
- In the UI, each finding can be **accepted**, **rejected**, or marked to **discuss**, with actions to:
  - **Save** to `pi-review.md`
  - **Send** accepted findings back to the agent
  - **Save & Send** both
- The browser UI highlights decisions visually and remembers theme preference in `~/.pi/pi-reviewer/config.json`.
- If the diff is empty or no inline comments are generated, the fallback UI still opens with the summary panel.
- For CI setup:
  - Run `npx github:zeflq/pi-reviewer init`
  - This generates `.github/workflows/pi-review.yml`
  - Required secrets include `PI_API_KEY` and `GITHUB_TOKEN`-based access for posting comments
- GitHub Action inputs include:
  - `github-token`
  - `pi-api-key`
  - optional `model` like `anthropic/claude-opus-4-6`
  - optional `post-comment`
  - `min-severity`
- Default CI comments appear under `github-actions[bot]`; posting under a custom bot name requires a GitHub App and token exchange via `tibdex/github-app-token@v2`.
- Shared extension options include:
  - `--branch <name>`
  - `--pr <number>`
  - `--diff <ref>`
  - `--ssh`
  - `--ui`
  - `--min-severity <level>`
  - `--dry-run`
- Diff handling details:
  - `/review` and `--branch` use `git merge-base`
  - staged, unstaged, and committed changes are included
  - `--pr` and `--diff` review exact refs/remote diffs
- It filters out noisy files before review, including:
  - lockfiles
  - `dist/`
  - `build/`
  - `.next/`
  - `node_modules/`
  - minified files
  - `.d.ts` files
- If the diff exceeds 100k characters, it drops whole file sections rather than slicing hunks, and tells the agent which files were skipped.
- The project encourages adding:
  - `AGENTS.md` for general conventions
  - `CLAUDE.md` as a fallback
  - `REVIEW.md` for review-specific rules
- Markdown links to other `.md` files are inlined automatically to give the agent more context.
- The page ends by pointing to `TODO.md` for the full roadmap.

### Assessment
This is a high-density, practical reference/documentation page for a developer tool, with a mix of tutorial, reference, and product overview content. Durability is medium: the core idea of AI-assisted PR review is fairly stable, but the setup commands, GitHub Actions details, and model/provider examples are tied to the current `pi` ecosystem and may change. The content is primarily a reference/source page rather than commentary, and it is meant to be revisited when setting up or configuring the tool, so refer-back value is high. Scrape quality looks good overall: the key sections, commands, YAML example, and configuration details are present, though rendered assets like the demo GIF are not included in text form.
