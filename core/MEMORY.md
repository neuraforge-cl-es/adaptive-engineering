# Evidence-Grounded Self-Correcting Memory

Adaptive Engineering may persist stable project knowledge, but memory is never the source of truth. Repository evidence is the source of truth; memory is a compact, re-verifiable index over that evidence.

## Core rules

1. **Evidence over memory.** Do not trust a remembered claim when current repository evidence disagrees with it.
2. **Reverify before reuse.** A claim that influences a decision must still be grounded in current evidence.
3. **Stale, do not silently overwrite.** When evidence changes, mark the claim `stale` or replace it only after re-verification.
4. **Scope memory to durable knowledge.** Do not persist transient task state, guesses, or information that is cheap to rediscover.
5. **No infrastructure requirement.** Memory must work as repository-local files. Do not require a database, vector store, daemon, MCP server, or external service.

## Project-local storage

When persistent memory is useful, use this conventional location in the project being worked on:

```text
.adaptive/
└── memory/
    └── claims.json
```

Do not create `.adaptive/memory/` merely because Adaptive Engineering is installed. Create it only when durable project knowledge is likely to be reused and the future verification benefit justifies the persistent state.

`claims.json` is intentionally plain JSON so every supported host can read and update it without additional dependencies.

## Claim model

A claim records a statement plus the evidence required to verify it again.

```json
{
  "schema_version": 1,
  "claims": [
    {
      "id": "architecture.auth",
      "type": "architecture",
      "statement": "Authentication is enforced by AuthMiddleware.",
      "status": "trusted",
      "evidence": [
        {
          "path": "internal/middleware/auth.go",
          "selector": "AuthMiddleware",
          "fingerprint": "git-blob:<sha>"
        }
      ],
      "verified_at": "2026-09-02T00:00:00Z"
    }
  ]
}
```

Recommended claim types:

- `architecture`
- `dependency`
- `convention`
- `constraint`
- `decision`
- `api-contract`
- `database`
- `infrastructure`
- `security`
- `workflow`

Recommended statuses:

- `trusted` — evidence was verified and still matches.
- `stale` — one or more evidence fingerprints changed or the claim is contradicted.
- `unverified` — recorded knowledge exists but has not yet been grounded strongly enough to trust.
- `superseded` — a newer verified claim intentionally replaces it.

## Evidence and fingerprints

Prefer exact repository evidence: source files, configuration, schemas, tests, migration files, infrastructure definitions, API specifications, or committed design records.

For repository files, prefer a whole-file Git blob fingerprint because it is deterministic and requires no runtime dependency:

```bash
git hash-object path/to/file
```

Store the result as `git-blob:<sha>`. If the current hash differs, treat every claim grounded in that file as potentially stale until the relevant evidence is re-checked.

Whole-file fingerprints are intentionally conservative: an unrelated edit may invalidate a claim. Prefer a false-positive re-verification over silently trusting stale architectural knowledge.

When Git is unavailable, inspect the evidence directly and keep the claim `unverified` unless another deterministic fingerprint is available.

## Read path

Before using a persisted claim:

1. Determine whether the claim is relevant to the current task.
2. Check the evidence path still exists.
3. Compare its stored fingerprint with the current evidence when possible.
4. If unchanged, the claim may remain `trusted`.
5. If changed or contradicted, mark it `stale` and inspect the source of truth before relying on it.
6. If the claim cannot be verified and it materially affects the task, inspect the source directly instead of guessing.

Do not let memory substitute for repository inspection on a high-consequence boundary.

## Write path

Persist or update a claim only when all of these are true:

- it is likely to matter again;
- it describes stable project knowledge rather than temporary work state;
- its evidence can be named precisely;
- the statement is narrower than the evidence supports;
- the verification cost is proportionate to its future value.

After a change, update memory only for claims affected by the change. Do not rewrite unrelated claims.

## Memory consistency gate

Before completion, ask:

- Did this change invalidate any trusted claim?
- Did architecture, interfaces, dependencies, configuration, infrastructure, data models, security assumptions, or project conventions change?
- Are any claims still marked `trusted` even though their evidence changed?
- Did this task establish durable knowledge worth recording?
- Are all new or refreshed claims grounded in exact evidence?

If evidence changed, a previously trusted claim must not remain trusted without re-verification.

## Mode-specific depth

- **FAST:** consult only directly relevant existing claims. Verify fingerprints before relying on them. Do not create memory for routine local work unless the change establishes durable knowledge.
- **STANDARD:** reverify claims used for planning or implementation and refresh affected claims at completion.
- **DEEP:** enumerate relevant claims and invariants, reverify all memory that influences the plan, search for contradictions across code/config/docs/tests, and run a scoped drift check after implementation.

Memory depth adapts with engineering depth; correctness rules do not.