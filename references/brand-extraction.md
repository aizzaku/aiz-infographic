# Brand Color Extraction

Loaded only when §5 Step 4 brand-color option 2 (`Pick brand color (auto-search)`) or option 3 (`Match a brand URL (extract)`) is chosen.

## Option 2 — auto-search

1. Run a web search for `"<brand name from content> brand guidelines"` and `"<brand name> primary color hex"`.
2. Extract the primary pair from results (brand-guidelines page, design-system docs, official press kit).
3. Apply as `--accent-1` / `--accent-2`.
4. Cite the source domain in the §5 Step 6 generation recap under an "Accent source" line.
5. If search yields nothing usable, fall back to option 1 (style default) and note the fallback.

## Option 3 — extract from a URL

The user gives a site URL. Run this 5-step flow:

### 1. Fetch

Use `WebFetch` on the URL. Keep only the `<head>` + first `<body>` screen worth of content (enough to catch brand CSS vars, logo, hero).

### 2. Extract colors

Scan in priority order:

1. CSS custom properties on `:root` / `html` / `body` starting with `--color-`, `--brand-`, `--primary`, `--accent`.
2. Inline `style="background/color: #…"` on hero-level elements.
3. Computed swatches from `<meta name="theme-color">` and SVG logo `fill=` attrs.
4. As a last resort, run a coarse frequency count of hex colors in the returned CSS and take the two most common non-neutral, non-`#000/#fff`, non-grayscale ones.

### 3. Map to accent pair

Pick the two strongest saturated colors as `--accent-1` (primary/brand) and `--accent-2` (complement/secondary). If only one strong color is found, auto-generate the second by rotating hue +20–40° toward warm or cool based on the first's temperature — stay within the 60-30-10 aesthetic, don't introduce a third color just because the site has one.

### 4. Diff-propose

Before committing, show the user a one-line proposal: *"Extracted `#F3A950` / `#F38150` from acme.xyz — apply as accent pair?"* via `AskUserQuestion` with options:

- `Apply`
- `Swap primary/secondary`
- `Try different colors`
- `Cancel — use style default`

### 5. Cite

Cite the source URL in the §5 Step 6 generation recap under an "Accent source" line.

## Fallback behavior

If any step fails (fetch blocked, no colors found, extracted colors fail basic contrast against `--canvas`), fall back to option 1 (style default) and note which step failed in the recap. **Never silently ship a broken extraction** — either the user sees the proposed pair, or they see the fallback.
