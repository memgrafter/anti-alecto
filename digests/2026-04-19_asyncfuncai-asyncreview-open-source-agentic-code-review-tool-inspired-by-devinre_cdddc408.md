---
url: https://github.com/AsyncFuncAI/AsyncReview/
title: 'AsyncFuncAI/AsyncReview: Open-source Agentic code review tool inspired by DevinReview, using Recursive Language Models (RLM)'
scraped_at: '2026-04-19T07:13:34Z'
word_count: 501
raw_file: raw/2026-04-19_asyncfuncai-asyncreview-open-source-agentic-code-review-tool-inspired-by-devinre_cdddc408.txt
tldr: AsyncReview is an open-source, agentic GitHub PR/issue code review tool that uses Recursive Language Models plus repo/file search and sandboxed Python execution to produce more grounded reviews than diff-only AI reviewers.
key_quote: Most AI review tools only look at the lines changed in a Pull Request (the diff). This leads to shallow feedback and hallucinations about files that don't exist.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- npx
- GitHub API
- Gemini API
- GitHub CLI
- Claude
- Cursor
- OpenCode
- Codex
libraries: []
companies:
- AsyncFuncAI
- GitHub
- Google
- Vercel
tags:
- code-review
- github
- agentic-ai
- recursive-reasoning
- developer-tools
---

### TL;DR
AsyncReview is an open-source, agentic GitHub PR/issue code review tool that uses Recursive Language Models plus repo/file search and sandboxed Python execution to produce more grounded reviews than diff-only AI reviewers.

### Key Quote
“Most AI review tools only look at the lines changed in a Pull Request (the diff). This leads to shallow feedback and hallucinations about files that don't exist.”

### Summary
- **What it is**
  - AsyncReview is an **open-source agentic code review tool** for **GitHub PRs and issues**.
  - It is described as being **inspired by DevinReview** and built around **Recursive Language Models (RLM)**.
  - Goal: move beyond shallow diff-only review by exploring the repository, gathering context, and verifying findings.

- **How it works**
  - The workflow is presented as a recursive loop:
    1. **Reason & plan**
    2. **Generate Python code**
    3. Execute in a **Python REPL sandbox**
       - Can run logic, `llm_query()`, and tool commands
    4. Use a **tool interceptor**
       - Supports **FETCH_FILE** and **SEARCH**
       - Pulls real data via the **GitHub API**
    5. **Observe results and repeat recursively**
  - The system emphasizes **verification in a secure sandbox** before answering.
  - The repository diagram claims this approach leads to “**10x High Quality Answer**.”

- **Why it exists**
  - The page argues that most AI review tools:
    - only inspect the **git diff**
    - miss repository-wide context
    - make incorrect assumptions about code structure
    - hallucinate APIs or file contents
  - AsyncReview claims to address this by:
    - reading **any file in the repo**
    - running **search queries**
    - executing **verification scripts**
    - citing **existing file paths and lines**
    - using **recursive reasoning** rather than one-shot prompting

- **Quick start / usage**
  - **No installation required** for basic use; run via `npx`:
    ```bash
    npx asyncreview review --url https://github.com/org/repo/pull/123 -q "Check for breaking changes"
    ```
  - Alternative install path through Skills:
    ```bash
    npx skills add AsyncFuncAI/AsyncReview
    ```

- **Public repository usage**
  - Requires only a **Gemini API key**:
    ```bash
    export GEMINI_API_KEY="your-key"
    npx asyncreview review --url https://github.com/org/repo/pull/123 -q "Review this"
    ```

- **Private repository usage**
  - Requires **Gemini API key** plus a **GitHub token**:
    ```bash
    export GITHUB_TOKEN=$(gh auth token)
    # or
    export GITHUB_TOKEN="ghp_..."
    ```
  - Then run:
    ```bash
    npx asyncreview review --url https://github.com/org/private-repo/pull/456 -q "Security audit"
    ```

- **Configuration**
  - **Required:** `GEMINI_API_KEY`
  - **Optional / needed for private repos:** `GITHUB_TOKEN`

- **Designed for other agents**
  - AsyncReview is also positioned as a **Skill** for agentic systems such as:
    - Claude
    - Cursor
    - OpenCode
    - Gemini
    - Codex
  - It can be installed with:
    ```bash
    npx skills add AsyncFuncAI/AsyncReview
    ```
  - Manual setup points agents to:
    - `skills/asyncreview/SKILL.md`

- **Advanced setup**
  - For the full backend server or web UI, the page sends readers to an **Installation Guide**: `INSTALLATION.md`

- **License**
  - **MIT**

### Assessment
This is a **mixed** content type, primarily a **tool/reference** page with some promotional framing. Its **durability is medium** because the core idea—agentic, repository-aware review—is relatively stable, but the exact setup depends on current tooling such as `npx`, Skills CLI compatibility, Gemini API access, and GitHub auth methods. The page is fairly **dense** for a README-style overview, with concrete commands, environment variables, and an architecture diagram, but it is still a **primary source** only for what the project claims about itself; there’s no benchmark evidence or external validation here. It’s best used as a **refer-back** reference when deciding how to run the tool or whether its approach fits your workflow. **Scrape quality is good**: the key README content, commands, configuration, and positioning are present, though the embedded image itself and the linked Installation Guide are not included in full.
