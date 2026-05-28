---
url: https://www.ycombinator.com/launches/Pdc-openspec-the-spec-framework-for-coding-agents
title: 'Launch YC: OpenSpec: The Spec Framework for Coding Agents | Y Combinator'
scraped_at: '2026-04-19T06:53:58Z'
word_count: 466
raw_file: raw/2026-04-19_launch-yc-openspec-the-spec-framework-for-coding-agents-y-combinator_65d4c548.txt
tldr: OpenSpec is an open-source spec framework that captures what you're building, why, and how, before your coding agent writes a line of code.
key_quote: Generating code is now cheap. Correctness is still expensive.
durability: medium
content_type: announcement
density: medium
originality: primary
reference_style: skim-once
scrape_quality: good
people:
- Tabish
tools:
- Claude Code
- Cursor
- Windsurf
- Copilot
libraries: []
companies:
- OpenSpec
- Fission-AI
tags:
- ai-assisted-development
- coding-agents
- software-specification
- developer-workflow
- product-launch
---

### TL;DR
OpenSpec is an open-source “spec layer” for AI-assisted coding that keeps requirements, design, and implementation plans in Markdown inside the repo so coding agents stay aligned across sessions and teams.

### Key Quote
“Generating code is now cheap. Correctness is still expensive.”

### Summary
- **What it is**
  - OpenSpec is an open-source spec framework for coding agents.
  - It adds an `openspec/` folder to a repository with:
    - `openspec/specs/`: a living documentation library of how the system works, organized by capability.
    - `openspec/changes/`: a workflow for each feature with a proposal, design, implementation tasks, and spec deltas.
  - When a feature ships, the deltas merge back into the spec library so the documentation evolves with the codebase.

- **Core problem it claims to solve**
  - The bottleneck in AI-assisted development is not model capability, but **underspecification**.
  - Teams struggle because they can’t reliably ensure AI-generated code matches intended requirements, edge cases, and architecture.
  - OpenSpec is positioned as the “workspace” where humans and agents align on what is being built, why, and how.

- **How it works**
  - Everything is stored as Markdown and checked into Git.
  - Specs are always available to both humans and coding agents.
  - Integrates with **20+ AI tools**, including:
    - Claude Code
    - Cursor
    - Windsurf
    - Copilot
  - Supports slash commands and skills to help create, evolve, and manage specs.

- **Stated benefits**
  - “Your thinking persists” across chats and sessions, unlike ephemeral plan mode.
  - Enables iterative spec evolution over time.
  - Makes changes cheaper to reason about in Markdown than in code.
  - Promotes **plan review** over **code review**, since specs are easier to read than large diffs and force clearer thinking.

- **Who is behind it / motivation**
  - The speaker is Tabish, founder of OpenSpec.
  - He says the idea came from experience as a team lead at a quantum computing startup, where managing coding agents resembled managing a team.
  - The message: coding agents can’t read your mind, so teams need a shared source of truth.

- **Call to action / audience**
  - Suggested for teams already using AI coding tools but struggling with alignment.
  - Quick-start claim: setup takes less than a minute.
  - GitHub repo: `github.com/Fission-AI/OpenSpec`
  - Website: `openspec.dev`
  - Contact: `tabish@openspec.dev`
  - They are also seeking engineering teams with large or multi-repo codebases to help shape “Workspaces” for deeper collaboration and multi-repo planning.

### Assessment
This is a **mixed** launch/announcement and product pitch with some conceptual framing. **Durability: medium** — the underlying idea of using specs to align humans and coding agents is fairly timeless, but the specific tool integrations, GitHub stars count, and launch context are version/current-state dependent. **Density: medium** — it contains a lot of concrete product claims and structure, but it’s still promotional rather than deeply technical. **Originality: primary source** — this is the founder’s own product announcement and positioning, not a third-party review. **Reference style: skim-once** unless you’re evaluating the product for adoption, in which case it becomes **refer-back**. **Scrape quality: good** — the main launch text and calls to action are captured, with no obvious missing code blocks or major sections, though this appears to be a short launch page rather than a full technical doc.
