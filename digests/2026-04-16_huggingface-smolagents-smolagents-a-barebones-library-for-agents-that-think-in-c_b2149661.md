---
url: https://github.com/huggingface/smolagents/tree/main
title: 'huggingface/smolagents: 🤗 smolagents: a barebones library for agents that think in code.'
scraped_at: '2026-04-16T03:59:04Z'
word_count: 1504
raw_file: raw/2026-04-16_huggingface-smolagents-smolagents-a-barebones-library-for-agents-that-think-in-c_b2149661.txt
tldr: smolagents is Hugging Face’s small, code-first agent library for building LLM agents with minimal abstractions, broad model/tool support, and sandboxed execution options.
key_quote: Agents that think in code!
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Aymeric Roucher
- Albert Villanova del Moral
- Thomas Wolf
- Leandro von Werra
- Erik Kaunismäki
tools:
- Blaxel
- E2B
- Modal
- Docker
- Pyodide
- Deno
- LangChain
- MCP
- helium
- LiteLLM
libraries:
- transformers
- ollama
companies:
- Hugging Face
- OpenAI
- Anthropic
- Together AI
- OpenRouter
- Amazon Bedrock
- Azure
tags:
- ai-agents
- code-generation
- llm-tools
- sandboxing
- agent-frameworks
---

### TL;DR
`smolagents` is Hugging Face’s small, code-first agent library for building LLM agents with minimal abstractions, broad model/tool support, and sandboxed execution options.

### Key Quote
"Agents that think in code!"

### Summary
- **What it is**
  - An open-source library from Hugging Face for building agents “in a few lines of code.”
  - Emphasizes keeping the core implementation small: the main logic in `agents.py` is said to be under 1,000 lines.
  - Positioned as a minimal framework that stays close to raw Python code rather than heavy abstractions.

- **Core idea: Code agents**
  - The flagship approach is `CodeAgent`, where the model writes actions as **Python code snippets** instead of emitting structured tool-call JSON.
  - Tool calls become ordinary Python function calls inside generated code.
  - The repo claims this approach:
    - uses **30% fewer steps**
    - means **30% fewer LLM calls**
    - performs better on difficult benchmarks
  - It also includes the more traditional `ToolCallingAgent` for JSON/text-style tool use.

- **Safety / execution**
  - Since code execution is inherently risky, the library supports running agents in sandboxed environments.
  - Supported sandbox options mentioned:
    - **Blaxel**
    - **E2B**
    - **Modal**
    - **Docker**
    - **Pyodide + Deno WebAssembly**
  - The built-in `LocalPythonExecutor` is explicitly **not** a security boundary and should not be used for untrusted code.

- **Model support**
  - The library is described as **LLM-agnostic** and supports many backends:
    - local `transformers`
    - `ollama`
    - Hugging Face inference providers
    - OpenAI
    - Anthropic
    - other providers via **LiteLLM**
    - Azure OpenAI
    - Amazon Bedrock
    - OpenAI-compatible servers such as Together AI and OpenRouter
  - Example model classes shown:
    - `InferenceClientModel`
    - `LiteLLMModel`
    - `OpenAIModel`
    - `TransformersModel`
    - `AzureOpenAIModel`
    - `AmazonBedrockModel`

- **Tool support**
  - Tool-agnostic design: tools can come from multiple ecosystems.
  - Mentioned integrations:
    - **MCP servers**
    - **LangChain**
    - **Hub Spaces** as tools
    - tools and agents shared via the **Hugging Face Hub**

- **Quick start**
  - Installation command:
    - `pip install "smolagents[toolkit]"`
  - Minimal example:
    - create an `InferenceClientModel`
    - build a `CodeAgent` with `WebSearchTool()`
    - run a natural-language task like estimating how long a leopard would take to run through Pont des Arts
  - Agents can be pushed to or loaded from the Hub:
    - `agent.push_to_hub("m-ric/my_agent")`
    - `agent.from_hub("m-ric/my_agent")`

- **CLI**
  - Two command-line entry points:
    - `smolagent` — general-purpose multi-step `CodeAgent`
    - `webagent` — a specialized web-browsing agent using **helium**
  - `smolagent` can be run with a prompt plus options like model type, model ID, imports, and tools.
  - Interactive mode launches a setup wizard for:
    - agent type
    - tool selection
    - model configuration
    - advanced imports
    - task prompt
  - `webagent` is shown with an example browsing task and region-specific shopping behavior.

- **How it works**
  - The repo includes a mermaid flowchart showing a ReAct-like loop:
    - user task is stored in memory
    - model generates code
    - code is parsed and executed
    - logs are stored back in memory until `final_answer` is called
  - Example of multi-step tool use in one action is given with repeated web searches over several queries.
  - The library highlights that code-form actions make it easier to batch operations and reuse normal Python control flow.

- **Broader positioning**
  - The project argues that a framework is useful because consistent code formatting, parsing, prompt design, and execution handling are non-trivial.
  - It invites users to hack into the source and use only the pieces they need.
  - It also claims open models can now compete strongly in agentic workflows, citing a benchmark comparing code agents across models.

- **Benchmarking**
  - The repo references a benchmark dataset:
    - `m-ric/agents_medium_benchmark_2`
  - It links benchmarking code in:
    - `examples/smolagents_benchmark/run.py`
  - The page claims the comparison shows open-source models can take on the best closed models, with a visual noting DeepSeek-R1 performing strongly.

- **Security and contribution**
  - Security is emphasized as a central concern for code-executing agents.
  - Users are pointed to `SECURITY.md` for policies and vulnerability reporting.
  - Contributions are welcomed via the contribution guide.

- **Citation**
  - A BibTeX citation is provided for academic use.
  - The citation lists authors including:
    - Aymeric Roucher
    - Albert Villanova del Moral
    - Thomas Wolf
    - Leandro von Werra
    - Erik Kaunismäki
  - Year listed: **2025**

### Assessment
This is a **mixed** reference/documentation and promotional repo overview with fairly high durability because the architectural ideas—code-first agents, sandboxed execution, tool/model agnosticism—are general patterns, though some concrete examples and model names will age quickly. The content is **high density** in the sections that explain CodeAgent, sandboxing, CLI commands, and supported integrations, but it also includes marketing-style claims and benchmark positioning, so it should be read as both documentation and advocacy. It is **primary source** material from the project maintainers, which makes it useful for evaluating intent and supported features, but some claims about performance are contextual and may depend on external benchmarks. This is best used **refer-back**: enough detail to quickly understand the library and confirm whether it fits a use case, while the full docs would be needed for implementation. Scrape quality is **good** overall: the README content is present, including code examples, details, and links, though images and external linked pages are not themselves captured here.
