# holiday-ai-operating-system

The instructions, reusable workflows, knowledge and standards that govern my AI-assisted work.

One source of truth, so I stop re-explaining myself in every chat and every AI gives me the same quality bar.

## Install (Claude Code)

```
/plugin marketplace add HMalepe/holiday-ai-operating-system
/plugin install holiday-os@holiday-ai-os
```

On Claude Code 2.1.275 or later: `/plugin install holiday-os --marketplace HMalepe/holiday-ai-operating-system`.

This adds 9 skills (`/holiday-os:qa-gate`, `feature-dev`, `project-audit`, `security-audit`, `ui-critique`, `architecture-review`, `release-check`, `gpt-handoff`, `ship-it`), 8 subagents, a session brief injected into every session, and a guard hook that blocks secret access and asks before destructive actions.

## How to use it

1. **Claude Code:** install the plugin (above). Wire each project once with `scripts/bootstrap-project.sh <project-dir>`; it adds a `CLAUDE.md`, `AGENTS.md`, Cursor rules, MCP config, CI and a settings file that auto-enables the plugin.
2. **Cursor:** the bootstrap kit's `.cursor/rules/` carries the standards. Cursor also reads `AGENTS.md`.
3. **ChatGPT and Codex:** paste-ready Projects, Custom GPTs, research prompts and a review prompt live in `chatgpt/`. ChatGPT can't read this repo, so setup is paste-once.
4. **One-off chat:** paste the relevant `agents/` file and say "run `workflows/<name>.md`".

Full step-by-step: `docs/setup-checklist.md`.

## Map

| Folder | What lives there | Read when |
|---|---|---|
| `intelligence/` | Who I am, how to collaborate with me, how I decide, how research must be done, the session brief | Always, first |
| `engineering/` | Architecture, frontend, backend, security, testing standards | Writing or reviewing code |
| `agents/` | Subagents (product architect, frontend, backend, security reviewer, QA, research, verifier, ship coach) | Need a specialist hat |
| `skills/` | Reusable procedures invoked as `/holiday-os:<name>` | Auditing, building, gating, releasing |
| `workflows/` | Playbooks with gates (new project, feature, review, debugging, deployment, cross-model pipeline, worktrees, research, weekly review) | Starting, building, reviewing, shipping |
| `hooks/`, `scripts/` | Guard hook, session brief, bootstrap and validation scripts | Maintaining the system |
| `templates/` | PRD, tech spec, audit, handoff packet, friction log, and `project-bootstrap/` (the kit copied into projects) | Producing a deliverable or wiring a project |
| `chatgpt/` | ChatGPT personalization, 5 Projects, 5 Custom GPTs, Deep research prompts, Codex review | Setting up or using ChatGPT |
| `docs/` | Capability map, setup checklist, hidden features | Orienting, setting up |
| `tests/` | Guard hook tests | Changing the guard |

## Operating rules for this repo

- **Ship before ready.** A rough file used on a real project beats a perfect file never used. Edit after friction, not before.
- **Every file earns its place.** If a file was never used in a real project, shrink or delete it.
- **Standards are defaults, not laws.** A project can override one if the reason is written down in its tech spec.
- **Change log lives in git.** Commit message = what friction caused the change.
- **Enforce what matters.** A rule that must never break becomes a hook, not a sentence.
- **Check yourself.** `python3 scripts/validate.py && python3 -m unittest discover -s tests` before merging; CI runs the same.

## Status

v0.2: plugin (skills, subagents, hooks), cross-tool kit (Claude Code, Cursor, Codex), ChatGPT kit, cross-model pipeline, CI and validator. Next step: run one real project through `workflows/cross-model-pipeline.md`, log what hurts in `templates/friction-log.md`, and fix it at the Friday review.
