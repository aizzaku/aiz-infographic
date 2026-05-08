# Infographic Skill — Revised Architecture (Post-DNA Analysis)

## Question 1: SVG vs HTML — The Right Path

### The honest answer: HTML-first with SVG export, not the other way around

After thinking hard about this, I'm reversing my earlier recommendation. Here's why:

**SVG pain points you've already hit:**
- SVG text wrapping is a nightmare — no native word-wrap, you have to manually calculate `<tspan>` positions
- SVG has no `flexbox`, no `grid`, no `overflow: hidden` — all positioning is absolute coordinates
- Complex layouts (your 3-6 section infographics) require hand-computing every x/y position
- Font rendering in SVG is inconsistent across viewers (browser vs Figma vs Inkscape)
- SVG filters (glow, blur, drop-shadow) render differently everywhere
- Figma's SVG import doesn't always work — you've experienced this firsthand

**HTML advantages for your use case:**
- CSS Grid/Flexbox handles your layout patterns naturally (your data shows 1-col: 68%, 2-col: 26%, 3-col: 6%)
- Web fonts load reliably (Bebas Neue, Montserrat, Orbitron — your top 3)
- CSS `box-shadow`, `backdrop-filter`, gradients, `background-blend-mode` — all your decorative DNA (glow effects 57%, gradient overlays 59%, geometric shapes 81%) work natively
- Opens in any browser instantly
- Responsive by default

### The architecture: HTML → PNG + SVG export

```
PRIMARY OUTPUT:   .html  (single-file, self-contained, opens in browser)
EXPORT 1:         .png   (via Puppeteer/Playwright screenshot)
EXPORT 2:         .svg   (via html-to-svg conversion, best-effort)
```

**How each export works:**

**PNG export (most reliable):**
- Use Puppeteer (already available in Claude Code environments)
- `puppeteer.launch()` → `page.setViewport()` → `page.screenshot({type: 'png'})`
- Pixel-perfect, works every time
- This is what most people actually need for social media, presentations, docs
- Script goes in `scripts/export-png.sh` (5 lines of bash calling a Node script)

**SVG export (best-effort for Figma):**
- Use `dom-to-svg` or `html-to-image` library
- Not perfect for every layout, but covers 80%+ of cases
- When it breaks: the HTML file is still the canonical output, and the user can use html.to.design Figma plugin as fallback
- Script goes in `scripts/export-svg.sh`

**HTML export (always works):**
- The HTML IS the primary output — it's always there
- Single-file with inlined CSS + fonts via Google Fonts `<link>`
- No external dependencies except font CDN

### What happens when SVG export breaks?

The skill should include a fallback chain in the SKILL.md:

```
## Export Priority
1. Always output the .html file (primary — always works)
2. Run PNG export script → save alongside .html
3. Attempt SVG export → if it fails, inform the user:
   "SVG export had rendering issues with this layout. 
    You can use the html.to.design Figma plugin to import 
    the HTML directly, or use the PNG for other purposes."
```

This way you never have a broken output — there's always a working deliverable.

### Free tools for export

| Tool | What it does | How to get it |
|------|-------------|---------------|
| Puppeteer | HTML → PNG screenshot | `npm install puppeteer` (free, open source) |
| dom-to-svg | HTML → SVG conversion | `npm install dom-to-svg` (free, open source) |
| html.to.design | HTML → Figma layers | Figma plugin (free tier available) |
| Playwright | Alternative to Puppeteer | `pip install playwright` (free, open source) |

All free, all work in Claude Code and on your Beelink.

---

## Question 2: Injecting Your DNA Into the Design System

Your 175-image analysis is a goldmine. Here's what it tells us about your design DNA and how to encode it.

### Your DNA fingerprint (extracted from analysis)

