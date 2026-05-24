# Badges — Status Pills and State Tags

Status indicators used across terminal, signal, forge, glasspaper, ash, and obsidian-ledger themes. Three variants; choose by theme.

## Variant 1: status-pill

4px border-radius rectangle. Used by default, forge, obsidian-ledger, and ash themes.

```html
<span class="badge-pill badge-active">NOMINAL</span>
<span class="badge-pill badge-warning">PENDING</span>
<span class="badge-pill badge-error">CRITICAL</span>
<span class="badge-pill badge-offline">OFFLINE</span>
<span class="badge-pill badge-neutral">INFO</span>

<style>
.badge-pill {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font: 700 10px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border: 1px solid transparent;
}
.badge-active {
  color: var(--positive, #00D018);
  background: color-mix(in srgb, var(--positive, #00D018) 12%, transparent);
  border-color: color-mix(in srgb, var(--positive, #00D018) 35%, transparent);
}
.badge-warning {
  color: #F3A950;
  background: color-mix(in srgb, #F3A950 12%, transparent);
  border-color: color-mix(in srgb, #F3A950 35%, transparent);
}
.badge-error {
  color: var(--negative, #D0002D);
  background: color-mix(in srgb, var(--negative, #D0002D) 12%, transparent);
  border-color: color-mix(in srgb, var(--negative, #D0002D) 35%, transparent);
}
.badge-offline {
  color: var(--text-muted, #606068);
  background: color-mix(in srgb, var(--text-muted, #606068) 12%, transparent);
  border-color: color-mix(in srgb, var(--text-muted, #606068) 35%, transparent);
}
.badge-neutral {
  color: var(--text-secondary, #A0A0A8);
  background: color-mix(in srgb, var(--text-secondary, #A0A0A8) 10%, transparent);
  border-color: color-mix(in srgb, var(--text-secondary, #A0A0A8) 25%, transparent);
}
</style>
```

## Variant 2: dot-label

Live indicator dot + text label. Used by signal and forge themes. The single dot `box-shadow` glow is permitted in signal theme only.

```html
<div class="dot-label dot-active">
  <span class="dot"></span>
  <span class="dot-text">ACTIVE</span>
</div>
<div class="dot-label dot-error">
  <span class="dot"></span>
  <span class="dot-text">BREACH</span>
</div>
<div class="dot-label dot-offline">
  <span class="dot"></span>
  <span class="dot-text">OFFLINE</span>
</div>

<style>
.dot-label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font: 700 10px/1 monospace;
  text-transform: uppercase;
  letter-spacing: 0.10em;
}
.dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}
.dot-active .dot  { background: var(--positive, #00D018); }
.dot-active .dot-text { color: var(--positive, #00D018); }

.dot-error .dot   { background: var(--negative, #D0002D); }
.dot-error .dot-text  { color: var(--negative, #D0002D); }

.dot-offline .dot { background: var(--text-muted, #606068); }
.dot-offline .dot-text { color: var(--text-muted, #606068); }

/* Signal theme only: permitted glow on the dot */
.signal-theme .dot-active .dot {
  box-shadow: 0 0 4px #FF4500;
}
</style>
```

## Variant 3: inline-tag

Flat chip, no border, opacity-based depth. Used by glasspaper theme.

```html
<span class="inline-tag tag-active">Active</span>
<span class="inline-tag tag-muted">Pending</span>

<style>
.inline-tag {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 4px;
  font: 600 11px/1 sans-serif;
  letter-spacing: 0.02em;
}
.tag-active {
  background: rgba(255,255,255,0.10);
  color: var(--text-primary, #C9B8F0);
}
.tag-muted {
  background: rgba(255,255,255,0.05);
  color: var(--text-secondary, #8AB4D4);
}
</style>
```

## Semantic color map

| State | Color | CSS var |
|---|---|---|
| Active / nominal / success | Green | `--positive` |
| Warning / pending | Amber | `#F3A950` (or theme amber) |
| Error / critical / breach | Red | `--negative` |
| Offline / inactive / dim | Muted gray | `--text-muted` |
| Neutral / info | Secondary gray | `--text-secondary` |

## Theme overrides

**Forge:** badge text in ALL CAPS (`NOMINAL`, `CRITICAL`, `OFFLINE`), monospace font, no pill — use `status-pill` variant with 0 border-radius override.

**Terminal:** no background fill; colored text only using terminal syntax colors (`#3FB950` active, `#F78166` error, `#8B949E` offline). Still use `status-pill` variant but strip bg and border.

**Signal:** ALL CAPS text, monospace, tight `letter-spacing: 0.10em`. Use `dot-label` variant; signal-theme glow class permitted on active dot only.

**Ash:** grayscale only — no color on badges. Use `#D0D0D0` for active, `#888888` for warning, `#555555` for error/offline, small-caps style.

## Step-connector badge override

When used as step-number badges in `step-connector` snippet, override to circle (default and glasspaper themes) or hard square (terminal/forge/ash themes):

```css
/* Circle number badge */
.step-badge {
  width: 32px;
  height: 32px;
  border-radius: 50%;   /* circle */
  background: var(--accent-1);
  color: var(--on-accent, #0F1115);
  display: flex; align-items: center; justify-content: center;
  font: 700 14px/1 'Montserrat', sans-serif;
  flex-shrink: 0;
}

/* Square number badge (terminal/forge/ash) */
.step-badge-square {
  width: 32px;
  height: 32px;
  border-radius: 0;     /* hard square */
  background: var(--accent-1);
  color: var(--on-accent, #0F1115);
  display: flex; align-items: center; justify-content: center;
  font: 700 14px/1 monospace;
  flex-shrink: 0;
}
```

## Variant 4: numbered-step badge

Small numbered chip used in card corners or step-flow nodes. Pure number, no label.

```html
<span class="badge-num">01</span>
<span class="badge-num badge-num--filled">02</span>

<style>
.badge-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 28px;
  height: 28px;
  padding: 0 8px;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, var(--accent-1) 45%, transparent);
  background: transparent;
  color: var(--accent-1);
  font: 700 14px/1 'Bebas Neue', 'Montserrat', sans-serif;
  letter-spacing: 0.05em;
  font-variant-numeric: tabular-nums;
}
.badge-num--filled {
  background: var(--accent-1);
  color: var(--on-accent);
  border-color: var(--accent-1);
}

/* Corner-mounted on a card: */
.card { position: relative; }
.card .badge-num--corner {
  position: absolute;
  top: -14px;
  right: 14px;
}
</style>
```

Use cases:
- Top-right corner of cards in a numbered grid (1, 2, 3, 4).
- Inline at the start of step-connector nodes.
- Paired with `tagged-header` for "01 — DISCOVERY" style labels.

Rules:
- Always tabular numerals (`font-variant-numeric: tabular-nums`) so 01/10 stay the same width.
- Use 2-digit zero-padded format (`01`, `02` … `09`) for ≤ 9 steps. Drop the zero only when count exceeds 9.
- Mix filled + outlined only when there's a "current step" — filled = current/active, outlined = upcoming. Otherwise pick one variant per infographic.

## Rules

- Never add a container div or circular bg behind a Phosphor icon — that is a separate icon rule from `icons.md`. Badge backgrounds here are for text-based status labels only.
- Use exactly one badge variant per infographic — do not mix pill + dot-label.
- Numbered-step badges may co-exist with one other badge variant since they serve different semantics (sequence vs status).
- In Ash theme: no color. Use only the 4 defined gray stops.
