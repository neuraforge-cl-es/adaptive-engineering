#!/usr/bin/env python3
"""Build a portable Agent Plugins 1.0 package from the canonical repository files."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "agent-plugin" / "adaptive-engineering"


def main() -> None:
    spec = json.loads((ROOT / "core" / "spec.json").read_text(encoding="utf-8"))
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": spec["name"],
        "version": spec["version"],
        "description": "Choose proportionate engineering process and ship the simplest verified solution.",
        "author": {"name": "Neuraforge"},
        "repository": "https://github.com/neuraforge-cl-es/adaptive-engineering",
        "license": "MIT",
        "keywords": ["software-engineering", "workflow", "verification", "simplicity"],
    }
    (OUTPUT / "plugin.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    shutil.copytree(ROOT / "skills", OUTPUT / "skills")
    shutil.copytree(ROOT / "core", OUTPUT / "core")
    shutil.copy2(ROOT / "LICENSE", OUTPUT / "LICENSE")
    print(f"Built Agent Plugin: {OUTPUT}")


if __name__ == "__main__":
    main()
