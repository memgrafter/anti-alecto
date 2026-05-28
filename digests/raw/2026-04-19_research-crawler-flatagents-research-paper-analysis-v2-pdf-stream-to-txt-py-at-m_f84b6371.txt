#!/usr/bin/env -S uv run python
"""Download PDF -> extract txt -> delete PDF (streaming/offline prebuild helper).

This script is intentionally decoupled from the main runner.
It prebuilds data/<arxiv_id>.txt while avoiding persistent PDF storage.

Behavior per paper:
1) Download to a temp PDF (gsutil first, export fallback)
2) Extract text to data/<arxiv_id>.txt
3) Delete temp PDF immediately (always)

By default it targets low-priority pending work to avoid contention.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import os
import sqlite3
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import httpx
from pypdf import PdfReader


DEFAULT_GSUTIL_BIN = str(Path.home() / "virtualenvs" / "gsutil" / "bin" / "gsutil")
DEFAULT_GCS_PREFIX = "gs://arxiv-dataset/arxiv/pdf"


@dataclass
class JobResult:
    arxiv_id: str
    status: str  # written | skipped | error
    source: str = ""
    pages: int = 0
    chars: int = 0
    error: str = ""


def _extract_pdf_to_txt(pdf_path: Path, txt_path: Path) -> tuple[int, int]:
    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append(f"[PAGE {i + 1}]\n{text}")

    full_text = "\n\n".join(pages)
    full_text = full_text.encode("utf-8", "replace").decode("utf-8")
    txt_path.write_text(full_text, encoding="utf-8")
    return len(reader.pages), len(full_text)


def _download_gsutil(gsutil_bin: str, gcs_prefix: str, arxiv_id: str, out_pdf: Path) -> bool:
    month = arxiv_id[:4]
    uri = f"{gcs_prefix}/{month}/{arxiv_id}v1.pdf"
    proc = subprocess.run(
        [gsutil_bin, "cp", uri, str(out_pdf)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=120,
    )
    return proc.returncode == 0 and out_pdf.exists() and out_pdf.stat().st_size > 0


def _download_export(client: httpx.Client, arxiv_id: str, out_pdf: Path) -> bool:
    url = f"https://export.arxiv.org/pdf/{arxiv_id}"
    with client.stream("GET", url) as resp:
        if resp.status_code != 200:
            return False
        with out_pdf.open("wb") as f:
            for chunk in resp.iter_bytes(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
    return out_pdf.exists() and out_pdf.stat().st_size > 0


def _process_one(
    arxiv_id: str,
    data_dir: Path,
    overwrite: bool,
    gsutil_bin: str,
    gcs_prefix: str,
    export_timeout: float,
) -> JobResult:
    safe_id = arxiv_id.replace("/", "_")
    txt_path = data_dir / f"{safe_id}.txt"

    if not overwrite and txt_path.exists() and txt_path.stat().st_size > 0:
        return JobResult(arxiv_id=safe_id, status="skipped", source="txt_cached")

    tmp_pdf: Optional[Path] = None
    source = ""

    try:
        with tempfile.NamedTemporaryFile(prefix=f"rpa_{safe_id}_", suffix=".pdf", delete=False) as tf:
            tmp_pdf = Path(tf.name)

        # 1) gsutil first
        if gsutil_bin and Path(gsutil_bin).exists():
            if _download_gsutil(gsutil_bin, gcs_prefix, safe_id, tmp_pdf):
                source = "gsutil"

        # 2) export fallback
        if not source:
            timeout = httpx.Timeout(export_timeout)
            with httpx.Client(timeout=timeout, follow_redirects=True) as client:
                ok = _download_export(client, safe_id, tmp_pdf)
            if not ok:
                return JobResult(arxiv_id=safe_id, status="error", source="export", error="download_failed")
            source = "export"

        pages, chars = _extract_pdf_to_txt(tmp_pdf, txt_path)
        return JobResult(arxiv_id=safe_id, status="written", source=source, pages=pages, chars=chars)

    except Exception as exc:  # noqa: BLE001
        return JobResult(arxiv_id=safe_id, status="error", source=source or "unknown", error=str(exc))

    finally:
        if tmp_pdf is not None:
            try:
                tmp_pdf.unlink(missing_ok=True)
            except Exception:
                pass


def _ids_from_db(db_path: Path, limit: int, low_priority_only: bool, require_pending: bool, data_dir: Path) -> list[str]:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row

    where = ["arxiv_id IS NOT NULL"]
    if require_pending:
        where.append("status='pending'")
    if low_priority_only:
        where.append("priority <= -1.0")

    query = f"""
    SELECT arxiv_id
    FROM executions
    WHERE {' AND '.join(where)}
    ORDER BY created_at ASC
    """

    out: list[str] = []
    for row in conn.execute(query):
        aid = str(row[0]).replace("/", "_")
        txt = data_dir / f"{aid}.txt"
        if txt.exists() and txt.stat().st_size > 0:
            continue
        out.append(aid)
        if limit > 0 and len(out) >= limit:
            break

    conn.close()
    return out


def _iter_ids(args: argparse.Namespace, data_dir: Path) -> list[str]:
    ids: list[str] = []

    if args.ids:
        ids.extend([x.strip().replace("/", "_") for x in args.ids if x.strip()])

    if args.ids_file:
        p = Path(args.ids_file)
        if p.exists():
            ids.extend([ln.strip().replace("/", "_") for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()])

    if not ids:
        db_path = Path(os.environ.get("V2_EXECUTIONS_DB_PATH", str(data_dir / "v2_executions.sqlite")))
        ids = _ids_from_db(
            db_path=db_path,
            limit=args.limit,
            low_priority_only=args.low_priority_only,
            require_pending=args.pending_only,
            data_dir=data_dir,
        )

    # de-dup preserve order
    seen = set()
    deduped = []
    for aid in ids:
        if aid in seen:
            continue
        seen.add(aid)
        deduped.append(aid)

    if args.limit > 0:
        deduped = deduped[: args.limit]

    return deduped


def main() -> int:
    parser = argparse.ArgumentParser(description="Stream PDFs to txt and delete PDFs immediately")
    parser.add_argument("--data-dir", default="data", help="Data directory (default: data)")
    parser.add_argument("--workers", type=int, default=12, help="Parallel workers")
    parser.add_argument("--limit", type=int, default=64, help="Max papers to process")
    parser.add_argument("--overwrite", action="store_true", help="Rewrite txt even if non-empty txt exists")

    parser.add_argument("--ids", nargs="*", default=[], help="Explicit arXiv IDs")
    parser.add_argument("--ids-file", default="", help="Text file with one arXiv ID per line")

    parser.add_argument("--pending-only", action="store_true", default=True, help="Select only pending rows from DB")
    parser.add_argument("--low-priority-only", action="store_true", default=True, help="Select only priority <= -1.0 rows from DB")

    parser.add_argument("--gsutil-bin", default=os.environ.get("RPA_V2_GSUTIL_BIN", DEFAULT_GSUTIL_BIN))
    parser.add_argument("--gcs-prefix", default=os.environ.get("RPA_V2_GCS_PDF_PREFIX", DEFAULT_GCS_PREFIX))
    parser.add_argument("--export-timeout", type=float, default=45.0)
    args = parser.parse_args()

    data_dir = Path(args.data_dir).resolve()
    data_dir.mkdir(parents=True, exist_ok=True)

    ids = _iter_ids(args, data_dir)
    if not ids:
        print("No IDs to process.")
        return 0

    workers = max(1, int(args.workers))
    print(
        f"Processing {len(ids)} papers | workers={workers} | pending_only={args.pending_only} "
        f"low_priority_only={args.low_priority_only} | overwrite={args.overwrite}"
    )

    written = skipped = errors = 0
    source_counts: dict[str, int] = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [
            ex.submit(
                _process_one,
                aid,
                data_dir,
                args.overwrite,
                args.gsutil_bin,
                args.gcs_prefix,
                args.export_timeout,
            )
            for aid in ids
        ]

        for fut in concurrent.futures.as_completed(futs):
            res = fut.result()
            source_counts[res.source] = source_counts.get(res.source, 0) + 1

            if res.status == "written":
                written += 1
                print(f"WRITE  {res.arxiv_id} source={res.source} pages={res.pages} chars={res.chars}")
            elif res.status == "skipped":
                skipped += 1
            else:
                errors += 1
                print(f"ERROR  {res.arxiv_id} source={res.source} err={res.error}")

    print(f"Summary: written={written} skipped={skipped} errors={errors} total={len(ids)}")
    print(f"Sources: {source_counts}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
