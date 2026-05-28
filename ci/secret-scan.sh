#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

CI_DIR="$ROOT/ci"
CACHE_DIR="${SECRET_SCAN_CACHE_DIR:-$ROOT/.cache/secret-scan}"
VENV_DIR="${SECRET_SCAN_VENV:-$CACHE_DIR/venv}"
BIN_DIR="$CACHE_DIR/bin"
REPORT_DIR="$CACHE_DIR/reports"

PYTHON_VERSION="${PYTHON_VERSION:-3.12}"
DETECT_SECRETS_VERSION="${DETECT_SECRETS_VERSION:-1.5.0}"
GITLEAKS_VERSION="${GITLEAKS_VERSION:-v8.30.0}"

DETECT_BASELINE="$CI_DIR/detect-secrets.baseline"
GITLEAKS_CONFIG="$CI_DIR/gitleaks.toml"
GITLEAKS_IGNORE="$CI_DIR/gitleaksignore"
GITLEAKS_REPORT="$REPORT_DIR/gitleaks.json"

usage() {
    cat <<'EOF'
Usage: ci/secret-scan.sh [--refresh-detect-secrets-baseline] [--refresh-gitleaks-ignore]

Runs two secret scanners for CI:
  - detect-secrets, installed into a uv-managed venv
  - gitleaks, using an existing binary or a pinned Go install in .cache

Options are intentionally explicit because refreshing baselines/ignores can
hide real leaks. Review scanner output before committing refreshed files.
EOF
}

REFRESH_DETECT_BASELINE=false
REFRESH_GITLEAKS_IGNORE=false
while [[ $# -gt 0 ]]; do
    case "$1" in
        --refresh-detect-secrets-baseline)
            REFRESH_DETECT_BASELINE=true
            shift
            ;;
        --refresh-gitleaks-ignore)
            REFRESH_GITLEAKS_IGNORE=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            usage >&2
            exit 2
            ;;
    esac
done

require_file() {
    local path="$1"
    if [[ ! -f "$path" ]]; then
        echo "Missing required file: $path" >&2
        exit 2
    fi
}

ensure_detect_secrets() {
    if ! command -v uv >/dev/null 2>&1; then
        echo "uv is required to install detect-secrets" >&2
        exit 2
    fi

    if [[ ! -x "$VENV_DIR/bin/python" ]]; then
        uv venv --python "$PYTHON_VERSION" "$VENV_DIR" >/dev/null
    fi

    uv pip install -p "$VENV_DIR/bin/python" "detect-secrets==$DETECT_SECRETS_VERSION" >/dev/null
    DETECT_SECRETS="$VENV_DIR/bin/detect-secrets"
    DETECT_SECRETS_HOOK="$VENV_DIR/bin/detect-secrets-hook"
}

ensure_gitleaks() {
    if [[ -n "${GITLEAKS_BIN:-}" ]]; then
        GITLEAKS="$GITLEAKS_BIN"
    elif command -v gitleaks >/dev/null 2>&1; then
        GITLEAKS="$(command -v gitleaks)"
    else
        mkdir -p "$BIN_DIR"
        GITLEAKS="$BIN_DIR/gitleaks"
        if [[ ! -x "$GITLEAKS" ]]; then
            if ! command -v go >/dev/null 2>&1; then
                echo "gitleaks is not installed and go is unavailable for pinned install" >&2
                echo "Install gitleaks or set GITLEAKS_BIN=/path/to/gitleaks" >&2
                exit 2
            fi
            GOBIN="$BIN_DIR" go install "github.com/zricethezav/gitleaks/v8@$GITLEAKS_VERSION" >/dev/null
        fi
    fi

    if [[ ! -x "$GITLEAKS" ]]; then
        echo "gitleaks binary is not executable: $GITLEAKS" >&2
        exit 2
    fi
}

tracked_files() {
    git ls-files -z -- ':!:ci/detect-secrets.baseline' ':!:ci/gitleaksignore'
}

refresh_detect_baseline() {
    echo "==> refreshing detect-secrets baseline"
    "$DETECT_SECRETS" scan \
        --exclude-files '(^|/)ci/(detect-secrets\.baseline|gitleaksignore)$' \
        > "$DETECT_BASELINE"
}

run_detect_secrets() {
    require_file "$DETECT_BASELINE"
    echo "==> running detect-secrets"
    tracked_files | xargs -0 "$DETECT_SECRETS_HOOK" --baseline "$DETECT_BASELINE"
}

refresh_gitleaks_ignore() {
    echo "==> refreshing gitleaks ignore fingerprints"
    mkdir -p "$REPORT_DIR"
    require_file "$GITLEAKS_CONFIG"
    "$GITLEAKS" detect \
        --source "$ROOT" \
        --config "$GITLEAKS_CONFIG" \
        --redact \
        --no-banner \
        --exit-code 0 \
        --report-format json \
        --report-path "$GITLEAKS_REPORT"

    "$VENV_DIR/bin/python" - "$GITLEAKS_REPORT" "$GITLEAKS_IGNORE" <<'PY'
import json
import sys

report_path, ignore_path = sys.argv[1:3]
with open(report_path, "r", encoding="utf-8") as handle:
    findings = json.load(handle)

fingerprints = sorted({item["Fingerprint"] for item in findings if item.get("Fingerprint")})
with open(ignore_path, "w", encoding="utf-8") as handle:
    handle.write("# Existing reviewed false positives from the current repository history.\n")
    handle.write("# Regenerate intentionally with: ci/secret-scan.sh --refresh-gitleaks-ignore\n")
    for fingerprint in fingerprints:
        handle.write(fingerprint + "\n")
PY
}

run_gitleaks() {
    require_file "$GITLEAKS_CONFIG"
    require_file "$GITLEAKS_IGNORE"
    mkdir -p "$REPORT_DIR"
    echo "==> running gitleaks"
    "$GITLEAKS" detect \
        --source "$ROOT" \
        --config "$GITLEAKS_CONFIG" \
        --redact \
        --no-banner \
        --gitleaks-ignore-path "$GITLEAKS_IGNORE" \
        --report-format json \
        --report-path "$GITLEAKS_REPORT"
}

ensure_detect_secrets
ensure_gitleaks

if [[ "$REFRESH_DETECT_BASELINE" == true ]]; then
    refresh_detect_baseline
else
    run_detect_secrets
fi

if [[ "$REFRESH_GITLEAKS_IGNORE" == true ]]; then
    refresh_gitleaks_ignore
else
    run_gitleaks
fi
