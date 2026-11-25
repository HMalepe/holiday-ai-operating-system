# Workflow: Deployment

Default path: GitHub -> Vercel (web) / Railway (workers). Deploy often; keep releases small.

## Pre-deploy checklist

- [ ] Branch merged to main; CI or local type-check, lint and tests pass
- [ ] Preview deployment verified on phone and desktop
- [ ] Env vars set in the target environment (compare names against `.env.example`)
- [ ] Database migrations reviewed; backup or branch taken for anything destructive
- [ ] `agents/security-reviewer` pass done for new auth, payments, webhooks or file handling
- [ ] Third-party config updated (webhook URLs, redirect URIs, allowed origins)
- [ ] Rollback plan known (previous deployment to promote, migration to revert)

## Deploy

1. Run migrations first if they're backward compatible (new columns/tables); app second.
2. Deploy to production via merge to main (or promote the verified preview).
3. Watch the deployment build log to completion.

## Post-deploy verification (within 10 minutes)

- [ ] Production URL loads; no console errors
- [ ] Core journey works end to end with a real test account
- [ ] Webhooks arrive and are processed (send a test event)
- [ ] Logs show no new error spike
- [ ] Health endpoint returns OK

## Rollback

- Web: promote the previous good deployment (Vercel instant rollback).
- Worker: redeploy the previous commit.
- Database: only roll back with a tested down-migration or restore; otherwise fix forward.
- After rollback, write down what failed before retrying.

## Rules

- Don't deploy on a Friday evening unless the change is trivial and reversible.
- Never run untested migrations on production data.
- Keep `main` always deployable.
- Tag meaningful releases and note what shipped in the commit or release notes.
