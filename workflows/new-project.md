# Workflow: New project

Goal: idea to a live v0 URL fast, without building the wrong thing.

**Time-box:** v0 live within 1-3 sessions. If it isn't, cut scope.

## Phase 0: Intake (10 min)
- [ ] Dump the idea in your own words, however rough.
- [ ] Agent restates it in one sentence. Correct it if wrong.

## Phase 1: Define (agent: `product-architect`)
- [ ] Problem, user, current alternative
- [ ] Quick competitor and substitute scan (`research-analyst`)
- [ ] The wedge: smallest version a real user would use this week
- [ ] Success metric + kill criteria (see `decision-framework.md`)
- [ ] Fill `templates/product-requirements.md`

**Gate 1:** I approve the PRD. No code before this.

## Phase 2: Design the build
- [ ] Data model, screens list, integrations needed
- [ ] Stack: default from `engineering/architecture-standards.md`, deviations written down
- [ ] Fill `templates/technical-specification.md`
- [ ] Security pre-check: what data, who can see it, what secrets (`security-standards.md`)

**Gate 2:** I approve the tech spec.

## Phase 3: Skeleton and deploy
- [ ] Create repo, `.gitignore` with `.env*`, project `CLAUDE.md` pointing to this repo
- [ ] Scaffold app, connect database, set env vars
- [ ] Deploy an empty-but-live version to a real URL
- [ ] Set up preview deployments

## Phase 4: Vertical slice
- [ ] Build the one core journey end to end (UI, API, data)
- [ ] Follow `workflows/feature-development.md` for the slice

## Phase 5: Harden and ship v0
- [ ] `agents/qa-engineer` and `agents/security-reviewer` pass
- [ ] Smoke checklist from `testing-standards.md`
- [ ] Deploy per `workflows/deployment.md`
- [ ] Put it in front of one real user within 48 hours

## Phase 6: Learn
- [ ] Write 5 lines: what worked, what hurt, what the user did, what's next
- [ ] Update this repo with any standard that failed me

## Anti-stall rule
If a phase takes more than twice its estimate, stop and ask: what's the smallest shippable slice?
