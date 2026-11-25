# Workflow: Cross-model pipeline

Idea to live product, with each model doing what it is best at and a second model checking the first. Use the tier that matches the risk; do not run the full pipeline on a typo fix.

## Who does what

| Stage | Who | Artifact | Gate |
|---|---|---|---|
| 1. Discover | ChatGPT (Product Development project, Deep research) | PRD from `templates/product-requirements.md` | **G1:** you approve the PRD |
| 2. Specify | ChatGPT (Software Engineering project; challenge it with the Architecture Reviewer GPT) | Tech spec from `templates/technical-specification.md` | **G2:** you approve the spec |
| 3. Explore | Claude Code in plan mode (read-only) | Plan: files to touch, risks, slices | You skim and say go |
| 4. Build | Claude Code with `/holiday-os:feature-dev` on a branch; subagents for backend, frontend | Commits in thin slices | CI quality gate green |
| 5. Verify | `/holiday-os:qa-gate` (runs the `verifier` subagent), plus `/holiday-os:security-audit` for auth, data or money | Evidence table | **G3:** PASS |
| 6. Second opinion | `/holiday-os:gpt-handoff` then ChatGPT or Codex (`chatgpt/codex-review.md`) | Handoff file with accepted / rejected findings | Blocking findings fixed |
| 7. Review and merge | You on the PR (and optional `claude-review.yml`) | Merged PR | **G4:** you approve |
| 8. Preview and release check | Vercel preview, `/holiday-os:release-check` | Go / No-go | **G5:** you approve production |
| 9. Promote | You (or Claude on your explicit instruction) | Production deploy | Smoke check on the live URL |
| 10. Learn | You, 2 minutes | One line in the friction log | n/a |

## Tiers

| Tier | Example | Stages |
|---|---|---|
| 1 Small | copy change, style tweak, small bug | 4, 5 (qa-gate), 7 |
| 2 Feature | new page, new endpoint, new table | 2 (short spec), 3, 4, 5, 6 (one reviewer), 7, 8 |
| 3 Risky | auth, payments, personal data, migrations, anything messaging real people | everything, with `security-audit` and a rollback plan |

## Rules

- **One writer, many checkers.** Only Claude Code (or you) edits code. ChatGPT and Codex review and advise.
- **Evidence over opinion.** Every "done" and every review finding gets checked against real output or real code.
- **Handoffs are files, not vibes.** Anything crossing from one model to another goes through `templates/handoff-packet.md`, redacted of secrets and personal data.
- **Time-box each stage.** Default: v0 live within 1-3 sessions. If a stage overruns, run `/holiday-os:ship-it`.
- **Production and migrations are one-way doors.** They need your explicit instruction naming the target. The guard hook asks before the risky commands.

## Handing the spec to Claude Code

Paste this with the approved spec (the Product Development project can generate it for you):

```
Use /holiday-os:feature-dev for this. Start in plan mode: read the repo, list files to touch, risks and slices, and wait for my go.
Spec: <paste>
Acceptance criteria: <paste>
Stack defaults and constraints: see CLAUDE.md. Do not touch main. When done, run /holiday-os:qa-gate and show me the evidence table.
```
