# Capability map

The ten capabilities from the AI operating environment plan, where each lives, and what is left for you.

| # | Capability | Where it lives | Built | You still do |
|---|---|---|---|---|
| 1 | Persistent intelligence | `intelligence/`, `intelligence/session-brief.md` (injected every session by the plugin), `chatgpt/personalization.md`, `chatgpt/projects/` | Yes | Paste into ChatGPT (setup step 3) |
| 2 | Agent orchestration | `agents/` (8 subagents: product-architect, frontend-engineer, backend-engineer, security-reviewer, qa-engineer, research-analyst, verifier, ship-coach) | Yes | Nothing; `/agents` to see them |
| 3 | Reusable skills | `skills/` (9: project-audit, architecture-review, feature-dev, ui-critique, security-audit, qa-gate, release-check, gpt-handoff, ship-it) | Yes | Install plugin (step 1) |
| 4 | Tool connectivity | `templates/project-bootstrap/.mcp.json` (Supabase read-only, Vercel, Playwright) | Yes | Authenticate with `/mcp` (step 4) |
| 5 | Autonomous execution with approvals | `hooks/hooks.json` + `scripts/hooks/guard.py` (deny secrets, ask before destructive actions), `workflows/cross-model-pipeline.md` gates | Yes | Nothing |
| 6 | Research intelligence | `workflows/research-deep-dive.md`, `chatgpt/deep-research-prompts.md`, `agents/research-analyst.md`, SA Market Researcher GPT | Yes | Create the GPT |
| 7 | Software engineering | `engineering/`, `.cursor/rules` in the bootstrap kit, `AGENTS.md` | Yes | Run bootstrap on a project (step 2) |
| 8 | Quality assurance | `verifier` subagent, `qa-gate`, `security-audit`, `release-check`, `templates/project-bootstrap/.github/workflows/quality-gate.yml`, `chatgpt/codex-review.md` | Yes | Optional CI secret (step 5) |
| 9 | Creative production | UX Creative Director GPT, `skills/ui-critique` | Yes | Create the GPT |
| 10 | Automation | `claude-review.yml` (PR review), `.github/workflows/validate.yml` (keeps this repo healthy), `/loop` and `/schedule` (see `docs/hidden-features.md`) | Partly | Add the secret if you want PR review; schedule only after a manual run proves useful |

## What this layer deliberately does not do

- **No MCP servers in the plugin itself.** They load into every session and cost context. They live in the per-project `.mcp.json` so each project takes only what it needs.
- **No auto-formatter hook.** Formatters differ per project; add one in the project's own `.claude/settings.json`.
- **No scheduled agents yet.** Automate a workflow only after you've run it by hand three times.
- **No ChatGPT automation.** ChatGPT can't read this repo; its setup is paste-once.
