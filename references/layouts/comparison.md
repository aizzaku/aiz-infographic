# Comparison Layout

Side-by-side comparisons of 2–4 options across multiple dimensions. When the whole infographic exists to contrast A vs B (vs C vs D), use this layout. For comparisons embedded inside a larger piece, use the `comparison.md` element instead.

## When to use

- Protocol A vs Protocol B (wallets, DEXes, L1s, etc.)
- Plan comparison (free vs pro vs enterprise)
- Before / after state
- Multi-chain or multi-platform feature matrix

## Required elements

`comparison.md` (VS block, feature table), `text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │  "X vs Y" or "A comparison"
├──────────────────────────────┤
│ Headline verdict (optional)  │  e.g., "best for [use case]"
├──────────────────────────────┤
│ Side-by-side hero blocks     │  big VS block, 2 options
│   OR feature table           │  3+ options
├──────────────────────────────┤
│ Feature breakdown by category│  optional — detail rows
├──────────────────────────────┤
│ Recommendation / summary     │  optional callout
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Two-option variant (VS block)

Use the `.vs-block` pattern from `references/elements/comparison.md`. Make it the hero of the infographic by upsizing the type:

```html
<section class="section vs-hero">
  <div class="vs-block">
    <div class="vs-side">
      <div class="vs-logo"><img src="{a_logo}" alt="{a_name}"></div>
      <h2 class="vs-name">{a_name}</h2>
      <div class="vs-tagline">{a_tagline}</div>
      <ul class="vs-list">
        <!-- 4-6 pros -->
      </ul>
    </div>
    <div class="vs-divider">
      <span class="vs-label">VS</span>
    </div>
    <div class="vs-side">
      <!-- same structure for option B -->
    </div>
  </div>
</section>
```

## Multi-option variant (feature table)

For 3+ options, pivot to a feature table. Use `.feature-table` from the elements file with 3-4 columns:

```html
<table class="feature-table">
  <thead>
    <tr>
      <th>Feature</th>
      <th>{a_name}</th>
      <th>{b_name}</th>
      <th>{c_name}</th>
    </tr>
  </thead>
  <tbody>
    <!-- rows -->
  </tbody>
</table>
```

## Composition rules

- **Order matters.** Put the recommended option first (or rightmost for "winner takes all" framing).
- **Symmetry of framing.** If option A has 5 pros, option B should also have 5 (positives and negatives). Unbalanced framing feels editorial, not analytical.
- **Use icons for binary features** (`ph-check-circle` / `ph-x-circle`), text for scalar ones ("Fast", "Slow", "Limited").
- **Limit to 3–4 options max.** 5+ comparisons belong in a dedicated table infographic with no graphic framing.
- **Disclose criteria.** A caption or subtitle should note "based on X" or "as of [date]" so viewers know the comparison's basis.

## Dimension guidance

- 2 options with rich detail: portrait-medium (1080 × 1440)
- 3–4 options, short rows: landscape (1920 × 1080)
- Feature-heavy matrix (many rows): portrait-tall (1080 × 1920)

## Anti-patterns

- Don't use the comparison layout to disparage — state facts, let the reader decide.
- Don't mix VS block + table in the same infographic. Pick one framing.
- Don't color-code the "winner" green and the "loser" red. Use `--accent-1` vs neutral, or positive semantic only where a feature is genuinely a pro.
