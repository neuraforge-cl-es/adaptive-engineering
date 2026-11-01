#!/usr/bin/env python3
"""Build a Google Antigravity plugin from the canonical repository files."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "antigravity" / "adaptive-engineering"


def main() -> None:
    spec = json.loads((ROOT / "core" / "spec.json").read_text(encoding="utf-8"))

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    manifest = {
        "$schema": "https://antigravity.google/schemas/v1/plugin.json",
        "name": spec["name"],
        "description": (
            "Choose proportionate engineering process and ship the simplest "
            "correct, verified solution."
        ),
    }
    (OUTPUT / "plugin.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    shutil.copytree(ROOT / "skills", OUTPUT / "skills")
    shutil.copytree(ROOT / "agents", OUTPUT / "agents")
    shutil.copytree(ROOT / "core", OUTPUT / "core")

    rules = OUTPUT / "rules"
    rules.mkdir()
    shutil.copy2(ROOT / "AGENTS.md", rules / "adaptive-engineering.md")
    shutil.copy2(ROOT / "LICENSE", OUTPUT / "LICENSE")

    print(f"Built Antigravity plugin: {OUTPUT}")


if __name__ == "__main__":
    main()
