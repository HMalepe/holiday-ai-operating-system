---
name: security-audit
description: Security review of the current repo or diff (secrets, RLS, authorisation, validation, webhooks, prompt injection, dependencies, POPIA). Use before shipping anything touching auth, user data, money or third-party webhooks.
---

# Security audit

Scope: `$ARGUMENTS` (a diff range, folder, or empty for the whole repo).

## Steps

1. Delegate to the `holiday-os:security-reviewer` subagent with the scope. Meanwhile run the mechanical checks yourself:
   - Secrets: search the tree **and** `git log -p` for key-shaped strings (`sk-`, `ghp_`, `AKIA`, `eyJ`, `service_role`, `-----BEGIN`). Confirm `.env*` is in `.gitignore`.
   - Client leaks: grep for `NEXT_PUBLIC_` values that look like secrets, and for the Supabase service-role key anywhere under client code.
   - Dependencies: `npm audit --omit=dev` (or the project's equivalent); list high and critical only.
   - RLS: list every table from migrations and confirm `enable row level security` plus at least one policy each. Missing means Critical.
2. Verify every finding the subagent reports at Critical or High by pointing to the code. Downgrade or drop anything you cannot confirm.
3. Test the permission boundary if the app can run: two users, user A requests user B's resource by ID.

## Output

| Severity | Finding | Where | How to exploit (1 line) | Fix |
|---|---|---|---|---|

Then: **Ship** / **Ship after fixes** / **Don't ship**, with blocking items listed.

## Rules

- Never print a secret's value; give file and line only.
- If a secret has leaked, the first fix is rotating it, then removing it from history.
- Propose correct fixes, never "fix" by disabling a control.
