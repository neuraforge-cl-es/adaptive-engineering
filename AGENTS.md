# Adaptive Engineering — portable instructions

Use the least process necessary to produce the simplest correct, verified solution.

For every meaningful software task:
1. Classify it as FAST, STANDARD, or DEEP based on risk, scope, ambiguity, reversibility, and blast radius.
2. Inspect existing code and native capabilities before adding dependencies or abstractions.
3. If `.adaptive/memory/claims.json` exists, treat it as re-verifiable context only: repository evidence is the source of truth, changed evidence makes claims stale, and stale claims must be reverified before reuse.
4. Use a complexity budget as a tripwire, not a target.
5. Implement the smallest coherent solution.
6. Verify with executable evidence.
7. Run a simplification pass before completion.
8. When memory exists or durable knowledge changed, run the memory consistency gate and refresh only affected claims.

FAST: local, low-risk, reversible change. Inspect -> relevant memory check -> reuse -> minimal change -> targeted verify -> simplify.

STANDARD: subsystem-level feature/bug/refactor. Inspect -> reverify relevant claims -> acceptance criteria -> short plan + budget -> implement/test -> simplify -> verify -> memory consistency.

DEEP: security/auth, data migration, public contracts, CI/CD/production infrastructure, cross-service consistency, difficult rollback, or major architecture. Discover invariants + relevant claims -> reverify and search for contradictions -> requirements/failure modes -> trade-offs -> staged plan + rollback + budget -> implement/test -> independent review -> simplify -> end-to-end verify -> drift check.

Never add a database, vector store, daemon, MCP server, or external service merely to support Adaptive Engineering memory. Plain repository-local files must remain sufficient.

Never lower safety, security, data-integrity, compatibility, or production-critical checks just to fit a requested mode.
