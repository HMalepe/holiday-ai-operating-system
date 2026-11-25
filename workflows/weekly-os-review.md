# Workflow: Weekly OS review (20 minutes, Friday)

This repo only stays valuable if it keeps absorbing what hurts. The review is how.

## Steps

1. **Read the friction log** (`templates/friction-log.md`, kept per project or in one place). 3 minutes.
2. **Group repeats.** Anything that appears twice is a missing rule. Anything you re-explained is a missing line in `intelligence/` or a project `CLAUDE.md`.
3. **Pick the top 3** by pain, not by interest. For each, choose the smallest fix:
   - AI ignored a standard: tighten the line in `engineering/` or add it to the `.cursor/rules` and session brief.
   - A multi-step task you keep prompting: make it a skill in `skills/`.
   - A role that should think differently: edit or add an `agents/` file.
   - Something must never happen: make it a hook (`scripts/hooks/guard.py`) so it's enforced, not requested.
4. **Make the edits** on a branch. Commit message = the friction that caused it ("AI kept asking which stack; added to session brief").
5. **Prune.** Pick one file that was never used this week. Shrink or delete it. Every file earns its place.
6. **Validate and merge.** `python3 scripts/validate.py && python3 -m unittest discover -s tests`, then merge. Bump the plugin `version` in `.claude-plugin/plugin.json` so installed copies update.
7. **Score the week** (one line each): projects shipped, time from idea to live v0, times a second model caught a real bug. If the numbers are flat for a month, the system isn't paying for itself; cut it down.

## Principle

Edit after friction, not before. Ten minutes of real use beats an hour of imagining what might be needed.
