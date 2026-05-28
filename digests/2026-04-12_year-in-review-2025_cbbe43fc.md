---
url: https://mariozechner.at/posts/2025-12-22-year-in-review-2025/
title: Year in Review 2025
scraped_at: '2026-04-12T10:29:51Z'
word_count: 7775
raw_file: raw/2026-04-12_year-in-review-2025_cbbe43fc.txt
tldr: Mario Zechner’s 2025 review is a dense, highly personal recap of a year dominated by electronics tinkering, anti-LLM skepticism, AI tooling experiments, investigative scraping projects, and public workshops/talks.
key_quote: 'Before I dive into a few select "AI" projects, I think my summary of a year of working with coding agents is: nobody knows yet how to do this properly.'
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people:
- Mario Zechner
- Armin Ronacher
- Cory Doctorow
- Peter Steinberger
- Steffi
- Jenia
- Max Müller
- Felix Krause
tools:
- Claude Code
- Cursor
- MCP
- VS Code
- Whisper
- Playwright
- Chrome DevTools Protocol
- GitHub Copilot
- OpenRouter
- Gemini
libraries:
- Whisper
companies:
- SPAR
- OE24
- Claude
- Anthropic
- fobizz
- Vercel
- Azure
- OpenAI
- Google
- WhatsApp
- Dynatrace
tags:
- agentic-coding
- llm-security
- web-scraping
- media-analysis
- electronics-projects
---

### TL;DR
Mario Zechner’s 2025 review is a dense, highly personal recap of a year dominated by electronics tinkering, anti-LLM skepticism, AI tooling experiments, investigative scraping projects, and public workshops/talks.

### Key Quote
"Before I dive into a few select "AI" projects, I think my summary of a year of working with coding agents is: nobody knows yet how to do this properly."

### Summary
- **Context and personal note**
  - The post is dated **2025-12-22** and frames itself as a memory aid for the author and a possible source of useful ideas for readers.
  - He notes a **gap in February/March** because of a hospital stay and slow recovery, which reduced his energy and explains the dip in GitHub activity.
  - The recurring theme is that the year’s work was a mix of **technical projects, hacktivism, and general bullshittery**.

- **Boxie**
  - His proudest project: an **always-offline audio player for his then three-year-old son**.
  - Built after deciding in summer 2024 to learn electronics, which led to:
    - basic LED experiments
    - self-designed PCBs
    - SMT soldering
    - buying a lot of equipment
    - porting **Doom** to an embedded system
  - The child uses it daily and has about **72 cartridges** with audio plays, audiobooks, and music.
  - He highlights the educational value of letting his son open it up and inspect how it works.

- **Cards for Ukraine**
  - The project crossed **€300,000** in donations in 2025.
  - Two batches were sent:
    - **May: 190 cards**
    - **October: 308 cards**
  - He says fundraising remains harder after three years of war and recession, but still works through social posts and donations.

- **heisse-preise.io**
  - The grocery price scraping project kept running.
  - **SPAR changed its API on Christmas Eve 2024**, breaking collection; he noticed in March and fixed it only in May.
  - Result: a data gap from **2024-12-24 to 2025-05-14** for SPAR products.
  - He argues Austrian law should be changed to:
    - legalize scraping of grocery price data
    - require retailers to expose **EAN codes**
  - He says the BWB (Federal Competition Authority) recommended this in **2023**, but the government did not implement it.
  - He mentions Cory Doctorow described him as “the kid in Austria who scraped all the web prices of the two major grocers.”
  - His mother uses the site to get angry about prices.

- **Messing with AI / coding agents**
  - He has used LLMs since **early 2023**.
  - The big change in 2025 was moving from chat-based use to **semi-autonomous coding agents**.
  - He links this to blog posts like:
    - **Prompts are Code**
    - **MCP vs CLI**
    - **What if you don't need MCP**
  - His view:
    - coding agents are useful, but
    - nobody really knows how to use them properly yet
    - “armies of agents” are overrated for his workflow
    - staying in the loop works better for him
  - He emphasizes that many agent users don’t publish their work, while he tries to open source and document his tools.

- **Texty**
  - A first “vibe coded” project built in **January 2025**.
  - Purpose: help his dyslexic writing by spell/grammar checking text inside the apps he already uses.
  - Implemented as:
    - a **browser extension**
    - an **Android app**
  - Android version uses the **Accessibility Service** to inspect and interact with app UI.
  - He used it for a few months but found the workflow too cumbersome and slow.
  - Main value: it was his first serious test of LLM-assisted engineering with minimal intervention.

