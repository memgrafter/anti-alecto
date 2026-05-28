---
url: https://www.reddit.com/r/ClaudeCode/comments/1rsur5s/i_built_a_claude_code_skill_that_applies/
title: 'I built a Claude Code skill that applies Karpathy''s autoresearch to any task ... not just ML : r/ClaudeCode'
scraped_at: '2026-04-19T21:57:39Z'
word_count: 2339
raw_file: raw/2026-04-19_i-built-a-claude-code-skill-that-applies-karpathy-s-autoresearch-to-any-task-not_1d7e7aba.txt
tldr: 'A r/ClaudeCode thread about u/uditgoenka’s open-source autoresearch skill for Claude Code: define a goal, metric, and verify command, then let Claude iterate with git commits and auto-reverts; the top commenters praised the examples and raised concerns about budgeting, metrics, and long-running loop safety.'
key_quote: Every improvement stacks. Every failure auto-reverts. Progress logged in TSV. You wake up to results.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- u/uditgoenka
- u/jarec707
- u/Overstay3461
- u/Business-Weekend-537
- u/Relative_Register_79
- u/Mishuri
- u/andruchs1
- u/r_rocks
- Karpathy
tools:
- Claude Code
- MCP
- Git
libraries: []
companies:
- Reddit
- Snowflake
tags:
- claude-code
- autonomous-agents
- llm-workflows
- software-optimization
- open-source-tools
---

### TL;DR
A r/ClaudeCode thread about u/uditgoenka’s open-source **autoresearch** skill for Claude Code: define a goal, metric, and verify command, then let Claude iterate with git commits and auto-reverts; the top commenters praised the examples and raised concerns about budgeting, metrics, and long-running loop safety.

### Key Quote
“Every improvement stacks. Every failure auto-reverts. Progress logged in TSV. You wake up to results.”

### Summary
- **Top comment (verbatim):** “You did a great job providing use case examples with code. Bravo!”
- **Top commenter:** `u/jarec707`
- **Thread topics:**
  - Generalizing Karpathy-style autoresearch beyond ML into arbitrary measurable tasks
  - Safety/cost concerns: token usage, monthly limits, and whether loops can run “forever”
  - How to define the right metric and verification command for non-obvious goals
  - Using MCP servers, hooks, and multi-agent setups for database/analytics-driven optimization
  - Self-improvement / recursive use cases, including improving the skill itself

- **Original post by u/uditgoenka:**
  - Introduces a **Claude Code skill** called **autoresearch** that turns a goal into an autonomous improvement loop.
  - Core loop:
    - define a **goal**
    - define a **mechanical metric**
    - define a **verification command**
    - Claude makes **one atomic change**
    - **git commit**
    - **verify**
    - **keep if improved**
    - **revert if not**
    - repeat indefinitely until interrupted
  - Claims it can work for measurable targets like:
    - test coverage
    - bundle size
    - Lighthouse scores
    - API response time
    - SEO scores
    - ad copy quality
    - SQL query optimization
  - Says it can combine with **MCP servers** for database- or analytics-driven loops.
  - States it is **MIT licensed** and open source: `github.com/uditgoenka/autoresearch`
  - Invites feedback and PRs.

- **Positive reactions / validation:**
  - Multiple commenters praised the concept and the use-case examples.
  - Several said they had built similar loop-based systems themselves.
  - Some commenters described it as especially useful for overnight runs and iterative improvement.

- **Budget / token-limit concern:**
  - `u/Business-Weekend-537` asked for a way to cap spending or stop at Claude Code monthly-plan limits.
  - OP replied that you can define goals and it will stop when it achieves them, and later said to use a regular **Max account**.
  - Other replies suggested hooks for checking limits.

- **Hard part: defining metrics and verification:**
  - `u/Relative_Register_79` noted that the repo assumes you already know your metric and verify command, which is often the hardest part.
  - They proposed a **meta-layer**:
    - human intent layer (“I want faster API responses”)
    - orchestration layer that infers the metric and verify command
    - then the existing autoresearch loop runs
  - `u/campionbouy123T` asked how much it would cost to use on educational-material improvement; replies pointed out that the result must be measurable first.
  - `u/HeoJunKorea` linked to Snowflake’s AI agent evaluation framework.

- **Skepticism / limitations:**
  - `u/Mishuri` argued the approach won’t work unless long-horizon behavior is enforced more robustly than prompting alone.
  - `u/ApprehensiveChip8361` said these loops can burn tokens and get stuck on hard bugs, making human intervention/pragmatism necessary after enough failed attempts.
  - `u/andruchs1` questioned whether short-horizon testing makes sense for SEO or ads; OP replied that you can use longer intervals and that it depends on scale and use case.

- **Extensions and follow-on ideas:**
  - `u/Only_Management_1010` suggested adding an analysis step to inspect training dynamics and shared a related repo.
  - `u/r_rocks` proposed a `/autoresearch:plan` helper to translate a textual goal into scope/metric/verify; OP responded that **v1.0.2** had been shipped and linked the release.
  - `u/Delicious-Storm-5243` described a complementary safety-focused system (“Ouro Loop”) with invariants, danger zones, and autonomous remediation.
  - `u/them`? No—thread also includes a commenter asking about context-window management, but no detailed answer is shown in the capture.

- **OP’s overall stance in replies:**
  - Confident that the approach works “great” if you define the goal and measurement clearly.
  - Encourages trying the repo and using the examples in the README.
  - Emphasizes that it’s meant to be practical, open source, and extensible.

### Assessment
This is a **mixed** social/thread capture centered on a tool announcement. Durability is **medium**: the core idea of metric-driven autonomous iteration is fairly timeless, but the specifics are tied to Claude Code, current repo versions, and plan limits. Density is **high** because the capture includes the original pitch plus a long slice of commenter feedback, objections, and implementation ideas. Originality is mostly **primary-source plus commentary**: it contains OP’s own product description and real thread responses. It’s best used as a **refer-back** reference if you want to recall the concept, see community concerns (especially budgeting and metric-definition), or find the linked repo and release notes. Scrape quality is **good** for text and comment structure; however, it appears to omit any linked images/previews and does not include the full repository content or code examples from the README.
