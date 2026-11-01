---
name: existing-system-scan
description: Inspect the repository for existing behavior, conventions, native capabilities, and installed dependencies before creating new code or abstractions.
---
# Existing System Scan

Search before inventing.

## Scan order

1. Find the closest existing implementation by behavior, not merely by filename.
2. Identify conventions for errors, validation, logging, configuration, persistence, tests, and dependency injection.
3. Check framework/runtime/standard-library support.
4. Check already-installed dependencies and whether they are already used for the same concern.
5. Identify extension points that remain coherent if reused.
6. Record invariants that must not change.

## Reject false reuse

Do not reuse code just because it exists. Reject reuse when it:
- couples unrelated domains
- weakens type or security boundaries
- creates hidden behavior
- would make the existing abstraction less coherent

## Output

Return only evidence that affects the implementation decision:
- reusable code/capability
- relevant convention
- invariant
- gap that truly requires new code
