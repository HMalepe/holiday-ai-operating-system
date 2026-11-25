---
name: qa-gate
description: Quality gate to run before calling work done: lint, types, tests, build, acceptance-criteria verification and the smoke checklist, with evidence. Use before opening a PR or claiming a feature is finished.
---

# QA gate

Run the gate on the current branch. A gate that was not run is a gate that failed.

## Steps

1. **Detect commands** from `package.json` / `Makefile` / CI config: lint, typecheck, unit tests, build. If a check does not exist, record "missing" (that is itself a finding).
2. **Run them** in this order and capture the result of each: lint, typecheck, tests, build. Stop on first failure only if later steps depend on it; otherwise continue and report all.
3. **Acceptance criteria.** Find them (PR description, `docs/spec.md`, the feature's user story). Hand them to `holiday-os:verifier` with the diff and ask for an evidence table.
4. **Smoke checklist** from `engineering/testing-standards.md`: sign in/out, core journey on a phone viewport, empty/error/slow states, permission boundary, no console errors, env vars present.
5. **Secrets scan** on the diff (key-shaped strings, `.env` files staged).

## Output

| Gate | Result | Evidence |
|---|---|---|
| Lint | pass / fail / missing | command + last lines |
| Types | | |
| Tests | | counts |
| Build | | |
| Acceptance criteria | | verifier table |
| Smoke checklist | | |
| Secrets scan | | |

Final line: **PASS**, **PASS with accepted gaps** (list), or **FAIL** (blockers first). Do not say "done" on anything but PASS.