```yaml
# THE AIZFOGRAPHICS DNA

identity:
  mood: bold, futuristic (100% of 175 images)
  background: dark (default), light (available)
  hierarchy: strong (100%)
  density: compact (73.7%)
  balance: asymmetric (72%)
  flow: top-to-bottom (87.4%)

colors:
  dark_mode:
    background: "#0F1115"
    text: "#E6E6E6"
  light_mode:
    background: "#F5F5F5"
    text: "#1A1A1A"
  accent_system: one color per infographic, 60-30-10 rule
  accent_pairing: monochromatic (two shades) or analogous (two neighbors)
  default_pairs:
    - ["#F3A950", "#F38150"]  # warm amber → burnt orange
    - ["#FFBB00", "#FF8800"]  # golden yellow → deep orange
    - ["#B2FF00", "#FFCC00"]  # lime → gold
    - ["#FF0048", "#FF336D"]  # hot red → pink
    - ["#67B39F", "#CEDFCC"]  # sage → mint
    - ["#00FF90", "#00F6FF"]  # green → cyan
  accent_selection: Claude picks based on content when user has no preference
  semantic_positive: "#00D018"
  semantic_negative: "#D0002D"
  saturation: vibrant (88.6%)

typography:
  rule: always exactly 2 fonts per infographic
  default_pair:
    display: Bebas Neue (hero title only)
    body: Montserrat (bold/caps for headers, regular for body)
  alt_pairs:
    retro: [Press Start 2P, VT323]
    playful: [Jua, Capriola]
    technical: [Kode Mono, Space Mono]
  behavior:
    uppercase: titles and headers always
    gradient_text: same-color lighter→darker at 30° for title emphasis
    body_emphasis: flat accent color only, never gradient

components:
  hero_section: 98.9% (full-bleed: 53%, split: 28%, boxed: 19%)
  badges_tags: 92.0%
  feature_cards: 82.3% (outlined: 45%, flat: 21%, filled: 20%)
  callout_box: 65.7%
  footer: 60.0%
  comparison_table: 34.3%
  stats_bar: 33.7%
  timeline: 28.6% (horizontal: 88%, vertical: 12%)
  progress_bars: 25.1%
  icons: 98.9% (custom-illustration: 41%, filled-svg: 41%)
  arrows_connectors: 70.9% (straight: 87%, curved: 10%)

styling:
  border_radius: rounded 8-12px (48%) or slight 2-4px (28%)
  borders: gradient (accent ~20% → transparent or ~40%), NEVER single-sided thick
  shadows: subtle (61%), glow (17%), none (22%)
  dividers: solid-line (90%)
  decorative:
    geometric_shapes: 81.1%
    gradient_overlays: ~5% opacity, same accent color
    glow_effects: same accent color, low opacity
    noise_texture: optional (9.1%)

dimensions:
  portrait_medium: 41% (3:4 or A4)
  portrait_tall: 22% (9:16)
  landscape: 18% (16:9)
  square: 6% (1:1)
```

### How to encode this: NOT in Figma — in the reference files

Here's the key insight: **you don't need to create atomic designs in Figma first.** Your design system lives in the SKILL.md reference files, not in a visual design tool. Here's why:

1. **Your "designs" are produced by Claude writing code.** Figma components don't help Claude write better HTML/CSS. What helps is explicit rules with exact values.

2. **Your DNA analysis already IS the design spec.** The catalog.json contains more precise design information than most Figma component libraries. You just need to encode it as rules.

3. **Figma is for the output (editing), not the input (generation).** Use Figma/Pencil for final tweaks on individual infographics, not for defining the system.

### Where the DNA goes in the skill architecture

The DNA splits across two types of reference files:

**Style files** (`references/styles/`) — encode the VISUAL tokens:
- Colors, fonts, spacing, decorative treatments
- This is your `aizfographics-style` default, extracted directly from the analysis

**Template files** (`references/templates/`) — encode the STRUCTURAL patterns:
- Specific infographic blueprints for recurring use cases
- These are NOT generic layouts — they're YOUR layout patterns from the 175 analyzed images

Think of it this way:
- **Layouts** = generic structural shapes (timeline, comparison, funnel...) — reusable across any brand
- **Styles** = your color/font/decoration DNA — makes any layout look like YOUR work
- **Templates** = layout + style + domain-specific content structure — for recurring infographic types you make often

### The DNA style file: `references/styles/aizfographics-style.md`

