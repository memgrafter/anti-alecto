---
url: https://github.com/Aider-AI/aider/blob/main/aider/coders/editblock_fenced_prompts.py
title: aider/aider/coders/editblock_fenced_prompts.py at main · Aider-AI/aider
scraped_at: '2026-04-16T03:57:56Z'
word_count: 623
raw_file: raw/2026-04-16_aider-aider-coders-editblock-fenced-prompts-py-at-main-aider-ai-aider_5929d030.txt
tldr: This file defines a prompt template class for Aider that teaches the model how to produce fenced SEARCH/REPLACE edit blocks, with examples and strict formatting rules.
key_quote: 'Every *SEARCH/REPLACE block* must use this format:'
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools: []
libraries: []
companies:
- Aider-AI
- Aider
tags:
- prompt-engineering
- code-editing
- developer-tools
- reference-format
- python
---

### TL;DR
This file defines a prompt template class for Aider that teaches the model how to produce fenced SEARCH/REPLACE edit blocks, with examples and strict formatting rules.

### Key Quote
"Every *SEARCH/REPLACE block* must use this format:"

### Summary
- **File / purpose**
  - `aider/coders/editblock_fenced_prompts.py` defines `EditBlockFencedPrompts`, a subclass of `EditBlockPrompts`.
  - Its job is to supply example chat messages and a system reminder for generating code edits in Aider’s fenced block format.

- **Example messages**
  - The class contains `example_messages`, a list of two prompt/response demonstrations.
  - First example:
    - User asks: `"Change get_factorial() to use math.factorial"`
    - Assistant shows how to edit `mathweb/flask/app.py` using fenced SEARCH/REPLACE blocks.
    - The example includes:
      - adding `import math`
      - removing a recursive `factorial()` function
      - changing `return str(factorial(n))` to `return str(math.factorial(n))`
    - The assistant message uses placeholders like `{fence[0]}python` and `{fence[1]}` for code fences.
    - It also includes a stray `<<<<<<< HEAD` line near the end, likely part of the training/example text or an artifact of the format being demonstrated.
  - Second example:
    - User asks: `"Refactor hello() into its own file."`
    - Assistant demonstrates creating a new `hello.py` file and updating `main.py` to import `hello`.
    - Shows how to represent a new file with an empty SEARCH section and REPLACE content.

- **System reminder**
  - The large `system_reminder` string is the core instruction set for outputting edit blocks.
  - It specifies the required block structure:
    1. opening fence and language
    2. full file path on its own line
    3. `<<<<<<< SEARCH`
    4. exact existing source lines
    5. `=======`
    6. replacement lines
    7. `>>>>>>> REPLACE`
    8. closing fence
  - Important constraints:
    - Use the **full file path** exactly as shown by the user.
    - SEARCH text must **exactly match** the file content character-for-character.
    - Blocks replace only the **first match occurrence**.
    - Prefer **concise** blocks with only the lines needed for the edit.
    - Use **multiple blocks** for multiple changes.
    - To create a **new file**, use a block with an empty SEARCH section.
    - To **rename** files already in chat, use shell commands at the end.
  - The reminder also stresses:
    - include comments/docstrings when they are part of the exact match
    - if code is wrapped in JSON/XML/quotes, edit the literal contents
    - if the user says “ok” or similar, they likely want actual SEARCH/REPLACE blocks
    - “ONLY EVER RETURN CODE IN A *SEARCH/REPLACE BLOCK*!” is the final output rule

- **What this file is for**
  - It is not application logic; it is prompt engineering / template data.
  - The file helps Aider reliably generate edit instructions that can be applied automatically to source files.

### Assessment
This is a high-durability reference-style source because it describes a prompt format and rules that are conceptually stable, though some specifics may evolve with Aider’s editing conventions. It is a mixed content type: mostly reference, with embedded examples and instructional text. The density is high, since most of the value is packed into a few strings and examples. It appears to be original source code from the Aider repository rather than commentary or synthesis. Best used as a refer-back document if you need to understand or replicate Aider’s fenced SEARCH/REPLACE prompting behavior. Scrape quality is good overall: the code and strings are present, though formatting artifacts like the displayed placeholders and the `<<<<<<< HEAD` line may reflect the source exactly or the way the page was rendered.
