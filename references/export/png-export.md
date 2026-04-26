# PNG Export

PNG export is **server-side only** via Playwright. There is no in-browser PNG button — html2canvas et al. can't render the modern CSS this skill uses (`color-mix`, layered `padding-box`/`border-box` gradient borders, `backdrop-filter`) reliably enough to ship.

## Round-trip after browser edits

1. Edit in the browser (text + accent colors via the creator toolbar).
2. Click **Save** in the toolbar (or press `Ctrl+S`) — writes the cleaned HTML over the source file.
3. Tell Claude *"export the new HTML as PNG"* — Claude runs the command below and produces the updated PNG alongside the HTML.

## Command

```bash
python scripts/export.py --png output/<name>.html
```

Or as part of the full chain:

```bash
python scripts/export.py --all output/<name>.html
```

Output: `output/<name>.png`

## Mechanics

The script:

1. Starts a local HTTP server rooted at the HTML's parent directory so Google Fonts, Phosphor Icons CDN, and Iconify API URLs resolve correctly (relative paths, too).
2. Launches Chromium with `device_scale_factor=2` (retina / 2x DPR).
3. Navigates to the HTML, waits for `document.fonts.ready`, then a 400ms settle for CSS transitions and lazy webfonts.
4. Measures `.infographic-canvas` bounding box, resizes viewport to match.
5. Before screenshot, forces phase-1 viewer features to final state:
   - Number counters: each `[data-counter-to]` element's textContent is set to its `data-counter-to` value with thousand separators.
   - Scroll reveals: `.section` gets `.visible` applied so animated entries aren't mid-fade.
6. Screenshot `{type: "png", omit_background: false, full_page: false}` on the canvas element only.

## Dimensions in the output

The PNG matches the canvas's actual rendered size × DPR. For a 1080×1440 canvas at 2x: 2160×2880 PNG.

Override DPR with `--scale 1` (for preview) or `--scale 3` (print quality).

## Common issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Fonts render as fallback | CDN blocked / timeout | Re-run; script retries once. If persistent, pre-download fonts into `output/` and reference locally. |
| Background is transparent | Canvas `.infographic-canvas` has no bg set | Every canvas MUST set `background: var(--canvas)`. Check the style. |
| Truncated content at bottom | Canvas height exceeds viewport after layout | The script auto-measures; if still truncated, the canvas has `overflow: hidden` with content outside. Remove it or reduce content. |
| Counters still at 0 | `[data-counter-to]` missing on numeric element | Add the attribute to every number-counter target. |

## Testing a single HTML without the full chain

```bash
python scripts/export.py --png path/to/file.html
```

The script runs self-contained — no project-specific config.