- **Hacking Claude Code**
  - Around April he reverse engineered Claude Code by:
    - patching the binary to disable anti-debugging
    - monkeypatching fetch to intercept API calls
  - Findings included:
    - Haiku generated the whimsical “please wait” messages
    - Haiku also checked bash commands for injection attacks
    - `/cost` was disabled for Max plan users
    - the system prompt told Claude to clean up test files, which explained unwanted deletions
    - emoji restrictions were added repeatedly
  - He built related tools:
    - **claude-trace**
    - **claude-bridge**
    - **cc-antidebug**
    - **cccost**
    - **claude-notify**
  - He later abandoned Claude Code and wrote his own agent harness.

- **Exploring and abandoning MCP**
  - He initially built **vs-claude**, an extension plus MCP server for VS Code integration.
  - Then built more MCP servers, including **mailcp** for Gmail, which he found poor because it dumped JSON into context.
  - His conclusion: MCP outputs are hard to compose efficiently, and they bloat context.
  - He shifted toward **CLI tools** that agents can invoke via bash:
    - **lsp-cli**
    - **gmcli**
    - **gccli**
    - **gdcli**
  - He concluded that for many uses, **CLI vs MCP matters less than keeping token usage low**.

- **Yakety**
  - A local voice transcription app built because existing tools demanded too many intrusive macOS permissions.
  - Features:
    - runs fully local
    - choose Whisper model
    - records only while holding a hotkey
    - supports **FN on macOS** or **Right Ctrl on Windows**
  - He no longer uses voice dictation much for coding, but still uses Yakety for writing.
  - It is now open source, though he expects bitrot.

- **VibeTunnel**
  - A 24-hour collaboration with Peter and Armin in Vienna.
  - Goal: control Claude Code from mobile phones.
  - The project was a fun “Skunk Works” style experiment, but ended up as a **Frankenstein** and was basically unmaintainable.
  - Peter later turned the idea into **Clawdis**, which he says works much better.

- **Sitegeist and Cellgeist**
  - **Sitegeist** is a browser extension for:
    - deep research on companies/persons/topics
    - one-off scrapes
    - site interaction and automation
  - Features:
    - full trace of the research process
    - session management
    - multi-provider/multi-model support
    - artifacts like HTML, Markdown, Excel, PowerPoint, Word
    - a skills system for reusable page automation
  - Under the hood, it can inject JS via:
    - script tags
    - user scripts
    - the debugger
  - He warns strongly about **prompt injection and exfiltration**, especially when using the debugger because it can access HTTP-only cookies and secrets.
  - He thinks browser agents are risky, especially for normies, and that the current ecosystem lacks a good security answer.
  - He originally considered commercializing Sitegeist but decided to open source it.
  - **Cellgeist** is the same idea inside Excel.

- **pi coding agent**
  - His own minimal agent harness, created after Claude Code changes kept breaking his workflow.
  - Explicit design choices:
    - no MCP
    - no sub-agents
    - no plan mode
    - no to-do tool
  - Core tools are minimal: **read, write, edit, bash**
  - Extensible through plugins/hooks/custom UI without changing core.
  - Multi-provider and multi-model support, including:
    - GitHub Copilot
    - Claude Max
    - Cerebras
    - OpenRouter
    - local models
  - Includes cost tracking and custom compaction.
  - He describes it as “the Hacker’s Open Source choice.”
  - It became his **exclusive daily driver** for the past two months.

- **Teaching Claude Code to his linguist wife**
  - He helped Steffi, a linguist, use Claude Code for data analysis in Excel-heavy research.
  - Her project involved:
    - **32 speakers**
    - **two conversation settings**
    - **18,000+ rows**
  - Claude Code generated a pipeline of Python scripts for:
    - Excel-to-CSV conversion
    - splitting semicolon-separated columns
    - filtering out asterisk-marked forms
    - counting values per speaker/setting
    - summary statistics
    - clustering
    - visualization
  - The big win was **reproducibility**: fixing source data and rerunning scripts regenerated everything.
  - He argues these tools work best in the hands of **domain experts**, who can verify outputs even if they cannot judge the code itself.

