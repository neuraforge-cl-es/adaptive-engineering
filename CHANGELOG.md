# Changelog

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
