---
name: memory-grounding
description: Ground durable project knowledge in exact repository evidence, detect stale claims when evidence changes, and reverify memory before it influences engineering decisions.
---
# Memory Grounding

Use repository evidence as the source of truth. Memory is only a compact, re-verifiable index over that evidence.

Read [MEMORY.md](../../core/MEMORY.md) before using persistent project memory.

## Workflow

1. Discover only claims relevant to the current task.
2. Check that each claim's evidence still exists.
3. Compare stored fingerprints with current evidence when possible.
4. Treat changed or contradicted claims as `stale`.
5. Inspect the source of truth before relying on stale or unverified knowledge.
6. Persist only durable, reusable knowledge with precise evidence.
7. After implementation, refresh only affected claims.
8. Run the memory consistency gate before completion.

## Mode behavior

- FAST: verify directly relevant memory; avoid writing routine transient knowledge.
- STANDARD: reverify planning claims and refresh affected durable knowledge.
- DEEP: enumerate relevant claims and invariants, search for contradictions, and run a scoped drift check after implementation.

Never add a database, vector store, daemon, MCP server, or external service just to enable this skill. Plain repository-local files must remain sufficient.