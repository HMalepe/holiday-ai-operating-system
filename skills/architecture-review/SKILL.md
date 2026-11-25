---
name: architecture-review
description: Review a system design, tech spec or existing architecture against the default stack and principles, naming one-way doors and cheaper alternatives. Use before committing to a design, or when a project feels over-engineered.
---

# Architecture review

Target: `$ARGUMENTS` (a spec file, a folder, or "this repo"). If empty, review the current repo.

## Steps

1. Read the target plus `engineering/architecture-standards.md` (from the AI OS repo or the session brief) and any `docs/decisions.md`.
2. **Draw it in text**: components, data stores, external services, trust boundaries, and which request or event flows through each.
3. **Score against the principles** (simplest thing, boring tech, deployable day one, separated concerns, config in env, phone-first). One line each with evidence.
4. **Find the doors.** List every decision that is hard to reverse (data model, auth provider, vendor lock-in, public API shape, pricing model baked into code). For each: the rollback cost.
5. **Find the weight.** Anything that is not justified by a measured problem (extra service, queue, cache, microservice, custom auth). Propose deleting or deferring it.
6. **Alternatives.** At least one genuinely different design, with what it trades off. Recommend one.

## Output

- Verdict: **Sound** / **Sound with changes** / **Rethink**.
- Table of risks: risk, likelihood, impact, mitigation.
- The decisions to record in `docs/decisions.md`, drafted as one paragraph each (decision, date, reason, what would change my mind).
- "Extras": the non-obvious thing a senior engineer would add.
