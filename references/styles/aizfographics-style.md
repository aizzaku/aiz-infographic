# aizfographics-style — Default Style

Source: 175-image DNA analysis, refined with April 2026 preferences.

Dark background, bold typography, one accent pair per infographic, gradient borders, restrained glow, no emoji ever. Compact density. Strong hierarchy, asymmetric balance, top-to-bottom flow.

## CSS variables (paste into every output)

```css
:root {
  /* canvas */
  --canvas:        #0F1115;
  --panel:         #161A20;
  --elevated:      #1C2028;

  /* text */
  --text-primary:   #E6E6E6;
  --text-secondary: #A0A0A8;
  --text-muted:     #606068;
  --on-accent:      #0F1115;

  /* accent pair — chosen per infographic, defaulting to pair #1 */
  --accent-1: #F3A950;
  --accent-2: #F38150;

  /* semantic */
  --positive: #00D018;
  --negative: #D0002D;

  /* spacing */
  --gap-section: 32px;
  --gap-element: 16px;
  --gap-card:    12px;
  --pad-container: 20px;

  /* radius */
  --radius-card:  10px;
  --radius-pill:   6px;
  --radius-btn:    8px;
}
```

Light mode (apply when user explicitly requests):

```css
:root[data-theme="light"] {
  --canvas:        #F8F8F8;
  /* sub-boxes are tinted from --accent-1, NOT greyscale.
     Greyscale panels look dull and corporate in light mode —
     a faint accent wash keeps the surface feeling alive and on-brand. */
  --panel:         color-mix(in srgb, var(--accent-1) 8%,  #FFFFFF);
  --elevated:      color-mix(in srgb, var(--accent-1) 14%, #FFFFFF);
  --text-primary:   #1A1A1A;
  --text-secondary: #4A4A4A;
  --text-muted:     #808080;
  --on-accent:      #F5F5F5;
  /* accents darken slightly for contrast; apply per pair */
}
```

**Light-mode sub-box rule.** `--panel` and `--elevated` MUST be derived from `--accent-1` via `color-mix`, never flat greyscale. The canvas itself stays near-white, but every card / sub-box / nested container picks up a faint accent tint so the page reads as alive and on-brand. If a section's accent role (per the colored-roles table) already mixes accent into its bg, that mix layers on top of the already-tinted `--panel` — which is the intent.

## Typography

### Rule: Exactly 2 fonts

One display font + one body font. Never three. Never one.

