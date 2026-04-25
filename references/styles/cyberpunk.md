# cyberpunk — Neon Dystopia

Magenta + cyan neon on black. Scan lines, glitches, hard shadows. Maximalist accent usage. Use when the subject IS cyberpunk-coded (cyberpunk games, dystopian themes, synth/vaporwave content).

## When to use

- Cyberpunk games / lore content
- Synth / vaporwave aesthetic
- "Neon city" themed projects
- Hacking / security-themed content (ethically framed)
- Album art, event posters

## CSS variables

```css
:root {
  --canvas:        #0A0014;
  --panel:         #14001F;
  --elevated:      #1F002E;

  --text-primary:   #F0E6FF;
  --text-secondary: #B399CC;
  --text-muted:     #664D80;
  --on-accent:      #0A0014;

  --accent-1: #FF00E6;
  --accent-2: #00F0FF;

  --positive: #00FF88;
  --negative: #FF3366;

  --gap-section: 28px;
  --gap-element: 16px;
  --gap-card:    12px;
  --pad-container: 24px;

  --radius-card: 0;
  --radius-pill: 0;
  --radius-btn:  0;
}
```

## Typography

### Pair: Orbitron + Share Tech Mono

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Orbitron | 900 | UPPERCASE | 56–76px |
| Section title | Orbitron | 700 | UPPERCASE | 18–22px |
| Card title | Orbitron | 700 | UPPERCASE | 14–16px |
| Body | Share Tech Mono | 400 | Sentence | 13–15px |
| Caption | Share Tech Mono | 400 | UPPERCASE | 10–11px |

## Decorative DNA

### Gradient text — cross-hue

Unlike aizfographics (same-hue), cyberpunk uses full magenta-cyan cross-hue gradient:

```css
.hero-title {
  background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 20px color-mix(in srgb, var(--accent-1) 50%, transparent);
}
```

### Hard neon glows

```css
.card-featured {
  box-shadow:
    0 0 20px color-mix(in srgb, var(--accent-1) 40%, transparent),
    0 0 40px color-mix(in srgb, var(--accent-1) 20%, transparent),
    inset 0 0 10px color-mix(in srgb, var(--accent-1) 15%, transparent);
}
```

### Scan lines overlay

```css
.infographic-canvas::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(255, 255, 255, 0.025) 2px,
    rgba(255, 255, 255, 0.025) 3px
  );
  z-index: 1;
}
```

### Sharp borders, high contrast

```css
.card {
  background: var(--panel);
  border: 1px solid var(--accent-1);
  border-radius: 0;
  position: relative;
}
.card::before {
  content: '';
  position: absolute;
  top: -1px; left: -1px; right: -1px; bottom: -1px;
  border: 1px solid var(--accent-2);
  opacity: 0.4;
  transform: translate(3px, 3px);
  pointer-events: none;
}
```

The "double border offset" creates a chromatic-aberration feel.

### Glitch text (sparingly)

```css
.glitch {
  position: relative;
  color: var(--text-primary);
}
.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
}
.glitch::before {
  color: var(--accent-1);
  transform: translate(-2px, 0);
  clip-path: inset(0 0 50% 0);
}
.glitch::after {
  color: var(--accent-2);
  transform: translate(2px, 0);
  clip-path: inset(50% 0 0 0);
}
```

## Component DNA

- **Hero**: large, glitchy, magenta-cyan gradient. Often with scan lines in the background.
- **Badges**: sharp rectangular, magenta or cyan border, uppercase mono text.
- **Cards**: black panel, neon border, offset double-border for chromatic aberration.
- **Connectors**: bright accent lines, often dashed for "digital signal" feel.
- **Charts**: magenta + cyan palette, glow on key segments.

## When to use

- Cyberpunk games / media
- Synthwave / vaporwave content
- Dystopian / near-future themes
- Edgy product launches in crypto/tech

## When NOT to use

- Professional / enterprise content → use corporate
- Calm / educational content → use editorial or clean-minimal
- Most crypto projects (even "futuristic" ones read better in aizfographics default)
