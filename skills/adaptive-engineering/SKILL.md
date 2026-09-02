---
name: adaptive-engineering
description: Select and execute the least process necessary for a software-engineering task using FAST, STANDARD, or DEEP mode, with explicit reuse, complexity, evidence-grounded memory, simplification, and verification gates. Use for implementation, debugging, refactoring, code review, architecture, CI/CD, infrastructure, security, data, and public-contract work when process depth should scale with risk.
---
# Adaptive Engineering

Use the least process necessary to produce the simplest correct, verified solution.

1. Read [PRINCIPLES.md](../../core/PRINCIPLES.md).
2. Classify the task using [METHODOLOGY.md](../../core/METHODOLOGY.md).
3. Load exactly one workflow:
   - [FAST](../../core/workflows/fast.md)
   - [STANDARD](../../core/workflows/standard.md)
   - [DEEP](../../core/workflows/deep.md)
4. If project-local Adaptive Engineering memory exists or durable project knowledge is material to the task, use [MEMORY.md](../../core/MEMORY.md) and the `memory-grounding` skill.
5. Inspect existing behavior and native capabilities before creating code, dependencies, or abstractions.
6. Declare a complexity budget for STANDARD and DEEP work.
7. Implement the smallest coherent solution.
8. Run the simplification gate.
9. Run the memory consistency gate when applicable.
10. Verify with executable evidence proportional to risk.

Escalate process depth when evidence exposes a higher-risk boundary. Never lower safety, security, data-integrity, compatibility, or production-critical checks to preserve a requested mode.
