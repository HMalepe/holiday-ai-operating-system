#!/usr/bin/env python3
"""Health check for the Holiday AI operating system repo.

    python3 scripts/validate.py

Checks (exit 1 if any fail):
  * JSON files parse; plugin and marketplace names agree
  * every agent and skill has valid frontmatter (name matches file/folder, description present)
  * shell scripts have a shebang and are executable
  * relative markdown links resolve
  * repo paths mentioned in README / CLAUDE / AGENTS / chatgpt / docs exist
  * no key-shaped secrets in text files
"""
import json
import os
import re
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules"}
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def text_files():
    for p in ROOT.rglob("*"):
        if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP_DIRS):
            if p.suffix.lower() in {".md", ".mdc", ".json", ".yml", ".yaml", ".sh", ".py", ".txt", ""}:
                yield p


def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def check_json():
    for p in ROOT.rglob("*.json"):
        if set(p.relative_to(ROOT).parts) & SKIP_DIRS:
            continue
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            err(f"{p.relative_to(ROOT)}: invalid JSON ({e})")
    try:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        names = [x["name"] for x in market["plugins"]]
        if plugin["name"] not in names:
            err(f"marketplace.json lists {names} but plugin.json name is {plugin['name']!r}")
    except Exception as e:  # noqa: BLE001
        err(f"plugin/marketplace check failed: {e}")


def check_agents_and_skills():
    for p in sorted((ROOT / "agents").glob("*.md")):
        fm = frontmatter(p)
        if fm is None:
            err(f"{p.relative_to(ROOT)}: missing frontmatter")
            continue
        if fm.get("name") != p.stem:
            err(f"{p.relative_to(ROOT)}: name {fm.get('name')!r} != file name {p.stem!r}")
        if not fm.get("description"):
            err(f"{p.relative_to(ROOT)}: missing description")
        if not fm.get("tools"):
            err(f"{p.relative_to(ROOT)}: missing tools (agents should list least-privilege tools)")
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        fm = frontmatter(p)
        if fm is None:
            err(f"{p.relative_to(ROOT)}: missing frontmatter")
            continue
        if fm.get("name") != p.parent.name:
            err(f"{p.relative_to(ROOT)}: name {fm.get('name')!r} != folder {p.parent.name!r}")
        if not fm.get("description"):
            err(f"{p.relative_to(ROOT)}: missing description")


def check_scripts():
    for p in ROOT.rglob("*.sh"):
        if set(p.relative_to(ROOT).parts) & SKIP_DIRS:
            continue
        first = p.read_text(encoding="utf-8").splitlines()[:1]
        if not first or not first[0].startswith("#!"):
            err(f"{p.relative_to(ROOT)}: missing shebang")
        if not (p.stat().st_mode & stat.S_IXUSR):
            err(f"{p.relative_to(ROOT)}: not executable (chmod +x)")
    guard = ROOT / "scripts/hooks/guard.py"
    if not (guard.stat().st_mode & stat.S_IXUSR):
        err("scripts/hooks/guard.py: not executable")


LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
REPO_PATH = re.compile(
    r"`((?:intelligence|engineering|agents|workflows|templates|docs|chatgpt|scripts|skills|hooks)/[A-Za-z0-9_./-]+\.(?:md|mdc|json|sh|py|yml))`"
)
PATH_CHECKED = ["README.md", "CLAUDE.md", "AGENTS.md"]


def check_links_and_paths():
    for p in text_files():
        if p.suffix != ".md":
            continue
        rel = p.relative_to(ROOT)
        # templates and skills describe paths in *other* projects; don't check those.
        text = p.read_text(encoding="utf-8")
        in_code = False
        for m in LINK.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#")[0]
            if target and not (p.parent / target).exists():
                err(f"{rel}: broken link -> {target}")
        checked = str(rel) in PATH_CHECKED or rel.parts[0] in {"chatgpt", "docs"}
        if checked:
            for m in REPO_PATH.finditer(text):
                if not (ROOT / m.group(1)).exists():
                    err(f"{rel}: mentions missing file {m.group(1)}")


SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9_-]{24,}", "API key (sk-...)"),
    (r"gh[pousr]_[A-Za-z0-9]{30,}", "GitHub token"),
    (r"github_pat_[A-Za-z0-9_]{30,}", "GitHub fine-grained token"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key"),
    (r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", "private key"),
    (r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.", "JWT"),
]


def check_secrets():
    for p in text_files():
        rel = p.relative_to(ROOT)
        if str(rel) == "scripts/validate.py":
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pat, label in SECRET_PATTERNS:
            if re.search(pat, text):
                err(f"{rel}: looks like a {label}")


def main() -> int:
    check_json()
    check_agents_and_skills()
    check_scripts()
    check_links_and_paths()
    check_secrets()
    if errors:
        print(f"FAIL: {len(errors)} problem(s)")
        for e in errors:
            print(f"  - {e}")
        return 1
    n_agents = len(list((ROOT / "agents").glob("*.md")))
    n_skills = len(list((ROOT / "skills").glob("*/SKILL.md")))
    print(f"OK: {n_agents} agents, {n_skills} skills, JSON valid, links resolve, no secrets found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
