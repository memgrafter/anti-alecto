---
url: https://simonwillison.net/2025/Dec/12/openai-skills/
title: OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI
scraped_at: '2026-04-12T09:40:30Z'
word_count: 774
raw_file: raw/2026-04-12_openai-are-quietly-adopting-skills-now-available-in-chatgpt-and-codex-cli_03abfed7.txt
tldr: OpenAI has quietly added Anthropic-style “skills” support to both ChatGPT’s Code Interpreter and the open-source Codex CLI, and Simon Willison demonstrates that these skills can be discovered, inspected, and used to automate real tasks like generating PDFs and writing a Datasette plugin.
key_quote: Skills are based on a very light specification, if you could even call it that, but I still think it would be good for these to be formally documented somewhere.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Simon Willison
- Elias Judin
tools:
- ChatGPT
- Code Interpreter
- Codex CLI
- Claude Code
- uvx
libraries:
- pluggy
companies:
- OpenAI
- Anthropic
- Datasette
tags:
- llm-tools
- agentic-ai
- chatgpt
- codex-cli
- software-development
---

### TL;DR
OpenAI has quietly added Anthropic-style “skills” support to both ChatGPT’s Code Interpreter and the open-source Codex CLI, and Simon Willison demonstrates that these skills can be discovered, inspected, and used to automate real tasks like generating PDFs and writing a Datasette plugin.

### Key Quote
“Skills are based on a very light specification, if you could even call it that, but I still think it would be good for these to be formally documented somewhere.”

### Summary
- **What the post is about**
  - Simon Willison reports that OpenAI has adopted “skills,” a mechanism originally associated with Anthropic.
  - The feature has appeared in:
    - **ChatGPT** (specifically the Code Interpreter environment)
    - **Codex CLI** (OpenAI’s open-source CLI tool)
  - Published date: **12th December 2025**

- **Why skills matter**
  - A skill is described as **just a folder** containing:
    - a **Markdown file**
    - optional **resources**
    - optional **scripts**
  - The key idea is that any LLM tool that can read a filesystem should be able to use skills.
  - Willison argues this portability makes skills a strong cross-platform pattern.

- **Skills in ChatGPT**
  - Willison learned from **Elias Judin** that ChatGPT’s Code Interpreter now has a hidden-ish skills directory:
    - `/home/oai/skills`
  - He says you can access it by prompting:
    - `Create a zip file of /home/oai/skills`
  - He did this successfully and explored the resulting zip with a UI.
  - The skills he found covered:
    - **spreadsheets**
    - **docx**
    - **PDFs**
  - For PDFs and documents, OpenAI’s approach is notable:
    - convert pages to **rendered PNGs**
    - feed those to **vision-capable GPT models**
    - presumably to preserve layout and graphics that text extraction would miss

- **Comparison to Anthropic**
  - Copies of the skills were shared by Elias in a GitHub repo.
  - Willison says they look **very similar** to Anthropic’s implementation in the **anthropics/skills** repository.

- **Example: generating a PDF in ChatGPT**
  - He prompted ChatGPT:
    - `Create a PDF with a summary of the rimu tree situation right now and what it means for kakapo breeding season`
  - The model appeared to:
    - read `skill.md` for PDF creation guidelines
    - search for relevant information about **rimu mast** and **kākāpō 2025 breeding status**
  - It took **just over eleven minutes** to produce the PDF.
  - He notes the system was careful and iterative:
    - it rendered its own output
    - noticed **macrons in kākāpō** were unsupported by the chosen font
    - switched fonts to fix the issue

- **Skills in Codex CLI**
  - About two weeks earlier, OpenAI’s **Codex CLI** gained experimental skills support in a PR titled:
    - `feat: experimental support for skills.md`
  - The docs for this are in:
    - `docs/skills.md`
  - The code that renders the skill prompt is in:
    - `codex-rs/core/src/skills/render.rs`
  - Willison links to a more readable Gist of the prompt.

- **Using a skill in Codex CLI**
  - He used **Claude Opus 4.5’s skill authoring skill** to create a skill for writing **Datasette plugins**
  - He installed it to:
    - `~/.codex/skills/datasette-plugin`
  - Installation command shown:
    - `git clone https://github.com/datasette/skill ~/.codex/skills/datasette-plugin`
  - Codex CLI must be run with:
    - `--enable skills`
  - He started Codex like this:
    - `codex --enable skills -m gpt-5.2`
  - After prompting `list skills`, Codex reported:
    - `datasette-plugins — Writing Datasette plugins using Python + pluggy`
    - `Discovery — How to find/identify available skills`
  - He then prompted Codex to write a plugin adding a page at:
    - `/-/cowsay?text=hello`
  - The plugin was generated successfully.

- **Local demo and verification**
  - Willison says the plugin code worked “perfectly.”
  - He provides a way to try it locally using `uvx`:
    - `uvx --with https://github.com/simonw/datasette-cowsay/archive/refs/heads/main.zip datasette`
  - Then visit:
    - `http://127.0.0.1:8001/-/cowsay?text=This+is+pretty+fun`

- **Willison’s conclusion**
  - He reiterates his earlier view that **Claude Skills are a big deal**, perhaps “a bigger deal than MCP.”
  - OpenAI’s adoption within just two months reinforces that belief.
  - He thinks the lightweight skills format should be **formally documented**, possibly by the **Agentic AI Foundation**.

### Assessment
This is a **mixed** piece: part news, part hands-on technical exploration, and part commentary. Its durability is **medium** because it’s tied to specific product versions, paths, and prompt behavior in late 2025, but the broader idea—filesystem-based skills for LLM tools—should remain relevant. The density is **high**, with concrete commands, file paths, tool names, prompt examples, and observed behavior. It’s primarily **original commentary and experimentation**, not a synthesis of third-party reporting, since Willison directly tests the feature in ChatGPT and Codex CLI. It’s best used as a **refer-back** item if you’re tracking agent/tooling patterns or want implementation clues. Scrape quality appears **good**: the full text, commands, examples, and links are present, though embedded images/tools referenced in the post are not included here.
