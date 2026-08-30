# Platform Matrix

| Capability | Cursor | Claude Code | ChatGPT / Codex plugin | Gemini CLI | Agent Plugins 1.0 | OpenCode |
|---|---:|---:|---:|---:|---:|---:|
| Canonical methodology | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Portable skills | 9 | 9 | 9 | 9 | 9 | 9 |
| Persistent instructions | Rule | Plugin context | Skill / `AGENTS.md` | `GEMINI.md` | Skill | `AGENTS.md` |
| Specialist agents | 4 | 4 | — | 4 preview | — | — |
| Explicit commands | 6 Markdown | 6 Markdown | — | 6 TOML | — | — |
| Native manifest | `.cursor-plugin` | `.claude-plugin` | `.codex-plugin` | `gemini-extension.json` | root `plugin.json` | discovery layout |
| Packaging | repository root | repository root | repository root | repository root | generated | generated |

## Portability boundary

The portable contract consists of the canonical `core/` and `skills/`. Rules, agents, commands, and context files adapt that contract to native host capabilities.

Agent Plugins and OpenCode packages are generated under `dist/`; generated output is not committed. This keeps the repository root compatible with native manifests and makes drift detectable through the validator.

## Deliberate exclusions

- No MCP server.
- No hooks.
- No automatic permission changes.
- No host-specific tool execution.

These remain future options only if behavioral evaluations show that instructions and skills are insufficient.
