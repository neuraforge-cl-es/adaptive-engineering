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

## Expected DEEP

### Scenario D1 — auth
`Allow service accounts to call the admin endpoint using a new credential type.`

Expected:
- DEEP regardless of small file count
- threat/security boundary analysis
- compatibility/failure semantics
- staged verification

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

## Anti-overengineering evaluation

Prompt:
`Add a boolean field to an internal struct and return it in one existing endpoint.`

Fail the evaluation if the agent proposes:
- a new service
- a new dependency
- a repository-wide architecture document
- a generic field-mapping framework
- a multi-agent workflow without evidence it is needed
