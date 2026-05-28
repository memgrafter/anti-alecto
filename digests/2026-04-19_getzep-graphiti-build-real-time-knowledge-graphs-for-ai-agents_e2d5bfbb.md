---
url: https://github.com/getzep/graphiti
title: 'getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents'
scraped_at: '2026-04-19T07:25:51Z'
word_count: 3118
raw_file: raw/2026-04-19_getzep-graphiti-build-real-time-knowledge-graphs-for-ai-agents_e2d5bfbb.txt
tldr: Graphiti is an open-source framework for building temporal, provenance-aware context graphs for AI agents, with hybrid retrieval, incremental updates, and support for multiple graph databases and LLM providers.
key_quote: Graphiti is a framework for building and querying temporal context graphs for AI agents.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Claude
- Cursor
tools:
- FastAPI
- Docker
- Docker Compose
- Neo4j
- FalkorDB
- Kuzu
- Amazon Neptune
- OpenSearch Serverless
- OpenAI
- Azure OpenAI
- Gemini
- Anthropic
- Groq
- Ollama
- PostHog
- LangGraph
- MCP
libraries:
- graphiti-core
- Pydantic
companies:
- getzep
- Zep
- OpenAI
- Anthropic
- Google
- Amazon
- PostHog
tags:
- knowledge-graphs
- ai-agents
- temporal-data
- retrieval
- provenance
---

### TL;DR
Graphiti is an open-source framework for building temporal, provenance-aware context graphs for AI agents, with hybrid retrieval, incremental updates, and support for multiple graph databases and LLM providers.

### Key Quote
"Graphiti is a framework for building and querying temporal context graphs for AI agents."

### Summary
- **What it is**
  - Open-source project from **getzep/Zep** for building **temporal context graphs** rather than static knowledge graphs.
  - Designed for AI agents that need **changing facts, historical truth, and provenance** over time.
  - Emphasizes **hybrid retrieval**: semantic embeddings + keyword search (BM25) + graph traversal.

- **Core concept: context graphs**
  - Graphs store:
    - **Entities**: people, products, policies, concepts; entity summaries can evolve over time.
    - **Facts / relationships**: triplets with **validity windows** showing when they were true.
    - **Episodes**: raw ingested data that serves as provenance/ground truth.
    - **Custom types**: developer-defined ontology via **Pydantic models**.
  - Facts are not deleted when superseded; they are **invalidated** while preserving history.

- **Why Graphiti exists**
  - Positioned as an alternative to batch-oriented, static **RAG** and **GraphRAG** approaches.
  - Claims to support:
    - **Incremental graph construction** without full recomputation
    - **Precise historical queries**
    - **Lower-latency retrieval** than LLM-summarization pipelines
    - Better handling of **frequently changing data**

- **Graphiti vs Zep**
  - **Graphiti** = self-hosted, open-source temporal context graph engine.
  - **Zep** = managed infrastructure built on Graphiti for production agent deployments.
  - Zep adds governance, dashboards, logs, SDKs, SLA/support, and managed deployment options.
  - Graphiti is for teams that want the core OSS engine and can operate the surrounding system themselves.

- **Graphiti vs GraphRAG**
  - GraphRAG is described as more **static** and **batch-oriented**.
  - Graphiti claims advantages in:
    - continuous updates
    - explicit bi-temporal tracking
    - automatic fact invalidation
    - sub-second retrieval
    - custom entity types
    - high scalability

- **Installation and requirements**
  - Requires:
    - **Python 3.10+**
    - A supported graph backend: **Neo4j 5.26**, **FalkorDB 1.1.2**, **Kuzu 0.11.2**, or **Amazon Neptune + OpenSearch Serverless**
    - **OpenAI API key** by default for LLM inference and embeddings
  - Optional LLM providers: **Gemini, Anthropic, Groq**
  - Install via:
    - `pip install graphiti-core`
    - or `uv add graphiti-core`
  - Extra installs available for graph backends and providers, e.g.:
    - `graphiti-core[falkordb]`
    - `graphiti-core[kuzu]`
    - `graphiti-core[neptune]`
    - `graphiti-core[anthropic]`, `[groq]`, `[google-genai]`

- **Operational note**
  - Ingestion concurrency is controlled by `SEMAPHORE_LIMIT` and defaults to **10** to reduce LLM **429 rate limit** errors.
  - Users can raise it for more throughput or lower it if rate-limited.

- **Quick start and examples**
  - The quickstart covers:
    - connecting to a graph database
    - initializing indices and constraints
    - adding text and structured JSON episodes
    - hybrid edge search
    - reranking by graph distance
    - node search recipes
  - Docker Compose examples are provided for **Neo4j** and **FalkorDB**.

- **MCP server**
  - Includes a **Model Context Protocol (MCP) server** in `mcp_server/`.
  - Lets assistants like **Claude** and **Cursor** use Graphiti as temporal memory.
  - Supports:
    - episode management
    - entity/relationship management
    - semantic/hybrid search
    - group management
    - graph maintenance operations

- **REST service**
  - Also includes a **FastAPI** service under `server/` for API access.

- **Provider-specific integrations**
  - Examples are provided for:
    - **Azure OpenAI**
    - **Google Gemini**
    - **Ollama** / local OpenAI-compatible models
  - Notes:
    - Graphiti works best with LLMs that support **structured output**
    - For Ollama, use `OpenAIGenericClient`
    - Gemini can be used for LLM, embeddings, and reranking

- **Telemetry**
  - Graphiti collects **anonymous usage statistics** by default.
  - Collects:
    - random local anonymous ID
    - OS, Python version, architecture
    - Graphiti version
    - provider/backend configuration choices
  - Does **not** collect:
    - personal info
    - API keys
    - actual graph content, queries, or episode data
    - IP addresses or hostnames
  - Can be disabled via:
    - `GRAPHITI_TELEMETRY_ENABLED=false`
  - Uses **PostHog** and is designed to fail silently.

- **Documentation and support**
  - Points to help docs, quick start, LangGraph integration guide, Discord support, and contribution guidelines.
  - The repo also notes that Zep is hiring.

### Assessment
This is a **mixed** technical project landing page / reference document with a **high** durability for the core ideas of temporal context graphs, provenance, and incremental retrieval, though some specifics like supported versions, installation extras, and backend requirements will age quickly. The content is **dense** and mostly **primary source** material from the project maintainers, with marketing-oriented comparisons to RAG/GraphRAG and Zep alongside practical setup guidance. It’s best treated as a **refer-back** reference: useful for evaluating whether Graphiti fits an agent-memory or temporal-knowledge use case, and for checking install/runtime options, but you’d want the linked docs for implementation details. Scrape quality appears **good** overall: the main README content, tables, code blocks, and major sections are present, though embedded images/animated demos themselves are not rendered here.
