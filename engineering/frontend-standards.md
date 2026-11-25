# Frontend standards

## UX baseline

- **Mobile-first.** Design at 375px, then scale up. Tap targets at least 44px.
- Every screen defines four states: **loading, empty, error, success.** No blank panels.
- One primary action per screen. Destructive actions need confirmation and are visually distinct.
- Forms: inline validation, preserve input on error, disable the submit button while pending.
- Money, dates, numbers: format for South Africa (ZAR, `en-ZA`), show currency symbols explicitly.

## Code

- TypeScript strict mode. No `any` without a comment explaining why.
- Components are small and single-purpose. Logic in hooks or utils, not inline in JSX.
- Server Components by default; add `"use client"` only for interactivity.
- Data fetching on the server where possible; client fetching via one consistent library.
- State: local first, then URL, then context. Add a global store only with a demonstrated need.
- Styling: Tailwind utility classes, shared tokens (colors, spacing, radius) in the config. No one-off magic numbers.
- Validate user input with a schema (zod) shared with the backend where practical.

## Accessibility (minimum bar)

- Semantic HTML: buttons are `<button>`, links are `<a>`.
- Every input has a label. Every image has alt text (or `alt=""` if decorative).
- Colour contrast at least 4.5:1 for body text. Don't rely on colour alone.
- Fully keyboard operable; visible focus states.

## Performance budget

- Largest Contentful Paint under 2.5s on a mid-range phone over 4G.
- Images through the framework image component, sized and lazy loaded.
- No dependency over ~50 KB gzipped without a reason in the PR.

## Design quality

- Pick a clear visual direction (type, colour, spacing scale) before building screens; avoid default-template look.
- Real copy, not lorem ipsum. Real data shapes in mock states.
- Check at 375px, 768px and desktop before calling it done.

## Done means

Works on phone and desktop, all four states handled, keyboard usable, no console errors, Lighthouse accessibility 90+.
