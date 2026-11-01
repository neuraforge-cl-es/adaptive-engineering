# Adaptive Engineering

Use the least process necessary to produce the simplest correct, verified solution.

For every meaningful software task:

1. Classify it as FAST, STANDARD, or DEEP from risk, scope, ambiguity, reversibility, and blast radius.
2. Inspect existing behavior and native capabilities before adding dependencies or abstractions.
3. Follow the matching workflow under `core/workflows/`.
4. If `.adaptive/memory/claims.json` exists, treat it as re-verifiable context only. Repository evidence is the source of truth; changed evidence makes claims stale until reverified.
5. Treat the complexity budget as a tripwire rather than a target.
6. Implement the smallest coherent solution.
7. Run a simplification pass.
8. Run the memory consistency gate when memory exists or durable project knowledge changed.
9. Report concrete verification evidence.

Do not require a database, vector store, daemon, MCP server, or external service for Adaptive Engineering memory. Plain repository-local files must remain sufficient.

Never reduce security, safety, data integrity, compatibility, or production-critical verification to keep work in a lower mode. Use `core/PRINCIPLES.md`, `core/METHODOLOGY.md`, and `core/MEMORY.md` as the canonical specification.
