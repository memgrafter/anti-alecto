---
url: https://github.com/fakoli/terminalq
title: 'fakoli/terminalq: Bloomberg-style financial terminal — Claude Code MCP plugin with 30 tools'
scraped_at: '2026-04-19T08:22:58Z'
word_count: 2071
raw_file: raw/2026-04-19_fakoli-terminalq-bloomberg-style-financial-terminal-claude-code-mcp-plugin-with-_4b896b3b.txt
tldr: TerminalQ is a Claude Code MCP plugin that turns Claude into a Bloomberg-style financial terminal with portfolio analysis, market data, macro research, charts, and workflow skills powered by local portfolio files and multiple external providers.
key_quote: Your portfolio data stays on your machine.
durability: medium
content_type: mixed
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- Claude Code
- uv
- yfinance
- FastMCP
libraries: []
companies:
- fakoli
- Finnhub
- FRED
- Brave Search
- SEC EDGAR
- Yahoo Finance
- CoinGecko
- Polygon.io
tags:
- financial-terminal
- mcp-plugin
- portfolio-analysis
- market-data
- claude-code
---

### TL;DR
TerminalQ is a Claude Code MCP plugin that turns Claude into a Bloomberg-style financial terminal with portfolio analysis, market data, macro research, charts, and workflow skills powered by local portfolio files and multiple external providers.

### Key Quote
"Your portfolio data stays on your machine."

### Summary
- **What it is:** An MIT-licensed GitHub repo for `fakoli/terminalq`, a “Bloomberg-style financial terminal” for Claude Code built as a **stdio MCP server**.
- **Core promise:** Lets you ask Claude about markets or your portfolio in conversation instead of switching tabs or copying data around.
- **Privacy claim:** Holdings, RSU schedules, and account data live in `~/.terminalq/` and are not sent to external APIs or stored in the cloud.
- **Installation prerequisites:**
  - Claude Code CLI
  - `uv` Python package manager
  - Python 3.11+
- **Quick start:**
  - `git clone https://github.com/fakoli/terminalq.git`
  - `cd terminalq`
  - `./setup.sh`
  - `claude plugin install .`
- **API keys:**
  - Required in `~/.env`: `FINNHUB_API_KEY`, `FRED_API_KEY`
  - Optional: `BRAVE_API_KEY`
- **Data providers and what they power:**
  - **Finnhub**: quotes, profiles, news, earnings, analyst ratings
  - **FRED**: economic indicators, yield curve, forex
  - **Brave Search**: web search for research
  - **SEC EDGAR**: financial statements, SEC filings
  - **Yahoo Finance via yfinance**: historical prices, dividends
  - **CoinGecko**: cryptocurrency data
  - **Polygon.io fallback**: fallback market data provider
- **Portfolio import:**
  - `/tq-ingest holdings`
  - or edit `~/.terminalq/portfolio-holdings.md`
  - Can parse brokerage statements, CSVs, or pasted text

- **6 workflow skills:**
  - `/market-overview` — morning market briefing; pulls index quotes, sector performance, macro indicators, economic calendar, and portfolio data
  - `/company-research SYMBOL` — deep-dive research report; runs 11 tools in parallel and produces financial health, valuation, technicals, bull/bear cases, analyst consensus, and portfolio fit
  - `/portfolio-health` — portfolio health check; uses Sharpe, Sortino, VaR, beta, allocation breakdown, concentration warnings, and RSU schedule
  - `/trade-research SYMBOL` — two-round investment decision support; outputs thesis, valuation, technical entry, portfolio fit, position sizing, risk management, and BUY / WAIT / AVOID
  - `/economic-outlook` — macro analysis; covers business cycle, inflation, labor market, Fed policy, and portfolio implications
  - `/earnings-preview` — earnings season prep; identifies holdings with upcoming earnings and analyzes EPS history, ratings, technicals, and news

