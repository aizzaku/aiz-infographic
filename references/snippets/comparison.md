# Comparison Snippet

Side-by-side comparison of 2-4 options. VS block for 2 options; feature table for 3-4.

## When to use

- Protocol A vs B (wallets, DEXes, L1s)
- Plan comparison (free vs pro vs enterprise)
- Before / after state
- Multi-option feature matrix

## Slot fit

| Canvas | Slot | Variant | Notes |
|---|---|---|---|
| bento-box | card-wide (`1/-1`) | VS block (2 opts) | Full-bleed VS the section's headline |
| bento-box | card-wide | feature table | 3-4 options, condensed rows |
| editorial | body-column | feature table | Inline figure |
| dashboard | panel-large (w-12) | feature table | Period A vs Period B |
| poster | centerpiece | VS block | Two-up A vs B as the hero |
| poster | support-card | mini comparison | Quick A/B summary |

## Required elements

`comparison.md` (VS block, feature table), `text.md`, `layout.md`, `decorative.md`, `icons.md`

## VS block (2 options)

```html
<div class="vs-block">
  <div class="vs-side">
    <div class="vs-logo"><img src="{a_logo}" alt="{a_name}"></div>
    <h2 class="vs-name">{a_name}</h2>
    <div class="vs-tagline">{a_tagline}</div>
    <ul class="vs-list">
      <li><i class="ph-bold ph-check-circle"></i> Pro one</li>
      <li><i class="ph-bold ph-check-circle"></i> Pro two</li>
      <!-- 4-6 pros -->
    </ul>
  </div>
  <div class="vs-divider"><span class="vs-label">VS</span></div>
  <div class="vs-side">
    <!-- mirror structure for option B -->
  </div>
</div>

<style>
.vs-block {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 24px; align-items: stretch;
}
.vs-side {
  padding: 20px;
  background: var(--panel);
  border: 1px solid color-mix(in srgb, var(--accent-1) 22%, transparent);
  border-radius: var(--radius-card);
  display: flex; flex-direction: column; gap: 10px;
}
.vs-divider {
  display: flex; align-items: center; justify-content: center;
}
.vs-label {
  font: 400 32px/1 'Bebas Neue', sans-serif;
  color: var(--accent-1);
  letter-spacing: 0.04em;
}
.vs-name {
  font: 400 28px/1 'Bebas Neue', sans-serif;
  text-transform: uppercase;
  margin: 0;
}
.vs-list { list-style: none; padding: 0; margin: 8px 0 0; display: flex; flex-direction: column; gap: 6px; }
.vs-list li { display: flex; align-items: center; gap: 8px; font: 400 13px/1.4 'Montserrat', sans-serif; }
.vs-list i { color: var(--accent-1); font-size: 16px; }
</style>
```

## Feature table (3-4 options)

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
    <tr>
      <td>Latency</td>
      <td>~200ms</td>
      <td>~500ms</td>
      <td>~150ms</td>
    </tr>
    <!-- repeat -->
  </tbody>
</table>

<style>
.feature-table {
  width: 100%; border-collapse: collapse;
  font: 400 13px/1.4 'Montserrat', sans-serif;
}
.feature-table th, .feature-table td {
  padding: 8px 12px; text-align: left;
  border-bottom: 1px solid color-mix(in srgb, var(--text-muted) 25%, transparent);
}
.feature-table th {
  font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.05em; font-size: 11px;
  color: var(--accent-1);
}
.feature-table tbody tr:hover { background: color-mix(in srgb, var(--accent-1) 5%, transparent); }
</style>
```

## Composition rules

- Order matters: put recommended option first (or rightmost for "winner takes all").
- Symmetry of framing: if A has 5 pros, B has 5. Unbalanced → editorial, not analytical.
- Icons for binary features (`ph-check-circle` / `ph-x-circle`); text for scalar values.
- Max 4 options. 5+ → switch to a tall feature-only table with no graphic framing.
- Always disclose criteria ("based on X" or "as of date").

## Anti-patterns

- Disparaging framing → state facts, let the reader decide.
- Mixing VS block + table in the same section.
- Color-coding "winner" green and "loser" red — use accent vs neutral instead.
