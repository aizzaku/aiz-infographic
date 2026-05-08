# Infographic Skill — End-to-End UX Design

## Target Platforms

| Platform | User type | Interaction model | Output delivery |
|----------|-----------|-------------------|-----------------|
| Claude Code | Developer, power user | CLI + chat + ask_user_input | File in filesystem, auto-open browser |
| OpenClaw | Agent operator | Chat (Telegram/Discord) + scheduled | File output + auto-export |
| Hermes | Agent operator | Chat + agent workspace | File output + auto-export |

---

## Two Modes

### Guided Mode (default)
Step-by-step. Claude asks questions using `ask_user_input` for tappable selections, shows previews, iterates with the user before finalizing. Best when the user has content but not a fully formed vision.

### One-Shot Mode
User provides everything upfront. Claude generates the complete infographic in a single pass. Best for power users, automated pipelines, and repeat workflows.

**Detection logic for SKILL.md:**

```
ONE-SHOT triggers (all must be true):
  ✓ Content/data is provided (structured text, bullet points, or file)
  ✓ Type is clear (explicit template name OR obvious content category)
  ✓ Enough data to fill required sections without guessing

ONE-SHOT override phrases:
  "one-shot", "just make it", "don't ask", "generate directly",
  "here's everything", "quick", "same as last time"

GUIDED triggers (any one is enough):
  ✗ Content is vague or incomplete
  ✗ No clear type/template match
  ✗ User asks for help choosing
  
GUIDED override phrases:
  "help me", "what layout", "walk me through",
  "I'm not sure", "what do you recommend"
```

---

## Guided Mode: Step-by-Step UX

### Step 1 → Content Intake

The user provides raw content in whatever form they have:
- Pasted text, bullet points, data
- A file attachment (markdown, CSV, JSON, PDF)
- A URL to pull content from
- A verbal description
- A reference image or previous infographic to redesign

Claude parses and extracts structured data, then confirms what it found:

```
Extracted from your content:

Topic: $AIZ Token Economics
Data points: 5 allocation categories + vesting schedule
Key metrics: Total supply, TGE price, FDV
Content density: Medium — fits a single portrait infographic

Moving to layout selection →
```

If content is too thin, Claude asks for more rather than guessing:
```
I have the allocation percentages, but I'm missing:
- Vesting terms for each category (cliff + unlock period)
- TGE date
- Any key metrics (FDV, initial price)

Can you provide those, or should I generate without them?
```

### Step 2 → Template / Layout Selection

Claude checks: does this content match a known template?

**Template match found:**

Claude presents the template structure using `ask_user_input`:

```
This looks like a token economics infographic.
I have a template that includes these sections:
→ Header → Key Metrics → Distribution Chart → Vesting Timeline → Allocation Cards → Footer
```

```json
ask_user_input: {
  "questions": [{
    "question": "Use this template or customize?",
    "options": ["Use token-economics template", "Customize sections", "Pick a different layout"],
    "type": "single_select"
  }]
}
```

**No template match — offer layout options:**

Claude recommends 2-3 best-fit layouts:

```json
ask_user_input: {
  "questions": [{
    "question": "Which layout fits best?",
    "options": [
      "Statistical — hero chart + metrics + callouts",
      "Grid Cards — equal-weight topic cards",
      "Process Flow — sequential steps with connectors",
      "Something else (describe)"
    ],
    "type": "single_select"
  }]
}
```

### Step 3 → Style Selection

Default: `aizfographics-style` is applied automatically. Claude mentions it once and moves on unless the user wants something different.

```
Style: aizfographics-style (dark, bold, teal/orange accents)
```

```json
ask_user_input: {
  "questions": [{
    "question": "Keep this style or switch?",
    "options": [
      "aizfographics-style (default)",
      "Clean minimal",
      "Blueprint",
      "Custom (I'll describe)"
    ],
    "type": "single_select"
  }]
}
```