```markdown
# aizfographics-style — Default Style

## Source
Based on analysis of 175 infographics, refined with updated 
design preferences (April 2026).

---

## Font System

### Rule: Always exactly 2 fonts per infographic

Every infographic uses one display font + one body font. Never three. 
Never one. The default pair is Bebas Neue + Montserrat.

### Default Pair: Bebas Neue + Montserrat

| Role | Font | Weight | Case | Usage |
|------|------|--------|------|-------|
| Hero title | Bebas Neue | 400 (inherently bold) | UPPERCASE | The single biggest text element on the page. One per infographic. |
| Section titles, card headers, item labels | Montserrat | 700 (Bold) | UPPERCASE | All structural headings below hero level. |
| Body text, descriptions, captions, footnotes | Montserrat | 400 (Regular) | Sentence case | All readable content. |

- Bebas Neue: letter-spacing 0.05-0.1em, size 36-64px
- Montserrat Bold: letter-spacing 0.04-0.08em, size 16-24px
- Montserrat Regular: size 13-16px, line-height 1.5

### Alternative Pairs (on request or thematic match)

These replace BOTH default fonts. Ask the user or detect thematic fit.

| Pair | Display | Body | When to use |
|------|---------|------|-------------|
| Retro/Pixel | Press Start 2P | VT323 | Gaming, 8-bit, retro arcade, pixel art content |
| Playful/Rounded | Jua | Capriola | Casual, fun, kids, community, non-technical content |
| Technical/Code | Kode Mono | Space Mono | Developer tools, code-heavy, protocol specs, technical docs |

When using an alternative pair, the same role rules apply: display font 
for hero title only, body font for everything else (bold for headers, 
regular for body text).

### Removed Fonts (do NOT use)
Teko, Orbitron, Rajdhani, Bungee, Space Grotesk, Barlow Condensed,
Inter, Poppins, Avenir Next, IBM Plex Mono, Cinzel, Cinzel Decorative.

---

## Typography Behavior

### Uppercase Rules
- Hero titles: ALWAYS uppercase
- Section headers, card titles, item labels, badges: ALWAYS uppercase
- Body text, descriptions, captions: Sentence case (never uppercase)

### Gradient Text (for titles and headers ONLY)
Use a gradient of the SAME accent color — lighter shade to darker shade 
at a 30-degree angle. Apply to full or partial text in titles and headers 
for emphasis.

CSS pattern:
background: linear-gradient(30deg, {accent-light}, {accent-dark});
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;

Example with amber accent:
background: linear-gradient(30deg, #FFD080, #E08A20);

Rules:
- ONLY on titles and headers (hero title, section titles)
- Can be full text or partial (highlighting a key word)
- Never on body text — body uses flat colors only
- The gradient should be subtle (same hue, different lightness), 
  not a rainbow or cross-hue gradient

### Body Text Emphasis
- For highlighted/important body text: use flat accent color
- For secondary emphasis: use bold weight (700)
- NEVER use gradient fills on body text

---

## Color System

### Mode-Based Backgrounds & Text

| Token | Dark Mode (default) | Light Mode |
|-------|-------------------|------------|
| canvas | #0F1115 | #F5F5F5 |
| panel | #161A20 | #EBEBEB |
| elevated | #1C2028 | #E0E0E0 |
| text-primary | #E6E6E6 | #1A1A1A |
| text-secondary | #A0A0A8 | #4A4A4A |
| text-muted | #606068 | #808080 |
| on-accent | #0F1115 | #F5F5F5 |

Dark mode is the default. Light mode is available via toggle or user request.
For light mode, darken the accent color pairs for sufficient contrast.

### Accent Color System

**Core rule: ONE accent color per infographic** unless the user requests 
more or the content thematically requires it (e.g., comparing two brands 
with different colors).

**Color strategy: 60-30-10 rule**
- 60% — background (canvas + panel)
- 30% — neutral/structural (text, borders, dividers)
- 10% — accent (highlights, titles, key data, interactive elements)

**Color pairing: Monochromatic or Analogous**
Each accent comes as a pair of two colors:
- Monochromatic: two shades of the same hue (lighter for titles, darker for supporting elements)
- Analogous: two adjacent colors on the color wheel

Use gradients between the pair (lighter → darker) for visual richness. 
The lighter shade is for primary emphasis (hero title, key stats). 
The darker shade is for secondary emphasis (section headers, borders, badges).

### Default Accent Pairs

Claude selects the best-fit pair based on content/topic when the user 
has no preference. If the infographic is for a specific brand, match 
the brand's primary and secondary colors instead.

| # | Primary | Secondary | Character | Best for |
|---|---------|-----------|-----------|----------|
| 1 | #F3A950 | #F38150 | Warm amber → burnt orange | Finance, tokenomics, general-purpose |
| 2 | #FFBB00 | #FF8800 | Golden yellow → deep orange | Announcements, launches, energy |
| 3 | #B2FF00 | #FFCC00 | Lime → gold | Growth, ecosystems, DeFi |
| 4 | #FF0048 | #FF336D | Hot red → pink | Alerts, competition, NFTs, bold statements |
| 5 | #67B39F | #CEDFCC | Sage → mint | Calm, educational, health, sustainability |
| 6 | #00FF90 | #00F6FF | Green → cyan | Tech, protocol, futuristic, web3 |

### Semantic Colors (fixed, not paired)
- Positive: #00D018 (success, gains, correct, up)
- Negative: #D0002D (error, loss, wrong, down)

### Chart Series
When a chart needs multiple distinct colors (pie segments, bar groups), 
use the primary color from each pair in order:
[#F3A950, #00FF90, #FF0048, #FFBB00, #67B39F, #B2FF00]

If 2-3 segments: use the selected pair's primary + secondary + one neighbor.
If 4+ segments: pull primaries from different pairs for maximum distinction.

---

## Spacing & Layout

### Density (compact is default — 73.7% of existing work)
- section-gap: 32-40px
- element-gap: 16-20px
- container-padding: 16-24px
- card-gap: 12-16px

### Border Radius
- cards/containers: 8-12px
- badges/tags: 4-6px
- buttons/CTAs: 6-8px
- full-round pills: 50% (for small status indicators)

---

## Decorative DNA

### Geometric Shapes (almost always present)
- Rectangular panels with rounded corners
- Angled divider lines
- Grid-like table structures
- Badge/tag pill shapes
- Use as structural elements, NOT random decoration

### Glow Effects
- Same accent color at low opacity
- box-shadow: 0 0 20px rgba(accent, 0.12) on key elements
- text-shadow: 0 0 10px rgba(accent, 0.25) on hero text (sparingly)

### Gradient Overlays (for background cards, sections)
- Same accent color at ~5% opacity fading to transparent
- Direction: top-to-bottom or diagonal
- Use on hero sections, feature cards, content panels
- Subtle — the color should be barely perceptible

### Borders
- Gradient borders using the accent pair:
  ~20% opacity → transparent, or ~20% → ~40% opacity
- Apply as full-perimeter borders (all sides)
- NEVER use single-sided thick borders (no border-top: 3px, 
  no border-left: 4px, no accent bar on one edge only)
- CSS pattern: border-image with linear-gradient, or 
  pseudo-element overlay for more control

CSS example:
border: 1px solid transparent;
border-image: linear-gradient(
  135deg, 
  rgba(accent, 0.2), 
  rgba(accent, 0.4)
) 1;

Or for rounded corners (border-image doesn't support border-radius):
background: linear-gradient(var(--canvas), var(--canvas)) padding-box,
            linear-gradient(135deg, rgba(accent, 0.2), rgba(accent, 0.4)) border-box;
border: 1px solid transparent;
border-radius: 10px;

### Background Treatment
- Dark mode: solid #0F1115
- Light mode: solid #F5F5F5
- Optional: radial gradient vignette from center (very subtle)
- Optional: noise/grain texture at 3-5% opacity

---

## Component DNA

### Hero Section (98.9% — nearly universal)
- Full-bleed: left-aligned title, full-width background
- Split-layout: image/illustration left, text right (or reversed)
- Boxed: contained within border, centered
- Hero title uses gradient text effect (accent lighter → darker at 30°)

### Badges/Tags (92.0%)
- Small pill shapes with accent background at 10-15% opacity
- Uppercase Montserrat Bold, 10-12px, letter-spacing 0.05em
- Often used for category labels, chain names, status indicators

### Feature Cards (82.3%)
- Outlined style (45%): transparent bg + gradient border
- Flat style (21%): solid panel bg, no border
- Filled style (20%): accent at ~5% opacity fill + gradient border
- NEVER single-sided border accent (top, bottom, or side bar)

### Connectors (70.9%)
- Straight arrows: 87% (simple, direct)
- Curved: 10% (process flows)
- Color: accent at 60% opacity, or muted text-secondary

### Footer (60%)
- Attribution text: text-muted color, Montserrat Regular 11px
- Logo + URL when present
- Always bottom-aligned, never dominant
```

