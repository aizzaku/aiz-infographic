# Hierarchical Layout

Parent → child relationships. Trees, org charts, category→subcategory breakdowns. Reading flow top-down.

## When to use

- Organization structure
- Category → subcategory taxonomies
- Decision trees (simplified)
- Governance hierarchy (DAO → councils → working groups)
- Product family (parent brand → variants)

## Required elements

`connectors.md`, `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## Section order

```
┌──────────────────────────────┐
│ Header strip                 │
├──────────────────────────────┤
│ Hero section                 │
├──────────────────────────────┤
│         [ROOT NODE]          │
│           /    \             │
│     [CHILD]    [CHILD]       │
│      /  \      /  \          │
│   [..][..] [..] [..]         │
├──────────────────────────────┤
│ Key or legend (optional)     │
├──────────────────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

## Tree node pattern

```html
<div class="htree">
  <div class="hnode root">
    <div class="hnode-inner">
      <i class="ph-bold ph-tree-structure"></i>
      <div class="hnode-title">Root</div>
      <div class="hnode-meta">Project</div>
    </div>
  </div>

  <div class="hnode-connector"></div>

  <div class="hnode-row">
    <div class="hnode child">
      <div class="hnode-inner">
        <div class="hnode-title">Branch A</div>
      </div>
    </div>
    <div class="hnode child">
      <div class="hnode-inner">
        <div class="hnode-title">Branch B</div>
      </div>
    </div>
  </div>
  <!-- repeat with more rows for deeper hierarchies -->
</div>

<style>
.htree { display: flex; flex-direction: column; align-items: center; gap: 0; }
.hnode {
  padding: 14px 20px;
  border-radius: var(--radius-card);
  background:
    linear-gradient(var(--panel), var(--panel)) padding-box,
    linear-gradient(135deg,
      color-mix(in srgb, var(--accent-1) 22%, transparent),
      color-mix(in srgb, var(--accent-1) 42%, transparent)) border-box;
  border: 1px solid transparent;
  text-align: center;
  min-width: 160px;
}
.hnode.root {
  background:
    linear-gradient(var(--elevated), var(--elevated)) padding-box,
    linear-gradient(135deg, var(--accent-1), var(--accent-2)) border-box;
  box-shadow: 0 0 24px color-mix(in srgb, var(--accent-1) 18%, transparent);
}
.hnode-title {
  font: 700 14px/1.2 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-primary);
}
.hnode-meta {
  font: 400 11px/1 'Montserrat', sans-serif;
  color: var(--text-muted);
  margin-top: 4px;
}

.hnode-connector {
  width: 1px; height: 24px;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 50%, transparent),
    color-mix(in srgb, var(--accent-1) 20%, transparent));
}

.hnode-row {
  display: flex;
  gap: 24px;
  justify-content: center;
  position: relative;
}
.hnode-row::before {
  content: '';
  position: absolute;
  top: -24px;
  left: 20%;
  right: 20%;
  height: 1px;
  background: color-mix(in srgb, var(--accent-1) 30%, transparent);
}
</style>
```

## Depth guidance

| Levels | Canvas | Notes |
|--------|--------|-------|
| 2 (root + children) | Any | Simple, works everywhere |
| 3 (root + children + grandchildren) | Portrait | Ideal |
| 4+ | Portrait-tall or landscape | Use abbreviated titles at leaf level |

## Composition rules

- Root node is visually distinct — stronger border, slight glow, larger padding.
- Children of the same parent are visually equal (same size, same style). Unequal siblings confuse the hierarchy.
- Keep branches symmetric where possible. If one branch has 5 children and another has 1, the eye expects balance — either rebalance or explain the asymmetry with a caption.
- At 4+ levels, consider sideways (left-to-right) orientation or split into multiple sub-trees.

## Anti-patterns

- Never connect nodes across branches with the same kind of connector you use for parent-child. Cross-connections need a different visual (dashed line, different color) or they look like data corruption.
- Avoid mixing hierarchy with chronology. If there's a time dimension, use timeline or roadmap instead.