For most of your personal work, this step is a one-tap confirmation. For client work, it becomes relevant.

### Step 4 → Dimensions

```json
ask_user_input: {
  "questions": [{
    "question": "Where will this be used?",
    "options": [
      "Social media tall (1080×1920)",
      "Blog/article (1080×1440)",
      "Presentation (1920×1080)",
      "Square post (1080×1080)"
    ],
    "type": "single_select"
  }]
}
```

Default for one-shot: portrait-medium 1080×1440 (3:4) — your most common format at 41%.

### Step 5 → Generation + Preview

Claude generates the HTML file and tells the user what it built:

```
Building your infographic...

📐 Layout: token-economics template
🎨 Style: aizfographics-style
📏 Dimensions: 1080 × 1440 (portrait 3:4)
📊 Sections: header → metrics → distribution chart → 
             vesting timeline → allocation cards → footer

[writes file, opens in browser]

Output: ./output/aiz-tokenomics.html
Preview opened in browser.

What would you like to adjust?
```

### Step 6 → Iteration Loop

This is the core interactive experience. The user gives natural language feedback, Claude modifies and regenerates.

**Types of iteration commands the skill recognizes:**

Content edits:
- "Change team allocation from 20% to 15%"
- "Add a category: Marketing at 5%"
- "The TGE date should be Q3 2026"

Layout edits:
- "Swap the chart and vesting timeline"
- "Make the header smaller"
- "Add a comparison table"
- "Remove the footer"
- "Make it a 2-column layout for the allocation cards"

Style edits:
- "Make the accent more orange"
- "Use Orbitron for the title"
- "Less glow, more flat"
- "Make it feel more premium"

Dimension edits:
- "Make it landscape"
- "Taller — it feels cramped"
- "Square version for Instagram"

Section-specific:
- "The vesting timeline is too cramped"
- "The hero section needs a background image"
- "Make the chart segments labeled with percentages"

**Claude's iteration behavior:**
1. Acknowledge what's changing (one sentence)
2. Regenerate the HTML
3. Re-open or refresh the browser preview
4. Ask "How's this?" or "What else?"

### Step 7 → Export

User signals completion:
- "Done", "looks good", "export", "give me the PNG"
- "I'm happy with it", "ship it", "finalize"

Claude runs the export chain:

```
Exporting...

📄 ./output/aiz-tokenomics.html (source — opens in browser)
🖼️ ./output/aiz-tokenomics.png (1080×1440, 2x res)
🔧 ./output/aiz-tokenomics.svg (vector — best-effort)

For Figma: use html.to.design plugin to import the HTML.
```

If SVG export fails:
```
📄 ./output/aiz-tokenomics.html ✓
🖼️ ./output/aiz-tokenomics.png ✓
🔧 SVG export had issues with this layout. 
   Use the html.to.design Figma plugin for vector editing.
```

---

## One-Shot Mode: Zero Questions

When the user provides everything upfront, Claude skips all interactive steps.

**Example input:**
```
One-shot. Tokenomics infographic for $GIG.
aizfographics-style, portrait 3:4.

Total Supply: 1,000,000,000
- Community: 40% (10% TGE, 24mo linear)
- Team: 20% (12mo cliff, 24mo linear)
- Ecosystem: 25% (10% TGE, 36mo linear)
- Investors: 15% (6mo cliff, 12mo linear)

FDV: $50M | TGE Price: $0.05
```

**Claude's response:**
```
[generates full infographic immediately]

Output: ./output/gig-tokenomics.html
Preview opened in browser.

Anything to adjust, or want the exports?
```

No template selection, no style confirmation, no dimension question. Straight to output. The user can still iterate from here — one-shot doesn't mean one-chance.

**One-shot with minimal input:**
```
Quick tokenomics for $XYZ, 500M supply, 5 categories, 
you fill in reasonable vesting terms.
```

