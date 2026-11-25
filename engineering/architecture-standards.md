# Architecture standards

Defaults for new projects. Override per project in the tech spec with a written reason.

## Principles

1. **Simplest thing that works, then grow.** One deployable, one database, until a real constraint says otherwise.
2. **Boring tech.** Pick tools with big communities so AI and search both know them well.
3. **Make it deployable on day one.** A live URL by end of session one beats a perfect local app.
4. **Separate concerns, not files for the sake of it.** UI, domain logic, data access, integrations.
5. **Everything configurable lives in env vars.** Nothing environment-specific in code.
6. **Design for the phone.** Many of my tools are used from a mobile browser.

## Default stack

| Layer | Default | Notes |
|---|---|---|
| Frontend / full-stack | Next.js (App Router) + TypeScript + Tailwind | Single-file HTML is fine for tiny tools |
| Database + auth | Supabase (Postgres, Auth, Storage) | Row Level Security always on |
| Hosting | Vercel | Preview deploy per branch |
| Long-running workers, bots, queues | Railway | Anything that can't be a serverless function |
| Messaging | WhatsApp Cloud API / Twilio | Verify webhook signatures |
| Payments | Provider-hosted checkout | Never touch raw card data |
| Source control | GitHub, trunk-based with short branches | |

## Suggested layout (Next.js)

```
src/
  app/            routes, layouts, server actions
  components/     presentational UI
  features/<x>/   feature-scoped UI + logic + types
  lib/            shared helpers (db client, auth, utils)
  server/         server-only code (services, integrations)
docs/
  decisions.md    short decision log
  spec.md         living tech spec
```

## Rules

- Define data model first (tables, relations, ownership), UI second.
- Every external integration sits behind one module (`server/integrations/<name>.ts`) so it can be mocked and swapped.
- Idempotency for anything triggered by webhooks or retries.
- Background work goes through a queue or scheduled job, not a request handler.
- Keep functions small; if a file passes ~300 lines, split by responsibility.
- Record any non-default choice in `docs/decisions.md`.

## Scale triggers (don't pre-optimise)

Add caching, queues, or services only when you can name the measured problem: p95 latency, rate limits, cost, or reliability incidents.
