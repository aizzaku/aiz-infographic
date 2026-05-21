# growth-hacking — Growth Hacking Infographic Style

Dark charcoal canvas, refined gold accent, serif headings. Professional, authoritative, data-confident. Inspired by editorial finance/GEO infographics.

## When to Use

- Growth hacking tactics, metrics, A/B testing frameworks
- Marketing strategy visuals with authoritative tone
- Startup/business growth data
- Comparison tables (what works vs what doesn't)

## When NOT to Use

- Playful or casual content (use `bold-graphic`)
- Code-heavy / technical deep-dives (use `blueprint`)
- Educational / academic (use `hand-drawn-edu`)

## CSS Variables

```css
:root {
  /* canvas — charcoal, not near-black */
  --canvas:        #1A1A1A;
  --panel:         #222222;
  --elevated:      #2A2A2A;

  /* text */
  --text-primary:   #FFFFFF;
  --text-secondary: #B0B0B0;
  --text-muted:     #666666;
  --on-accent:      #1A1A1A;

  /* accent pair — refined gold, not amber */
  --accent-1: #D4A843;
  --accent-2: #C4963A;

  /* semantic */
  --positive: #4ADE80;
  --negative: #F87171;

  /* spacing */
  --gap-section: 36px;
  --gap-element: 18px;
  --gap-card:    14px;
  --pad-container: 24px;

  /* radius */
  --radius-card:  8px;
  --radius-pill:  4px;
  --radius-btn:   6px;
}
```

## Typography

### Fonts: Libre Baskerville (serif display) + DM Sans (body)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Libre Baskerville | 700 | Sentence (title case) | 64–88px |
| Section title | Libre Baskerville | 700 | Sentence | 24–32px |
| Card title / label | DM Sans | 700 | UPPERCASE | 14–18px |
| Body | DM Sans | 400 | Sentence | 14–16px |
| Caption / footnote | DM Sans | 400 | Sentence | 11–13px |
| KPI number | Libre Baskerville | 700 | — | 56–80px |
| Badge / tag | DM Sans | 700 | UPPERCASE | 10–12px |

Body `line-height: 1.6`. Hero `line-height: 1.1`.

### Accent Color Pairs

| # | `--accent-1` | `--accent-2` | Character | Best for |
|---|-------------|-------------|-----------|----------|
| 1 | `#D4A843` | `#C4963A` | Refined gold | Default — growth, marketing, business |
| 2 | `#D4A843` | `#4ADE80` | Gold + green | A/B test results, positive wins |
| 3 | `#D4A843` | `#60A5FA` | Gold + blue | Social proof, channel comparisons |

### Gradient Text

```css
.gradient-text {
  background: linear-gradient(30deg, var(--accent-1), var(--accent-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

## Decorative DNA

### Cards

Gradient border with gold accent — rounded corners (8px). Never single-sided borders.

```css
.card {
  border-radius: var(--radius-card);
  border: 1px solid transparent;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 15%, transparent),
      color-mix(in srgb, var(--accent-1) 35%, transparent)) border-box;
}
```

### KPI Number Highlight

Large serif numerals in gold, adjacent to white label:

```css
.kpi-number {
  font-family: 'Libre Baskerville', serif;
  font-size: 64px;
  font-weight: 700;
  color: var(--accent-1);
  line-height: 1;
}
```

### Section Dividers

Thin gold horizontal rules (1px, 20% opacity):

```css
.section-divider {
  height: 1px;
  background: linear-gradient(90deg,
    transparent,
    color-mix(in srgb, var(--accent-1) 20%, transparent) 30%,
    color-mix(in srgb, var(--accent-1) 20%, transparent) 70%,
    transparent);
  margin: var(--gap-section) 0;
}
```

### Badges

Gold text on gold-tinted bg, pill shape:

```css
.badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  background: color-mix(in srgb, var(--accent-1) 12%, transparent);
  border: 1px solid color-mix(in srgb, var(--accent-1) 35%, transparent);
  color: var(--accent-1);
  font: 700 11px/1 'DM Sans', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
```

### Footer

`var(--text-muted)`, DM Sans 400, 11px, bottom-aligned. Source attribution right-aligned.

## Component DNA

### Hero Section

Left-aligned title, full-width charcoal bg. Gold badge above title. Subtitle in white. Optional gold divider below.

### Comparison Tables

Two-column bento-box. Left column: gold accent border. Right column: muted gray border. Clear "WHAT WORKS" vs "WHAT DOESN'T" headers.

### Action Cards

Numbered 1–4. Each card: dark panel, gold number, white title, grey description. Bordered with gold gradient.

### Copy Patterns Section

3-column grid of dark grey cards with gold top border. Monospace for template text examples.

## Verification Checklist

- [ ] Serif (Baskerville) headings, sans (DM Sans) body — never one font
- [ ] Gold accent throughout (#D4A843)
- [ ] All section/card headers: sentence case (not ALL CAPS)
- [ ] KPI numbers: large serif in gold
- [ ] Badges: uppercase DM Sans
- [ ] No emoji anywhere
- [ ] Dark charcoal background (#1A1A1A), not near-black
- [ ] Body copy flat colors (no gradients on text)