Claude fills in sensible defaults for anything missing, generates, and notes its assumptions:

```
Generated with these assumptions:
- Community 35%, Team 20%, Ecosystem 20%, Investors 15%, Reserve 10%
- Standard vesting: 12mo cliff for team/investors, linear unlock
- Portrait 3:4, aizfographics-style

Adjust anything that's off?
```

---

## Interactive HTML Features

Since the output is HTML, the infographic itself can be interactive. These features split into two categories: creator tools (for the design session) and viewer features (for the published output).

### Creator Tools (stripped on final export)

These help during the design/iteration process and get removed from the clean export.

**1. Section label overlay**
A toggle in the corner shows faint labels on each section ("HERO", "METRICS", "CHART", "FOOTER"). Helps the user reference specific sections when requesting changes in chat.

```html
<div data-creator-tools style="position:fixed;top:12px;right:12px;z-index:9999;
     display:flex;gap:8px;">
  <button onclick="toggleLabels()">📋 Labels</button>
  <button onclick="toggleGrid()">📐 Grid</button>
  <button onclick="toggleSpacing()">📏 Spacing</button>
</div>
```

**2. Grid overlay toggle**
Shows the underlying column structure, margins, and alignment guides. Helps verify the layout matches the intended grid.

**3. Spacing visualizer**
Highlights padding and gaps between elements with colored overlays (like browser DevTools box model). Useful for spotting cramped or uneven spacing.

**4. Click-to-copy section ID**
Click any section → copies its ID to clipboard → makes it easy to say "change the hero-section" or "make the metrics-strip wider" in chat. A toast notification confirms: "Copied: hero-section"

**5. Export toolbar**

```html
<div data-creator-tools id="export-bar" 
     style="position:fixed;bottom:12px;right:12px;z-index:9999;
            display:flex;gap:8px;">
  <button onclick="exportPNG()">📸 PNG</button>
  <button onclick="exportSVG()">🔧 SVG</button>
  <button onclick="copyHTML()">📋 Copy HTML</button>
  <button onclick="cleanDownload()">⬇️ Clean Download</button>
</div>
```

"Clean Download" strips all `data-creator-tools` elements and downloads pristine HTML.

### Viewer Features (stay in final export)

These remain in the published infographic and enhance the experience for viewers.

**1. Hover tooltips on data elements**
Hovering over a pie/donut slice shows exact percentage + value. Hovering over a timeline node reveals full vesting details. Pure CSS with minimal JS:

```css
.chart-segment:hover .tooltip {
  opacity: 1;
  transform: translateY(-4px);
  transition: all 0.2s ease;
}
```

**2. Animated number counters**
KPI numbers (Total Supply: 1,000,000,000) count up from 0 to their final value when the section scrolls into view. Uses IntersectionObserver + requestAnimationFrame. Feels premium, zero dependencies.

**3. Scroll-triggered section reveals**
Sections fade or slide in as you scroll down. Creates narrative flow. Especially effective for tall portrait infographics (9:16). CSS keyframes + IntersectionObserver:

```javascript
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.15 });
document.querySelectorAll('.section').forEach(s => observer.observe(s));
```

```css
.section { opacity: 0; transform: translateY(20px); transition: all 0.5s ease; }
.section.visible { opacity: 1; transform: translateY(0); }
```

**4. Expandable detail sections**
For dense infographics (cheatsheets, ecosystem overviews), sections can collapse/expand. Click a section header → smooth reveal of detail content. Keeps the overview scannable while allowing deep dives.

**5. Dark/light mode toggle (optional)**
A small toggle that swaps the palette. Useful when viewers need to embed in a light context. CSS variables make this trivial:

```css
:root { --bg: #060606; --text: #F4F3E9; --accent: #42F3EE; }
[data-theme="light"] { --bg: #F8F9FA; --text: #1A1A1A; --accent: #0F6E56; }
```