### Default pair: Bebas Neue + Montserrat

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;700&display=swap">
```

| Role | Font | Weight | Case | Size | Letter-spacing |
|------|------|--------|------|------|----------------|
| Hero title | Bebas Neue | 400 | UPPERCASE | 72–96px | 0.04–0.08em |
| Section title | Montserrat | 700 | UPPERCASE | 20–28px | 0.05–0.08em |
| Card title / item label | Montserrat | 700 | UPPERCASE | 16–20px | 0.04–0.06em |
| Badge / tag | Montserrat | 700 | UPPERCASE | 10–12px | 0.05em |
| Body | Montserrat | 400 | Sentence | 14–16px | normal |
| Caption / footnote | Montserrat | 400 | Sentence | 11–13px | normal |

Body `line-height: 1.5`. Hero `line-height: 1`.

### Alternative pairs (on request or thematic match)

These replace BOTH fonts. Same role rules apply.

| Pair | Display | Body | When |
|------|---------|------|------|
| Retro / pixel | Press Start 2P | VT323 | 8-bit, arcade, pixel-art content |
| Playful / rounded | Jua | Capriola | Casual, fun, community, kids |
| Technical / code | Kode Mono | Space Mono | Devtools, code-heavy, protocol specs |

### Do NOT use

Teko, Orbitron, Rajdhani, Bungee, Space Grotesk, Barlow Condensed, Inter, Poppins, Avenir Next, IBM Plex Mono, Cinzel, Cinzel Decorative.

### Uppercase rule

- Hero titles, section headers, card titles, item labels, badges: **always uppercase**.
- Body text, descriptions, captions: **never uppercase**.

### Gradient text (titles and headers only)

Same-hue gradient, lighter → darker, 30° angle:

```css
.gradient-text {
  background: linear-gradient(30deg, var(--accent-1), var(--accent-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}
```

Apply sparingly. Full title or one key word. Never on body copy.

## Accent color system

### Rule: one accent pair per infographic

Unless the content genuinely needs two (comparing two brands, etc.). Apply with **60-30-10**: 60% canvas, 30% neutrals, 10% accent.

### Default pairs — pick by content

| # | `--accent-1` | `--accent-2` | Character | Best for |
|---|-------------|-------------|-----------|----------|
| 1 | `#F3A950` | `#F38150` | Warm amber → burnt orange | Finance, tokenomics, general-purpose |
| 2 | `#FFBB00` | `#FF8800` | Golden yellow → deep orange | Announcements, launches, energy |
| 3 | `#B2FF00` | `#FFCC00` | Lime → gold | Growth, ecosystems, DeFi |
| 4 | `#FF0048` | `#FF336D` | Hot red → pink | Alerts, competition, NFTs, bold statements |
| 5 | `#67B39F` | `#CEDFCC` | Sage → mint | Calm, educational, health, sustainability |
| 6 | `#00FF90` | `#00F6FF` | Green → cyan | Tech, protocol, futuristic, web3 |

Claude picks based on content when user has no preference. For branded work, match the brand's primary + secondary instead.

### Semantic (fixed, not paired)

- Positive: `#00D018` (gains, success, up)
- Negative: `#D0002D` (loss, error, down)

### Chart series

When a chart needs ≥3 distinct colors, pull primaries from the six pairs in order:
`#F3A950, #00FF90, #FF0048, #FFBB00, #67B39F, #B2FF00`.

For 2–3 segments, use the selected pair's primary + secondary + one analogous neighbor.

### Node / card roles (semantic token layer)

Used by `data-widgets`, `comparison`, `quadrant`, `swimlane`, `flowchart`, and any layout that has multiple typed nodes/cards. Each role maps to a fill + border recipe expressed in `color-mix` over the current accent pair — so swapping the accent via the creator tools still produces coherent results.

| Role | When to use | Fill | Border |
|------|-------------|------|--------|
| `focal` | The single most important node/card in the section (one per section). | `color-mix(in srgb, var(--accent-1) 10%, var(--panel))` | gradient border, `--accent-1` 30% → 50% |
| `primary` | Core nodes carrying the story; 2–5 per section. | `var(--panel)` | gradient border, `--accent-1` 20% → 40% |
| `secondary` | Supporting detail — referenced, not central. | `var(--panel)` | 1px `color-mix(in srgb, var(--text-muted) 40%, transparent)` |
| `external` | Out-of-scope / third-party / upstream systems. | transparent | 1px **dashed** `color-mix(in srgb, var(--text-muted) 50%, transparent)` |
| `optional` | Conditional or nice-to-have paths. | `var(--panel)` at 60% alpha | 1px dashed `color-mix(in srgb, var(--accent-1) 30%, transparent)` |
| `positive` | Gains, wins, unlocks, live state. | `color-mix(in srgb, var(--positive) 8%, var(--panel))` | 1px `color-mix(in srgb, var(--positive) 40%, transparent)` |
| `negative` | Losses, risks, deprecated, blocked. | `color-mix(in srgb, var(--negative) 8%, var(--panel))` | 1px `color-mix(in srgb, var(--negative) 40%, transparent)` |

Rules:

- **Max one `focal` per section**, max 2 per infographic. If everything is focal, nothing is.
- `primary` + `focal` combined should stay ≤ the density cap declared by the canvas / snippet being used (see the relevant `references/canvases/<name>.md` or `references/snippets/<name>.md`).
- `external` must always be dashed; never a hex color change alone — viewers rely on the stroke style to read "out of scope".
- Do NOT introduce new roles at generation time (no `warning`, `experimental`, etc.). If content needs a distinction not on this table, use `primary` + a badge label.
- When the role is color-mixed with `--positive` / `--negative`, those are fixed semantic colors from this style — they do not rotate with the accent pair.

Reference implementation available as class names in `references/elements/data-widgets.md` (`.role-focal`, `.role-primary`, etc.); reuse those rather than hand-writing per component.

## Spacing & density

**Compact is default.** See CSS variables. A portrait-3:4 canvas typically has 3–6 sections; sections internally gap at `--gap-element`.

## Border radius

- Cards / containers: 10px (`--radius-card`)
- Badges / tags: 6px (`--radius-pill`)
- Buttons / CTAs: 8px (`--radius-btn`)
- Small status pills (dot-sized): `border-radius: 999px`

## Decorative DNA

### Gradient borders (primary emphasis technique)

Never single-sided thick borders. Always full-perimeter gradient borders.

Rectangular (no radius):
```css
.card {
  border: 1px solid transparent;
  border-image: linear-gradient(135deg,
    color-mix(in srgb, var(--accent-1) 20%, transparent),
    color-mix(in srgb, var(--accent-1) 40%, transparent)) 1;
}
```

With rounded corners (border-image doesn't play with border-radius, use double-background):
```css
.card {
  border-radius: var(--radius-card);
  border: 1px solid transparent;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 20%, transparent),
      color-mix(in srgb, var(--accent-1) 40%, transparent)) border-box;
}
```

### Glow effects (restrained)

Same accent, low opacity:
```css
.hero-title  { text-shadow: 0 0 12px color-mix(in srgb, var(--accent-1) 25%, transparent); }
.key-card    { box-shadow:  0 0 24px color-mix(in srgb, var(--accent-1) 12%, transparent); }
```

### Gradient overlays (background cards, hero sections)

Same accent, ~5% opacity, fading to transparent:
```css
background:
  linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 5%, transparent),
    transparent);
```

### Geometric shapes

Rectangular panels, angled dividers, pill badges, grid-like tables. Decorative, never arbitrary — always serves structure.

### Backgrounds

Dark mode default: solid `--canvas` (#0F1115). Optional radial vignette from center at 2–4% opacity. Optional noise overlay at 3–5% opacity for texture.

## Component DNA (applied consistently)

### Hero section

- Full-bleed (left-aligned title, full-width bg) — preferred
- Split-layout (image/illustration + text) — for illustrated content
- Boxed (contained, centered) — for short punchy statements
- Hero title uses gradient text (accent-1 → accent-2)

### Badges / tags

Pill shape, accent bg at 10–15% opacity, accent-1 border at 30%:
```css
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
```

### Feature cards

Outlined (preferred): transparent bg + gradient border. Or flat: solid `--panel` bg. Or filled: accent at 5% + gradient border.

### Connectors

Straight arrows default. Color: `color-mix(in srgb, var(--accent-1) 60%, transparent)` or `var(--text-secondary)`. Curved used only for process flows that need it.

### Footer

`var(--text-muted)`, Montserrat 400, 11px. Small. Bottom-aligned. Never dominant.

## Icons

Phosphor Bold (primary), Iconify API (fallback). Never emoji. See `references/elements/icons.md`.

## Style verification checklist

Before finalizing:
- [ ] Exactly two fonts in use
- [ ] One accent pair (unless content needs two)
- [ ] All headers and labels uppercase
- [ ] No single-sided thick borders
- [ ] No emoji anywhere
- [ ] Dark background (unless light explicitly requested)
- [ ] Gradient text restricted to titles/headers
- [ ] Body copy uses flat colors only
