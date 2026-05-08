# Snippet: Network / Ecosystem Graph

**Pattern:** Nodes connected by edges, positioned by D3 force-directed simulation. The layout auto-arranges based on link density — highly connected nodes gravitate to the center; isolated nodes push to the periphery.

**Best for:** Ecosystem partner maps, protocol relationship graphs, DAO governance connections, multi-chain presence maps. Use when: (a) there are 5–20 entities with non-hierarchical relationships, AND (b) the exact spatial arrangement doesn't matter — what matters is which nodes connect to which.

**Not for:** Hierarchical trees (use `hierarchical`). Fewer than 5 nodes (use `mind-map` or `venn`). Ordered/sequential flows (use `process-flow` or `sankey-flow`).

**Canvas fit:** poster (centerpiece), bento-box (card-wide / square), dashboard (panel-large)

**Density cap:** 20 nodes, 30 edges. Beyond that, the canvas becomes an unreadable hairball.

---

## CDN requirement

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

---

## Node groups and visual encoding

| `group` value | Visual |
|---|---|
| `"focal"` | Larger circle (r=36), filled accent-1, white label |
| `"partner"` | Medium circle (r=24), panel background, accent-1 stroke |
| `"external"` | Small circle (r=20), panel background, accent-2 stroke at 60% opacity |

One focal node per graph. Use it for the subject protocol/entity at the center of the ecosystem.

---

## Data shape

```json
{
  "nodes": [
    { "id": "Protocol X", "group": "focal" },
    { "id": "Partner A",  "group": "partner" },
    { "id": "Partner B",  "group": "partner" },
    { "id": "Chain A",    "group": "external" },
    { "id": "Chain B",    "group": "external" },
    { "id": "Protocol Y", "group": "partner" }
  ],
  "links": [
    { "source": "Protocol X", "target": "Partner A" },
    { "source": "Protocol X", "target": "Partner B" },
    { "source": "Protocol X", "target": "Chain A" },
    { "source": "Protocol X", "target": "Chain B" },
    { "source": "Partner A",  "target": "Protocol Y" }
  ]
}
```

Optional `"weight"` on nodes (integer 1–3) scales the node radius: `r = baseRadius * sqrt(weight)`. Omit for uniform sizing.

---

## Full pattern

```html
<!-- Requires D3 in <head> -->
<div class="snippet-network">
  <canvas id="network-1" style="display: block; width: 100%;"></canvas>
</div>

<style>
.snippet-network {
  width: 100%;
  padding: var(--pad-container);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  function resolveColor(v) {
    const c = document.createElement('canvas'); c.width = c.height = 1;
    const x = c.getContext('2d'); x.fillStyle = v; x.fillRect(0,0,1,1);
    const [r,g,b] = x.getImageData(0,0,1,1).data;
    return { rgb: `rgb(${r},${g},${b})`, rgba: a => `rgba(${r},${g},${b},${a})` };
  }
  const root = getComputedStyle(document.documentElement);
  const c1     = resolveColor(root.getPropertyValue('--accent-1').trim());
  const c2     = resolveColor(root.getPropertyValue('--accent-2').trim());
  const panel  = resolveColor(root.getPropertyValue('--panel').trim());
  const tp     = resolveColor(root.getPropertyValue('--text-primary').trim());

  // --- DATA: replace with actual values ---
  const graphData = {
    nodes: [
      { id: 'Protocol X', group: 'focal' },
      { id: 'Partner A',  group: 'partner' },
      { id: 'Partner B',  group: 'partner' },
      { id: 'Chain A',    group: 'external' },
      { id: 'Chain B',    group: 'external' },
      { id: 'Protocol Y', group: 'partner' },
    ],
    links: [
      { source: 'Protocol X', target: 'Partner A' },
      { source: 'Protocol X', target: 'Partner B' },
      { source: 'Protocol X', target: 'Chain A' },
      { source: 'Protocol X', target: 'Chain B' },
      { source: 'Partner A',  target: 'Protocol Y' },
    ]
  };
  // --- END DATA ---

  const canvas = document.getElementById('network-1');
  const W = canvas.parentElement.clientWidth || 640;
  const H = Math.round(W * 0.65);
  canvas.width  = W;
  canvas.height = H;

  const nodeRadius = { focal: 36, partner: 24, external: 20 };

  // Deep-clone nodes/links so D3 can mutate them
  const nodes = graphData.nodes.map(d => ({ ...d }));
  const links = graphData.links.map(d => ({ ...d }));

  // Pre-compute layout synchronously — no animation loop
  const sim = d3.forceSimulation(nodes)
    .force('link',    d3.forceLink(links).id(d => d.id).distance(100))
    .force('charge',  d3.forceManyBody().strength(-320))
    .force('center',  d3.forceCenter(W / 2, H / 2))
    .force('collide', d3.forceCollide(d => nodeRadius[d.group] + 12))
    .alpha(1)
    .stop();

  for (let i = 0; i < 300; i++) sim.tick();

  // Clamp nodes to canvas bounds
  nodes.forEach(n => {
    const r = nodeRadius[n.group];
    n.x = Math.max(r + 4, Math.min(W - r - 4, n.x));
    n.y = Math.max(r + 4, Math.min(H - r - 4, n.y));
  });

  const ctx = canvas.getContext('2d');

  // Draw edges
  links.forEach(link => {
    ctx.beginPath();
    ctx.moveTo(link.source.x, link.source.y);
    ctx.lineTo(link.target.x, link.target.y);
    ctx.strokeStyle = c1.rgba(0.28);
    ctx.lineWidth = 1.5;
    ctx.stroke();
  });

  // Draw nodes
  nodes.forEach(node => {
    const r = nodeRadius[node.group] * Math.sqrt(node.weight || 1);

    // Fill
    ctx.beginPath();
    ctx.arc(node.x, node.y, r, 0, Math.PI * 2);
    ctx.fillStyle = node.group === 'focal' ? c1.rgb : panel.rgb;
    ctx.fill();

    // Stroke
    ctx.lineWidth = 2;
    ctx.strokeStyle = node.group === 'external' ? c2.rgba(0.6) : c1.rgb;
    ctx.stroke();

    // Label
    ctx.fillStyle = '#ffffff';
    ctx.font = `${node.group === 'focal' ? '700' : '600'} ${node.group === 'focal' ? 12 : 10}px 'Montserrat', sans-serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // Word-wrap long labels inside the circle
    const words = node.id.split(' ');
    if (words.length === 1 || r < 24) {
      ctx.fillText(node.id, node.x, node.y);
    } else {
      ctx.fillText(words[0], node.x, node.y - 7);
      ctx.fillText(words.slice(1).join(' '), node.x, node.y + 7);
    }
  });

  canvas.dataset.canvasReady = 'true';
});
</script>
```

---

## Rules

- Always pre-compute the force layout with `simulation.stop()` + loop of `sim.tick()`. Never use an animation loop — the graph must be fully drawn at page load for Playwright exports.
- Clamp node positions to canvas bounds after ticking so labels don't clip.
- One `focal` node per graph. Never make all nodes the same group.
- Edge labels are not supported in this pattern — keep the graph readable by controlling node count.
- If a node's label is longer than 12 characters, split at the first space and render on two lines.
- Never use this snippet for fewer than 5 nodes — `mind-map` is better for small relational sets.
