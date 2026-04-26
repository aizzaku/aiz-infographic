# Hierarchical Snippet

Parent → child tree. Top-down reading. Org charts, taxonomies, governance hierarchies.

## When to use

- Organization structure
- Category → subcategory taxonomies
- Governance hierarchy (DAO → councils → working groups)
- Product family (parent brand → variants)

## Slot fit

| Canvas | Slot | Notes |
|---|---|---|
| bento-box | card-wide | 2-3 levels deep, 5-9 nodes total |
| editorial | body-column | Inline tree figure |
| poster | centerpiece | Deep tree (3-4 levels) as the hero |
| poster | support-card | Mini 2-level subtree |

## Required elements

`connectors.md`, `text.md`, `layout.md`, `decorative.md`, `icons.md`.

## HTML pattern

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
  text-transform: uppercase; letter-spacing: 0.05em;
  color: var(--text-primary);
}
.hnode-meta { font: 400 11px/1 'Montserrat', sans-serif; color: var(--text-muted); margin-top: 4px; }
.hnode-connector {
  width: 1px; height: 24px;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--accent-1) 50%, transparent),
    color-mix(in srgb, var(--accent-1) 20%, transparent));
}
.hnode-row {
  display: flex; gap: 24px; justify-content: center; position: relative;
}
.hnode-row::before {
  content: ''; position: absolute;
  top: -24px; left: 20%; right: 20%; height: 1px;
  background: color-mix(in srgb, var(--accent-1) 30%, transparent);
}
</style>
```

## Depth guidance

| Levels | Slot orientation | Notes |
|---|---|---|
| 2 (root + children) | Any | Simple, works everywhere |
| 3 (root + children + grandchildren) | Portrait | Ideal |
| 4+ | Portrait-tall or sideways | Use abbreviated leaf titles |

## Composition rules

- Root node visually distinct — stronger border, glow, larger padding.
- Siblings under one parent are visually equal. Unequal sizes confuse hierarchy.
- Keep branches symmetric; if asymmetric, explain in a caption.
- 4+ levels → consider sideways orientation or split into sub-trees.

## Anti-patterns

- Cross-branch connections with the same line style as parent-child → looks like data corruption. Use dashed or different color.
- Mixing chronology with hierarchy → use timeline or roadmap instead.
