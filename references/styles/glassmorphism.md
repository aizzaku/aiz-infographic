# glassmorphism — Glassmorphism Dark Style

Dark background with frosted-glass card effects, gold accent for KPIs. User's preferred style for growth hacking social infographics.

## When to Use

- Growth hacking case study infographics (default for this content type)
- Any compact social media infographic where the user hasn't specified another style
- When the user says "glassmorphism" or "glass style"

## When NOT to Use

- Full-size bento-box infographics with many sections (use `aizfographics-style`)
- Technical/developer-focused content (use `blueprint`)
- Editorial long-form (use `editorial`)

## CSS Variables

```css
:root {
  --canvas:        #080808;
  --body-bg:       #050505;
  --text-primary:   #FFFFFF;
  --text-secondary: rgba(255, 255, 255, 0.6);
  --text-muted:     rgba(255, 255, 255, 0.45);
  --text-dim:       rgba(255, 255, 255, 0.2);
  --accent-1: #D4A843;
  --accent-2: #B8922F;
  --glass-bg:       rgba(255, 255, 255, 0.05);
  --glass-bg-deep:  rgba(255, 255, 255, 0.01);
  --glass-bg-end:   rgba(255, 255, 255, 0.03);
  --glass-border:   rgba(255, 255, 255, 0.07);
  --glass-shine:    rgba(255, 255, 255, 0.04);
  --glass-inner-top: rgba(255, 255, 255, 0.06);
  --canvas-border:  rgba(255, 255, 255, 0.04);
  --divider:        rgba(255, 255, 255, 0.06);
  --footer-divider: rgba(255, 255, 255, 0.04);
}
```

## Typography

### Fonts: Libre Baskerville (serif display) + DM Sans (body)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Libre Baskerville | 700 | Sentence | 42px |
| Hero gold highlight | Libre Baskerville | 700 | Sentence | 42px (gradient text) |
| KPI number | Libre Baskerville | 700 | As-is | 56px |
| Card title / label | DM Sans | 700 | UPPERCASE | 14px, letter-spacing 0.1em |
| Card body | DM Sans | 400 | Sentence | 16px, line-height 1.55 |
| Source / footer | DM Sans | 400 | Sentence | 12px |

## Glassmorphism Card DNA

The signature visual element. Three layered effects create the frosted-glass look:

```css
.card {
  background: linear-gradient(165deg,
    rgba(255,255,255,0.05) 0%,
    rgba(255,255,255,0.01) 60%,
    rgba(255,255,255,0.03) 100%);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.07);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.06);
  position: relative;
  overflow: hidden;
}
.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 200%;
  background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, transparent 100%);
  pointer-events: none;
}
```

**Critical:** Card child elements must have `position: relative` to render above the `::before` pseudo-element.

## Gold Gradient Text

```css
.hero span {
  background: linear-gradient(135deg, #D4A843 0%, #B8922F 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

## Canvas Background

```css
body { background: #050505; }
.canvas {
  background: radial-gradient(ellipse at 50% 0%, rgba(30,30,27,0.4) 0%, #080808 50%, #000000 100%);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 12px;
}
```

## Dividers

Hero-to-content: `1px solid rgba(255,255,255,0.06)`, `padding-bottom: 28px`, `margin-bottom: 36px`
Footer: `1px solid rgba(255,255,255,0.04)`, `margin-top: 28px`, `padding-top: 14px`

## Export Notes

- Root element class: `.canvas` (not `.infographic-canvas`)
- Export requires `--selector ".canvas"` flag
- Width: 1920px, content-driven height

## Verification Checklist

- [ ] Dark body (#050505) with radial gradient canvas (#080808)
- [ ] All cards have backdrop-filter blur(12px)
- [ ] Card `::before` pseudo-element for diagonal shine
- [ ] Card children have `position: relative`
- [ ] Gold accent (#D4A843) on KPI numbers only
- [ ] Hero highlight uses gradient text
- [ ] No emoji anywhere
- [ ] No em dashes anywhere
- [ ] Source attribution bottom-right, rgba(255,255,255,0.2)
