---
url: https://www.youtube.com/watch?v=1o74a8a0rBw&list=TLPQMTIwNDIwMjYIYJRkHJ1QQA&index=5
title: Maintaining a codebase with AI | The Standup - YouTube
scraped_at: '2026-04-19T07:49:50Z'
word_count: 8834
raw_file: raw/2026-04-19_maintaining-a-codebase-with-ai-the-standup-youtube_01b096fb.txt
tldr: Cloudflare’s Steve Faulkner and Dane W. describe a Next.js-compatible project built on Vite/V that they maintain with AI bots for triage, PR review, security checks, and upstream tracking, arguing that AI makes this kind of open-source upkeep sustainable.
key_quote: “We maintain it with AI, right? We have AI bots that are doing triaging.”
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- Steve Faulkner
- Dane W.
- Dylan Moscow
- Evan
- Fred
- John Carmack
tools:
- Vite
- V
- Next.js
- Turbopack
- Sentry
- GitHub
- Jira
- Make
libraries:
- Hono
companies:
- Cloudflare
- Vercel
- Astro
- WordPress
- Sentry
tags:
- ai-assisted-development
- open-source-maintenance
- nextjs
- frontend-tooling
- web-frameworks
---

### TL;DR
Cloudflare’s Steve Faulkner and Dane W. describe a Next.js-compatible project built on Vite/V that they maintain with AI bots for triage, PR review, security checks, and upstream tracking, arguing that AI makes this kind of open-source upkeep sustainable.

### Key Quote
“We maintain it with AI, right? We have AI bots that are doing triaging.”

### Summary
- This is a podcast-style discussion on Cloudflare’s effort to support **the official Next.js API surface on a different runtime/build setup**, using **Vite/V** rather than the Next.js stack people usually associate with Vercel.
- The project began as a customer-driven request: make Next.js easier to deploy on Cloudflare’s “deploy once, goes everywhere” infrastructure.
- A Cloudflare intern first explored the idea, initially scoped to the **pages router**; later Steve picked it back up and expanded it with heavy AI assistance.
- The maintainers repeatedly emphasize that this is meant to stay **API-compatible with current Next.js behavior**, not to become a radically different fork:
  - They say they are **holding the line on matching Next one-for-one**
  - They are **not accepting feature requests outside the Next surface area**
  - They distinguish this from more divergent forks like the separately named **M** example they mention
- AI is described as central to both building and maintaining the project:
  - AI bots handle **triaging**
  - AI bots **review PRs**
  - AI bots do **security reviews**
  - AI bots watch the **Next.js repo** and open issues when relevant commits land upstream
  - The project reportedly has **50+ committers**, where “committer” means someone who wrote a plan for an agent to implement something
- They give concrete examples of how AI-driven work still needs human oversight:
  - A **2,000-line template string** became “slop” and had to be manually broken into modules
  - Steve says he now regularly asks AI, “what’s the sloppiest part of this codebase?”
  - They maintain an **agents.md** file that is updated on a schedule based on PR comments and recurring mistakes
- Guardrails they mention for keeping AI-generated code usable:
  - Porting a large suite of **Next.js tests**
  - Using **end-to-end tests, unit tests, smoke tests**
  - **Linting**
  - Some formatting discipline so diffs stay readable
  - Human review remains important; internally, they still use a more traditional PR process
- They say the project exposed a broader pattern for open source in the AI era:
  - AI can help sustain large maintenance burdens
  - But humans still need to set direction, catch architectural mistakes, and enforce standards
- They cite a few examples of compatibility friction and user demand:
  - People ask for old Next.js behavior like **`getInitialProps`** from older versions
  - They run into trouble when packages depend on **undocumented Next internals** or imports from **`next/dist`**
- They discuss what still feels incomplete:
  - Better or full **pre-rendering** support
  - Some behavior differences between **Vite and Turbopack**
  - Navigation/hydration details that don’t perfectly mirror Next.js yet
- The reception is described as strong:
  - They saw a large one-day spike in new users
  - They say the project already has **400+ PRs in a month** and active external usage
- On the broader AI question, Steve says:
  - AI is good at taking feedback and rewriting
  - But he currently feels like a **“glorified AI babysitter”**
  - Humans are not going away; instead, their role shifts toward architecture, judgment, writing, communication, and higher-level problem solving
- The discussion ends on a larger uncertainty: how future engineers will gain the kind of judgment that now comes from years of direct hands-on coding.

### Assessment
This is a **mixed** content piece: part announcement, part technical discussion, part opinionated reflection on AI-assisted development. Its **durability is medium** because the concrete project status, API compatibility details, and numbers like “50+ committers” and “400+ PRs” are time-sensitive, though the broader lessons about AI maintenance and open-source workflows will age better. The **density is high** despite the podcast format, with lots of specific claims, examples, and operational details. It appears to be **primary-source commentary** from the maintainers themselves rather than a neutral synthesis. It’s best used as a **refer-back** reference if you care about Cloudflare’s AI-maintained Next.js-compatible project, open-source maintenance patterns, or their guardrails for agentic coding. **Scrape quality is partial**: the transcript is noisy, includes ads and banter, and some project naming is ambiguous or inconsistent, so a few terms should be treated cautiously even though the core claims are clear.