### Where does Figma fit then?

Figma is useful for ONE thing in this workflow: **visual QA and final edits.** After Claude generates an infographic, you export it (HTML → Figma via plugin, or SVG), then tweak spacing, swap colors, adjust text — the stuff that's faster with a mouse than with a prompt.

You could also create a Figma "reference board" of your 175 analyzed images organized by type, to show Claude as visual examples when you want a specific layout. But the design system itself lives in markdown, not in Figma components.

---

## Question 3: Domain-Specific Templates

Yes — and this is where your DNA analysis becomes extremely powerful. Your data shows 11 clear infographic types with distinct structural patterns. These should become **templates** in the skill.

### Templates vs Layouts vs Styles

| Concept | What it defines | Example |
|---------|----------------|---------|
| **Layout** | Generic structural shape | "timeline", "comparison", "funnel" |
| **Style** | Visual identity tokens | "aizfographics-style", "clean-minimal" |
| **Template** | Layout + style + domain structure | "token-economics", "ecosystem-overview" |

A template is a PRESET that combines a specific layout with domain-specific section names, content expectations, and your default style. It's the "I make this exact type of infographic regularly" shortcut.

### Your templates (from the 175-image analysis)

```
references/templates/
├── token-economics.md       # 62 images (35.4%) — your #1 type
├── crypto-explainer.md      # 29 images (16.6%)
├── game-overview.md          # 25 images (14.3%)
├── ecosystem-overview.md     # 22 images (12.6%)
├── airdrop-guide.md          # 17 images (9.7%)
├── nft-showcase.md           # 6 images (3.4%)
├── how-it-works.md           # 6 images (3.4%)
├── report.md                 # 4 images (2.3%)
├── comparison.md             # 2 images (1.1%)
├── cheatsheet.md             # (new — you mentioned this)
└── game-mechanics.md         # (new — you mentioned this)
```

