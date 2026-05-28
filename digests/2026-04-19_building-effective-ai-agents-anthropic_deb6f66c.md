---
url: https://www.anthropic.com/engineering/building-effective-agents#agents
title: Building Effective AI Agents \ Anthropic
scraped_at: '2026-04-19T08:06:59Z'
word_count: 2651
raw_file: raw/2026-04-19_building-effective-ai-agents-anthropic_deb6f66c.txt
tldr: Anthropic argues that most effective LLM agent systems are built from simple, composable patterns—start with plain LLM calls, add workflows like chaining/routing only when needed, and reserve autonomous agents for open-ended tasks with clear feedback loops and strong tool design.
key_quote: “Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs.”
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Erik S.
- Barry Zhang
tools:
- Claude Agent SDK
- Strands Agents SDK
- Rivet
- Vellum
- Model Context Protocol
- SWE-bench Verified
libraries: []
companies:
- Anthropic
- AWS
tags:
- llm-agents
- prompt-engineering
- workflow-design
- tool-use
- software-development
---

### TL;DR
Anthropic argues that most effective LLM agent systems are built from simple, composable patterns—start with plain LLM calls, add workflows like chaining/routing only when needed, and reserve autonomous agents for open-ended tasks with clear feedback loops and strong tool design.

### Key Quote
“Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs.”

### Summary
- **Core thesis**
  - Over the past year, Anthropic worked with dozens of teams building LLM agents and found that the most successful systems usually **did not** rely on complex frameworks.
  - The best implementations use **simple, composable patterns** and add complexity only when it clearly improves results.

- **Definitions**
  - Anthropic distinguishes between:
    - **Workflows**: LLMs and tools are orchestrated through **predefined code paths**.
    - **Agents**: LLMs **dynamically direct their own process and tool use**, controlling how they accomplish the task.
  - Anthropic uses “agentic systems” as an umbrella term for both.

- **General guidance**
  - Prefer the **simplest solution possible**.
  - Sometimes the right answer is **not to build an agentic system at all**.
  - Agentic systems often trade **latency and cost** for better task performance.
  - For many applications, a **single LLM call plus retrieval and in-context examples** is enough.
  - Anthropic recommends using **LLM APIs directly** first; frameworks can obscure prompts/responses and make debugging harder.

- **Frameworks mentioned**
  - Claude Agent SDK
  - Strands Agents SDK by AWS
  - Rivet
  - Vellum
  - These help with tool calling, parsing, and chaining, but can add abstraction and tempt overengineering.

- **Foundational building block**
  - The base unit is an **augmented LLM** with access to:
    - retrieval
    - tools
    - memory
  - Anthropic highlights **Model Context Protocol (MCP)** as one way to connect models to third-party tools through a client implementation.

- **Workflows covered**
  - **Prompt chaining**
    - Break a task into fixed sequential steps.
    - Useful when subtasks are clear and you want higher accuracy at the cost of latency.
    - Examples: generate marketing copy then translate it; write an outline, check it, then draft the document.
  - **Routing**
    - Classify input and send it to a specialized downstream prompt/tool/model.
    - Good when inputs fall into distinct categories.
    - Example: customer support routing; sending easy questions to **Claude Haiku 4.5** and hard ones to **Claude Sonnet 4.5**.
  - **Parallelization**
    - Run LLM calls simultaneously and aggregate results.
    - Two forms:
      - **Sectioning**: independent subtasks in parallel.
      - **Voting**: multiple attempts on the same task for confidence.
    - Examples: separate guardrails from response generation; multiple prompts for vulnerability review or moderation decisions.
  - **Orchestrator-workers**
    - A central LLM decomposes the task and delegates to worker LLMs.
    - Useful when subtasks are not known in advance, such as complex coding changes across multiple files or multi-source search tasks.
  - **Evaluator-optimizer**
    - One model generates, another critiques and guides iteration.
    - Best when there are clear evaluation criteria and iterative improvement matters.
    - Examples: literary translation; complex search with multiple rounds.

- **Agents**
  - Agents are presented as useful when:
    - the number of steps cannot be predicted,
    - the system cannot be hardcoded,
    - and the developer can trust the model’s judgment to some degree.
  - Agents work by:
    - starting from a user command or discussion,
    - planning and acting independently,
    - using **ground truth from tools/environment** at each step,
    - pausing for human input at checkpoints or blockers,
    - stopping via completion or explicit limits like max iterations.
  - Anthropic stresses that agents are often “just LLMs using tools in a loop,” so **tool quality and documentation matter enormously**.
  - Risks include **higher cost** and **compounding errors**, so extensive sandbox testing and guardrails are recommended.

- **Where agents fit best**
  - **Customer support**
    - conversation + external data + programmatic actions
    - clear resolution criteria
    - measurable success
    - can support usage-based pricing tied to successful resolutions
  - **Software development**
    - output can be verified with automated tests
    - agents can iterate from test feedback
    - the task space is structured
    - Anthropic says its coding agent can solve real **SWE-bench Verified** GitHub issues from PR descriptions alone, though human review still matters

- **Appendix: prompt engineering your tools / ACI**
  - Tool definitions should be treated with the same care as prompts.
  - Anthropic emphasizes **agent-computer interface (ACI)** design, analogous to HCI.
  - Advice includes:
    - give the model enough tokens to think,
    - keep tool formats natural and familiar,
    - avoid formats with heavy overhead like line-counting or escaping hassles,
    - write clear descriptions and examples,
    - test how the model actually uses the tools,
    - “poka-yoke” tools to make mistakes harder.
  - Example from SWE-bench: switching from **relative filepaths** to **absolute filepaths** improved reliability.

- **Overall takeaway**
  - Start simple, measure performance, and only add multi-step agentic behavior when simpler approaches fail.
  - The goal is not maximum sophistication, but the **right system for the task**.

### Assessment
This is a high-durability technical/reference article with mixed tutorial and opinion content: it gives a practical taxonomy of agentic system patterns, recommends when to use each, and includes concrete implementation guidance for tools and interfaces. The density is high, with many specific workflows, examples, and named frameworks/models, and the piece is clearly a primary-source industry position from Anthropic rather than a synthesis. It’s best used as a refer-back reference when designing LLM systems, especially for deciding between prompt-only, workflow-based, and autonomous-agent approaches. Scrape quality appears good overall: the main content and appendices are present, though the page footer/newsletter boilerplate is included and any diagrams or code examples referenced in the text are not captured here.
