# corporate — Professional / B2B Style

Conservative, clean, boardroom-presentation feel. Navy + gold accents, Inter, moderate density. Approachable for stakeholders who don't want "crypto energy".

## When to use

- Investor decks translated to infographic
- Enterprise / B2B reports
- Regulatory-compliant content
- Formal partnership announcements
- Content for traditional finance audiences

## CSS variables

```css
:root {
  --canvas:        #FFFFFF;
  --panel:         #F7F8FA;
  --elevated:      #EDEFF3;

  --text-primary:   #0F1E3D;
  --text-secondary: #3A4A6B;
  --text-muted:     #7A8AA8;
  --on-accent:      #FFFFFF;

  --accent-1: #0F1E3D;
  --accent-2: #C5A046;

  --positive: #1B8A3B;
  --negative: #B0302D;

  --gap-section: 36px;
  --gap-element: 18px;
  --gap-card:    14px;
  --pad-container: 32px;

  --radius-card: 4px;
  --radius-pill: 12px;
  --radius-btn:  4px;
}
```

## Typography

### Pair: Inter + Merriweather (for display emphasis)

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Merriweather:wght@700;900&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Merriweather | 900 | Title Case | 42–56px |
| Section title | Inter | 700 | Title Case | 18–22px |
| Card title | Inter | 600 | Title Case | 15–17px |
| Body | Inter | 400 | Sentence | 14–16px |
| Caption | Inter | 500 | Sentence | 11–12px |
| KPI value | Merriweather | 700 | Sentence | 32–44px |

## Decorative DNA

### Borders

Simple 1px borders in a soft neutral. Rounded 4px corners. Gold accent line above cards for emphasis where needed.

```css
.card {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--text-primary) 8%, transparent);
  border-radius: 4px;
}
.card-featured {
  border-top: 3px solid var(--accent-2);
}
```

Note: single-sided border allowed here — corporate convention (hero card with a gold top rule is a specific visual idiom).

### No glow, subtle shadows only

```css
.card {
  box-shadow: 0 1px 3px rgba(15, 30, 61, 0.06);
}
.card-featured {
  box-shadow: 0 2px 8px rgba(15, 30, 61, 0.08);
}
```

### Dividers

Full-width horizontal rule at section boundaries, very light gray.

```css
.divider {
  height: 1px;
  background: color-mix(in srgb, var(--text-primary) 8%, transparent);
  margin: 24px 0;
}
```

## Component DNA

- **Hero**: boxed with generous padding. Subtitle below. Optional date/ID stamp top-right.
- **Badges**: rounded pill, navy border, navy text (or gold accent for featured status).
- **Cards**: white bg, subtle shadow, thin border. "Featured" cards get gold top-rule.
- **KPI values** in Merriweather for presence; labels in Inter for clarity.
- **Connectors**: navy thin lines. No accent color on flow arrows.
- **Footer**: horizontal rule above, attribution in `--text-muted` uppercase tiny.

## Charts

Navy primary, gold secondary. No gradients on chart elements — flat fills only.

## When to use

- Corporate reports
- Investor / board materials
- Regulatory-conservative content
- B2B partnership announcements

## When NOT to use

- Consumer-facing marketing → use aizfographics-style
- Gaming content → use retro or aizfographics
- Technical specs → use blueprint
