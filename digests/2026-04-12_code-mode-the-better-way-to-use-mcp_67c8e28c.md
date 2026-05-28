---
url: https://blog.cloudflare.com/code-mode/
title: 'Code Mode: the better way to use MCP'
scraped_at: '2026-04-12T07:27:50Z'
word_count: 2917
raw_file: raw/2026-04-12_code-mode-the-better-way-to-use-mcp_67c8e28c.txt
tldr: Cloudflare argues that LLM agents should use MCP servers by writing TypeScript code against a generated API in a sandbox, rather than by directly emitting tool calls, and introduces Cloudflare Agents SDK “code mode” plus a Dynamic Worker Loader API to make this work securely.
key_quote: LLMs are better at writing code to call MCP, than at calling MCP directly.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Wrangler
- workerd
- streamText
libraries:
- ai-sdk
companies:
- Cloudflare
tags:
- model-context-protocol
- ai-agents
- typescript
- cloudflare-workers
- sandboxing
---

### TL;DR
Cloudflare argues that LLM agents should use MCP servers by writing TypeScript code against a generated API in a sandbox, rather than by directly emitting tool calls, and introduces Cloudflare Agents SDK “code mode” plus a Dynamic Worker Loader API to make this work securely.

### Key Quote
“LLMs are better at writing code to call MCP, than at calling MCP directly.”

### Summary
- **Core thesis:** The post claims most MCP usage is “wrong” because agents directly expose tools to the LLM; instead, MCP tools should be converted into a **TypeScript API** and the LLM should write code that calls that API.
- **Why this is better:**
  - LLMs have seen **far more real-world TypeScript/code** than synthetic tool-call formats.
  - Code can chain many tool calls without repeatedly sending intermediate results back through the LLM, reducing **tokens, time, and energy**.
  - The approach is especially strong for agents that need to **compose multiple calls**.
- **MCP explained:**
  - MCP = **Model Context Protocol**, a standard for giving AI agents access to external tools.
  - It can be viewed as a uniform way to:
    - expose an API,
    - provide documentation for LLM understanding,
    - handle authorization out-of-band.
  - MCP tools are basically **RPC-style functions** with parameters and responses.
- **How direct tool calling works:**
  - LLMs output special tool-call tokens plus a JSON structure describing the call.
  - The harness intercepts the tool call, invokes the MCP server, then returns the result to the model using special result tokens.
- **What Cloudflare says is wrong with direct tool calling:**
  - Tool-call tokens are **synthetic** and not common in natural training data.
  - Models can struggle when there are **many tools** or **complex tools**.
  - MCP server authors often have to **simplify APIs** to make tool calling work well.
- **Why MCP is still useful even in code mode:**
  - MCP’s biggest value is **uniformity**:
    - consistent connectivity,
    - consistent authorization,
    - documentation embedded in the protocol,
    - no need for the AI to search the internet for docs.
  - This uniform layer remains useful even if the model is writing code rather than tool calls.
- **Cloudflare’s implementation:**
  - The Cloudflare Agents SDK now supports **`codemode`**.
  - Example usage:
    - wrap existing `system` prompt and `tools` with `codemode(...)`,
    - then feed the returned `system` and `tools` into `streamText(...)`.
  - Result: the app generates and runs **code** that calls the tools, including MCP servers.
- **How MCP becomes TypeScript:**
  - In code mode, the SDK fetches an MCP server schema and converts it into a **TypeScript API** with doc comments.
  - The post shows a generated interface/API for `gitmcp.io/cloudflare/agents`, including methods like:
    - `fetch_agents_documentation`
    - `search_agents_documentation`
    - `search_agents_code`
    - `fetch_generic_url_content`
  - The full API is currently loaded into context, though future versions may browse/search it more dynamically.
- **Execution model:**
  - The agent is given a single tool: run **TypeScript code**.
  - Code runs in a **secure sandbox**.
  - The sandbox has **no direct internet access**; it can only use the TypeScript APIs representing connected MCP servers.
  - Output is returned via `console.log()`.
- **Sandbox/runtime infrastructure:**
  - Cloudflare says this uses **V8 isolates**, not containers.
  - Isolates start in **milliseconds** and use only a few megabytes of memory.
  - Cloudflare claims it can create a new isolate **per code snippet**, making reuse/prewarming unnecessary.
- **Worker Loader API:**
  - Cloudflare introduces a new API for **loading Worker code on demand**.
  - The example shows `env.LOADER.get(id, async () => { ... })`, where the loader:
    - supplies module code,
    - sets `compatibilityDate`,
    - configures `env`,
    - wires RPC bindings via `ctx.exports`,
    - optionally proxies or blocks outbound internet via `globalOutbound`.
  - Supports getting entrypoints and invoking methods like `fetch()`.
  - It is available **locally now** with Wrangler/workerd and in **closed beta** for production.
- **Why Workers are “better sandboxes” according to the post:**
  - **Faster/cheaper/disposable:** isolates are lighter than containers and suitable for one-off execution.
  - **Isolated but connected:** private access should be granted through **bindings**, not generic network access.
  - **No API keys leak:** bindings provide already-authorized access, so code doesn’t need to handle secrets directly.
- **Security model:**
  - The sandbox cannot use `fetch()` or `connect()` to reach the internet.
  - It can only call approved bindings corresponding to MCP servers.
  - This is presented as cleaner than network filtering or HTTP proxying.
- **Availability / call to action:**
  - Cloudflare invites users to **sign up for the production beta** of Dynamic Worker Loader API.
  - Local experimentation is available now via **Wrangler** and **workerd**.
  - Readers are directed to the docs for **Dynamic Worker Loading** and **code mode**.

### Assessment
This is a **mixed** technical/product announcement and opinion piece with a clear thesis: Cloudflare is proposing a new agent pattern built around TypeScript code generation and sandboxed execution instead of direct MCP tool calls. Durability is **medium** because the core idea about code being better than raw tool calls may age well, but much of the article is tied to current Cloudflare products, APIs, and beta status. Density is **high**: it includes conceptual explanation, an extended product pitch, code snippets, API examples, and security/runtime details. Originality is mainly **primary source** with some architectural commentary; it is Cloudflare’s own explanation of its design choices and new features. Reference style is **refer-back** for anyone evaluating MCP agent architecture or Cloudflare’s implementation, and possibly **deep-study** for those building agents on Workers. Scrape quality looks **good** overall: the article appears substantially captured, including prose and code blocks, though embedded images or interactive docs are not present here.