**6. Responsive scaling**
Auto-scales to fit viewport while maintaining aspect ratio:

```css
.infographic-canvas {
  width: 100%;
  max-width: 1080px;
  aspect-ratio: 3/4;
  margin: 0 auto;
}
```

### What NOT to make interactive

- Chart proportions (accuracy > interactivity)
- Text content (not editable in viewer — Figma is for that)
- Layout structure (sections don't rearrange in the viewer)
- Core color palette (except dark/light toggle)

Principle: **interactivity enhances understanding, never distorts information.**

### Feature Matrix

| Feature | In HTML? | Creator-only? | In final export? | In PNG? |
|---------|----------|---------------|-----------------|---------|
| Section label overlay | ✓ | ✓ stripped | ✗ | ✗ |
| Grid overlay | ✓ | ✓ stripped | ✗ | ✗ |
| Spacing visualizer | ✓ | ✓ stripped | ✗ | ✗ |
| Click-to-copy IDs | ✓ | ✓ stripped | ✗ | ✗ |
| Export toolbar | ✓ | ✓ stripped | ✗ | ✗ |
| Hover tooltips | ✓ | ✗ | ✓ | ✗ (static) |
| Number counters | ✓ | ✗ | ✓ | ✗ (shows final) |
| Scroll reveals | ✓ | ✗ | ✓ | ✗ (all visible) |
| Expandable sections | ✓ | ✗ | ✓ | ✗ (all expanded) |
| Dark/light toggle | ✓ | ✗ | ✓ (optional) | ✗ (dark default) |
| Responsive scaling | ✓ | ✗ | ✓ | ✗ (fixed size) |

### How stripping works

All creator tools carry `data-creator-tools`:

```javascript
function cleanDownload() {
  const clone = document.documentElement.cloneNode(true);
  clone.querySelectorAll('[data-creator-tools]').forEach(el => el.remove());
  const blob = new Blob(['<!DOCTYPE html>' + clone.outerHTML], {type: 'text/html'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'infographic.html';
  a.click();
}
```

For PNG export: Puppeteer hides `[data-creator-tools]` before screenshot, and forces all sections visible (no scroll-reveal delay), all expandables open, all counters at final value.

---

## Platform-Specific Behavior

### Claude Code

- `ask_user_input` for layout/style/dimension selection (tappable in terminal)
- Output file to working directory
- Auto-open browser: `open output.html` (macOS) or `xdg-open output.html` (Linux)
- Creator tools active by default in the HTML preview
- PNG/SVG export via `scripts/export-png.js` and `scripts/export-svg.js`
- Iteration via chat: "make the header bigger" → regenerate → refresh browser
- Supports slash-command style for power users:
  `/aiz-infographic --template token-economics --style aizfographics-style --dim 1080x1440`

### OpenClaw / Hermes

- Default to one-shot mode (agents receive structured data, generate output)
- If content is incomplete, agent asks via chat channel (Telegram/Discord)
- File output to configured directory
- Export scripts run automatically (HTML + PNG always, SVG best-effort)
- Creator tools stripped by default (no interactive editing in agent context)
- Can be triggered by cron or event (e.g., "generate weekly ecosystem update infographic")
- Style defaults to aizfographics-style unless SOUL.md or workspace config overrides

---

## Full UX Decision Tree

```
User message arrives
│
├─ Has structured data + type hint + enough info?
│   └─ YES → ONE-SHOT
│       ├─ Auto-select template/layout
│       ├─ Apply aizfographics-style (unless specified)
│       ├─ Apply default dimensions (3:4 unless specified)
│       ├─ Generate HTML immediately
│       └─ "Anything to adjust?"
│
├─ Has partial info?
│   └─ GUIDED (ask only what's missing)
│       ├─ Missing content → "What data should I include?"
│       ├─ Missing type → ask_user_input with 2-3 layout options
│       ├─ Missing style → apply aizfographics-style, mention once
│       └─ Missing dimensions → ask_user_input with use-case options
│
└─ Vague request ("make an infographic")?
    └─ GUIDED (start from scratch)
        └─ "What topic? Paste your content or tell me what you need."

After generation (both modes):
├─ User requests changes → iterate (modify + regenerate)
├─ User says "done" / "export" / "PNG" → export chain
├─ User says "start over" / "different layout" → reset to step 2
└─ User says nothing → wait (don't push)
```

---

## End-to-End Examples

### Guided Mode (Claude Code)

```
USER: Make me an infographic about our token launch

CLAUDE: I'll help build that. What token data do you have? 
Paste allocations, vesting terms, key metrics — whatever you've got.

USER: $AIZ token
500M supply, Community 35%, Team 20%, Ecosystem 25%, 
Investors 15%, Reserve 5%
No vesting details yet, use standard terms

CLAUDE: Got it — token economics infographic.

[ask_user_input: "Use the token-economics template?" 
 → "Yes" / "Customize sections" / "Different layout"]

USER: [taps "Yes"]

CLAUDE: [ask_user_input: "Dimensions?"
 → "Social tall (9:16)" / "Blog (3:4)" / "Presentation (16:9)" / "Square"]

USER: [taps "Blog (3:4)"]

CLAUDE: Generating with aizfographics-style, 1080×1440...

Output: ./output/aiz-tokenomics.html
Preview opened in browser.

I used standard vesting: 12mo cliff for team/investors, 
linear unlock for community/ecosystem, reserve locked 24mo.

What would you like to adjust?

USER: Make community teal and team orange. 
The vesting section is too cramped, give it more room.

CLAUDE: Updated — community is teal, team is orange.
Expanded vesting section by 40%.

[regenerates, refreshes browser]

How's this?

USER: Perfect. Export.

CLAUDE: 
📄 ./output/aiz-tokenomics.html
🖼️ ./output/aiz-tokenomics.png (2160×2880, 2x)
🔧 ./output/aiz-tokenomics.svg

All in ./output/
```

### One-Shot Mode (Claude Code)

```
USER: One-shot. Ecosystem overview for Abstract chain. 
Landscape 16:9. Categories:

DeFi: Relay, Cleo, LiquidSwap
Gaming: Gigaverse, Parallel, Fableborne
NFTs: Magic Eden, Zora, Foundation
Infra: Alchemy, Goldsky, Gelato
Wallets: AGW, Rabby, Rainbow

CLAUDE: Output: ./output/abstract-ecosystem.html
Preview opened in browser.

5 categories, grid-card layout, landscape.
Adjust anything, or want exports?

USER: Exports.

CLAUDE:
📄 ./output/abstract-ecosystem.html
🖼️ ./output/abstract-ecosystem.png
🔧 ./output/abstract-ecosystem.svg
```

### Agent Mode (OpenClaw)

```
[Agent receives scheduled task or chat message]

OPENCLAW TASK: Generate weekly Gigaverse ecosystem update.
Data source: ecosystem-partners.json

[Agent reads data file, auto-selects ecosystem-overview template,
 applies aizfographics-style, generates HTML + PNG]

AGENT → TELEGRAM: Here's this week's ecosystem update.
[attaches PNG]
[saves HTML to workspace for manual editing if needed]
```

---

## What's Left to Build

After this UX design, the remaining work is:

1. ☐ SKILL.md — the actual router file with all the logic above
2. ☐ Element reference files (9 files in references/elements/)
3. ☐ Layout reference files (20 files in references/layouts/)
4. ☐ Style reference files (10 files in references/styles/)
5. ☐ Template reference files (10+ files in references/templates/)
6. ☐ Export scripts (scripts/export-png.js, scripts/export-svg.js)
7. ☐ Export reference docs (references/export/)
8. ☐ Evals (test prompts + expected outputs)
