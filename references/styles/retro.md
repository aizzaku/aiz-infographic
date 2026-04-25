# retro — 8-Bit Arcade

Pixel-art typography, high-contrast palette, arcade cabinet vibe. For gaming content, retro-themed launches, pixel-art projects.

## When to use

- 8-bit / pixel-art games
- Retro-themed launches
- Arcade-styled event posters
- Gigaverse-style content (pairs with the spec's "retro" alternative font pair)

## CSS variables

```css
:root {
  --canvas:        #0B0F1C;
  --panel:         #161B2E;
  --elevated:      #21283F;

  --text-primary:   #F4F3E9;
  --text-secondary: #AFB5C8;
  --text-muted:     #606480;
  --on-accent:      #0B0F1C;

  --accent-1: #FFD166;
  --accent-2: #EF4444;

  --positive: #00D95E;
  --negative: #EF4444;

  --gap-section: 28px;
  --gap-element: 14px;
  --gap-card:    10px;
  --pad-container: 24px;

  --radius-card: 0;
  --radius-pill: 0;
  --radius-btn:  0;
}
```

## Typography

### Pair: Press Start 2P + VT323

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Press Start 2P | 400 | UPPERCASE | 32–48px (small because pixel fonts read big) |
| Section title | Press Start 2P | 400 | UPPERCASE | 12–14px |
| Card title | Press Start 2P | 400 | UPPERCASE | 10–12px |
| Body | VT323 | 400 | Sentence | 20–24px |
| Caption | VT323 | 400 | UPPERCASE | 16–18px |

Press Start 2P is BIG per-character — hero title of 32px reads like 48px of a normal font. Calibrate sizes down.

Line-height: 1.5 for Press Start 2P (it needs breathing room), 1.3 for VT323.

## Decorative DNA

### Pixel borders

Sharp 2px borders, no radius ever. Layered offset borders for "sticker" effect:

```css
.card {
  background: var(--panel);
  border: 2px solid var(--text-primary);
  border-radius: 0;
  box-shadow: 4px 4px 0 var(--accent-1);
}
```

The offset solid shadow is a staple retro pattern.

### Dithered backgrounds (optional)

```css
.infographic-canvas::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image:
    radial-gradient(circle, var(--text-primary) 1px, transparent 1px);
  background-size: 4px 4px;
  opacity: 0.06;
}
```

### CRT scan lines (subtle)

```css
.infographic-canvas::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 0, 0, 0.15) 2px,
    rgba(0, 0, 0, 0.15) 4px
  );
  z-index: 1;
}
```

### Color restraint

8-bit vibe respects a limited palette. Use `--accent-1` and `--accent-2` with occasional `--positive`/`--negative`. No gradients — flat fills only.

### Icons

Phosphor icons CAN work but pixel-style icons (from Iconify's `pixelarticons` set) are more on-brand:

```html
<img src="https://api.iconify.design/pixelarticons/heart.svg?color=%23EF4444&height=24">
```

## Component DNA

- **Hero**: Press Start 2P title with offset color shadow (red shadow under yellow title = classic arcade).
- **Badges**: sharp rectangular, accent-colored bg, black text.
- **Cards**: offset box-shadow for sticker effect.
- **Connectors**: straight pixel-aligned lines, no curves.
- **Numbers**: blocky, VT323 for large values (displays as pseudo-segmented LCD).

## Text shadow (arcade signature)

```css
.hero-title {
  color: var(--accent-1);
  text-shadow:
    4px 4px 0 var(--accent-2),
    6px 6px 0 var(--text-primary);
}
```

## When to use

- Retro / pixel-art games
- Arcade themes
- Gigaverse and similar onchain games with 8-bit roots
- Nostalgia-themed content

## When NOT to use

- Professional / enterprise content
- Modern consumer-facing product launches (unless the product is explicitly retro-themed)
- Any content where readability at small sizes matters — Press Start 2P is hard to read tiny
