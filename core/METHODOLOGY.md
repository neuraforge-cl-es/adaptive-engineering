# Adaptive Engineering Methodology

## Thesis

Coding agents commonly fail in opposite directions:

1. **Under-process:** implementation begins before constraints and failure modes are understood.
2. **Over-process:** small changes accumulate ceremony, dependencies, abstractions, and architecture that cost more than the behavior they add.

Treat engineering process as a risk-control mechanism. Scale its depth to the task, then ship the simplest verified solution.

## Decision model

Classify work from five dimensions:

| Dimension | Low signal | High signal |
|---|---|---|
| Risk | cosmetic or local | security, data, production |
| Scope | one behavior | multiple modules or services |
| Ambiguity | known cause and design | unclear requirements or architecture |
| Reversibility | easy revert | migration or external contract |
| Blast radius | isolated | shared, public, or operational |

A single high-consequence signal can justify DEEP even when the code diff is small.

## Modes

- **FAST:** local, low-risk, obvious, reversible work.
- **STANDARD:** subsystem-level features, non-trivial bugs, and coherent refactors.
- **DEEP:** security, data, public contracts, infrastructure, distributed behavior, difficult rollback, or major ambiguity.

Use the detailed workflows in `core/workflows/` after selecting a mode.

## Necessity and reuse gate

Before creating something new, ask:

1. Can the outcome be achieved without code?
2. Does the repository already contain the behavior or a suitable extension point?
3. Can the current runtime, framework, or standard library provide it directly?
4. Can an already-installed dependency provide it safely?
5. Can an existing file, type, or function be extended coherently?

Create a new abstraction, dependency, service, or subsystem only after those options are exhausted. Do not force reuse when it would couple unrelated domains or weaken a real boundary.

## Complexity budget

Estimate only dimensions relevant to the task:

- files, modules, and services touched
- dependencies
- abstractions, interfaces, or public APIs
- persistent state or schema
- configuration and operational surface

Treat the budget as a tripwire, not a target. If implementation materially exceeds it, stop and simplify or revisit assumptions before adding more structure.

## Simplification gate

Before completion, inspect the final change and ask:

- What can be deleted?
- What can be collapsed into existing code?
- Is any new dependency avoidable?
- Is a generic abstraction serving only one concrete case?
- Can configuration be derived or defaulted?
- Did the change duplicate validation, transformation, or error handling?
- Is a boring implementation easier to operate than a clever one?

Preserve justified domain and security boundaries. Simplicity means low total complexity, not minimum line count.

## Verification contract

Do not claim completion because code looks plausible. Produce executable evidence proportional to risk: targeted tests, broader suites, type checking, linting, builds, integration checks, dry runs, rollback validation, or end-to-end verification.

State exactly what was run, what passed, and what remains unverified.
