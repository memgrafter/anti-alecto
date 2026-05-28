"""Configuration loader."""

import re
from pathlib import Path
from typing import Any

import yaml


_DEFAULT_CONFIG = {
    "skip_patterns": [],
    "tracking_params": [],
    "triage": {"batch_size": 30, "interest_profile": ""},
    "scrape": {
        "timeout_seconds": 30,
        "max_concurrent": 3,
        "playwright_wait_ms": 3000,
        "min_content_length": 200,
        "cache_ttl_hours": 24,
    },
    "jina": {"enabled": False},
}


class Config:
    """Loads and provides access to config.yml."""

    def __init__(self, config_path: Path | None = None):
        if config_path is None:
            config_path = Path(__file__).parent.parent.parent / "config.yml"
        self._path = config_path
        self._data = dict(_DEFAULT_CONFIG)
        if self._path.exists():
            with open(self._path) as f:
                loaded = yaml.safe_load(f) or {}
            self._deep_merge(self._data, loaded)
        self._compiled_skip: list[re.Pattern] | None = None

    def _deep_merge(self, base: dict, override: dict) -> None:
        for k, v in override.items():
            if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                self._deep_merge(base[k], v)
            else:
                base[k] = v

    def get(self, key: str, default: Any = None) -> Any:
        """Dot-notation access: config.get('scrape.timeout_seconds')."""
        parts = key.split(".")
        val = self._data
        for p in parts:
            if isinstance(val, dict):
                val = val.get(p)
            else:
                return default
            if val is None:
                return default
        return val

    @property
    def skip_patterns(self) -> list[re.Pattern]:
        if self._compiled_skip is None:
            raw = self._data.get("skip_patterns", [])
            self._compiled_skip = [re.compile(p, re.IGNORECASE) for p in raw]
        return self._compiled_skip

    @property
    def tracking_params(self) -> set[str]:
        return set(self._data.get("tracking_params", []))

    def should_skip(self, url: str) -> tuple[bool, str]:
        """Check if URL matches a skip pattern. Returns (skip, reason)."""
        for pat in self.skip_patterns:
            if pat.search(url):
                return True, f"matches skip pattern: {pat.pattern}"
        return False, ""
