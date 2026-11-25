# Testing standards

Test enough to ship with confidence, not to chase a coverage number.

## What to test, in priority order

1. **Money, auth and data-loss paths.** Always automated.
2. **Core user journey** (the one thing the product exists to do). One end-to-end test.
3. **Business logic** (calculations, rules, parsing). Unit tests, fast and many.
4. **Integrations.** Contract tests against sample payloads; mock the network.
5. **UI details.** Manual check unless it's a regression-prone component.

## Test pyramid (lite)

| Level | Tool (default) | Share |
|---|---|---|
| Unit | Vitest | Most |
| Integration (API + DB) | Vitest + test database or Supabase branch | Some |
| End-to-end | Playwright | A few, critical flows only |

## Rules

- A bug fix starts with a failing test that reproduces it, then the fix.
- Tests are deterministic: no real network, no real time, no shared state.
- Name tests as behaviours: `rejects a webhook with an invalid signature`.
- Use realistic fixtures (real payload shapes, ZAR amounts, SA phone formats).
- Don't mock what you own; mock the boundary.

## Manual smoke checklist (before every release)

- [ ] Sign up / sign in / sign out
- [ ] The core journey, start to finish, on a phone
- [ ] Empty state, error state, slow network
- [ ] A permission boundary: user A cannot see user B's data
- [ ] No console errors; no failed network calls
- [ ] Env vars present in the target environment

## Definition of done

Feature works, tests for the risky parts pass, smoke checklist run, no new lint or type errors, docs or decision log updated.

## AI-written code

Treat it as untrusted until run. Run it, read it, test the edge cases yourself (empty input, huge input, duplicates, wrong types, unauthenticated).
