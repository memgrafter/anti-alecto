---
url: https://github.com/memgrafter/flatagents/tree/main/sdk/examples/openai_codex_oauth/python
title: flatagents/sdk/examples/openai_codex_oauth/python at main · memgrafter/flatagents
scraped_at: '2026-04-19T06:49:16Z'
word_count: 105
raw_file: raw/2026-04-19_flatagents-sdk-examples-openai-codex-oauth-python-at-main-memgrafter-flatagents_8878a164.txt
tldr: A Python example for FlatAgents showing how to authenticate OpenAI Codex via OAuth, verify the saved credentials, and run a Codex-backed agent call.
key_quote: Browser/callback login (`--login-codex`)
durability: medium
content_type: tutorial
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- openai codex
- flatagents
libraries: []
companies:
- memgrafter
tags:
- oauth
- authentication
- command-line
- github-example
- agent-workflow
---

### TL;DR
A Python example for FlatAgents showing how to authenticate OpenAI Codex via OAuth, verify the saved credentials, and run a Codex-backed agent call.

### Key Quote
“Browser/callback login (`--login-codex`)”

### Summary
- This is a **GitHub example directory** for **`openai_codex_oauth` in Python** under `memgrafter/flatagents`.
- It demonstrates three main actions:
  - **Browser/callback login** with `--login-codex`
  - **Auth diagnostics** with `--check-codex-auth`
  - **A real agent invocation** using `backend: codex` with `--run`
- The default authentication file is:
  - `~/.agents/flatmachines/auth.json`
- Basic local usage:
  - `cd sdk/examples/openai_codex_oauth/python`
  - `./run.sh --local -- --check-codex-auth`
  - `./run.sh --local -- --login-codex`
  - `./run.sh --local -- --run --prompt "Reply with CODEX_OK"`
- It also documents **remote-machine login** when browser-based OAuth is inconvenient:
  - Use `--paste-callback-url` and `--no-browser` to paste the callback URL/code manually.
  - Alternatively, pass the callback URL/code directly with `--callback-url "http://localhost:1455/auth/callback?..." --no-browser`
  - If state mismatch problems occur, the docs suggest passing only the code value, e.g. `--callback-url "ac_xxx..." --no-browser`
- The page is mostly a **usage reference** for one example, not a conceptual explanation of OAuth or Codex.

### Assessment
Durability is **medium** because the OAuth flow and example structure are useful patterns, but the exact flags, auth file path, and Codex backend integration are tied to this repository and may change with future versions. The content type is **reference/tutorial**: it gives concrete commands and workflow steps rather than theory. Density is **medium**—short but specific, with actionable CLI examples and login variants. Originality is **primary source**, since it appears to be repository documentation for the example itself. It is best used **refer-back** when you need to run or troubleshoot this exact example. Scrape quality is **good** for the visible text; no code blocks or sections appear missing from the provided content.
