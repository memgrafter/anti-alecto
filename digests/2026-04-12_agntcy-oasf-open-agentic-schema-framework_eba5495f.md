---
url: https://github.com/agntcy/oasf
title: 'agntcy/oasf: Open Agentic Schema Framework'
scraped_at: '2026-04-12T07:40:29Z'
word_count: 1283
raw_file: raw/2026-04-12_agntcy-oasf-open-agentic-schema-framework_eba5495f.txt
tldr: OASF is an Apache-licensed schema framework for AI agents, centered on a `record` object and extensible with `skills`, `domains`, and `modules`, with a local/server workflow built around Taskfile, Docker, and hot-reload schema development.
key_quote: The framework includes development tools, schema validation, and hot-reload capabilities for rapid schema development, all managed through a Taskfile-based workflow and containerized development environment.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Taskfile
- Docker
- Buildx
- yq
- curl
- tar
- Kind
- Helm
- Cursor
- MCP
libraries: []
companies:
- AGNTCY
- Outshift by Cisco
- Cisco
tags:
- ai-agents
- schema-framework
- developer-tools
- validation
- hot-reload
---

### TL;DR
OASF is an Apache-licensed schema framework for AI agents, centered on a `record` object and extensible with `skills`, `domains`, and `modules`, with a local/server workflow built around Taskfile, Docker, and hot-reload schema development.

### Key Quote
“The framework includes development tools, schema validation, and hot-reload capabilities for rapid schema development, all managed through a Taskfile-based workflow and containerized development environment.”

### Summary
- **Open Agentic Schema Framework (OASF)** is a standardized schema system for defining and managing:
  - AI agent capabilities
  - interactions
  - metadata
- It is **inspired by OCSF (Open Cybersecurity Schema Framework)**:
  - similar data modeling philosophy
  - similar implementation approach
  - the server is a derivative work of the OCSF schema server
  - schema update workflows reproduce OCSF-developed workflows
- The framework’s stated goals are to:
  - define common data structures for standardization, validation, and interoperability
  - ensure unique agent identification for discovery and consumption
  - provide extension capabilities for third-party features
- **Key concepts**
  - The core data structure is the **`record` object**: `./schema/objects/record.json`
  - Records can be annotated with **skills** and **domains** for announcement and discovery
  - **Modules** extend records in a modular, composable way
- **Extensibility and governance**
  - OASF is expected to evolve to support new use cases and capabilities
  - community contributions are welcomed via `CONTRIBUTING.md`
  - private schema extensions are supported
  - an OASF instance with extensions can be hosted and used for validation
- **Schema versioning**
  - once released, a schema version is treated as immutable
  - only non-breaking fixes like documentation updates or minor bug corrections are expected
  - structural changes, additions, and deletions go into the next schema version
  - this is meant to preserve backward compatibility and stability
- **Useful links / usage**
  - schema browser/server: `https://schema.oasf.outshift.com`
  - local/server deployment guide: `oasf-server.md`
  - agent record guide: https://docs.agntcy.org/how-to-guides/agent-record-guide/
  - skill taxonomy: `https://schema.oasf.outshift.com/skill_categories`
- **MCP Server integration**
  - the **Directory MCP Server** can help create valid OASF agent records when paired with an LLM in Cursor or another MCP-compatible IDE
  - capabilities include:
    - schema discovery
    - record generation
    - validation and iterative fixing
    - format conversion from MCP/A2A and export to other formats
  - example prompts include:
    - “Create an OASF record for this project”
    - “Validate this OASF record and fix any errors”
    - “Import this MCP server configuration to OASF format”
- **Server**
  - `server/` contains the OASF schema server source code
  - it provides browsing and schema validation
  - local access is possible; the hosted instance runs the latest released schema
- **Development workflow**
  - prerequisites:
    - Taskfile
    - Docker
    - Go
    - `yq`
    - `curl`
    - `tar`
    - Docker Buildx
  - clone:
    - `git clone https://github.com/agntcy/oasf.git`
  - build:
    - `task deps`
    - `task build`
  - local deploy:
    - `IMAGE_TAG=latest task build:server`
    - `task up`
    - browse at `http://localhost:8080`
  - increase verbosity:
    - `LOG_LEVEL=debug task up`
  - hot reload for schema changes:
    - `task reload`
  - local multi-version testing:
    - `HELM_VALUES_PATH=./install/charts/oasf/values-test-versions.yaml task up`
    - can be combined with `LOG_LEVEL=debug`
  - cleanup:
    - `task down`
- **Distribution**
  - artifacts are published via the AGNTCY GitHub registry
  - Protocol Buffers live in `proto/`
  - generated stubs and versions are hosted at `https://buf.build/agntcy/oasf`
- **License**
  - Apache 2.0

### Assessment
This is a fairly durable **mixed** repository README: the schema and versioning concepts are high-level and likely to remain relevant for a long time, but the concrete commands, URLs, and workflow details are tied to the current project state and tooling versions. It is primarily a **reference** document with some **tutorial** elements for local development and server deployment. The density is **high**, because it packs architecture, concepts, contribution policy, runtime commands, and distribution details into a single README. Originality is mostly **primary source** material for this project, though it is explicitly shaped by and derivative of OCSF in both philosophy and implementation. For later use, this is a **refer-back** resource: useful when you need the project’s core concepts, local setup commands, or schema/versioning policy. Scrape quality appears **good**: the README content is complete enough to capture the main sections, commands, and links, with no obvious missing code blocks or major sections in the provided text.
