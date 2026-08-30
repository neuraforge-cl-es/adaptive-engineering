# DEEP Workflow

Use DEEP when failure cost or ambiguity is high, or the task changes security, data, architecture, public contracts, CI/CD, networking, deployment, or distributed behavior.

1. Discover constraints, invariants, and current architecture.
2. Define requirements, failure modes, and rollback expectations.
3. Compare viable approaches and select the least complex one that satisfies the constraints.
4. Declare a task-specific complexity budget and rollback strategy.
5. Produce a staged implementation and verification plan.
6. Implement with evidence at each meaningful boundary.
7. Review correctness, security, data, compatibility, and operability as applicable.
8. Run the simplification gate.
9. Perform final end-to-end verification.

Do not impose an arbitrary file limit. Justify each new dependency, service, persistent state change, configuration surface, and public interface.
