# Workflow: Feature development

## 1. Define (5-15 min)
- One sentence: "As <user>, I can <action> so that <outcome>."
- Acceptance criteria as a checklist (observable, testable).
- Out of scope list.

## 2. Plan
- Which tables, endpoints, components change? List files expected to be touched.
- Risks: auth, money, data migration, third-party limits.
- If the plan touches more than ~8 files or any one-way door, write a short spec first.

## 3. Branch
- `feature/<short-name>` off the main branch. Small, short-lived.

## 4. Build in thin vertical slices
- Data and migration first, then API, then UI.
- Commit small and often with messages that say why.
- Write tests for risky logic as you go; for bug fixes, failing test first.

## 5. Self-check before review
- [ ] Runs locally, no console errors
- [ ] Acceptance criteria each verified by hand
- [ ] Loading / empty / error states handled
- [ ] Inputs validated, permissions checked server-side
- [ ] No secrets, no stray debug code, types and lint clean
- [ ] Phone viewport checked

## 6. Review
- Run `workflows/code-review.md`.

## 7. Merge and ship
- Merge to main after the preview deploy is verified.
- Follow `workflows/deployment.md` for production.

## 8. Close the loop
- Update docs or the decision log if anything non-obvious was decided.
- Note anything deferred as a follow-up task, not a "TODO" buried in code.
