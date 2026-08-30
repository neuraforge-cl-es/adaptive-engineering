#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="adaptive-engineering"
DEST="${HOME}/.cursor/plugins/local/${NAME}"

python3 "${ROOT}/scripts/validate.py"
mkdir -p "$(dirname "$DEST")"

# Cursor 3.17.x may ignore symlinks that point outside ~/.cursor/plugins/local.
# Install a physical copy instead.
if [[ -L "$DEST" || -e "$DEST" ]]; then
  echo "Removing previous local installation: $DEST"
  rm -rf "$DEST"
fi

mkdir -p "$DEST"
cp -a "$ROOT"/. "$DEST"/

# Do not keep development/cache artifacts in the installed copy.
rm -rf "$DEST/scripts/__pycache__" 2>/dev/null || true

MANIFEST="$DEST/.cursor-plugin/plugin.json"
if [[ ! -f "$MANIFEST" ]]; then
  echo "ERROR: plugin manifest was not copied to $MANIFEST" >&2
  exit 1
fi

printf '\nInstalled Cursor plugin as a physical copy:\n  %s\n' "$DEST"
printf 'Manifest:\n  %s\n' "$MANIFEST"
printf '\nNext steps:\n'
echo '  1. Cursor Settings → Rules, Skills, Subagents'
echo '  2. Ensure "Include third-party Plugins, Skills, and other configs" is ON'
echo '  3. Run "Developer: Reload Window" from the Command Palette'
echo '  4. Open Customize and check Plugins / Rules / Skills / Subagents / Commands'
echo
printf 'Quick verification:\n  test -f "%s" && echo "Adaptive Engineering files installed: OK"\n' "$MANIFEST"
