---
url: https://github.com/brainopia/pi-ultrathink
title: 'brainopia/pi-ultrathink: pi-ultrathink is a Pi extension that gives your agent the ability to reflect, verify, and iteratively improve its work before handing it back to you.'
scraped_at: '2026-04-19T06:55:59Z'
word_count: 1772
raw_file: raw/2026-04-19_brainopia-pi-ultrathink-pi-ultrathink-is-a-pi-extension-that-gives-your-agent-th_0369a42c.txt
tldr: pi-ultrathink is a Pi extension that turns multi-pass code review into an explicit git-backed workflow, with `/ultrathink`, `/ultrathink-review`, and `/ultrathink-oracle` for iterative refinement or AI-mediated review.
key_quote: “Complex coding tasks often need more than one pass.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- brainopia
tools:
- pi
libraries: []
companies:
- brainopia
tags:
- code-review
- git
- ai-agents
- pi
- developer-tools
---

### TL;DR
`pi-ultrathink` is a Pi extension that turns multi-pass code review into an explicit git-backed workflow, with `/ultrathink`, `/ultrathink-review`, and `/ultrathink-oracle` for iterative refinement or AI-mediated review.

### Key Quote
“Complex coding tasks often need more than one pass.”

### Summary
- **What it is**
  - A Pi extension from `brainopia` that adds three commands:
    - `/ultrathink <prompt>`: runs a git-driven review loop on a temporary branch
    - `/ultrathink-review [optional prompt]`: reviews and improves existing branch changes through visible passes
    - `/ultrathink-oracle <prompt>`: uses an AI oracle reviewer instead of git-based stopping
- **Core idea**
  - The extension makes iterative coding work explicit and inspectable:
    - initial task is visible in chat
    - follow-up review prompts are visible
    - every changed pass becomes a git commit on a scratch branch
    - the final summary lists branch outcome and commit history
- **How `/ultrathink` works**
  - Starts from a clean working tree
  - Opens a continuation-prompt editor for review instructions
  - Prepends:
    - the original task
    - a `git diff` command based on the baseline commit
  - Creates a temporary branch named like `ultrathink/<ai-generated-slug>`
  - Runs repeated agent passes until one pass makes no changes or another stop condition is reached
  - Commits each changed pass with AI-generated title/body
  - Reintegration rules:
    - 0 scratch commits: delete scratch branch
    - 1 scratch commit: rebase then fast-forward original branch
    - 2+ scratch commits: merge back with an AI-authored merge commit
- **How `/ultrathink-review` differs**
  - Intended for existing changes already on the current branch
  - Does **not** open the continuation-prompt editor
  - Converts dirty working tree changes into a bootstrap commit on the scratch branch if needed
  - Determines review base by branch situation:
    - dirty tree → bootstrap commit
    - tracking pushed upstream → review from `last-pushed`
    - tracking another upstream → `first-unique`
    - no upstream but other local branches exist → compare against all local branches to find unique commits
  - Fails clearly if there is no sensible base to review from
- **Oracle mode**
  - `/ultrathink-oracle` replaces git stop conditions with an AI reviewer
  - Works without git and in any directory
  - Uses a setup overlay to choose:
    - oracle model
    - thinking level (`minimal`, `low`, `medium`, `high`, `xhigh`)
    - oracle system prompt
  - The oracle is a separate in-process agent session with tools like `read`, `bash`, `grep`, `find`, and `ls`
  - Acceptance is signaled by a dedicated `oracle_accept` tool, not by text parsing
  - Stops when:
    - oracle accepts
    - max rounds are reached
    - user cancels
    - active turn is interrupted
- **Configuration**
  - Config is stored globally in `~/.pi/ultrathink.json`
  - Key settings include:
    - `maxIterations`
    - `continuationPromptTemplate`
    - `commitBodyMaxChars`
    - `naming.provider` / `naming.modelId`
    - `oracle.provider` / `oracle.modelId`
    - `oracle.thinkingLevel`
    - `oracle.systemPromptTemplate`
    - `oracle.maxRounds`
  - The naming model is only used for:
    - scratch-branch slug generation
    - commit title/body generation
    - merge commit title/body generation when needed
- **Git behavior details**
  - Scratch branch names have no run-id suffix, only the generated slug
  - If the branch name already exists, the naming model is asked for another slug
  - Normal completion attempts automatic reintegration
  - On conflicts during final rebase/merge, it aborts and preserves the scratch branch for manual resolution
- **Stop conditions**
  - No git changes
  - `maxIterations` reached
  - User cancellation
  - Interrupt cancellation
  - Naming failure, which falls back to a generic commit and ends with `naming-error`
  - Git failure
- **Final summaries**
  - Git task runs summarize:
    - original branch
    - scratch branch
    - naming model
    - reintegration result
    - whether scratch branch was deleted
    - each commit SHA/title/description
    - final merge commit if present
  - Review runs also include:
    - review source (`dirty-bootstrap`, `last-pushed`, or `first-unique`)
    - diff base used in the injected prompt
    - reviewed commit list
  - Oracle runs summarize:
    - number of oracle review rounds
    - oracle verdict if accepted
- **Installation and development**
  - Install via npm:
    - `pi install @brain0pia/pi-ultrathink`
  - Quick try:
    - `pi -e npm:@brain0pia/pi-ultrathink`
  - Local dev load:
    - `pi -e ./src/index.ts`
  - Development commands:
    - `npm install`
    - `npm run check`
    - `npm run demo`
  - The demo uses a scripted provider and does not require real model credentials

### Assessment
This is a high-density, practical reference/tutorial with strong implementation detail and clear operational behavior. Durability is **medium**: the workflow concepts are fairly stable, but the specifics depend on Pi, the extension’s config format, model provider IDs, and the current npm/package setup. It is **mixed** content, leaning tutorial/reference, and appears to be **primary source** documentation from the project README rather than commentary. It is best used as **refer-back** material when installing, configuring, or understanding the extension’s branching/review behavior. Scrape quality is **good**: the README content, code fences, and Mermaid diagrams are present, and the key sections seem intact.
