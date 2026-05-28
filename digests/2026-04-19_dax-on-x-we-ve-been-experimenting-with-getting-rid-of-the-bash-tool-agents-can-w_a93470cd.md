---
url: https://x.com/thdxr/status/2034364283413283224
title: 'dax on X: "we''ve been experimenting with getting rid of the bash tool agents can write js fine which can do what bash can (though some gaps with things like git) and is more cross platform and then could run that in this" / X'
scraped_at: '2026-04-19T07:03:05Z'
word_count: 102
raw_file: raw/2026-04-19_dax-on-x-we-ve-been-experimenting-with-getting-rid-of-the-bash-tool-agents-can-w_a93470cd.txt
tldr: Dax says they’re testing replacing the Bash tool for agents with JavaScript, since agents can already write JS for most shell tasks and JS is more cross-platform, possibly running it via Rivet’s Secure Exec SDK.
key_quote: we've been experimenting with getting rid of the bash tool agents can write js fine which can do what bash can (though some gaps with things like git) and is more cross platform
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: good
people:
- dax
- thdxr
tools:
- bash
- JavaScript
- Rivet's Secure Exec SDK
- Node.js
- Bun
- Cloudflare Workers
libraries: []
companies:
- Rivet
- Cloudflare
tags:
- agent-tools
- javascript
- cross-platform
- shell-replacement
- developer-tools
---

### TL;DR
Dax says they’re testing replacing the Bash tool for agents with JavaScript, since agents can already write JS for most shell tasks and JS is more cross-platform, possibly running it via Rivet’s Secure Exec SDK.

### Key Quote
“we've been experimenting with getting rid of the bash tool agents can write js fine which can do what bash can (though some gaps with things like git) and is more cross platform”

### Summary
- This is a short X post from **dax (@thdxr)** discussing an internal agent tooling experiment.
- Main idea: **remove the Bash tool** from agent workflows and let agents use **JavaScript instead**.
- Rationale given:
  - Agents can already write JS.
  - JS can do many of the same things Bash can.
  - JS is **more cross-platform** than Bash.
  - There are still **gaps**, with **git** mentioned as one example.
- The post appears to be referencing or reacting to **Rivet’s Secure Exec SDK**:
  - “Secure Node.js execution without a sandbox”
  - Claims include **17.9 ms coldstart**, **3.4 MB mem**, **56x cheaper**
  - Supports **Node.js, Bun, and browsers**
  - “Powered by the same tech as Cloudflare Workers”
- The implication is that a secure JS execution environment could serve as the runtime for agent actions that would otherwise be handled by Bash.
- Because this is a single-post thread capture with one quoted post, there’s **no extended discussion or replies included** beyond the quoted Rivet announcement.

### Assessment
This is a **mixed** social-thread/announcement-style post with a mostly speculative product/tooling idea rather than a finished technical proposal. Durability is **medium**: the general argument for using JavaScript as a cross-platform agent tool is likely to remain relevant, but the specifics depend on agent runtime tooling and current ecosystem capabilities, especially around gaps like git. Density is **medium**—it’s brief, but it contains a concrete architecture idea plus performance claims from the quoted Rivet SDK post. Originality is **commentary** from dax, with the quote providing a **product announcement** from Rivet. It’s best used as **skim-once** or **refer-back** material depending on whether you’re tracking agent tool design; the scrape quality is **good** for the visible content, though it likely omits broader thread context and any replies.
