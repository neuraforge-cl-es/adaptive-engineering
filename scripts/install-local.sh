#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="adaptive-engineering"
PLUGIN_ROOT="${ADAPTIVE_ENGINEERING_CURSOR_PLUGIN_ROOT:-${HOME}/.cursor/plugins/local}"
DEST="${PLUGIN_ROOT}/${NAME}"

python3 "${ROOT}/scripts/validate.py"

verify_existing_installation() {
  python3 - "$DEST" <<'PY'
import json
import sys
from pathlib import Path

manifest = Path(sys.argv[1]) / ".cursor-plugin" / "plugin.json"
try:
    data = json.loads(manifest.read_text(encoding="utf-8"))
except Exception as exc:
    raise SystemExit(f"Refusing to replace an unrecognized directory at {manifest.parent.parent}: {exc}")
if data.get("name") != "adaptive-engineering":
    raise SystemExit(f"Refusing to replace a different plugin at {manifest.parent.parent}")
PY
}

mkdir -p "$PLUGIN_ROOT"
if [[ -L "$DEST" || -e "$DEST" ]]; then
  verify_existing_installation
  echo "Replacing previous local installation: $DEST"
  if [[ -L "$DEST" ]]; then
    rm -- "$DEST"
  else
    rm -rf -- "$DEST"
  fi
fi

mkdir -p "$DEST"
for item in .cursor-plugin rules skills agents commands core docs LICENSE README.md; do
  cp -a "$ROOT/$item" "$DEST/"
done

MANIFEST="$DEST/.cursor-plugin/plugin.json"
test -f "$MANIFEST"

printf '\nInstalled Cursor plugin as a physical copy:\n  %s\n' "$DEST"
printf 'Manifest:\n  %s\n' "$MANIFEST"
printf '\nNext steps:\n'
echo '  1. Run "Developer: Reload Window" from the Command Palette'
echo '  2. Open Cursor Customize / Plugins'
echo '  3. Confirm Adaptive Engineering rules, skills, agents, and commands are enabled'
echo
echo 'Run this installer again after changing the source repository.'
