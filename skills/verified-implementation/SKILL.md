---
name: verified-implementation
description: Implement a planned change in small coherent increments, preserving repository conventions and verifying behavior as work progresses.
---
# Verified Implementation

## Execution rules

1. Make the smallest coherent change that satisfies the current acceptance criterion.
2. Preserve existing architecture and conventions unless the task explicitly requires changing them.
3. Avoid speculative extension points and generic abstractions.
4. Avoid new dependencies unless existing/native options are materially worse and the trade-off is stated.
5. Keep unrelated cleanup out of the diff unless it is necessary for correctness.
6. Verify each meaningful boundary before expanding the change.
7. If actual scope exceeds the complexity budget, stop and run the simplification gate.

## Evidence-driven delivery

For STANDARD or DEEP behavior changes, follow [the execution protocol](../../core/EXECUTION.md): state a compact acceptance contract, reproduce failure or the intended behavior with a targeted test where useful, and verify the changed path. For DEEP/cross-module work, reconcile the planned impact map with the final diff. Delegate only independent, bounded tasks; hand over exact context and constraints, then inspect their diffs and results. Do not accept self-reported success as verification or authorize external side effects implicitly.

## Testing

Prefer tests at the behavior boundary most likely to regress.

Do not:
- test private implementation details merely to raise coverage
- duplicate framework guarantees
- mock so aggressively that the real integration path is never exercised

For a bug, reproduce the failure before or alongside the fix whenever practical.
