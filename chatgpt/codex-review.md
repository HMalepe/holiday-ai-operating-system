# Independent review with Codex (or any second model)

The point: the model that wrote the code should not be the one that signs it off. A second model with a different failure profile catches what the first one is blind to.

> Codex availability and cloud features depend on your ChatGPT plan and rollout. If you don't see it in your account, use the same prompt in a plain ChatGPT chat with the diff pasted, or in the Software Engineering project.

## Setup (once per repo)

1. Make sure the repo has `AGENTS.md` (the bootstrap script adds it). Codex reads it for its role and the standards.
2. In ChatGPT, open Codex and connect the GitHub repo (if your plan offers it).
3. On a pull request, you can also ask for a review by commenting `@codex review` once the GitHub integration is connected.

## The review prompt

Paste with a handoff packet from `/holiday-os:gpt-handoff`, or point Codex at the branch:

```
You are an independent code reviewer. You did not write this code. Do not assume it is correct, and do not edit files.

Context: <goal and acceptance criteria>
Standards: AGENTS.md and the engineering standards it references.

1. Run lint, typecheck, tests and build. Quote the output.
2. Review the diff for: secrets, missing authorisation, RLS gaps, unvalidated input, webhook signature and idempotency, missing UI states, race conditions, error handling, N+1 queries, and anything that passes locally but fails in production.
3. List the assumptions this work depends on that nothing verifies.
4. Name the 3 most likely production failures.
5. Say what is missing from the acceptance criteria and what has not been tested.

Report a table: severity (Critical/High/Medium/Low), finding, file:line, how it fails, fix. Only include findings you can point to in code; label the rest "unverified".
End with a verdict: Ship / Ship after fixes / Don't ship, blocking items first.
```

## After the review

Treat every finding as a hypothesis. Verify it in code before acting. Record accepted and rejected findings in the handoff file with one line each, so the reasoning survives. Feed accepted fixes back to Claude Code, then re-run the verifier.
