---
url: https://simonwillison.net/2025/Oct/16/claude-skills/
title: Claude Skills are awesome, maybe a bigger deal than MCP
scraped_at: '2026-04-12T09:39:35Z'
word_count: 1764
raw_file: raw/2026-04-12_claude-skills-are-awesome-maybe-a-bigger-deal-than-mcp_ee1227a5.txt
tldr: Simon Willison argues that Anthropic’s new Claude Skills are a deceptively simple but very powerful way to extend LLMs—possibly more impactful than MCP—because they let models load task-specific Markdown instructions, scripts, and resources on demand inside a coding environment.
key_quote: Skills are Markdown with a tiny bit of YAML metadata and some optional scripts in whatever you can make executable in the environment.
durability: medium
content_type: opinion
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Simon Willison
- Anthropic
tools:
- Claude
- Claude Code
- Cursor
- Codex CLI
- Gemini CLI
- ChatGPT Code Interpreter
- MCP
- Slack
libraries:
- PIL
- Image
- ImageDraw
- ImageFont
companies:
- Anthropic
- GitHub
- Slack
- Datasette Cloud
tags:
- llm-agents
- prompt-engineering
- coding-environments
- model-context-protocol
- anthopic-claude-skills
---

### TL;DR
Simon Willison argues that Anthropic’s new **Claude Skills** are a deceptively simple but very powerful way to extend LLMs—possibly more impactful than MCP—because they let models load task-specific Markdown instructions, scripts, and resources on demand inside a coding environment.

### Key Quote
“Skills are Markdown with a tiny bit of YAML metadata and some optional scripts in whatever you can make executable in the environment.”

### Summary
- **What Claude Skills are**
  - Anthropic introduced **Claude Skills** on **16th October 2025**.
  - A skill is basically a **folder** containing:
    - a **Markdown file** with instructions
    - optional **extra documents/resources**
    - optional **scripts** the model can run
  - Claude only loads a skill **when it’s relevant** to the task.
  - The design is meant to improve performance on specialized tasks like:
    - working with **Excel**
    - following **brand guidelines**
    - creating documents like **PDF, DOCX, XLSX, PPTX**

- **How they work in practice**
  - Anthropic’s harnesses can scan available skills at session start and read short YAML frontmatter summaries.
  - This is **token efficient**: only a small summary is loaded up front, and the full skill details are loaded only when needed.
  - Willison tested Anthropic’s **slack-gif-creator** skill in the Claude mobile web app with **Sonnet 4.5**.
  - He prompted: **“Make me a gif for slack about how Skills are way cooler than MCPs”**
  - Claude produced a GIF, though he says it was “terrible,” but notes the important point is that skills are **easy to iterate on**.
  - He includes a Python snippet showing the skill’s code using:
    - `PIL` / `Image`, `ImageDraw`, `ImageFont`
    - a `GIFBuilder`
    - a Slack size check via `check_slack_size(...)`
  - The included validation is practical because **Slack GIFs must be under 2MB**.

- **Why the coding environment matters**
  - Skills depend on Claude having:
    - a **filesystem**
    - tools to **browse files**
    - the ability to **execute commands**
  - Willison frames this as part of the broader **coding agent / code interpreter** pattern.
  - He cites earlier examples:
    - **ChatGPT Code Interpreter** (early 2023)
    - coding agents like **Cursor, Claude Code, Codex CLI, Gemini CLI**
  - He argues this dependency is what makes skills much more capable than older approaches like **MCP** or **ChatGPT Plugins**.
  - He also warns that safe sandboxing is crucial, since prompt injection could cause damage in these environments.

- **Claude Code as a general agent**
  - Willison says his earlier skepticism about “agents” in 2025 was wrong.
  - In his view, **Claude Code** is not just for coding; it is a **general computer automation tool**.
  - He describes agents as “tools in a loop.”
  - Skills make this broader automation use-case more visible.
  - He gives a speculative example of a **data journalism agent** made from skills for:
    - locating **US census data**
    - loading it into **SQLite or DuckDB**
    - publishing to **S3** or **Datasette Cloud**
    - identifying stories
    - making **D3 visualizations**
  - The point: a folder of Markdown files and a few scripts could create a surprisingly capable domain-specific agent.

- **Skills vs MCP**
  - Willison contrasts Skills with **Model Context Protocol (MCP)**, which has been widely hyped since its release in **November 2024**.
  - His critique of MCP is mainly about **token overhead**:
    - some MCP setups consume **tens of thousands of tokens**
    - that leaves little room for actual task work
  - He says he has become less interested in MCP because many use cases are better served by **CLI tools**, which LLMs can discover via `--help`.
  - Skills offer a similar advantage without needing to build a whole new CLI tool:
    - just drop in a **Markdown skill file**
    - add scripts only when useful for reliability/efficiency

- **Why he likes the simplicity**
  - He emphasizes that many people have already used similar patterns, such as **AGENTS.md** files with instructions like “Read PDF.md before attempting to create a PDF.”
  - But he thinks Skills are exciting precisely because they formalize this simple pattern.
  - He contrasts:
    - **MCP**: a large protocol specification with hosts, clients, servers, resources, prompts, tools, sampling, roots, elicitation, and multiple transports
    - **Skills**: Markdown + tiny YAML + optional executable scripts
  - His view is that Skills align better with how LLM systems actually work: give them instructions and tools, then let the harness/environment do the heavy lifting.

- **Portability and ecosystem potential**
  - He expects many skills to be shared easily, often as **single files**.
  - He points to Anthropic’s:
    - **Agent Skills documentation**
    - **Claude Skills Cookbook**
  - He says skills are not limited to Claude:
    - you can point **Codex CLI** or **Gemini CLI** at a skills folder and use it too
  - He predicts a **“Cambrian explosion”** of Skills that could outpace the MCP boom.

### Assessment
This is a **commentary/opinion** piece with strong practical grounding and some reporting on Anthropic’s announcement. Its **durability is medium**: the broader ideas about task-specific agent instructions and coding-environment automation are likely to last, but the specifics are tied to Claude Skills, Anthropic’s repo, and the 2025 agent ecosystem. The piece is **dense** with concrete examples, names, and claims, and it is clearly a **primary-source adjacent synthesis/commentary** rather than a neutral reference. It works best as a **refer-back** piece if you want to remember Willison’s argument that Skills are a simpler, more efficient alternative to MCP-style integration. **Scrape quality is good**: the main article text, headings, examples, and quoted code snippet are present, though the embedded GIF itself is not included beyond description.
