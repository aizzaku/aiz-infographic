# Decorative — Backgrounds, Shapes, Borders

Decoration serves structure. Never ornamental for its own sake.

## Gradient border (primary emphasis)

For rounded containers (double-background technique):

```css
.bordered {
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 20%, transparent),
      color-mix(in srgb, var(--accent-1) 40%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
}
```

Stronger variant (for key callout cards):

```css
.bordered-strong {
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg, var(--accent-1), var(--accent-2)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
}
```

For rectangular (no radius):

```css
.bordered-rect {
  border: 1px solid transparent;
  border-image: linear-gradient(135deg,
    color-mix(in srgb, var(--accent-1) 20%, transparent),
    color-mix(in srgb, var(--accent-1) 40%, transparent)) 1;
}
```

### Forbidden: single-sided thick borders

NO `border-top: 3px solid var(--accent-1)`.
NO `border-left: 4px solid var(--accent-2)`.
NO accent bar along one edge of a card.

Always full-perimeter gradient OR no border.

## Glow effect

Same accent, low opacity. Restraint is critical — more than 2-3 glowing elements per infographic becomes noise.

```css
.glow-subtle {
  box-shadow: 0 0 20px color-mix(in srgb, var(--accent-1) 12%, transparent);
}
.glow-strong {
  box-shadow: 0 0 32px color-mix(in srgb, var(--accent-1) 25%, transparent);
}
.glow-text {
  text-shadow: 0 0 10px color-mix(in srgb, var(--accent-1) 25%, transparent);
}
```

Apply to: hero title (text-glow sparingly), primary KPI card (glow-subtle), chart center text.

Do NOT apply to: body text, section dividers, grid cells, footer.

## Gradient overlay (for background sections)

Same accent, ~5% opacity, fading to transparent. Adds tonal depth without competing with content.

```css
.overlay-top {
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 5%, transparent),
    transparent);
}
.overlay-diagonal {
  background: linear-gradient(135deg,
    color-mix(in srgb, var(--accent-1) 5%, transparent),
    transparent 60%);
}
```

Apply to: hero section wrapper, feature card clusters, content panels.

## Background noise (optional texture)

```css
.canvas-noise::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.04;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' seed='3'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  mix-blend-mode: overlay;
  z-index: 0;
}
```

Wrap canvas content in a higher z-index to sit above the noise.

## Radial vignette

```css
.canvas-vignette {
  background:
    radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.35) 100%),
    var(--canvas);
}
```

Use for cinematic hero emphasis. Optional.

## Geometric accent shapes

Not random — always structural. Use as:

- Angled divider lines between major sections
- Pill badge shapes (see `text.md` `.badge`)
- Rectangular panels with rounded corners (see card patterns)
- Small corner accents on hero sections

Angled divider:

```css
.divider-angle {
  height: 1px;
  background: linear-gradient(90deg,
    transparent,
    color-mix(in srgb, var(--accent-1) 40%, transparent) 20%,
    color-mix(in srgb, var(--accent-1) 40%, transparent) 80%,
    transparent);
  transform: skewY(-2deg);
  transform-origin: left center;
}
```

## Hero backdrop treatment

Combines overlay + geometric shape:

```html
<section class="hero">
  <div class="hero-bg"></div>
  <h1 class="hero-title gradient-text">Your Title</h1>
  …
</section>

<style>
.hero { position: relative; padding: 32px; overflow: hidden; }
.hero-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,
    color-mix(in srgb, var(--accent-1) 8%, transparent),
    transparent 60%);
  z-index: 0;
}
.hero > * { position: relative; z-index: 1; }
</style>
```

## Rules

- Every decoration must be removable without breaking comprehension.
- Gradient borders use the accent pair. Glows use `--accent-1` only (never the pair).
- Never stack three decorative effects on one element (border + glow + overlay = too much).
- Noise and vignette are optional. Default is clean solid `--canvas`.
