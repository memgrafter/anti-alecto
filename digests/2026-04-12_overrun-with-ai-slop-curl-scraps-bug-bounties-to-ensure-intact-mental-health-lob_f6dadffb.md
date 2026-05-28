---
url: https://lobste.rs/s/ijyacx/overrun_with_ai_slop_curl_scraps_bug
title: Overrun with AI slop, cURL scraps bug bounties to ensure "intact mental health" | Lobsters
scraped_at: '2026-04-12T10:32:44Z'
word_count: 2168
raw_file: raw/2026-04-12_overrun-with-ai-slop-curl-scraps-bug-bounties-to-ensure-intact-mental-health-lob_f6dadffb.txt
tldr: Lobsters discussion of a cURL article about ending or reducing bug bounty participation because AI-generated security reports have become so overwhelming that they say it threatens their “intact mental health.”
key_quote: “Good on the cURL maintainers for taking the steps they need to take.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: partial
people:
- Brian Campbell
tools:
- HackerOne
- bugzilla
- GPG
- nginx
- Caddy
- Codeberg
- GitHub
- GitLab
- Trac
- LLVM
- Lua
- FreeRADIUS
- llama.cpp
- tldraw
libraries:
- std::string
- libc
- libc++
companies:
- curl
- Mozilla
- Amazon
- Coinbase
- crypto.com
- Alibaba
- Huawei
- Zerodium
- NSO Group
tags:
- ai-slop
- bug-bounties
- security-reporting
- open-source-maintenance
- developer-tooling
---

### TL;DR
Lobsters discussion of a cURL article about maintainers dropping bug bounties because AI-generated security reports have become so overwhelming that they say it threatens their “intact mental health.”

### Key Quote
“Good on the cURL maintainers for taking the steps they need to take.”

### Summary
- This is a Lobsters comment thread reacting to a cURL post/article about ending or reducing bug bounty participation because the maintainers are being flooded with low-quality, AI-generated security reports.
- The central complaint is not just volume, but wasted maintainer time:
  - many reports are clearly bogus,
  - some describe vulnerabilities in functions that do not exist,
  - others repeat misunderstandings of language/runtime behavior,
  - and the overall effect is described as abusive rather than merely noisy.
- Several commenters frame the issue as a scaling/externality problem:
  - HackerOne-style platforms let reporters broadcast bad reports across many programs,
  - raising the “barrier to reporting” may reduce slop,
  - but any private reporting system can be overwhelmed once it becomes popular.
- There is discussion of possible mitigations:
  - requiring bug reports via GPG-encrypted email,
  - using bugzilla or other “annoying” submission workflows as a deterrent,
  - keeping a security@ inbox with auto-replies for triage,
  - self-hosting on systems like Codeberg or a personal forge,
  - using nginx/Caddy rules and firewall ASN bans to reduce scraper traffic.
- The thread broadens from security reports to AI-generated pull requests:
  - one commenter mentions AI slop PRs on FreeRADIUS,
  - others say they’ve moved projects off GitHub because of the problem,
  - and there’s mention of similar policies in other projects like ggml / llama.cpp and tldraw.
- There are also side discussions about bug-report quality and language/runtime contracts:
  - LLVM security reports are described as increasingly spammy,
  - Lua received bogus reports about `argv[0]` not being checked for NULL,
  - a side debate notes that `argc == 0` is technically possible in `execve`, though many such reports are still invalid in context,
  - another long example involves a misleading `std::string` “security” report that was really based on reading out of bounds.
- The thread includes disagreement over statistics:
  - one person cites curl’s HackerOne dashboard and argues the ratio of real reports to junk is not obvious,
  - another points out that curl’s disclosures and HackerOne numbers are not directly comparable,
  - and there is discussion of whether disclosure timing reflects actual reporting volume.
- Overall tone: sympathetic to maintainers, frustrated with AI-generated noise, and skeptical that current reporting infrastructure or bounty platforms will solve the problem.

### Assessment
This is a mixed announcement/commentary thread rather than a clean primary-source article: the underlying news is the cURL decision to scrap bug bounties for the sake of maintainer well-being, but most of the captured content is community reaction, anecdotes, and debate. Durability is medium: the specific cURL and HackerOne details are current and may age quickly, but the broader pattern—low-quality automated reports overwhelming volunteers—is likely to remain relevant. Content type is mixed, leaning opinion/commentary with some factual references. Density is medium-high because the thread is packed with concrete examples, platform names, metrics, and operational suggestions. Originality is mostly commentary/synthesis, not primary reporting. Reference style is skim-once to refer-back, mainly useful for remembering the cURL + AI slop controversy and the kinds of mitigations people discussed. Scrape quality is partial: the page captures many comments and subthreads, but it’s clearly a discussion dump with missing context from the linked article, and no visible formatting for the original post beyond the thread excerpts.
