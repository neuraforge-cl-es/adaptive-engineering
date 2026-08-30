#!/usr/bin/env bash
set -euo pipefail

NAME="adaptive-engineering"
DEST="${HOME}/.cursor/plugins/local/${NAME}"

if [[ -L "$DEST" ]]; then
  rm "$DEST"
  echo "Removed local plugin symlink: $DEST"
elif [[ -e "$DEST" ]]; then
  echo "$DEST exists but is not a symlink; refusing to delete it automatically." >&2
  exit 1
else
  echo "Local plugin is not installed at $DEST"
fi
