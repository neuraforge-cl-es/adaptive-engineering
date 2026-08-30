# Adaptive Engineering Methodology

The canonical specification lives in:

- `core/PRINCIPLES.md`
- `core/METHODOLOGY.md`
- `core/workflows/fast.md`
- `core/workflows/standard.md`
- `core/workflows/deep.md`

## Operating model

Classify each meaningful task from risk, scope, ambiguity, reversibility, and blast radius. Choose FAST, STANDARD, or DEEP, but escalate whenever evidence exposes a higher-risk boundary.

Apply four gates in every mode:

1. **Necessity and reuse:** inspect existing behavior and native capabilities before creating structure.
2. **Complexity budget:** estimate the expected cost and stop when implementation materially exceeds it.
3. **Simplification:** remove avoidable code, dependencies, abstraction, configuration, and duplication.
4. **Verification:** provide executable evidence proportional to failure cost.

The modes differ in depth, not in their commitment to correctness. FAST removes ceremony; it does not remove safety.

`core/spec.json` records the versioned component contract used by validation and package builders.
