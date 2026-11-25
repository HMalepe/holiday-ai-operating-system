#!/usr/bin/env bash
# SessionStart hook: injects the compact brief into every session so the
# standards apply even in projects that never copied a CLAUDE.md snippet.
# stdout of a SessionStart hook is added to Claude's context.
root="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
brief="$root/intelligence/session-brief.md"
[ -f "$brief" ] && cat "$brief"
exit 0