### Example: `references/templates/token-economics.md`

```markdown
# Token Economics Template

## When to use
User asks about tokenomics, token distribution, vesting schedules,
supply allocation, TGE info, or any token-related data visualization.

## Base layout
Use the "statistical" layout as the structural foundation.

## Default style
aizfographics-style

## Expected sections (in order)

### 1. Header Strip
- Left: token name/ticker in accent color + "TOKENOMICS" label
- Right: project logo
- Separator: thin horizontal rule

### 2. Key Metrics Strip
- 3-4 boxed metrics in a row: Total Supply, Initial Price, FDV, TGE Date
- Use data-widget: big-number style
- Centered, equal spacing

### 3. Distribution Chart (hero)
- Pie chart OR donut chart (23 of 62 tokenomics images use pie)
- Flanked by allocation cards (left and right stacked info cards)
- OR: horizontal segmented bar showing allocation percentages
- Each segment: category label + percentage + optional vesting note

### 4. Vesting Schedule
- Horizontal timeline (88% of your timelines are horizontal)
- Segmented bars showing unlock progression
- Lock icons for cliff periods
- Percentage labels at key milestones
- Mini bar charts per allocation category

### 5. Allocation Details
- Feature cards (outlined style) for each allocation category
- Each card: category name, percentage, token amount, vesting terms
- 2-column layout

### 6. Footer
- Source attribution, disclaimer text
- Project logo small, bottom-right

## Required elements
- charts.md: pie/donut chart, horizontal segmented bar, mini bar charts
- data-widgets.md: big-number, progress-bar
- connectors.md: timeline spine, allocation connector lines
- text.md: all levels
- layout.md: grid, containers
- decorative.md: background, geometric accent shapes

## Content expectations (what the user should provide)
- Token name and ticker
- Total supply
- Allocation categories with percentages
- Vesting terms per category (cliff, unlock schedule)
- Optional: TGE date, initial price, FDV
```

### Example: `references/templates/ecosystem-overview.md`

```markdown
# Ecosystem Overview Template

## When to use
User asks about ecosystem, integrations, partnerships, deployments,
or project landscape visualization.

## Base layout
Use the "grid-cards" layout with a "list" sub-layout for partners.

## Default style
aizfographics-style

## Expected sections (in order)

### 1. Header
- Left: project name + "ECOSYSTEM OVERVIEW"
- Right: project logo
- Short one-line chain/platform subtitle

### 2. Category Sections (repeating)
For each ecosystem category (Integrations, Deployments, Partners, etc.):
- Section header pill (accent-colored badge)
- 2-3 column grid of partner entries
- Each entry: circular/square logo + name + category tag + one-line description
- Dense layout (your ecosystem infographics are information-heavy)

### 3. Footer
- Attribution, bottom-right logo

## Required elements
- icons.md: logo placeholders, category badges
- layout.md: grid (2-3 columns), section containers
- text.md: section headers, partner names, descriptions, tags
- decorative.md: section header pills, dividers

## Content expectations
- List of ecosystem partners/integrations
- Categories for grouping
- Optional: logos (as image URLs or placeholders)
```

### Example: `references/templates/cheatsheet.md`

```markdown
# Cheatsheet Template

## When to use
User asks for a cheatsheet, quick reference, pocket guide,
or condensed how-to for a game, protocol, or system.

## Base layout
Use the "list" layout with dense card grid.

## Default style
aizfographics-style

## Expected sections

### 1. Header
- Bold title: "[TOPIC] CHEATSHEET"
- Optional: version/date badge

### 2. Quick Stats Strip
- 3-5 key metrics/facts in a horizontal row
- Boxed, compact

### 3. Content Blocks (repeating)
For each topic area:
- Section header with numbered badge or icon
- Dense bullet list OR comparison table
- Feature cards with outlined borders
- Tips/warnings in callout boxes

### 4. Quick Reference Table
- Comparison table for key values
- Compact, no wasted space

### 5. Footer
- Source, attribution

## Content expectations
- Topic name
- Key sections with bullet points
- Any reference tables or value lookups
```

---

## Design Source Philosophy

How the design for each layer is authored, and where the visual decisions come from.

### Elements — Guided Improvisation (Source C)

Element files contain **design rules + a reference HTML/CSS example**, not rigid copy-paste templates. Claude follows the rules but adapts to the specific content.

Why this approach: the 175-image analysis shows infographics that are consistent in *feel* but not identical in *structure*. Donut charts across different tokenomics pieces use the same color system and spacing density, but vary in segment count, label placement, and supporting elements. Claude needs to understand the *design intent* and adapt.

