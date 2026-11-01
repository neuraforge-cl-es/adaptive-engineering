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

Return the compact evidence receipt described in [EXECUTION.md](../../core/EXECUTION.md), scaled to the task:
- mode and PASS / FAIL / BLOCKED / PARTIAL outcome
- acceptance criterion and actual evidence
- precise command/check and observed result (or NOT RUN with reason)
- expected-versus-actual scope when relevant
- remaining blocker, rollback risk or unknown

For delegated work, independently examine returned artifacts rather than reporting a subordinate agent's assertion as proof. Do not claim measured savings, reliability or performance improvements without a real baseline and repeatable measurement.
