---
url: https://docs.parallel.ai/task-api/task-quickstart
title: Task API Quickstart - Parallel
scraped_at: '2026-04-18T05:02:33Z'
word_count: 1099
raw_file: raw/2026-04-18_task-api-quickstart-parallel_3a707946.txt
tldr: Parallel’s Task API quickstart shows how to create AI-powered web research tasks that take plain-language or JSON inputs and return cited, confidence-scored outputs for enrichment, reports, and structured data extraction.
key_quote: Transform complex knowledge work into programmable, repeatable operations powered by AI web research
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- cURL
companies:
- Parallel
tags:
- ai-web-research
- api-quickstart
- data-enrichment
- market-research
- structured-output
---

### TL;DR
Parallel’s Task API quickstart shows how to create AI-powered web research tasks that take plain-language or JSON inputs and return cited, confidence-scored outputs for enrichment, reports, and structured data extraction.

### Key Quote
“Transform complex knowledge work into programmable, repeatable operations powered by AI web research”

### Summary
- The page introduces the **Task API** as a way to combine **AI inference, web search, and live crawling** into repeatable workflows.
- It emphasizes that users can define tasks in **plain language or JSON**, and the API will handle:
  - research
  - synthesis
  - structured output
  - citations
  - confidence levels
- Main use cases listed:
  - **Data enrichment**: enhance CRM records, company databases, or contact lists
  - **Market research**: generate reports on industries, competitors, or trends
  - **Due diligence**: automate compliance checks, background research, verification
  - **Content generation**: produce research-backed reports, summaries, analyses

- **Prerequisites**:
  - Generate an API key on **Platform**
  - Set up with the **TypeScript SDK**, **Python SDK**, or **cURL**
  - Example environment setup includes:
    - `export PARALLEL_API_KEY="PARALLEL_API_KEY"`
    - note to install `curl` and `jq`

- **Quick start workflow**:
  1. **Create** a task run
  2. **Wait** for completion
  3. **Retrieve** the result
- Example Python usage:
  - `client = Parallel(api_key="PARALLEL_API_KEY")`
  - `client.task_run.create(...)`
  - `client.task_run.result(task_run.run_id, api_timeout=3600)`

- The page points to two fuller workflows:
  - **Enrichment Quickstart**
  - **Deep Research Quickstart**
  - These are described as covering polling, webhooks, SSE, async examples, and multiple languages.

- **Core concepts** highlighted:
  - **Task specs**: define research tasks via input/output schemas
  - **Processors**: choose a tier based on research depth and latency
  - **Research Basis**: outputs include citations, reasoning, and confidence

- **Output schema types** supported:
  - **Text string**: simple lookup or single-field answer
  - **JSON schema**: structured enrichment with typed fields
  - **Text schema**: markdown reports with inline citations
  - **Auto**: processor decides the best structure, or omit `task_spec`

- **Input/output patterns** shown:
  - **Question in → Answer out**
    - Example: founding date of the United Nations
    - Output example: `"10-1945"`
  - **Question in → Report out**
    - Example: market research report on the HVAC industry in the USA
    - Uses `processor="ultra"`
    - Produces a multi-page markdown report with citations
  - **Question in → Auto-structured output**
    - Example: top 5 AI infrastructure companies and funding
    - Produces automatically structured JSON
  - **Structured input → Structured output**
    - Example input: `{ "company_name": "Stripe", "website": "stripe.com" }`
    - Example output fields:
      - `founding_year`
      - `employee_count`
      - `total_funding`
    - Uses `processor="core"`

- **Next steps** link to:
  - Enrichment quickstart
  - Deep Research quickstart
  - Task Groups
  - Streaming Events
  - Webhooks
  - API Reference

- **Rate limits** are deferred to the separate Rate Limits documentation.

### Assessment
This is a **high-durability** technical reference/tutorial for Parallel’s Task API, though some specifics like processor names, SDK types, and endpoints may change over time. The content type is **tutorial/reference**, and it is fairly **dense** because it combines conceptual explanation, example code, schema types, and navigation pointers in a compact page. It appears to be **primary source** documentation from Parallel itself, so it’s generally trustworthy for intended usage, though still subject to product/version changes. Best used as a **refer-back** resource when implementing or reviewing Task API workflows. **Scrape quality is good**: the page structure, headings, code blocks, and tables are captured, though some linked subpages and interactive UI elements are only represented as navigation text.
