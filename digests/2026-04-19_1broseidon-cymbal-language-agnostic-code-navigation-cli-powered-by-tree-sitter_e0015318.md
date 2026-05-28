---
url: https://github.com/1broseidon/cymbal?tab=readme-ov-file#agent-integration
title: '1broseidon/cymbal: Language-agnostic code navigation CLI powered by tree-sitter'
scraped_at: '2026-04-19T08:03:17Z'
word_count: 2192
raw_file: raw/2026-04-19_1broseidon-cymbal-language-agnostic-code-navigation-cli-powered-by-tree-sitter_e0015318.txt
tldr: cymbal is a Go-based, tree-sitter-powered CLI and library for language-agnostic code navigation that builds a per-repo SQLite index to provide fast symbol search, references, impact analysis, tracing, and agent-friendly code exploration.
key_quote: Fast, language-agnostic code indexer and symbol navigator built on [tree-sitter](https://tree-sitter.github.io/).
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- cymbal
- docker
- brew
libraries:
- tree-sitter
companies:
- GitHub
tags:
- code-navigation
- cli-tools
- tree-sitter
- sqlite
- developer-tools
---

### TL;DR
`cymbal` is a Go-based, tree-sitter-powered CLI and library for language-agnostic code navigation that builds a per-repo SQLite index to provide fast symbol search, references, impact analysis, tracing, and agent-friendly code exploration.

### Key Quote
> "Fast, language-agnostic code indexer and symbol navigator built on [tree-sitter](https://tree-sitter.github.io/)."

### Summary
- **What it is**
  - `cymbal` is a command-line tool for code navigation and indexing.
  - It parses a repository into a local SQLite database and exposes semantic queries like symbol search, references, call tracing, and impact analysis.
  - It is explicitly designed to be useful for **AI agents**, editor plugins, and terminal workflows.

- **Installation options**
  - **Homebrew**: `brew install 1broseidon/tap/cymbal`
  - **Windows PowerShell**: install via `install.ps1`
  - **Go install**: `CGO_CFLAGS="-DSQLITE_ENABLE_FTS5" go install github.com/1broseidon/cymbal@latest`
  - **Docker**: prebuilt images available at `ghcr.io/1broseidon/cymbal:latest`, with version pinning supported (example: `v0.8.4`)
  - A binary is also available from GitHub Releases.

- **Uninstall behavior**
  - The Windows uninstall script removes the binary and PATH entry by default but keeps repo indexes.
  - `-Purge` removes all per-repo SQLite indexes stored under `%LOCALAPPDATA%\cymbal\repos\`.

- **Core quick-start workflow**
  - A suggested Docker alias makes the CLI feel native:
    - `alias cymbal='docker run --rm -v "$(pwd)":/workspace ghcr.io/1broseidon/cymbal'`
  - Typical commands:
    - `cymbal index .`
    - `cymbal investigate handleAuth`
    - `cymbal trace handleAuth`
    - `cymbal refs handleAuth`
    - `cymbal impact handleAuth`
    - `cymbal context handleAuth`
    - `cymbal outline internal/auth/handler.go`
  - The index auto-builds on first use; no manual indexing step is required.
  - Subsequent queries refresh incrementally when files change.

- **Command set**
  - `investigate`: adaptive all-purpose symbol exploration
  - `structure`: repo overview, hotspots, entry points
  - `trace`: downward call graph
  - `index`: parse and index a directory
  - `ls`: file tree or repo stats
  - `search`: symbol search or `--text` grep-like search
  - `show`: display source for a symbol
  - `outline`: list symbols in a file
  - `refs`: find references/call sites
  - `importers`: reverse import lookup
  - `impls`: implementers/conformers
  - `impact`: transitive callers / change impact
  - `diff`: git diff scoped to a symbol
  - `context`: bundled source + callers + imports + types
  - `hook`: agent integration hooks (`nudge`, `remind`, `install <agent>`)

- **Agent integration**
  - The README strongly emphasizes using `cymbal` instead of generic shell search tools for code exploration.
  - It provides copy-paste policy blocks for:
    - native installs
    - Docker-based usage
  - The hooks are intended to reduce agent drift toward `grep`/`find` as context grows.
  - Two hook commands are highlighted:
    - `cymbal hook nudge` — detects likely code-search shell commands and suggests cymbal equivalents
    - `cymbal hook remind` — prints reminder text agents can inject at session start
  - Claude Code installation is supported with `cymbal hook install claude-code` and `uninstall`.

- **Supported languages**
  - Indexed via tree-sitter for many languages including:
    - Go, Python, JavaScript/TypeScript, Rust, C/C++, C#, Java, Ruby, Swift, Kotlin, Scala, PHP, Lua, Bash, YAML, Elixir, HCL/Terraform, Protobuf, Dart, and more.
  - Additional file types are recognized for classification and heuristics even if not fully parseable, including:
    - Dockerfile, Makefile, Jenkinsfile, CMakeLists.txt, JSON, TOML, Markdown, SQL, Vue, Svelte, Zig, Erlang, Haskell, OCaml, R, Perl.
  - Adding a language requires a tree-sitter grammar plus symbol extraction query.

- **How it works**
  - **Indexing**: tree-sitter extracts symbols, references, imports, and type usage into SQLite with FTS5.
  - **Querying**: all lookups read from the local repo database; no cross-repo bleed.
  - **Freshness**: changed files are automatically reindexed before query results are returned.
  - Storage location is per-repo under the OS cache directory unless overridden with `--db` or `CYMBAL_DB`.

- **Benchmarks and claims**
  - Benchmarks compare against ripgrep on real repos: **gin**, **kubectl**, and **fastapi**.
  - Reported query speed: **9–27 ms**
  - Reindex with no changes: **8–20 ms**
  - Reported precision/recall: **100%** across 43 checks
  - Canonical ranking: **100% @1** across 9 hard disambiguation cases
  - Grep-footgun avoidance: **7/7** tests pass
  - Token savings: **17–100% fewer tokens** than ripgrep for targeted lookups in examples given.

- **Library usage**
  - The project is also a Go library.
  - Exported packages:
    - `index`
    - `lang`
    - `parser`
    - `symbols`
    - `walker`
  - Example APIs shown:
    - `index.Index(...)`
    - `index.RepoDBPath(...)`
    - `index.SearchSymbols(...)`
    - `index.Investigate(...)`
    - `index.FindTrace(...)`
    - `index.FindImpact(...)`
    - `index.FindReferences(...)`
  - Example `lang` helpers include:
    - `Supported("typescript")`
    - `Known("dockerfile")`
    - `LangForFile("Dockerfile")`

- **Docs and metadata**
  - Links to:
    - library guide
    - changelog
    - license
  - License is **MIT**.

### Assessment
This is a **mixed** reference/tutorial/documentation page with some promotional and benchmark material. Durability is **medium-high**: the conceptual model of tree-sitter-based code navigation is fairly durable, but install commands, supported versions, benchmarks, and hook integrations can age as releases change. Density is **high** because the README packs installation, command reference, architecture, benchmarks, agent prompt snippets, and Go API examples into one page. It is primarily a **primary source** for the project’s own capabilities and usage, though the performance claims are self-reported and should be treated as vendor-style benchmarks rather than independent evaluation. This is best used as a **refer-back** reference when you want to remember commands, supported languages, or integration patterns; the scrape quality is **good** and appears to include the full README sections relevant to the page, with code blocks and tables intact.
