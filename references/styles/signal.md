# signal — Ops Monitoring Style

Concept: Ops monitoring / broadcast alert. Everything is a status readout. Built to surface one thing: is it on, is it alerting, when did it happen.

> **Font-rule override.** This style uses 1 font (JetBrains Mono only), overriding the SKILL.md "2 fonts default." Ops dashboards and alert feeds use monospace top-to-bottom — values line up by column, timestamps prefix every entry, and there are no decorative headings to need a second face.

## When to use

- Live ops status boards
- Incident reports and post-mortems
- Alert feeds and monitoring snapshots
- Protocol status / uptime infographics
- Any content where state (active/offline/breach) is the primary message

## CSS variables

```css
:root {
  /* canvas */
  --canvas:        #0B0B0B;   /* near-black, slightly warm */
  --panel:         #111111;
  --elevated:      #161616;

  /* text */
  --text-primary:   #FF6B35;  /* active/alert — this theme's "foreground" */
  --text-secondary: #666666;  /* labels */
  --text-muted:     #333333;  /* metadata, dim entries */
  --on-accent:      #0B0B0B;

  /* accent — red-orange; alert/active state ONLY */
  --accent-1: #FF4500;
  --accent-2: #FF4500;        /* single accent, no pair rotation */

  /* semantic */
  --positive: #00FF00;        /* nominal / OK state */
  --negative: #FF4500;        /* breach / critical */

  /* border — only appears in alert state */
  --border-alert:    #FF4500;
  --border-inactive: #1A1A1A;

  /* spacing — dense, no padding waste */
  --gap-section:   16px;
  --gap-element:   8px;
  --gap-card:      4px;
  --pad-container: 12px;

  /* radius — none */
  --radius-card:  0px;
  --radius-pill:  0px;
  --radius-btn:   0px;
}
```

## Typography

100% monospace. No sans-serif, no serif.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
```

| Role | Weight | Case | Size | Letter-spacing |
|------|--------|------|------|----------------|
| Section header / state label | 700 | ALL CAPS | 12-14px | 0.10-0.12em |
| Timestamp | 400 | as-is | 11-13px | 0 |
| Entry message | 400 | Sentence | 12-13px | 0 |
| Delta value | 700 | as-is | 13-14px | 0 |

All text left-aligned. Timestamp-prefixed entry format: `23:14:08 · message`.

## Layout rules

### Feed style

Entries stack top-to-bottom, newest first. No card borders except in alert state.

```html
<div class="signal-feed">
  <div class="signal-entry signal-alert">
    <span class="signal-ts">23:14:08</span>
    <span class="signal-sep">·</span>
    <span class="signal-sev badge-pill badge-error">BREACH</span>
    <span class="signal-sep">·</span>
    <span class="signal-msg">TVL threshold crossed: $12.4M below floor</span>
  </div>
  <div class="signal-divider"></div>
  <div class="signal-entry signal-nominal">
    <span class="signal-ts">23:10:22</span>
    <span class="signal-sep">·</span>
    <span class="signal-sev badge-pill badge-active">NOMINAL</span>
    <span class="signal-sep">·</span>
    <span class="signal-msg">Heartbeat OK</span>
  </div>
</div>

<style>
.signal-feed { display: flex; flex-direction: column; gap: 0; }

.signal-entry {
  display: flex;
  align-items: baseline;
  gap: 6px;
  padding: 8px 0;
  font: 400 12px/1.4 'JetBrains Mono', monospace;
}

.signal-alert {
  border-left: 2px solid #FF4500;
  padding-left: 10px;
}

.signal-ts    { color: #666666; flex-shrink: 0; }
.signal-sep   { color: #333333; }
.signal-msg   { color: #FF6B35; }
.signal-nominal .signal-msg { color: #666666; }

.signal-divider {
  height: 1px;
  background: linear-gradient(90deg, #FF4500, transparent);
  opacity: 0.25;
  margin: 2px 0;
}
</style>
```

### Scan-line dividers

```css
.scan-divider {
  height: 1px;
  background: linear-gradient(90deg, var(--accent-1, #FF4500), transparent);
  margin: 8px 0;
  opacity: 0.4;
}
```

### Status dots

The single permitted glow in this theme — on active status dots only:

```html
<div class="dot-label dot-active">
  <span class="dot"></span>
  <span class="dot-text">ACTIVE</span>
</div>

<style>
/* signal-theme: permitted glow on active dot only */
.signal-theme .dot-active .dot {
  background: #FF4500;
  box-shadow: 0 0 4px #FF4500;
}
</style>
```

### Delta values

```html
<span class="signal-delta signal-delta-up">D+340%</span>
<span class="signal-delta signal-delta-down">D-12ms</span>

<style>
.signal-delta {
  font: 700 13px/1 'JetBrains Mono', monospace;
  font-variant-numeric: tabular-nums;
}
.signal-delta-up   { color: #FF4500; }
.signal-delta-down { color: #666666; }
</style>
```

## Alert state card

The only context where a card border appears:

```css
.card-alert {
  border: 1px solid #FF4500;
  background: #111111;
  border-radius: 0;
  padding: 12px;
}
.card-inactive {
  border: 1px solid #1A1A1A;
  background: #111111;
  border-radius: 0;
}
```

## Badge override

Use `dot-label` variant from `badges.md`. ALL CAPS, monospace, letter-spacing 0.10em. Signal-theme glow on active dot permitted.

## Progress bar override

Use `flat-bar` variant from `progress-bars.md`. Fill color: `#FF4500` (accent). No gradient.

## Gradient text

Disabled. All text flat.

## Style verification checklist

- [ ] One font: `'JetBrains Mono', monospace`
- [ ] `--accent-1: #FF4500` — used exclusively for alert/active state
- [ ] No rounded corners
- [ ] No card borders except `card-alert` and `card-inactive`
- [ ] Dense layout — no padding waste
- [ ] Glow only on active status dot, nowhere else

## What to avoid

Multiple accent colors, rounded cards, sans-serif fonts, decorative icons, any softness, gradients (except the scan-line), fills on inactive cards.
