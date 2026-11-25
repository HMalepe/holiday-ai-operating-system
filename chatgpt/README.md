# ChatGPT kit

Paste-ready configuration for the ChatGPT side of the stack. ChatGPT is the **research, reasoning and independent-review layer**; Claude Code builds. Nothing here is automatic: ChatGPT can't read this repo by itself, so each item below is something you paste or upload once.

| File | Where it goes in ChatGPT | When |
|---|---|---|
| `personalization.md` | Settings > Personalization > Custom instructions | Once |
| `projects/*.md` | Create a Project per file; paste the instructions, upload the listed files | Once per project |
| `custom-gpts/*.md` | Explore GPTs > Create; paste name, description, instructions, starters | Once per GPT |
| `deep-research-prompts.md` | Start a chat, pick Deep research, paste a prompt | Whenever you research |
| `codex-review.md` | Codex (or a plain chat) as independent reviewer | After each Claude build |

Limits worth knowing (they change; check the editor if a paste is rejected): Custom GPT instructions allow roughly 8,000 characters, the Custom instructions fields in Personalization roughly 1,500 each. Files in this kit are written to fit.

Availability depends on your plan. Projects, Custom GPTs and Deep research are the core; Codex and agent-style features vary by plan and rollout, so use what your account actually shows and skip what it doesn't.

Never paste real secrets, customer data or phone numbers into ChatGPT. Use placeholders.
