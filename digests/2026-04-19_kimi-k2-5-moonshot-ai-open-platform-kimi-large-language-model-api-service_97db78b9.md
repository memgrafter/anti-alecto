---
url: https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart
title: Kimi K2.5 - Moonshot AI Open Platform - Kimi Large Language Model API Service
scraped_at: '2026-04-19T03:55:02Z'
word_count: 2067
raw_file: raw/2026-04-19_kimi-k2-5-moonshot-ai-open-platform-kimi-large-language-model-api-service_97db78b9.txt
tldr: Kimi K2.5 is Moonshot AI’s multimodal, 256K-context flagship model, and this quickstart shows how to use it via the OpenAI-compatible API for text, images, video, and tool-calling, including how to disable thinking mode.
key_quote: “Kimi K2.5 is Kimi’s most intelligent model to date, achieving open-source SoTA performance in Agent, code, visual understanding, and a range of general intelligent tasks.”
durability: medium
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- openai
- ffprobe
- ffmpeg
libraries: []
companies:
- Moonshot AI
tags:
- multimodal-ai
- api-integration
- tool-calling
- context-window
- model-pricing
---

### TL;DR
Kimi K2.5 is Moonshot AI’s multimodal, 256K-context flagship model, and this quickstart shows how to use it via the OpenAI-compatible API for text, images, video, and tool-calling, including how to disable thinking mode.

### Key Quote
“Kimi K2.5 is Kimi’s most intelligent model to date, achieving open-source SoTA performance in Agent, code, visual understanding, and a range of general intelligent tasks.”

### Summary
- **What Kimi K2.5 is**
  - Moonshot AI positions `kimi-k2.5` as its most intelligent and most versatile model.
  - It has a **native multimodal architecture** supporting:
    - text
    - image
    - video
    - thinking and non-thinking modes
    - dialogue and Agent tasks
  - The page links to a tech blog for more background.

- **Notable capabilities**
  - **Coding:** claimed breakthrough in frontend code quality and design expressiveness.
    - The model can generate **interactive user interfaces** from natural language.
    - It is described as handling complex visual effects like dynamic layouts and scrolling animations.
  - **Context window:** several models, including `kimi-k2.5`, support **256K context**.
  - **Reasoning:** supports **multi-step tool invocation** and complex reasoning, including math and code.

- **Getting started**
  - Kimi API is **OpenAI SDK compatible**.
  - Install:
    ```bash
    pip install --upgrade 'openai>=1.0'
    ```
  - Verify installation:
    ```bash
    python -c 'import openai; print("version =",openai.__version__)'
    ```

- **Quick start links**
  - “Try it now” links to the playground / Dev Workbench.
  - “Apply for API Key” links to the console API key page.

- **Image understanding example**
  - Shows Python code using `openai.OpenAI` with:
    - `base_url="https://api.moonshot.ai/v1"`
    - `api_key=os.environ.get("MOONSHOT_API_KEY")`
  - Images are sent as a **base64 data URL** inside a multimodal `messages` payload.
  - The user message content is a list combining:
    - `{"type": "image_url", ...}`
    - `{"type": "text", ...}`
  - Example model call:
    - `model="kimi-k2.5"`

- **Video understanding example**
  - Same pattern as images, but with:
    - `{"type": "video_url", ...}`
  - Video is base64-encoded into a `data:video/...;base64,...` URL.
  - The prompt asks the model to describe the video content.

- **Multimodal tool-calling example**
  - Demonstrates an agent loop using a custom function tool:
    - `watch_video_clip(path, start_time=None, end_time=None)`
  - The tool:
    - checks that the file exists
    - optionally uses `ffprobe` to determine duration
    - uses `ffmpeg` to extract a clip
    - returns multimodal tool output containing:
      - a `video_url`
      - a text label describing the clip
  - The agent loop:
    - calls `client.chat.completions.create(...)` with `tools=tools` and `tool_choice="auto"`
    - executes returned tool calls
    - appends tool results back into the conversation
  - Example user request:
    - “Analyze what happens between seconds 8-13 in ~/Download/test_video.mp4”

- **Supported formats and constraints**
  - **Images:** png, jpeg, webp, gif
  - **Videos:** mp4, mpeg, mov, avi, x-flv, mpg, webm, wmv, 3gpp
  - **Image quantity:** no hard limit, but request body must stay under **100M**
  - **URL-formatted images:** not supported; only **base64-encoded** image content is supported
  - For very large videos, the docs recommend **file upload** instead of embedding base64 in the request body.

- **Token usage and billing**
  - Image/video token usage is **dynamically calculated**.
  - It recommends using the **token estimation API** before sending requests with media.
  - More resolution and more video keyframes mean more tokens.
  - Billing follows the same general method as `moonshot-v1`: based on total tokens processed.
  - Pricing is referenced via the pricing docs.

- **Recommended resolution**
  - Images: no higher than **4K (4096×2160)**
  - Videos: no higher than **2K (2048×1080)**
  - Higher resolutions increase processing time without improving understanding.

- **Request parameter differences for k2.5**
  - Default recommended settings are preferred over manual tuning.
  - `max_tokens`: default **32k (32768)**
  - `thinking`: optional, default enabled; can be:
    - `{"type": "enabled"}`
    - `{"type": "disabled"}`
  - `temperature`:
    - fixed to **1.0** in k2.5
    - **0.6** in non-thinking mode
    - other values error
  - `top_p`: fixed **0.95**
  - `n`: fixed **1**
  - `presence_penalty`: fixed **0.0**
  - `frequency_penalty`: fixed **0.0**

- **Tool-use compatibility notes**
  - When thinking is enabled:
    - `tool_choice` must be `auto` or `none`
    - assistant `reasoning_content` must be preserved across multi-step tool calls
    - the built-in `$web_search` tool is temporarily incompatible with thinking mode
  - The docs recommend disabling thinking first if you need web search.

- **How to disable thinking**
  - cURL example:
    ```json
    "thinking": {"type": "disabled"}
    ```
  - Python example uses `extra_body={"thinking": {"type": "disabled"}}`
  - The sample sets:
    - `model="kimi-k2.5"`
    - `max_tokens=1024*32`

- **Pricing**
  - For `kimi-k2.5`:
    - Unit: **1M tokens**
    - Input price (cache hit): **$0.10**
    - Input price (cache miss): **$0.60**
    - Output price: **$3.00**
    - Context window: **262,144 tokens**

- **Related docs**
  - Benchmark best practice
  - How to use Kimi Vision Model
  - Agent support for Claude Code, Roo Code, and Cline
  - Thinking model guide
  - Web search and official tools docs
  - Pricing and billing/rate limit pages

### Assessment
This is a **tutorial/reference** page with fairly high technical density and good practical detail, especially for API usage, multimodal payload structure, and tool-calling constraints. Its **durability is medium**: the general patterns are useful for a while, but parameter defaults, tool compatibility notes, pricing, and model claims may change as the platform evolves. The content is a **primary source** from Moonshot AI, so it is authoritative for current platform behavior, though some sections are clearly promotional (for example, “most intelligent model to date” and performance claims). It is best used as a **refer-back** reference when implementing or debugging Kimi K2.5 integration. **Scrape quality is good** overall: the page appears complete enough for the main documentation, with code blocks, tables, and key sections preserved, though embedded images are represented only by links and there may be minor formatting artifacts.
