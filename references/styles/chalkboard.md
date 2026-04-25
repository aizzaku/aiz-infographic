# chalkboard — Schoolroom Slate

Textured dark green "chalkboard", white hand-drawn marker strokes, casual educational feel. For explainers that want to feel like a teacher sketching on a board.

## When to use

- Tutorial / explainer content
- "Back to basics" educational infographics
- Informal protocol walkthroughs
- Kid/community-friendly content

## CSS variables

```css
:root {
  --canvas:        #2D3B2A;
  --panel:         #374735;
  --elevated:      #3F4F3D;

  --text-primary:   #F0EDE0;
  --text-secondary: #C4C0AE;
  --text-muted:     #807D6E;
  --on-accent:      #2D3B2A;

  --accent-1: #FFD166;
  --accent-2: #EF476F;

  --positive: #06D6A0;
  --negative: #EF476F;

  --gap-section: 32px;
  --gap-element: 18px;
  --gap-card:    14px;
  --pad-container: 28px;

  --radius-card: 0;
  --radius-pill: 4px;
  --radius-btn:  4px;
}
```

## Typography

### Pair: Caveat + Patrick Hand

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&family=Patrick+Hand&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Caveat | 700 | Title Case | 56–72px |
| Section title | Caveat | 700 | Title Case | 24–30px |
| Card title | Patrick Hand | 400 | Title Case | 16–20px |
| Body | Patrick Hand | 400 | Sentence | 15–17px |
| Caption | Patrick Hand | 400 | Sentence | 12–13px |

Hand-drawn feel means normal sentence case, NOT uppercase. Deviates from aizfographics uppercase rule intentionally.

## Decorative DNA

### Chalkboard texture

```css
.infographic-canvas {
  background:
    radial-gradient(ellipse at top, rgba(255,255,255,0.04), transparent 50%),
    radial-gradient(ellipse at bottom, rgba(0,0,0,0.2), transparent 60%),
    var(--canvas);
  position: relative;
}
.infographic-canvas::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image:
    url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.08 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  mix-blend-mode: screen;
}
```

### Borders — rough hand-drawn

```css
.card {
  background: transparent;
  border: 2px solid var(--text-primary);
  border-radius: 4px;
  /* SVG filter approach for rough edges — optional */
  position: relative;
}
/* optional: add SVG filter="url(#roughen)" for sketchy edge effect */
```

### Underlines (emphasis)

Common chalkboard convention — underline important words in accent:

```css
.highlight {
  text-decoration: underline;
  text-decoration-color: var(--accent-1);
  text-decoration-thickness: 3px;
  text-underline-offset: 4px;
}
```

### Arrows — hand-drawn curves

Use SVG arrows with slightly wobbly paths instead of straight lines. Keep stroke-linecap round.

### No hard glow

Chalk doesn't glow. Use slight text-shadow to simulate chalk dust:

```css
.hero-title {
  text-shadow: 0 0 2px rgba(255, 255, 255, 0.3);
}
```

## Component DNA

- **Hero**: handwritten feel, underlined key word for emphasis. Scribbled border around text optional.
- **Badges**: small rounded pills with hand-drawn outline.
- **Cards**: white-outlined boxes, no fill.
- **Connectors**: curly hand-drawn arrows (SVG paths with slight irregularity).
- **Numbers**: circled (drawn-circle around the number).

## When to use

- Tutorials and "explain like I'm 5" content
- Community / educational workshops
- Lightweight, informal visual explainers
- Storytelling / narrative content

## When NOT to use

- Financial / serious content → use corporate or editorial
- Technical specs → use blueprint
- Consumer product launches → use aizfographics-style
