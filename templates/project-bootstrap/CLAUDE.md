# <Project name>

<One sentence: what this is and who it is for.>

## AI operating system

Standards live in https://github.com/HMalepe/holiday-ai-operating-system and load automatically through the `holiday-os` plugin (see `.claude/settings.json`). If the plugin is not active, read `intelligence/collaboration-principles.md` and the `engineering/` standards there before starting. Project-specific rules below win over the defaults.

## Stack

- Next.js (App Router) + TypeScript + Tailwind
- Supabase (Postgres, Auth, Storage), RLS on every table
- Vercel (preview per branch), GitHub trunk-based

## Commands

```bash
npm run dev        # local dev server
npm run lint       # lint
npm run typecheck  # tsc --noEmit
npm test           # unit tests
npm run build      # production build
```

## Verify before "done"

Run lint, typecheck, tests and build. Use `/holiday-os:qa-gate` for the full gate and `/holiday-os:release-check` before production. Never claim done from reading code alone.

## Project facts the AI can't infer

- Core user journey: <the one thing this product exists to do>
- Data ownership: <which tables are per-user, which are shared>
- External services: <WhatsApp / Twilio / payments, and which env var names they use>
- Not allowed: <things that must never happen here>

## Overrides to the default standards

<None yet. Write the reason for every override here and in docs/decisions.md.>
