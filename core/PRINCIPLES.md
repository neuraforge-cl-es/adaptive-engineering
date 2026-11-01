# Adaptive Engineering Principles

Use the least process necessary to produce the simplest correct, verified solution.

1. Understand before changing.
2. Reuse before creating.
3. Prefer deletion or modification over addition when behavior remains correct.
4. Prefer standard-library, framework-native, and already-installed capabilities before new dependencies.
5. Match process depth to risk, scope, ambiguity, reversibility, and blast radius.
6. Test behavior that matters instead of mirroring implementation details.
7. Require concrete verification evidence before declaring completion.
8. Make every added concept justify its ongoing complexity cost.
9. Treat repository evidence as the source of truth; persisted memory must be re-verifiable and must become stale when its evidence changes.
10. Persist only durable project knowledge that is likely to be reused and whose verification value justifies the state it adds.

Never reduce security, safety, data integrity, compatibility, or production-critical verification merely to keep a task in a lower process mode.
