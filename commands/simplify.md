---
name: simplify
description: Run the simplification gate against the current diff and remove or flag unjustified complexity.
---
# Simplify Current Diff

Run the simplification-gate skill against the current changes.

Prefer direct edits when safe. Otherwise return findings categorized as REMOVE, REUSE, COLLAPSE, or KEEP.
Preserve required behavior and meaningful domain boundaries.
