# Changelog

## 0.3.0 — 2026-08-30

- Added a generated Google Antigravity plugin using the official `plugin.json` schema.
- Reused the canonical nine skills and core methodology without host-specific duplication.
- Added four Antigravity-discoverable specialist agents and a compact persistent rule.
- Added global, workspace, and Antigravity CLI installation instructions.
- Extended zero-dependency validation and CI to build and verify the Antigravity package.

## 0.2.0 — 2026-08-30

- Extracted a canonical, host-agnostic methodology under `core/`.
- Added the portable `adaptive-engineering` entry skill, bringing the shared skill set to nine.
- Preserved the Cursor plugin surface and upgraded its manifest to `0.2.0`.
- Added native Claude Code, ChatGPT/Codex, and Gemini CLI manifests and adapters.
- Added six Gemini CLI TOML commands alongside the existing Markdown commands.
- Added builders for Agent Plugins 1.0 and OpenCode discovery layouts.
- Expanded zero-dependency validation across native and generated packages.
- Added GitHub Actions validation and Cursor install/uninstall round-trip testing.
- Fixed physical-copy uninstall behavior and clarified that source updates require reinstalling Cursor.

## 0.1.2 — 2026-08-30

- Fixed invalid YAML frontmatter in `commands/fast.md`; Cursor was silently dropping `/fast`, leaving only five commands.
- Fixed the same YAML scalar issue in `rules/adaptive-engineering.mdc`.
- Strengthened the zero-dependency validator to reject unquoted YAML scalars containing `: ` so this class of discovery failure is caught before installation.

## 0.1.1

- Local installer now copies the plugin into `~/.cursor/plugins/local/adaptive-engineering` instead of using a symlink, matching current Cursor 3.17.x behavior.
- Simplified `plugin.json` to documented fields and automatic component discovery.
- Installer now replaces an older local installation and verifies the manifest after copy.

## 0.1.0 — 2026-08-30

Initial MVP:
- FAST / STANDARD / DEEP adaptive task modes
- persistent Cursor rule
- eight engineering skills
- four specialist agents
- six slash commands
- complexity budget and simplification gate
- evidence-based verification contract
- zero-dependency structural validator
- local Cursor symlink installer
