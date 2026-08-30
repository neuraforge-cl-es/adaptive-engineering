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

## Testing

Prefer tests at the behavior boundary most likely to regress.

Do not:
- test private implementation details merely to raise coverage
- duplicate framework guarantees
- mock so aggressively that the real integration path is never exercised

For a bug, reproduce the failure before or alongside the fix whenever practical.
