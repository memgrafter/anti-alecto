---
url: https://github.com/Fission-AI/OpenSpec/
title: 'Fission-AI/OpenSpec: Spec-driven development (SDD) for AI coding assistants.'
scraped_at: '2026-04-19T06:53:38Z'
word_count: 837
raw_file: raw/2026-04-19_fission-ai-openspec-spec-driven-development-sdd-for-ai-coding-assistants_1a98f2f8.txt
tldr: OpenSpec is a MIT-licensed CLI/spec framework for AI coding assistants that adds a lightweight, folder-based specification workflow so humans and AI agree on requirements before code is generated.
key_quote: AI coding assistants are powerful but unpredictable when requirements live only in chat history.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- 0xTab
tools:
- OpenSpec
- npm
- pnpm
- yarn
- bun
- nix
- Discord
libraries: []
companies:
- Fission-AI
- GitHub
- AWS
- Kiro
- Spec Kit
tags:
- spec-driven-development
- ai-coding-assistants
- cli-tools
- developer-workflow
- software-documentation
---

### TL;DR
OpenSpec is a MIT-licensed CLI/spec framework for AI coding assistants that adds a lightweight, folder-based specification workflow so humans and AI agree on requirements before code is generated.

### Key Quote
“AI coding assistants are powerful but unpredictable when requirements live only in chat history.”

### Summary
- **What it is**
  - OpenSpec is a spec-driven development (SDD) tool for AI coding assistants.
  - It is distributed as the npm package `@fission-ai/openspec`.
  - The project positions itself as “the most loved spec framework.”

- **Core philosophy**
  - “fluid not rigid”
  - “iterative not waterfall”
  - “easy not complex”
  - “built for brownfield not just greenfield”
  - “scalable from personal projects to enterprises”

- **New workflow / main interaction model**
  - The repo highlights a new “artifact-guided workflow.”
  - Primary command: `/opsx:propose "your idea"`
  - Example lifecycle:
    - `/opsx:propose add-dark-mode`
    - creates `openspec/changes/add-dark-mode/`
    - includes:
      - `proposal.md`
      - `specs/`
      - `design.md`
      - `tasks.md`
    - `/opsx:apply` implements tasks
    - `/opsx:archive` archives completed work to `openspec/changes/archive/...`
  - Additional expanded workflow commands mentioned:
    - `/opsx:new`
    - `/opsx:continue`
    - `/opsx:ff`
    - `/opsx:verify`
    - `/opsx:sync`
    - `/opsx:bulk-archive`
    - `/opsx:onboard`

- **Quick start**
  - Requires **Node.js 20.19.0 or higher**
  - Install globally:
    ```bash
    npm install -g @fission-ai/openspec@latest
    ```
  - Initialize in a project:
    ```bash
    cd your-project
    openspec init
    ```
  - Then instruct the AI with `/opsx:propose <what-you-want-to-build>`
  - Supports multiple package managers / environments:
    - pnpm
    - yarn
    - bun
    - nix

- **Docs structure**
  - `docs/getting-started.md` — first steps
  - `docs/workflows.md` — combos and patterns
  - `docs/commands.md` — slash commands & skills
  - `docs/cli.md` — terminal reference
  - `docs/supported-tools.md` — integrations & install paths
  - `docs/concepts.md` — how it fits together
  - `docs/multi-language.md` — multi-language support
  - `docs/customization.md` — customization

- **Why it exists**
  - The project argues that AI coding assistants become unpredictable when requirements only exist in chat history.
  - OpenSpec adds a lightweight spec layer so teams align on what to build before coding starts.
  - Claimed benefits:
    - agree before you build
    - stay organized with per-change folders
    - update artifacts anytime without rigid phase gates
    - work across 20+ AI assistants via slash commands

- **Comparison claims**
  - **Vs. Spec Kit (GitHub)**:
    - OpenSpec claims to be lighter, less rigid, and easier to iterate with.
    - Spec Kit is described as thorough but heavyweight, with phase gates and more Markdown/Python setup.
  - **Vs. Kiro (AWS)**:
    - OpenSpec claims more flexibility because it works with existing tools rather than locking you into one IDE/model.
  - **Vs. no specs**:
    - OpenSpec presents itself as a way to avoid vague prompts and unpredictable outcomes.

- **Updating / maintenance**
  - Upgrade package with:
    ```bash
    npm install -g @fission-ai/openspec@latest
    ```
  - Refresh project agent instructions with:
    ```bash
    openspec update
    ```

- **Usage guidance**
  - Recommends high-reasoning models, specifically **Opus 4.5** and **GPT 5.2**.
  - Advises maintaining a clean context window for best results.

- **Contribution model**
  - Small fixes can be submitted directly.
  - Larger features/refactors should start as an OpenSpec change proposal.
  - AI-generated code is allowed if tested and verified.
  - PRs with AI-generated code should mention the agent/model used.
  - Development commands:
    - `pnpm install`
    - `pnpm run build`
    - `pnpm test`
    - `pnpm run dev`
    - `pnpm run dev:cli`

- **Telemetry**
  - Collects anonymous usage stats.
  - Only records command names and version.
  - Excludes arguments, paths, content, and PII.
  - Disabled in CI.
  - Opt out via:
    - `export OPENSPEC_TELEMETRY=0`
    - `export DO_NOT_TRACK=1`

- **Other notes**
  - Maintainers/advisors are listed in `MAINTAINERS.md`.
  - License is MIT.
  - The page includes badges for CI, npm version, license, and Discord, plus screenshots/dashboards, though the actual image content is not captured here.

### Assessment
This is a **mixed** content type: part tool documentation, part product pitch, part usage reference. Durability is **medium** because the core SDD concept is fairly stable, but the specific commands, recommended models, Node version requirement, and workflow names are version-dependent and may change. Density is **high**: the page packs installation, workflow examples, comparisons, contribution rules, telemetry, and doc links into a single README. Originality is mostly **primary source** for the project’s own workflow and philosophy, though it also contains marketing-style comparisons. It’s best used as **refer-back** material for setup, command names, and project positioning rather than deep study. Scrape quality is **good** overall: the main README content, commands, and text sections are present, but the visual screenshots/images and linked docs themselves are not included here.
