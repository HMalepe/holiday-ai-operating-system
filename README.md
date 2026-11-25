# holiday-ai-operating-system

The instructions, reusable workflows, knowledge and standards that govern my AI-assisted work.

One source of truth, so I stop re-explaining myself in every chat and every AI gives me the same quality bar.

## How to use it

1. **Claude Code / any coding agent:** drop the snippet from `CLAUDE.md` into a project's own `CLAUDE.md` (or point at this repo). The agent reads the standards and follows the workflows.
2. **ChatGPT / Claude Projects:** upload `intelligence/` plus whichever `agents/` and `workflows/` files fit the job into the project's knowledge or instructions.
3. **One-off chat:** paste the relevant agent file, say "run `workflows/<name>.md`".

## Map

| Folder | What lives there | Read when |
|---|---|---|
| `intelligence/` | Who I am, how to collaborate with me, how I decide, how research must be done | Always, first |
| `engineering/` | Architecture, frontend, backend, security, testing standards | Writing or reviewing code |
| `agents/` | Role prompts (product architect, frontend, backend, security, QA, research) | Need a specialist hat |
| `workflows/` | Step-by-step playbooks with gates | Starting, building, reviewing, debugging, shipping |
| `templates/` | Fill-in documents (PRD, tech spec, audit) | Producing a deliverable |

## Operating rules for this repo

- **Ship before ready.** A rough file used on a real project beats a perfect file never used. Edit after friction, not before.
- **Every file earns its place.** If a file was never used in a real project, shrink or delete it.
- **Standards are defaults, not laws.** A project can override one if the reason is written down in its tech spec.
- **Change log lives in git.** Commit message = what friction caused the change.

## Status

v0.1: starter content for every file. Next step: run one real project through `workflows/new-project.md` and fix whatever hurts.
