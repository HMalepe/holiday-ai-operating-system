---
name: feature-dev
description: Plan and build a feature end to end with gates (define, plan, thin slices, self-check, independent verification). Use when asked to build, add or implement a feature.
---

# Feature development

Feature: `$ARGUMENTS`

Follow `workflows/feature-development.md` from the AI OS repo. Condensed, with the gates enforced:

1. **Define.** Write one sentence ("As <user>, I can <action> so that <outcome>"), acceptance criteria as an observable checklist, and an out-of-scope list. If anything blocks building and cannot be inferred, ask once; otherwise state the assumption and continue.
2. **Plan.** List the tables, endpoints and components expected to change. Flag auth, money and migrations as risks. If more than ~8 files or any one-way door, write a short spec in `docs/spec.md` first.
3. **Branch.** `feature/<short-name>`. Never work on main.
4. **Build in thin vertical slices**: data and migration, then API, then UI. Failing test first for logic and bug fixes. Commit each slice with a message that says why.
5. **Self-check** against the checklist in `workflows/feature-development.md` (four UI states, validated inputs, server-side permissions, no secrets, phone viewport).
6. **Independent verification.** Hand the acceptance criteria and diff to the `holiday-os:verifier` subagent. Do not mark done until it reports Verified or the gaps are accepted by the owner.
7. **Close the loop.** Update `docs/decisions.md` for any non-obvious decision. List follow-ups as tasks, not TODO comments.

## Finish with

- What shipped (3 lines), how it was verified (evidence), what is deferred.
- "Extras": one risk, one cheaper path, one related opportunity.
