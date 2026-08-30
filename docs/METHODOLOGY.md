# Adaptive Engineering Methodology

## Thesis

Two failure modes are common in coding agents:

1. **Under-process:** implementation begins before the system and failure modes are understood.
2. **Over-process:** trivial work receives architecture ceremonies, abstractions, and dependencies that cost more than the change.

Adaptive Engineering treats engineering process as a risk-control mechanism whose depth should scale with the task.

> Use the least process necessary to produce the simplest correct, verified solution.

## Decision model

The mode is chosen from five dimensions:

| Dimension | Low | High |
|---|---|---|
| Risk | cosmetic/local | security/data/production |
| Scope | one local behavior | multi-module/service |
| Ambiguity | known cause/design | unclear architecture/requirements |
| Reversibility | easy revert | migration/external contract |
| Blast radius | isolated | shared/public/operational |

A single high-consequence signal can justify DEEP even when code size is small.

## Modes

### FAST
Goal: minimum latency and minimum diff.

No ceremony unless evidence requires it.

### STANDARD
Goal: enough planning and testing to control subsystem-level risk without turning the task into an architecture project.

### DEEP
Goal: make hidden constraints, failure modes, compatibility, rollout, and rollback explicit before high-cost mistakes are committed.

## Complexity budget

The budget makes expected complexity visible before implementation. It is intentionally approximate.

Useful dimensions:
- files/modules/services
- new dependencies
- public APIs
- persistent state
- abstractions
- configuration

If actual complexity substantially exceeds expectation, the correct response is not to normalize the new complexity. Re-check assumptions, reuse, and design first.

## Simplification gate

The gate asks whether every added concept is required by current behavior or a real boundary. It does **not** optimize for fewest lines. A clear domain type or security boundary may add lines while reducing total system complexity.

## Verification contract

"Done" means there is evidence. Evidence strength scales with risk. A FAST copy edit may need a targeted check; a DEEP migration may require dry-run, integration tests, compatibility validation, and rollback evidence.
