---
url: https://github.com/kevinrgu/autoagent
title: 'kevinrgu/autoagent: autonomous harness engineering'
scraped_at: '2026-04-19T07:57:35Z'
word_count: 815
raw_file: raw/2026-04-19_kevinrgu-autoagent-autonomous-harness-engineering_68603bc0.txt
tldr: autoagent is a Harbor-compatible framework for “autonomous harness engineering,” where a meta-agent iterates overnight on a single-file agent harness (`agent.py`) using benchmark scores as the optimization signal.
key_quote: Give an AI agent a task, let it build and iterate on an agent harness autonomously overnight.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- docker
- uv
libraries: []
companies:
- Third Layer
tags:
- agent-engineering
- benchmark-optimization
- harbor
- llm-agents
- docker-workflows
---

### TL;DR
`autoagent` is a Harbor-compatible framework for “autonomous harness engineering,” where a meta-agent iterates overnight on a single-file agent harness (`agent.py`) using benchmark scores as the optimization signal.

### Key Quote
“Give an AI agent a task, let it build and iterate on an agent harness autonomously overnight.”

### Summary
- **What this project is**
  - A GitHub repo for **AutoAgent**, described as “like autoresearch but for agent engineering.”
  - The core workflow is to let an AI agent modify an agent harness, run benchmarks, inspect scores, and keep or discard changes based on performance.
  - The repository is positioned as a product prototype from **Third Layer**, with a note that a self-configuring agents product is launching soon.

- **Main idea / workflow**
  - Instead of a human editing harness Python files directly, the human edits **`program.md`**, which instructs the meta-agent.
  - The meta-agent then:
    - reads the directive,
    - inspects the harness,
    - runs the benchmark,
    - diagnoses failures,
    - modifies **`agent.py`**,
    - and iterates on the score.
  - The optimization objective is the benchmark’s **total score** from task test suites.

- **Important repository files**
  - **`agent.py`**: the entire harness under test, kept in one file.
    - Contains config, tool definitions, agent registry, routing/orchestration, and Harbor adapter boundary.
    - The adapter section is marked fixed; the rest is meant to be editable by the meta-agent.
  - **`program.md`**: human-edited instructions and directive for the meta-agent.
  - **`tasks/`**: benchmark tasks in **Harbor** format.
  - **`.agent/`**: optional workspace for reusable prompts, notes, skills, or instructions.
  - **`jobs/`** and **`results.tsv`**: run outputs / experiment log.

- **Quick start / required setup**
  - Requirements listed:
    - Docker
    - Python 3.10+
    - `uv`
    - whatever model-provider credentials the current `agent.py` needs
  - Setup steps include:
    - install `uv`
    - run `uv sync`
    - set environment variables like `OPENAI_API_KEY`
    - build a base Docker image with `docker build -f Dockerfile.base -t autoagent-base .`
    - add tasks under `tasks/`
    - run Harbor benchmarks using `uv run harbor run ... --agent-import-path agent:AutoAgent`
  - Example commands are given for:
    - a single task run
    - running all tasks in parallel with `-n 100`

- **Task format**
  - The repo does **not** ship with tasks by default.
  - Tasks should follow Harbor’s task layout:
    - `task.toml`
    - `instruction.md`
    - `tests/test.sh`
    - `tests/test.py`
    - `environment/Dockerfile`
    - `files/`
  - Tests must write a score between **0.0 and 1.0** to `/logs/reward.txt`.
  - The meta-agent uses that score to hill-climb.

- **Design choices emphasized**
  - **Program the meta-agent, not the harness directly**: humans steer via `program.md`.
  - **Single-file, registry-driven harness**: simplifies implementation while preserving structure.
  - **Docker isolation**: the agent runs in containers and cannot damage the host.
  - **Score-driven iteration**: each experiment is accepted or rejected based on benchmark score.
  - **Harbor-compatible tasks**: intended to transfer across benchmark datasets.

- **Operational notes**
  - The repo includes cleanup advice because Docker images/containers accumulate:
    - `uv run harbor cache clean -f`
    - `docker system prune -a -f`
    - `docker container prune -f`
  - If Docker becomes unresponsive, restart Docker Desktop.

- **Extra note**
  - It suggests performance improvements using external “skills” such as:
    - Agent Skills for Context Engineering
    - context7

### Assessment
This is a **mixed** technical/project reference with both docs and product pitch. Durability is **medium**: the high-level architecture and idea of meta-agent harness optimization are fairly stable, but the concrete commands, repository structure, and Harbor integration are version- and toolchain-dependent. Density is **medium-high** because it contains specific workflow details, file roles, and command examples, though it is also partly promotional. Originality is **primary source** since it documents the project’s own design and setup rather than summarizing others. It is best used as **refer-back** material if you plan to run or modify the repo, and the scrape quality is **good**: the key README content, commands, and structure appear captured, though images and any linked external docs are not included.