Each element file contains:
- **When to use** — what data shape or content calls for this element
- **Design rules** — exact CSS values (font sizes, spacing, colors, border-radius) derived from the 175-image DNA analysis
- **HTML/CSS pattern** — a concrete code block Claude can adapt, not copy verbatim
- **Variations** — alternative configurations (e.g., KPI strip of 3 vs 4 items)

Element files are **style-agnostic in structure, style-specific in their example code**. The structural pattern (how to build a donut chart) works with any style. The example code uses aizfographics-style tokens. When a different style is selected, Claude swaps the tokens.

Design rule sources:
- **Font choices** → `patterns-summary.json` (Bebas Neue 43%, Montserrat 57%)
- **Sizing and spacing** → `catalog.json` density distribution (compact 74%)
- **Color application** → color palette extraction (teal, orange, pink accents)
- **Component patterns** → component prevalence data (stats bar 34%, badges 92%)
- **Decorative treatments** → decorative element data (glow 57%, geometric shapes 81%)

For element types NOT in the existing work (maps, Sankey diagrams, etc.): the element file describes the structural pattern without aizfographics-specific styling. The style gets applied from the style file at composition time. Build these only when a real project demands them.

### Layouts — Spatial Grammar, Not Pixel Coordinates

Layout files define **section order, grid zones, proportions, and adaptation rules** — not exact pixel positions. Claude interprets these rules and generates CSS Grid/Flexbox code at runtime, adapted to the content volume.

Layout sources (in priority order):
1. **Existing work patterns** (primary) — extracted from 175 `layout_pattern` descriptions in `catalog.json`. The recurring structural skeletons for tokenomics (35%), ecosystem (13%), game-overview (14%) are directly encoded.
2. **Established infographic conventions** (secondary) — for types not well-represented in existing work (flowcharts, mind maps, fishbone), standard information design practice provides the spatial relationships.
3. **Professional tool references** (tertiary) — Venngage, Piktochart, Canva layout grids for proportion and flow reference. Not for visual style, only spatial grammar.

Each layout file contains:
- **Section order** — what zones exist and their sequence
- **Grid specifications** — per-dimension (portrait 3:4, landscape 16:9, etc.) with zone heights, column counts, gaps
- **Required element files** — which element categories are needed
- **Composition rules** — visual weight distribution, information flow direction
- **Adaptation guidance** — how the layout flexes for 3 vs 8 data items, thin vs dense content

### Styles — Locked Visual Tokens

Style files are **fully prescriptive**. Every color, font, spacing value, and decorative rule is defined. Claude does not improvise visual design — it applies the tokens exactly.

`aizfographics-style.md` is derived from the 175-image DNA analysis. Other styles (clean-minimal, blueprint, etc.) are authored from scratch using the same token structure.

### Templates — Presets That Combine All Three

Template files specify: which layout + which style + domain-specific section names and content expectations. They're the "I make this exact type of infographic regularly" shortcut.

Template sources: the 11 infographic types identified in the DNA analysis, plus new types (cheatsheet, game-mechanics).

### What Claude Creates vs What's Pre-Designed

