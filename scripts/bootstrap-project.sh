#!/usr/bin/env bash
# Wire a project into the Holiday AI OS.
#
#   scripts/bootstrap-project.sh /path/to/project          # everything, never overwrites
#   scripts/bootstrap-project.sh /path/to/project --no-ci  # skip GitHub workflows
#   scripts/bootstrap-project.sh /path/to/project --no-mcp # skip .mcp.json
#
# Copies templates/project-bootstrap/* into the project. Existing files are left
# alone and reported, so it is safe to re-run.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="$here/templates/project-bootstrap"
target="${1:-}"
[ -n "$target" ] && [ -d "$target" ] || { echo "usage: $0 <project-dir> [--no-ci] [--no-mcp] [--no-cursor]" >&2; exit 1; }
shift || true

skip_ci=0; skip_mcp=0; skip_cursor=0
for flag in "$@"; do
  case "$flag" in
    --no-ci) skip_ci=1 ;;
    --no-mcp) skip_mcp=1 ;;
    --no-cursor) skip_cursor=1 ;;
    *) echo "unknown flag: $flag" >&2; exit 1 ;;
  esac
done

copied=0; kept=0
while IFS= read -r -d '' file; do
  rel="${file#"$src"/}"
  case "$rel" in
    .github/*) [ "$skip_ci" = 1 ] && continue ;;
    .mcp.json) [ "$skip_mcp" = 1 ] && continue ;;
    .cursor/*) [ "$skip_cursor" = 1 ] && continue ;;
  esac
  dest="$target/$rel"
  if [ -e "$dest" ]; then
    echo "kept    $rel (already exists)"; kept=$((kept+1))
  else
    mkdir -p "$(dirname "$dest")"; cp "$file" "$dest"
    echo "created $rel"; copied=$((copied+1))
  fi
done < <(find "$src" -type f -print0 | sort -z)

# Make sure secrets stay out of git.
gi="$target/.gitignore"
touch "$gi"
for line in ".env" ".env.*" "!.env.example" "CLAUDE.local.md" ".claude/settings.local.json"; do
  grep -qxF "$line" "$gi" || { echo "$line" >> "$gi"; echo "gitignore + $line"; }
done

echo
echo "Done: $copied created, $kept kept."
cat <<'EOF'

Next (2 minutes):
  1. Edit CLAUDE.md: fill in the project name, core journey, data ownership, external services.
  2. If you kept .mcp.json: replace YOUR_PROJECT_REF in the Supabase URL (or delete that server).
  3. Commit. The next Claude Code session in this repo offers to install the holiday-os plugin
     (from .claude/settings.json), which brings the skills, subagents and guard hook.
  4. CI: add repo secret ANTHROPIC_API_KEY (or CLAUDE_CODE_OAUTH_TOKEN) only if you keep claude-review.yml.
EOF
