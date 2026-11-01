# STANDARD Workflow

Use STANDARD for moderate features, non-trivial bugs, local refactors, or work spanning one subsystem.

1. Inspect current behavior, conventions, architecture, and directly relevant project memory.
2. Reverify any persisted claims that influence planning or implementation.
3. State concise acceptance criteria and assumptions.
4. Declare a small complexity budget.
5. Create a short implementation plan.
6. For meaningful behavior, use the compact acceptance contract in [EXECUTION.md](../EXECUTION.md); where practical, reproduce a failing behavior test before the fix.
7. Implement in coherent increments and add or update meaningful behavior tests.
8. Run the simplification gate.
9. Verify the final state and report an evidence receipt with actual commands/results and anything not run.
10. Run the memory consistency gate and refresh only affected durable claims.

Default budget: one subsystem, no new dependency or service by default, and abstractions only for demonstrated duplication or a real boundary.

Escalate to DEEP when security, persistent data, public compatibility, infrastructure, distributed consistency, or difficult rollback emerges.
