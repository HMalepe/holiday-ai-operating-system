---
name: ui-critique
description: Critique a screen, page or flow for hierarchy, mobile usability, states, accessibility and design distinctiveness, with concrete fixes. Use when a UI feels off, before shipping a page, or when asked to review design.
---

# UI critique

Target: `$ARGUMENTS` (URL, route or component path). If it is a running app, open it in a browser tool (Playwright MCP or Claude in Chrome) at **375px, 768px and 1280px** and screenshot each. If you cannot run it, review the code and say so.

## Checklist

1. **Hierarchy.** What is the one primary action? Is it obvious in 3 seconds? Is anything competing?
2. **Mobile.** Tap targets 44px or more, no horizontal scroll, thumb-reachable primary action, readable at arm's length.
3. **Four states.** Loading, empty, error, success. Find each in the code and check it renders sensibly.
4. **Forms.** Inline validation, input preserved on error, submit disabled while pending, labels present.
5. **Accessibility.** Semantic elements, labels, alt text, contrast 4.5:1, keyboard path and visible focus.
6. **Content.** Real copy not lorem ipsum, ZAR and `en-ZA` formats, plain language.
7. **Distinctiveness.** Does it look like a default template? Name the specific choices (type, colour, spacing, motion) that would give it an identity.

## Output

- Verdict in one line.
- Table: issue, where, why it matters, fix (code-level where possible), effort S/M/L. Sort by impact.
- "Quick wins under 30 minutes" (max 5).
- If asked to apply fixes, do the quick wins first and re-screenshot to prove the change.
