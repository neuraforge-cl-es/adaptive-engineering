---
name: simplification-gate
description: Review an implementation or diff for avoidable complexity, unnecessary code, dependencies, abstractions, configuration, and duplication before completion.
---
# Simplification Gate

Treat complexity as a cost that requires evidence.

## Review sequence

1. Compare actual scope with the declared complexity budget.
2. Look for code that can be deleted without changing required behavior.
3. Look for new code that duplicates repository capabilities.
4. Challenge each new dependency, abstraction, interface, service, config key, and persistent field.
5. Replace clever/general solutions with boring/specific ones when the latter satisfy current requirements.
6. Ensure simplification does not hide real domain boundaries or compromise correctness.

## Findings

Classify findings:
- `REMOVE`: no value for current requirements
- `REUSE`: existing capability should replace it
- `COLLAPSE`: abstraction is premature
- `KEEP`: complexity is justified by a concrete boundary or requirement

Apply safe simplifications directly when operating in implementation mode. Otherwise report them with the expected impact.
