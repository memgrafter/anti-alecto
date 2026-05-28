---
url: https://simonwillison.net/2026/Feb/7/software-factory/
title: How StrongDM’s AI team build serious software without even looking at the code
scraped_at: '2026-04-19T07:12:09Z'
word_count: 1560
raw_file: raw/2026-04-19_how-strongdm-s-ai-team-build-serious-software-without-even-looking-at-the-code_aca500a4.txt
tldr: 'Simon Willison describes StrongDM’s “software factory” approach to AI coding: humans write specs and monitor systems, but agents write and test code without human review, using scenario-based validation and simulated third-party service “digital twins.”'
key_quote: Code must not be reviewed by humans
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Simon Willison
- Dan Shapiro
- Cem Kaner
- Jay Taylor
- Justin McCarthy
- Navan Chauhan
tools:
- Cursor
- Claude Opus 4.5
- GPT 5.2
- Claude Sonnet 3.5
- Claude 3.5
- Claude Max
libraries: []
companies:
- StrongDM
tags:
- ai-coding
- software-testing
- agentic-workflows
- digital-twins
- software-engineering
---

### TL;DR
Simon Willison describes StrongDM’s “software factory” approach to AI coding: humans write specs and monitor systems, but agents write and test code without human review, using scenario-based validation and simulated third-party service “digital twins.”

### Key Quote
“Code must not be reviewed by humans”

### Summary
- StrongDM’s AI team is presented as an example of the “Dark Factory” level of AI adoption, where **humans do not look at the code** produced by coding agents.
- Their core rules and framing:
  - **Code must not be written by humans**
  - **Code must not be reviewed by humans**
  - A more practical benchmark is spending **at least $1,000/day on tokens per human engineer**
- Simon says this feels especially significant because the hard problem is no longer just generating code, but **proving that agent-written code actually works** when both implementation and tests may be AI-generated.
- StrongDM’s answer is based on **scenario testing**:
  - “Scenario” means an end-to-end user story, often kept **outside the codebase** like a holdout set.
  - They replace a simple pass/fail test model with a probabilistic notion called **“satisfaction”**: across observed trajectories, what fraction likely satisfy the user?
- A major innovation is the **Digital Twin Universe (DTU)**:
  - Behavioral clones of services like **Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets**
  - These clones replicate APIs, edge cases, and observable behaviors
  - They allow thousands of scenarios per hour without rate limits, abuse detection, or API costs
- Simon explains that the DTU was built by having agents ingest **public API documentation** and generate self-contained simulations, sometimes with a simplified UI.
- Jay Taylor later added a key prompting insight: use **popular public SDK client libraries as compatibility targets**, aiming for **100% compatibility**.
- StrongDM also uses terminology for other techniques:
  - **Gene Transfusion**: extracting patterns from existing systems and reusing them elsewhere
  - **Semports**: porting code directly between languages
  - **Pyramid Summaries**: layered summaries so agents can start with short versions and expand as needed
- StrongDM released two projects:
  - **attractor**: a non-interactive coding agent repo containing **only three markdown spec files**, with instructions to feed them to your own coding agent
  - **cxdb**: a more conventional release, an **AI Context Store** in Rust, Go, and TypeScript, storing conversation histories and tool outputs in an immutable DAG
- Simon visited the team in October 2025 and was impressed that a **three-person team** had already built working demos of:
  - the coding agent harness
  - DTU clones of several services
  - simulated test-agent swarms
- He sees this as a preview of a future where engineers spend less time writing code directly and more time **building and semi-monitoring systems that generate code**.
- He is enthusiastic but cautious about the economics:
  - If the approach really costs **$20,000/month per engineer**, it may only make sense as a business model for certain companies
  - He hopes similar ideas can be used at much lower cost
- The post ends with Simon emphasizing that the most interesting open question is still: **how can agents prove their code works without humans reviewing every line?**

### Assessment
This is a high-density, mostly primary-source commentary on a very recent AI/software-development practice, with some reporting and interpretation layered on top. **Durability is medium**: the concepts (scenario testing, holdout-style validation, agentic software factories) may last, but the specifics are tied to late-2025/early-2026 model capabilities, StrongDM’s internal setup, and the cited token-cost threshold. The content type is **mixed**—part essay, part field report, part technical reference to StrongDM’s methods and releases. **Originality is commentary/synthesis**, since Simon is synthesizing what he observed plus public material from StrongDM. It’s best treated as **refer-back** material if you’re tracking agentic coding workflows, testing architecture, or StrongDM’s terminology. **Scrape quality is good**: the post content appears intact and includes the main narrative, quotations, and named projects, though embedded screenshots/visual context are not available here.
