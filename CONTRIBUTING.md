# Contributing to Adaptive Engineering

Thanks for helping improve Adaptive Engineering.

## Contribution principles

Adaptive Engineering itself follows the same discipline it promotes:

- use the least process necessary for the change;
- inspect existing behavior before adding new abstractions;
- prefer the smallest coherent solution;
- preserve compatibility across supported hosts unless a breaking change is intentional;
- verify changes with executable evidence;
- simplify before considering the work complete.

## Development workflow

1. Fork the repository or create a feature branch from `main`.
2. Keep each pull request focused on one coherent change.
3. Make the smallest change that satisfies the requirement.
4. Run the validation suite locally.
5. Open a pull request against `main`.

Suggested branch names:

```text
feat/<short-description>
fix/<short-description>
docs/<short-description>
chore/<short-description>
```

## Validation

Python 3.11 or newer is required. No third-party Python packages are needed.

Before opening a pull request, run:

```bash
python3 scripts/validate.py
python3 scripts/build-agent-plugin.py
python3 scripts/build-antigravity.py
python3 scripts/build-opencode.py
python3 scripts/validate.py --dist
```

For Cursor-specific changes, also verify the installer round trip when relevant:

```bash
./scripts/install-local.sh
./scripts/uninstall-local.sh
```

GitHub Actions runs the repository validation workflow on every pull request.

## Pull requests

Pull requests should:

- explain the problem or goal;
- describe the chosen solution and relevant trade-offs;
- identify affected platforms or adapters;
- include verification evidence;
- avoid unrelated refactors;
- call out compatibility or migration impact when applicable.

Use Conventional Commit-style pull request titles where practical:

```text
feat: ...
fix: ...
docs: ...
refactor: ...
test: ...
chore: ...
```

The repository uses squash merging, so the pull request title becomes the commit title on `main`.

## Changes to the methodology

Changes under `core/` are canonical and may affect every platform integration. Treat methodology changes as higher impact than host-specific adapter changes and verify generated packages after modifying the canonical core.

Host-specific manifests and adapters should remain thin. Avoid duplicating canonical methodology content when it can be referenced or generated instead.

## Reporting bugs and proposing features

Use the GitHub issue templates for reproducible bugs and feature proposals. Security-sensitive reports should follow `SECURITY.md` instead of being filed as public issues.
