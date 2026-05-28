---
url: https://github.com/tobi/qmd
title: 'tobi/qmd: mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local'
scraped_at: '2026-04-19T07:09:29Z'
word_count: 3839
raw_file: raw/2026-04-19_tobi-qmd-mini-cli-search-engine-for-your-docs-knowledge-bases-meeting-notes-what_d339c484.txt
tldr: QMD is a local-first Markdown/document search engine and SDK for Node/Bun that combines BM25, vector search, LLM query expansion, and reranking, with CLI, MCP server, and library APIs for agentic workflows.
key_quote: QMD combines BM25 full-text search, vector semantic search, and LLM re-ranking—all running locally via node-llama-cpp with GGUF models.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- tobi
tools:
- qmd
- node-llama-cpp
- tree-sitter
- Claude Desktop
- Claude Code
- sqlite-vec
libraries: []
companies:
- GitHub
- Hugging Face
- Homebrew
tags:
- local-search
- markdown-notes
- hybrid-retrieval
- mcp
- knowledge-base
---

### TL;DR
QMD is a local-first Markdown/document search engine and SDK for Node/Bun that combines BM25, vector search, LLM query expansion, and reranking, with CLI, MCP server, and library APIs for agentic workflows.

### Key Quote
"QMD combines BM25 full-text search, vector semantic search, and LLM re-ranking—all running locally via node-llama-cpp with GGUF models."

### Summary
- **What it is**
  - QMD stands for **Query Markup Documents**.
  - It is an **on-device search engine** for markdown notes, meeting transcripts, documentation, and knowledge bases.
  - It is designed for **local-only use** and for **agentic workflows**.

- **Core search approach**
  - Uses **three retrieval layers**:
    - **BM25 / SQLite FTS5** for keyword search
    - **Vector semantic search** for meaning-based retrieval
    - **LLM reranking** for final relevance ordering
  - The main `query` mode performs:
    - LLM query expansion
    - Parallel lexical + vector retrieval
    - **Reciprocal Rank Fusion (RRF)**
    - LLM reranking with a **position-aware blend**
  - The architecture keeps exact matches from being drowned out by expanded queries via:
    - Original query weighted **×2**
    - Top-rank bonus
    - Different retrieval/reranker blend by rank band

- **CLI usage**
  - Install globally:
    - `npm install -g @tobilu/qmd`
    - or `bun install -g @tobilu/qmd`
  - Common workflow:
    - Add collections: `qmd collection add ~/notes --name notes`
    - Add context: `qmd context add qmd://notes "Personal notes and ideas"`
    - Build embeddings: `qmd embed`
    - Search:
      - `qmd search "project timeline"` for fast keyword search
      - `qmd vsearch "how to deploy"` for semantic search
      - `qmd query "quarterly planning process"` for hybrid best-quality search
  - Retrieval commands:
    - `qmd get "meeting.md"`
    - `qmd get "#abc123"`
    - `qmd multi-get "journals/2025-05*.md"`

- **Agent/MCP support**
  - Exposes an **MCP server** with tools:
    - `query`
    - `get`
    - `multi_get`
    - `status`
  - Supports both:
    - **stdio** transport for local client launch
    - **HTTP transport** for a shared long-lived server
  - Intended for Claude Desktop / Claude Code integration and other MCP clients.

- **SDK/library usage**
  - Can be used as a Node.js/Bun library via `@tobilu/qmd`.
  - Main API is `createStore()`, which supports:
    - inline config
    - YAML config file
    - reopening an existing database
  - Search API examples include:
    - `store.search({ query: "authentication flow" })`
    - `store.searchLex(...)`
    - `store.searchVector(...)`
    - `store.expandQuery(...)`
  - Retrieval and indexing APIs include:
    - `get`
    - `multiGet`
    - `addCollection`
    - `addContext`
    - `update`
    - `embed`
    - `close`

- **Indexing and chunking**
  - Documents are stored in SQLite at `~/.cache/qmd/index.sqlite`.
  - Index schema includes:
    - `collections`
    - `path_contexts`
    - `documents`
    - `documents_fts`
    - `content_vectors`
    - `vectors_vec`
    - `llm_cache`
  - Embeddings use ~900-token chunks with 15% overlap.
  - Chunking is “smart”:
    - prefers markdown structure like headings, code fences, horizontal rules, paragraphs
    - supports **AST-aware chunking** for code via tree-sitter when `--chunk-strategy auto` is enabled
  - AST chunking applies to:
    - `.ts`, `.tsx`, `.js`, `.jsx`, `.py`, `.go`, `.rs`

- **Models and requirements**
  - Requires:
    - **Node.js >= 22**
    - **Bun >= 1.0.0**
    - On macOS, Homebrew SQLite for extension support
  - Uses three auto-downloaded GGUF models:
    - `embeddinggemma-300M-Q8_0` for embeddings
    - `qwen3-reranker-0.6b-q8_0` for reranking
    - `qmd-query-expansion-1.7B-q4_k_m` for query expansion
  - Supports overriding the embedding model via `QMD_EMBED_MODEL`, with a note that re-embedding is required when switching models.

- **Notable features**
  - Local-only operation with models cached under `~/.cache/qmd/models/`
  - Flexible output formats for automation:
    - `--json`
    - `--files`
    - `--csv`
    - `--md`
    - `--xml`
  - Editor-aware clickable terminal links via `QMD_EDITOR_URI`
  - Explicit `dbPath` requirement in the SDK to avoid side effects
  - Maintenance commands like `qmd status`, `qmd update`, `qmd cleanup`

- **Overall positioning**
  - The repo is both a **tool** and a **reference implementation** for a modern local hybrid search pipeline.
  - It emphasizes current SOTA-style retrieval patterns while staying fully local.
  - It looks especially aimed at people building personal knowledge bases, RAG-style workflows, and agent integrations.

### Assessment
Durability is **medium**: the general ideas behind hybrid retrieval, RRF, embeddings, reranking, and local-first knowledge search are fairly durable, but many concrete details here are tied to specific model names, Node/Bun requirements, and current MCP/LLM tooling. Content type is **mixed**—mostly reference/docs with tutorial-style quick start and implementation details. Density is **high** because it packs CLI commands, SDK examples, architecture diagrams, model configuration, and storage schema into a single README. Originality is best described as **primary source**: this is the project’s own documentation, not a third-party summary. Reference style is **refer-back** for installation, commands, API signatures, and architecture; it’s not something to deep-study unless you’re extending or integrating the tool. Scrape quality is **good**: the README content appears largely intact, including code blocks, tables, and architecture text, though embedded images/diagrams are referenced rather than visually rendered here.
