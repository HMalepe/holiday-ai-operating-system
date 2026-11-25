# Workflow: Debugging

Stop guessing. Find the cause, then fix the cause.

## 1. Reproduce
- Write the exact steps, inputs and environment that trigger it.
- Can't reproduce? Gather more evidence (logs, request IDs, user's device/browser) before touching code.

## 2. Observe
- Read the actual error message and stack trace in full.
- Check logs for the failing request (Vercel logs, Railway logs, Supabase logs, browser console, network tab).
- Note what changed recently: last deploy, env var, dependency, data, third-party outage.

## 3. Narrow
- Bisect: which layer? UI, API, database, third party, config.
- Make the failure smaller: minimal input, minimal component, single request via curl.
- Use `git bisect` or compare against the last known good deploy when it's a regression.

## 4. Hypothesise
- Write 2-3 candidate causes ranked by likelihood.
- For each, define a test that would disprove it. Run the cheapest first.

## 5. Fix
- Change one thing at a time.
- Fix the root cause, not the symptom. Ask "why was this possible?"
- Add a failing-then-passing test that guards against the bug.

## 6. Verify
- Re-run the original reproduction. Check nearby paths for the same bug.
- Verify in the real environment where it failed, not just locally.

## 7. Record
- One paragraph: symptom, root cause, fix, how to spot it sooner. Add to `docs/decisions.md` or the commit message.

## Rules for AI-assisted debugging
- Give the AI the full error, the relevant code and what you already tried.
- Reject "try this" shotgun fixes. Ask for the diagnosis first.
- If two attempts fail, stop and re-observe; the model of the problem is wrong.
