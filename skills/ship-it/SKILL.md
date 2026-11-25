---
name: ship-it
description: Cut scope and set a time-box to get a v0 live. Use when a task keeps growing, the owner is polishing instead of shipping, or says it does not feel ready.
---

# Ship it

Context: `$ARGUMENTS` (what is stalling). If empty, use the current branch and conversation.

Delegate to the `holiday-os:ship-coach` subagent with the current state, then act on its result:

1. Write the **smallest shippable slice** and the **cut list** into `docs/ship-plan.md` (or the PR description).
2. Set the **time-box**, **success signal** and **kill signal** (see `intelligence/decision-framework.md`).
3. Start the first action immediately. Do not ask whether to start.
4. Anything real-defect (data loss, security hole, broken core journey) stays in scope; everything else that is cosmetic goes to the cut list.

Close with one line: what is live-able by when.
