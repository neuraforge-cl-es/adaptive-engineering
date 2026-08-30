#!/usr/bin/env python3
"""Zero-dependency structural validator for the Adaptive Engineering Cursor plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".cursor-plugin" / "plugin.json"
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")
    meta: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"invalid frontmatter line: {raw!r}")
        key, value = raw.split(":", 1)
        value = value.strip()
        # YAML plain scalars cannot safely contain ": ". Cursor parses this
        # frontmatter as YAML and may silently skip the component if invalid.
        if value and value[0] not in {"\"", "'"} and ": " in value:
            raise ValueError(
                f"invalid unquoted YAML scalar containing ': ': {raw!r}; quote the value"
            )
        meta[key.strip()] = value
    return meta


def validate_manifest(errors: list[str]) -> None:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{MANIFEST.relative_to(ROOT)}: invalid JSON: {exc}")
        return

    name = data.get("name", "")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        errors.append("plugin name must be lowercase kebab-case/dotted identifier")

    version = data.get("version")
    if version is not None and not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", str(version)):
        errors.append("version should be semantic-version shaped")

    for field in ("rules", "skills", "agents", "commands"):
        value = data.get(field)
        if not value:
            continue
        paths = [value] if isinstance(value, str) else value
        for rel in paths:
            candidate = (ROOT / rel).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"manifest {field} path escapes plugin root: {rel}")
                continue
            if not candidate.exists():
                errors.append(f"manifest {field} path does not exist: {rel}")


def validate_components(errors: list[str]) -> None:
    specs = [
        (ROOT / "rules", {".mdc"}, {"description", "alwaysApply"}),
        (ROOT / "agents", {".md", ".mdc", ".markdown"}, {"name", "description"}),
        (ROOT / "commands", {".md", ".mdc", ".markdown", ".txt"}, {"name", "description"}),
    ]

    for folder, suffixes, required in specs:
        for path in sorted(folder.iterdir()):
            if not path.is_file() or path.suffix not in suffixes:
                continue
            try:
                meta = parse_frontmatter(path)
            except ValueError as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
                continue
            missing = required - meta.keys()
            if missing:
                errors.append(f"{path.relative_to(ROOT)}: missing frontmatter keys {sorted(missing)}")
            if "name" in meta and not NAME_RE.fullmatch(meta["name"]):
                errors.append(f"{path.relative_to(ROOT)}: invalid component name {meta['name']!r}")

    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if not skill_dir.is_dir():
            continue
        path = skill_dir / "SKILL.md"
        if not path.exists():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
            continue
        try:
            meta = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        for key in ("name", "description"):
            if key not in meta:
                errors.append(f"{path.relative_to(ROOT)}: missing frontmatter key {key}")
        if meta.get("name") and not NAME_RE.fullmatch(meta["name"]):
            errors.append(f"{path.relative_to(ROOT)}: invalid skill name {meta['name']!r}")


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.exists():
        errors.append("missing .cursor-plugin/plugin.json")
    else:
        validate_manifest(errors)
    validate_components(errors)

    if errors:
        print("Validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    skills = len(list((ROOT / "skills").glob("*/SKILL.md")))
    agents = len(list((ROOT / "agents").glob("*.md")))
    commands = len(list((ROOT / "commands").glob("*.md")))
    rules = len(list((ROOT / "rules").glob("*.mdc")))
    print(f"Validation OK: {rules} rule(s), {skills} skill(s), {agents} agent(s), {commands} command(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