| Layer | Pre-designed (in reference files) | Claude creates at runtime |
|-------|-----------------------------------|--------------------------|
| Style | All tokens — colors, fonts, spacing, decorative rules | Nothing — style is locked |
| Layout | Section order, grid zones, proportions, adaptation rules | Exact CSS Grid code, section heights based on content volume |
| Elements | Design rules + HTML/CSS patterns | Actual HTML with real data (segment counts, labels, values) |
| Template | Layout + style + section names + content expectations | Content parsing, data extraction, filling sections |
| Composition | Nothing (this is Claude's job) | Connecting everything — matching data to chart types, sizing sections, handling edge cases |

Claude's creative contribution is **composition and adaptation** — not visual design. The SKILL.md also includes heuristic rules for edge cases (e.g., "if any pie segment exceeds 75%, switch to a horizontal bar").

---

## Icon System

No emoji. Ever. All icons use professional open-source SVG icon packs.

### Primary: Phosphor Icons (Bold weight)

Phosphor is the default icon library. Use the **bold** weight — it matches the compact, high-contrast aizfographics aesthetic. Available via jsDelivr CDN as a webfont.

**How to include in the HTML output:**
```html
<link rel="stylesheet" 
  href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/bold/style.css"/>
```

**How to use:**
```html
<i class="ph-bold ph-chart-pie" style="color: var(--accent-1); font-size: 20px;"></i>
<i class="ph-bold ph-lightning" style="color: var(--accent-2); font-size: 24px;"></i>
```

Phosphor has 1,000+ icons across 6 weights (thin, light, regular, bold, fill, duotone). Bold is the default for aizfographics-style. Fill can be used for emphasis or active states.

### Fallback: Iconify API (for anything Phosphor doesn't have)

Iconify provides 200,000+ icons across 100+ sets via a public API that generates SVG on demand. Use when Phosphor doesn't cover a specific need — crypto token logos, chain icons, niche domain symbols.

**As an inline image:**
```html
<img src="https://api.iconify.design/ph/chart-pie-bold.svg?color=%23F3A950&height=20" 
     alt="chart" />
```

**As CSS background (for decorative use):**
```css
.icon-ethereum::before {
  content: url('https://api.iconify.design/cryptocurrency/eth.svg?height=16');
}
```

**Accessing Lucide through Iconify (secondary icon set):**
```html
<img src="https://api.iconify.design/lucide/wallet.svg?color=%23E6E6E6&height=20" />
```

### Icon Rules for `references/elements/icons.md`

- NEVER use emoji (no 🎯 📊 🔥 ⚡ etc. — not in icons, not in labels, nowhere)
- Default: Phosphor Bold weight
- Secondary: Lucide via Iconify API (when Phosphor lacks coverage)
- Sizing: 16-20px inline with text, 24-32px in cards/badges, 40-48px in hero sections
- Color: always `currentColor` or an explicit CSS variable — never hardcoded hex in the icon tag
- Alignment: `vertical-align: -0.15em` for inline icons to sit on the text baseline
- For domain-specific icons (token logos, chain logos): use Iconify's cryptocurrency set (`cryptocurrency:eth`, `cryptocurrency:btc`) or inline SVG if no set covers it
- When multiple icons appear in a row (e.g., feature list), they must all be from the same library and same weight for visual consistency

### Icon Weight Selection by Style

| Style | Phosphor weight | When |
|-------|----------------|------|
| aizfographics-style | Bold | Default — matches compact, high-contrast look |
| clean-minimal | Light or Regular | Thinner strokes match airy aesthetic |
| blueprint | Regular | Technical, precise feel |
| hand-drawn | Duotone | Playful, layered look |
| Any style | Fill | For active/selected states, emphasis |

---

## Skill-Creator Compliance

The skill must pass validation by `package_skill.py` before distribution. These are the requirements and how we meet them.

### SKILL.md Frontmatter Requirements

```yaml
---
name: aiz-infographic
description: >
  Create professional infographics as HTML files with PNG/SVG export.
  Supports 20 layout types (statistical, timeline, comparison, process,
  hierarchical, funnel, flowchart, dashboard, grid-cards, mind-map, etc.)
  and multiple visual styles with aizfographics-style as default.
  Use this skill whenever the user asks to create, design, generate, or
  build an infographic, data visualization, visual explainer, visual
  summary, chart poster, or any visual representation of information.
  Also trigger when the user says "make this visual", "turn this into
  a graphic", "visualize this data", "infographic for", or provides
  structured data and asks for a visual output. Trigger for tokenomics,
  ecosystem overviews, game overviews, cheatsheets, airdrop guides,
  comparison graphics, and any request to make data look presentable.
---
```

### Validation Checklist

| Requirement | Status | Notes |
|-------------|--------|-------|
| `name` field present | ✓ | `aiz-infographic` (kebab-case, 15 chars) |
| `name` is kebab-case | ✓ | Lowercase, hyphens only |
| `name` max 64 chars | ✓ | 15 chars |
| `description` field present | ✓ | See above |
| `description` max 1024 chars | ✓ | ~630 chars (well under limit) |
| `description` no angle brackets | ✓ | None used |
| No unexpected frontmatter keys | ✓ | Only `name` + `description` |
| SKILL.md body under ~500 lines | ✓ | Targeting ~400 lines |
| Reference files under ~300 lines each | ✓ | With TOC if over |
| Bundled resources in correct folders | ✓ | `references/`, `scripts/`, `assets/` |
| `evals/` excluded from packaging | ✓ automatic | `package_skill.py` excludes root-level `evals/` |

### Description Optimization

The description is "pushy" by design — it lists explicit trigger phrases and content types to ensure Claude activates the skill for relevant requests. This follows the skill-creator's guidance that skills tend to "undertrigger" rather than overtrigger.

After the skill is built and tested, the description can be further optimized using the skill-creator's `run_loop.py` script in Claude Code, which tests trigger accuracy against a set of eval queries.

### Testing Without Installing

The skill can be tested as a folder without packaging or installing:

**In Claude Code:**
```
Read ./aiz-infographic/SKILL.md and follow its instructions
to create a tokenomics infographic for $AIZ. Data: ...
```

Or using `@` file reference:
```
@aiz-infographic/SKILL.md Create an ecosystem overview
for Abstract chain. Categories: DeFi, Gaming, NFTs, Infra, Wallets.
```

Claude reads the SKILL.md, follows its instructions to load reference files from `./aiz-infographic/references/...`, and generates the output. The only difference from an installed skill is that installed skills trigger automatically based on the description match — uninstalled skills need explicit file reference.

**Development workflow:**
1. Edit reference files in `aiz-infographic/`
2. Test via explicit file reference in Claude Code
3. Review output, iterate on reference files
4. When satisfied, package with `package_skill.py`
5. Install the `.skill` file for auto-triggering
6. Optionally run description optimization via `run_loop.py`

---

## Revised Architecture (Final)

```
aiz-infographic/
├── SKILL.md                           # Core router (~400 lines)
├── references/
│   ├── elements/                      # Atomic design elements
│   │   ├── charts.md                  # Chart types + HTML/CSS patterns
│   │   ├── text.md                    # Typography atoms
│   │   ├── layout.md                  # Grid, containers, sections
│   │   ├── connectors.md             # Arrows, timelines, flow paths
│   │   ├── icons.md                   # Pictograms, symbols
│   │   ├── data-widgets.md            # Gauges, KPIs, progress bars
│   │   ├── decorative.md             # Backgrounds, shapes, borders
│   │   ├── maps.md                    # Geographic elements
│   │   └── comparison.md             # VS blocks, feature tables
│   ├── layouts/                       # Generic structural skeletons
│   │   ├── statistical.md
│   │   ├── timeline.md
│   │   ├── comparison.md
│   │   ├── process-flow.md
│   │   ├── hierarchical.md
│   │   ├── list.md
│   │   ├── funnel.md
│   │   ├── flowchart.md
│   │   ├── dashboard.md
│   │   ├── grid-cards.md
│   │   ├── mind-map.md
│   │   ├── pyramid.md
│   │   ├── circular-flow.md
│   │   ├── iceberg.md
│   │   ├── fishbone.md
│   │   ├── venn.md
│   │   ├── journey-path.md
│   │   ├── roadmap.md
│   │   ├── anatomical.md
│   │   └── geographic.md
│   ├── styles/                        # Visual identity token sets
│   │   ├── aizfographics-style.md     # YOUR default DNA style
│   │   ├── clean-minimal.md
│   │   ├── blueprint.md
│   │   ├── editorial.md
│   │   ├── corporate.md
│   │   ├── cyberpunk.md
│   │   ├── chalkboard.md
│   │   ├── hand-drawn.md
│   │   ├── retro.md
│   │   └── _custom-template.md
│   ├── templates/                     # Domain-specific presets
│   │   ├── token-economics.md         # 35.4% of your work
│   │   ├── crypto-explainer.md        # 16.6%
│   │   ├── game-overview.md           # 14.3%
│   │   ├── ecosystem-overview.md      # 12.6%
│   │   ├── airdrop-guide.md           # 9.7%
│   │   ├── nft-showcase.md            # 3.4%
│   │   ├── how-it-works.md            # 3.4%
│   │   ├── cheatsheet.md              # New
│   │   ├── game-mechanics.md          # New
│   │   └── report.md                  # 2.3%
│   └── export/
│       ├── png-export.md              # Puppeteer screenshot instructions
│       ├── svg-export.md              # dom-to-svg + fallback chain
│       └── figma-import.md            # html.to.design plugin guide
├── scripts/
│   ├── export-png.js                  # Node script for PNG export
│   └── export-svg.js                  # Node script for SVG export
└── evals/
    └── evals.json
```

### How the routing works in SKILL.md

```
User request
    │
    ├─ Matches a template? (e.g., "make a tokenomics infographic")
    │   └─ YES → Load template (which specifies layout + style + sections)
    │            → Load required element files
    │            → Generate HTML
    │
    ├─ Matches a layout type? (e.g., "make a timeline of crypto events")
    │   └─ YES → Load layout
    │            → Load style (default: aizfographics-style)
    │            → Load required element files
    │            → Generate HTML
    │
    └─ Generic request? (e.g., "make an infographic about X")
        └─ Classify content → pick best layout
           → Load style (default: aizfographics-style)
           → Generate HTML
```

### Summary of key decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Primary output | HTML | Reliable rendering, CSS layout power, font support |
| PNG export | Puppeteer screenshot | Pixel-perfect, free, works every time |
| SVG export | dom-to-svg (best-effort) | Figma compat, with fallback to html.to.design plugin |
| Design DNA | In markdown reference files | Claude reads rules, not Figma components |
| Figma role | Post-generation editing only | Export → import → manual tweaks |
| Templates layer | Yes, 10+ domain presets | Covers 95%+ of recurring infographic types |
| Default style | aizfographics-style (from DNA analysis) | Your actual visual identity, data-driven |
| Icons | Phosphor Bold (primary) + Iconify API (fallback) | Professional SVG icons, no emoji ever |
| Skill packaging | `package_skill.py` compatible | Validated frontmatter, correct folder structure |
| Testing | Folder-based, no install needed | `@SKILL.md` reference in Claude Code |
