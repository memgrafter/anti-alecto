#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

# Parse arguments
USE_LOCAL_SDK=false
while [[ $# -gt 0 ]]; do
    case "$1" in
        --local)
            USE_LOCAL_SDK=true
            shift
            ;;
        *)
            echo "Usage: $0 [--local]"
            echo "  --local  Install flatagents/flatmachines from ~/code/flatagents/sdk/python (editable)"
            exit 1
            ;;
    esac
done

LOCAL_SDK_PATH="${FLATAGENTS_SDK_PATH:-${FLATMACHINES_SDK_PATH:-$HOME/code/flatmachines}}/sdk/python"

# Detect package manager
if command -v uv &>/dev/null; then
    USE_UV=true
else
    USE_UV=false
fi

pip_install() {
    if [[ "$USE_UV" = true ]]; then
        uv pip install -p "$VENV/bin/python" "$@"
    else
        "$VENV/bin/python" -m pip install "$@"
    fi
}

# Create venv
if [[ ! -d "$VENV" ]]; then
    echo "Creating virtualenv..."
    if [[ "$USE_UV" = true ]]; then
        uv venv --python 3.12 "$VENV"
    else
        python3 -m venv "$VENV"
    fi
fi

source "$VENV/bin/activate"

# Ensure pip
if [[ "$USE_UV" = false ]]; then
    python -m ensurepip --upgrade 2>/dev/null || true
    python -m pip install -U pip
fi

# Install flatagents SDK
if [[ "$USE_LOCAL_SDK" = true ]]; then
    if [[ -f "$LOCAL_SDK_PATH/flatagents/pyproject.toml" ]]; then
        echo "Installing flatagents from local SDK (editable)..."
        pip_install -e "$LOCAL_SDK_PATH/flatagents"
        [[ -f "$LOCAL_SDK_PATH/flatmachines/pyproject.toml" ]] && \
            pip_install -e "$LOCAL_SDK_PATH/flatmachines"
    elif [[ -f "$LOCAL_SDK_PATH/pyproject.toml" ]]; then
        pip_install -e "$LOCAL_SDK_PATH"
    else
        echo "ERROR: Local SDK not found at $LOCAL_SDK_PATH" >&2
        exit 1
    fi
fi

# Install project
echo "Installing anti-alecto..."
pip_install -e "$SCRIPT_DIR"

# Install playwright browsers
echo "Installing Playwright Chromium..."
"$VENV/bin/python" -m playwright install chromium

echo ""
echo "✓ anti-alecto installed"
echo ""
echo "  source $VENV/bin/activate"
echo "  ./bin/aa --help"
