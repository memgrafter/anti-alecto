---
url: https://github.com/ClaytonFarr/ralph-playbook
title: 'ClaytonFarr/ralph-playbook: A comprehensive guide to running autonomous AI coding loops using Geoff Huntley''s Ralph methodology. View as formatted guide below 👇'
scraped_at: '2026-04-12T07:44:35Z'
word_count: 10227
raw_file: raw/2026-04-12_claytonfarr-ralph-playbook-a-comprehensive-guide-to-running-autonomous-ai-coding_cd521f27.txt
tldr: 'A detailed, opinionated playbook for running “Ralph” autonomous AI coding loops: split work into specs, generate a prioritized implementation plan, then let a fresh-context bash loop repeatedly pick one task, implement it, validate it with backpressure, commit, and restart.'
key_quote: “Ralph should be doing _all_ of the work, including decided which planned work to implement next and how to implement it.”
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: deep-study
scrape_quality: good
people:
- Clayton Farr
- Geoff Huntley
- Matt Pocock
- Ryan Carson
- Terry
- Blackroses
- Jake Cukjati
- Thariq
- Jason Cohen
tools:
- claude
- loop.sh
- envsubst
- git
- gh
- stream-json
libraries:
- Claude Code
companies:
- GitHub
- Anthropic
- Fly
- E2B
- Gemini
- OpenAI
tags:
- autonomous-coding
- ai-workflows
- prompt-engineering
- software-development
- planning
---

### TL;DR
A detailed, opinionated playbook for running “Ralph” autonomous AI coding loops: split work into specs, generate a prioritized implementation plan, then let a fresh-context bash loop repeatedly pick one task, implement it, validate it with backpressure, commit, and restart.

### Key Quote
“Ralph should be doing _all_ of the work, including decided which planned work to implement next and how to implement it.”

### Summary
- This GitHub repo is a practical guide for applying Geoff Huntley’s “Ralph” methodology to autonomous AI-assisted coding.
- The author says recent posts/videos and community overviews helped, but they dug into Geoff’s original material to build a more precise playbook.
- The core framing is:
  - **Phase 1: Define requirements** in conversation, using JTBD (“Jobs to Be Done”) and topic-level specs.
  - **Phase 2/3: Run the Ralph loop** in one of two modes:
    - **PLANNING**: compare specs to code and generate/update `IMPLEMENTATION_PLAN.md`
    - **BUILDING**: implement the highest-priority task from the plan, validate, commit, and update the plan as a side effect
- The workflow is intentionally simple and file-based:
  - `specs/*.md` = source-of-truth requirements
  - `IMPLEMENTATION_PLAN.md` = mutable prioritized task list
  - `PROMPT.md` / `PROMPT_plan.md` / `PROMPT_build.md` = loop instructions
  - `AGENTS.md` = brief operational run/build notes loaded every iteration
  - `loop.sh` = a dumb outer bash loop that repeatedly feeds the prompt to Claude
- A major principle is that **context is everything**:
  - Use the main agent as a scheduler
  - Spawn subagents for research and file work
  - Keep each loop iteration narrow so the model stays in the “smart zone”
  - Prefer brevity and Markdown over JSON for efficiency
- The playbook emphasizes **steering by patterns and backpressure**:
  - “Upstream” steering: deterministic setup, known files, existing code patterns
  - “Downstream” steering: tests, typechecks, lints, builds, and other gates that reject bad work
- A key operational idea is to **let Ralph self-correct**:
  - The plan is disposable
  - If the loop goes off track, regenerate the plan instead of forcing it
  - Add guardrails only after observing failure modes
- Safety is treated seriously:
  - Autonomous runs require `--dangerously-skip-permissions`
  - You should use isolated environments with minimal secrets and restricted network access
  - Stop/revert escape hatches include Ctrl+C and `git reset --hard`
- The loop mechanics are intentionally simple:
  - `while :; do cat PROMPT.md | claude ; done`
  - `IMPLEMENTATION_PLAN.md` persists between iterations and acts as shared state
  - Each iteration starts with fresh context and picks the next most important task
- The repo includes a more elaborate example `loop.sh`:
  - supports `plan` vs `build`
  - can cap iterations
  - pushes after each task
  - optionally uses `stream-json` and a parser for readable streamed output
- The document also describes the repository layout and role of each file:
  - `loop.sh`
  - `PROMPT_build.md`
  - `PROMPT_plan.md`
  - `AGENTS.md`
  - `IMPLEMENTATION_PLAN.md`
  - `specs/`
  - `src/`
  - `src/lib/`
- There is a substantial “Enhancements?” section proposing future improvements, including:
  - use Claude’s AskUserQuestionTool during planning
  - derive test requirements directly from acceptance criteria
  - add non-deterministic LLM-as-judge backpressure for subjective outputs
  - support work-scoped branches and plans
  - connect JTBDs to story maps and SLC (“Simple, Lovable, Complete”) releases
  - add specs-audit mode
  - reverse-engineer brownfield codebases into specs before planning
- The enhancement ideas are presented as exploratory and not yet proven, with several detailed prompt/script templates included.

### Assessment
This is a high-density, highly actionable reference-style guide with a clear opinionated workflow and lots of concrete implementation detail, commands, and prompt templates. Its durability is **medium**: the core ideas about specs, planning, looped execution, backpressure, and context management are fairly timeless, but several specifics are tied to Claude CLI behavior, current model names, December 2025 references, and the author’s evolving experimentation. The content type is **mixed**, leaning tutorial/reference with substantial commentary and design opinion. It appears to be **original synthesis** rather than a simple aggregation, based on the author’s direct experience and proposed refinements. For later use, this is best treated as a **refer-back** or **deep-study** reference depending on whether you’re adopting the workflow. Scrape quality is **good** overall: the text is comprehensive and includes large code blocks and templates, though image assets are referenced rather than embedded in a way that adds much searchable detail.
