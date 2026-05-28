---
url: https://github.com/mitsuhiko/agent-stuff/blob/main/skills/librarian/SKILL.md
title: agent-stuff/skills/librarian/SKILL.md at main · mitsuhiko/agent-stuff
scraped_at: '2026-04-19T07:48:31Z'
word_count: 279
raw_file: raw/2026-04-19_agent-stuff-skills-librarian-skill-md-at-main-mitsuhiko-agent-stuff_a1049103.txt
tldr: A small “librarian” skill for caching remote git repositories into a stable local path under `~/.cache/checkouts/...`, so future references can reuse the same checkout with periodic refreshes instead of repeated full clones.
key_quote: Cache and refresh remote git repositories under ~/.cache/checkouts/<host>/<org>/<repo> so future references can reuse a local copy.
durability: medium
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- checkout.sh
libraries: []
companies: []
tags:
- git
- caching
- repositories
- workflow
- version-control
---

### TL;DR
A small “librarian” skill for caching remote git repositories into a stable local path under `~/.cache/checkouts/...`, so future references can reuse the same checkout with periodic refreshes instead of repeated full clones.

### Key Quote
"Cache and refresh remote git repositories under ~/.cache/checkouts/<host>/<org>/<repo> so future references can reuse a local copy."

### Summary
- **Purpose of the skill**
  - Designed for when a user points to a remote git repository or when one is encountered indirectly.
  - Supports GitHub, GitLab, Bitbucket URLs, `git@...` forms, and `owner/repo` shorthand.
  - Goal is to maintain a reusable local checkout that is:
    - **stable**: predictable filesystem path
    - **up to date**: refreshed periodically, fast-forwarded when safe
    - **efficient**: uses partial clones with `--filter=blob:none`

- **Cache location**
  - Repositories are stored at:
    - `~/.cache/checkouts/<host>/<org>/<repo>`
  - Example:
    - `github.com/mitsuhiko/minijinja` → `~/.cache/checkouts/github.com/mitsuhiko/minijinja`

- **Primary command**
  - Resolve or update a repo checkout with:
    - `bash checkout.sh <repo> --path-only`
  - Accepted forms:
    - `bash checkout.sh mitsuhiko/minijinja --path-only`
    - `bash checkout.sh github.com/mitsuhiko/minijinja --path-only`
    - `bash checkout.sh https://github.com/mitsuhiko/minijinja --path-only`

- **What the script does**
  - Parses the repository reference into `host/org/repo`.
  - Clones the repository if it is missing.
  - Reuses an existing checkout if present.
  - Fetches from `origin` when the checkout is stale.
  - Default staleness interval is **300 seconds**.
  - Attempts a fast-forward merge if:
    - the checkout is clean, and
    - it has an upstream configured.

- **Update strategy**
  - Default behavior is a **throttled refresh** every 5 minutes to reduce unnecessary network traffic.
  - Immediate refresh is available with:
    - `bash checkout.sh <repo> --force-update --path-only`

- **Recommended workflow**
  - First, get the repository path via `checkout.sh --path-only`.
  - Use that local path for searching, reading, and analysis.
  - For later references to the same repo, call `checkout.sh` again so it can reuse and refresh the cached checkout.

- **Editing guidance**
  - Avoid editing directly in the shared cache.
  - If changes are needed, create a separate worktree or copy for task-specific modifications.

- **Default behavior note**
  - `owner/repo` shorthand assumes `github.com` if no host is provided.

### Assessment
This is a **reference** document with practical workflow instructions rather than conceptual discussion. Its durability is **medium**: the overall caching pattern is fairly stable, but the specific command names, default refresh interval of 300 seconds, and cache path conventions are implementation-dependent and could change. The content is **dense** and **highly specific**, with concrete paths, commands, and operational rules. It is **primary source** material because it documents the intended behavior of the `librarian` skill itself. It is best used **refer-back** when you need to remember how to resolve, cache, or refresh repository checkouts. Scrape quality is **good**: the full markdown content appears captured, and no obvious sections, code blocks, or images seem missing.
