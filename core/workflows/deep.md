# DEEP Workflow

Use DEEP when failure cost or ambiguity is high, or the task changes security, data, architecture, public contracts, CI/CD, networking, deployment, or distributed behavior.

1. Discover constraints, invariants, current architecture, and relevant persisted project claims.
2. Reverify every memory claim that influences the plan; search for contradictions across code, configuration, tests, schemas, and documentation.
3. Define requirements, failure modes, and rollback expectations.
4. Compare viable approaches and select the least complex one that satisfies the constraints.
5. Declare a task-specific complexity budget and rollback strategy.
6. Produce a staged implementation and verification plan; define the impact map, acceptance contract and authorized side effects in [EXECUTION.md](../EXECUTION.md).
7. Implement with evidence at each meaningful boundary; delegate only independent work with bounded context and inspect returned artifacts.
8. Review correctness, security, data, compatibility, and operability as applicable.
9. Run the simplification gate.
10. Reconcile actual impact with the planned map, protect the quality bar, perform end-to-end verification, and return an evidence receipt with known gaps.
11. Run a scoped memory drift check and refresh or mark stale every affected durable claim.

Do not impose an arbitrary file limit. Justify each new dependency, service, persistent state change, configuration surface, and public interface.
