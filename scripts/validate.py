#!/usr/bin/env python3
"""Zero-dependency validator for Adaptive Engineering native and generated packages."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "core" / "spec.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{relative(path)}: invalid JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{relative(path)}: expected a JSON object")
        return {}
    return value


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
        if value and value[0] not in {"\"", "'"} and ": " in value:
            raise ValueError(
                f"invalid unquoted YAML scalar containing ': ': {raw!r}; quote the value"
            )
        meta[key.strip()] = value
    return meta


def validate_named_markdown(
    folder: Path,
    suffixes: set[str],
    required: set[str],
    errors: list[str],
) -> set[str]:
    names: set[str] = set()
    if not folder.is_dir():
        errors.append(f"missing directory: {relative(folder)}")
        return names

    for path in sorted(folder.iterdir()):
        if not path.is_file() or path.suffix not in suffixes:
            continue
        try:
            meta = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{relative(path)}: {exc}")
            continue
        missing = required - meta.keys()
        if missing:
            errors.append(f"{relative(path)}: missing frontmatter keys {sorted(missing)}")
        name = meta.get("name")
        if name:
            if not NAME_RE.fullmatch(name):
                errors.append(f"{relative(path)}: invalid component name {name!r}")
            names.add(name)
    return names


def validate_skills(folder: Path, errors: list[str]) -> set[str]:
    names: set[str] = set()
    if not folder.is_dir():
        errors.append(f"missing directory: {relative(folder)}")
        return names

    for skill_dir in sorted(folder.iterdir()):
        if not skill_dir.is_dir():
            continue
        path = skill_dir / "SKILL.md"
        if not path.exists():
            errors.append(f"{relative(skill_dir)}: missing SKILL.md")
            continue
        try:
            meta = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{relative(path)}: {exc}")
            continue
        unexpected = set(meta) - {"name", "description"}
        if unexpected:
            errors.append(f"{relative(path)}: unsupported frontmatter keys {sorted(unexpected)}")
        for key in ("name", "description"):
            if not meta.get(key):
                errors.append(f"{relative(path)}: missing frontmatter key {key}")
        name = meta.get("name", "")
        if name:
            if not NAME_RE.fullmatch(name):
                errors.append(f"{relative(path)}: invalid skill name {name!r}")
            if name != skill_dir.name:
                errors.append(
                    f"{relative(path)}: skill name {name!r} must match directory {skill_dir.name!r}"
                )
            names.add(name)
    return names


def validate_gemini_commands(errors: list[str]) -> set[str]:
    names: set[str] = set()
    for path in sorted((ROOT / "commands").glob("*.toml")):
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{relative(path)}: invalid TOML: {exc}")
            continue
        for field in ("description", "prompt"):
            if not isinstance(data.get(field), str) or not data[field].strip():
                errors.append(f"{relative(path)}: missing non-empty {field!r}")
        names.add(path.stem)
    return names


def compare_names(label: str, actual: set[str], expected: list[str], errors: list[str]) -> None:
    wanted = set(expected)
    if actual != wanted:
        missing = sorted(wanted - actual)
        extra = sorted(actual - wanted)
        errors.append(f"{label}: component mismatch; missing={missing}, extra={extra}")


def validate_native_packages(spec: dict[str, Any], errors: list[str]) -> None:
    manifests = {
        "cursor": ROOT / ".cursor-plugin" / "plugin.json",
        "claude-code": ROOT / ".claude-plugin" / "plugin.json",
        "codex": ROOT / ".codex-plugin" / "plugin.json",
        "gemini-cli": ROOT / "gemini-extension.json",
    }
    loaded: dict[str, dict[str, Any]] = {}
    for platform, path in manifests.items():
        if not path.exists():
            errors.append(f"missing {platform} manifest: {relative(path)}")
            continue
        data = load_json(path, errors)
        loaded[platform] = data
        if data.get("name") != spec.get("name"):
            errors.append(f"{relative(path)}: name must be {spec.get('name')!r}")
        version = str(data.get("version", ""))
        if not SEMVER_RE.fullmatch(version):
            errors.append(f"{relative(path)}: invalid semantic version {version!r}")
        if version != spec.get("version"):
            errors.append(f"{relative(path)}: version must match core/spec.json")

    if loaded.get("codex", {}).get("skills") != "./skills/":
        errors.append(".codex-plugin/plugin.json: skills must be './skills/'")
    if loaded.get("gemini-cli", {}).get("contextFileName") != "GEMINI.md":
        errors.append("gemini-extension.json: contextFileName must be 'GEMINI.md'")

    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    marketplace = load_json(marketplace_path, errors)
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        errors.append(".claude-plugin/marketplace.json: expected exactly one plugin")
    elif plugins[0].get("name") != spec.get("name") or plugins[0].get("source") != "./":
        errors.append(".claude-plugin/marketplace.json: plugin must reference adaptive-engineering at './'")


def validate_core(errors: list[str]) -> dict[str, Any]:
    if not SPEC_PATH.exists():
        errors.append("missing core/spec.json")
        return {}
    spec = load_json(SPEC_PATH, errors)
    if spec.get("name") != "adaptive-engineering":
        errors.append("core/spec.json: unexpected package name")
    version = str(spec.get("version", ""))
    if not SEMVER_RE.fullmatch(version):
        errors.append(f"core/spec.json: invalid semantic version {version!r}")
    for path in (
        ROOT / "core" / "PRINCIPLES.md",
        ROOT / "core" / "METHODOLOGY.md",
        ROOT / "core" / "workflows" / "fast.md",
        ROOT / "core" / "workflows" / "standard.md",
        ROOT / "core" / "workflows" / "deep.md",
    ):
        if not path.is_file():
            errors.append(f"missing canonical file: {relative(path)}")
    return spec


def validate_generated_packages(spec: dict[str, Any], errors: list[str]) -> None:
    agent_root = ROOT / "dist" / "agent-plugin" / "adaptive-engineering"
    manifest_path = agent_root / "plugin.json"
    if not manifest_path.exists():
        errors.append("missing generated Agent Plugin; run scripts/build-agent-plugin.py")
    else:
        manifest = load_json(manifest_path, errors)
        allowed = {
            "$schema", "name", "version", "description", "author", "homepage",
            "repository", "license", "keywords", "extensions",
        }
        extra = set(manifest) - allowed
        if extra:
            errors.append(f"{relative(manifest_path)}: unsupported Agent Plugin fields {sorted(extra)}")
        if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            errors.append(f"{relative(manifest_path)}: invalid Agent Plugins schema")
        if manifest.get("name") != spec.get("name") or manifest.get("version") != spec.get("version"):
            errors.append(f"{relative(manifest_path)}: identity must match core/spec.json")
        generated_skills = validate_skills(agent_root / "skills", errors)
        compare_names("generated Agent Plugin skills", generated_skills, spec["components"]["skills"], errors)
        if not (agent_root / "core" / "spec.json").is_file():
            errors.append("generated Agent Plugin is missing canonical core")

    opencode_root = ROOT / "dist" / "opencode"
    if not opencode_root.exists():
        errors.append("missing generated OpenCode adapter; run scripts/build-opencode.py")
    else:
        generated_skills = validate_skills(opencode_root / ".opencode" / "skills", errors)
        compare_names("generated OpenCode skills", generated_skills, spec["components"]["skills"], errors)
        for path in (
            opencode_root / "AGENTS.md",
            opencode_root / ".opencode" / "AGENTS.md",
            opencode_root / ".opencode" / "core" / "spec.json",
        ):
            if not path.is_file():
                errors.append(f"generated OpenCode adapter missing {relative(path)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", action="store_true", help="also validate generated packages")
    args = parser.parse_args()

    errors: list[str] = []
    spec = validate_core(errors)
    components = spec.get("components", {})

    rule_files = {path.stem for path in (ROOT / "rules").glob("*.mdc")}
    validate_named_markdown(ROOT / "rules", {".mdc"}, {"description", "alwaysApply"}, errors)
    agent_names = validate_named_markdown(ROOT / "agents", {".md"}, {"name", "description"}, errors)
    command_names = validate_named_markdown(ROOT / "commands", {".md"}, {"name", "description"}, errors)
    skill_names = validate_skills(ROOT / "skills", errors)
    gemini_names = validate_gemini_commands(errors)

    if components:
        compare_names("rules", rule_files, components["rules"], errors)
        compare_names("agents", agent_names, components["agents"], errors)
        compare_names("Markdown commands", command_names, components["commands"], errors)
        compare_names("Gemini commands", gemini_names, components["commands"], errors)
        compare_names("skills", skill_names, components["skills"], errors)

    validate_native_packages(spec, errors)

    for path in (
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "docs" / "INSTALLATION.md",
        ROOT / "docs" / "METHODOLOGY.md",
        ROOT / "docs" / "PLATFORMS.md",
        ROOT / "docs" / "TEST-SCENARIOS.md",
        ROOT / ".github" / "workflows" / "validate.yml",
    ):
        if not path.is_file():
            errors.append(f"missing required file: {relative(path)}")

    if args.dist and components:
        validate_generated_packages(spec, errors)

    if errors:
        print("Validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    suffix = ", generated packages" if args.dist else ""
    print(
        "Validation OK: "
        f"{len(rule_files)} rule(s), {len(skill_names)} skill(s), "
        f"{len(agent_names)} agent(s), {len(command_names)} Markdown command(s), "
        f"{len(gemini_names)} Gemini command(s){suffix}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
