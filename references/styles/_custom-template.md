# _custom-template — Blank Style Scaffold

Copy this file to `references/styles/<your-style-name>.md` and fill in the values. Leading underscore keeps it sorted first in directory listings and marks it as a scaffold, not a usable style.

## When to use

Create a new style when:
- A specific brand has mandatory colors / fonts that the existing styles can't accommodate
- A content type has a distinct mood not covered (e.g., wedding announcement, medical infographic)
- You're doing a one-off piece that needs a unique visual identity

Do NOT create a new style just to tweak aizfographics slightly — override tokens inline instead.

## Required fields

Every style file must define:

1. **Header** — style name, one-line mood description
2. **When to use** — bullet list, 3–5 triggers
3. **CSS variables** — complete block matching the aizfographics-style token structure
4. **Typography** — font pair, Google Fonts link, per-role sizing table
5. **Decorative DNA** — borders, glow/no-glow, backgrounds, signature treatments
6. **Component DNA** — hero, badges, cards, connectors, footer treatments
7. **When to use / When NOT to use** — final two bullet lists

## CSS variable template

```css
:root {
  /* canvas */
  --canvas:        #______;
  --panel:         #______;
  --elevated:      #______;

  /* text */
  --text-primary:   #______;
  --text-secondary: #______;
  --text-muted:     #______;
  --on-accent:      #______;

  /* accent pair (can be same value for single-accent styles) */
  --accent-1: #______;
  --accent-2: #______;

  /* semantic */
  --positive: #______;
  --negative: #______;

  /* spacing */
  --gap-section:   __px;
  --gap-element:   __px;
  --gap-card:      __px;
  --pad-container: __px;

  /* radius */
  --radius-card: __px;
  --radius-pill: __px;
  --radius-btn:  __px;
}
```

## Typography template

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=______&family=______&display=swap">
```

| Role | Font | Weight | Case | Size |
|------|------|--------|------|------|
| Hero title | ______ | ___ | ______ | __–__px |
| Section title | ______ | ___ | ______ | __–__px |
| Card title | ______ | ___ | ______ | __–__px |
| Body | ______ | ___ | Sentence | __–__px |
| Caption | ______ | ___ | ______ | __–__px |

## Design decision checklist

Before publishing a new style, answer:

- [ ] Is dark or light the default canvas?
- [ ] Single accent or pair?
- [ ] Uppercase headers, or title case, or sentence case?
- [ ] Gradient text allowed, flat only, or disabled?
- [ ] Glow / shadow / flat?
- [ ] Gradient borders or hairline solid?
- [ ] Rounded corners, sharp, or irregular?
- [ ] Scan lines / noise / grid overlay?
- [ ] Phosphor icon weight (thin/regular/bold/fill/duotone)?

Each decision should be explicitly stated in the style doc — no "use your judgment" — otherwise two infographics under the same style will diverge.

## Publishing

1. Create `references/styles/<your-style-name>.md`
2. Fill every section — use other styles as reference
3. Test by generating one infographic in each of 2–3 template types (tokenomics, ecosystem, cheatsheet) to validate the style works across content shapes
4. Update this skill's SKILL.md if the new style deserves first-class routing (e.g., content type X always uses this style)

## Style review checklist

When reviewing outputs in a new style:

- [ ] Consistent typography — exactly 2 fonts throughout
- [ ] Consistent spacing — same gaps, same padding
- [ ] Consistent accent usage — same color story per infographic
- [ ] Readable body copy at 14–16px
- [ ] KPI values stand out from labels
- [ ] No surprise color introductions (off-palette hex)
- [ ] Decorative elements serve structure, not decoration

If any box is unticked, the style spec has a gap that needs filling in.
