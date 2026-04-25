# hand-drawn — Sketchnote Style

Casual, sketched, slightly imperfect. Cream paper, muted colors, Kalam/Caveat typography. For content that benefits from a personal, handmade feel.

## When to use

- Personal notes / "my take on X" content
- Workshop handouts, zine-style pieces
- Informal walkthroughs
- Creative / indie project announcements

## CSS variables

```css
:root {
  --canvas:        #F5EFE0;
  --panel:         #FFFBF0;
  --elevated:      #EDE5D0;

  --text-primary:   #2B2420;
  --text-secondary: #5A4E44;
  --text-muted:     #8A7E70;
  --on-accent:      #F5EFE0;

  --accent-1: #D84B20;
  --accent-2: #3B7A9E;

  --positive: #2D8659;
  --negative: #B03030;

  --gap-section: 36px;
  --gap-element: 20px;
  --gap-card:    16px;
  --pad-container: 32px;

  --radius-card: 6px;
  --radius-pill: 12px;
  --radius-btn:  6px;
}
```

## Typography

### Pair: Kalam + Architects Daughter

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Architects+Daughter&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Kalam | 700 | Title Case | 44–56px |
| Section title | Kalam | 700 | Title Case | 22–26px |
| Card title | Architects Daughter | 400 | Title Case | 18–20px |
| Body | Architects Daughter | 400 | Sentence | 15–17px |
| Caption | Architects Daughter | 400 | Sentence | 12–13px |

Slight rotation on some elements adds handmade feel:
```css
.badge { transform: rotate(-1.5deg); }
.card { transform: rotate(0.3deg); }
```

## Decorative DNA

### Paper texture

```css
.infographic-canvas {
  background: var(--canvas);
  position: relative;
}
.infographic-canvas::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.04;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='2'/><feColorMatrix values='0 0 0 0 0.1  0 0 0 0 0.1  0 0 0 0 0.1  0 0 0 1 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  mix-blend-mode: multiply;
}
```

### Hand-drawn borders (SVG-based)

Use SVG `<rect>` with wobbly path or CSS `border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;` to approximate:

```css
.card {
  background: var(--panel);
  border: 2px solid var(--text-primary);
  border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
  padding: 16px 20px;
}
.card:nth-child(even) {
  border-radius: 15px 225px 15px 255px/255px 15px 225px 15px;
}
```

### Highlighter-style highlights

```css
.highlight {
  background: linear-gradient(180deg,
    transparent 55%,
    color-mix(in srgb, var(--accent-1) 35%, transparent) 55%,
    color-mix(in srgb, var(--accent-1) 35%, transparent) 90%,
    transparent 90%);
  padding: 0 2px;
}
```

### Doodle accents

Small hand-drawn arrows, stars, or underlines (inline SVG) placed as decorative accents near key elements. Keep sparse.

### No glow

Sketched content doesn't glow. Zero box-shadow on decorative elements.

## Component DNA

- **Hero**: Kalam bold title with a hand-drawn underline accent.
- **Badges**: rounded pills with irregular radius, slight rotation.
- **Cards**: paper-colored bg, dark outline, irregular border-radius.
- **Connectors**: wobbly SVG arrows with round stroke-linecap.
- **Numbers**: circled with hand-drawn circle outlines.

## When to use

- Personal blog graphics
- Indie project announcements
- Tutorial / sketchnote content
- Zine-style, low-fi pieces

## When NOT to use

- Financial / regulated content → corporate or editorial
- Product launches with serious positioning → aizfographics
- Technical specs → blueprint
