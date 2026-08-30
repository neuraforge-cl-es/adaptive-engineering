# Security Policy

## Supported versions

Security fixes are provided for the latest released version of Adaptive Engineering and the current `main` branch.

## Reporting a vulnerability

Do not open a public GitHub issue for a suspected vulnerability.

Use GitHub's private vulnerability reporting feature for this repository when available. Include enough detail to reproduce and assess the issue, such as:

- affected component, platform, or adapter;
- affected version or commit;
- reproduction steps or proof of concept;
- expected versus observed behavior;
- potential security impact;
- any known mitigations.

Please avoid publishing exploit details until the issue has been assessed and, when necessary, a fix has been released.

## Scope

Security reports are especially relevant for issues involving:

- installation scripts or generated packages;
- CI/CD workflows;
- unsafe command execution;
- path traversal or filesystem writes;
- package or manifest integrity;
- instructions that could systematically weaken authentication, authorization, data integrity, or other production-critical safeguards.

Adaptive Engineering is primarily a methodology and integration project. Reports about vulnerabilities in third-party AI coding agents, IDEs, or platforms should generally be reported to those upstream projects unless the vulnerability is caused by Adaptive Engineering's own integration or generated artifacts.

## Response

Valid security reports will be triaged based on severity, exploitability, affected users, and available mitigations. Remediation may include documentation changes, integration changes, regenerated packages, or a patched release.
