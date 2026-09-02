# Behavioral Test Scenarios

Use these prompts to evaluate whether the plugin selects the right amount of process.

## Expected FAST

### Scenario F1 — rename
`Rename the JSON field display_name to displayName in this private response object and update its test.`

Expected:
- FAST
- no design document
- no new abstraction/dependency
- targeted test

### Scenario F2 — local bug
`This formatter produces an extra comma for an empty list. Fix it.`

Expected:
- reproduce or inspect failing case
- smallest fix
- regression test if meaningful

## Expected STANDARD

### Scenario S1 — cache existing endpoint
`Cache the customer summary endpoint for 60 seconds using capabilities already present in the repo.`

Expected:
- inspect existing cache conventions/dependencies
- acceptance criteria
- short plan
- no new cache library if existing capability suffices
- behavior verification

### Scenario S2 — refactor
`Extract duplicated invoice validation used by these three handlers.`

Expected:
- STANDARD unless risk signals appear
- preserve behavior
- abstraction justified by real duplication
- tests remain behavior-focused

### Scenario S3 — stale project memory
`The project memory says authentication is handled by AuthMiddleware, but auth.go changed after that claim was recorded. Add a new authenticated endpoint.`

Expected:
- inspect `.adaptive/memory/claims.json` if present
- compare the stored evidence fingerprint with current repository evidence
- treat the authentication claim as stale when the fingerprint changed
- inspect current authentication code before planning or implementation
- refresh only the affected durable claim after verification
- never trust the old claim merely because it exists in memory

## Expected DEEP

### Scenario D1 — auth
`Allow service accounts to call the admin endpoint using a new credential type.`

Expected:
- DEEP regardless of small file count
- threat/security boundary analysis
- compatibility/failure semantics
- staged verification
- reverify any persisted security or authentication claims before use

### Scenario D2 — database
`Split full_name into first_name and last_name in production without downtime.`

Expected:
- DEEP
- migration/compatibility/rollback strategy
- staged rollout
- data verification

### Scenario D3 — CI/CD
`Deploy public API and private API independently from the same binary based on changed paths.`

Expected:
- DEEP
- current pipeline/release discovery
- failure and rollback analysis
- deployment verification

### Scenario D4 — architecture drift
`Change the production system from direct PostgreSQL access to a new persistence boundary. Existing project memory contains architecture and infrastructure claims.`

Expected:
- enumerate relevant architecture/infrastructure claims
- reverify their evidence before relying on them
- search code, configuration, tests, and deployment definitions for contradictions
- implement with normal DEEP safeguards
- run a scoped memory drift check after implementation
- mark invalidated claims stale or replace them only after verification

## Anti-overengineering evaluation

Prompt:
`Add a boolean field to an internal struct and return it in one existing endpoint.`

Fail the evaluation if the agent proposes:
- a new service
- a new dependency
- a repository-wide architecture document
- a generic field-mapping framework
- a multi-agent workflow without evidence it is needed
- a database, vector store, daemon, MCP server, or external service merely to support memory
