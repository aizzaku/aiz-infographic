# Tagged Header — Banner-tab Strip

A narrow strip with a flag-cut right edge that sits at the top of a card, callout, or section. Functions as a labeled banner — like a paper tab clipped onto a folder.

## When to use

- Top of a `callout-card` to label its category ("NOTE", "WARNING", "INSIGHT", "Q3 RESULTS").
- Top of any grid card when category labeling is needed instead of a section header.
- Wrapping a numbered chip + label (e.g., "01 — DISCOVERY").

## HTML / CSS

```html
<div class="tagged-header">
  <span class="tagged-header__label">Key Insight</span>
</div>

<style>
.tagged-header {
  --notch: 12px;
  display: inline-flex;
  align-items: center;
  padding: 8px 28px 8px 14px;
  background: color-mix(in srgb, var(--accent-1) 18%, var(--panel));
  border: 1px solid color-mix(in srgb, var(--accent-1) 35%, transparent);
  border-radius: 4px 0 0 4px;
  /* Right-edge flag cut */
  clip-path: polygon(
    0 0,
    calc(100% - var(--notch)) 0,
    100% 50%,
    calc(100% - var(--notch)) 100%,
    0 100%
  );
}

.tagged-header__label {
  font: 700 13px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-1);
}
</style>
```

## Mounted on a card

Sits flush against the card's top-left corner, overlapping slightly:

```html
<div class="card" style="position:relative;padding-top:36px;">
  <div class="tagged-header" style="position:absolute;top:-1px;left:14px;">
    <span class="tagged-header__label">Note</span>
  </div>
  <!-- card body -->
</div>
```

## Variants

| Variant | Background | Border | Label color |
|---|---|---|---|
| Default (accent) | `accent-1 @ 18%` | `accent-1 @ 35%` | `--accent-1` |
| Positive | `positive @ 12%` | `positive @ 40%` | `--positive` |
| Negative | `negative @ 12%` | `negative @ 40%` | `--negative` |
| Muted | `panel` | `text-muted @ 30%` | `--text-secondary` |

## Rules

- Notch width: 10-14px. Smaller doesn't read as a flag; larger looks like a chevron.
- Label: 1-3 words, uppercase, ≤ 14px. Longer text reads as a card title, not a tag.
- Max 1 tagged-header per card (left side only). Don't put one on each edge — it stops being an emphasis device.
- When paired with `callout-card`, the tagged-header acts as the category label and the card body holds the message. Don't repeat the label in the body.
