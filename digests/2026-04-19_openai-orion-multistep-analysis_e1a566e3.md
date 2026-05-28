---
url: https://github.com/openai/orion-multistep-analysis
title: openai/orion-multistep-analysis
scraped_at: '2026-04-19T07:19:49Z'
word_count: 707
raw_file: raw/2026-04-19_openai-orion-multistep-analysis_e1a566e3.txt
tldr: A local-first, multi-agent research-and-analysis framework for SQLite datasets that combines a FastAPI backend, React frontend, and Python agents, but is explicitly marked as unsafe for shared or production use without added auth and execution isolation.
key_quote: “This repository is intended for trusted single-operator/local use only and is not production-hardened.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- fastapi
- react
- vite
- pandas
- openai responses api
libraries: []
companies:
- OpenAI
tags:
- multi-agent-systems
- data-analysis
- sqlite
- fastapi
- react-frontend
---

### TL;DR
A local-first, multi-agent research-and-analysis framework for SQLite datasets that combines a FastAPI backend, React frontend, and Python agents, but is explicitly marked as unsafe for shared or production use without added auth and execution isolation.

### Key Quote
“This repository is intended for trusted single-operator/local use only and is not production-hardened.”

### Summary
- **What it is**
  - A domain-agnostic “Multistep Research & Analysis Agentic Framework” described as an extensible, general-purpose version of ORION.
  - Designed for multi-turn AI research and data analysis over structured datasets stored as SQLite `.db` files.
  - Uses multiple agents:
    - a **data analysis agent**
    - a **literature-review planning agent**
    - a **supervisor reviewer** to keep work transparent, reproducible, and goal-aligned.

- **Architecture / components**
  - **Backend:** FastAPI app for dataset management, run orchestration, and event streaming.
  - **Frontend:** React + Vite UI for launching runs and viewing logs/artifacts.
  - **Agents:** Python implementations for analysis, literature review planning, and supervision.
  - Repository layout highlights:
    - `src/research_agent/backend/` — API, job manager, storage, routes
    - `src/research_agent/agents/` — analysis/literature/supervision logic
    - `src/research_agent/analysis/` — ingestion and analysis utilities
    - `src/research_agent/supervisor/` — orchestration and review logic
    - `src/research_agent/interface/` — CLI entrypoints
    - `frontend/` — web UI
    - `runtime/` — datasets, runs, prompts, events
    - `scripts/` and `tests/` — helpers and test coverage

- **Important safety warning**
  - The repo is intended only for **trusted single-operator/local use**.
  - It **does not implement inbound authentication or authorization**.
  - Analysis runs may trigger **host-side Python execution**.
  - Any shared or production deployment should add its own authentication and execution isolation.

- **Prerequisites**
  - Python **3.10+**
  - Node.js **18+**
  - OpenAI API key with access to the **Responses API** via `OPENAI_API_KEY`
  - Optional `OPENAI_BASE_URL`

- **Setup**
  - Create and activate a Python virtual environment.
  - Install dependencies with `pip install -r requirements.txt`.
  - Set `OPENAI_API_KEY` and `PYTHONPATH="$PWD/src"`.
  - Install frontend dependencies with `npm install` inside `frontend/`.
  - Optional: copy `.env.example` to `.env`.

- **Running the app**
  - Recommended dev startup:
    - `./scripts/run_dev.sh`
  - Backend only:
    - `uvicorn research_agent.backend.main:app --reload --port 8000`
  - Frontend only:
    - `cd frontend && npm run dev`
  - Backend docs are available at:
    - `http://127.0.0.1:8000/api/docs`

- **Configuration / environment variables**
  - Data and runtime paths:
    - `ORION_DATA_ROOT` (default `runtime/data`)
    - `ORION_RUNS_ROOT` (default `runtime/runs`)
    - `ORION_EVENTS_DB` (default `runtime/events.db`)
    - `ORION_PROMPTS_STORE` (default `runtime/prompts_store.json`)
  - Run limits:
    - `ORION_MAX_CONCURRENT_RUNS` (default `1`)
    - `ORION_ALLOW_PARALLEL` (default `false`)
  - Upload limits:
    - `ORION_MAX_UPLOAD_BYTES` (default `104857600`)
    - `ORION_MAX_ZIP_MEMBERS` (default `1000`)
    - `ORION_MAX_ZIP_UNCOMPRESSED_BYTES` (default `524288000`)
  - Legacy `MRDAA_*` variables are still accepted for backward compatibility.

- **Data workflow**
  - Users can upload a `.db` through the UI or place it directly in `runtime/data/`.
  - CSV and ZIP imports are supported:
    - a single `.csv`, or
    - a `.zip` containing multiple CSV files
  - The backend converts CSVs into a new SQLite `.db` using pandas, with one table per CSV and table names derived from filenames.
  - Available databases can be browsed for table schemas and previews.
  - Runs are launched by selecting a database and entering a goal; logs stream live and artifacts are saved under `runtime/runs/<session-id>/`.

- **Scripts**
  - `scripts/run_dev.sh` — start backend + frontend together
  - `scripts/run_backend.sh` — start FastAPI server
  - `scripts/run_frontend.sh` — start Vite server
  - `scripts/run_cli.sh` — run the CLI entrypoint
  - `scripts/backend_smoke.py` — lightweight API smoke test

- **Runtime artifacts**
  - `runtime/data/` — user datasets and CSV imports
  - `runtime/runs/` — transcripts, JSON payloads, generated artifacts
  - `runtime/events.db` — persistent SQLite log of run metadata
  - `runtime/prompts_store.json` — editable prompt overrides

- **Status / roadmap**
  - The “Next Steps” section suggests the project is still evolving:
    - implement the generic orchestrator with the data-analysis, literature, and supervisor agents
    - map existing UI flows to generalized endpoints

### Assessment
This is a fairly durable **reference** and **setup/usage** document, though parts are version-sensitive because it depends on specific tooling choices (FastAPI, React/Vite, OpenAI Responses API, Python 3.10+, Node 18+) and environment variable names. The content is a **mixed** technical reference/tutorial: it explains the project’s purpose, architecture, safety constraints, installation, runtime configuration, and operational workflows. Density is **medium-high** because it includes concrete commands, file paths, defaults, and limits. It appears to be **primary source** documentation from the repository itself rather than commentary or synthesis. It is best used **refer-back** rather than deep-study: enough detail to set up, run, and navigate the codebase, but not enough to understand internal implementation in depth. Scrape quality looks **good** overall, with the main README-style sections captured; no obvious code blocks or major sections appear missing from the provided content.
