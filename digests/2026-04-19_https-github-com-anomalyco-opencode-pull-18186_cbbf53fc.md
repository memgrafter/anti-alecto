---
url: https://github.com/anomalyco/opencode/pull/18186
title: https://github.com/anomalyco/opencode/pull/18186
scraped_at: '2026-04-19T21:16:01Z'
word_count: 2672
raw_file: raw/2026-04-19_https-github-com-anomalyco-opencode-pull-18186_cbbf53fc.txt
tldr: This PR removes OpenCode’s bundled Anthropic auth/plugin support, strips Anthropic-specific prompt and beta headers, and rewrites the provider docs to say Claude Pro/Max plugins are no longer bundled as of 1.3.0 and are explicitly prohibited by Anthropic.
key_quote: Previous versions of OpenCode came bundled with these plugins but that is no longer the case as of 1.3.0
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Dax Raad
tools: []
libraries: []
companies:
- OpenCode
- Anthropic
- GitHub
- GitLab
tags:
- anthopic
- plugin-support
- documentation
- provider-integration
- policy-change
---

### TL;DR
This PR removes OpenCode’s bundled Anthropic auth/plugin support, strips Anthropic-specific prompt and beta headers, and rewrites the provider docs to say Claude Pro/Max plugins are no longer bundled as of 1.3.0 and are explicitly prohibited by Anthropic.

### Key Quote
"Previous versions of OpenCode came bundled with these plugins but that is no longer the case as of 1.3.0"

### Summary
- **What changed overall**
  - The patch removes built-in Anthropic integration from the OpenCode codebase and updates docs to reflect that Claude Pro/Max support is no longer officially bundled.
  - It also cleans up request/header behavior so Anthropic-specific logic is no longer treated specially in several code paths.

- **Code changes**
  - `packages/opencode/src/cli/cmd/providers.ts`
    - Removed the `anthropic: "API key"` hint from the provider login UI.
  - `packages/opencode/src/plugin/index.ts`
    - Deleted the hardcoded built-in plugin list:
      - `opencode-anthropic-auth@0.0.13`
    - Removed automatic insertion of bundled default plugins when `Flag.OPENCODE_DISABLE_DEFAULT_PLUGINS` is false.
  - `packages/opencode/src/provider/provider.ts`
    - Simplified Anthropic beta headers:
      - Removed `claude-code-20250219`
      - Kept only:
        - `interleaved-thinking-2025-05-14`
        - `fine-grained-tool-streaming-2025-05-14`
  - `packages/opencode/src/session/llm.ts`
    - Changed request headers so only `opencode*` providers get the special `x-opencode-*` tracing headers.
    - Removed the special-case `User-Agent: opencode/<version>` logic for non-Anthropic providers.
    - Anthropic no longer gets a separate branch here; headers are now added only when provider IDs start with `opencode`.
  - `packages/opencode/src/session/prompt/anthropic-20250930.txt`
    - Deleted the Anthropic-specific system prompt entirely.
    - That prompt contained:
      - defensive-security-only restrictions
      - guidance to use Claude Code docs via WebFetch
      - terse CLI-style response rules
      - TodoWrite/task-management instructions
      - hook behavior notes
  - `packages/web/src/content/docs/providers.mdx`
    - Removed the old auth-choice UI screenshot/text showing:
      - “Claude Pro/Max”
      - “Create an API Key”
    - Replaced the docs callout with a stronger statement:
      - plugins exist for Claude Pro/Max
      - Anthropic explicitly prohibits this
      - other providers/subscriptions supported with zero setup:
        - ChatGPT Plus
        - GitHub Copilot
        - GitLab Duo
    - Follow-up patch adds:
      - “Previous versions of OpenCode came bundled with these plugins but that is no longer the case as of 1.3.0”

- **Likely intent / impact**
  - This is both a product and policy change: OpenCode is distancing itself from bundled Anthropic/Claude Pro/Max support.
  - The docs now frame Claude Pro/Max support as plugin-based and prohibited by Anthropic, while emphasizing supported alternatives.
  - The deleted prompt suggests OpenCode previously shipped a custom Anthropic-oriented instruction file, but that path is now removed.

### Assessment
This is a high-value reference for understanding a policy-driven product change in OpenCode. Durability is medium: the broad lesson about removing bundled provider support is durable, but the specifics are tied to version `1.3.0`, Anthropic policy, and exact header/plugin implementation details that may age quickly. Content type is mixed, mostly announcement/news with implementation details and docs updates. Density is high because the patch touches several subsystems—CLI, plugins, provider headers, LLM session headers, and docs—with concrete deletions and behavior changes. Originality is primary source, since this is a patch diff from the repo itself. Reference style is refer-back: useful when checking why Claude/Anthropic support disappeared, what changed in request plumbing, or how docs now describe provider options. Scrape quality is good for the diff content shown, but partial for broader PR context because there’s no discussion thread, review comments, or linked issue text.
