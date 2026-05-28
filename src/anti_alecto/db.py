"""SQLite store — single source of truth for the pipeline."""

import sqlite3
from pathlib import Path
from typing import Any


SCHEMA_PATH = Path(__file__).parent.parent.parent / "sql" / "schema.sql"
DEFAULT_DB_PATH = Path(__file__).parent.parent.parent / "anti-alecto.db"


class Store:
    """SQLite-backed store for the anti-alecto pipeline."""

    def __init__(self, db_path: Path | None = None):
        self._path = db_path or DEFAULT_DB_PATH
        self._conn = sqlite3.connect(str(self._path))
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        schema = SCHEMA_PATH.read_text()
        self._conn.executescript(schema)
        self._ensure_migrations()

    def _ensure_migrations(self) -> None:
        """Lightweight runtime migrations for existing local DBs."""
        # Legacy table no longer used; raw artifacts live in digests/raw on disk.
        try:
            self._conn.execute("DROP TABLE IF EXISTS content")
            self._conn.commit()
        except sqlite3.Error:
            pass

        # Enforce canonical de-duplication at DB level when possible.
        try:
            self._conn.execute(
                "CREATE UNIQUE INDEX IF NOT EXISTS idx_urls_normalized_unique ON urls(url_normalized)"
            )
            self._conn.commit()
        except sqlite3.Error:
            # If legacy duplicates exist, keep DB usable; app-level checks still apply.
            pass

    def close(self) -> None:
        self._conn.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    # ── Dumps ──

    def record_dump(self, filename: str, tab_count: int) -> int | None:
        """Record an imported dump. Returns id if new, None if already imported."""
        try:
            cur = self._conn.execute(
                "INSERT INTO dumps (filename, tab_count) VALUES (?, ?)",
                (filename, tab_count),
            )
            self._conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None  # already imported

    def get_imported_dumps(self) -> list[str]:
        """Return filenames of all imported dumps."""
        rows = self._conn.execute("SELECT filename FROM dumps").fetchall()
        return [r["filename"] for r in rows]

    # ── URLs ──

    def add_url(
        self,
        url: str,
        url_normalized: str,
        title: str,
        domain: str,
        dump_id: int | None = None,
        status: str = "pending",
        triage_reason: str | None = None,
    ) -> int | None:
        """Add URL. Returns id if new, None if duplicate."""
        try:
            cur = self._conn.execute(
                """INSERT INTO urls (url, url_normalized, title, domain, dump_id, status, triage_reason)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (url, url_normalized, title, domain, dump_id, status, triage_reason),
            )
            self._conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None

    def update_url_status(
        self,
        url_id: int,
        status: str,
        *,
        triage_reason: str | None = None,
        scrape_strategy: str | None = None,
        scrape_failed_reason: str | None = None,
        summarize_failed_reason: str | None = None,
    ) -> None:
        """Update URL pipeline status."""
        fields = ["status = ?", "updated_at = strftime('%Y-%m-%dT%H:%M:%SZ', 'now')"]
        values: list[Any] = [status]

        if triage_reason is not None:
            fields.append("triage_reason = ?")
            values.append(triage_reason)
        if scrape_strategy is not None:
            fields.append("scrape_strategy = ?")
            values.append(scrape_strategy)
        if scrape_failed_reason is not None:
            fields.append("scrape_failed_reason = ?")
            values.append(scrape_failed_reason)
        elif status != "scrape_failed":
            # Clear stale failure reasons when moving out of failed state.
            fields.append("scrape_failed_reason = NULL")
        if summarize_failed_reason is not None:
            fields.append("summarize_failed_reason = ?")
            values.append(summarize_failed_reason)

        values.append(url_id)
        self._conn.execute(
            f"UPDATE urls SET {', '.join(fields)} WHERE id = ?", values
        )
        self._conn.commit()

    def get_urls_by_status(self, status: str, limit: int | None = None) -> list[dict]:
        """Get URLs with given status."""
        sql = "SELECT * FROM urls WHERE status = ? ORDER BY added_at"
        params: list[Any] = [status]
        if limit:
            sql += " LIMIT ?"
            params.append(limit)
        return [dict(r) for r in self._conn.execute(sql, params).fetchall()]

    def get_url_by_id(self, url_id: int) -> dict | None:
        row = self._conn.execute("SELECT * FROM urls WHERE id = ?", (url_id,)).fetchone()
        return dict(row) if row else None

    def get_url_by_normalized(self, url_normalized: str) -> dict | None:
        row = self._conn.execute(
            "SELECT * FROM urls WHERE url_normalized = ?", (url_normalized,)
        ).fetchone()
        return dict(row) if row else None

    def add_url_reference(self, source_url_id: int, target_url_id: int, ref_type: str = "outbound") -> int | None:
        """Create a directed relation between two URL rows (idempotent)."""
        self._conn.execute(
            """INSERT OR IGNORE INTO url_references (source_url_id, target_url_id, ref_type)
               VALUES (?, ?, ?)""",
            (source_url_id, target_url_id, ref_type),
        )
        self._conn.commit()
        row = self._conn.execute(
            """SELECT id FROM url_references
               WHERE source_url_id = ? AND target_url_id = ? AND ref_type = ?""",
            (source_url_id, target_url_id, ref_type),
        ).fetchone()
        return row["id"] if row else None

    def find_terminal_duplicate_by_normalized(
        self,
        url_id: int,
        url_normalized: str,
    ) -> dict | None:
        """Find another terminal record with the exact same normalized URL."""
        if not url_normalized:
            return None

        row = self._conn.execute(
            """SELECT * FROM urls
               WHERE id != ?
                 AND url_normalized = ?
                 AND status IN ('summarized', 'scrape_failed', 'triaged_skip', 'ineligible')
               ORDER BY CASE status
                   WHEN 'summarized' THEN 0
                   WHEN 'ineligible' THEN 1
                   WHEN 'scrape_failed' THEN 2
                   WHEN 'triaged_skip' THEN 3
                   ELSE 9 END,
                   updated_at DESC
               LIMIT 1""",
            (url_id, url_normalized),
        ).fetchone()
        return dict(row) if row else None

    def find_walled_prefix_match(self, url_id: int, normalized_prefix: str) -> dict | None:
        """Find prior ineligible/walled failures sharing a normalized URL prefix."""
        if not normalized_prefix:
            return None

        like_pattern = f"{normalized_prefix}%"
        row = self._conn.execute(
            """SELECT * FROM urls
               WHERE id != ?
                 AND url_normalized LIKE ?
                 AND status IN ('ineligible', 'scrape_failed')
                 AND (
                    LOWER(COALESCE(scrape_failed_reason, '')) LIKE '%paywall%'
                    OR LOWER(COALESCE(scrape_failed_reason, '')) LIKE '%login%'
                    OR LOWER(COALESCE(scrape_failed_reason, '')) LIKE '%auth%'
                    OR LOWER(COALESCE(scrape_failed_reason, '')) LIKE '%session%'
                    OR LOWER(COALESCE(triage_reason, '')) LIKE '%ineligible%'
                    OR LOWER(COALESCE(triage_reason, '')) LIKE '%login%'
                    OR LOWER(COALESCE(triage_reason, '')) LIKE '%auth%'
                    OR LOWER(COALESCE(triage_reason, '')) LIKE '%session%'
                    OR LOWER(COALESCE(triage_reason, '')) LIKE '%paywall%'
                 )
               ORDER BY updated_at DESC
               LIMIT 1""",
            (url_id, like_pattern),
        ).fetchone()
        return dict(row) if row else None

    def find_walled_prefix_match_any(self, normalized_prefix: str) -> dict | None:
        """Prefix blocker lookup for ingest-time global dedupe."""
        return self.find_walled_prefix_match(0, normalized_prefix)

    # ── Summaries ──

    def save_summary(
        self,
        url_id: int,
        summary_md: str,
        frontmatter_json: str | None = None,
        tldr: str | None = None,
        tags: str | None = None,
        content_type: str | None = None,
        durability: str | None = None,
        reference_style: str | None = None,
    ) -> int:
        """Save summary. Replaces existing if re-summarized."""
        self._conn.execute(
            """INSERT INTO summaries
               (url_id, summary_md, frontmatter_json, tldr, tags, content_type, durability, reference_style)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(url_id) DO UPDATE SET
                 summary_md = excluded.summary_md,
                 frontmatter_json = excluded.frontmatter_json,
                 tldr = excluded.tldr,
                 tags = excluded.tags,
                 content_type = excluded.content_type,
                 durability = excluded.durability,
                 reference_style = excluded.reference_style,
                 created_at = strftime('%Y-%m-%dT%H:%M:%SZ', 'now')""",
            (url_id, summary_md, frontmatter_json, tldr, tags, content_type, durability, reference_style),
        )
        self._conn.commit()
        return self._conn.execute(
            "SELECT id FROM summaries WHERE url_id = ?", (url_id,)
        ).fetchone()["id"]

    def search_summaries(self, query: str, limit: int = 20) -> list[dict]:
        """Search summaries by text match."""
        like = f"%{query}%"
        rows = self._conn.execute(
            """SELECT s.*, u.url, u.title, u.domain
               FROM summaries s JOIN urls u ON s.url_id = u.id
               WHERE s.summary_md LIKE ? OR s.tldr LIKE ? OR s.tags LIKE ?
                  OR u.title LIKE ?
               ORDER BY s.created_at DESC LIMIT ?""",
            (like, like, like, like, limit),
        ).fetchall()
        return [dict(r) for r in rows]

    # ── Stats ──

    def status_counts(self) -> dict[str, int]:
        """Pipeline status breakdown."""
        rows = self._conn.execute(
            "SELECT status, COUNT(*) as n FROM urls GROUP BY status"
        ).fetchall()
        return {r["status"]: r["n"] for r in rows}

    def total_urls(self) -> int:
        return self._conn.execute("SELECT COUNT(*) as n FROM urls").fetchone()["n"]

    def total_summaries(self) -> int:
        return self._conn.execute("SELECT COUNT(*) as n FROM summaries").fetchone()["n"]

    def recent_summaries(self, limit: int = 10) -> list[dict]:
        """Most recent summaries with URL info."""
        rows = self._conn.execute(
            """SELECT s.*, u.url, u.title, u.domain
               FROM summaries s JOIN urls u ON s.url_id = u.id
               ORDER BY s.created_at DESC LIMIT ?""",
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]

    def failed_scrapes(self, limit: int = 50) -> list[dict]:
        """URLs that failed scraping."""
        rows = self._conn.execute(
            """SELECT * FROM urls
               WHERE status = 'scrape_failed'
               ORDER BY updated_at DESC LIMIT ?""",
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]
