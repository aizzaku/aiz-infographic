# vercel-dark — Developer Utility Style

Source: Vercel brand system — geist.vercel.app, vercel.com
Concept: Developer utility black. Pure white on pure black. Infrastructure as aesthetic. Everything reads like a deployment log or build output. Maximum contrast, zero warmth.

```
canvas-fit: [bento-box, dashboard, editorial]
```

## When to use

- Vercel product, deployment, or infrastructure infographics
- Frontend deployment metrics, build analytics
- Any content explicitly requesting the Vercel brand style
- Auto-selected when content is primarily about Vercel, Next.js deployments, or Vercel infrastructure

## CSS variables

```css
:root {
  /* canvas — true black; the only style in the system that uses #000 */
  --canvas:        #000000;
  --panel:         #111111;
  --elevated:      #1A1A1A;

  /* no accent color */
  --accent-1:      #EDEDED;   /* set to primary text to avoid broken color-mix calls */
  --accent-2:      #888888;
  --on-accent:     #000000;

  /* text */
  --text-primary:   #EDEDED;
  --text-secondary: #888888;
  --text-muted:     #444444;

  /* borders */
  --border-default: #1A1A1A;   /* slightly warmer than OpenAI's rgba — more visible */
  --border-subtle:  #111111;

  /* semantic — no color */
  --positive: #EDEDED;
  --negative: #888888;

  /* spacing — information-rich but structured */
  --gap-section:   24px;
  --gap-element:   16px;
  --gap-card:      12px;
  --pad-container: 20px;

  /* radius — minimal, less than OpenAI */
  --radius-card:  4px;
  --radius-pill:  2px;
  --radius-btn:   2px;
}
```

## Typography

Geist and Geist Mono. Falls back to system-ui and monospace.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap">
<!-- Geist not on Google Fonts — use Inter as nearest equivalent -->
<!-- For local installs: @font-face with Geist from vercel.com/font -->
```

| Role | Font | Weight | Case | Size | Notes |
|------|------|--------|------|------|-------|
| Hero | Inter (Geist) | 500 | as-is | 40-56px | letter-spacing -0.02em |
| Label | Inter | 500 | UPPERCASE | 11px | letter-spacing 0.08em, text-secondary |
| Slug / path | JetBrains Mono (Geist Mono) | 400 | as-is | 13px | text-primary |
| Body | Inter | 400 | Sentence | 14px | line-height 1.5, text-secondary |
| Metadata | Inter | 400 | Sentence | 11px | text-muted |

**Font weight 500 for all labels** — not 400, not 700. Medium only. No Bebas Neue or display-weight fonts.

## Decorative DNA

### Square status markers (signature element)

Never circles for status. Squares are the Vercel tell:

```css
.status-marker {
  width: 8px;
  height: 8px;
  border-radius: 0;          /* square — never circle */
  background: var(--text-primary);
  flex-shrink: 0;
}
.status-marker-secondary { background: var(--text-secondary); }
.status-marker-muted     { background: var(--text-muted); }
```

### Deployment-log copy

Slugs, hashes, paths, semver strings as structural content:

```html
<div class="deploy-entry">
  <span class="status-marker"></span>
  <span class="deploy-slug">prod-2026-05-20</span>
  <span class="deploy-arrow">-></span>
  <span class="deploy-state">live</span>
  <span class="deploy-time">14:22:08</span>
</div>

<style>
.deploy-entry {
  display: flex;
  align-items: center;
  gap: 8px;
  font: 400 13px/1 'JetBrains Mono', monospace;
  color: var(--text-secondary);
  padding: 8px 0;
  border-bottom: 1px solid var(--border-default);
}
.deploy-slug  { color: var(--text-primary); }
.deploy-arrow { color: var(--text-muted); }
.deploy-state { color: var(--text-primary); }
.deploy-time  { margin-left: auto; color: var(--text-muted); }
</style>
```

### Build status pattern

```html
<div class="build-status">
  <span class="status-marker"></span>
  <span class="build-label">READY</span>
  <span class="build-sep">·</span>
  <span class="build-ts">2026-05-20T14:22:08Z</span>
</div>
```

### Cards

```css
.card {
  background: var(--panel);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-card, 4px);
  padding: 16px;
}
```

### Hairline dividers

```css
.divider {
  border: none;
  border-top: 1px solid var(--border-default);
  margin: 0;
}
```

## Layout rules

```
alignment:   left-aligned
hero:        large slug or build path in monospace — the aesthetic IS the output
sections:    hairline borders 1px #1A1A1A, tight spacing
cards:       minimal, hard edges, 4px max radius
grid:        clean columns, no bento complexity — grid-pure
density:     information-rich but not crowded — structured, not dense
```

## Gradient text

Disabled entirely.

## Style verification checklist

- [ ] Canvas is `#000000` — true black, the differentiator from OpenAI's `#0A0A0A`
- [ ] Square status markers — no circles, no dots
- [ ] Weight 500 for labels — not 400, not 700
- [ ] Deployment-log aesthetic: slugs, hashes, paths as content
- [ ] Max 4px border-radius
- [ ] No color, no gradient, no glow

## Forbidden

No color accent. No rounded corners above 4px. No gradient text. No glow or shadow. No warmth. No Bebas Neue or heavy display fonts. No decorative icons (functional only, 16px, text-secondary).
