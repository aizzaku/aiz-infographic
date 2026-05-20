# ash — Monochrome Editorial Style

Concept: Monochrome editorial. Color is noise. Every piece of information earns its place through size and weight.

## When to use

- Executive summaries and annual reports
- Editorial infographics where color would distract
- Research findings that need maximum credibility
- Content where the data itself must carry all visual weight

## CSS variables

```css
:root {
  /* canvas */
  --canvas:        #0E0E0E;   /* near-black, no color cast */
  --panel:         #0E0E0E;   /* same as canvas — sections breathe via spacing */

  /* 4 gray stops — use only these */
  --text-primary:   #D0D0D0;  /* primary values, headlines */
  --text-secondary: #888888;  /* labels, section headers */
  --text-muted:     #555555;  /* metadata, secondary text */
  --border-color:   #333333;  /* borders, dividers, structure */
  --on-accent:      #0E0E0E;

  /* accent — none. No color. */
  --accent-1: #D0D0D0;        /* set to primary gray to avoid broken color-mix */
  --accent-2: #888888;

  /* semantic — kept as desaturated as viable */
  --positive: #D0D0D0;        /* no green in ash; use weight/size instead */
  --negative: #555555;        /* no red in ash; use weight/size instead */

  /* spacing — generous, Ash breathes */
  --gap-section:   48px;
  --gap-element:   24px;
  --gap-card:      16px;
  --pad-container: 32px;

  /* radius — minimal */
  --radius-card:  0px;
  --radius-pill:  2px;
  --radius-btn:   2px;
}
```

## Typography

Sans-serif for headlines and large numerics. Monospace for codes and IDs. Small-caps for category labels.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=JetBrains+Mono:wght@400;700&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero metric / large number | Inter | 900 | as-is | 48-96px |
| Section header | Inter | 700 | SMALL-CAPS | 16-20px |
| Card title | Inter | 700 | UPPERCASE | 13-15px |
| Body | Inter | 400 | Sentence | 14-15px |
| Code / ID | JetBrains Mono | 400 | as-is | 11-13px |
| Caption | Inter | 400 | Sentence | 11-12px |

### Large numeric (primary visual element)

One large number per section. At least 2x body size.

```html
<div class="ash-metric">
  <div class="ash-metric-label">REVENUE</div>
  <div class="ash-metric-value">$4.2M</div>
</div>

<style>
.ash-metric { display: flex; flex-direction: column; gap: 4px; }
.ash-metric-label {
  font: 700 11px/1 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.10em;
  color: #888888;
  font-variant-caps: small-caps;
}
.ash-metric-value {
  font: 900 48px/1 'Inter', sans-serif;
  color: #D0D0D0;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
</style>
```

## Layout rules

- Square bullets only: `■` (`U+25A0`) or `▪` (`U+25AA`) — no circles, no icons.
- Borders: `0.5px solid #333333` only. Never thicker.
- Spacing is generous — Ash breathes. Do not compress `--gap-section`.
- No color to convey meaning — use position, size, and weight instead.
- Major section breaks: `1px solid #333333` full-width horizontal rule.

```html
<hr class="ash-rule">
<style>
.ash-rule {
  border: none;
  border-top: 1px solid #333333;
  margin: var(--gap-section) 0;
}
</style>
```

### Delta notation

Weight, not color:

```html
<span class="ash-delta-up">+12%</span>
<span class="ash-delta-down">-3%</span>

<style>
.ash-delta-up   { font: 900 15px/1 'Inter', sans-serif; color: #D0D0D0; }
.ash-delta-down { font: 400 15px/1 'Inter', sans-serif; color: #555555; }
</style>
```

### Column table

```html
<div class="ash-table">
  <div class="ash-row ash-header-row">
    <span>CATEGORY</span>
    <span>VALUE</span>
    <span>SHARE</span>
  </div>
  <div class="ash-row">
    <span>Protocol fees</span>
    <span>$2.1M</span>
    <span>50%</span>
  </div>
</div>

<style>
.ash-table { display: flex; flex-direction: column; gap: 0; }
.ash-row {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  padding: 10px 0;
  border-bottom: 0.5px solid #333333;
  font: 400 13px/1.4 'Inter', sans-serif;
  color: #D0D0D0;
}
.ash-header-row {
  font: 700 11px/1 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #888888;
  font-variant-caps: small-caps;
}
.ash-row span:not(:first-child) { text-align: right; font-variant-numeric: tabular-nums; }
</style>
```

## Decorative DNA

No color. No gradients. No glow. No icons. Dashes as the only ornamentation.

```html
<div class="ash-ornament">— Q3 2026 —</div>
<style>
.ash-ornament {
  font: 400 12px/1 'Inter', sans-serif;
  color: #555555;
  text-align: center;
  letter-spacing: 0.12em;
}
</style>
```

## Badge override

Grayscale only. Use `status-pill` variant but override all semantic colors to the 4 gray stops:

```css
.ash-theme .badge-active  { color: #D0D0D0; background: rgba(208,208,208,0.10); border-color: rgba(208,208,208,0.25); }
.ash-theme .badge-warning { color: #888888; background: rgba(136,136,136,0.10); border-color: rgba(136,136,136,0.25); }
.ash-theme .badge-error   { color: #555555; background: rgba(85,85,85,0.10);    border-color: rgba(85,85,85,0.25); }
```

## Step-connector override

Square badges, `#D0D0D0` background, `#0E0E0E` text. Connector line: `#333333`.

## Gradient text

Disabled. All text flat from the 4 gray stops.

## Style verification checklist

- [ ] Only 4 gray values used: `#D0D0D0`, `#888888`, `#555555`, `#333333`
- [ ] No color (no green, red, blue, orange) anywhere
- [ ] One large number per section (at least 48px)
- [ ] Square bullets `■` — no circles, no Phosphor icons
- [ ] Spacing generous: `--gap-section: 48px`
- [ ] Borders exactly `0.5px solid #333333`

## What to avoid

Any color (even subtle tints), gradients, icons, rounded shapes, decorative elements, pattern fills, compressed spacing.
