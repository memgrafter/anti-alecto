---
url: https://github.com/cachix/devenv
title: 'cachix/devenv: Fast, Declarative, Reproducible, and Composable Developer Environments using Nix'
scraped_at: '2026-04-12T07:20:18Z'
word_count: 1218
raw_file: raw/2026-04-12_cachix-devenv-fast-declarative-reproducible-and-composable-developer-environment_f80afe6c.txt
tldr: devenv is a Nix-based tool for defining fast, reproducible, composable developer environments, with built-in support for languages, services, tasks, containers, secrets, and an interactive CLI.
key_quote: “Fast, Declarative, Reproducible, and Composable Developer Environments”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- devenv
- direnv
- nixd
libraries:
- git-hooks.nix
- crate2nix
- uv2nix
companies:
- Cachix
- Nixpkgs
tags:
- nix
- developer-environments
- cli-tools
- reproducible-builds
- devops
---

### TL;DR
devenv is a Nix-based tool for defining fast, reproducible, composable developer environments, with built-in support for languages, services, tasks, containers, secrets, and an interactive CLI.

### Key Quote
“Fast, Declarative, Reproducible, and Composable Developer Environments”

### Summary
- **Project identity**
  - GitHub repo: `cachix/devenv`
  - Website: [devenv.sh](https://devenv.sh)
  - License: Apache 2.0
  - Current version shown in the CLI help: `2.0.0`
- **What it does**
  - Uses Nix to create developer environments that are:
    - declarative
    - reproducible
    - composable
    - fast to start and reload
  - Supports both full project configs and ad hoc CLI-driven environments.
- **Developer experience features**
  - Terminal UI with live build progress, task hierarchy, and error details
  - Native shell reloading that rebuilds in the background while the shell remains usable
  - Incremental evaluation caching with “sub 100ms when nothing changed”
  - LSP support for `devenv.nix` via bundled `nixd`
  - AI-assisted environment generation via `devenv generate` / `devenv.new`
  - CLI-only ad hoc environments and out-of-tree configs via `--from`
- **Languages, packages, and services**
  - 50+ language toolchains with compilers, LSPs, formatters, linters, and version selection
  - 100,000+ packages from Nixpkgs across Linux, macOS, x64, ARM64, and WSL2
  - 40+ services including PostgreSQL, Redis, MySQL, MongoDB, Elasticsearch, and Caddy
- **Processes and task management**
  - Rust-based native process manager with:
    - dependency ordering
    - restart policies
    - readiness probes (`exec`, HTTP, systemd notify)
    - socket activation
    - watchdog heartbeats
    - file watching
  - Automatic port allocation to avoid collisions between parallel environments
  - Tasks with DAG execution, caching, parallel runs, and namespaces
  - Scripts that can access all environment packages
- **Packaging and deployment**
  - OCI container support without Docker
  - Outputs for packaging apps with language-specific tools like `crate2nix` and `uv2nix`
  - Polyrepo support for referencing outputs and options across repositories
- **Composition and configuration**
  - Profiles for variants like `--profile backend --profile testing`
  - Imports for sharing/reusing environments across projects
  - Inputs for pinning and overriding Nix dependencies
- **Security and integrations**
  - SecretSpec for provider-agnostic secrets management
  - Git hooks through `git-hooks.nix`
  - `devenv test` to start/stop processes automatically during tests
  - direnv integration for auto-activation
  - MCP server for AI assistant package/option search
- **Quick start example**
  - `devenv init` generates a `devenv.nix`
  - Example config shows:
    - environment variables via `env.GREET`
    - packages like `pkgs.git`
    - optional language/process/service config
    - scripts such as `scripts.hello.exec`
    - shell setup via `enterShell`
    - tests via `enterTest`
    - outputs and git hooks
  - `devenv shell` activates the environment
- **CLI surface**
  - Major commands include:
    - `init`, `generate`, `shell`, `update`, `search`, `info`, `up`, `processes`, `tasks`, `test`, `container`, `inputs`, `changelogs`, `repl`, `gc`, `build`, `eval`, `direnvrc`, `version`, `mcp`, `lsp`
  - Supports:
    - `--from` to source config from a repo or local path
    - `--override-input` for flake inputs
    - `--option` for typed config overrides
    - Nix execution controls like `--max-jobs`, `--cores`, `--system`, `--impure`, `--offline`
    - shell behavior controls like `--clean`, `--profile`, `--reload`, `--eval-cache`
    - tracing and TUI toggles
- **Documentation links**
  - Getting Started
  - Basics
  - Roadmap
  - Blog
  - `devenv.yaml` reference
  - `devenv.nix` reference
  - Contributing

### Assessment
This is a high-durability, mixed reference/announcement/tool page: mostly a product/project reference with some marketing-style positioning and a detailed CLI help excerpt. It is dense with specifics—feature lists, command names, flags, and examples—but the content is clearly tied to the current project version and documentation state, so some details may change over time. The original work is primarily a project-maintained reference and product overview rather than a third-party synthesis. Best used as a refer-back resource when evaluating whether devenv fits a workflow, or when looking up commands and capabilities. Scrape quality is good overall: the README content and large CLI help block are present, though linked documentation, images, and external pages are not included beyond the visible text.
