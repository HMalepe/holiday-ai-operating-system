# Workflow: Research deep dive

For decisions worth more than an hour of thought: which niche, which vendor, whether to build X, how to price. Uses two independent research runs so one model's blind spots don't become your decision.

## Steps

1. **Frame the decision (10 min).** Write: the decision, the options, what evidence would change your mind, and the deadline. Research without a decision is reading.
2. **Run A: ChatGPT Deep research.** Pick the matching prompt from `chatgpt/deep-research-prompts.md`. Let it run; save the report.
3. **Run B: Claude.** In Claude (chat with web search, or a Claude Code session using the `research-analyst` subagent) run the same question with the same output format. Don't show it Run A.
4. **Triangulate.** Build a table: claim, Run A, Run B, source quality. Agreement across independent sources is signal; a claim in only one run is a hypothesis.
5. **Verify the load-bearing facts yourself.** Open the primary source for the 3 facts the decision depends on most (pricing page, regulator text, vendor docs). Note the date.
6. **Decide with the framework.** Classify the door, apply the 70% rule, score if close (`intelligence/decision-framework.md`).
7. **Write it down.** Save `docs/research/<topic>.md` in the project: decision, evidence table, what would change your mind, review date.
8. **Cheapest test.** End with one thing you can do this week to test the riskiest assumption before spending real time.

## Output template

```
# <Topic>: decision <YYYY-MM-DD>
Decision:
Options considered:
Recommendation (confidence high/medium/low):
Evidence: | Claim | A | B | Primary source (date) |
Disagreements between runs and how resolved:
Risks / what would change my mind:
Cheapest test this week:
Review date:
```

## Quality bar

- Every market fact has a source and a date. "No reliable data found" is an acceptable finding; an invented number is not.
- Separate FACT from INFERENCE from OPINION.
- Prefer South African sources and ZAR figures where the product is for South Africa; convert and note the rate and date.
