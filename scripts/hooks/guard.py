#!/usr/bin/env python3
"""PreToolUse guard for the Holiday AI operating system.

Reads the hook JSON from stdin and returns a decision:

* DENY  - secrets: reading or writing .env / key files, dumping env vars.
* ASK   - one-way doors: force pushes, hard resets, recursive deletes,
          destructive SQL, production deploys, publishing packages.
* (nothing) - everything else goes through the normal permission flow.

Design rules:
* Fail open. If the input can't be parsed, exit 0 with no decision, so a bug
  here never bricks a session.
* One approach per hook: exit 0 + JSON on stdout (no exit-code 2).
"""
import json
import os
import re
import sys

SECRET_PATH_PATTERNS = [
    r"(^|/)\.env($|\.(?!example$|sample$|template$)[^/]*$)",  # .env, .env.local ...
    r"\.(pem|key|p12|pfx|keystore)$",
    r"(^|/)id_(rsa|ed25519|ecdsa)(\.pub)?$",
    r"(^|/)credentials\.json$",
    r"(^|/)\.aws/credentials$",
    r"(^|/)\.npmrc$",
    r"(^|/)service[-_]?account.*\.json$",
]

FILE_TOOLS = {"Read", "Edit", "Write", "MultiEdit", "NotebookEdit"}

# (regex, reason) - checked against the Bash command text.
BASH_DENY = [
    (
        r"\b(cat|less|more|head|tail|bat|type|grep|rg|awk|sed|cp|mv|scp|base64|xxd|strings)\b[^|;&]*"
        r"(\s|/)\.env(?!\.(example|sample|template)\b)(\.[A-Za-z0-9_-]+)?(\s|$|\"|')",
        "Reading an .env file would put secrets into the conversation.",
    ),
    (
        r"^\s*(printenv|env|export\s+-p|set)\s*(\||$|;|&)",
        "Dumping the environment would print secrets. Print the one variable name you need (and check only that it is set).",
    ),
]

BASH_ASK = [
    (r"\bgit\s+push\b[^;&|]*(--force\b|--force-with-lease\b|\s-f(\s|$))", "Force push rewrites shared history."),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard throws away uncommitted work."),
    (r"\bgit\s+clean\b[^;&|]*-[a-zA-Z]*f", "git clean -f permanently deletes untracked files."),
    (r"\bgit\s+(branch\s+-D|push\s+\S+\s+--delete|push\s+\S+\s+:)", "Deleting a branch can lose commits."),
    (r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r|--recursive\s+--force|--force\s+--recursive)\b", "Recursive force delete."),
    (r"\b(drop|truncate)\s+(table|database|schema)\b", "Destructive SQL."),
    (r"\bdelete\s+from\s+\w+(\s*;|\s*$|\s*\")", "DELETE without a WHERE clause."),
    (r"\bsupabase\s+(db\s+reset|db\s+push|projects\s+delete|migration\s+repair)\b", "Supabase command that changes or resets a database."),
    (r"\bvercel\b[^;&|]*(--prod\b|--production\b)", "Production deploy."),
    (r"\bvercel\s+(env\s+rm|remove|rm)\b", "Removes Vercel resources."),
    (r"\bnpm\s+publish\b", "Publishing a package is public and hard to undo."),
    (r"\bgh\s+(repo\s+delete|release\s+delete|pr\s+merge)\b", "GitHub action that is hard to undo."),
    (r"\bcurl\b[^|;&]*\|\s*(sudo\s+)?(ba)?sh\b", "Piping a download straight into a shell."),
    (r"\bchmod\s+-R\s+777\b", "World-writable permissions."),
]


def emit(decision: str, reason: str) -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": decision,
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    sys.stdout.write("\n")


def is_secret_path(path: str) -> bool:
    norm = path.replace("\\", "/")
    return any(re.search(p, norm) for p in SECRET_PATH_PATTERNS)


def evaluate(payload: dict):
    """Return (decision, reason) or None. Pure function so it can be unit tested."""
    tool = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}

    if tool in FILE_TOOLS:
        path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        if path and is_secret_path(path):
            return (
                "deny",
                f"Blocked by holiday-os guard: {os.path.basename(path)} holds secrets. "
                "Use .env.example for variable names and set real values in the host's environment settings.",
            )
        return None

    if tool == "Bash":
        cmd = tool_input.get("command") or ""
        for pattern, reason in BASH_DENY:
            if re.search(pattern, cmd, re.IGNORECASE):
                return ("deny", f"Blocked by holiday-os guard: {reason}")
        for pattern, reason in BASH_ASK:
            if re.search(pattern, cmd, re.IGNORECASE):
                return ("ask", f"holiday-os guard: {reason} Confirm the exact target before running.")
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        result = evaluate(payload)
    except Exception:  # fail open
        return 0
    if result:
        emit(*result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
