# Callout Card — Folded-corner Container

A card with a notched / folded bottom-right corner, used for emphasis callouts, "note" panels, and quoted insights. Distinct from `.card` (clean rectangle) because the folded corner signals "look here, this is annotated."

Use sparingly — max 2 per infographic. If everything has a folded corner, nothing does.

## When to use

- Pull-quote or insight callout that needs more weight than a regular card.
- Annotation panel sitting next to a chart or metric.
- "Note" / "caveat" / "key takeaway" boxes.

## When NOT to use

- Normal grid cards — use `.card` (in `decorative.md` / inline).
- Status pills or badges — use `badges.md`.
- Multi-card grids — folded corners stack badly when repeated.

## HTML / CSS

```html
<div class="callout-card">
  <div class="callout-card__body">
    <div class="card-title">Key insight</div>
    <p class="body">Community supply unlocks 4× faster than team supply over the first 24 months.</p>
  </div>
</div>

<style>
.callout-card {
  --fold: 22px;
  position: relative;
  padding: 24px;
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 35%, transparent);
  border-radius: var(--radius-card);
  /* CSS clip-path notches the bottom-right corner */
  clip-path: polygon(
    0 0,
    100% 0,
    100% calc(100% - var(--fold)),
    calc(100% - var(--fold)) 100%,
    0 100%
  );
}

/* Fold triangle — sits inside the notch */
.callout-card::after {
  content: "";
  position: absolute;
  right: 0;
  bottom: 0;
  width: var(--fold);
  height: var(--fold);
  background: color-mix(in srgb, var(--accent-1) 25%, var(--panel));
  clip-path: polygon(100% 0, 100% 100%, 0 100%);
}
</style>
```

## Variants

**Accent-tinted (default):** subtle accent wash background.
```css
.callout-card { background: color-mix(in srgb, var(--accent-1) 6%, var(--panel)); }
```

**Bordered-only:** transparent fill, dashed border.
```css
.callout-card {
  background: transparent;
  border-style: dashed;
}
```

**Tab + fold combined:** add a `.tagged-header` strip (see `tagged-header.md`) on top of the card for a banner-headed callout.

## Rules

- Fold size: 16-28px. Smaller looks like a render bug; larger eats content.
- Never place text inside the fold area — leave at least `var(--fold) + 8px` of padding on the bottom-right.
- Fold direction is always bottom-right. Don't mirror to other corners — readers expect the bottom-right convention.
- Use `--accent-1` border at 30-40% opacity. Never solid accent border.
- Cap: 2 per infographic. Over that, demote extras to plain `.card`.
