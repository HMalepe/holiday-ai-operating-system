# Workflow: Code review

Works for AI-written code and for my own. The reviewer's job is to find problems, not to be polite.

## Order of review

1. **Intent**: does the change do what the acceptance criteria say, and nothing extra?
2. **Correctness**: logic, edge cases (empty, null, huge, duplicate), off-by-one, time zones, currency rounding.
3. **Security** (`security-standards.md`): secrets, authorisation, RLS, input validation, webhook verification, injection.
4. **Data safety**: migrations reversible or safe, no destructive change without explicit approval.
5. **Reliability**: error handling, timeouts, retries, idempotency.
6. **Tests**: risky paths covered, tests deterministic.
7. **Readability**: names, size of functions, comments that explain why.
8. **Performance**: N+1 queries, unbounded lists, heavy client bundles.
9. **UX**: states, accessibility, phone viewport.

## Output format

```
Verdict: APPROVE / CHANGES REQUESTED / BLOCK

Blocking (must fix):
- <file:line> <problem> -> <fix>

Should fix:
- ...

Nits:
- ...

Verified by running: <what was actually executed>
```

## Rules

- Run the code. Reading is not reviewing.
- Every blocking comment has a concrete fix or a reproduction.
- Separate **blocking** from **preference**. Don't hold up shipping for style.
- Praise only what's genuinely good, briefly. Not filler.
- For AI-generated diffs: check for hallucinated APIs, packages that don't exist, silently deleted code, and tests that assert nothing.
