---
name: systematic-debugging
description: Debug failures by reproducing, narrowing, forming evidence-based hypotheses, and verifying the root cause before applying the smallest durable fix.
---
# Systematic Debugging

## Workflow

1. Reproduce the failure or gather the strongest available evidence.
2. State observed behavior separately from assumptions.
3. Reduce the failing surface: input, boundary, component, environment, or commit.
4. Form one or a small number of falsifiable hypotheses.
5. Test the cheapest discriminating hypothesis first.
6. Identify the root cause, not merely a symptom.
7. Implement the smallest durable fix.
8. Add a regression test when it protects meaningful behavior.
9. Verify both the original failure path and nearby success paths.

## Avoid

- random edits followed by reruns
- broad refactors during diagnosis
- changing multiple suspected causes at once
- adding retries/timeouts without understanding the failure
- swallowing errors to make tests green
