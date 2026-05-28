---
url: https://docs.z.ai/guides/capabilities/thinking-mode
title: Thinking Mode - Overview - Z.AI DEVELOPER DOCUMENT
scraped_at: '2026-04-19T04:01:51Z'
word_count: 977
raw_file: raw/2026-04-19_thinking-mode-overview-z-ai-developer-document_25062bbb.txt
tldr: Z.AI’s Thinking Mode docs explain how to control GLM reasoning behavior across models and sessions, including default thinking, interleaved tool reasoning, preserved reasoning across turns, and per-turn enable/disable controls.
key_quote: Remember to return the historical `reasoning_content` to keep the reasoning coherent.
durability: high
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- OpenAI client
libraries: []
companies:
- Z.AI
tags:
- llm-reasoning
- tool-calling
- api-documentation
- session-state
- prompt-engineering
---

### TL;DR
Z.AI’s Thinking Mode docs explain how to control GLM reasoning behavior across models and sessions, including default thinking, interleaved tool reasoning, preserved reasoning across turns, and per-turn enable/disable controls.

### Key Quote
“Remember to return the historical `reasoning_content` to keep the reasoning coherent.”

### Summary
- This is a **developer documentation page** for Z.AI’s **Thinking Mode** capability in GLM models.
- It says GLM supports **multiple thinking modes** for different scenarios, and the page covers:
  - default thinking behavior
  - interleaved thinking
  - preserved thinking
  - turn-level thinking
  - example usage
- **Default thinking behavior**
  - Thinking is **enabled by default in GLM-5 and GLM-4.7**.
  - This differs from the **default hybrid thinking in GLM-4.6**.
  - To disable thinking, set:
    ```json
    "thinking": { "type": "disabled" }
    ```
- **Interleaved thinking**
  - Supported **by default since GLM-4.5**.
  - Lets the model think **between tool calls** and **after tool results**.
  - Intended for multi-step reasoning, interpreting tool outputs, and chaining calls.
  - Important requirement: **thinking blocks must be explicitly preserved and returned together with tool results**.
- **Preserved thinking**
  - Introduced in **GLM-5 and GLM-4.7** for coding scenarios.
  - The model can retain reasoning from previous assistant turns to preserve continuity and improve performance/cache hit rates.
  - It is:
    - **enabled by default** on the **Coding Plan endpoint**
    - **disabled by default** on the **standard API endpoint**
  - To enable it on the API endpoint, set:
    - `"clear_thinking": false`
  - You must return the **complete, unmodified `reasoning_content`** back to the API.
  - All consecutive `reasoning_content` blocks must **exactly match the original sequence**; do not reorder or edit them.
- **Turn-level thinking**
  - Introduced in **GLM-4.7**.
  - Lets you independently enable or disable reasoning **per request within the same session**.
  - Benefits:
    - better **cost/latency control**
    - smoother multi-turn experience
    - better behavior in **agent/tool-use scenarios**
  - The doc frames it as: use thinking for hard tasks, disable it for lightweight turns.
- **Example usage**
  - Shows a Python example using the **OpenAI client** with:
    - `base_url="https://api.z.ai/api/paas/v4/"`
    - model `"glm-4.7"`
    - a function tool called `get_weather`
    - streaming responses
    - `extra_body={"thinking": {"type": "enabled", "clear_thinking": False}}`
  - The sample code:
    - collects `reasoning_content`, `content`, and `tool_calls` from streamed chunks
    - appends the assistant message back with `reasoning_content`
    - sends a tool response
    - then makes a second request to continue reasoning and produce the final reply
- The page emphasizes that the same usage applies to both **Interleaved Thinking** and **Preserved Thinking**; the developer should simply **return historical reasoning content** to keep the reasoning coherent.

### Assessment
This is a **reference** document with moderate-to-high durability: the core ideas about reasoning modes and tool-call handling are useful long term, but the exact defaults and model names are version-dependent and likely to change as GLM releases evolve. The content type is **mixed** but mostly **technical reference/tutorial**, with a high density of actionable configuration details, parameter names, and code. It appears to be **primary source** documentation from Z.AI rather than commentary or aggregation. Best used as a **refer-back** resource when integrating GLM thinking features or debugging tool-call flows. Scrape quality is **good** overall: the main sections and code example are present, though the page also includes navigation chrome and images/diagrams whose visual details are not captured in the text.
