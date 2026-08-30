# Adaptive Engineering

Adaptive software-engineering workflows for AI coding agents.

> Use the least process necessary to produce the simplest correct, verified solution.

**Status:** `0.2.0`

Adaptive Engineering selects one of three modes for each task:

| Mode | Use for | Workflow |
|---|---|---|
| **FAST** | local, low-risk, reversible work | inspect → reuse → minimal change → verify → simplify |
| **STANDARD** | subsystem features, bugs, refactors | inspect → criteria → budget → implement/test → simplify → verify |
| **DEEP** | security, data, public contracts, CI/CD, infrastructure, distributed or high-risk changes | constraints → failures → trade-offs → staged plan → implement/test → review → simplify → E2E verify |

A small diff can still be DEEP when its failure cost is high.

## Platform support

| Platform | Integration | Status |
|---|---|---|
| Cursor | `.cursor-plugin/plugin.json`, rules, skills, agents, Markdown commands | Native |
| Claude Code | plugin and marketplace manifests | Native |
| ChatGPT / Codex | `.codex-plugin/plugin.json` and portable skills | Native |
| Gemini CLI | extension manifest, context, skills, agents, TOML commands | Native |
| Agent Plugins 1.0 | generated portable package | Build target |
| OpenCode | generated `.opencode/skills` adapter | Build target |

See [installation instructions](docs/INSTALLATION.md) and the [platform matrix](docs/PLATFORMS.md).

## Architecture

`core/` is the canonical, host-agnostic methodology:

- `core/PRINCIPLES.md`
- `core/METHODOLOGY.md`
- `core/workflows/{fast,standard,deep}.md`
- `core/spec.json`

Native manifests and host-specific command formats are thin adapters around that core. The shared `skills/` directory contains one portable entry skill and eight focused engineering skills.

## Included components

### Skills

- `adaptive-engineering`
- `task-triage`
- `existing-system-scan`
- `minimal-planning`
- `verified-implementation`
- `systematic-debugging`
- `simplification-gate`
- `verification`
- `code-review`

### Agents

- `adaptive-architect`
- `adaptive-builder`
- `adaptive-reviewer`
- `adaptive-simplifier`

### Commands

- `/fast`
- `/standard`
- `/deep`
- `/triage`
- `/simplify`
- `/review`

The agent should normally choose the mode automatically. Commands are explicit overrides and tools, not required ceremony.

## Validate

Python 3.11 or newer is required. No third-party packages are used.

```bash
python3 scripts/validate.py
python3 scripts/build-agent-plugin.py
python3 scripts/build-opencode.py
python3 scripts/validate.py --dist
```

## Design constraints

- No MCP server: the methodology does not need network tools.
- No hooks yet: native instructions and skills establish the behavior with less operational risk.
- No mandatory subagents: delegation should be used only when work separates cleanly.
- No external runtime dependencies.
- Cursor `0.1.2` installation paths remain compatible.

## Methodology

Read [the methodology overview](docs/METHODOLOGY.md) and [behavioral test scenarios](docs/TEST-SCENARIOS.md).

## License

MIT. See `LICENSE`.
