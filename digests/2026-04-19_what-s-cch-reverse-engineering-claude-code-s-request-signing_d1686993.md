---
url: https://a10k.co/b/reverse-engineering-claude-code-cch.html
title: What's cch? Reverse Engineering Claude Code's Request Signing
scraped_at: '2026-04-19T07:32:53Z'
word_count: 2254
raw_file: raw/2026-04-19_what-s-cch-reverse-engineering-claude-code-s-request-signing_d1686993.txt
tldr: This post reverse-engineers Claude Code’s “fast mode” request signing, showing that a hidden `cch` field is filled by Bun’s native runtime with a seeded `xxHash64` over the full JSON body, while `cc_version` gets a 3-hex suffix derived in JavaScript from the first user message.
key_quote: From JavaScript’s perspective, it’s magic.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- mitmproxy
- lldb
- bun
- fetch
libraries:
- xxHash64
- xxhash
companies:
- Anthropic
- Oven
tags:
- reverse-engineering
- request-signing
- claude-code
- bun-runtime
- api-security
---

### TL;DR
This post reverse-engineers Claude Code’s “fast mode” request signing, showing that a hidden `cch` field is filled by Bun’s native runtime with a seeded `xxHash64` over the full JSON body, while `cc_version` gets a 3-hex suffix derived in JavaScript from the first user message.

### Key Quote
“From JavaScript’s perspective, it’s magic.”

### Summary
- The article investigates the mysterious `x-anthropic-billing-header` injected into Claude Code requests:
  - `cc_version=2.1.37.fbe`
  - `cc_entrypoint=cli`
  - `cch=a112b`
- It claims `cch` is a request-integrity hash used to gate features like fast mode; if it is wrong, the API rejects the request with a fast-mode-related error.
- The research was done by:
  - intercepting requests with `mitmproxy`
  - extracting the bundled JavaScript from the Bun executable
  - attaching LLDB and setting memory watchpoints
- They found the JavaScript only writes `cch=00000`; the real value is inserted later by Bun’s native `fetch` implementation.
- The custom Bun build allegedly mutates the request body string in place during `fetch()`, which the post describes as a JavaScript spec violation.
- The native signing logic is described as:
  - trigger only when the URL contains `/v1/messages`
  - `anthropic-version` header is present
  - the body contains `cch=00000`
  - compute `xxHash64` over the serialized body
  - mask to `0xFFFFF`
  - format as a 5-character lowercase hex string
  - replace the placeholder in the body
- They used 142 input/output oracle pairs and ruled out common hashes like SHA-256, SHA-1, MD5, CRC32, and wyhash before identifying the algorithm.
- The version suffix logic for `cc_version` is described as:
  - take the first user message
  - extract characters at positions 4, 7, and 20, padding with `0` if missing
  - concatenate `salt + picked_chars + version`
  - SHA-256 hash it
  - take the first 3 hex characters
- The article includes a validation table claiming the hash covers the entire serialized request body:
  - replay succeeds
  - editing system prompt non-billing blocks succeeds
  - changing session UUID, tools array, tool descriptions, adding MCP tools, or emptying tools array causes `400`
- It argues this is not DRM but a billing/attribution mechanism:
  - Anthropic is verifying that the client understands the current signing protocol
  - the use of `xxHash64` suggests speed over cryptographic security
  - the scheme depends on obscurity, hidden constants, and version-specific details
- A full proof-of-concept Python script is provided that:
  - reads OAuth credentials from macOS Keychain
  - builds the request body
  - computes `cc_version` suffix
  - computes `cch`
  - sends a Claude API request with the needed headers
- The author’s main takeaway is that third-party tooling can reimplement the mechanism once the constants and algorithm are known, and that the “hard part” was discovering the hash, not reproducing it.

### Assessment
This is a high-density technical reverse-engineering writeup with a clear primary-source feel, though it is also somewhat adversarial in tone and makes strong claims about Bun’s runtime behavior and Anthropic’s internal mechanism. Durability is medium: the reverse-engineering techniques and general pattern of hidden request signing are durable, but the specific version constants, seeds, headers, and fast-mode behavior are tied to a particular Claude Code/Bun release window in February 2026. The content type is mixed, leaning research/technical with a proof-of-concept tutorial embedded at the end. Originality appears high because it presents a fresh reverse-engineering analysis rather than summarizing others. It is best used as a refer-back reference if you need to reproduce or verify the signing scheme, not just skim once. Scrape quality looks good: the main article text and the PoC are present, though any visual diagrams or external evidence from the original page are not available here.
