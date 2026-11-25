# Setup checklist

Everything in the repo is built. These are the steps only you can do (logins, buttons, accounts). Roughly 45 minutes in total; do them in order, stop whenever you've got what you need.

## 1. Merge and install the plugin (5 min)

1. Merge the PR that added this layer.
2. In Claude Code (terminal, Cursor or web), run:
   ```
   /plugin marketplace add HMalepe/holiday-ai-operating-system
   /plugin install holiday-os@holiday-ai-os
   ```
3. Check it loaded: type `/holiday-os:` and you should see `qa-gate`, `feature-dev`, `project-audit` and the rest. `/agents` should list `security-reviewer`, `verifier`, `ship-coach` and friends.
4. Optional local check: `claude plugin validate .` from the repo root.

## 2. Wire your first project (5 min per project)

From a clone of this repo:

```bash
scripts/bootstrap-project.sh ~/code/<project>
```

It copies `CLAUDE.md`, `AGENTS.md`, Cursor rules, `.claude/settings.json`, `.mcp.json`, `.env.example` and GitHub workflows without overwriting anything. Then open `CLAUDE.md` in the project and fill in the four "project facts" lines. Commit.

No local clone? In a Claude Code session on the project, ask: "Copy everything from `templates/project-bootstrap/` in HMalepe/holiday-ai-operating-system into this repo, without overwriting existing files."

Start with the project you're actively shipping, not the one you'd like to tidy.

## 3. ChatGPT setup (25 min)

Open `chatgpt/README.md`, then:

- [ ] Settings > Personalization: paste both blocks from `chatgpt/personalization.md` (2 min)
- [ ] Create the 5 Projects from `chatgpt/projects/`; paste instructions, upload the files listed (3 min each)
- [ ] Create the 5 Custom GPTs from `chatgpt/custom-gpts/` (3 min each); start with Architecture Reviewer and Programming Tutor
- [ ] Keep `chatgpt/deep-research-prompts.md` open in a tab

Skip any feature your plan doesn't show.

## 4. Connections (10 min, only what you need)

- [ ] **Supabase MCP:** edit `.mcp.json`, replace `YOUR_PROJECT_REF`, start Claude Code, run `/mcp` and authenticate. It starts read-only (`read_only=true`); leave it that way until you have a reason.
- [ ] **Vercel MCP:** run `/mcp`, authenticate `vercel`.
- [ ] **Playwright MCP:** needs Node; first run downloads a browser. Used by `/holiday-os:ui-critique` and `qa-gate`.
- [ ] Don't add more servers until one solves a real problem you've hit.

## 5. Optional CI review (5 min)

`.github/workflows/quality-gate.yml` works as-is. For `claude-review.yml`, add a repo secret `ANTHROPIC_API_KEY` (or run `claude setup-token` and add `CLAUDE_CODE_OAUTH_TOKEN`, then swap the commented line). No secret, no review; delete the file if you don't want it.

## 6. Make it a habit

- [ ] Put a recurring Friday 20-minute slot in your calendar for `workflows/weekly-os-review.md`.
- [ ] Next feature you build: run the pipeline tier from `workflows/cross-model-pipeline.md` and note what hurts in the friction log.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Skills don't appear | `/plugin` > check `holiday-os` is enabled; run `/reload-plugins` or restart the session |
| Guard hook blocks something legitimate | Read the reason it prints; for a one-off, run the command yourself in a terminal. For a rule that's wrong, edit `scripts/hooks/guard.py` and add a test in `tests/test_guard.py` |
| Hook seems silent | Check `python3` is on PATH; the hook fails open by design, so a broken hook never blocks work |
| ChatGPT rejects a paste | Instructions have length limits that change; trim the Extras and examples first |
