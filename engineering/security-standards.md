# Security standards

## Secrets

- Never commit secrets, tokens, `.env` files or private keys. `.env*` in `.gitignore` from the first commit.
- Secrets live in the host's environment settings (Vercel, Railway, Supabase). Rotate immediately if one leaks, then purge from git history.
- Separate keys per environment. Service-role keys are server-only, never in client bundles or `NEXT_PUBLIC_*` variables.
- Never paste real credentials into an AI chat.

## Authentication and authorisation

- Use the provider's auth (Supabase Auth) rather than rolling your own.
- **Row Level Security on every table**, with policies written and tested. "RLS off" is a defect.
- Authorise on the server for every request: check who the user is and whether they own the resource. Hiding a button is not security.
- Least privilege: separate roles for admin, staff, customer.

## Input and output

- Validate and sanitise all external input (forms, query strings, webhooks, file uploads).
- Parameterised queries only. No string-built SQL.
- Escape output; never render untrusted HTML. Set sensible CORS and security headers.
- File uploads: check type and size, store outside the web root or in private storage buckets, serve via signed URLs.

## Webhooks and third parties

- Verify signatures on every inbound webhook.
- Rate limit public endpoints and auth routes.
- Treat all third-party responses as untrusted input.

## AI-specific risks

- **Prompt injection:** text from users, emails, web pages or documents can contain instructions. Never let it trigger tools with side effects (sending, deleting, paying) without a confirmation step.
- Never pass secrets or unnecessary personal data into prompts.
- Constrain what an AI feature can do: allow-listed tools, scoped credentials, output validation.

## Trading and financial tools

- Never store broker passwords or API secrets client-side. Server-side only, encrypted, minimum permissions.
- Any action that moves money or places orders requires an explicit confirmation showing the exact amounts and instruments.

## Personal data (POPIA)

- Collect only what's needed, state why, allow deletion on request.
- Keep personal data out of logs and analytics.
- Know where data is stored and who processes it.

## Dependencies

- Pin versions, review new packages (maintenance, downloads, licence), run `npm audit` before release.
- Remove unused packages.

## Done means

No secrets in repo, RLS verified, server-side authorisation checked, inputs validated, webhooks verified, dependencies audited.
