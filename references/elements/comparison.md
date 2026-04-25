# Comparison — VS Blocks, Feature Tables

For side-by-side comparisons (2 options) or feature matrices (3+ options × N features).

## VS block (2 options, big)

```html
<div class="vs-block">
  <div class="vs-side">
    <h3 class="card-title">Option A</h3>
    <ul class="vs-list">
      <li><i class="ph-bold ph-check"></i>Fast</li>
      <li><i class="ph-bold ph-check"></i>Cheap</li>
      <li class="dim"><i class="ph-bold ph-minus"></i>Centralized</li>
    </ul>
  </div>
  <div class="vs-divider">
    <span class="vs-label">VS</span>
  </div>
  <div class="vs-side">
    <h3 class="card-title">Option B</h3>
    <ul class="vs-list">
      <li><i class="ph-bold ph-check"></i>Decentralized</li>
      <li class="dim"><i class="ph-bold ph-minus"></i>Slower</li>
      <li><i class="ph-bold ph-check"></i>Open</li>
    </ul>
  </div>
</div>

<style>
.vs-block {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: var(--gap-element);
  align-items: stretch;
}
.vs-side {
  padding: 20px;
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 20%, transparent),
      color-mix(in srgb, var(--accent-1) 40%, transparent)) border-box;
  border: 1px solid transparent;
  border-radius: var(--radius-card);
}
.vs-list { list-style: none; padding: 0; margin: 12px 0 0; display: flex; flex-direction: column; gap: 8px; }
.vs-list li {
  display: flex; align-items: center; gap: 8px;
  font: 400 14px/1.3 'Montserrat', sans-serif;
  color: var(--text-primary);
}
.vs-list li.dim { color: var(--text-muted); }
.vs-list .ph-bold.ph-check { color: var(--positive); }
.vs-list .ph-bold.ph-minus { color: var(--text-muted); }

.vs-divider {
  display: flex; align-items: center; justify-content: center;
  min-width: 48px;
}
.vs-label {
  font: 400 28px/1 'Bebas Neue', sans-serif;
  letter-spacing: 0.08em;
  color: var(--accent-1);
}
</style>
```

## Feature table (N options × M features)

```html
<table class="feature-table">
  <thead>
    <tr>
      <th></th>
      <th>Relay</th>
      <th>Cleo</th>
      <th>LiquidSwap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Swaps</th>
      <td><i class="ph-bold ph-check-circle"></i></td>
      <td><i class="ph-bold ph-check-circle"></i></td>
      <td><i class="ph-bold ph-check-circle"></i></td>
    </tr>
    <tr>
      <th>Bridging</th>
      <td><i class="ph-bold ph-check-circle"></i></td>
      <td><i class="ph-bold ph-x-circle dim"></i></td>
      <td><i class="ph-bold ph-x-circle dim"></i></td>
    </tr>
    <tr>
      <th>Limit orders</th>
      <td><i class="ph-bold ph-x-circle dim"></i></td>
      <td><i class="ph-bold ph-check-circle"></i></td>
      <td><i class="ph-bold ph-check-circle"></i></td>
    </tr>
  </tbody>
</table>

<style>
.feature-table {
  width: 100%;
  border-collapse: collapse;
  font: 400 13px/1 'Montserrat', sans-serif;
}
.feature-table thead th {
  text-align: left;
  padding: 10px 12px;
  font: 700 12px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-primary);
  border-bottom: 1px solid color-mix(in srgb, var(--text-primary) 12%, transparent);
}
.feature-table tbody th {
  text-align: left;
  padding: 10px 12px;
  font-weight: 700;
  color: var(--text-secondary);
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.04em;
}
.feature-table tbody td {
  padding: 10px 12px;
  text-align: center;
}
.feature-table tbody tr:nth-child(odd) {
  background: color-mix(in srgb, var(--text-primary) 3%, transparent);
}
.feature-table .ph-bold.ph-check-circle { color: var(--positive); font-size: 18px; }
.feature-table .ph-bold.ph-x-circle.dim { color: var(--text-muted); font-size: 18px; }
</style>
```

## Side-by-side cards (3–4 options, equal weight)

Use `.grid-3` or `.grid-2` from `layout.md` with individual outlined cards. Each card has:
- Icon or logo at top
- Name
- Short description
- 2–3 key stats

## Rules

- Don't use comparison layouts when a single ranked bar chart would communicate the same thing.
- Use icons (`ph-check-circle`, `ph-x-circle`) not words ("yes", "no") for binary comparisons.
- Feature tables stay at ≤6 rows. More than that, switch to a layout of multiple themed tables.
- The "winner" option (if any) gets the accent-1 border; others get accent-2 or neutral borders.
