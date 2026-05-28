---
url: https://hankweave.southbridge.ai/concepts/hanks/
title: Hanks – Hankweave Documentation
scraped_at: '2026-04-19T07:51:44Z'
word_count: 1981
raw_file: raw/2026-04-19_hanks-hankweave-documentation_cb74d816.txt
tldr: Hankweave “hanks” are declarative AI workflow programs made of sequential codons, with explicit context-flow, model, and checkpoint rules designed to make agent runs reproducible and rollback-friendly.
key_quote: A hank is a declarative AI program.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- hankweave
libraries:
- zod
companies: []
tags:
- ai-workflows
- declarative-programming
- configuration
- checkpoints
- agent-orchestration
---

### TL;DR
Hankweave “hanks” are declarative AI workflow programs made of sequential codons, with explicit context-flow, model, and checkpoint rules designed to make agent runs reproducible and rollback-friendly.

### Key Quote
“A hank is a declarative AI program.”

### Summary
- **Core concept**
  - A **hank** is the top-level declarative program in Hankweave.
  - It is a **sequence of codons** executed in order, defining:
    - which models run
    - how context flows between steps
    - how checkpoints are created
  - The design goal is **reproducibility**: the same hank should produce the same results for the same inputs.

- **Declarative, not procedural**
  - Hanks describe **what should happen**, not how to implement it.
  - There are **no conditionals or traditional loops** in hanks, though Hankweave provides a controlled **Loops** primitive.

- **File structure**
  - Hanks are defined in `hank.json`.
  - Top-level sections include:
    - `meta` — optional metadata (`name`, `version`, `description`, `author`)
    - `overrides` — optional runtime settings overrides
    - `requirements` — optional required environment variables
    - `globalSystemPromptFile` / `globalSystemPromptText` — optional prompts applied to all codons
    - `hank` — required codon array
  - A minimal hank can be just a `hank` array with one codon.
  - The root codon array may also be named **`strand`**, but that is a legacy term; **`hank`** is preferred.

- **Environment requirements**
  - The `requirements.env` section declares required environment variables.
  - Hankweave validates them during `--validate` and startup.
  - It fails fast if variables are missing.
  - `HANKWEAVE_` prefixes are automatically supported, so `API_KEY` can be satisfied by either `API_KEY` or `HANKWEAVE_API_KEY`.

- **Global system prompts**
  - `globalSystemPromptFile` and `globalSystemPromptText` apply to **all codons**.
  - Useful for global conventions, coding standards, or safety rules.
  - Global prompts are **prepended** before codon-specific append prompts.

- **Execution and checkpoints**
  - Codons run **sequentially from top to bottom**.
  - Each codon must finish before the next begins.
  - Between codons, Hankweave creates a **checkpoint** as a git commit, enabling rollback to prior states.

- **Context flow via `continuationMode`**
  - `fresh`
    - starts a new conversation
    - sees only its own prompt and current files
    - useful for self-contained tasks or model switching
    - described as a **“context firewall”**
  - `continue-previous`
    - resumes the previous conversation
    - useful when the next codon depends on what the last one just did
    - only works if the **model is the same as the previous codon**
  - If a codon is skipped, `continue-previous` chains to the last codon that actually ran and produced a session ID.

- **Template variables**
  - Codon prompts can include runtime-expanded variables like:
    - `<%EXECUTION_DIR%>`
    - `<%DATA_DIR%>`
  - This makes hanks portable and avoids hardcoded paths.

- **Five-layer configuration precedence**
  - Configuration is resolved by deep merge across five layers, highest to lowest:
    1. CLI arguments
    2. Environment variables prefixed with `HANKWEAVE_RUNTIME_`
    3. Hank overrides in `hank.json`
    4. Runtime config in `hankweave.json`
    5. Built-in defaults
  - Most settings merge deeply.
  - **Model** is special:
    - In CLI/env/runtime config, it forces the model for all codons.
    - In hank overrides or built-in defaults, it acts as a fallback only for codons without their own model.

- **Mixing models**
  - Different codons can use different models to balance cost and capability.
  - But if you switch models, you must use `fresh` because sessions cannot be shared across models.
  - Example pattern:
    - `haiku` for analysis
    - `sonnet` for generation
    - `opus` for review

- **Example pipeline**
  - A realistic example processes CSV data into documented TypeScript schemas.
  - Phases:
    - `observe` — inspect data with a cheaper model
    - `schema` — generate schemas
    - `refine` — loop up to 3 iterations to validate/fix schemas
    - `document` — generate docs from validated schemas
  - The example demonstrates:
    - `rigSetup`
    - `checkpointedFiles`
    - `outputFiles`
    - a loop codon with `terminateOn.iterationLimit`

- **When to split codons**
  - Split when:
    - different models fit different phases
    - you want rollback points
    - the conversation would get noisy
    - the task has distinct stages
  - Keep a single codon when:
    - conversational memory is required
    - the task is atomic and splitting would hurt it

- **Common mistakes**
  - Don’t use `continue-previous` after switching models.
  - Don’t cram an entire workflow into one codon.
  - Don’t rely on conversation context when files are the real source of truth; for validation, use `fresh` and inspect files directly.

- **Related docs**
  - Links out to:
    - Codons
    - Loops
    - Rigs
    - Budgets
    - Checkpoints
    - Configuration Reference
  - Next steps suggest reading:
    - Building a Hank
    - Loops
    - Debugging

### Assessment
This is a **reference/documentation** page with a **high** durability level for the core concepts, though some configuration details may evolve with Hankweave versions. The content is a **mixed** technical reference and tutorial-style guide, dense with concrete fields, examples, and precedence rules. It appears to be a **primary source** from the project documentation rather than commentary or synthesis. It’s best used as a **refer-back** resource when authoring or debugging hanks, though the overview is also good enough for a skim-once introduction. **Scrape quality is good**: the page content, tables, examples, and section structure are present, with no obvious missing code blocks or major omissions.
