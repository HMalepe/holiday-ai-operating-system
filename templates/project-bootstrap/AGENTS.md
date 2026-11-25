# AGENTS.md

Same project, same rules as `CLAUDE.md`. Read `CLAUDE.md` first for stack, commands and project facts.

## Role

If you are Codex or another reviewing agent: you are the independent reviewer. Do not edit unless asked to fix. Run `npm run lint`, `npm run typecheck`, `npm test` and `npm run build`, quote the output, and review the diff against the standards at https://github.com/HMalepe/holiday-ai-operating-system (`engineering/` and `workflows/code-review.md`).

Report a table of severity, finding, where and fix, then a verdict: Ship / Ship after fixes / Don't ship.

## Never

- Read, print or commit `.env*` files or any secret.
- Run destructive database commands or production deploys.
