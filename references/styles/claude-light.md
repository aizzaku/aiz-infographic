# claude-light — Warm Editorial Authority Style

Source: Anthropic brand guidelines — official palette `#FAF9F5`, `#D97757`, Poppins + Lora
Concept: Warm editorial authority. The only light style in the skill. Off-white parchment field, terracotta orange accent, serif body. Considered, not cold.

```
canvas-fit: [bento-box, editorial, poster]
```

## When to use

- Claude or Anthropic product infographics
- AI safety, alignment, or Anthropic research explainers
- Any content explicitly requesting the Claude or Anthropic brand style
- Auto-selected when content is primarily about Claude models, Anthropic research, or the Claude ecosystem

## CSS variables

```css
:root {
  /* canvas — official Anthropic light, warm off-white */
  --canvas:        #FAF9F5;
  --panel:         #F0EDE5;   /* card background */
  --elevated:      #E8E4DC;   /* nested surfaces */

  /* accent — Anthropic orange */
  --accent-1:      #D97757;
  --accent-2:      #C86040;   /* darker variant for gradient */
  --accent-dim:    rgba(217,119,87,0.12);
  --accent-muted:  rgba(217,119,87,0.06);
  --on-accent:     #FAF9F5;

  /* text */
  --text-primary:   #141413;  /* official Anthropic dark */
  --text-secondary: #8A8070;  /* warm gray */
  --text-muted:     #B0AEA5;  /* official Anthropic mid-gray */

  /* borders — warm, never cool gray */
  --border-default: #E8E4DC;
  --border-accent:  rgba(217,119,87,0.25);

  /* semantic */
  --positive: #2E7D32;        /* warm green — not the default neon */
  --negative: #C0392B;        /* warm red */

  /* spacing — generous editorial */
  --gap-section:   40px;
  --gap-element:   24px;
  --gap-card:      16px;
  --pad-container: 28px;

  /* radius */
  --radius-card:  10px;
  --radius-pill:  6px;
  --radius-btn:   8px;
}
```

## Typography

Two fonts: Poppins (headers/UI) + Lora (body copy). The Lora serif body is the fingerprint of this style.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Lora:wght@400;700&display=swap">
```

| Role | Font | Weight | Case | Size | Notes |
|------|------|--------|------|------|-------|
| Hero title | Poppins | 700 | UPPERCASE | 56-72px | letter-spacing 0.02em |
| Section label | Poppins | 700 | UPPERCASE | 11px | letter-spacing 0.14em, accent |
| Card title | Poppins | 700 | UPPERCASE | 16px | letter-spacing 0.06em |
| Body | Lora | 400 | Sentence | 14px | line-height 1.65 — MUST be Lora |
| Feature text | Lora | 400 | Sentence | 13px | line-height 1.6, text-secondary |
| Metadata | Poppins | 400 | Sentence | 11px | text-muted, letter-spacing 0.06em |
| Badge | Poppins | 700 | UPPERCASE | 11px | letter-spacing 0.05em |

**Body copy MUST be Lora.** Never swap Lora for a sans-serif body. This is the non-negotiable rule.

**No Bebas Neue.** Display type is Poppins only.

## Decorative DNA

### Gradient text (permitted on hero and major section headers)

```css
.gradient-text {
  background: linear-gradient(135deg, #D97757 30%, #C86040 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}
```

### Cards

Warm surface with gentle shadow — the Anthropic card feel:

```css
.card {
  background: var(--panel);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-card, 10px);
  padding: 24px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
```

No gradient borders — Anthropic uses solid warm borders.

### Badges

```css
.badge {
  background: var(--accent-dim);
  border: 1px solid var(--border-accent);
  border-radius: var(--radius-pill, 6px);
  color: var(--accent-1);
  font: 700 11px/1 'Poppins', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 4px 10px;
}
```

### Feature dots

```css
.feat-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--accent-1);
  flex-shrink: 0;
  margin-top: 6px;
}
```

### Section dividers

```css
.section-divider {
  border: none;
  border-top: 1px solid var(--border-default);
  margin: 0;
}
```

### Footer

```css
.footer {
  border-top: 1px solid var(--border-default);
  padding-top: 16px;
  font: 400 11px/1 'Poppins', sans-serif;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-variant-caps: small-caps;
}
```

## Layout rules

```
alignment:    left-aligned
canvas-feel:  warm, open, editorial — generous padding
hero:         large Poppins headline + Lora subtext, accent on key terms
cards:        surface bg, border-default, generous internal padding (24-28px)
sections:     separated by border-default horizontal rules
grid:         max 4-col, but 2-col is the Anthropic preference for readability
```

## Style verification checklist

- [ ] Canvas is `#FAF9F5` — must have warm cream cast, never pure white or cool white
- [ ] Body copy is Lora serif — never swapped for sans-serif
- [ ] All borders use warm grays (`#E8E4DC` range) — never cool grays
- [ ] `box-shadow: 0 2px 12px rgba(0,0,0,0.06)` on cards — gentle, not heavy
- [ ] Accent (`#D97757`) on labels and key terms only — not large fills
- [ ] No Bebas Neue, no dark backgrounds

## Forbidden

No dark backgrounds. No cool grays. No sans-serif body copy (Lora is non-negotiable for paragraph text). No second accent color. No high-contrast harsh edges. No Bebas Neue. No gradient borders — Anthropic uses solid warm borders.
