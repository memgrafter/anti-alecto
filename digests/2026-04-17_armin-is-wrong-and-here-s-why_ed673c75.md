---
url: https://mariozechner.at/posts/2025-11-22-armin-is-wrong/
title: Armin is wrong and here's why
scraped_at: '2026-04-17T05:19:09Z'
word_count: 2185
raw_file: raw/2026-04-17_armin-is-wrong-and-here-s-why_ed673c75.txt
tldr: Mario Zechner argues that LLM “messages” are not a fake abstraction hiding a cleaner state model; the real issue is that closed providers hide internal state, so local-first thinking only makes sense for the client’s own canonical log, not the provider’s black box.
key_quote: Under a local-first lens, you have to treat that server session as a cache and store the full session state on your side instead.
durability: high
content_type: opinion
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people:
- Mario Zechner
- Armin
tools:
- OpenAI Responses API
- CRDT
libraries: []
companies:
- OpenAI
tags:
- llm-apis
- local-first
- state-synchronization
- provider-internals
- agent-systems
---

### TL;DR
Mario Zechner argues that LLM “messages” are not a fake abstraction hiding a cleaner state model; the real issue is that closed providers hide internal state (thinking traces, caches, VM/container state), so local-first thinking only makes sense for the client’s own canonical log, not the provider’s black box.

### Key Quote
“Under a local-first lens, you have to treat that server session as a cache and store the full session state on your side instead.”

### Summary
- **Context / stance**
  - This is a rebuttal to “Armin” (the linked post is not included here), written as a conversational critique from one friend to another.
  - The author’s thesis: Armin is wrong to frame LLM APIs as fundamentally a state synchronization problem in a local-first / CRDT sense.

- **Main argument: messages are not the problem**
  - Zechner argues that the **messages abstraction is baked into model training and prompt templates**; it is not merely a superficial API layer hiding a simpler underlying system.
  - For open-weight models, token sequences still need to conform to the chat template the model was trained on.
  - He claims that a “cleaner” API than JSON message formatting is unlikely to matter in practice.

- **Hidden server state exists, but it is not sync state in the local-first sense**
  - Providers increasingly hide state in opaque server-side features:
    - **Thinking blobs / traces**
    - **Server-side tool result blobs / IDs**
    - **Prefix cache markers**
    - **Responses-style server-managed sessions**
    - **VM/container state for agent execution**
  - His argument is that, from the client’s perspective, this is mostly just **echoing provider-issued opaque data back to the server**.
  - He compares this to **HTTP-only cookies**: client stores server-issued state keys, but that does not make the system a peer-to-peer sync problem.

- **Switching providers is awkward, but not a CRDT problem**
  - If you move from one provider to another mid-session, you may need to discard or reformat opaque server-specific state.
  - Zechner says this is an interoperability limitation, not something local-first/CRDT techniques can solve.
  - Provider caches and hidden state are not transferable across vendors, and likely never will be.

- **Quadratic retransmission is real, but still not sync**
  - He agrees that completion-style APIs require resending the prompt history each turn, causing **quadratic cumulative egress** over time.
  - He says providers mitigate this with file/image upload APIs, making the extra bytes manageable because text/tool results are small relative to attachments.
  - Again, he frames this as **resource management**, not a synchronization problem.

- **Responses API critique**
  - He criticizes OpenAI’s **Responses API** implementation as not great and poorly documented, especially around **network splits**.
  - The API can be used with `store: false`, which returns responsibility for full observable state management to the client.
  - His view: if the server-managed state becomes inaccessible, your fallback is basically a restart.

- **Most serious case: provider-managed VMs / containers**
  - He says provider-run execution environments are the biggest problem:
    - The model can create files, artifacts, modify environment state, and rely on that state across turns.
    - This hidden state can be **catastrophic** to lose for an agent run.
  - His solution is not CRDTs, but to **manage containers and artifact storage yourself** as part of your own canonical state.

- **Where local-first still applies**
  - Zechner concedes that **local-first is useful on the client side**:
    - Keep your own canonical state as messages, tool calls, and file references.
    - Treat provider-side state as transient, lossy scratchpad state.
    - Make correctness and recovery depend only on what you control.
  - He explicitly says:
    - **Thinking traces are nice-to-have**
    - **Prefix cache is just an optimization**
    - **Server-side session stores are effectively caches from the client perspective**

- **Bottom line**
  - For closed SaaS LLMs, providers will continue hiding internal state for IP and architectural reasons.
  - Local-first cannot force providers to expose replayable internal state.
  - Therefore, the practical strategy is:
    - keep your own replayable log,
    - treat provider internals as black-box derived state,
    - and avoid depending on hidden state for correctness or recovery.

### Assessment
This is a high-durability opinion piece with a medium-to-high density of concrete API and systems examples (messages, prefix caching, Responses API, file uploads, VM/container state, `store: false`). It is original commentary/rebuttal rather than a neutral reference or synthesis. The intended use is mainly refer-back or deep-study if you care about LLM API design, provider-managed state, or local-first architectures. Scrape quality is good: the main essay content is present, including quoted examples and the key technical arguments, though the linked opposing post is not included.
