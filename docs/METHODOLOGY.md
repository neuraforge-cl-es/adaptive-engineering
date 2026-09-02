# Adaptive Engineering Methodology

The canonical specification lives in:

- `core/PRINCIPLES.md`
- `core/METHODOLOGY.md`
- `core/MEMORY.md`
- `core/workflows/fast.md`
- `core/workflows/standard.md`
- `core/workflows/deep.md`

## Operating model

Classify each meaningful task from risk, scope, ambiguity, reversibility, and blast radius. Choose FAST, STANDARD, or DEEP, but escalate whenever evidence exposes a higher-risk boundary.

Apply five gates as applicable:

1. **Necessity and reuse:** inspect existing behavior and native capabilities before creating structure.
2. **Complexity budget:** estimate the expected cost and stop when implementation materially exceeds it.
3. **Evidence-grounded memory:** treat repository evidence as the source of truth, reverify persisted claims before reuse, and mark changed claims stale.
4. **Simplification:** remove avoidable code, dependencies, abstraction, configuration, and duplication.
5. **Verification:** provide executable evidence proportional to failure cost.

Persistent memory is optional. When useful, Adaptive Engineering stores durable project claims in `.adaptive/memory/claims.json` and keeps them tied to exact evidence and deterministic fingerprints. It must not require a database, vector store, MCP server, daemon, or external runtime service.

The modes differ in depth, not in their commitment to correctness. FAST removes ceremony; it does not remove safety or the requirement to distrust stale knowledge.

`core/spec.json` records the versioned component contract used by validation and package builders.
