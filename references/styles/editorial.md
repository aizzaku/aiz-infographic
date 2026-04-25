# editorial — Magazine-Style Layout

Long-form article feel. Serif display type, generous whitespace, single-column body. Evokes thoughtful analysis and newsroom authority.

## When to use

- Research reports
- Market commentary
- Thought-leadership pieces
- Explainers with narrative arc
- Print-oriented output

## CSS variables

```css
:root {
  --canvas:        #F8F6F0;
  --panel:         #FFFFFF;
  --elevated:      #EFEAE0;

  --text-primary:   #1A1A1A;
  --text-secondary: #3A3A3A;
  --text-muted:     #7A7A7A;
  --on-accent:      #F8F6F0;

  --accent-1: #B0352A;
  --accent-2: #B0352A;

  --positive: #1B8A3B;
  --negative: #B0352A;

  --gap-section: 48px;
  --gap-element: 20px;
  --gap-card:    16px;
  --pad-container: 40px;

  --radius-card: 0;
  --radius-pill: 0;
  --radius-btn:  0;
}
```

## Typography

### Pair: Playfair Display + Source Sans Pro

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Source+Sans+Pro:wght@400;600;700&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Playfair Display | 900 | Title Case | 48–64px |
| Subtitle / deck | Playfair Display | 400 italic | Sentence | 18–22px |
| Section title | Source Sans Pro | 700 | UPPERCASE | 13–14px (small caps vibe) |
| Card title | Playfair Display | 700 | Title Case | 20–24px |
| Body | Source Sans Pro | 400 | Sentence | 15–17px |
| Byline / meta | Source Sans Pro | 600 | UPPERCASE | 10–11px |
| Pull quote | Playfair Display | 400 italic | Sentence | 22–28px |

Body line-height: 1.55 (airier than default 1.5).

## Decorative DNA

### Borders

Hairlines. 1px solid in neutral gray, never accent.

```css
.divider {
  height: 1px;
  background: color-mix(in srgb, var(--text-primary) 15%, transparent);
  margin: 32px 0;
}
.card {
  border-top: 1px solid color-mix(in srgb, var(--text-primary) 12%, transparent);
  border-bottom: 1px solid color-mix(in srgb, var(--text-primary) 12%, transparent);
  padding: 16px 0;
  background: transparent;
}
```

Note: the "never single-sided" rule from aizfographics-style is relaxed here — editorial tradition uses top/bottom rules for article dividers.

### Drop caps (signature)

```css
.lead-para::first-letter {
  font-family: 'Playfair Display', serif;
  font-weight: 900;
  font-size: 4em;
  line-height: 0.85;
  float: left;
  margin: 0.05em 0.1em 0 0;
  color: var(--accent-1);
}
```

### No glow, no gradients

```css
.hero-title { text-shadow: none; }
.kpi-card   { box-shadow: none; }
.gradient-text {
  background: none;
  -webkit-text-fill-color: var(--accent-1);
  color: var(--accent-1);
}
```

### Pull-quote treatment

```css
.pull-quote {
  border-left: 4px solid var(--accent-1);
  padding-left: 20px;
  font: italic 400 22px/1.4 'Playfair Display', serif;
  color: var(--text-primary);
  margin: 24px 0;
}
```

This is the one place single-sided borders are allowed in editorial — it's a typographic convention.

## Component DNA

- **Hero**: boxed or centered, always with a subtitle/deck below. Byline and date above or below title.
- **Badges**: thin border + uppercase tiny text. Rectangular.
- **Cards**: mostly borderless; dividers between instead.
- **Charts**: simple, restrained. Single color, minimal legend.
- **Footer**: attribution + date + author.

## When to use

- Long-form articles
- Research and analysis
- "Annual report" style pieces
- Narrative-driven explainers

## When NOT to use

- Dashboard / data-heavy content → use aizfographics-style
- Technical specs → use blueprint
- Gaming content → use retro or aizfographics
