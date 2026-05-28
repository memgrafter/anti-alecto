---
url: https://github.com/MaximeRivest/rat/blob/67a037e0204cbbc7ddd25881953d4f0acc042056/internal/runtimes/pi/runtime.yaml
title: rat/internal/runtimes/pi/runtime.yaml at 67a037e0204cbbc7ddd25881953d4f0acc042056 · MaximeRivest/rat
scraped_at: '2026-04-19T07:26:50Z'
word_count: 67
raw_file: raw/2026-04-19_rat-internal-runtimes-pi-runtime-yaml-at-67a037e0204cbbc7ddd25881953d4f0acc04205_afe5b563.txt
tldr: This YAML file defines the pi runtime for the rat project, including how to detect it, which CLI options it supports, and how it runs inside tmux with an npm-installed Pi coding agent.
key_quote: 'detect: commands: [pi] env: RAT_PI'
durability: high
content_type: reference
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- tmux
- npm
libraries:
- '@mariozechner/pi-coding-agent'
companies:
- rat
tags:
- runtime-configuration
- tmux
- cli-options
- npm
- project-config
---

### TL;DR
This YAML file defines the **`pi` runtime** for the `rat` project, including how to detect it, which CLI options it supports, and how it runs inside **tmux** with an npm-installed Pi coding agent.

### Key Quote
"detect:
  commands: [pi]
  env: RAT_PI"

### Summary
- This is a **runtime configuration file** for `rat`, specifically for the runtime named **`pi`**.
- Basic metadata:
  - `name: pi`
  - `display: pi`
- **Detection logic**:
  - Detects the runtime if the `pi` command exists.
  - Also detects via the `RAT_PI` environment variable.
- **Supported options**:
  - `model`
    - CLI arg: `--model`
    - Description: “Model pattern or ID”
  - `provider`
    - CLI arg: `--provider`
    - Description: “Provider name”
  - `thinking`
    - CLI arg: `--thinking`
    - Allowed values: `off`, `minimal`, `low`, `medium`, `high`, `xhigh`
    - Description: “Thinking level”
- **Kernel/runtime execution**:
  - Uses `tmux` as the kernel type.
  - Command template:
    - `"{runtime} {opts} --extension {bridge} --session-dir {data_dir}/sessions"`
  - Bridge file: `bridge.ts`
  - Key bindings:
    - Submit: `Enter`
    - Cancel: `Escape`
- **Frontend**:
  - Also uses `tmux`
- **Installation requirements**:
  - Requires `tmux` to be present (`check_commands: [tmux]`)
  - Installs runtime via `npm`
  - Dependency: `@mariozechner/pi-coding-agent`
- **Smoke test / validation**:
  - Uses `status` as the smoke-check command (`ctl: status`)

### Assessment
This is a **high-durability reference** for a project-specific runtime definition, though its exact details are tied to the `rat` codebase and the `pi-coding-agent` package version in use. The content type is **reference**, with a very dense, schema-like structure rather than prose. It appears to be **primary source** configuration, not commentary or synthesis. It’s best used as a **refer-back** document when you need to understand how the `pi` runtime is wired up, what options it accepts, or what dependencies and terminal controls it expects. **Scrape quality is good** for the YAML content shown; it appears complete for this file, with no obvious missing sections or code blocks.