- **MCP tools:** The README explicitly says TerminalQ exposes **32 MCP tools** in five categories:
  - **Quotes & Market Data**
    - `terminalq_get_quote`
    - `terminalq_get_quotes_batch`
    - `terminalq_get_historical`
    - `terminalq_get_dividends`
    - `terminalq_get_economic_calendar`
  - **Portfolio & Analytics**
    - `terminalq_get_portfolio`
    - `terminalq_get_portfolio_live`
    - `terminalq_get_rsu_schedule`
    - `terminalq_get_watchlist`
    - `terminalq_get_risk_metrics`
    - `terminalq_get_allocation`
  - **Research & Fundamentals**
    - `terminalq_get_company_profile`
    - `terminalq_get_news`
    - `terminalq_get_earnings`
    - `terminalq_get_analyst_ratings`
    - `terminalq_get_financials`
    - `terminalq_get_filings`
    - `terminalq_get_technicals`
    - `terminalq_screen_stocks`
    - `terminalq_web_search`
  - **Charts & Visualization**
    - `terminalq_chart_price`
    - `terminalq_chart_comparison`
    - `terminalq_chart_allocation`
    - `terminalq_chart_yield_curve`
    - `terminalq_chart_sector_heatmap`
  - **Economics & Crypto**
    - `terminalq_get_economic_indicator`
    - `terminalq_get_macro_dashboard`
    - `terminalq_get_forex`
    - `terminalq_get_crypto`
    - `terminalq_get_crypto_batch`
  - **Audit & Usage**
    - `terminalq_get_audit_log`
    - `terminalq_get_usage_stats`

- **Slash commands:** The README says there are **27 slash commands**, all prefixed with `tq-`, including:
  - `/tq-setup`
  - `/tq-quote AAPL`
  - `/tq-portfolio`
  - `/tq-news AAPL`
  - `/tq-earnings AAPL`
  - `/tq-financials AAPL`
  - `/tq-technicals AAPL`
  - `/tq-ratings AAPL`
  - `/tq-chart AAPL 1y`
  - `/tq-compare AAPL,MSFT,GOOGL`
  - `/tq-historical AAPL 6mo`
  - `/tq-dividends VTI`
  - `/tq-filings AAPL 10-K`
  - `/tq-screen Technology`
  - `/tq-economy`
  - `/tq-yield-curve`
  - `/tq-forex`
  - `/tq-crypto BTC`
  - `/tq-risk`
  - `/tq-allocation`
  - `/tq-rsu`
  - `/tq-watchlist`
  - `/tq-events`
  - `/tq-search "AAPL earnings"`
  - `/tq-ingest holdings`
  - `/tq-audit`
  - `/tq-usage`

- **Architecture highlights:**
  - `terminalq/.claude-plugin/plugin.json`
  - `src/terminalq/server.py` — FastMCP server
  - `src/terminalq/config.py` — API keys, TTLs, rate limits
  - `src/terminalq/cache.py` — file-based cache
  - `src/terminalq/audit.py` — audit trail and arg sanitization
  - `src/terminalq/usage_tracker.py` — budgets and counters
  - `src/terminalq/rate_limiter.py` — token-bucket limiter
  - `src/terminalq/charts.py` — terminal charts
  - `src/terminalq/providers/` — provider modules for Finnhub, FRED, EDGAR, historical data, Polygon, technicals, screener, CoinGecko, search, and portfolio parsing
  - `src/terminalq/analytics/` — risk and allocation analytics
  - `skills/`, `commands/`, `hooks/`, `tests/`, `docs/`
- **Design decisions:**
  - MCP over REST, so Claude Code manages lifecycle and no ports/auth are needed
  - privacy-first local portfolio storage
  - graceful degradation with error objects instead of exceptions
  - standardized output contracts with freshness tables and disclaimers
  - audit trail logging for each tool call

- **Testing:**
  - `uv run pytest tests/ -v`
  - `uv run pytest tests/contracts/ -v`
  - `uv run pytest tests/ --cov=terminalq --cov-report=term-missing`
  - README claims **267 tests**
  - Contract tests check for frontmatter, tool references, numbered steps, output contract references, failure modes, and “when not to use” guidance

- **Contributing:**
  - New provider: create `src/terminalq/providers/your_provider.py`, return `{"error": "...", "source": "your_provider"}` on failure, add TTL/rate limits, register in `server.py`, add tests
  - New skill: create `skills/your-skill/SKILL.md` with frontmatter, numbered steps, tool references, output contract reference, failure modes table, and “when not to use”

- **Note on source consistency:** The README title says **“30 tools”** while the body says **“32 MCP tools”**; that mismatch is present in the source and should be treated as an unresolved inconsistency.

### Assessment
This is a **mixed** reference/documentation and product README with strong installation, architecture, and feature detail. Durability is **medium**: the concepts around MCP plugins, local portfolio storage, and financial workflows are fairly durable, but the specific APIs, counts, and integrations are version- and provider-dependent. Density is **high**, with lots of concrete commands, paths, provider names, and tool lists. Originality is mostly **primary source** marketing/documentation from the repo itself. It’s best used as **refer-back** material rather than deep-study unless you plan to install or extend the project. Scrape quality is **good**: the core README structure, commands, file paths, and most sections are present, though the source itself contains a notable internal inconsistency between “30 tools” and “32 MCP tools,” and another count tension should be treated carefully rather than normalized.
