---
url: https://github.com/zenobi-us/pi-footer/
title: zenobi-us/pi-footer
scraped_at: '2026-04-19T06:48:33Z'
word_count: 949
raw_file: raw/2026-04-19_zenobi-us-pi-footer_b8939e5b.txt
tldr: pi-footer is a plugin for pi that lets you build a configurable footer from provider-fed template pipelines, with built-in model/git/time/context fields, transforms, and extension hooks.
key_quote: A composable footer for [`pi`](https://pi.dev) with provider-driven data and a compiled pipeline renderer.
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- pi
libraries:
- '@zenobius/pi-footer'
companies:
- zenobi-us
tags:
- developer-tools
- command-line
- templating
- plugins
- configuration
---

### TL;DR
`pi-footer` is a plugin for `pi` that lets you build a configurable footer from provider-fed template pipelines, with built-in model/git/time/context fields, transforms, and extension hooks.

### Key Quote
> "A composable footer for [`pi`](https://pi.dev) with provider-driven data and a compiled pipeline renderer."

### Summary
- **What it is**
  - A `pi` extension/package named `@zenobius/pi-footer` for rendering a customizable footer.
  - Emphasizes a pipeline model: template expressions resolve through **context providers** and **transforms**.

- **Core capabilities**
  - Template-based footer rendering with dynamic data.
  - Built-in support for:
    - model info (`model_name`, `model_provider`, context window/usage, thinking mode/level)
    - usage stats (`usage_tokens_read`, `usage_tokens_write`, `usage_cost_usd`, `usage_plan`)
    - git state (`git_branch_name`, `git_worktree_name`, `git_status`, `recent_commits`)
    - filesystem/time (`cwd`, `path`, `time`)
  - Layout features:
    - left/right alignment
    - flex growth
    - separators
  - Debugging:
    - a `/pi-footer debug {expr}` command to inspect pipeline execution.

- **Install / usage**
  - Install with:
    - `pi install @zenobius/pi-footer`
  - Quick-start config file:
    - `~/.pi/agent/pi-footer.json`
  - Reload footer after editing:
    - `/pi-footer reload`

- **Template format**
  - Templates are arrays of rows.
  - Each row can contain strings or objects with layout metadata.
  - Expressions use curly braces, e.g. `{path}` or `{model_context_used | humanise_percent | context_used_color}`.
  - Literal text is supported with `{"static text"}`.
  - Pipelines are parsed once and cached by template string.

- **Transforms**
  - Built-in transforms include:
    - `humanise_time`
    - `humanise_percent` / `humanise_percentage`
    - `humanise_amount`
    - `humanise_number`
    - `round(n)`
    - `clamp(min,max)`
    - `fg('themeColor')`, `bg('themeColor')`
    - `thinking_level_icons('ascii' | 'unicode')`
    - `git_status_icons('ascii' | 'unicode')`
    - `context_used_color` / `model_context_colors`
  - `context_used_color` maps usage to theme colors:
    - `< 50` → success
    - `50..79` → warning
    - `>= 80` → error

- **Example behavior**
  - The advanced example renders a footer with:
    - model/provider and context percentage on the left
    - path plus git worktree/branch on the right
    - a second row with token counts, cost, thinking mode, and plan
  - Demonstrated output:
    - `openai-codex.gpt-4.0 [200k:64%] ... [my-worktree:main]`
    - `ctx:128,400 in:110,002 out:18,398 $:0.2321 mode:normal plan:pro`

- **Configuration and schema**
  - JSON Schema is published at:
    - `config.schema.json`
    - `resolved-config.schema.json`
  - Schemas are generated from `src/services/config/schema.ts` using:
    - `mise run generate-schema`

- **Extension API**
  - Other extensions can register:
    - custom context providers via `Footer.registerContextValue(...)`
    - custom transforms via `Footer.registerContextTransform(...)`
  - The README gives a TypeScript example that adds a `custom_value` provider and a `custom_format` transform.

- **Commands**
  - `/pi-footer` — help
  - `/pi-footer providers` — list registered providers
  - `/pi-footer debug {expr}` — inspect expression execution
  - `/pi-footer reload` — reload config and rerender
  - `/pi-footer <subcommand> [args]` — run extension-registered subcommands

### Assessment
This is a high-durability technical reference for configuring and extending a `pi` footer, though some specifics are tied to the current `pi` ecosystem and package/version conventions. It is a **reference/tutorial** mix: mostly practical docs with setup, template syntax, built-in providers/transforms, and extension examples. The content is **high-density** and fairly detailed, with concrete commands, schema URLs, and code snippets. It appears to be **primary source** documentation from the project itself, so it is useful for evaluating the intended API, but trustworthiness depends on the repository staying current. This is best used as a **refer-back** resource when implementing or debugging footer templates and extensions. Scrape quality looks **good**: the main README sections, examples, commands, and API snippets are present, with no obvious missing code blocks or major sections.
