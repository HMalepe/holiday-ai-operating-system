# Deep Research prompt pack

Use with ChatGPT's Deep research mode. Each prompt states the decision it informs, the output format and the evidence bar, which is what separates a useful report from a pile of links. Replace the `<...>` parts.

## 1. Competitor teardown

```
Decision this informs: whether to build <product> and how to position it.
Research the top 8 competitors and substitutes for <product/niche>, South Africa first, then global.
For each: who it serves, pricing in ZAR (state source and date), key features, what customers complain about (from reviews, forums, social), and the gap.
Output: comparison table, then 5 positioning gaps ranked by how underserved they are, then a recommendation (go / narrow / no-go) with the cheapest test I can run this week.
Evidence bar: primary sources preferred, every claim cited with date, separate FACT from INFERENCE, give confidence levels, and say "no reliable data" rather than guess.
```

## 2. Market sizing the honest way

```
Decision: is <niche> big enough to build for?
Estimate the number of reachable customers in South Africa and what they'd pay, bottom-up (count of businesses by segment x realistic adoption x price), not a top-down analyst percentage.
Show the maths, the assumptions and the sources for each input. Give a low / base / high case and the 3 assumptions the answer is most sensitive to.
Finish with the first 10 customers: where they hang out and how I'd reach them.
```

## 3. Technical due diligence on a tool

```
Decision: should I build on <tool/API/platform>?
Check: current pricing and the point where costs jump, rate limits, uptime and incident history, lock-in and export options, security posture and data location, approval or review steps, recent changelog direction, and alternatives.
Output: a one-page brief with a clear recommendation, a "what breaks first at 10x usage" section, and a fallback plan.
Use official docs and status pages; cite everything with dates.
```

## 4. Regulation scan

```
Decision: what must I comply with for <product> in South Africa?
Cover POPIA obligations (lawful processing, consent, retention, deletion, operator agreements, breach notification), plus any sector rules, FICA/ECTA/CPA where relevant, WhatsApp Business policy and payment provider rules.
Output: a practical checklist in plain language, what is mandatory vs best practice, and what needs a lawyer. State that this is research, not legal advice, and cite the primary legal sources.
```

## 5. Pricing study

```
Decision: how to price <offer>.
Find what comparable services charge in ZAR (setup vs monthly), how they package tiers, and what customers say about value for money.
Output: good/better/best structure with ranges and the logic for each (value delivered, cost to serve, competitor anchors), the discount I should never give, and an A/B test I can run in two weeks.
```

## 6. "What am I missing?" sweep

```
I'm building <project> with <stack>. Find what ordinary builders in this space don't know or don't do: unusual distribution channels, free tools or programs, platform features most people never enable, partnership or reseller angles, and failure modes that kill similar products.
Output: 10 non-obvious findings ranked by leverage for a solo builder, each with a source, why it matters, and the first action. Mark each as verified or speculative.
```

## 7. Learn-this-fast brief

```
I need to learn <topic> well enough to build <thing> in <time>.
Give: the 20% of concepts that unlock 80% of the work, in dependency order; the best primary resources for each (official docs first); the 5 mistakes beginners make; and a 5-day plan where each day ends with something running.
```
