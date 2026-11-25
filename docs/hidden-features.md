# Features most people never use

Only items checked against the current Claude Code docs and CLI (v2.1.x) are listed. Names and flags move fast; if something is missing, type `/` in a session or run `claude --help`.

## Claude Code

| Feature | What it does | Try it |
|---|---|---|
| **Plan mode** | Claude reads and plans without editing anything; you approve before it builds. Cheapest way to avoid a wrong build. | `claude --permission-mode plan` or cycle modes with Shift+Tab |
| **`/simplify`** | Four parallel review agents check your changed code for reuse, simplification and efficiency, then apply fixes. | `/simplify` after a feature |
| **`/security-review`** | Reviews your branch diff for injection, auth issues and data exposure. | `/security-review` before a PR |
| **`/review`** (alias of `/code-review`) | Reviews the current diff or a PR number; can comment on the PR. | `/review 42` |
| **`/ultrareview`** | Deep multi-agent review in a cloud sandbox. | `/ultrareview <PR or branch>` |
| **`/batch`** | Plans a large change, splits it into 5-30 independent units and runs them in parallel. | `/batch rename X to Y across the repo` |
| **`/rewind`** (aliases `/checkpoint`, `/undo`) | Roll back the conversation and/or the code to an earlier point. Lets you be bold. | `/rewind` |
| **`/context`** | Shows what is eating your context window and how to trim it. | `/context` when answers get worse |
| **`/btw`** | Ask a side question without polluting the main conversation. | `/btw what does RLS stand for?` |
| **`/loop`, `/schedule`** | Repeat a prompt while the session is open, or schedule recurring runs. | `/loop 10m check the deploy` |
| **Worktrees** | Parallel agents on separate branches. | `claude -w feature-name` (see `workflows/parallel-worktrees.md`) |
| **Teleport** | Pull a cloud (web) session into your terminal, with its branch and conversation. | `/teleport` or `claude --teleport` |
| **Headless mode** | Run Claude in scripts and CI: `-p` prints the answer and exits. Pair with `--output-format json` and `--max-budget-usd` as a cost cap. | `claude -p "list TODOs in src/"` |
| **`--agents`** | Define throwaway subagents as JSON for a single run. | `claude --agents '{...}'` |
| **`--strict-mcp-config`** | Use only the MCP servers you pass, ignoring the rest. Keeps context lean. | `claude --mcp-config mcp.json --strict-mcp-config` |
| **`--add-dir`** | Give a session access to a second folder or repo (e.g. this AI OS repo). | `claude --add-dir ../holiday-ai-operating-system` |
| **Hooks** | Deterministic code on events (before a tool runs, on session start). Instructions are requests; hooks are enforcement. | `/hooks`, and see `scripts/hooks/guard.py` |
| **Subagents** | Specialists with their own context window and tool limits, so exploration doesn't clutter your main session. | `/agents` |
| **Plugins and marketplaces** | Package skills, agents and hooks so every project gets them. | `/plugin` |
| **Skills** | Reusable procedures Claude loads when relevant, or you call as `/name`. | `/holiday-os:qa-gate` |

## Claude Code on the web

- Sessions keep running after you close the tab. Start a long task, leave, review the PR later.
- Per-project `.claude/settings.json` can auto-enable the `holiday-os` plugin for every session on that repo (the bootstrap kit does this).
- Run several sessions on one repo, each on its own branch, as your parallel workforce.

## ChatGPT

| Feature | Why it matters |
|---|---|
| **Projects** | Persistent instructions and files per area of work, so you stop re-explaining. |
| **Deep research** | Multi-source cited reports. Give it a decision to inform and an output format (`chatgpt/deep-research-prompts.md`). |
| **Custom GPTs** | Reusable specialists with fixed instructions and knowledge (`chatgpt/custom-gpts/`). |
| **Data analysis** | Upload CSVs and spreadsheets; it runs Python to analyse and chart them. |
| **Codex** | A second coding agent for independent review (plan-dependent; see `chatgpt/codex-review.md`). |

## The leverage nobody sets up

1. **Enforcement beats instruction.** A line in CLAUDE.md is a suggestion; a PreToolUse hook is a rule.
2. **Cross-model review.** The model that wrote it shouldn't approve it.
3. **A friction log.** Every re-explanation is a missing line somewhere. Fix it once.
4. **One source of truth.** This repo, loaded by a plugin, instead of five slightly different copies of your preferences.
