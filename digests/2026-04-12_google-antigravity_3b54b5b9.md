---
url: https://antigravity.google/docs/plans
title: Google Antigravity
scraped_at: '2026-04-12T10:40:15Z'
word_count: 380
raw_file: raw/2026-04-12_google-antigravity_3b54b5b9.txt
tldr: Google Antigravity’s plan page explains that access is tied to Google AI plan type, with baseline quotas for all users, higher refreshed quotas for Pro/Ultra, and optional AI credit overages for Pro/Ultra once baseline limits are exhausted.
key_quote: Under the hood, the rate limits are correlated with the amount of work done by the agent, which can differ from prompt to prompt.
durability: medium
content_type: reference
density: medium
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Agent Manager
libraries:
- Gemini 3 Pro
- Gemini 3 Flash
companies:
- Google
- Vertex
tags:
- rate-limits
- subscription-plans
- ai-credits
- quota-management
- product-documentation
---

### TL;DR
Google Antigravity’s plan page explains that access is tied to Google AI plan type, with baseline quotas for all users, higher refreshed quotas for Pro/Ultra, and optional AI credit overages for Pro/Ultra once baseline limits are exhausted.

### Key Quote
“Under the hood, the rate limits are correlated with the amount of work done by the agent, which can differ from prompt to prompt.”

### Summary
- **Availability**
  - Google Antigravity is currently available:
    - To **individual accounts** under Google’s terms of service
    - In **preview (pre-GA)** for teams under Section 5 of the General Service Terms in Google Cloud’s enterprise terms of service
  - Rate limits and model availability vary depending on the user’s **Google AI plan**

- **Baseline quota for all plans**
  - All plans include:
    - Use of **Gemini 3 Pro**
    - **Gemini 3 Flash**
    - Other offered **Vertex Model Garden** models as the core agent model
    - **Unlimited Tab completions**
    - **Unlimited Command requests**
    - Access to product features like **Agent Manager** and **Browser integration**

- **Plan tiers and quota behavior**
  - **Google AI Ultra**
    - Highest and most generous quota
    - Quota refreshes **every five hours**
    - **Highest weekly rate limits**
  - **Google AI Pro**
    - High, generous quota
    - Refreshes **every five hours** until the weekly limit is reached
    - **Higher weekly rate limit**
  - **Not on AI Pro or Ultra**
    - Meaningful quota
    - Refreshes **weekly**
    - **Weekly rate limit**

- **How rate limits work**
  - Baseline rate limits are mainly based on available capacity and are intended to **prevent abuse**
  - Actual prompt allowance depends on how much work the agent performs
    - Simpler tasks may allow many more prompts
    - More complex tasks may consume quota faster

- **Overages and AI credits**
  - Users on **Google AI Pro or Ultra** can:
    - Use included **AI credits** for extra usage beyond baseline quota
    - Purchase additional AI credits
  - AI credits are charged at **Vertex API pricing**
  - The **AI Credit Overages** setting controls whether credits are used after baseline quota is exhausted:
    - **Never**: do not use AI credits automatically; wait for quota refresh
    - **Always**: automatically use AI credits when baseline quota runs out, then return to baseline after refresh

- **Visibility and account controls**
  - Baseline quota usage across models can be viewed in the **settings page**

- **Current limitations**
  - No support for:
    - **Bring-your-own-key**
    - **Bring-your-own-endpoint** for additional rate limits
    - **Organizational tiers** in general availability or via contract

### Assessment
This is a **reference** page with **high durability** in terms of the general quota model and account-tier structure, but **medium** durability overall because plan limits, pricing, and availability are likely to change as Antigravity moves beyond preview. The content type is **reference** with some **announcement-like** product status details. It is **medium-density**: concise but specific, with concrete plan names, refresh intervals, and settings. The source appears to be **primary source** documentation from Google. It is best used as a **refer-back** page when checking entitlement, quota behavior, or limitations. **Scrape quality is good**: the main text and key sections are captured, though the page structure is minimal and any visual layout elements are not meaningful here.
