# Cheatsheet Template

Dense quick-reference guide. Every pixel earns its place. Scannable at a glance, rewarding on a careful read.

## When to use

User mentions any of: cheatsheet, quick reference, pocket guide, tips, how to X, quick guide, reference card, key rules, strategy guide, condensed how-to, TL;DR.

## Base layout

`bento-box` (see `references/layouts/bento-box.md`) — hero strip + mixed-span tip cards. Heavier rules get wider cards; quick lookups become tall sidebar cards; reference tables become full-bleed footer cards.

**Layout fallback:** if the user explicitly asks for the old uniform-grid look, swap to `grid-cards` (dense variant) with the same required elements.

## Default style

`aizfographics-style`

## Required elements

- `text.md` — all atoms
- `layout.md` — canvas, grid recipes, kpi-strip
- `decorative.md` — gradient borders, small angled dividers between content blocks
- `icons.md` — Phosphor Bold heavily used (one per tip card)
- `data-widgets.md` — big-number, progress bar, kpi-card
- `comparison.md` — feature-table for reference lookups

## Section order (most common pattern)

The bento canvas arranges these as a hero row plus 2–4 content rows of mixed-span cards.

1. **Hero card (full-bleed: `1 / -1`)** — "[TOPIC] CHEATSHEET" title + owner badge + 3–4 quick-stat KPIs inline
2. **Core rules row** — one wide card (`1 / 3`) with the headline rule list + 2 small tip cards (`3`, `4`)
3. **Themed tip rows** — 2–3 rows mixing wide tip-grid cards and numbered-list cards based on content density
4. **Reference table card** — full-bleed (`1 / -1`) lookup/feature-table near the bottom
5. **Footer card** (optional, full-bleed) — source + version + attribution

Unlike tokenomics/ecosystem, cheatsheet card-mix is highly variable — the user's content dictates which cards become wide vs small.

## Tip card pattern

```html
<div class="tip-card">
  <div class="tip-icon"><i class="ph-bold ph-lightning"></i></div>
  <div class="tip-title">Stake early</div>
  <p class="tip-body">Earlier stakers compound higher multiplier bonuses in the first 30 days.</p>
</div>

<style>
.tip-card {
  padding: 12px 14px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 16%, transparent),
      color-mix(in srgb, var(--accent-1) 32%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
  display: flex; flex-direction: column; gap: 6px;
}
.tip-icon {
  color: var(--accent-1);
  font-size: 20px;
}
.tip-title {
  font: 700 14px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--text-primary);
}
.tip-body {
  font: 400 12px/1.4 'Montserrat', sans-serif;
  color: var(--text-secondary);
  margin: 0;
}
</style>
```

## Numbered list variant (when tips are ordered)

```html
<ol class="num-list">
  <li>
    <span class="num">01</span>
    <div>
      <h4 class="card-title">Open with a quick feeler</h4>
      <p class="body">Small stake. Read the table.</p>
    </div>
  </li>
  <!-- repeat -->
</ol>
```

## Reference table

Use the `.feature-table` from `comparison.md`, densified:

- Row padding 6–8px instead of 10–12px
- Font size 12px
- 2–4 columns typical (name | value | modifier | notes)

## Content expectations

Required:
- Topic name
- At least 4 tips or items

Strongly recommended:
- Groupings (sections) if >6 items
- Reference values or thresholds if applicable

Nice-to-have:
- Numeric stats for the quick-stats strip
- Formula or lookup table for the reference block

## Accent pair selection

Default: pair #3 (lime → gold) — energetic, matches cheatsheet vibe.
Override to pair #2 (yellow → orange) for "hot tips" feel.
Override to pair #6 (green → cyan) for technical/dev cheatsheets.
Otherwise match the subject's brand.

## Dimension guidance

Bento cheatsheets are landscape-first.

