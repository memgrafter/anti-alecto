---
url: https://www.anthropic.com/glasswing
title: https://www.anthropic.com/glasswing
scraped_at: '2026-04-19T20:07:20Z'
word_count: 1898
raw_file: raw/2026-04-19_https-www-anthropic-com-glasswing_0deaf33f.txt
tldr: Anthropic announces Project Glasswing, a multi-partner cybersecurity initiative using its unreleased frontier model Claude Mythos Preview to find and fix zero-day vulnerabilities, while arguing that AI now has near-best-human offensive cyber capability and urgently needs defensive safeguards and industry coordination.
key_quote: “AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.”
durability: medium
content_type: announcement
density: high
originality: primary
reference_style: refer-back
scrape_quality: partial
people: []
tools:
- Claude Mythos Preview
- Claude Opus 4.6
- CyberGym
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry
libraries: []
companies:
- Anthropic
- Amazon Web Services
- Apple
- Broadcom
- Cisco
- CrowdStrike
- Google
- JPMorganChase
- Linux Foundation
- Microsoft
- NVIDIA
- Palo Alto Networks
- OpenSSF
- Alpha-Omega
- Apache Software Foundation
- OpenBSD
- FFmpeg
- Linux
tags:
- cybersecurity
- artificial-intelligence
- zero-day-vulnerabilities
- critical-infrastructure
- policy
---

### TL;DR
Anthropic announces Project Glasswing, a multi-partner cybersecurity initiative using its unreleased frontier model Claude Mythos Preview to find and fix zero-day vulnerabilities, while arguing that AI now has near-best-human offensive cyber capability and urgently needs defensive safeguards and industry coordination.

### Key Quote
“AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.”

### Summary
- **What Project Glasswing is**
  - A new Anthropic-led initiative to “secure the world’s most critical software” for the AI era.
  - Partners named include **AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks**.
  - Anthropic says it will use **Claude Mythos Preview** for defensive security work and extend access to **40+ additional organizations** that maintain critical infrastructure.

- **Why Anthropic says it matters**
  - The post argues frontier AI has reached a point where it can:
    - find software vulnerabilities,
    - develop exploits,
    - and do so at a level competitive with top human experts.
  - Anthropic frames this as a major cybersecurity and national security risk if such capabilities spread to malicious actors.
  - It estimates global cybercrime costs could be around **$500B/year**.

- **What Claude Mythos Preview reportedly did**
  - Anthropic claims the model identified **thousands of zero-day vulnerabilities**, including many critical ones in:
    - every major operating system,
    - every major web browser,
    - and other important software.
  - It says many findings were done **autonomously, without human steering**.
  - Three examples highlighted:
    - a **27-year-old OpenBSD vulnerability** that could remotely crash a machine,
    - a **16-year-old FFmpeg vulnerability** in code tested five million times without detection,
    - a chain of Linux kernel vulnerabilities enabling privilege escalation to full machine control.
  - Anthropic says the reported vulnerabilities have now been **patched**.

- **Evidence and comparisons**
  - The post references evaluation benchmarks such as **CyberGym** and says Mythos Preview substantially outperforms Anthropic’s next-best model, **Claude Opus 4.6**, on cyber-related tasks.
  - It describes Mythos Preview as having the strongest agentic coding/reasoning skills and highest scores on a variety of software coding tasks.

- **How Anthropic plans to use it**
  - Project Glasswing participants will use Mythos Preview for:
    - local vulnerability detection,
    - black-box binary testing,
    - endpoint security,
    - penetration testing.
  - Anthropic says it committed **up to $100M in usage credits** for the initiative.
  - It also donated **$4M** to open-source security organizations, broken down as:
    - **$2.5M** to **Alpha-Omega** and **OpenSSF** via the Linux Foundation,
    - **$1.5M** to the **Apache Software Foundation**.
  - After the research preview, the model would be priced at **$25/$125 per million input/output tokens** on:
    - Claude API,
    - Amazon Bedrock,
    - Google Cloud Vertex AI,
    - Microsoft Foundry.

- **Safeguards and longer-term goals**
  - Anthropic says it does **not plan to make Claude Mythos Preview generally available**.
  - Its goal is to eventually enable safe deployment of Mythos-class models at scale, including by improving safeguards that detect/block dangerous outputs.
  - It plans to launch new safeguards with an upcoming **Claude Opus** model instead.
  - Within **90 days**, Anthropic says it will report publicly on:
    - what it learned,
    - vulnerabilities fixed,
    - and improvements made.
  - It intends to produce practical recommendations for evolving security practices, including:
    - vulnerability disclosure,
    - software updates,
    - open-source/supply-chain security,
    - secure-by-design development,
    - regulated-industry standards,
    - triage scaling and automation,
    - patching automation.

- **Policy / government angle**
  - Anthropic says it has been discussing Mythos Preview with **US government officials**.
  - It argues governments have an essential role in assessing and mitigating AI-related cyber risks.
  - It invites broader industry participation and suggests an independent third-party body may eventually be the best home for this work.

- **Appendix notes**
  - The project name refers to the **glasswing butterfly (Greta oto)**, used as a metaphor for both hidden vulnerabilities and transparency in defense.
  - It mentions a **Cyber Verification Program** for security professionals whose legitimate work is affected by the safeguards.

### Assessment
This is a **mixed announcement / technical policy post** with strong promotional framing from Anthropic. **Durability is medium**: the broad argument about AI-accelerated cybersecurity will likely remain relevant, but the specifics about **Claude Mythos Preview, pricing, partner list, credits, and benchmark comparisons** are version- and moment-specific. The post is **high density** and mostly **primary source** material, though it is also advocacy-oriented and selective in what it emphasizes. It’s best used as a **refer-back** reference if you want the exact claims, partner names, funding amounts, and rollout details. **Scrape quality is partial/good**: the main text is captured, but the mention of “evaluation results below” suggests some charts/images/benchmark tables are likely missing, along with any code or linked technical detail in the referenced blog/system card.
