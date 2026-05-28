---
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md
title: pi-mono/packages/coding-agent/docs/skills.md at main · badlogic/pi-mono
scraped_at: '2026-04-19T08:03:56Z'
word_count: 865
raw_file: raw/2026-04-19_pi-mono-packages-coding-agent-docs-skills-md-at-main-badlogic-pi-mono_300a11bb.txt
tldr: 'This document explains how Pi’s agent “skills” work: where they’re discovered, how they’re loaded on demand, how to invoke them with `/skill:name`, and how to structure and validate them using the Agent Skills standard.'
key_quote: “Skills are self-contained capability packages that the agent loads on-demand.”
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Pi
- Claude Code
- OpenAI Codex
libraries: []
companies:
- Pi
- Anthropic
- GitHub
- OpenAI
tags:
- agent-skills
- configuration
- cli-commands
- documentation
- validation
---

### TL;DR
This document explains how Pi’s agent “skills” work: where they’re discovered, how they’re loaded on demand, how to invoke them with `/skill:name`, and how to structure and validate them using the Agent Skills standard.

### Key Quote
“Skills are self-contained capability packages that the agent loads on-demand.”

### Summary
- **What skills are**
  - Self-contained capability packages for Pi’s agent.
  - Can include specialized workflows, setup instructions, helper scripts, and reference docs for specific tasks.
  - Pi follows the [Agent Skills standard](https://agentskills.io/specification), warning on violations but staying relatively lenient.

- **Where Pi loads skills from**
  - **Global paths:**
    - `~/.pi/agent/skills/`
    - `~/.agents/skills/`
  - **Project paths:**
    - `.pi/skills/`
    - `.agents/skills/` in the current working directory and ancestor directories, up to the git repo root or filesystem root
  - **Packages/settings/CLI:**
    - `skills/` directories or `pi.skills` entries in `package.json`
    - `skills` array in settings
    - `--skill <path>` CLI flag, repeatable and additive even with `--no-skills`
  - **Discovery rules**
    - In `~/.pi/agent/skills/` and `.pi/skills/`, root `.md` files are discovered as individual skills
    - In all skill locations, directories containing `SKILL.md` are discovered recursively
    - In `~/.agents/skills/` and project `.agents/skills/`, root `.md` files are ignored
    - Discovery can be disabled with `--no-skills`, except explicitly passed `--skill` paths still load

- **How skills are used**
  - At startup, Pi scans skill locations and extracts each skill’s name and description.
  - The system prompt receives the available skills in XML form.
  - When a task matches, the agent loads the full `SKILL.md` with `read`.
  - The agent then follows the skill instructions, using relative paths for scripts/assets.
  - This is described as **progressive disclosure**: only summaries are always in context, full instructions load only when needed.
  - The doc notes that models don’t always load the full file automatically, so prompting or `/skill:name` can force it.

- **Skill commands**
  - Skills can be invoked as commands like:
    - `/skill:brave-search`
    - `/skill:pdf-tools extract`
  - Arguments after the command are appended into the skill content as `User: <args>`.
  - Skill commands can be enabled/disabled via `/settings` or `settings.json` with:
    - `enableSkillCommands: true`

- **Skill structure**
  - A skill is usually a directory containing a required `SKILL.md`.
  - Other files are freeform and can include:
    - `scripts/` for helper scripts
    - `references/` for on-demand documentation
    - `assets/` for templates or bundled files
  - `SKILL.md` should contain YAML frontmatter plus instructions.
  - Relative links should be used from the skill directory.

- **Frontmatter requirements**
  - Required:
    - `name` — max 64 chars, lowercase letters/numbers/hyphens, must match parent directory
    - `description` — required, max 1024 chars, explains what the skill does and when to use it
  - Optional:
    - `license`
    - `compatibility`
    - `metadata`
    - `allowed-tools`
    - `disable-model-invocation`
  - `disable-model-invocation: true` hides the skill from the system prompt, requiring manual `/skill:name` use.

- **Validation behavior**
  - Pi validates skills against the standard.
  - Most issues only produce warnings, including:
    - name mismatch with directory
    - invalid name format
    - overly long names/descriptions
  - Unknown frontmatter fields are ignored.
  - A missing `description` is an exception: the skill will not load.
  - If two skills share the same name, Pi warns and keeps the first one found.

- **Example**
  - The doc shows a sample `brave-search/` skill directory with:
    - `SKILL.md`
    - `search.js`
    - `content.js`
  - Example usage includes:
    - `./search.js "query"`
    - `./search.js "query" --content`
    - `./content.js https://example.com`

- **Skill repositories linked**
  - **Anthropic Skills**: document processing and web development skills
  - **Pi Skills**: web search, browser automation, Google APIs, transcription

### Assessment
This is a **reference** document with a **high** durability for the general pattern of agent skill packaging, though some operational details may change as Pi evolves. The content is mostly **technical/factual**, with a dense, structured explanation of discovery rules, invocation, frontmatter, and validation. It is primarily **original documentation** from the Pi project rather than commentary or synthesis. As a reference, it is best used **refer-back** rather than skim-once, since it defines conventions and file/path rules you may need to consult later. Scrape quality appears **good**: the main sections, examples, code blocks, and linked repository references are present, though embedded images or external linked pages are not included here.
