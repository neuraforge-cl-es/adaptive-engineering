# FAST Workflow

Use FAST when the change is local, low-risk, obvious, reversible, and has no security, data, public-contract, or production boundary.

1. Inspect only the context required to act safely.
2. If relevant project memory exists, verify the directly relevant claim evidence before relying on it.
3. Check for an existing or native solution.
4. Make the smallest coherent change.
5. Run targeted verification.
6. Simplify the resulting diff.
7. If the change affects a persisted claim, mark it stale or refresh it from current evidence.

Default budget: at most a few files, zero dependencies, zero services, and ideally zero new abstractions.

Do not create persistent memory for routine local work unless the task establishes durable knowledge likely to be reused.

Escalate to STANDARD or DEEP when evidence exposes a larger boundary or failure cost.
