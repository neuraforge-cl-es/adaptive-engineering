# STANDARD Workflow

Use STANDARD for moderate features, non-trivial bugs, local refactors, or work spanning one subsystem.

1. Inspect current behavior, conventions, and architecture.
2. State concise acceptance criteria and assumptions.
3. Declare a small complexity budget.
4. Create a short implementation plan.
5. Implement in coherent increments.
6. Add or update meaningful behavior tests.
7. Run the simplification gate.
8. Verify the final state.

Default budget: one subsystem, no new dependency or service by default, and abstractions only for demonstrated duplication or a real boundary.

Escalate to DEEP when security, persistent data, public compatibility, infrastructure, distributed consistency, or difficult rollback emerges.
