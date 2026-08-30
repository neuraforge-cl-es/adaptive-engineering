# Installation

## Release downloads

Starting with `v0.4.0`, GitHub Releases publishes ready-to-download ZIP packages in addition to the source archives:

- `adaptive-engineering-cursor-vX.Y.Z.zip`
- `adaptive-engineering-agent-plugin-vX.Y.Z.zip`
- `adaptive-engineering-antigravity-vX.Y.Z.zip`
- `adaptive-engineering-opencode-vX.Y.Z.zip`
- `SHA256SUMS.txt`

Use `SHA256SUMS.txt` to verify downloaded packages before installing them. The release workflow checks that the Git tag matches the version declared in `core/spec.json`, rebuilds generated adapters from the tagged source, validates them, and only then uploads the assets.

## Cursor

Install globally for the current user:

```bash
./scripts/install-local.sh
```

Then run **Developer: Reload Window** from the Command Palette and open **Customize / Plugins** to confirm Adaptive Engineering is enabled.

The installer creates a physical copy under `~/.cursor/plugins/local/adaptive-engineering`. Run it again after changing or updating this repository; reloading Cursor alone does not refresh a physical copy.

Uninstall:

```bash
./scripts/uninstall-local.sh
```

For isolated testing, both scripts accept `ADAPTIVE_ENGINEERING_CURSOR_PLUGIN_ROOT` as an alternate plugin directory.

## Claude Code

Add this repository as a marketplace, then install the plugin:

```text
/plugin marketplace add https://github.com/neuraforge-cl-es/adaptive-engineering
/plugin install adaptive-engineering@neuraforge-plugins
```

Reload plugins if Claude Code requests it after installation.

## ChatGPT and Codex plugin surfaces

The repository contains a native skills-only manifest at `.codex-plugin/plugin.json`. Add the repository through a local or workspace plugin marketplace, then install `adaptive-engineering`.

For global standalone-skill discovery in Codex CLI or the IDE extension, copy the shared skills and their canonical references together:

```bash
mkdir -p ~/.agents/skills ~/.agents/core
cp -a skills/. ~/.agents/skills/
cp -a core/. ~/.agents/core/
```

Repository-local `AGENTS.md` remains available as a compact fallback.

## Gemini CLI

For local development:

```bash
gemini extensions link "$(pwd)"
```

After a tagged release, install from GitHub:

```bash
gemini extensions install https://github.com/neuraforge-cl-es/adaptive-engineering --ref v0.4.0
```

Restart the Gemini CLI session after installing or updating the extension.

## Google Antigravity

Build the generated plugin:

```bash
python3 scripts/build-antigravity.py
```

For a global Antigravity installation available to every project:

```bash
adaptive_plugin_target="$HOME/.gemini/config/plugins/adaptive-engineering"
mkdir -p "$adaptive_plugin_target"
cp -a dist/antigravity/adaptive-engineering/. "$adaptive_plugin_target/"
```

For a workspace-only installation, run this from the target workspace root:

```bash
adaptive_plugin_target=".agents/plugins/adaptive-engineering"
mkdir -p "$adaptive_plugin_target"
cp -a /path/to/adaptive-engineering/dist/antigravity/adaptive-engineering/. "$adaptive_plugin_target/"
```

For Antigravity CLI across all working directories:

```bash
adaptive_plugin_target="$HOME/.gemini/antigravity-cli/plugins/adaptive-engineering"
mkdir -p "$adaptive_plugin_target"
cp -a dist/antigravity/adaptive-engineering/. "$adaptive_plugin_target/"
```

Restart Antigravity or begin a new agent session after installing or updating the plugin. The package contains the nine shared skills, four specialist agents, a persistent adaptive-engineering rule, and the canonical core.

## Agent Plugins 1.0

Build the portable package:

```bash
python3 scripts/build-agent-plugin.py
```

Output:

```text
dist/agent-plugin/adaptive-engineering/
```

The generated package contains a root `plugin.json`, the nine skills, the canonical core, and the license. It is generated outside the repository root so native platform manifests cannot be discovered ambiguously.

## OpenCode

Build the adapter:

```bash
python3 scripts/build-opencode.py
```

For a project installation, copy the generated `.opencode` directory into the project and merge the portable `AGENTS.md` instructions with any existing project instructions.

For a global installation on Linux or macOS:

```bash
mkdir -p ~/.config/opencode/skills ~/.config/opencode/core
cp -a dist/opencode/.opencode/skills/. ~/.config/opencode/skills/
cp -a dist/opencode/.opencode/core/. ~/.config/opencode/core/
```

Merge `dist/opencode/.opencode/AGENTS.md` with an existing global `AGENTS.md` instead of overwriting user instructions. The adapter uses OpenCode's documented `skills/` discovery directory rather than a non-standard `skills` property in `opencode.json`.
