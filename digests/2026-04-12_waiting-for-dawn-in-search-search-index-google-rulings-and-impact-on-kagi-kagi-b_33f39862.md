---
url: https://blog.kagi.com/waiting-dawn-search
title: 'Waiting for dawn in search: Search index, Google rulings and impact on Kagi | Kagi Blog'
scraped_at: '2026-04-12T07:31:47Z'
word_count: 2422
raw_file: raw/2026-04-12_waiting-for-dawn-in-search-search-index-google-rulings-and-impact-on-kagi-kagi-b_33f39862.txt
tldr: Kagi argues that Google’s search-index monopoly now constrains both search and AI, and that the DOJ’s 2024–2025 antitrust remedies could finally force open index access on fair terms, enabling a layered search ecosystem where Kagi can compete.
key_quote: if one company controls the index, it controls the floor on how good AI can be - and who gets to build it.
durability: medium
content_type: mixed
density: high
originality: commentary
reference_style: refer-back
scrape_quality: good
people:
- Vladimir Prelovac
- Raghu Murthi
- Ian Bremmer
- Sergey Brin
- Larry Page
- Amit Mehta
tools:
- SerpApi
- Bing Search APIs
- Google Search
- Programmable Search Engine
- Vertex AI
libraries: []
companies:
- Kagi
- Google
- Microsoft
- Mojeek
- Brave
- Yandex
- Wikipedia
- TripAdvisor
- Yelp
- Apple
- Wolfram Alpha
- Bing
- Startpage
- Nvidia
- Adobe
- Samsung
- Stanford
- DeepMind
- Uber
- United Nations
- DOJ
tags:
- search-monopoly
- antitrust
- search-index
- ai-infrastructure
- information-access
---

### TL;DR
Kagi argues that Google’s search-index monopoly now constrains both search and AI, and that the DOJ’s 2024–2025 antitrust remedies could finally force open index access on fair terms, enabling a layered search ecosystem where Kagi can compete.

### Key Quote
“if one company controls the index, it controls the floor on how good AI can be - and who gets to build it.”

### Summary
- This is a follow-up to Kagi’s earlier post, “Dawn of a new era in Search,” and frames the past year as a turning point:
  - the Google antitrust case advanced,
  - AI became the central battleground,
  - and open index access became even more important.
- Core thesis:
  - Google controls the dominant web search index, and that control affects not just search but also AI systems that depend on grounding in real-world information.
  - Kagi argues that a single ad-driven gatekeeper shaping search results is harmful to competition and to users’ ability to make informed decisions.
- Market concentration is presented as extreme:
  - Worldwide search market share in October 2025: Google 90.06%, Bing 4.31%, Yandex 1.84%, Yahoo 1.45%, DuckDuckGo 0.89%, Baidu 0.73%.
  - U.S. market share is described as similar: Google 85%, Bing 9%, everyone else negligible.
- Kagi says it tried to secure direct, FRAND-style licensing from major index vendors:
  - Successful direct licenses: Mojeek, Brave, Yandex, Wikipedia, TripAdvisor, Yelp, Apple, Wolfram Alpha, and its own Small Web Index.
  - Failed attempts:
    - **Bing**: terms blocked reordering/merging results; Microsoft later raised API prices up to 10x in Feb. 2023 and retired Bing Search APIs in May 2025.
    - **Google**: no public search API; only an ad-syndication bundle akin to Startpage, which Kagi says is incompatible with its ad-free model.
- Kagi says its current workaround is using third-party SERP API providers:
  - These vendors reportedly serve large enterprises such as Nvidia, Adobe, Samsung, Stanford, DeepMind, Uber, and the United Nations.
  - Kagi describes this as interim and undesirable, and wants direct contractual access instead.
- The DOJ antitrust case against Google is the centerpiece:
  - The case began in 2020.
  - On Aug. 5, 2024, the court ruled Google violated Section 2 of the Sherman Act by maintaining its monopoly through exclusive distribution agreements.
  - On Sept. 2, 2025, the DOJ announced remedies including:
    - limits on exclusivity in Search, Chrome, Assistant, and Gemini,
    - data sharing and syndication requirements,
    - and measures aimed at dismantling exclusionary agreements.
  - In Dec. 2025, Judge Mehta’s memorandum reportedly specified:
    - mandatory syndication for “Qualified Competitors,”
    - no ad bundling as a condition of access,
    - access to Web Search Index data at marginal cost,
    - a 6-year judgment with 5-year syndication licenses.
- Kagi’s view of enforcement:
  - Google is simultaneously moving to close scraping loopholes, including a Dec. 2025 lawsuit against SerpApi.
  - Kagi argues Google’s current enforcement posture is the product of monopoly power, not a neutral rule system.
  - The company says regulators must ensure the “front door” to index access is genuinely open if the “back door” is being closed.
- The post proposes a three-layer search ecosystem:
  - **Layer 1: Search as a public good** — a taxpayer-funded, ad-free, intermediary-free baseline service (a long-term idea, not expected soon).
  - **Layer 2: Free, ad-based search** — commercial search funded by ads.
  - **Layer 3: Paid, subscription-based search** — premium, privacy-focused, high-quality search; this is where Kagi positions itself.
- Broader conclusion:
  - Kagi sees the DOJ remedies as a way to convert search from a closed choke point into shared infrastructure.
  - If implemented well, they could support a healthier market with public baseline access, ad-supported free products, and premium paid services competing on quality and privacy.
- The post ends by emphasizing that Kagi is preparing for a future where it can rely on legitimate multi-source access rather than gray-market workarounds.

### Assessment
This is a high-density, mixed opinion/announcement/technical-policy post with strong advocacy framing. Its durability is medium: the underlying arguments about search monopolies, index access, and antitrust are fairly durable, but many specifics are tightly bound to late-2025 legal proceedings, market-share snapshots, and vendor/API status that may age quickly. It is original commentary from Kagi rather than neutral synthesis, and it is best used as a refer-back source if you want Kagi’s position on Google, DOJ remedies, and the future structure of search. Scrape quality is good: the full argument, tables, references, and footnote content appear captured, though any original formatting nuance beyond plain text is naturally lost.
