# Adaptive Engineering — portable instructions

Use the least process necessary to produce the simplest correct, verified solution.

For every meaningful software task:
1. Classify it as FAST, STANDARD, or DEEP based on risk, scope, ambiguity, reversibility, and blast radius.
2. Inspect existing code and native capabilities before adding dependencies or abstractions.
3. Use a complexity budget as a tripwire, not a target.
4. Implement the smallest coherent solution.
5. Verify with executable evidence.
6. Run a simplification pass before completion.

FAST: local, low-risk, reversible change. Inspect -> reuse -> minimal change -> targeted verify -> simplify.

STANDARD: subsystem-level feature/bug/refactor. Inspect -> acceptance criteria -> short plan + budget -> implement/test -> simplify -> verify.

DEEP: security/auth, data migration, public contracts, CI/CD/production infrastructure, cross-service consistency, difficult rollback, or major architecture. Discover invariants -> requirements/failure modes -> trade-offs -> staged plan + rollback + budget -> implement/test -> independent review -> simplify -> end-to-end verify.

Never lower safety, security, data-integrity, compatibility, or production-critical checks just to fit a requested mode.
