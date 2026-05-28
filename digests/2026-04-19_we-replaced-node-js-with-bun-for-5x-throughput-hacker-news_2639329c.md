---
url: https://news.ycombinator.com/item?id=47656114
title: We replaced Node.js with Bun for 5x throughput | Hacker News
scraped_at: '2026-04-19T21:47:06Z'
word_count: 839
raw_file: raw/2026-04-19_we-replaced-node-js-with-bun-for-5x-throughput-hacker-news_2639329c.txt
tldr: Hacker News commenters debate a “We replaced Node.js with Bun for 5x throughput” claim, arguing the speedup mostly came from app/query/schema optimizations rather than Bun itself, while a few others praise Bun’s `bun build --compile` and compare it with Deno, Node SEA, and JS backend ergonomics.
key_quote: “Claiming 5x throughput from "replacing Node.js with Bun" is a wild misrepresentation of the findings.”
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: skim-once
scrape_quality: partial
people: []
tools:
- Bun
- SQLite
- Zod
- Deno
- Node SEA
- Docker
- yarn
- pnpm
libraries: []
companies: []
tags:
- javascript-runtimes
- performance-benchmarks
- backend-development
- deployment-packaging
- developer-tools
---

### TL;DR
Hacker News commenters debate a “We replaced Node.js with Bun for 5x throughput” claim, arguing the speedup mostly came from app/query/schema optimizations rather than Bun itself, while a few others praise Bun’s `bun build --compile` and compare it with Deno, Node SEA, and JS backend ergonomics.

### Key Quote
“Claiming 5x throughput from "replacing Node.js with Bun" is a wild misrepresentation of the findings.”

### Summary
- **Top comment (verbatim):** “I'm puzzled by the title of this post. From what I can gather most, if not all, of the performance improvements came from sacking SQLite and Zod.”
- **Top commenter:** not explicitly named in the provided content
- **Thread topics:**
  - Whether the reported **5x throughput** is attributable to **Bun** or to **application-level optimizations**
  - Criticism of the benchmark’s methodology, especially **CPU-time reductions before the Node vs Bun comparison**
  - Discussion of **`bun build --compile`** as a deployment/runtime packaging feature
  - Comparisons among **Bun, Deno, Node SEA**, and traditional Node deployment
  - Broader opinions about whether **JavaScript belongs on the backend**

- The thread centers on skepticism toward a performance article titled **“We replaced Node.js with Bun for 5x throughput.”**
  - One commenter argues the improvement is overstated because the article appears to credit Bun for gains that actually came from:
    - dropping or changing **SQLite**
    - removing **Zod**
    - applying **phase 3 optimizations**
    - removing **`safeParse`**
  - They say the benchmark sequence makes it impossible to cleanly attribute the throughput gain to Bun alone.

- Several replies focus on **deployment and runtime packaging**:
  - A user quotes Bun docs describing `bun build --compile`, which creates a **single self-contained executable**.
  - The docs say compiled executables reduce **memory usage** and **startup time**, because Bun’s normal runtime does parsing/transpiling work at import/require time.
  - Another commenter clarifies that Bun’s compiled output is a **large self-contained executable** and says it is “Almost like a large electron build.”
  - **Deno** is mentioned as offering similar functionality, but with a **smaller optimized binary**.

- The article’s database/query choices get strong criticism:
  - A commenter calls the SQL rewrite “extremely cringe and amateurish,” specifically mocking the use of **`DISTINCT`** to hide redundancy from an inefficient key-value metadata schema.
  - They say the post unfairly blames **SQLite** and that this undermined their confidence in the authors.

- The thread broadens into a discussion of **JS as a backend language**:
  - Some users say they would prefer to keep JavaScript mostly on the browser and not care much about “healthy competition” between runtimes.
  - Others argue that shared FE/BE JS can reduce duplication, especially for things like **input validation**.
  - A counterpoint says FE and BE are different disciplines and code sharing can feel like a “trojan horse.”
  - One commenter notes that in modern SaaS/agent/AI workflows, the need for backend JS is often driven by **SDK/customer requirements**, not preference.

- There is also some practical tooling discussion:
  - One user says they use **Bun for everything except monorepos with isolated deployment targets and shared packages**.
  - They prefer **yarn or pnpm** for monorepos, citing issues with **Docker dependency resolution** and Bun’s lockfile behavior across the whole repo.
  - They mention spending time with docs, online resources, and AI agents without finding a satisfying fix.

- Overall, the thread is split between:
  - **skepticism** about the benchmark and its attribution of speedups
  - **interest** in Bun’s compile-to-binary and deployment story
  - **pragmatic runtime/tooling preferences** based on monorepos, Docker, and ecosystem constraints

### Assessment
This is a **mixed** social-thread capture with fairly high topical density but incomplete attribution details from the scrape. The durability is **medium**: the specific performance claims and Bun/Deno/Node tooling references will age as versions and benchmarks change, but the general critique of attribution in performance posts is long-lived. Content type is primarily **commentary/opinion**, with some embedded **reference** to Bun docs. Density is **high** because the thread covers benchmark methodology, deployment packaging, runtime comparisons, and backend language philosophy. Originality is **commentary** rather than primary reporting. It is best used as a **skim-once / refer-back** card if you want the shape of the debate, not a source of truth on benchmark validity. Scrape quality is **partial**: the comments are present, but no clear author handles are provided for the top comment, and the underlying article itself is not included.
