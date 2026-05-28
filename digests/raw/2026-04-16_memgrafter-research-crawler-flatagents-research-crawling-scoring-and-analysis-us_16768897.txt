# Discovery Pipeline

Unified pipeline that discovers, scores, enriches, and summarizes new AI/ML papers.

## Quick Start

```bash
# Set required environment variables
export OPENALEX_MAILTO='your-email@example.com'
export OPENALEX_API_KEY='your-openalex-key'
export CEREBRAS_API_KEY='your-cerebras-key'

# Run the pipeline
cd discovery_pipeline
./run.sh
```

Install behavior: `run.sh` skips dependency installs if required packages are already present in `.venv`. Use `--upgrade`/`-u` to force reinstall/upgrade.

## Usage

### Automatic Backfill (Normal Case)

The pipeline automatically determines the date range by checking the last successful crawler run:

```bash
./run.sh
```

- If no previous runs exist, defaults to **last 7 days**
- Otherwise, fetches papers since the last completed run
- This is the recommended approach for scheduled (cron) runs

### Custom Date Ranges

**Last 7 days:**
```bash
./run.sh --since 2025-12-29
```

**Last 31 days:**
```bash
./run.sh --since 2025-12-05
```

**Specific date:**
```bash
./run.sh --since 2024-01-01
```

### Skip Phases

Generate only a report from existing data (no crawling/scoring/enriching):
```bash
./run.sh --skip-crawl --skip-score --skip-enrich
```

Skip just the enrichment phase:
```bash
./run.sh --skip-enrich
```

### All Options

| Argument | Description |
|----------|-------------|
| `--since YYYY-MM-DD` | Override auto-detected start date |
| `--db-path PATH` | Path to SQLite database (default: `../arxiv_crawler/data/arxiv.sqlite`) |
| `--report-path PATH` | Directory for reports (default: `./reports`) |
| `--limit N` | Max papers per phase (default: 10000) |
| `--skip-crawl` | Skip arXiv crawling |
| `--skip-score` | Skip relevance scoring |
| `--skip-enrich` | Skip OpenAlex enrichment |
| `--dry-run` | Run without making changes |
| `--upgrade` / `-u` | Reinstall/upgrade dependencies |

## Pipeline Phases

1. **Crawl** - Fetch new papers from arXiv API
2. **Score** - Calculate FMR relevance scores using sentence embeddings
3. **Enrich** - Add author/citation data from OpenAlex
4. **Report** - Generate LLM-powered summary of top papers

## Output

Reports are saved to `./reports/discovery_report_YYYY-MM-DD_HHMM.md` and include:
- Executive summary of themes and trends
- Top 10 papers with implementation notes
- arXiv links, publication dates, and categories

## Scheduling

Add to crontab for weekly runs:
```bash
0 6 * * 1 cd /path/to/discovery_pipeline && ./run.sh >> /tmp/discovery.log 2>&1
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENALEX_MAILTO` | Yes | Email for OpenAlex API (polite pool) |
| `OPENALEX_API_KEY` | Yes | API key for OpenAlex |
| `CEREBRAS_API_KEY` | Yes | API key for report generation |
