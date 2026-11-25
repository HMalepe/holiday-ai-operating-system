# Backend standards

## API design

- Resource-oriented routes, plural nouns: `GET /api/leads`, `POST /api/leads`.
- Validate every input at the boundary with a schema. Reject early with a clear 400.
- Consistent response shapes:

```json
{ "data": { }, "error": null }
{ "data": null, "error": { "code": "VALIDATION_FAILED", "message": "…", "details": [] } }
```

- Correct status codes: 200/201 success, 400 validation, 401 unauthenticated, 403 unauthorised, 404 not found, 409 conflict, 429 rate limited, 500 unexpected.
- Pagination on every list endpoint (cursor preferred). Never return unbounded lists.

## Data

- Schema changes only via migrations, committed to git. No manual edits to production schema.
- Every table: `id`, `created_at`, `updated_at`, and an owner column where data is per-user.
- Use foreign keys and constraints. The database should refuse bad data, not just the app.
- Index columns used in filters and joins; check query plans for anything slow.
- Soft-delete only where history matters; otherwise delete for real (POPIA data-minimisation).

## Reliability

- **Idempotency:** webhooks and retries must be safe to replay. Store event IDs and skip duplicates.
- **Timeouts and retries:** every outbound call has a timeout; retry with exponential backoff and a cap.
- **Queues for slow work:** anything over ~5 seconds leaves the request path.
- **Graceful failure:** a failed integration degrades the feature, not the whole app.

## Observability

- Structured logs (JSON) with a request ID. Log events and IDs, never secrets or full personal data.
- Errors reported somewhere you will actually see them (Vercel logs at minimum, an alert for critical paths).
- A `/api/health` endpoint for workers and bots.

## Integrations (WhatsApp, Twilio, payments)

- Verify webhook signatures before parsing the body.
- Respond 200 quickly, process asynchronously.
- Keep message templates and copy in config or the database, not hard-coded in handlers.
- Respect platform rules: opt-in, 24-hour windows, template approval.

## Done means

Inputs validated, errors handled and logged, migration committed, idempotent where needed, secrets in env, tested against a real or realistic payload.
