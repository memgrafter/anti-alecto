---
url: https://github.com/simonw/LLM
title: 'simonw/llm: Access large language models from the command-line'
scraped_at: '2026-04-19T08:43:57Z'
word_count: 1443
raw_file: raw/2026-04-19_simonw-llm-access-large-language-models-from-the-command-line_c0091986.txt
tldr: llm is a command-line tool and Python library by Simon Willison for using many LLMs—OpenAI, Claude, Gemini, Llama, local models, and plugins—with features like chat, logging, embeddings, structured extraction, and tool use.
key_quote: A CLI tool and Python library for interacting with **OpenAI**, **Anthropic’s Claude**, **Google’s Gemini**, **Meta’s Llama** and dozens of other Large Language Models
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Simon Willison
tools:
- llm
- brew
- pip
- pipx
- uv
- Ollama
- Datasette
libraries: []
companies:
- OpenAI
- Anthropic
- Google
- Meta
- Homebrew
- PyPI
tags:
- command-line-tools
- large-language-models
- python-libraries
- embeddings
- plugins
---

### TL;DR
`llm` is a command-line tool and Python library by Simon Willison for using many LLMs—OpenAI, Claude, Gemini, Llama, local models, and plugins—with features like chat, logging, embeddings, structured extraction, and tool use.

### Key Quote
"A CLI tool and Python library for interacting with **OpenAI**, **Anthropic’s Claude**, **Google’s Gemini**, **Meta’s Llama** and dozens of other Large Language Models"

### Summary
- **What it is**
  - A GitHub repository for **LLM**, a CLI + Python library for interacting with large language models.
  - Supports both **remote APIs** and **local/self-hosted models**.
  - Licensed under **Apache 2.0**.

- **Primary capabilities**
  - Run prompts from the command line.
  - Store prompts and responses in **SQLite**.
  - Generate and query **embeddings**.
  - Extract **structured content** from text and images using schemas.
  - Give models access to **tools**.
  - Use interactive **chat** mode.
  - Extend functionality through **plugins**.

- **Quick start / installation**
  - Install via:
    - `pip install llm`
    - `brew install llm`
    - `pipx install llm`
    - `uv tool install llm`
  - Set an OpenAI key:
    - `llm keys set openai`
  - Example prompt:
    - `llm "Ten fun names for a pet pelican"`
  - Example image extraction:
    - `llm "extract text" -a scanned-document.jpg`
  - Example system prompt on stdin:
    - `cat myfile.py | llm -s "Explain this code"`

- **Model support via plugins**
  - For **Gemini**:
    - `llm install llm-gemini`
    - `llm keys set gemini`
    - `llm -m gemini-2.0-flash 'Tell me fun facts about Mountain View'`
  - For **Anthropic**:
    - `llm install llm-anthropic`
    - `llm keys set anthropic`
    - `llm -m claude-4-opus 'Impress me with wild facts about turnips'`
  - For **local models**, it mentions plugins such as **llm-ollama**:
    - `llm install llm-ollama`
    - `ollama pull llama3.2:latest`
    - `llm -m llama3.2:latest 'What is the capital of France?'`

- **Interactive usage**
  - Start a chat with:
    - `llm chat -m gpt-4.1`
  - The sample chat shows:
    - multiline entry support
    - prompt editing via `!edit`
    - fragment insertion via `!fragment`
    - exit commands `exit` or `quit`

- **Documentation structure**
  - The README is essentially a table of contents for a large docs site.
  - Major sections include:
    - Setup
    - Usage
    - OpenAI models
    - Other models
    - Tools
    - Schemas
    - Templates
    - Fragments
    - Model aliases
    - Embeddings
    - Plugins
    - Python API
    - Logging to SQLite
    - Related tools
    - CLI reference
    - Contributing
    - Changelog

- **Notable emphasis**
  - The project is positioned as both:
    - a practical terminal interface for LLM work
    - a developer platform for extensibility via Python and plugins
  - It highlights ongoing additions like:
    - multimodal inputs
    - structured extraction
    - long-context support
    - template and fragment workflows

### Assessment
This is a **reference/tutorial/mixed** project README with **high durability** at the conceptual level but **medium durability** in the command examples because model names, plugins, and feature details will evolve over time. The content is highly **dense** and mostly **primary source** documentation from the project itself, not commentary. It is best used as **refer-back** material: a quick map to the tool’s capabilities and docs, with the full documentation needed for implementation details. Scrape quality is **good**: the README content, example commands, and table of contents are present, though any linked subpages, images, or deeper code/docs content are not included here.
