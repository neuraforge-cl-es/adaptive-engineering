#!/usr/bin/env python3
"""Build deterministic ZIP assets for an Adaptive Engineering GitHub release."""

from __future__ import annotations

import hashlib
import json
import shutil
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
RELEASES = DIST / "releases"
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def load_version() -> str:
    spec = json.loads((ROOT / "core" / "spec.json").read_text(encoding="utf-8"))
    version = spec.get("version")
    if not isinstance(version, str) or not version:
        raise SystemExit("core/spec.json does not contain a valid version")
    return version


def build_generated_packages() -> None:
    import subprocess

    for script in (
        "build-agent-plugin.py",
        "build-antigravity.py",
        "build-opencode.py",
    ):
        subprocess.run(["python3", str(ROOT / "scripts" / script)], check=True)


def add_file(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    info = zipfile.ZipInfo(arcname.replace("\\", "/"), FIXED_TIMESTAMP)
    mode = source.stat().st_mode
    permissions = stat.S_IMODE(mode)
    info.external_attr = (permissions & 0xFFFF) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    archive.writestr(info, source.read_bytes())


def add_tree(archive: zipfile.ZipFile, source: Path, prefix: str = "") -> None:
    for path in sorted(p for p in source.rglob("*") if p.is_file()):
        relative = path.relative_to(source).as_posix()
        arcname = f"{prefix.rstrip('/')}/{relative}" if prefix else relative
        add_file(archive, path, arcname)


def create_zip(path: Path, entries: list[tuple[Path, str]]) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        for source, prefix in entries:
            if source.is_dir():
                add_tree(archive, source, prefix)
            elif source.is_file():
                arcname = prefix or source.name
                add_file(archive, source, arcname)
            else:
                raise SystemExit(f"Missing release input: {source.relative_to(ROOT)}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    version = load_version()
    build_generated_packages()

    if RELEASES.exists():
        shutil.rmtree(RELEASES)
    RELEASES.mkdir(parents=True)

    cursor_root = "adaptive-engineering"
    cursor_entries: list[tuple[Path, str]] = []
    for item in (
        ".cursor-plugin",
        "rules",
        "skills",
        "agents",
        "commands",
        "core",
        "docs",
    ):
        cursor_entries.append((ROOT / item, f"{cursor_root}/{item}"))
    cursor_entries.extend(
        [
            (ROOT / "LICENSE", f"{cursor_root}/LICENSE"),
            (ROOT / "README.md", f"{cursor_root}/README.md"),
        ]
    )

    assets = {
        f"adaptive-engineering-cursor-v{version}.zip": cursor_entries,
        f"adaptive-engineering-agent-plugin-v{version}.zip": [
            (DIST / "agent-plugin" / "adaptive-engineering", "adaptive-engineering")
        ],
        f"adaptive-engineering-antigravity-v{version}.zip": [
            (DIST / "antigravity" / "adaptive-engineering", "adaptive-engineering")
        ],
        f"adaptive-engineering-opencode-v{version}.zip": [
            (DIST / "opencode", "")
        ],
    }

    created: list[Path] = []
    for filename, entries in assets.items():
        output = RELEASES / filename
        create_zip(output, entries)
        created.append(output)
        print(f"Created {output.relative_to(ROOT)}")

    checksums = RELEASES / "SHA256SUMS.txt"
    checksums.write_text(
        "".join(f"{sha256(path)}  {path.name}\n" for path in sorted(created)),
        encoding="utf-8",
    )
    print(f"Created {checksums.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
