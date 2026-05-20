# terminal — Shell Output Style

Concept: Shell output. Data is program output. The user is reading a process.

100% monospace, left-aligned, GitHub-dark palette. Box-drawing for structure. No circles, no rounded shapes, no icons.

## When to use

- Technical data, process output, protocol specs
- Developer-facing infographics
- Log-style timelines and status feeds
- Any content where a technical, no-decoration aesthetic is the point

## CSS variables

```css
:root {
  /* canvas */
  --canvas:          #0D1117;
  --panel:           #161B22;
  --elevated:        #1C2230;

  /* text — terminal syntax roles (never swap) */
  --text-primary:    #E6EDF3;   /* default output text */
  --text-secondary:  #A5D6FF;   /* strings / labels (pale blue) */
  --text-muted:      #8B949E;   /* comments / metadata (gray) */
  --on-accent:       #0D1117;

  /* accent — syntax color roles (fixed semantic, do not reassign) */
  --accent-1:        #3FB950;   /* prompts / section headers (green) */
  --accent-2:        #79C0FF;   /* values / numbers (blue) */
  --accent-error:    #F78166;   /* errors / negatives (red-orange) */
  --accent-string:   #A5D6FF;   /* strings / labels (pale blue) */
  --accent-comment:  #8B949E;   /* comments / metadata (gray) */

  /* semantic */
  --positive: #3FB950;
  --negative: #F78166;

  /* border */
  --border:          #30363D;   /* hairline, 0.5-1px only */

  /* spacing — compact, dense */
  --gap-section:     24px;
  --gap-element:     12px;
  --gap-card:        8px;
  --pad-container:   16px;

  /* radius — none */
  --radius-card:  0px;
  --radius-pill:  0px;
  --radius-btn:   0px;
}
```

## Typography

One font only: monospace. No sans-serif, no display font, no serif.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
```

Use `'JetBrains Mono', 'Fira Code', monospace` in all font-family declarations.

| Role | Weight | Case | Size | Letter-spacing |
|------|--------|------|------|----------------|
| Hero title / section header | 700 | UPPERCASE | 18-24px | 0.02em |
| Item label / prompt line | 700 | lowercase or UPPERCASE | 13-14px | 0 |
| Value / number | 400 | as-is | 14-18px | 0 |
| Body copy | 400 | Sentence | 13-14px | 0 |
| Metadata / comment | 400 | Sentence | 11-12px | 0 |

Minimum font size: 11px. Body: 14px. Major values: 18px.

## Layout rules

- **Left-align always.** No centering, no right-align.
- **Section dividers:** `────────────────` (box-drawing `─` U+2500) or `════════` for major breaks. Never gap alone.
- **Hierarchy via indentation:** 2-space or 4-space. Not via size differences.
- **Prompt lines:** `$ command --flag value`
- **Arrow outputs:** `→ result`
- **Tree structures:** `└─ child`, `├─ sibling`, `│  nested`
- **Timestamps:** `[2026-05-20 23:14:08]`

## Decorative DNA

### Cards / containers

Flat dark rectangles. Hairline border only (0.5-1px). No radius, no shadow, no glow.

```css
.card {
  background: var(--panel);
  border: 1px solid var(--border, #30363D);
  border-radius: 0;
  padding: 16px;
}
```

### No decorative elements

No gradients, no glows, no rounded corners, no icons, no emoji, no decorative shapes. Structure comes entirely from indentation, box-drawing characters, and the 5-color syntax palette.

### Color usage (strict semantic roles)

```css
/* Green: prompts, section headers, positive state */
.prompt, .section-header { color: #3FB950; }

/* Blue: values, numbers */
.value, .number { color: #79C0FF; }

/* Red-orange: errors, negatives */
.error, .negative { color: #F78166; }

/* Pale blue: strings, labels */
.label, .string { color: #A5D6FF; }

/* Gray: comments, metadata */
.comment, .meta { color: #8B949E; }
```

Never use one syntax color in another's semantic role.

### Prompt-style headers

```html
<div class="term-section">
  <div class="term-prompt">$ infographic --section tokenomics</div>
  <div class="term-divider">────────────────────────────────</div>
  <div class="term-content">
    <!-- section content -->
  </div>
</div>

<style>
.term-prompt {
  font: 700 14px/1.5 'JetBrains Mono', monospace;
  color: #3FB950;
}
.term-divider {
  font: 400 12px/1 'JetBrains Mono', monospace;
  color: #30363D;
  letter-spacing: -0.02em;
}
</style>
```

## Badge / status pill override

No background fill. Colored text only. Use syntax role colors.

```css
/* terminal badge: text only, no bg */
.badge-pill {
  background: transparent;
  border: none;
  padding: 0;
  font: 700 11px/1 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}
.badge-active  { color: #3FB950; }
.badge-error   { color: #F78166; }
.badge-offline { color: #8B949E; }
```

## Progress bar override

Use ascii-bar variant from `progress-bars.md`. No graphical bars.

## Step-connector override

Square badges (not circles), monospace labels, no arrow tip on connector lines.

## Gradient text

Disabled. All text is flat syntax colors.

## Glow effects

Disabled. No `text-shadow`, no `box-shadow`.

## Style verification checklist

- [ ] One font family: `'JetBrains Mono', 'Fira Code', monospace` everywhere
- [ ] No rounded corners (`border-radius: 0` on all cards)
- [ ] Left-aligned only — no `text-align: center`
- [ ] Syntax colors used only in their defined semantic role
- [ ] No gradients, glows, icons, or emoji
- [ ] Box-drawing chars for dividers, not `<hr>` or gap-only

## What to avoid

Gradients, glows, rounded corners, sans-serif, centered text, decorative icons, filled backgrounds on badges, shadow effects.
