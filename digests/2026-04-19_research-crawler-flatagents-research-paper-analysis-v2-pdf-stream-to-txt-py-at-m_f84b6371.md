---
url: https://github.com/memgrafter/research-crawler-flatagents/blob/main/research_paper_analysis_v2/pdf_stream_to_txt.py#L46
title: research-crawler-flatagents/research_paper_analysis_v2/pdf_stream_to_txt.py at main · memgrafter/research-crawler-flatagents
scraped_at: '2026-04-19T06:49:26Z'
word_count: 793
raw_file: raw/2026-04-19_research-crawler-flatagents-research-paper-analysis-v2-pdf-stream-to-txt-py-at-m_f84b6371.txt
tldr: This Python utility batch-downloads arXiv PDFs, converts them to per-paper text files in `data/<arxiv_id>.txt`, and deletes the temporary PDFs immediately, preferring `gsutil`-backed GCS copies and falling back to `export.arxiv.org`.
key_quote: Download PDF -> extract txt -> delete PDF (streaming/offline prebuild helper).
durability: high
content_type: tutorial
density: high
originality: primary
reference_style: refer-back
scrape_quality: good
people: []
tools:
- gsutil
- httpx
libraries:
- pypdf
companies: []
tags:
- arxiv
- pdf-processing
- text-extraction
- python-scripting
- batch-downloads
---

### TL;DR
This Python utility batch-downloads arXiv PDFs, converts them to per-paper text files in `data/<arxiv_id>.txt`, and deletes the temporary PDFs immediately, preferring `gsutil`-backed GCS copies and falling back to `export.arxiv.org`.

### Key Quote
"Download PDF -> extract txt -> delete PDF (streaming/offline prebuild helper)."

### Summary
- **Purpose**
  - A standalone helper script, intentionally separate from the main runner.
  - Prebuilds text output for papers as `data/<arxiv_id>.txt` while avoiding long-term PDF storage.

- **Per-paper workflow**
  - Creates a temporary PDF file.
  - Tries to download the PDF via `gsutil cp` first from a Google Cloud Storage prefix.
  - If that fails, falls back to downloading from `https://export.arxiv.org/pdf/{arxiv_id}` using `httpx`.
  - Extracts text from the PDF with `pypdf.PdfReader`.
  - Writes one text file per paper, with page markers like `[PAGE 1]`.
  - Deletes the temp PDF in a `finally` block no matter what.

- **Text extraction details**
  - Iterates through all PDF pages.
  - Uses `page.extract_text()` per page, defaulting to empty string if extraction fails.
  - Joins pages with blank lines and prefixes each page with its page number.
  - Re-encodes via UTF-8 with replacement to avoid encoding errors.

- **Input selection**
  - Explicit IDs can be passed with `--ids`.
  - IDs can also be loaded from a file via `--ids-file`.
  - If neither is provided, it queries a SQLite database:
    - Default DB path: `data/v2_executions.sqlite`
    - Override via environment variable `V2_EXECUTIONS_DB_PATH`
  - DB query targets the `executions` table and can filter by:
    - `status='pending'` with `--pending-only`
    - `priority <= -1.0` with `--low-priority-only`
  - It skips papers whose text file already exists and is non-empty unless `--overwrite` is set.

- **Concurrency and limits**
  - Uses `ThreadPoolExecutor` with configurable `--workers` (default 12).
  - Processes up to `--limit` papers (default 64).
  - Deduplicates IDs while preserving order.

- **Defaults and configuration**
  - `--gsutil-bin` defaults to `~/virtualenvs/gsutil/bin/gsutil`, overridable by `RPA_V2_GSUTIL_BIN`.
  - `--gcs-prefix` defaults to `gs://arxiv-dataset/arxiv/pdf`, overridable by `RPA_V2_GCS_PDF_PREFIX`.
  - Export download timeout defaults to 45 seconds.

- **Outputs and reporting**
  - Tracks per-job status as `written`, `skipped`, or `error`.
  - Prints a line for each successful write including source, page count, and character count.
  - Prints an error line for failures.
  - Emits a final summary with totals and source counts.
  - Exits with status code `1` if any errors occurred, otherwise `0`.

### Assessment
This is a high-durability, technical reference/tutorial piece: the concepts are fairly stable, but the exact defaults and data sources are tied to a specific repository and arXiv pipeline. It is dense and implementation-specific, with clear commands, DB assumptions, and fallback logic; the content is original source code rather than commentary or synthesis. It’s best used as a refer-back reference when you need to understand or modify this PDF-to-text prebuild helper. Scrape quality is good for the full file content shown here; no obvious sections or code blocks appear missing.
