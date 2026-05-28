---
url: https://github.com/psi-oss/get-physics-done
title: 'psi-oss/get-physics-done: The first open-source agentic AI physicist, by Physical Superintelligence PBC (PSI).'
scraped_at: '2026-04-19T08:07:26Z'
word_count: 5082
raw_file: raw/2026-04-19_psi-oss-get-physics-done-the-first-open-source-agentic-ai-physicist-by-physical-_4f11498b.txt
tldr: Get Physics Done (GPD) is a Python/Node bootstrap package that installs a structured, agentic physics-research workflow into supported AI terminal runtimes like Claude Code, Codex, Gemini CLI, and OpenCode.
key_quote: '“GPD helps turn a research question into a structured workflow: scope the problem, plan the work, derive results, verify them, and package the output.”'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Physical Superintelligence PBC
- C. Ferko
- J. Halverson
- V. Jejjala
- B. Robinson
tools:
- Claude Code
- Codex
- Gemini CLI
- OpenCode
- npx
- uv
libraries: []
companies:
- Physical Superintelligence PBC
- PSI
tags:
- physics-research
- agentic-ai
- cli-tools
- workflow-automation
- scientific-writing
---

### TL;DR
Get Physics Done (GPD) is a Python/Node bootstrap package that installs a structured, agentic physics-research workflow into supported AI terminal runtimes like Claude Code, Codex, Gemini CLI, and OpenCode.

### Key Quote
“GPD helps turn a research question into a structured workflow: scope the problem, plan the work, derive results, verify them, and package the output.”

### Summary
- **What it is**
  - An open-source agentic AI system for physics research from **Physical Superintelligence PBC (PSI)**.
  - Not a standalone app; it installs commands into supported runtimes.
  - Claims to be “the first open-source agentic AI physicist.”

- **Supported runtimes**
  - **Claude Code**
  - **Codex**
  - **Gemini CLI**
  - **OpenCode**
  - Each runtime gets its own command prefix and help/start/tour/new-project/resume commands.

- **Installation / prerequisites**
  - Main install command: `npx -y get-physics-done`
  - Source checkout development path: `uv sync --dev` then `uv run gpd --help`
  - Requires:
    - **Node.js 20+**
    - **Python 3.11+** with `venv`
    - Network access to npm/GitHub
    - One supported runtime
    - API access for the chosen model provider
  - Ordinary installs are pinned to matching tagged releases; `--upgrade` pulls unreleased GitHub `main`.

- **Intended use**
  - Designed for **long-horizon physics research projects** needing:
    - structured research memory
    - multi-step analytical work
    - numerical studies
    - manuscript writing/review
    - explicit verification
  - Emphasizes **scientific rigor and critical thinking over agreeability**.

- **Core workflow**
  - GPD organizes work into four stages:
    1. **Formulate** — clarify scope, assumptions, notation, verification targets
    2. **Plan** — create phased roadmap with tasks, dependencies, success criteria
    3. **Execute** — run specialist agents for derivations, numerical checks, literature, writing
    4. **Verify** — check dimensional consistency, limiting cases, symmetry, conservation laws, numerical stability
  - Produces artifacts such as:
    - `PROJECT.md`
    - `REQUIREMENTS.md`
    - `ROADMAP.md`
    - `STATE.md`
    - `.tex` derivations
    - `.py` verification scripts
    - figures

- **Project structure**
  - Hierarchy:
    - Project → Milestone → Phase → Plan → Task
  - Execution is grouped into **waves** based on dependencies.
  - Phase numbers continue across milestones rather than resetting.

- **Command surface**
  - Typical post-install sequence:
    - `help -> start -> tour -> new-project / map-research -> resume-work`
  - Core commands include:
    - `start`, `tour`
    - `new-project`, `new-project --minimal`, `map-research`
    - `resume-work`, `pause-work`, `suggest-next`
    - `discuss-phase`, `plan-phase`, `execute-phase`, `verify-work`
    - `write-paper`, `peer-review`, `respond-to-referees`, `arxiv-submission`
    - `settings`, `set-profile`, `set-tier-models`, `tangent`, `branch-hypothesis`
  - Also includes validation, observability, tracing, cost reporting, and manuscript build commands like `gpd validate ...`, `gpd observe ...`, `gpd trace ...`, and `gpd paper-build`.

- **Model profiles / tiers**
  - Maps runtime-specific models into three tiers:
    - `tier-1` = highest capability
    - `tier-2` = balanced default
    - `tier-3` = fastest / most economical
  - Profiles include:
    - `deep-theory`
    - `numerical`
    - `exploratory`
    - `review`
    - `paper-writing`

- **Paper / publication workflow**
  - Has a structured publication lane with explicit manuscript roots and intake/provenance handling.
  - Supports writing papers, peer review, referee response, and arXiv packaging.
  - Mentions review/publication contracts and preflight validation commands.

- **Documentation and UX**
  - Strong emphasis on onboarding:
    - beginner hub in `docs/README.md`
    - runtime-specific guides in `docs/`
  - README separates beginner guidance from advanced reference surfaces.

- **Other notable details**
  - Includes citation instructions with `CITATION.cff`.
  - Lists example papers that cite or acknowledge GPD.
  - Licensed under **Apache 2.0**.

### Assessment
This is a **mixed** reference/tutorial README with a lot of operational detail. Durability is **medium**: the conceptual workflow and project structure are fairly stable, but install commands, runtime support, and version details are tied to current tooling and could change. Density is **high**—it’s packed with commands, flags, workflows, and path-specific behavior. Originality is mostly **primary source** because it documents the project’s own software and conventions. It’s best used as **refer-back** material rather than a one-time skim, especially for install, command syntax, and workflow decisions. Scrape quality is **good**: the README content appears largely complete, including code blocks, tables, and major sections, though embedded images/media are not inspectable from the text alone.
