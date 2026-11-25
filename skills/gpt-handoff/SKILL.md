---
name: gpt-handoff
description: Package the current work (spec, diff summary, test evidence, open questions) into a paste-ready packet for ChatGPT or Codex to review independently. Use when you want a second model to challenge a plan or implementation.
---

# GPT handoff packet

Goal: give a second model everything it needs to review critically, without leaking secrets and without your conclusions steering it.

## Steps

1. Gather: the one-paragraph goal, the acceptance criteria, the design decisions made and why, the diff summary (files changed + intent, not the whole diff unless small), test and verification evidence, and the open questions or doubts.
2. Redact: remove secrets, keys, personal data (customer names, phone numbers, emails) and internal URLs that should not leave the project. Replace with placeholders.
3. Fill `templates/handoff-packet.md` from the AI OS repo (or the structure below) and save it as `docs/handoffs/<YYYY-MM-DD>-<topic>.md` in the project.
4. Print the packet so it can be pasted, plus the exact review instruction to send with it.

## Structure

```
# Handoff: <topic>
Goal:
Acceptance criteria:
Decisions made (with reasons):
What changed (file: intent):
Evidence (commands + results):
Known gaps / doubts:
## Review request
You are an independent reviewer. Do not assume the implementation is correct.
1. List the assumptions this work depends on and which are unverified.
2. Find the 3 most likely ways this fails in production.
3. Name anything missing from the acceptance criteria.
4. Say what you would test that has not been tested.
5. Verdict: Ship / Ship after fixes / Don't ship, blocking items first.
```

## Rules

- Do not include your own verdict ("this looks good"). State facts and evidence only.
- When the reviewer's reply comes back, treat each point as a hypothesis: verify in code before acting, and record accepted/rejected points in the handoff file.