- Default: **1920w wide**, content-driven height.
- Very dense (20+ items across 4+ themes): keep 1920w; let height grow, or split into two cheatsheets per the §6 density cap.
- Compact / social variant only on explicit request: 1080w (collapses bento to 2 columns).

## HTML skeleton (excerpt)

```html
<div class="infographic-canvas">
  <div class="bento-grid">

    <section class="section bento-card s1"><!-- hero: 1 / -1 -->
      <span class="brand">{topic_owner}</span>
      <h1 class="hero-title gradient-text">{TOPIC} Cheatsheet</h1>
      <div class="kpi-strip"><!-- 3-4 headline stats inline --></div>
    </section>

    <section class="section bento-card s2"><!-- core rules: 1 / 3 -->
      <h2 class="card-title">Core rules</h2>
      <!-- numbered list of headline rules -->
    </section>
    <section class="section bento-card s3"><!-- tip: 3 --></section>
    <section class="section bento-card s4"><!-- tip: 4 --></section>

    <section class="section bento-card s5"><!-- themed tips wide: 1 / 3 --></section>
    <section class="section bento-card s6"><!-- tall lookup sidebar: 3 / 5, r3/r5 --></section>

    <section class="section bento-card s7"><!-- reference table: 1 / -1 -->
      <h2 class="card-title">Quick lookup</h2>
      <!-- feature-table -->
    </section>

    <footer class="section bento-card s8"><!-- footer: 1 / -1 -->
      <span class="caption">{source}</span>
      <span class="caption">v{version} · {date}</span>
    </footer>

  </div>
</div>
```

## Composition rules

- Density is the point. Don't pad.
- Every tip has an icon + title + 1-sentence body. Not 2. Not 0.
- Headlines are verb-first when possible: "Stake early" not "Early staking".
- Reference tables go last before the footer — they're look-up material, not scanning material.
- If you run out of space, split into two cheatsheets rather than shrink type below 11px.

## Anti-patterns

- Don't mix bullet lists and numbered lists within one infographic. Pick one ordering semantic.
- Don't let any tip card exceed 25 words of body copy.
- Don't add decorative dividers between every tip — decoration must be structural (between sections, not between parallel items).

---

## Signals variant

Used by §8.6 Signal Sheet (see `references/templates/_signals.md`). This variant constrains the cheatsheet base to a uniform grouped 3-column grid for honest cross-card comparison. **Not a standalone trigger** — only loaded when the signals flow fires.

### Differences from default cheatsheet

| Aspect | Default cheatsheet | Signals variant |
|---|---|---|
| Layout | `bento-box` mixed-span | Grouped 3-column grid (no mixed spans) |
| Grouping | Themed rows, content-driven | Fixed lenses: Derived / Comparative / Causal |
| Card schema | Icon + title + body | Headline + evidence (math/comparison/causal) + source citation |
| Card count | ≤ 16 | ≤ 9 total, ≤ 3 per lens |
| Hero card | Topic + KPI strip | Eyebrow (parent title) + "{Title} — Signals" + one-line subtitle |
| Reference table | Required at bottom | Omitted |
| Footer card | Optional | Omitted (cards already cite sources) |
| Icons | One per card | None (chrome stays out of the way of the claim) |

### When to use this variant vs default

- §8.6 fires → signals variant.
- User asks for a "cheatsheet" of any kind → default bento variant.
- The signals variant is never the answer to "make me a cheatsheet" on its own.

### Grid behavior

`display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;` per lens-group. A group with fewer than 3 cards leaves the trailing columns empty — cards do not stretch. Empty lens groups are not rendered (so a sheet may show 1, 2, or 3 groups).

### Inheritance from default

Tokens, fonts, accent pair, viewer-feature inclusion, creator-tools inclusion, density rules, no-emoji rule, gradient-text-on-headers-only rule — all inherited from the default cheatsheet template and §6.

See `references/templates/_signals.md` for the full card schema, two-pass extraction protocol, comparative sourcing modes, merge behavior, and agent-context rules.
