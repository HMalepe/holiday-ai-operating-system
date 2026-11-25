---
name: project-audit
description: Comprehensive audit of an existing application (architecture, code quality, security, tests, UX, deployment) producing a prioritised fix list. Use when taking over a repo, before a big feature, or when asked "what's wrong with this project".
---

# Project audit

Audit the current repository against the Holiday AI OS standards and produce a prioritised report. Read-only: change nothing.

## Steps

1. **Orient (2 min).** Read `README`, `package.json`, the project `CLAUDE.md`, folder tree, and the last 20 commits. State what the app is, the stack, and how it deploys, in 5 lines.
2. **Fan out in parallel** with the Agent tool, one call each, all in a single message:
   - `holiday-os:security-reviewer`: secrets, RLS, authz, input validation, webhooks, dependencies.
   - `holiday-os:backend-engineer`: schema, migrations, API shape, idempotency, error handling (review only, no edits).
   - `holiday-os:frontend-engineer`: four states, mobile layout, accessibility, bundle weight (review only, no edits).
   - `holiday-os:qa-engineer`: what is tested, what is not, the riskiest untested path.
3. **Merge** findings. De-duplicate. Re-check any Critical or High finding yourself in the code before including it.
4. **Write** `docs/audit-<YYYY-MM-DD>.md` using `templates/project-audit.md` if it exists in the AI OS repo, otherwise this structure: Summary, Scorecard (Architecture / Security / Tests / UX / Ops, each 1-5), Findings table (severity, where, impact, fix, effort S/M/L), Top 5 actions, What is already good.
5. **Extras** (label them "Extras"): one cheaper path, one risk the owner has not mentioned, one quick win under 30 minutes.

## Rules

- Evidence only: file path and line for every finding, or label it "unverified".
- Never print secret values, only their location.
- End with the single best next action and its time-box.
