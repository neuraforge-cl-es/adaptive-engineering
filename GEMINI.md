# Adaptive Engineering

Use the least process necessary to produce the simplest correct, verified solution.

For every meaningful software task:

1. Classify it as FAST, STANDARD, or DEEP from risk, scope, ambiguity, reversibility, and blast radius.
2. Inspect existing behavior and native capabilities before adding dependencies or abstractions.
3. Follow the matching workflow under `core/workflows/`.
4. Treat the complexity budget as a tripwire rather than a target.
5. Implement the smallest coherent solution.
6. Run a simplification pass.
7. Report concrete verification evidence.

Never reduce security, safety, data integrity, compatibility, or production-critical verification to keep work in a lower mode. Use `core/PRINCIPLES.md` and `core/METHODOLOGY.md` as the canonical specification.
