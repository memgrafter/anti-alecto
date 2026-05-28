---
url: https://www.reddit.com/r/tmux/comments/1s5cmp0/cms_agent_statusaware_tmux_session_manager/
title: 'cms - agent status-aware tmux session manager : r/tmux'
scraped_at: '2026-04-19T23:51:38Z'
word_count: 1188
raw_file: raw/2026-04-19_cms-agent-status-aware-tmux-session-manager-r-tmux_083a3924.txt
tldr: A r/tmux post by u/blluecalx announces `cms`, an agent-status-aware tmux session manager for fuzzy-switching between projects, worktrees, sessions, and running agents, and the top comment praises its minimal “search then jump” workflow while the thread also branches into agent-status tracking and criticism of repetitive “agent-aware tmux” tools.
key_quote: Composable Fuzzy switcher for projects (repos), worktrees, and running agents.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- blluecalx
- gavraz
- sultanmvp
- ReferenceBoring7865
tools:
- tmux
- cms
- tms
- fzf
libraries: []
companies:
- Reddit
- GitHub
tags:
- tmux
- cli-tools
- agent-orchestration
- fuzzy-finder
- worktrees
---

### TL;DR
A r/tmux post by u/blluecalx announces `cms`, an agent-status-aware tmux session manager for fuzzy-switching between projects, worktrees, sessions, and running agents, and the top comment praises its minimal “search then jump” workflow while the thread also branches into agent-status tracking and criticism of repetitive “agent-aware tmux” tools.

### Key Quote
“Composable Fuzzy switcher for projects (repos), worktrees, and running agents.”

### Summary
- **Thread type:** Reddit discussion thread about a tmux-related CLI/tool release.
- **Original post:** u/blluecalx shares the GitHub repo for `cms` and describes it as:
  - an **agent status-aware tmux session manager**
  - based on **`tms`** (`jrmoulton/tmux-sessionizer`)
  - which itself is based on **ThePrimeagen’s tmux-sessionizer**
- The post includes a GIF link and positions the tool as an evolution of existing tmux sessionizers.

- **Top comment (verbatim):** "Composable Fuzzy switcher for projects (repos), worktrees, and running agents. cms # everything (configurable via [finder].include) cms -p # projects (what tms does out of the box) cms -a # agents only (live sorted by status) cms -awsp # agents, worktrees, sessions, projects \- Item ranking configurable per section. Section order set by flag order. `cms` tries to make the first item in the list always useful: * agents — sorted by state (`waiting` for input first, then `completed`, `idle`, `working`). (seen / unseen ranking on best effort basis) * projects / worktrees — sorted by `recent`. First item takes you back to last visited. The headless version: [`cms next`](https://github.com/ser-ge/cms/blob/main/README.md#navigation) will jump to the first item in a given list. E.g. `cms next -a` will cycle through the agent queue based on priority. \+ git work tree ops hooked into tmux nav ( see README.md) full session restore coming soon."
- **Top commenter:** `u/blluecalx`

- **Thread topics:**
  - `cms` usage modes:
    - `cms` = everything
    - `cms -p` = projects
    - `cms -a` = agents only
    - `cms -awsp` = agents, worktrees, sessions, projects
  - Ranking/ordering behavior:
    - agents sorted by status priority: `waiting`, `completed`, `idle`, `working`
    - projects/worktrees sorted by `recent`
    - section order follows flag order
  - Headless navigation:
    - `cms next -a` cycles through the agent queue
  - Integration with tmux navigation:
    - git worktree operations are hooked into tmux nav
    - full session restore is planned
  - Comparison to other agent/workflow tooling:
    - similar concepts appear in other tmux-based or TUI monitoring tools

- **Notable replies / opinion clusters:**
  - **Positive/curious:** u/gavraz says it’s “very cool,” likes the minimalist search-and-jump approach, and shares a related project (`recon`).
  - **Technical discussion:** u/blluecalx explains their mental model:
    - session = project
    - window = worktree
    - pane = process / agent
    - they use live filtered pane search by agent status as the main navigation mode
    - they mention challenges around scraping status updates from Claude/Codex code and smoothing status transitions
  - **Humor / skepticism:** u/sultanmvp jokes that tmux should be renamed “agentmux” or “cmux,” then expands into criticism that many of these posts are repetitive, self-promotional, and centered on the same agent/worktree/fzf patterns.
  - **Pushback:** u/ReferenceBoring7865 argues the recent examples are not the same and that they bring new ideas.

- **What stands out about the tool:**
  - It is not just a session switcher; it is explicitly **status-aware** for agents.
  - It emphasizes **fuzzy-find → jump** as the core interaction model.
  - It introduces a consistent mapping of tmux concepts to workflow concepts.
  - It aims to surface the “most useful” item first, especially for agent queues.

### Assessment
This is a medium-to-high durability thread for anyone tracking tmux-based workflow tools or agent orchestration patterns, but it is time-sensitive because it references a specific repo state, current agent tooling, and ongoing “full session restore coming soon” plans. The content type is mixed: mostly a tool announcement with a technical/social discussion around usage patterns and broader skepticism about the trend. Density is medium-high because the top comment and follow-up reply include concrete flags, status order, conceptual mappings, and implementation notes. Originality is mixed: the post is a primary announcement of `cms`, while the thread includes commentary, comparison, and criticism from other users. This is best used as a skim-once or refer-back reference for discovering the repo and understanding the tool’s intended workflow. Scrape quality is good overall for text content, though the linked GIF, repo contents, and full README are not captured, so some implementation details may be missing.
