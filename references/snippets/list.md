# List Snippet

Numbered or unordered items, one per row, consistent structure. Top-N rankings, numbered tips, principles, checklists.

## When to use

- Top 10 / ranked lists
- Numbered tips, rules, principles
- Feature rosters where each item has the same shape
- When items are parallel but read better top-to-bottom than tile-style (else use grid-cards)

## Slot fit

| Canvas | Slot | Variant | Notes |
|---|---|---|---|
| bento-box | card-tall (right edge sidebar) | numbered or icon list | 5-12 rows |
| bento-box | card-wide | numbered with metric | 3-8 rows |
| editorial | sidebar | icon list | 3-6 supporting points |
| editorial | body-column | numbered | Inline numbered list (e.g., "10 things to know") |
| poster | support-card | icon list | 3-5 quick takeaways |

## Required elements

`text.md`, `layout.md`, `decorative.md`, `icons.md`. Optional `data-widgets.md` for per-row metric.

## Numbered pattern

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
  gap: 16px; align-items: center;
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

## Icon-led pattern (unordered)

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
  gap: 14px; align-items: start;
}
.icon-row i { color: var(--accent-1); font-size: 22px; margin-top: 2px; }
</style>
```

## Adaptation by row count

| Items | Treatment |
|---|---|
| 3-5 | Rich rows: title + body + metric |
| 6-8 | Trimmed: title + body OR title + metric |
| 9-12 | Compact: title + one-line body, no decorative borders |
| 13+ | Split into multiple columns OR sectioned with sub-headers |

## Composition rules

- Numbers use display font. Two-digit with leading zero: `01`, `02`, ... `10`.
- Row heights equal. Use `grid-auto-rows: 1fr` if needed.
- Don't skip numbers (no 01, 02, 05). Increment only.
- Ranked list: #1 gets emphasis (larger, glow). Others equal.

## Anti-patterns

- Don't number items then sort alphabetically — numbering implies ranked order.
- Don't mix numbered + unnumbered in one list.
- Don't list items with wildly different field shapes — use grid-cards with mixed card types instead.
