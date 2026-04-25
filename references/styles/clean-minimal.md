# clean-minimal — Alternative Style

Light background, single accent, generous whitespace, no glow, thin neutral borders. Use when the user wants an editorial, magazine, or corporate feel — or explicitly asks for "minimal", "clean", "airy", "editorial".

Proves the token-swap mechanism: same token structure as `aizfographics-style`, different values.

## CSS variables

```css
:root {
  /* canvas — light by default */
  --canvas:        #FAFAFA;
  --panel:         #FFFFFF;
  --elevated:      #F2F2F2;

  /* text */
  --text-primary:   #111111;
  --text-secondary: #4A4A4A;
  --text-muted:     #8A8A8A;
  --on-accent:      #FFFFFF;

  /* accent — single color, no pair */
  --accent-1: #0F6E56;
  --accent-2: #0F6E56;   /* identical on purpose — no gradient text */

  /* semantic */
  --positive: #1B8A3B;
  --negative: #B0202F;

  /* spacing — generous */
  --gap-section: 56px;
  --gap-element: 24px;
  --gap-card:    20px;
  --pad-container: 32px;

  /* radius — slight */
  --radius-card: 4px;
  --radius-pill: 2px;
  --radius-btn:  4px;
}
```

Dark mode variant available on request, but the style's intent is light.

## Typography

### Default pair: Inter + IBM Plex Serif

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:wght@400;700&family=Inter:wght@400;500;700&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | IBM Plex Serif | 700 | Title Case | 44–56px |
| Section title | Inter | 700 | Title Case | 20–24px |
| Card title | Inter | 700 | Title Case | 15–18px |
| Body | Inter | 400 | Sentence | 14–16px |
| Caption | Inter | 400 | Sentence | 11–12px |

Notice: **NOT uppercase** — editorial uses title case. This is the intentional deviation from aizfographics-style.

### No gradient text

`.gradient-text` renders as flat `var(--accent-1)`. Minimalism means no decorative text treatments.

## Accent

Single color. No pair. One-brand feel.

Defaults to a deep teal `#0F6E56`. User can supply a brand color. `--accent-1` and `--accent-2` hold the same value so style-agnostic element code (which references both) still works.

## Decorative DNA

### Borders

1px solid `--elevated` or 1px solid `color-mix(in srgb, var(--text-primary) 10%, transparent)`. Full perimeter. No gradient, no glow.

```css
.card {
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--text-primary) 10%, transparent);
  border-radius: var(--radius-card);
}
```

### No glow

```css
.hero-title { text-shadow: none; }
.key-card   { box-shadow: none; }
```

### No gradient overlays

Solid `--panel` on all containers. Rely on spacing and typography for hierarchy, not color layering.

### Background

Solid `--canvas`. Never vignette, never noise.

## Component DNA

- **Hero**: boxed or full-bleed with plenty of top/bottom padding.
- **Badges**: thin 1px border, no fill, `var(--accent-1)` text.
- **Cards**: outlined only, never filled, never gradient-border.
- **Connectors**: `var(--text-muted)` straight lines. Very thin (1px).
- **Footer**: `var(--text-muted)`, bottom-right.

## When to use

- Editorial layouts (long-form, article-style)
- Corporate or B2B infographics
- Print-oriented output
- Any time the user says "minimal", "clean", "airy", "editorial", "print"

## When NOT to use

- High-energy launch graphics → use aizfographics-style
- Gaming / crypto-native / web3 content → use aizfographics-style
- Content requiring multiple accent colors → use aizfographics-style
