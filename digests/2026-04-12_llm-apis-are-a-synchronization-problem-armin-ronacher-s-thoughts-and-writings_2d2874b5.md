---
url: https://lucumr.pocoo.org/2025/11/22/llm-apis/
title: LLM APIs are a Synchronization Problem | Armin Ronacher's Thoughts and Writings
scraped_at: '2026-04-12T07:26:33Z'
word_count: 1530
raw_file: raw/2026-04-12_llm-apis-are-a-synchronization-problem-armin-ronacher-s-thoughts-and-writings_2d2874b5.txt
tldr: Armin Ronacher argues that LLM provider APIs should be thought of as distributed state synchronization systems, not just message-passing interfaces, because hidden provider state, KV caches, injected context, and replay/failure semantics make “chat” abstractions misleading.
key_quote: Maybe it’s time to start thinking about what a state synchronization API would look like, rather than a message-based API.
durability: high
content_type: opinion
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Armin Ronacher
tools:
- OpenAI Responses API
- OpenRouter
- Vercel AI SDK
- Ollama
- MCP
libraries: []
companies:
- OpenAI
- Anthropic
- OpenRouter
- Vercel
- Ollama
tags:
- llm-apis
- state-synchronization
- agent-infrastructure
- distributed-systems
- local-first
---

### TL;DR
Armin Ronacher argues that LLM provider APIs should be thought of as distributed state synchronization systems, not just message-passing interfaces, because hidden provider state, KV caches, injected context, and replay/failure semantics make “chat” abstractions misleading.

### Key Quote
“Maybe it’s time to start thinking about what a state synchronization API would look like, rather than a message-based API.”

### Summary
- **Main thesis:** Current LLM APIs expose a message-based abstraction that hides the real problem: synchronizing partially hidden state between client and provider.
- **Core model framing:**
  - At the lowest level, an LLM processes tokens through fixed weights, activations, and attention layers.
  - Conversation state is not just visible message history; it also includes derived internal state like the GPU KV cache.
  - Replaying the same tokens restores text context, but not necessarily the exact derived state.
- **Why completion-style APIs are awkward:**
  - You resend the full prompt history on each turn.
  - This makes per-request size grow linearly with conversation length, while total transmitted data over a long chat grows quadratically.
  - Providers also inject hidden tokens and context such as:
    - prompt templates
    - role markers
    - tool definitions
    - provider-side tool outputs
    - cache points
    - reasoning/search-related hidden state
- **Problems with hidden state:**
  - Some provider APIs hide reasoning tokens or search-result injection details.
  - In some cases, the client receives an opaque/encrypted blob that must be sent back to continue the conversation.
  - This makes synchronization fragile when there is divergence, corruption, or network failure.
- **Responses API critique:**
  - OpenAI’s Responses API with saved state moves conversation history to the server.
  - Ronacher says this creates a more explicit synchronization problem with hidden server state and limited client control.
  - He reports seeing the API get stuck in unrecoverable ways and says it is unclear how long a conversation can safely continue or what happens on partition/divergence.
- **Ecosystem/tooling observation:**
  - Intermediaries like OpenRouter and SDKs like Vercel AI SDK can mask provider differences, but they cannot unify the underlying hidden state semantics.
  - The hardest part of “unifying” LLM APIs is not visible message format; it is incompatible hidden state management.
- **Local-first analogy:**
  - Ronacher compares the problem to local-first systems, which handle offline use, forks, merges, conflict resolution, and healing.
  - He suggests LLM systems may need similar concepts:
    - canonical state
    - derived state
    - transport mechanics
    - replay
    - synchronization boundaries
    - failure handling
- **Potential standardization direction:**
  - If standards emerge, they should reflect how models actually work rather than preserve current UI/message conventions.
  - A future standard should account for hidden state, replayability, and failure modes.
- **Overall stance:**
  - He is skeptical that the current message-based API paradigm is the right long-term abstraction.
  - He doubts the status quo will survive, especially as agents and provider-side hidden state become more central.

### Assessment
This is a **high-durability** opinion/technical essay: it’s tied to current LLM API design, but the underlying ideas about distributed state, replay, and synchronization are broadly reusable and likely to remain relevant. The piece is **dense** and conceptually rich, with specific references to OpenAI’s completion-style APIs, the Responses API with saved state, MCP, OpenRouter, Vercel AI SDK, and local-first systems. It is **original commentary** rather than a synthesis or reference doc, presenting one author’s architectural argument and critique. Best treated as **refer-back** material if you work on LLM tooling, API design, or agent infrastructure; it’s not a tutorial. Scrape quality appears **good**: the text is complete and coherent, though no code blocks or diagrams are present, so there doesn’t seem to be missing technical material from the excerpt provided.
