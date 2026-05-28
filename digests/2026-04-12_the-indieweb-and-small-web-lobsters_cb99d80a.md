---
url: https://lobste.rs/s/yryapx/indieweb_small_web
title: The IndieWeb and Small web | Lobsters
scraped_at: '2026-04-12T10:33:47Z'
word_count: 1339
raw_file: raw/2026-04-12_the-indieweb-and-small-web-lobsters_cb99d80a.txt
tldr: A Lobsters discussion questions whether IndieWeb/Small Web has real traction, with replies split between frustration over low adoption and centralization, and enthusiasm for the movement’s user autonomy, slow pace, and practical tools like Webmention and IndieAuth.
key_quote: “it wasn't about pushing updates, making everything an SaaS and shoehorning AI into every nook and cranny.”
durability: medium
content_type: mixed
density: medium
originality: commentary
reference_style: skim-once
scrape_quality: partial
people:
- Darcy DiNucci
- Aaron Parecki
tools:
- IndieAuth
- Webmention
- webmention.io
- Feedly
- Kagi Small Web
- blog-quest
libraries: []
companies:
- Lobsters
- Yahoo
- Google
tags:
- indieweb
- small-web
- web-decentralization
- webmention
- indieauth
---

### TL;DR
A Lobsters discussion questions whether IndieWeb/Small Web has real traction, with replies split between frustration over low adoption and centralization, and enthusiasm for the movement’s user autonomy, slow pace, and practical tools like Webmention and IndieAuth.

### Key Quote
“it wasn't about pushing updates, making everything an SaaS and shoehorning AI into every nook and cranny.”

### Summary
- **Main topic:** Whether the IndieWeb / Small Web movement is actually growing or merely a long-running niche.
- **Original poster’s concern:**
  - IndieWeb seems to have “zero traction.”
  - Standards/tools appear to come from a very small group.
  - Many implementations look stale, with “last commit date of 10y ago.”
  - The poster has prior experience, including writing a Webmention library in 2013, and has recently been revisiting IndieAuth.
- **Counterpoint: changing expectations**
  - One commenter argues IndieWeb/Small Web should not be judged by mass adoption or fast-paced growth.
  - The movement is framed as a reaction against the modern web’s commodification of users and loss of autonomy.
  - Its value is described as restoring agency: letting people create and express themselves independently of centralized governance.
  - The “slow pace” is presented as intentional and even freeing, not a failure.
- **Adoption / traction skepticism**
  - Another commenter says the amount of daily content/discussion around IndieWeb feels roughly comparable to Lobsters itself.
  - They characterize it as a niche invite-only community, not a broadly adopted ecosystem.
  - A recurring analogy is “Linux on the desktop”: always promising, never breaking through.
- **Practical tools and usage**
  - IndieAuth is praised as “pretty neat” for logging into services by signing messages with a PGP key linked from one’s own site.
  - A downside is noted: one IndieAuth service is in maintenance mode, and a reimplementation has narrower features that reportedly no longer include PGP-based sign-in.
  - Several commenters mention Webmention:
    - Some have recently built microblogs or are planning to add Webmention support.
    - Others say they have repeatedly gotten lost trying to understand how to implement it on a static site.
    - One answer points to **webmention.io** as a receiver service, plus JavaScript to fetch and display mentions.
- **Discovery and ecosystem concerns**
  - A commenter asks where the “Yahoo style directories” and RSS-reader-like tools are that would help users actually find and use the Small Web.
  - Another replies that there is “a ton happening,” but ad-driven social media dominates attention.
  - They cite:
    - **Feedly** as a popular RSS reader with millions of downloads.
    - **Kagi Small Web** as a curated list.
    - A blogroll-based network at **alexsci.com/rss-blogroll-network/**.
    - Starter packs at **youneedfeeds.com/starter-packs**.
    - An extension called **blog-quest** that collects feeds while browsing.
- **Critique of implementation burden**
  - One commenter is broadly skeptical of IndieWeb/Small Web.
  - They say the ecosystem requires too much template/microformat work for far-end parsers to understand posts.
  - They argue a lot of the working ecosystem depends on one library or one developer/service, especially **Aaron Parecki**, which feels centralized despite decentralization goals.
  - They also criticize **POSSE** as awkward, saying they don’t want to post elsewhere just because “that’s where the people are.”
- **Overall tone**
  - The thread mixes enthusiasm, frustration, and realism.
  - Common tensions:
    - autonomy vs. usability
    - decentralization vs. dependence on a few maintainers
    - slow, intentional growth vs. lack of visible traction
    - owning your site vs. the convenience of large social platforms

### Assessment
This is a **mixed** discussion thread with high specificity but uneven depth: **durability is medium** because the core ideas about web decentralization, user autonomy, and social platform dependence are long-lived, but many concrete references (maintenance-mode services, current tools, active links) may age quickly. The content type is mostly **opinion** with some **tutorial/reference** elements around Webmention and IndieAuth. **Density is medium**: there are several substantial viewpoints and tool mentions, but it’s conversational and fragmented rather than tightly argued. It is mostly **commentary** rather than primary documentation or research. Best used as a **skim-once / refer-back** reference for gauging community sentiment and finding tool names, not as a deep technical guide. **Scrape quality is partial**: it captures many comments, but the thread is incomplete/fragmented and lacks full context, formatting, and any linked article content beyond discussion excerpts.
