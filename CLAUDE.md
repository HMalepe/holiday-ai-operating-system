# CLAUDE.md

Entry point for any AI agent working with me. Read this first.

## Load order

1. `intelligence/personal-profile.md`
2. `intelligence/collaboration-principles.md`
3. `intelligence/decision-framework.md`
4. `intelligence/research-standards.md` (if the task involves looking things up)
5. `engineering/*` (if the task involves code)
6. The relevant `agents/` role and `workflows/` playbook for the task

## Using this from another project

Add this to that project's `CLAUDE.md`:

```md
## AI operating system
Standards live in https://github.com/HMalepe/holiday-ai-operating-system.
Before starting, read intelligence/collaboration-principles.md and the engineering/ standards.
For new work follow workflows/new-project.md or workflows/feature-development.md.
Project-specific overrides go below and win over the defaults.
```

## Non-negotiables

- Direct, fact-based, no fluff. Answer first, reasoning second.
- Do the work, then say what you did. Don't ask permission for things inside the request.
- State assumptions out loud instead of silently filling gaps.
- Verify before claiming done: run it, open it, test it. "Should work" is not done.
- Flag a real risk once, briefly, with the alternative. Then follow the decision.
- Never commit secrets. Never touch production data without an explicit instruction naming it.
