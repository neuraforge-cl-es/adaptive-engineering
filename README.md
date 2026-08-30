# Adaptive Engineering

A Cursor plugin that makes software-engineering process **adaptive** instead of uniformly heavy or uniformly impulsive.

> Use the least process necessary to produce the simplest correct, verified solution.

**Status:** MVP `0.1.2`

## Why

Coding agents commonly fail in opposite directions:

- **Under-process:** they start editing before understanding constraints and failure modes.
- **Over-process:** they add ceremony, abstractions, dependencies, and architecture to changes that should have stayed small.

Adaptive Engineering chooses one of three modes per task:

| Mode | Use for | Workflow |
|---|---|---|
| **FAST** | local, low-risk, reversible work | inspect -> reuse -> minimal change -> verify -> simplify |
| **STANDARD** | subsystem features, bugs, refactors | inspect -> criteria -> short plan + budget -> implement/test -> simplify -> verify |
| **DEEP** | security, data, public contracts, CI/CD, infra, distributed or high-risk changes | constraints -> failure modes -> trade-offs -> staged plan -> implement/test -> review -> simplify -> E2E verify |

A small code diff can still be DEEP when the failure cost is high.

## Included in the MVP

### Persistent rule

`rules/adaptive-engineering.mdc`

Always-on guidance for:
- automatic task triage
- necessity/reuse gate
- complexity budgets
- FAST / STANDARD / DEEP workflows
- simplification gate
- evidence-based verification

### Skills

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

The agent should normally choose the mode itself. Commands are explicit overrides/tools, not a required workflow.

## Local installation in Cursor

Cursor currently supports local plugin development under `~/.cursor/plugins/local/`.

From this repository:

```bash
./scripts/install-local.sh
```

Then in Cursor:

1. Run **Developer: Reload Window** (or restart Cursor).
2. Open **Customize**.
3. Confirm **Adaptive Engineering** and its rules/skills are present.

The installer uses a physical copy, so edits in this repository are picked up after reloading Cursor.

Manual equivalent:

```bash
mkdir -p ~/.cursor/plugins/local
ln -s "$(pwd)" ~/.cursor/plugins/local/adaptive-engineering
```

Uninstall:

```bash
./scripts/uninstall-local.sh
```

## Validate the plugin

No third-party packages are required:

```bash
python3 scripts/validate.py
```

The validator checks the manifest, paths, component frontmatter, names, and expected skill layout.

## Try it

### Automatic triage

Ask Cursor:

```text
Add a boolean field to this internal response and update its test.
```

Expected behavior: FAST, no architecture ceremony, no new dependency/abstraction, targeted verification.

Then try:

```text
Split this production database column without downtime.
```

Expected behavior: DEEP, including compatibility, staged migration, rollback, and data verification concerns.

See `docs/TEST-SCENARIOS.md` for more behavioral evaluations.

## Design choices in 0.1.2

- **No MCP server.** The methodology does not need network or external-tool complexity.
- **No hooks yet.** The persistent rule and skills are sufficient to validate the core behavior first.
- **No mandatory subagents.** Subagents are useful when work can genuinely be separated; they are overhead for small tasks.
- **No external runtime dependencies.** Even the validator uses Python's standard library.

These omissions are deliberate: the plugin should obey its own simplicity rules.

## Portability

`AGENTS.md` contains a compact instruction-only version for agents that understand that convention. The Cursor plugin remains the primary MVP because Cursor-specific rules, agents, and commands provide the full experience.

## Methodology

See `docs/METHODOLOGY.md`.

## Inspiration and attribution

Adaptive Engineering is an original implementation inspired by the broader ideas of disciplined agent workflows and simplicity-first engineering. The MVP does not copy source code from Superpowers or Ponytail.

If future versions directly incorporate or modify MIT-licensed material from either project, their required copyright and license notices must be preserved.

## License

MIT. See `LICENSE`.
