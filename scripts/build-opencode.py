#!/usr/bin/env python3
"""Build a project/global OpenCode adapter using documented discovery paths."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "opencode"
CONFIG = OUTPUT / ".opencode"


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    CONFIG.mkdir(parents=True)

    shutil.copytree(ROOT / "skills", CONFIG / "skills")
    shutil.copytree(ROOT / "core", CONFIG / "core")
    shutil.copy2(ROOT / "AGENTS.md", OUTPUT / "AGENTS.md")
    shutil.copy2(ROOT / "AGENTS.md", CONFIG / "AGENTS.md")
    shutil.copy2(ROOT / "LICENSE", OUTPUT / "LICENSE")
    print(f"Built OpenCode adapter: {OUTPUT}")


if __name__ == "__main__":
    main()
