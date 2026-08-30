---
name: verification
description: Establish concrete evidence that a change works by selecting and running the strongest practical tests, checks, builds, or integration validations for the task.
---
# Verification

## Select evidence by risk

Possible evidence includes:
- focused unit/behavior tests
- integration tests
- full relevant test suite
- type checker
- linter/static analysis
- build/package step
- reproducible CLI/API request
- migration dry run
- rollback test
- deployment/configuration validation

## Verification rules

1. Prefer executable evidence over visual confidence.
2. Verify the changed behavior and at least one important adjacent path when risk warrants it.
3. Do not report commands as passing unless they were actually run and passed.
4. Separate pre-existing failures from failures caused by the change.
5. If verification is blocked, identify the exact blocker and residual risk.

## Completion evidence

Return:
- command/check
- result
- relevant failure/blocker, if any
