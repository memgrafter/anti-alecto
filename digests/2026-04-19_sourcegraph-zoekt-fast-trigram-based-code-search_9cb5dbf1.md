---
url: https://github.com/sourcegraph/zoekt/tree/main
title: 'sourcegraph/zoekt: Fast trigram based code search'
scraped_at: '2026-04-19T06:54:29Z'
word_count: 616
raw_file: raw/2026-04-19_sourcegraph-zoekt-fast-trigram-based-code-search_9cb5dbf1.txt
tldr: Zoekt is a trigram-based code search engine for source code, offering fast substring/regexp search, a boolean query language, and both CLI and server-based workflows for indexing and searching repositories.
key_quote: Zoekt is a text search engine intended for use with source code.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Jan Eertink
- Han-Wen Nienhuys
- Alexander Neubeck
tools:
- git
- Universal ctags
- Zoekt
libraries: []
companies:
- Sourcegraph
tags:
- code-search
- trigram-indexing
- cli-tools
- server-administration
- source-code
---

### TL;DR
Zoekt is a trigram-based code search engine for source code, offering fast substring/regexp search, a boolean query language, and both CLI and server-based workflows for indexing and searching repositories.

### Key Quote
“Zoekt is a text search engine intended for use with source code.”

### Summary
- **What it is**
  - Zoekt is a code-search engine optimized for source code rather than generic text.
  - It supports:
    - fast substring matching
    - regular expression search
    - boolean query operators: `and`, `or`, `not`
  - Search ranking uses code-aware signals, especially whether a match is on a symbol.
  - It is designed around trigram indexing and syntactic parsing, which helps it work well across many programming languages.
  - This repository is the maintained source since 2017, forked from `github.com/google/zoekt`.

- **Main ways to use it**
  - **Command-line tools** for local indexing/searching
  - **Indexserver + webserver** for larger-scale, remote repository indexing and browsing via UI or API

- **Installation**
  - Install with:
    - `go get github.com/sourcegraph/zoekt/`
  - Recommended dependency:
    - **Universal ctags**
      - improves symbol information
      - symbol information is a key ranking signal
      - referenced in `doc/ctags.md`

- **Command-based usage**
  - Index a local git repo:
    - `go install github.com/sourcegraph/zoekt/cmd/zoekt-git-index`
    - `zoekt-git-index -index ~/.zoekt /path/to/repo`
  - Index a local directory:
    - `go install github.com/sourcegraph/zoekt/cmd/zoekt-index`
    - `zoekt-index -index ~/.zoekt /path/to/repo`
  - Search an index:
    - `go install github.com/sourcegraph/zoekt/cmd/zoekt`
    - `zoekt 'hello'`
    - `zoekt 'hello file:README'`

- **Server-based usage**
  - **Indexserver**
    - periodically fetches and reindexes repositories from a code host
    - example shown for a GitHub organization (`apache`)
    - uses a JSON mirror config with GitHub token credentials
    - command:
      - `go install github.com/sourcegraph/zoekt/cmd/zoekt-indexserver`
      - `zoekt-indexserver -mirror_config config.json -data_dir ~/.zoekt/`
  - **Webserver**
    - serves a simple search UI at `http://localhost:6070`
    - command:
      - `go install github.com/sourcegraph/zoekt/cmd/zoekt-webserver`
      - `zoekt-webserver -index ~/.zoekt/`
    - supports the query syntax documented in `doc/query_syntax.md`

- **Container image**
  - Publishes a container at `ghcr.io/sourcegraph/zoekt`
  - Includes:
    - Zoekt binaries
    - `git`
    - `universal-ctags`
  - Default behavior:
    - runs `zoekt-webserver` against `/data/index`
  - Example commands show:
    - mounting an index directory for web search
    - overriding the default command to run `zoekt-indexserver`
  - If started with `-rpc`, the webserver exposes a JSON search API at:
    - `http://localhost:6070/api/search`

- **API features**
  - JSON API supports:
    - streaming search results via `FlushWallTime`
    - BM25 scoring via `UseBM25Scoring`
    - context lines via `NumContextLines`
  - Web server also exposes a **gRPC API**
    - supports structured query objects
    - supports advanced search options

- **Documentation pointers**
  - `doc/` for design and additional details
  - `doc/query_syntax.md` for query language
  - `doc/json-api.md` for JSON API details
  - `cmd/zoekt-indexserver/config.go` for mirror config details
  - `query/query.go` for structured query objects

- **Acknowledgements**
  - Credits Han-Wen Nienhuys as creator of Zoekt
  - Credits Alexander Neubeck for the original idea and helping develop it

### Assessment
This is a high-durability **reference** and **tool/documentation** page: the core concepts of trigram-based code search, CLI indexing/search, and server-based deployment are stable, but some installation commands and paths may be version-sensitive (for example `go get` versus `go install`, and current container/runtime details). The page is fairly **dense** with actionable specifics, commands, and config examples, and it appears to be a **primary source** maintained by the project owners rather than a synthesis. It’s best used as a **refer-back** resource when setting up or operating Zoekt, though the scrape is only partial in the sense that it captures the README-level overview and examples, not the linked docs or code internals.
