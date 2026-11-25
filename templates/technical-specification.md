# Technical Specification: <Project name>

**Status:** Draft / Approved   **PRD:** <link>   **Date:**

## 1. Summary
<What we're building and the approach in 3-5 lines.>

## 2. Stack
| Layer | Choice | Reason (required if not the default) |
|---|---|---|
| Frontend | | |
| Backend | | |
| Database / auth | | |
| Hosting | | |
| Integrations | | |

## 3. Architecture
<Diagram or bullet flow: client -> server -> database -> third parties.>

## 4. Data model
| Table | Key columns | Owner column | RLS policy summary |
|---|---|---|---|

Relationships and indexes:

## 5. API / contracts
| Method + path | Auth | Request | Response | Errors |
|---|---|---|---|---|

## 6. Screens and states
| Screen | Purpose | States (loading / empty / error / success) |
|---|---|---|

## 7. Integrations
| Service | Purpose | Auth method | Webhooks | Rate limits / rules |
|---|---|---|---|---|

## 8. Security and privacy
- Data stored and sensitivity:
- Who can read/write what:
- Secrets and where they live:
- POPIA considerations:
- Abuse cases (what a malicious user would try):

## 9. Reliability
- Idempotency and retry approach:
- Background jobs:
- Failure modes and degraded behaviour:

## 10. Testing plan
- Automated (critical paths):
- Manual smoke checklist:

## 11. Deployment
- Environments, env vars, migration plan, rollback:

## 12. Milestones
| Milestone | Definition of done | Estimate |
|---|---|---|

## 13. Decisions and trade-offs
| Decision | Alternatives | Why |
|---|---|---|

## 14. Open questions and risks
-
