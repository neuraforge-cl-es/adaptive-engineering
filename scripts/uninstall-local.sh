#!/usr/bin/env bash
set -euo pipefail

NAME="adaptive-engineering"
PLUGIN_ROOT="${ADAPTIVE_ENGINEERING_CURSOR_PLUGIN_ROOT:-${HOME}/.cursor/plugins/local}"
DEST="${PLUGIN_ROOT}/${NAME}"

if [[ ! -L "$DEST" && ! -e "$DEST" ]]; then
  echo "Local plugin is not installed at $DEST"
  exit 0
fi

python3 - "$DEST" <<'PY'
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
manifest = root / ".cursor-plugin" / "plugin.json"
try:
    data = json.loads(manifest.read_text(encoding="utf-8"))
except Exception as exc:
    raise SystemExit(f"Refusing to remove an unrecognized directory at {root}: {exc}")
if data.get("name") != "adaptive-engineering":
    raise SystemExit(f"Refusing to remove a different plugin at {root}")
PY

if [[ -L "$DEST" ]]; then
  rm -- "$DEST"
else
  rm -rf -- "$DEST"
fi
echo "Removed local Cursor plugin: $DEST"
