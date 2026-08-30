---
name: code-review
description: Review a change for correctness, regressions, security, compatibility, operational risk, and unnecessary complexity, prioritizing actionable findings over style noise.
---
# Code Review

Review the diff in this order:

1. Correctness against intended behavior.
2. Data integrity, security, concurrency, and compatibility where applicable.
3. Error handling and failure semantics.
4. Test adequacy for material behavior.
5. Operational concerns: observability, configuration, deployment, rollback.
6. Complexity and consistency with existing code.

## Finding quality

Each finding should include:
- severity: critical/high/medium/low
- exact location or behavior
- why it can fail
- smallest reasonable correction

Do not generate style-only findings when formatting/linting already enforces them.
Do not invent hypothetical risks without a plausible execution path.
If there are no material findings, say so explicitly and note any verification gap.
