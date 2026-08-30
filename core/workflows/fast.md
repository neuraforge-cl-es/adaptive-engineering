# FAST Workflow

Use FAST when the change is local, low-risk, obvious, reversible, and has no security, data, public-contract, or production boundary.

1. Inspect only the context required to act safely.
2. Check for an existing or native solution.
3. Make the smallest coherent change.
4. Run targeted verification.
5. Simplify the resulting diff.

Default budget: at most a few files, zero dependencies, zero services, and ideally zero new abstractions.

Escalate to STANDARD or DEEP when evidence exposes a larger boundary or failure cost.
