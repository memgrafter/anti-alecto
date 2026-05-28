---
url: https://devenv.sh/
title: Fast, Declarative, Reproducible, and Composable Developer Environments - devenv
scraped_at: '2026-04-12T07:12:00Z'
word_count: 1579
raw_file: raw/2026-04-12_fast-declarative-reproducible-and-composable-developer-environments-devenv_a564849f.txt
tldr: devenv is a Nix-based tool for defining fast, reproducible, composable development environments with declarative packages, tasks, services, profiles, containers, tests, outputs, and runtime secrets.
key_quote: Activate your environment in under 100ms with precise Nix evaluation caching.
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
- process-compose
- git-hooks.nix
- SecretSpec
libraries: []
companies: []
tags:
- developer-environments
- nix
- reproducible-builds
- devops
- secrets-management
---

### TL;DR
devenv is a Nix-based tool for defining fast, reproducible, composable development environments with declarative packages, tasks, services, profiles, containers, tests, outputs, and runtime secrets.

### Key Quote
“Activate your environment in under 100ms with precise Nix evaluation caching.”

### Summary
- **What it is**
  - A developer environment manager built around Nix, aimed at making environments **fast, declarative, reproducible, and composable**.
  - Supports native development, container workflows, and team/shared configurations.

- **Core claims / performance**
  - Shows shell startup from a first build of about **4.832s** to a cached run of **0.047s**.
  - Emphasizes **smart invalidation**: tracks files accessed during evaluation and re-evaluates only what changed.
  - Claims **zero configuration** and no daemon/file-watching setup.

- **Basic configuration**
  - Uses a `devenv.nix` file with declarative options such as:
    - `env` for environment variables
    - `packages` for installing prebuilt packages
    - `enterShell` for commands run on shell entry
    - `dotenv.enable = true` for loading secrets from `.env`
  - Example shown with `pkgs.ncdu`, `env.GREET`, and an `enterShell` script.

- **Tasks and git hooks**
  - Supports declarative tasks, with dependency relationships and execution in parallel.
  - Git hooks are configured through `git-hooks.nix`-style options; examples include:
    - `black.enable = true`
    - custom hook `generate-css` running `devenv tasks run myapp:build`
  - Hook/task output shown in the shell, including `Succeeded` statuses and timings.

- **Language support**
  - Supports **50+ programming languages**.
  - Provides tooling like **LSP servers, formatters, linters, compilers**, and version selection.
  - Examples shown for:
    - Python 3.11 with `venv`, `requirements`, and `uv`
    - Rust nightly with `rustflags` and targets
    - PHP 8.1 with `ini` and `fpm` pool settings
  - Mentions languages such as Python, Terraform, Rust, Go, PHP, and Ruby.

- **Processes**
  - Lets you define processes declaratively and run them with `devenv up`.
  - Inspired by `Procfile`, but integrated with the environment.
  - Uses `process-compose` by default for log viewing and restart management.
  - Example shown with `cargo-watch` running `cargo watch -x run`.

- **Services**
  - Includes many community-maintained service modules such as:
    - PostgreSQL, Redis, MySQL, RabbitMQ, WireMock, MinIO, Caddy, Elasticsearch, OpenTelemetry Collector, Prometheus
  - Services can be customized with package selection, initial databases, extensions, settings, and initialization scripts.
  - Example shown configuring PostgreSQL 15 with `postgis`, `timescaledb`, preload libraries, and an init script.

- **Testing**
  - `devenv test` runs scripts with all processes active.
  - Example uses `wait_for_port 8000` and `curl` against a local docs server to verify behavior.
  - Positioning: integrated environment testing without manual process management.

- **Containers**
  - Can generate containers from the development environment.
  - Commands shown:
    - `devenv container run shell`
    - `devenv container run processes`
    - `devenv container build processes`
    - `devenv container copy processes`
  - Supports custom container definitions via `containers.mycontainer.*`.

- **Composing environments**
  - Supports monorepo and polyrepo composition through imports.
  - `imports:` examples show bringing in root/shared config and remote repositories.
  - Uses `${config.git.root}` for stable path references.

- **Profiles**
  - Profiles let you selectively activate parts of the environment, such as backend vs frontend.
  - Can extend other profiles and auto-activate by hostname or username.
  - Useful for shared standards, team-specific setup, and reducing duplication.

- **Outputs / packaging**
  - Can define build outputs for applications with `devenv build`.
  - Language integrations choose packaging tools automatically, e.g.:
    - `crate2nix` for Rust
    - `uv2nix` for Python
  - Output derivations are intended for distribution and deployment.

- **Ad-hoc environments**
  - Supports one-off environments from the CLI without config files.
  - Examples include:
    - instant Python environment
    - quick Elixir REPL
    - CI matrix testing across versions
  - Useful for experiments and temporary overrides of existing config.

- **Secrets**
  - Integrates with **SecretSpec** for declarative secrets management.
  - Secrets can come from Keychain, 1Password, LastPass, dotenv, or environment variables.
  - Supports profile-based differences and runtime retrieval so secrets aren’t stored in config files.
  - Example shows a `KEYCLOAK_ADMIN_PASSWORD` secret used by a Keycloak service.

### Assessment
This is a **high-durability** reference/tutorial hybrid: the underlying ideas—declarative dev environments, reproducibility, composable configs, services, profiles, and secrets—are fairly timeless, though specific commands, package versions, and supported tooling may change over time. The content is **mixed** (part product announcement, part documentation, part tutorial), and it is **high-density** because it packs many concrete features, commands, and configuration examples into a single page. It is primarily **primary source** material from the project’s own site rather than commentary or synthesis. Best used as a **refer-back** resource when deciding whether devenv fits a workflow or when looking up feature areas; it’s also suitable for a quick skim. Scrape quality is **good** overall: the main page’s text, examples, and feature sections are present, though formatting is flattened and any richer visual structure from the original site is likely lost.
