# Snippet: Sankey Flow

**Pattern:** Left-to-right flow diagram where link width encodes transferred value between named nodes. Shows where resources go and how much.

**Best for:** Token emission flows, protocol money flows, treasury allocation breakdowns, user-to-product funnels with value transfer (3–12 nodes, 3–16 links).

**Not for:** Sequential process steps without value transfer (use `process-flow`). Hierarchical trees (use `hierarchical`). Cyclical loops (use `circular-flow`).

**Canvas fit:** poster (centerpiece), bento-box (card-wide), dashboard (panel-large)

**Density cap:** 12 nodes max, 16 links max. Beyond that, links overlap illegibly.

---

## CDN requirement

```html
<!-- Both required. D3 first. -->
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/d3-sankey@0.12/dist/d3-sankey.min.js"></script>
```

---

## Data shape

Pass nodes and links as inline JSON in the script block. Link `value` is a raw number — the layout scales widths proportionally, so units are arbitrary (%, $, tokens, users).

```json
{
  "nodes": [
    { "id": "Emission" },
    { "id": "Staking Rewards" },
    { "id": "Treasury" },
    { "id": "Team" },
    { "id": "Ecosystem Grants" }
  ],
  "links": [
    { "source": "Emission", "target": "Staking Rewards", "value": 45 },
    { "source": "Emission", "target": "Treasury",        "value": 30 },
    { "source": "Emission", "target": "Team",            "value": 15 },
    { "source": "Treasury", "target": "Ecosystem Grants","value": 20 }
  ]
}
```

---

## Full pattern

```html
<!-- Requires D3 + d3-sankey in <head> -->
<div class="snippet-sankey">
  <svg id="sankey-1" style="width: 100%; display: block;"></svg>
</div>

<style>
.snippet-sankey {
  width: 100%;
  padding: var(--pad-container);
}
.sankey-node rect {
  rx: 4px;
}
.sankey-label {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 12px;
  fill: var(--text-primary);
  letter-spacing: 0.03em;
}
.sankey-value {
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;
  font-size: 11px;
  fill: var(--text-muted);
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
  const c1 = resolveColor(root.getPropertyValue('--accent-1').trim());
  const c2 = resolveColor(root.getPropertyValue('--accent-2').trim());
  const panel = resolveColor(root.getPropertyValue('--panel').trim());

  // --- DATA: replace with actual values ---
  const graphData = {
    nodes: [
      { id: 'Emission' },
      { id: 'Staking Rewards' },
      { id: 'Treasury' },
      { id: 'Team' },
      { id: 'Ecosystem Grants' },
    ],
    links: [
      { source: 'Emission', target: 'Staking Rewards', value: 45 },
      { source: 'Emission', target: 'Treasury',        value: 30 },
      { source: 'Emission', target: 'Team',            value: 15 },
      { source: 'Treasury', target: 'Ecosystem Grants',value: 20 },
    ]
  };
  // --- END DATA ---

  const svgEl = document.getElementById('sankey-1');
  const W = svgEl.parentElement.clientWidth || 800;
  const H = Math.max(320, Math.round(W * 0.45));
  svgEl.setAttribute('width', W);
  svgEl.setAttribute('height', H);
  svgEl.setAttribute('viewBox', `0 0 ${W} ${H}`);

  const { sankey, sankeyLinkHorizontal, sankeyLeft } = d3;
  const layout = sankey()
    .nodeId(d => d.id)
    .nodeWidth(16)
    .nodePadding(24)
    .nodeAlign(sankeyLeft)
    .extent([[24, 16], [W - 24, H - 16]]);

  // Deep-clone data so d3-sankey can mutate it
  const graph = layout({
    nodes: graphData.nodes.map(d => Object.assign({}, d)),
    links: graphData.links.map(d => Object.assign({}, d)),
  });

  const svg = d3.select(svgEl);

  // Gradient defs for links
  const defs = svg.append('defs');
  graph.links.forEach((link, i) => {
    const grad = defs.append('linearGradient')
      .attr('id', `sk-grad-${i}`)
      .attr('gradientUnits', 'userSpaceOnUse')
      .attr('x1', link.source.x1).attr('x2', link.target.x0);
    grad.append('stop').attr('offset', '0%').attr('stop-color', c1.rgb).attr('stop-opacity', 0.55);
    grad.append('stop').attr('offset', '100%').attr('stop-color', c2.rgb).attr('stop-opacity', 0.55);
  });

  // Links
  svg.append('g').attr('fill', 'none')
    .selectAll('path')
    .data(graph.links).join('path')
    .attr('d', sankeyLinkHorizontal())
    .attr('stroke', (d, i) => `url(#sk-grad-${i})`)
    .attr('stroke-width', d => Math.max(1, d.width));

  // Nodes
  const nodeGroup = svg.append('g')
    .selectAll('g').data(graph.nodes).join('g')
    .attr('class', 'sankey-node');

  nodeGroup.append('rect')
    .attr('x', d => d.x0).attr('y', d => d.y0)
    .attr('width',  d => d.x1 - d.x0)
    .attr('height', d => d.y1 - d.y0)
    .attr('rx', 4)
    .attr('fill', (d, i) => i === 0 ? c1.rgb : panel.rgb)
    .attr('stroke', c1.rgb)
    .attr('stroke-width', 1.5)
    .attr('stroke-opacity', 0.6);

  // Labels: left of left-edge nodes, right of all others
  nodeGroup.append('text')
    .attr('class', 'sankey-label')
    .attr('x', d => d.x0 < W / 2 ? d.x1 + 8 : d.x0 - 8)
    .attr('y', d => (d.y0 + d.y1) / 2)
    .attr('dy', '-0.2em')
    .attr('text-anchor', d => d.x0 < W / 2 ? 'start' : 'end')
    .text(d => d.id);

  nodeGroup.append('text')
    .attr('class', 'sankey-value')
    .attr('x', d => d.x0 < W / 2 ? d.x1 + 8 : d.x0 - 8)
    .attr('y', d => (d.y0 + d.y1) / 2)
    .attr('dy', '1em')
    .attr('text-anchor', d => d.x0 < W / 2 ? 'start' : 'end')
    .text(d => `${d.value}`);

  svgEl.dataset.canvasReady = 'true';
});
</script>
```

---

## Rules

- Never label link widths with raw pixel values — always show the source data unit (%, tokens, $).
- Node label position alternates: source-side nodes label to the right, sink-side nodes to the left. Never overlap a label with a link.
- Maximum 2 accent colors for nodes. Source nodes use accent-1; intermediate and sink nodes use panel background with accent-1 stroke.
- If total values at the source don't match total values at the sink (partial flows), that's valid — d3-sankey handles unbalanced graphs.
- Never use sankey for time-series data. Use a line or area chart instead.
