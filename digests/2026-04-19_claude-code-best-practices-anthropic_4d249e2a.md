---
url: https://www.anthropic.com/engineering/claude-code-best-practices
title: Claude Code Best Practices \ Anthropic
scraped_at: '2026-04-19T03:58:58Z'
word_count: 4958
raw_file: raw/2026-04-19_claude-code-best-practices-anthropic_4d249e2a.txt
tldr: 'Anthropic’s Claude Code best-practices guide says the biggest lever is managing context: give Claude verification, plan before coding on complex tasks, keep prompts and `CLAUDE.md` concise, and use tools like permissions, subagents, hooks, MCP, and parallel sessions to scale safely.'
key_quote: 'Most best practices are based on one constraint: Claude’s context window fills up fast, and performance degrades as it fills.'
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Anthropic
tools:
- Claude Code
- Plan Mode
- auto mode
- CLAUDE.md
- gh
- aws
- gcloud
- sentry-cli
- MCP
- hooks
- SKILL.md
- AskUserQuestion
- Esc
- /rewind
- /clear
- /compact
- /btw
- claude -p
- --output-format json
- --output-format stream-json
- --allowedTools
- claude mcp add
libraries: []
companies:
- Anthropic
tags:
- ai-agents
- prompt-engineering
- developer-workflows
- code-automation
- context-management
---

### TL;DR
Anthropic’s Claude Code best-practices guide says the biggest lever is managing context: give Claude verification, plan before coding on complex tasks, keep prompts and `CLAUDE.md` concise, and use tools like permissions, subagents, hooks, MCP, and parallel sessions to scale safely.

### Key Quote
“Most best practices are based on one constraint: Claude’s context window fills up fast, and performance degrades as it fills.”

### Summary
- **What this page is**
  - A practical docs page for using **Claude Code** effectively.
  - Focuses on workflows for agentic coding, not model theory.
  - Says the guidance is based on Anthropic’s internal teams and broader Claude Code usage.

- **Central principle: context management**
  - Claude Code’s biggest limitation is that its **context window fills quickly**.
  - The page emphasizes that performance degrades as context fills, leading to forgotten instructions and more mistakes.
  - It recommends tracking context usage and reducing token consumption when possible.

- **Give Claude a way to verify its work**
  - The guide calls this the **single highest-leverage** improvement.
  - Best verification sources:
    - tests
    - screenshots
    - expected outputs
    - lint/typecheck/build commands
  - Example pattern:
    - state exact success criteria
    - implement
    - run tests
    - fix failures
  - For UI work, Claude in Chrome can compare screenshots and iterate.

- **Explore first, then plan, then code**
  - Recommended for multi-file or uncertain tasks.
  - Four-phase workflow:
    1. **Explore** in Plan Mode
    2. **Plan** the implementation
    3. **Implement** in Normal Mode
    4. **Commit** with a descriptive message and PR
  - For trivial changes like typos or small renames, skip planning and go straight to implementation.

- **Be specific in prompts**
  - Better prompts name:
    - files
    - scenarios
    - constraints
    - expected behavior
    - existing patterns to follow
  - The docs contrast vague prompts with more actionable ones, such as writing a failing test for a logged-out edge case or tracing git history for an API design.

- **Provide rich content**
  - Good context sources include:
    - `@file` references
    - pasted screenshots/images
    - URLs to docs/API references
    - piped command output like `cat error.log | claude`
    - letting Claude fetch context itself via Bash or MCP tools

- **Configure your environment**
  - **CLAUDE.md**
    - Generated with `/init`
    - Loaded at the start of every conversation
    - Should contain only broadly applicable, high-value repo instructions
    - Suggested content:
      - code style rules
      - bash commands
      - workflow rules
      - required env vars
      - repository etiquette
    - Avoid bloating it with things Claude can infer from code or docs.
  - **Permissions**
    - Use **auto mode**, allowlists, or **sandboxing** to reduce approval friction.
    - Auto mode uses a classifier to block risky actions.
  - **CLI tools**
    - Anthropic recommends using tools like `gh`, `aws`, `gcloud`, and `sentry-cli`.
    - `gh` is highlighted as especially useful for GitHub workflows.
  - **MCP servers**
    - Connect external tools like Notion, Figma, or databases with `claude mcp add`.
  - **Hooks**
    - Deterministic scripts that run at specific workflow points.
    - Useful for actions that must always happen, like linting after edits.
  - **Skills**
    - `SKILL.md` files in `.claude/skills/`
    - Encapsulate domain knowledge or reusable workflows
    - Can be invoked directly, e.g. `/fix-issue 1234`
  - **Custom subagents**
    - Specialized assistants in `.claude/agents/`
    - Useful for isolated tasks like security review
  - **Plugins**
    - Bundle skills, hooks, subagents, and MCP servers into installable units
    - Especially recommended for typed languages and code intelligence

- **Communicate effectively**
  - Ask Claude codebase questions like you would ask a senior engineer.
  - For larger features, have Claude **interview you first** using `AskUserQuestion`, then write a spec to `SPEC.md`.
  - Start a fresh session afterward to implement the spec with clean context.

- **Manage your session**
  - Use feedback loops aggressively:
    - `Esc` to stop Claude
    - `Esc + Esc` or `/rewind` to restore previous states
    - `"Undo that"` to revert changes
    - `/clear` to reset context between unrelated tasks
  - If you’ve corrected Claude more than twice on the same issue, start over with a clearer prompt.
  - Use subagents for investigation to keep the main conversation clean.
  - Rewind creates checkpoints before changes; it is not a substitute for git.
  - `claude --continue` and `--resume` help you pick up old sessions.
  - `/rename` can label sessions meaningfully.

- **Automate and scale**
  - `claude -p "prompt"` runs non-interactively for CI, scripts, and pre-commit hooks.
  - Use `--output-format json` or `stream-json` for structured automation.
  - Parallel sessions can be run via:
    - Claude Code desktop
    - Claude Code on the web
    - agent teams
  - Example workflow:
    - one session writes code
    - another reviews it
  - For large migrations, fan out across files using loops and `--allowedTools`.
  - Auto mode can run unattended with safety checks.

- **Common failure patterns to avoid**
  - **Kitchen sink session** → fix with `/clear`
  - **Repeated corrections** → fix with `/clear` and a better prompt
  - **Over-specified CLAUDE.md** → prune aggressively
  - **Trust-then-verify gap** → always provide tests or other verification
  - **Infinite exploration** → scope investigations or use subagents

- **Overall tone / takeaway**
  - The guide is practical, operational, and strongly opinionated.
  - It treats Claude Code like a collaborator whose quality depends heavily on:
    - context discipline
    - explicit verification
    - good repo setup
    - deliberate session management
    - scaling through automation and parallelism
  - It ends by emphasizing that these are starting points; users should develop their own intuition over time.

### Assessment
This is a **reference/tutorial** page with **high durability** for general agentic-workflow patterns, though some details are version-dependent because it references specific Claude Code features like Plan Mode, auto mode, `/rewind`, MCP, hooks, plugins, and Chrome integration. The content is **high-density** and highly actionable, mostly **primary-source documentation** from Anthropic rather than commentary or synthesis. It’s best used as a **refer-back** resource for Claude Code workflow design, prompt crafting, session management, and repo configuration. Scrape quality is **good**: the page structure, headings, examples, and code blocks are present, though images are not meaningfully captured beyond their placeholders.
