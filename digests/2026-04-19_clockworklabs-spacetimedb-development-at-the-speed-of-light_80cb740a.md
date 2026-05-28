---
url: https://github.com/clockworklabs/SpacetimeDB
title: 'clockworklabs/SpacetimeDB: Development at the speed of light'
scraped_at: '2026-04-19T08:39:57Z'
word_count: 1059
raw_file: raw/2026-04-19_clockworklabs-spacetimedb-development-at-the-speed-of-light_80cb740a.txt
tldr: SpacetimeDB is a Rust-built relational database that doubles as an application server, letting you ship schema, logic, and real-time client sync as one module with no separate backend infrastructure.
key_quote: “SpacetimeDB is a relational database that is also a server.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- spacetime
- docker
libraries: []
companies:
- Clockwork Labs
tags:
- database
- application-server
- real-time-sync
- rust
- backend-infrastructure
---

### TL;DR
SpacetimeDB is a Rust-built relational database that doubles as an application server, letting you ship schema, logic, and real-time client sync as one module with no separate backend infrastructure.

### Key Quote
“SpacetimeDB is a relational database that is also a server.”

### Summary
- **What it is**
  - SpacetimeDB is presented as a database/server hybrid: you upload application logic directly into the database, and clients connect to it without an intermediate server.
  - It is designed for real-time applications and emphasizes low latency, ACID guarantees, and in-memory state with disk commit log durability.

- **Programming model**
  - Application code is written as a **module** in:
    - Rust
    - C#
    - TypeScript
    - C++
  - Modules define:
    - **tables** for data
    - **reducers** for logic / API-like endpoints
  - Clients subscribe to tables and receive automatic state updates when data changes.

- **Core pitch / claimed benefits**
  - No separate web server, containers, Kubernetes, VMs, caching layer, or “DevOps” overhead is needed in the idealized workflow.
  - The whole app can be written in one language and deployed as a single binary.
  - Permissions and authorization logic live inside the module.

- **Architecture and performance claims**
  - The README claims SpacetimeDB provides:
    - all ACID guarantees of a traditional RDBMS
    - speed comparable to an optimized web server
    - in-memory application state for fast access
    - commit log on disk for durability and crash recovery
  - It cites BitCraft Online as a real-world example: the entire MMORPG backend reportedly runs as a single SpacetimeDB module synchronized to thousands of players in real time.

- **Quick start**
  - Install:
    - macOS/Linux: `curl -sSf https://install.spacetimedb.com | sh`
    - Windows PowerShell: `iwr https://windows.spacetimedb.com -useb | iex`
  - Log in:
    - `spacetime login` opens GitHub authentication in a browser.
  - Start a project:
    - `spacetime dev --template chat-react-ts`
    - This creates a template project, publishes it to Maincloud, and watches/rebuilds on file changes.

- **Example usage**
  - Rust example shows:
    - `#[spacetimedb::table(...)]` for a `Message` table
    - `#[spacetimedb::reducer]` for a `send_message` function that inserts rows
  - TypeScript client example shows:
    - `const [messages] = useTable(tables.message);`
    - Updates happen automatically without polling or refetching.

- **Language and SDK support**
  - **Server modules:** Rust, C#, TypeScript, C++
  - **Client SDKs:** TypeScript (React, Next.js, Vue, Svelte, Angular, Node.js, Bun, Deno), Rust, C# (including Unity), C++ (including Unreal Engine)

- **Running and building**
  - Docker command:
    - `docker run --rm --pull always -p 3000:3000 clockworklabs/spacetime start`
  - Building from source requires:
    - Rust toolchain
    - `wasm32-unknown-unknown` target
  - Build command:
    - `cargo build --locked --release -p spacetimedb-standalone -p spacetimedb-update -p spacetimedb-cli`
  - The README includes separate install steps for macOS/Linux and Windows after building.

- **Documentation pointers**
  - Full docs are at `spacetimedb.com/docs`
  - The README points to:
    - quickstarts
    - core concepts (tables, reducers, subscriptions, authentication)
    - tutorials
    - deployment guide for Maincloud
    - CLI reference
    - SQL reference

- **License**
  - Licensed under **Business Source License 1.1 (BSL)**.
  - It says the license converts to **AGPL v3.0 with a linking exception** after a few years.
  - The README explicitly states you are not required to open-source your own code when using SpacetimeDB, only changes to SpacetimeDB itself.
  - The authors explain they chose this because they want to avoid competing with AWS while still encouraging contributions back upstream.

### Assessment
This is a **mixed** technical/product reference with strong marketing language. Its **durability is medium** because the core concepts of tables, reducers, and server-in-database architecture are fairly stable, but install commands, supported languages, versioning, deployment flow, and license timing can change. The **density is medium-high**: it packs a lot of concrete setup commands, language support details, and conceptual framing into a relatively short README. It is primarily a **primary source** for the project’s own positioning and usage instructions, so it’s useful for evaluating the product’s official claims but not independent verification. Best treated as **refer-back** material: good for recalling what SpacetimeDB is, how to get started, and where the docs are, rather than for deep technical study. **Scrape quality is good** overall; the main README content, examples, commands, and license notes are present, though images and linked docs are referenced rather than fully included.
