---
name: release-check
description: Pre-release readiness check for deploying to production (env vars, migrations, preview verification, rollback plan, monitoring). Read-only; it never deploys. Use before promoting a preview to production.
---

# Release check

Read-only readiness check. This skill never deploys, migrates or changes settings. Follow `workflows/deployment.md` from the AI OS repo for the actual release.

## Steps

1. **Branch state.** Clean working tree, branch up to date with main, PR approved or self-reviewed with `workflows/code-review.md`. Confirm `holiday-os:qa-gate` last passed on this commit.
2. **Preview verification.** Find the preview URL (Vercel MCP or `vercel ls` if available). Load it; check the core journey on a phone viewport and that there are no console errors or failed network calls.
3. **Environment.** Compare variable *names* required by the code (`process.env.*`, `.env.example`) against what the production environment defines. Report missing names only, never values.
4. **Database.** List migrations in the branch not yet applied to production. For each: reversible? long lock? data backfill? Mark anything destructive as a one-way door that needs explicit approval.
5. **Webhooks and third parties.** Endpoints, signing secrets present, callback URLs pointing at the production domain.
6. **Rollback plan.** One paragraph: how to revert the deploy, the migration and any data change, and how long it takes.
7. **Monitoring.** Where will errors show up in the first hour, and who looks.

## Output

Checklist with pass / fail / n/a and evidence per line, then **Go** / **Go after fixes** / **No-go**, and the exact commands the owner will run (not run by this skill).
