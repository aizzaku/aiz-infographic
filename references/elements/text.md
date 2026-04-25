# Text — Typography Atoms

All text atoms. References the style's CSS variables so swapping styles changes everything.

## Atoms

| Atom | Role | Style tokens |
|------|------|--------------|
| `.hero-title` | Single biggest text on the page | display font, 48–64px, uppercase, gradient text |
| `.section-title` | Structural section headers | body font bold, 20–28px, uppercase |
| `.card-title` | Card / block headers | body font bold, 16–20px, uppercase |
| `.item-label` | Row labels, axis labels | body font bold, 13–15px, uppercase |
| `.body` | Paragraph copy | body font regular, 14–16px, sentence case |
| `.caption` | Footnotes, sources | body font regular, 11–13px, sentence case |
| `.badge` | Category / status tag | body font bold, 10–12px, uppercase |
| `.metric-value` | Big numbers | display font, 36–48px, tabular-nums |
| `.metric-label` | Metric sub-labels | body font regular, 12–13px, sentence case |

## HTML / CSS pattern

```html
<h1 class="hero-title gradient-text">Token Economics</h1>
<h2 class="section-title">Distribution</h2>
<h3 class="card-title">Community</h3>
<p class="body">40% of total supply allocated to community rewards over 24 months.</p>
<span class="badge">Vesting</span>
<div class="metric">
  <div class="metric-value">1,000,000,000</div>
  <div class="metric-label">Total supply</div>
</div>
```

```css
.hero-title {
  font: 400 56px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin: 0;
}

.section-title {
  font: 700 24px/1.1 'Montserrat', sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--text-primary);
  margin: 0 0 var(--gap-element);
}

.card-title {
  font: 700 18px/1.2 'Montserrat', sans-serif;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--text-primary);
}

.item-label {
  font: 700 14px/1.2 'Montserrat', sans-serif;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--text-secondary);
}

.body {
  font: 400 15px/1.5 'Montserrat', sans-serif;
  color: var(--text-secondary);
}

.caption {
  font: 400 12px/1.4 'Montserrat', sans-serif;
  color: var(--text-muted);
}

.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  background: color-mix(in srgb, var(--accent-1) 12%, transparent);
  border: 1px solid color-mix(in srgb, var(--accent-1) 30%, transparent);
  color: var(--accent-1);
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.metric-value {
  font: 400 44px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.04em;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}

.metric-label {
  font: 400 12px/1.3 'Montserrat', sans-serif;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.gradient-text {
  background: linear-gradient(30deg, var(--accent-1), var(--accent-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}
```

## Variations

- **Partial gradient**: wrap one key word in `<span class="gradient-text">`.
- **Caps body**: never. Body stays sentence case regardless of emphasis need — use bold weight instead.
- **Accent body**: for keyword highlights, wrap in `<span style="color: var(--accent-1); font-weight: 700;">`.

## Rules

- Never use three or more distinct sizes within a single section.
- Never mix uppercase and title-case headers in the same infographic.
- Always use tabular-nums for number-heavy columns (`font-variant-numeric: tabular-nums;`).
- Hero title appears exactly once per infographic.
