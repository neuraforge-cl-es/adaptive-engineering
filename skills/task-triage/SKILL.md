---
name: task-triage
description: Classify a software task as FAST, STANDARD, or DEEP based on risk, scope, ambiguity, reversibility, and blast radius. Use before non-trivial implementation or when choosing process depth.
---
# Task Triage

Classify the task before choosing the workflow.

## Inputs

Inspect enough repository context to answer:

- What behavior is changing?
- How many modules/services/contracts are involved?
- What breaks if the change is wrong?
- Is the change easy to roll back?
- Are security, data integrity, public compatibility, concurrency, production infrastructure, or deployment involved?
- Is the current architecture sufficiently understood?

## Decision

Choose exactly one initial mode:

### FAST
All or nearly all are true:
- local scope
- low failure cost
- low ambiguity
- reversible
- no security/data/public-contract/production boundary
- expected implementation is small

### STANDARD
Any are true:
- multiple coherent files in one subsystem
- new behavior needs acceptance criteria
- bug cause needs investigation
- meaningful tests must be added or changed
- refactor has moderate blast radius

### DEEP
Any strong-risk signal is present:
- auth/security boundary
- destructive/persistent data migration
- public API/protocol compatibility
- CI/CD, networking, release, or production infrastructure
- multiple services or distributed consistency
- difficult rollback
- architectural ambiguity with large blast radius

## Output

Keep the triage concise:

- `Mode: FAST|STANDARD|DEEP`
- `Why:` one sentence
- `Key risks:` only material risks
- `Expected budget:` files/dependencies/services/abstractions as relevant

Do not turn triage into a design document.
