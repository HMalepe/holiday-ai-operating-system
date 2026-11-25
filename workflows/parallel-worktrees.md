# Workflow: Parallel agents with git worktrees

A worktree is a second working folder on the same repository, on its own branch. Two agents can edit at the same time without stepping on each other's files or branches.

## When it is worth it

- Two or more tasks that touch **different files** (e.g. a landing page and a webhook handler).
- A long task you don't want to block (migration, big refactor) while you keep shipping small things.
- Comparing two approaches to the same problem; keep the better one.

Not worth it when tasks touch the same files, or when one depends on the other's output. Then do them in order.

## Claude Code (terminal or Cursor)

```bash
claude -w feature-invoices      # new worktree + branch for this session
claude -w fix-webhook-retries   # second terminal, second worktree
```

`-w` / `--worktree [name]` creates the worktree for the session. List and clean up with plain git:

```bash
git worktree list
git worktree remove ../<folder>   # after the branch is merged
```

## Claude Code on the web

Each web session already runs in its own cloud sandbox on its own branch. Start one session per task from the same repo and merge via PRs. For a mechanical change across many files, try `/batch <instruction>`: it plans, splits the work into independent units and runs them in parallel.

## Ground rules

1. **Disjoint files.** Write down which files each task owns before starting.
2. **One migration owner.** Only one branch at a time creates database migrations; number them on merge to avoid collisions.
3. **Small and short-lived.** Merge within the day if possible. Long-lived branches turn into merge conflicts.
4. **Merge order.** Foundations first (schema, shared types), then features, then UI polish. Rebase the later branches on main after each merge.
5. **Verify each branch alone**, then once more on main after merging both (`/holiday-os:qa-gate`).
6. **Don't share a dev database.** Use separate Supabase branches or schemas so one agent's test data doesn't break the other's.

## Parallel reviewers (the cheap win)

You don't need worktrees to parallelise review: ask for `security-reviewer`, `qa-engineer` and `frontend-engineer` subagents in one message (that is what `/holiday-os:project-audit` does), or run `/simplify` for four parallel cleanup reviewers on the changed code.
