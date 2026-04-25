# List Layout

Ordered or unordered items with consistent structure per row. The most readable layout for scanning. Workhorse for "Top N", numbered tips, rankings, checklists.

## When to use

- Top 10 / ranked lists
- Numbered steps (if steps aren't a true process with branching — else use process-flow)
- Feature lists where each feature has the same shape
- Rules, guidelines, or principles
- Prioritized task lists

For dense parallel items with visual icons, prefer `grid-cards` instead. List is best when each item has multiple fields that read better top-to-bottom than left-to-right.

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`, optionally `data-widgets.md` for per-row metrics.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│ Optional intro stats strip   │
├──────────────────────────────┤
│ 01 ───────────────────────── │  numbered row
│ 02 ───────────────────────── │
│ 03 ───────────────────────── │
│ …                            │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Numbered list pattern

```html
<ol class="num-list">
  <li class="num-row">
    <span class="num">01</span>
    <div class="num-body">
      <h3 class="card-title">Open with a quick feeler</h3>
      <p class="body">Small stake, read the table, adjust.</p>
    </div>
    <span class="num-meta">15%</span>
  </li>
  <!-- repeat -->
</ol>

<style>
.num-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; }
.num-row {
  display: grid;
  grid-template-columns: 48px 1fr auto;
  gap: 16px;
  align-items: center;
  padding: 14px 16px;
  border-radius: var(--radius-card);
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 16%, transparent),
      color-mix(in srgb, var(--accent-1) 32%, transparent)) border-box;
  border: 1px solid transparent;
}
.num {
  font: 400 32px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.04em;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
  text-align: center;
}
.num-meta {
  font: 400 20px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  font-variant-numeric: tabular-nums;
}
</style>
```

## Unordered (bullet or icon-led) pattern

```html
<ul class="icon-list">
  <li class="icon-row">
    <i class="ph-bold ph-lightning"></i>
    <div>
      <h3 class="card-title">Fast finality</h3>
      <p class="body">Under 2 seconds from submission to confirmation.</p>
    </div>
  </li>
  <!-- repeat -->
</ul>

<style>
.icon-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; }
.icon-row {
  display: grid;
  grid-template-columns: 32px 1fr;
  gap: 14px;
  align-items: start;
}
.icon-row i { color: var(--accent-1); font-size: 22px; margin-top: 2px; }
</style>
```

## Adaptation rules

| Items | Treatment |
|-------|-----------|
| 3–5 | Rich rows with title + body + metric |
| 6–8 | Trimmed rows — title + body only, or title + metric |
| 9–12 | Compact: title + one-line body, no decorative borders |
| 13+ | Split into multiple columns OR multiple sections with headers |

## Composition rules

- Numbers use display font (Bebas Neue). Two-digit with leading zero: `01`, `02`, … `10`, `11`.
- Row heights are equal — grid-auto-rows if necessary.
- Don't skip numbers (no 01, 02, 05, 06). Incrementing integers only.
- Ranked lists: #1 gets visual emphasis (larger number, stronger glow). Others equal.
- Use metrics column for values (`--pct`, `$`, `score`) — optional but powerful.

## Anti-patterns

- Don't use a list when items aren't truly parallel in structure. If row shapes vary, use grid-cards with differing card types.
- Never number items and then sort alphabetically — numbering implies ranked or ordered meaning.
- Don't mix numbered + unnumbered items in one list.