- **Investigating slop in the wild**
  - He and others used LLM artifacts and punctuation patterns to detect AI-generated content in Austrian media.

  - **Austrian Media LLM Usage**
    - Investigated **OE24** after spotting raw ChatGPT artifacts in an article.
    - Scraped articles from October across **2021–2025** and counted dash usage.
    - Found stable dash use from **2021–2024**, then a large spike in **2025**.
    - Concluded this was strong evidence of LLM-written content in some categories.
    - He later expanded the study with Jenia to **Exxpress, Heute, Krone, Falter**.
    - Differentiated:
      - **CMS replacement pattern**: dashes rise while hyphens fall proportionally
      - **LLM pattern**: dashes rise while hyphens stay flat
    - Found selective adoption in categories like **lifestyle and entertainment** for some outlets.
    - Notes public funding:
      - OE24 parent got **€287,000** for AI-related work
      - Heute got **€140,876** for “KI-gestützter Journalismus”
    - He is building a public media monitoring/search tool from this data.

  - **fobizz School AI Tools**
    - Reviews fobizz, a school AI platform, and a related German-language conference talk.
    - Critiques:
      - automated homework correction gives essentially random grades
      - teachers are pushed toward direct use of generated PDFs with little verification guidance
      - “TÜV certified” security claims coexist with warnings not to enter sensitive data
      - transcription scrapes YouTube/Vimeo
      - historical roleplay bots include a **Sophie Scholl bot**, which responded inappropriately to a question about injustice
    - He also critiques an Austrian school AI pilot project involving **114 schools** and a final report that he says is basically just a link collection with poor evaluation.

  - **Facial Recognition Hiring Paper**
    - He says a paper claiming facial analysis can predict personality traits for hiring is methodological garbage.
    - Criticisms include:
      - misuse of genetics literature
      - reliance on AI-generated data
      - weak predictive power
      - laughably small robustness checks
    - He calls it essentially **phrenology with an AI coat of paint**.

  - **Other Investigations**
    - Government chatbot audits:
      - Kremsi, Feldi, KLARA, Telfer Copilot
      - finds jailbreakability, wrong hosting claims, or useful access depending on system
    - **Clinara** medical transcription:
      - tests transcription accuracy against a Standard article
      - estimates Whisper-style error rates around **5–10%**
      - notes their web app leaks a system prompt and can be abused as a free GPT endpoint
    - **StoryOne** book generator:
      - generated a 75-page book from one of his posts
      - mostly hallucinated slop and blank “for layout” pages
    - **Parliament Watch**:
      - tracks parliamentary absences from stenographic protocols
    - **Carinthian Honors Dashboard**:
      - classifies honors by gender from names
    - **Coalition Protocol Leaks**:
      - hosted leaked Austrian coalition negotiation documents and archived them
    - **WaveMind**:
      - scrapes and transcribes Austrian audio news sources
      - includes searchable transcripts and LLM-based interrogation
    - **Cremer Archive**:
      - archived a photo blog documenting Austrian politics

- **Talks**
  - He resumed conference speaking in 2025 after not doing much since **2016**.
  - Talks/panels included:
    - Vienna Tech Soirée panel on “How to vibe code to a billion dollars”
    - first Claude Code Anonymous meetup in Vienna
    - LLMs in Real Software meetup in Graz
    - GrazJS talk on JailJS and Sitegeist
    - Bit & Babel with Jenia
  - He likes meeting people in real life and says these events were enjoyable and energizing.

- **Workshops**
  - He created multiple workshops in 2025:
    - a **generative AI workshop for normies**
    - an **agentic coding workshop** in December
  - The aim is not hype but demystification:
    - how LLMs process PDFs
    - how vision works
    - limitations and failure modes
    - how to use agentic tools effectively
  - He ran the workshop for:
    - a local software company
    - investigative journalists at **Profil**
  - The materials are interactive but locked unless he provides a key.
  - He also did a German livestream of the workshop.

- **Conclusion**
  - He says the year was long and he could have added much more.
  - His biggest takeaway is that he enjoys meeting peers in real life.
  - He feels his electronics skills are now “dangerous enough to build things that can kill me.”
  - On software engineering, he thinks he kept up with the agentic coding scene without drinking too much Kool-Aid.
  - He does not know whether LLMs made him more productive overall.
  - His sense is that this year’s projects had more technical depth, even if the total volume wasn’t much larger.
  - Final theme: **“It’s all just vibes.”**

### Assessment
This is a **mixed** personal year-in-review post with strong opinionated commentary, project updates, and many specific findings from the author’s own experiments. Durability is **medium**: the broad lessons about coding agents, MCP vs CLI, browser-agent security, and reproducible workflows should age reasonably well, but many details are tied to 2025 tools, versions, and current Austrian media/government projects. The content density is **high**—it’s packed with names, dates, tools, claims, and project links—but it is also somewhat sprawling because it covers an entire year and many side projects. Originality is mostly **primary source**: this is the author reporting on his own work, experiments, and conclusions, not a synthesis of others. It is best used as **refer-back** material if you want the specifics of any project, tool, or investigation; the full post is worth rereading if you care about his evolving opinions on agentic coding, scraping, or media/LLM misuse. Scrape quality appears **good** overall: the main text is present, but images, embedded videos, charts, tables, and linked references are not included in the extracted content, so some supporting evidence and visuals are missing.
