---
url: https://github.com/ghuntley/how-to-ralph-wiggum
title: 'ghuntley/how-to-ralph-wiggum: The Ralph Wiggum Technique—the AI development methodology that reduces software costs to less than a fast food worker''s wage.'
scraped_at: '2026-04-12T07:44:18Z'
word_count: 8157
raw_file: raw/2026-04-12_ghuntley-how-to-ralph-wiggum-the-ralph-wiggum-technique-the-ai-development-metho_d0a5c34a.txt
tldr: 'A GitHub repo/article by Clayton Farr that distills Geoffrey Huntley’s “Ralph Wiggum Technique” into a practical playbook: use a fresh-context bash loop (`while :; do cat PROMPT.md | claude ; done`), keep the evolving plan on disk, and steer the agent with prompt files, specs, and tests/backpressure.'
key_quote: One mechanism for everything; clean file I/O; easy stop/restart
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: deep-study
scrape_quality: good
people:
- Clayton Farr
- Geoffrey Huntley
- Matt Pocock
- Ryan Carson
- Jason Cohen
- Thariq
tools:
- claude
- amp
- codex
- opencode
- gh
- AskUserQuestionTool
libraries: []
companies:
- GitHub
- Claude
- Fly
- E2B
- Google
- OpenAI
tags:
- ai-development
- agent-workflows
- prompt-engineering
- software-automation
- test-backpressure
---

### TL;DR
A GitHub repo/article by Clayton Farr that distills Geoffrey Huntley’s “Ralph Wiggum Technique” into a practical playbook: use a fresh-context bash loop (`while :; do cat PROMPT.md | claude ; done`), keep the evolving plan on disk, and steer the agent with prompt files, specs, and tests/backpressure.

### Key Quote
"One mechanism for everything; clean file I/O; easy stop/restart"

### Summary
- This repository is titled **`ghuntley/how-to-ralph-wiggum`** and presents **“The Ralph Playbook”**, a write-up dated **December 2025** that tries to reverse-engineer Geoffrey Huntley’s Ralph workflow from recent videos and the original Ralph post.
- The central claim is that Ralph is **not just “a loop that codes”**; it is a **pipeline**:
  - **Phase 1: Define Requirements** in an LLM conversation
  - **Phase 2 / 3: Run Ralph Loop** in either:
    - **PLANNING** mode: compare `specs/*` against code and produce/update `IMPLEMENTATION_PLAN.md`
    - **BUILDING** mode: implement from the plan, run tests, commit, and update the plan as a side effect
- The article repeatedly emphasizes the core operating model:
  - **fresh context every iteration**
  - **one task per loop**
  - **shared state lives on disk** in `IMPLEMENTATION_PLAN.md`
  - each loop reloads the same context files, especially `PROMPT.md` and `AGENTS.md`
- The exact minimal outer loop quoted in the article is:
  - `while :; do cat PROMPT.md | claude ; done`
- The plan for the workflow is highly structured:
  - **JTBD** = job to be done
  - **Topic of concern** = a distinct aspect of a JTBD
  - **Spec** = one markdown file per topic, under `specs/FILENAME.md`
  - **Task** = work item derived from comparing specs to code
- It gives a concrete concept map:
  - **1 JTBD → multiple topics**
  - **1 topic → 1 spec**
  - **1 spec → multiple tasks**
- The article’s main steering ideas are:
  - **Context is everything**: don’t waste main-agent context; use subagents as memory extension
  - **Simplicity and brevity win**: fewer parts, less verbose input, better determinism
  - **Prefer Markdown over JSON** for work tracking
  - **Steer upstream** with deterministic setup and existing code patterns
  - **Steer downstream** with tests, typechecks, lints, builds, and other backpressure
- It stresses that Ralph should be left alone to do the work:
  - the operator’s job is to manage the environment, not micromanage each step
  - the plan is **disposable** and can be regenerated whenever it becomes stale or wrong
- The loop mechanics section explains why the bash loop works:
  - the agent reads the prompt
  - performs one task
  - updates `IMPLEMENTATION_PLAN.md`
  - commits
  - exits
  - the shell loop restarts it in a fresh context
- It includes an expanded example `loop.sh` that adds:
  - **mode selection** (`plan` vs build)
  - **max iterations**
  - **git push after each iteration**
  - Claude CLI flags like `-p`, `--dangerously-skip-permissions`, `--output-format=stream-json`, `--model opus`, and `--verbose`
- The file layout section anchors the workflow in concrete files:
  - `loop.sh`
  - `PROMPT_build.md`
  - `PROMPT_plan.md`
  - `AGENTS.md`
  - `IMPLEMENTATION_PLAN.md`
  - `specs/`
  - `src/`
  - `src/lib/`
- A large “Enhancements?” section explores possible extensions to the Ralph workflow, including:
  - **AskUserQuestionTool** for planning interviews
  - **acceptance-driven backpressure**
  - **LLM-as-judge / non-deterministic backpressure**
  - **work branches with scoped plans**
  - **JTBD → story map → SLC release** thinking
- The write-up is very implementation-oriented and includes example prompt templates, guardrails, and code blocks rather than a conceptual essay.

### Assessment
This is a **mixed reference/tutorial** with high practical density and strong operational specificity. Its durability is **medium**: the underlying ideas about context management, looped execution, plans as shared state, and test backpressure are fairly durable, but many details are tied to specific tooling and current Claude CLI assumptions, plus the dated **December 2025** framing makes it somewhat event/version sensitive. The content is **original-ish synthesis/commentary** on Huntley’s technique rather than primary research or official docs, because it reorganizes and interprets the approach into a “playbook” instead of presenting first-party product documentation. It is best used as a **deep-study / refer-back** piece if you want to adopt or evaluate the Ralph workflow in practice. **Findability is high**: the exact repo/title, “The Ralph Playbook” framing, the `while :; do cat PROMPT.md | claude ; done` loop, and the PLANNING vs BUILDING split are distinctive anchors that make this easy to recognize later. **Scrape quality is good** for the article body and code blocks; the main missing pieces are the externally hosted images/links and any content behind linked pages, but the core nested sections and examples are present in full.
