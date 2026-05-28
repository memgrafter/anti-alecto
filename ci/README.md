# CI secret scanning

Run locally or from CI:

```bash
ci/secret-scan.sh
```

The script installs `detect-secrets` into a uv-managed venv under `.cache/` and uses `gitleaks` from `PATH`, `GITLEAKS_BIN`, or a pinned Go install under `.cache/`.

Refresh reviewed false-positive state only after reviewing scanner output:

```bash
ci/secret-scan.sh --refresh-detect-secrets-baseline
ci/secret-scan.sh --refresh-gitleaks-ignore
```
