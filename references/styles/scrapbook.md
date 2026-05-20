# scrapbook — Physical Evidence Style

Concept: Physical evidence pinned to a notice board. Data is pinned, taped, and annotated on a journal spread. Warmth, imprecision, and tactile texture are intentional.

## When to use

- Research findings, qualitative insights
- Persona or user journey boards
- Mood boards, concept exploration
- Human-centered content where the "physical artifact" metaphor fits

## CSS variables

```css
:root {
  /* canvas */
  --canvas:        #F7F4EF;   /* warm off-white, aged paper */

  /* card surfaces */
  --panel:         #FFF9EE;   /* slightly warm white */
  --elevated:      #F0EAD8;   /* light tan */

  /* text */
  --text-primary:   #2C2418;  /* dark warm brown */
  --text-secondary: #6B5A3E;  /* medium warm brown */
  --text-muted:     #9A8A72;  /* warm gray-brown */
  --on-accent:      #2C2418;

  /* accent — tape and highlight only */
  --accent-tape:   rgba(255,230,150,0.55);  /* yellow tape strip */
  --accent-hl:     rgba(255,220,80,0.35);   /* marker highlight */
  --accent-pin:    rgba(0,0,0,0.12);        /* pin shadow */
  --accent-string: #C0392B;                  /* red string for connectors */

  /* borders */
  --border:        #C8BFA8;   /* aged paper edge */

  /* semantic */
  --positive: #2E7D32;
  --negative: #C0392B;

  /* spacing — intentionally varied, not rigid */
  --gap-section:   36px;
  --gap-element:   20px;
  --gap-card:      16px;
  --pad-container: 28px;

  /* radius — varied per card type */
  --radius-card:   3px;   /* slight aging, not sharp */
  --radius-pill:   2px;
  --radius-btn:    3px;
}
```

## Typography

Mixed intentionally: serif for body, cursive/handwritten for annotations.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:wght@400;700&family=Caveat:wght@400;700&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | Lora | 700 | Title Case | 48-64px |
| Section title | Lora | 700 | Title Case | 20-26px |
| Card title | Lora | 700 | Title Case | 15-18px |
| Annotation / handwritten note | Caveat | 400-700 | Sentence | 14-18px |
| Body | Lora | 400 | Sentence | 14-15px |
| Caption | Caveat | 400 | Sentence | 12-13px |

Font sizes may vary per card by ±2px. Imprecision is intentional.

**No monospace unless simulating a typewriter label:**

```css
.typewriter-label {
  font: 400 12px/1.4 'Courier New', monospace;
  color: var(--text-secondary);
}
```

## Layout rules

### Card rotation (signature)

Every card is rotated slightly. Never perfectly aligned.

```css
.card-pinned { transform: rotate(-1.5deg); }
.card-taped  { transform: rotate(2deg); }
.card-note   { transform: rotate(-0.8deg); }
.card-photo  { transform: rotate(1.2deg); }
```

Rotation range: -3deg to +3deg. No card at exactly 0deg. No two adjacent cards at the same angle.

### Tape marks

```html
<div class="card-taped" style="transform: rotate(2deg);">
  <div class="tape tape-top"></div>
  <div class="card-content">...</div>
</div>

<style>
.tape {
  position: absolute;
  width: 32px;
  height: 14px;
  background: rgba(255,230,150,0.55);
  border-radius: 1px;
}
.tape-top {
  top: -7px;
  left: 50%;
  transform: translateX(-50%) rotate(-1deg);
}
.tape-corner-tl { top: -5px; left: 10px; transform: rotate(-30deg); }
.tape-corner-tr { top: -5px; right: 10px; transform: rotate(30deg); }
</style>
```

### Highlight bands

On key values or phrases:

```html
<span class="hl">$42 million</span>

<style>
.hl {
  background: rgba(255,220,80,0.35);
  padding: 0 3px;
  border-radius: 2px;
}
</style>
```

### Polaroid frame

```html
<div class="polaroid">
  <div class="polaroid-img" style="background: #E8DDD0; height: 120px;">
    <!-- image placeholder or <img> -->
  </div>
  <div class="polaroid-caption">Caption below the image</div>
</div>

<style>
.polaroid {
  background: #FEFEFE;
  padding: 10px 10px 20px;
  border: 1px solid #D8CDB8;
  box-shadow: 2px 3px 6px rgba(0,0,0,0.12);
  display: inline-block;
}
.polaroid-caption {
  font: 400 12px/1.4 'Caveat', cursive;
  color: var(--text-secondary);
  text-align: center;
  margin-top: 8px;
}
</style>
```

### Red string connector

For linking related cards visually (decorative only, not functional SVG):

```html
<div class="string-connector" style="
  position: absolute;
  left: 120px; top: 80px;
  width: 140px; height: 2px;
  background: #C0392B;
  transform: rotate(12deg);
  transform-origin: left center;
"></div>
```

### Sticky note card

```css
.sticky {
  background: #FFF9C4;  /* yellow sticky */
  border: none;
  padding: 14px;
  min-height: 80px;
  box-shadow: 2px 3px 8px rgba(0,0,0,0.10);
}
.sticky-pink  { background: #FCE4EC; }
.sticky-blue  { background: #E3F2FD; }
.sticky-green { background: #E8F5E9; }
```

### Z-index stacking

Overlapping is intentional:

```css
.card-pinned { position: relative; z-index: 2; }
.card-behind { position: relative; z-index: 1; }
```

## Scrapbook exception to universal rules

This theme explicitly permits:
- `transform: rotate(Xdeg)` on cards — imprecision is the aesthetic
- Mixed font families (serif + cursive) — both are declared in this style
- `box-shadow` on polaroid and sticky note cards — simulates paper depth
- Non-4px-multiple font sizes (±2px variation per card) — intentional

All other universal rules apply (no emoji, no en/em dashes, no images from invented URLs).

## What to avoid

Dark backgrounds, monospace as the primary font, perfect grid alignment, hairline borders, high contrast color schemes, gradients, glow effects.
