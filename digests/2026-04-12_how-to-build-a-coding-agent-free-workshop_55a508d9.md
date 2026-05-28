---
url: https://ghuntley.com/agent/
title: 'how to build a coding agent: free workshop'
scraped_at: '2026-04-12T09:37:08Z'
word_count: 3939
raw_file: raw/2026-04-12_how-to-build-a-coding-agent-free-workshop_55a508d9.txt
tldr: This workshop argues that a coding agent is mostly a simple loop around an LLM plus a few core tools—read, list, bash, edit, and search—and walks through toy examples showing how those primitives combine into an agentic coding harness.
key_quote: 300 lines of code running in a loop with LLM tokens. You just keep throwing tokens at the loop, and then you've got yourself an agent.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Geoffrey Huntley
tools:
- Cursor
- Windsurf
- Claude Code
- GitHub Copilot
- Amp
- MCP
- ripgrep
libraries:
- Node.js
companies:
- Canva
- Sourcegraph
- Anthropic
- OpenAI
- Google
- GitHub
- SST
tags:
- coding-agents
- llm-tools
- prompt-engineering
- software-automation
- developer-productivity
---

### TL;DR
This workshop argues that a coding agent is mostly a simple loop around an LLM plus a few core tools—read, list, bash, edit, and search—and walks through toy examples showing how those primitives combine into an agentic coding harness.

### Key Quote
"300 lines of code running in a loop with LLM tokens. You just keep throwing tokens at the loop, and then you've got yourself an agent."

### Summary
- **What this is:** A conference workshop talk by Geoffrey Huntley, titled **“how to build a coding agent: free workshop”**, focused on demystifying coding agents and showing how to build one from scratch.
- **Main thesis:** Coding agents are not magical; they are mostly:
  - an **LLM in a loop**
  - a **tool-calling harness**
  - a handful of basic primitives
- **Core claim:** The speaker repeatedly emphasizes that there is "no moat" and that the model does most of the work; the agent is just orchestration around it.

- **Speaker’s framing and motivation:**
  - Learning to build a coding agent is presented as a key 2025 skill.
  - The speaker claims AI is changing work so people can delegate tasks to agents while doing something else, even during meetings.
  - He argues disruption comes from people not investing in their own skills, not from AI itself.

- **Model selection advice:**
  - Not all LLMs are equally “agentic.”
  - The speaker describes a rough quadrant of model behavior:
    - **high safety**
    - **low safety**
    - **oracle**
    - **agentic**
  - He says a strong agentic model should be used first, then other models can be wired in as tools.
  - Examples mentioned:
    - **Claude Sonnet** and **Kimi K2** as agentic
    - **GPT** as an “oracle” tool for checking work or doing research
    - **Grok** as a low-safety model for security research

- **Context window guidance:**
  - He stresses using the context window for **one task at a time**.
  - Reusing a session for unrelated tasks causes degraded results.
  - He says larger context allocations and too many MCP tools reduce performance.
  - He cites **Claude Sonnet’s advertised 200k context**, with roughly **176k usable** after system prompt and harness overhead.

- **MCP explanation:**
  - MCP is described as essentially a function with a description that gets placed into the context window so the model knows how to invoke it.
  - He warns against installing too many MCP servers or exposing too many tools.

- **Five primitives of a coding harness / agent:**
  1. **read tool**
     - Reads a file into context.
     - Example tool definition: `read_file`
  2. **list tool**
     - Lists files and directories.
     - Example tool definition: `list_files`
  3. **bash tool**
     - Executes shell commands.
     - Example tool definition: `bash`
  4. **edit tool**
     - Applies file edits.
     - Example tool definition: `edit_file`
  5. **search tool**
     - Searches source code using **ripgrep (`rg`)** under the hood.
     - Example tool definition: `code_search`

- **Workshop demos shown:**
  - **Weather tool stub**
    - Demonstrates a simple function call like `get_weather(Melbourne, Australia)`.
    - Used to show basic tool invocation.
  - **Read file demo**
    - Creates `riddle.txt` with a horse riddle.
    - Agent uses `read_file` to read it and answers correctly: **horse**.
  - **List files demo**
    - Uses `list_files` to find `README.md` and inspect `riddle.txt`.
  - **Bash demo**
    - Runs `ps aux` to summarize processes on the machine.
  - **Edit demo**
    - Creates `fizzbuzz.js`, runs it with Node.js, and verifies correct FizzBuzz output up to 20.
  - **Search demo**
    - Uses `code_search` with pattern `riddle`.
    - Finds a reference in `README.md`, then lists files and reads `riddle.txt`.

- **Implementation message:**
  - The loop is:
    - user input or tool result → allocate into context → infer → maybe call tool → return result → continue
  - The speaker says once these primitives exist, the rest is mostly **prompt tuning** and harness design.
  - He notes the harness prompt should include:
    - tool registrations
    - OS information
    - operating system command choice (PowerShell vs bash)

- **Closing points:**
  - Mentions open-source examples of coding agents, including **SST Open Code** and a **100-line agent** that scored well on **SWE Bench**.
  - Suggests that similar automation primitives could help in other jobs like data engineering.
  - Ends with a self-help style conclusion: invest in yourself; “Your current workers are going to take your job, not AI.”

### Assessment
This is a **mixed** content piece: part tutorial, part opinionated keynote, part product/industry commentary. Its **durability is medium** because the high-level agent concepts are fairly timeless, but the specific model recommendations, context-window numbers, and 2025 claims are highly version- and market-dependent. The **density is medium-high**: it contains many specific examples, tool definitions, and code snippets, but the rhetoric is repetitive and promotional in places. The work is **primary source** commentary from the speaker, not a neutral synthesis, and it reads best as **refer-back** material if you want the conceptual framing and primitive list, rather than deep study for exact implementation details. The **scrape quality is good overall**: the text includes the main narrative, code snippets, tool definitions, and demos, though any original visuals/sequence diagrams and “see below” references are not preserved, so some contextual elements are likely missing.
