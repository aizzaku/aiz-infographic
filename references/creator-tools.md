# Creator Tools

Authoring aids that appear in the generated HTML during iteration. Automatically stripped from PNG exports. Two surfaces only: **accent color editor** and **inline text editing**, plus a floating toolbar that hosts Save / Revert / PNG / Copy HTML / Clean Download.

All creator-tool elements carry the attribute `data-creator-tools` so `export.py` can hide them before screenshotting. Never render these elements outside of an iteration context — clean exports should omit them entirely.

## Master switch

Wrap all creator tools in a single container and toggle with one class:

```html
<div class="creator-tools" data-creator-tools>
  <!-- toolbar, color editor, handlers -->
</div>
```

```css
.creator-tools { pointer-events: none; }
.creator-tools > * { pointer-events: auto; }
```

## 1. Floating toolbar

Bottom-right group: Edit · Color | Save · Revert | PNG · Copy · CleanDL.

```html
<div class="ct-toolbar" data-creator-tools>
  <button onclick="ctToggleEdit()" aria-label="Edit" title="Edit mode (E)">
    <i class="ph-bold ph-pencil-simple"></i>
  </button>
  <button onclick="ctToggleColorEditor()" aria-label="Color" title="Accent colors">
    <i class="ph-bold ph-palette"></i>
  </button>
  <span class="ct-sep"></span>
  <button onclick="ctSave()" aria-label="Save" title="Save to disk (Ctrl+S)">
    <i class="ph-bold ph-floppy-disk"></i>
  </button>
  <button onclick="ctRevert()" aria-label="Revert" title="Revert to original">
    <i class="ph-bold ph-arrow-counter-clockwise"></i>
  </button>
  <span class="ct-sep"></span>
  <button onclick="ctExportPNG()" aria-label="PNG" title="Export PNG">
    <i class="ph-bold ph-image"></i>
  </button>
  <button onclick="ctCopyHTML()" aria-label="Copy" title="Copy HTML">
    <i class="ph-bold ph-copy"></i>
  </button>
  <button onclick="ctCleanDownload()" aria-label="CleanDL" title="Clean Download (no creator tools)">
    <i class="ph-bold ph-download-simple"></i>
  </button>
</div>

<style>
.ct-toolbar {
  position: fixed;
  bottom: 16px; right: 16px;
  display: flex; gap: 4px;
  padding: 6px;
  background: var(--elevated, #1a1a1a);
  border: 1px solid color-mix(in srgb, var(--accent-1, #F3A950) 40%, transparent);
  border-radius: 8px;
  z-index: 9999;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}
.ct-toolbar button {
  padding: 8px 10px;
  background: transparent;
  border: none;
  border-radius: 4px;
  color: var(--text-secondary, #cccccc);
  cursor: pointer;
  font-size: 18px;
  transition: background 0.15s, color 0.15s;
}
.ct-toolbar button:hover {
  background: color-mix(in srgb, var(--accent-1, #F3A950) 15%, transparent);
  color: var(--accent-1, #F3A950);
}
.ct-sep {
  width: 1px;
  align-self: stretch;
  margin: 2px 2px;
  background: color-mix(in srgb, var(--accent-1, #F3A950) 25%, transparent);
}
@keyframes ct-spin { to { transform: rotate(360deg); } }
</style>

<script data-creator-tools>
window.ctCopyHTML = () => {
  const clone = document.documentElement.cloneNode(true);
  clone.querySelectorAll('[data-creator-tools]').forEach(el => el.remove());
  navigator.clipboard.writeText('<!DOCTYPE html>\n' + clone.outerHTML);
};
window.ctCleanDownload = () => {
  const clone = document.documentElement.cloneNode(true);
  clone.querySelectorAll('[data-creator-tools]').forEach(el => el.remove());
  const blob = new Blob(['<!DOCTYPE html>\n' + clone.outerHTML], { type: 'text/html' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = document.title.toLowerCase().replace(/\s+/g, '-') + '.html';
  a.click();
};
(function () {
  let _h2cPromise = null;

  function _loadH2C() {
    if (window.html2canvas) return Promise.resolve(window.html2canvas);
    if (_h2cPromise) return _h2cPromise;
    _h2cPromise = new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
      s.setAttribute('data-creator-tools', '');
      s.onload = () => resolve(window.html2canvas);
      s.onerror = () => reject(new Error('html2canvas load failed'));
      document.head.appendChild(s);
    });
    return _h2cPromise;
  }

  function _pngToast(msg) {
    const t = document.createElement('div');
    t.setAttribute('data-creator-tools', '');
    t.className = 'ct-toast';
    t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(() => t.remove(), 1800);
  }

  window.ctExportPNG = async () => {
    const btn = document.querySelector('.ct-toolbar [aria-label="PNG"]');
    const origHTML = btn ? btn.innerHTML : '';
    if (btn) {
      btn.innerHTML = '<i class="ph-bold ph-circle-notch" style="display:inline-block;animation:ct-spin 1s linear infinite"></i>';
      btn.disabled = true;
    }
    try {
      const h2c = await _loadH2C();
      const canvas_el = document.querySelector('.infographic-canvas');
      if (!canvas_el) throw new Error('No .infographic-canvas');

      // Mirror export.py _prepare_page_state
      document.querySelectorAll('[data-counter-to]').forEach(el => {
        const v = parseInt(el.dataset.counterTo, 10);
        if (!isNaN(v)) el.textContent = v.toLocaleString('en-US');
      });
      document.querySelectorAll('.section').forEach(el => el.classList.add('visible'));

      await document.fonts.ready;

      const rendered = await h2c(canvas_el, {
        scale: 2,
        useCORS: true,
        allowTaint: false,
        logging: false,
        backgroundColor: null,
        ignoreElements: el => el.hasAttribute('data-creator-tools'),
      });

      rendered.toBlob(blob => {
        if (!blob) { _pngToast('Export failed'); return; }
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = (document.title || 'infographic').toLowerCase().replace(/\s+/g, '-') + '.png';
        a.click();
        setTimeout(() => URL.revokeObjectURL(a.href), 1000);
        _pngToast('PNG saved');
      }, 'image/png');

    } catch (err) {
      console.error('[ctExportPNG]', err);
      _pngToast('Export failed');
    } finally {
      if (btn) { btn.innerHTML = origHTML; btn.disabled = false; }
    }
  };
})();
</script>
```

### Robustness notes

- Toolbar colors fall back to hardcoded hex values when the active style doesn't define `--elevated`, `--accent-1`, or `--text-secondary`. Tools remain visible on any style.
- If the Phosphor Icons CDN is blocked, the toolbar buttons can still be identified by their `aria-label` / `title` attrs on hover. For a stronger fallback, gate a `::after { content: attr(aria-label); }` rule on `.ph-bold:empty` — not emitted by default.

## 2. Clean download

Same as the toolbar button above — `ctCleanDownload()` removes every `[data-creator-tools]` element from a cloned DOM and triggers a download of the pristine HTML. This is the canonical path for producing a "shippable" HTML without having to regenerate.

## 3. Inline text editing

Toggle with the pencil button or `e`. Turns every text-bearing element inside `.infographic-canvas` into `contenteditable="plaintext-only"`. Headers keep their CSS `text-transform: uppercase` — users type in any case, display stays uppercase. Emoji typed/pasted into fields are silently stripped to uphold the no-emoji rule.

```html
<script data-creator-tools>
(function() {
  const EMOJI = /[\p{Extended_Pictographic}\u200D\uFE0F]/gu;
  const TEXT_SEL = '.infographic-canvas h1, .infographic-canvas h2, .infographic-canvas h3, .infographic-canvas h4, .infographic-canvas h5, .infographic-canvas h6, .infographic-canvas p, .infographic-canvas li, .infographic-canvas span, .infographic-canvas td, .infographic-canvas th, .infographic-canvas figcaption, .infographic-canvas label, .infographic-canvas dt, .infographic-canvas dd';

  function editableEls() {
    return Array.from(document.querySelectorAll(TEXT_SEL))
      .filter(el => !el.closest('[data-creator-tools]'))
      .filter(el => !el.querySelector(TEXT_SEL));
  }

  window.ctToggleEdit = () => {
    const h = document.documentElement;
    const on = h.dataset.editMode !== 'true';
    h.dataset.editMode = on ? 'true' : 'false';
    editableEls().forEach(el => {
      if (on) {
        el.setAttribute('contenteditable', 'plaintext-only');
        if (!el.dataset.ctOrig) el.dataset.ctOrig = el.textContent;
      } else {
        el.removeAttribute('contenteditable');
      }
    });
  };

  let debounceTimer = null;
  let pendingTarget = null;
  let pendingOldValue = null;

  document.addEventListener('focusin', (e) => {
    const el = e.target;
    if (!el.hasAttribute || !el.hasAttribute('contenteditable')) return;
    if (el.closest('[data-creator-tools]')) return;
    if (el.dataset.ctPrevValue === undefined) {
      el.dataset.ctPrevValue = el.textContent;
    }
  });

  document.addEventListener('input', (e) => {
    const el = e.target;
    if (!el.hasAttribute('contenteditable')) return;
    if (el.closest('[data-creator-tools]')) return;

    const stripped = el.textContent.replace(EMOJI, '');
    if (stripped !== el.textContent) {
      const sel = window.getSelection();
      const offset = sel.anchorOffset;
      el.textContent = stripped;
      try { sel.collapse(el.firstChild || el, Math.min(offset, stripped.length)); } catch {}
    }

    if (pendingTarget !== el) {
      pendingTarget = el;
      pendingOldValue = el.dataset.ctPrevValue ?? el.dataset.ctOrig ?? '';
    }
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      const newValue = pendingTarget.textContent;
      if (newValue !== pendingOldValue) {
        window.ctUndoPush && window.ctUndoPush({
          type: 'text',
          selector: window.ctCssPath(pendingTarget),
          oldValue: pendingOldValue,
          newValue,
        });
        pendingTarget.dataset.ctPrevValue = newValue;
      }
      pendingTarget = null;
    }, 300);
  });
})();
</script>

<style>
html[data-edit-mode="true"] .infographic-canvas [contenteditable]:hover {
  outline: 1px dashed color-mix(in srgb, var(--accent-1, #F3A950) 40%, transparent);
  outline-offset: 2px;
  cursor: text;
}
html[data-edit-mode="true"] .infographic-canvas [contenteditable]:focus {
  outline: 1px solid color-mix(in srgb, var(--accent-1, #F3A950) 70%, transparent);
  outline-offset: 2px;
}
</style>
```

## 4. Accent color editor

Toggle with the palette button. Fixed popover, top-right, 240px wide. Two color inputs bound to `:root`'s `--accent-1` / `--accent-2`. Because the aizfographics style centralizes every gradient, border, glow, and fill on these two variables via `color-mix`, a single swap recolors the whole infographic instantly.

```html
<div class="ct-color-editor" data-creator-tools>
  <div class="ct-color-header">Accent Colors</div>
  <label>
    <span>Primary</span>
    <input type="color" id="ct-color-1">
  </label>
  <label>
    <span>Secondary</span>
    <input type="color" id="ct-color-2">
  </label>
  <div class="ct-presets">
    <button class="ct-preset" data-c1="#F3A950" data-c2="#F38150" title="Amber / Burnt"></button>
    <button class="ct-preset" data-c1="#FFBB00" data-c2="#FF8800" title="Gold / Orange"></button>
    <button class="ct-preset" data-c1="#B2FF00" data-c2="#FFCC00" title="Lime / Gold"></button>
    <button class="ct-preset" data-c1="#FF0048" data-c2="#FF336D" title="Red / Pink"></button>
    <button class="ct-preset" data-c1="#67B39F" data-c2="#CEDFCC" title="Sage / Mint"></button>
    <button class="ct-preset" data-c1="#00FF90" data-c2="#00F6FF" title="Green / Cyan"></button>
    <button class="ct-preset" data-c1="#C084FC" data-c2="#22D3EE" title="Violet / Cyan"></button>
    <button class="ct-preset" data-c1="#F472B6" data-c2="#FB923C" title="Pink / Peach"></button>
  </div>
  <a class="ct-reset" onclick="ctResetAccent()">Reset to original</a>
</div>

<style>
.ct-color-editor {
  position: fixed;
  top: 16px; right: 16px;
  width: 240px;
  padding: 14px;
  background: var(--elevated, #1a1a1a);
  border: 1px solid color-mix(in srgb, var(--accent-1, #F3A950) 40%, transparent);
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  z-index: 9999;
  display: none;
  font: 700 11px/1 'Montserrat', sans-serif;
}
html[data-color-editor="true"] .ct-color-editor { display: block; }
.ct-color-header {
  color: var(--accent-1, #F3A950);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 10px;
}
.ct-color-editor label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 6px 0;
  color: var(--text-secondary, #cccccc);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.ct-color-editor input[type="color"] {
  width: 40px; height: 26px;
  border: none; background: transparent;
  cursor: pointer;
}
.ct-presets {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  margin: 10px 0;
}
.ct-preset {
  height: 24px;
  border: 1px solid color-mix(in srgb, var(--accent-1, #F3A950) 20%, transparent);
  border-radius: 4px;
  cursor: pointer;
  padding: 0;
}
.ct-preset:hover { transform: scale(1.08); }
.ct-reset {
  display: block;
  margin-top: 4px;
  color: var(--text-muted, #888888);
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0;
  cursor: pointer;
  text-decoration: underline;
  font-size: 10px;
}
.ct-reset:hover { color: var(--accent-1, #F3A950); }
</style>

<script data-creator-tools>
(function() {
  const root = document.documentElement;
  const read = (name) => getComputedStyle(root).getPropertyValue(name).trim();
  const ORIG_1 = read('--accent-1') || '#F3A950';
  const ORIG_2 = read('--accent-2') || '#F38150';

  window.ctToggleColorEditor = () => {
    const on = root.dataset.colorEditor !== 'true';
    root.dataset.colorEditor = on ? 'true' : 'false';
    if (on) {
      document.getElementById('ct-color-1').value = toHex(read('--accent-1')) || ORIG_1;
      document.getElementById('ct-color-2').value = toHex(read('--accent-2')) || ORIG_2;
    }
  };

  function toHex(c) {
    if (!c) return '';
    if (c.startsWith('#')) return c.length === 4
      ? '#' + c.slice(1).split('').map(x => x + x).join('')
      : c;
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return '';
    const parts = m[1].split(',').map(s => parseFloat(s));
    return '#' + parts.slice(0, 3).map(n => Math.round(n).toString(16).padStart(2, '0')).join('');
  }

  function setAccent(name, value, pushUndo = true) {
    const old = read(name);
    root.style.setProperty(name, value);
    if (pushUndo && window.ctUndoPush && old !== value) {
      window.ctUndoPush({ type: 'color', selector: name, oldValue: old, newValue: value });
    }
  }

  document.addEventListener('input', (e) => {
    if (e.target.id === 'ct-color-1') setAccent('--accent-1', e.target.value);
    if (e.target.id === 'ct-color-2') setAccent('--accent-2', e.target.value);
  });

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.ct-preset');
    if (!btn) return;
    setAccent('--accent-1', btn.dataset.c1);
    setAccent('--accent-2', btn.dataset.c2);
    document.getElementById('ct-color-1').value = btn.dataset.c1;
    document.getElementById('ct-color-2').value = btn.dataset.c2;
  });

  window.ctResetAccent = () => {
    setAccent('--accent-1', ORIG_1);
    setAccent('--accent-2', ORIG_2);
    document.getElementById('ct-color-1').value = ORIG_1;
    document.getElementById('ct-color-2').value = ORIG_2;
  };

  window.ctApplyAccent = (c1, c2) => {
    setAccent('--accent-1', c1, false);
    setAccent('--accent-2', c2, false);
  };
  window.ctGetAccent = () => ({
    '--accent-1': read('--accent-1'),
    '--accent-2': read('--accent-2'),
  });
  window.ctGetOriginalAccent = () => ({ '--accent-1': ORIG_1, '--accent-2': ORIG_2 });
})();
</script>
```

## 5. Persistence & undo

Three pieces: undo/redo stack, localStorage autosave, explicit Save-to-disk. Nothing writes to the file without user action, so mistakes are always recoverable.

### Undo stack

Command pattern, 100-entry cap. `Ctrl+Z` / `Cmd+Z` undoes, `Ctrl+Shift+Z` redoes. Text edits are debounced at 300ms (one entry per word, not per keystroke). Color edits are one entry per input change.

### localStorage autosave

Key = `infographic-edits:` + a SHA-like content hash of the original HTML at page load, so different infographics can't collide. Saved on every undo-stack push, throttled to 1/sec. On reload, if edits exist, show a toast — "Restored edits from <time>. [Revert]".

### Save to disk

One button, two paths:

- **File System Access API** (Chromium): `showSaveFilePicker()` on first use, cache the handle on `window.ctFileHandle` for one-click subsequent saves. Writes the cleaned DOM (no `[data-creator-tools]`, no `contenteditable` attrs).
- **Fallback** (Firefox/Safari): triggers the existing `ctCleanDownload()` Blob path. The user manually overwrites the original file.

`Ctrl+S` triggers Save and `preventDefault`s the browser's own save dialog.

### Revert

Clears localStorage for this hash and reloads the page, restoring whatever Claude last generated.

```html
<script data-creator-tools>
(function() {
  function hashString(s) {
    let h = 0x811c9dc5;
    for (let i = 0; i < s.length; i++) {
      h ^= s.charCodeAt(i);
      h = Math.imul(h, 0x01000193);
    }
    return (h >>> 0).toString(16);
  }

  const STORAGE_PREFIX = 'infographic-edits:';
  const originalHTML = document.documentElement.outerHTML.replace(/\s+/g, ' ');
  const STORAGE_KEY = STORAGE_PREFIX + hashString(originalHTML);

  window.ctCssPath = function(el) {
    if (!el || el.nodeType !== 1) return '';
    const parts = [];
    while (el && el.nodeType === 1 && el !== document.body) {
      let part = el.tagName.toLowerCase();
      if (el.id) { part += '#' + el.id; parts.unshift(part); break; }
      const parent = el.parentNode;
      if (parent) {
        const sibs = Array.from(parent.children).filter(n => n.tagName === el.tagName);
        if (sibs.length > 1) part += `:nth-of-type(${sibs.indexOf(el) + 1})`;
      }
      parts.unshift(part);
      el = el.parentNode;
    }
    return parts.join(' > ');
  };

  const undoStack = [];
  const redoStack = [];
  const MAX = 100;

  window.ctUndoPush = (entry) => {
    undoStack.push(entry);
    if (undoStack.length > MAX) undoStack.shift();
    redoStack.length = 0;
    scheduleSave();
  };

  function applyEntry(entry, useNew) {
    const value = useNew ? entry.newValue : entry.oldValue;
    if (entry.type === 'text') {
      const el = document.querySelector(entry.selector);
      if (el) { el.textContent = value; el.dataset.ctPrevValue = value; }
    } else if (entry.type === 'color') {
      document.documentElement.style.setProperty(entry.selector, value);
      const input = document.getElementById(
        entry.selector === '--accent-1' ? 'ct-color-1' : 'ct-color-2'
      );
      if (input) input.value = value.trim();
    }
  }

  window.ctUndo = () => {
    const e = undoStack.pop();
    if (!e) return;
    applyEntry(e, false);
    redoStack.push(e);
    scheduleSave();
  };
  window.ctRedo = () => {
    const e = redoStack.pop();
    if (!e) return;
    applyEntry(e, true);
    undoStack.push(e);
    scheduleSave();
  };

  let saveTimer = null;
  function scheduleSave() {
    if (saveTimer) return;
    saveTimer = setTimeout(() => {
      saveTimer = null;
      persistToStorage();
    }, 1000);
  }

  function collectTextEdits() {
    const out = {};
    document.querySelectorAll('.infographic-canvas [data-ct-orig]').forEach(el => {
      if (el.textContent !== el.dataset.ctOrig) {
        out[window.ctCssPath(el)] = el.textContent;
      }
    });
    return out;
  }

  function persistToStorage() {
    const accent = window.ctGetAccent ? window.ctGetAccent() : {};
    const orig = window.ctGetOriginalAccent ? window.ctGetOriginalAccent() : {};
    const payload = {
      textEdits: collectTextEdits(),
      accent: {
        '--accent-1': accent['--accent-1'] !== orig['--accent-1'] ? accent['--accent-1'] : null,
        '--accent-2': accent['--accent-2'] !== orig['--accent-2'] ? accent['--accent-2'] : null,
      },
      timestamp: Date.now(),
    };
    const hasEdits = Object.keys(payload.textEdits).length > 0
      || payload.accent['--accent-1']
      || payload.accent['--accent-2'];
    if (hasEdits) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
    } else {
      localStorage.removeItem(STORAGE_KEY);
    }
  }

  function restoreFromStorage() {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return;
    let data;
    try { data = JSON.parse(raw); } catch { return; }

    if (data.textEdits) {
      for (const [sel, text] of Object.entries(data.textEdits)) {
        const el = document.querySelector(sel);
        if (el) {
          el.dataset.ctOrig = el.dataset.ctOrig ?? el.textContent;
          el.textContent = text;
          el.dataset.ctPrevValue = text;
        }
      }
    }
    if (data.accent && window.ctApplyAccent) {
      const c1 = data.accent['--accent-1'];
      const c2 = data.accent['--accent-2'];
      if (c1 || c2) {
        const orig = window.ctGetOriginalAccent();
        window.ctApplyAccent(c1 || orig['--accent-1'], c2 || orig['--accent-2']);
      }
    }

    showRestoreToast(data.timestamp);
  }

  function showRestoreToast(ts) {
    const toast = document.createElement('div');
    toast.dataset.creatorTools = '';
    toast.className = 'ct-toast ct-restore-toast';
    const ago = timeAgo(ts);
    toast.innerHTML = `Restored edits from ${ago}. <a onclick="ctRevert()">Revert</a>`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 6000);
  }

  function timeAgo(ts) {
    const s = Math.floor((Date.now() - ts) / 1000);
    if (s < 60) return `${s}s ago`;
    if (s < 3600) return `${Math.floor(s / 60)}m ago`;
    if (s < 86400) return `${Math.floor(s / 3600)}h ago`;
    return `${Math.floor(s / 86400)}d ago`;
  }

  window.ctSave = async () => {
    const cleanHTML = buildCleanHTML();
    if ('showSaveFilePicker' in window) {
      try {
        if (!window.ctFileHandle) {
          const suggested = (document.title || 'infographic').toLowerCase().replace(/\s+/g, '-') + '.html';
          window.ctFileHandle = await window.showSaveFilePicker({
            suggestedName: suggested,
            types: [{ description: 'HTML', accept: { 'text/html': ['.html'] } }],
          });
        }
        const writable = await window.ctFileHandle.createWritable();
        await writable.write(cleanHTML);
        await writable.close();
        flashToast('Saved');
        localStorage.removeItem(STORAGE_KEY);
      } catch (err) {
        if (err && err.name === 'AbortError') return;
        console.error(err);
        flashToast('Save failed — using download');
        downloadCleanHTML(cleanHTML);
      }
    } else {
      downloadCleanHTML(cleanHTML);
      flashToast('Downloaded (overwrite your file)');
    }
  };

  function buildCleanHTML() {
    const clone = document.documentElement.cloneNode(true);
    clone.querySelectorAll('[data-creator-tools]').forEach(el => el.remove());
    clone.querySelectorAll('[contenteditable]').forEach(el => el.removeAttribute('contenteditable'));
    clone.querySelectorAll('[data-ct-orig]').forEach(el => delete el.dataset.ctOrig);
    clone.querySelectorAll('[data-ct-prev-value]').forEach(el => delete el.dataset.ctPrevValue);
    const accent = window.ctGetAccent ? window.ctGetAccent() : null;
    if (accent) {
      const styleEl = clone.querySelector('style');
      if (styleEl) {
        styleEl.textContent = styleEl.textContent.replace(
          /(--accent-1:\s*)[^;]+;/,
          `$1${accent['--accent-1']};`
        ).replace(
          /(--accent-2:\s*)[^;]+;/,
          `$1${accent['--accent-2']};`
        );
      }
    }
    ['editMode', 'colorEditor'].forEach(k => delete clone.dataset[k]);
    return '<!DOCTYPE html>\n' + clone.outerHTML;
  }

  function downloadCleanHTML(html) {
    const blob = new Blob([html], { type: 'text/html' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = (document.title || 'infographic').toLowerCase().replace(/\s+/g, '-') + '.html';
    a.click();
  }

  function flashToast(msg) {
    const t = document.createElement('div');
    t.dataset.creatorTools = '';
    t.className = 'ct-toast';
    t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(() => t.remove(), 1600);
  }

  window.ctRevert = () => {
    const n = undoStack.length;
    if (n > 0 && !confirm(`Discard ${n} edit${n === 1 ? '' : 's'}?`)) return;
    localStorage.removeItem(STORAGE_KEY);
    window.ctFileHandle = null;
    location.reload();
  };

  document.addEventListener('keydown', (e) => {
    const meta = e.metaKey || e.ctrlKey;
    if (meta && !e.shiftKey && e.key.toLowerCase() === 'z') { e.preventDefault(); window.ctUndo(); }
    else if (meta && e.shiftKey && e.key.toLowerCase() === 'z') { e.preventDefault(); window.ctRedo(); }
    else if (meta && e.key.toLowerCase() === 's') { e.preventDefault(); window.ctSave(); }
  });

  window.addEventListener('load', () => setTimeout(restoreFromStorage, 50));
})();
</script>

<style>
.ct-toast {
  position: fixed;
  bottom: 72px; left: 50%;
  transform: translateX(-50%);
  padding: 8px 14px;
  background: var(--elevated, #1a1a1a);
  border: 1px solid var(--accent-1, #F3A950);
  border-radius: 4px;
  color: var(--accent-1, #F3A950);
  font: 700 11px/1 'Montserrat', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  z-index: 9999;
  animation: ct-toast-in 0.2s ease;
}
@keyframes ct-toast-in {
  from { opacity: 0; transform: translateX(-50%) translateY(8px); }
  to { opacity: 1; transform: translateX(-50%) translateY(0); }
}
.ct-restore-toast {
  bottom: auto;
  top: 72px;
  background: var(--elevated, #1a1a1a);
  border-color: color-mix(in srgb, var(--accent-1, #F3A950) 60%, transparent);
}
.ct-restore-toast a {
  color: var(--accent-1, #F3A950);
  text-decoration: underline;
  margin-left: 8px;
  cursor: pointer;
}
</style>
```

## Keyboard shortcuts

```html
<script data-creator-tools>
document.addEventListener('keydown', (e) => {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  if (document.activeElement && document.activeElement.hasAttribute('contenteditable')) return;
  if (e.key === 'e') window.ctToggleEdit && window.ctToggleEdit();
});
</script>
```

`e` — edit mode. `Ctrl+Z` / `Ctrl+Shift+Z` — undo / redo. `Ctrl+S` — save.

## Export behavior

The PNG button renders `.infographic-canvas` in-browser via html2canvas (loaded lazily on first click) and downloads a 2× PNG. Creator-tool elements are excluded via `ignoreElements`. `scripts/export.py` provides an alternative pixel-perfect Playwright render when invoked by Claude in the export chain.

## When to include

- **Always include** for iteration-mode HTML in Claude Code context (the default). Emit the toolbar + color editor unconditionally so the user can always reach them.
- **Omit** only for HTML that's being embedded somewhere (partner site, Notion embed, pitch deck slide), or when the user explicitly asks for a "clean" / "embed" / "final" export. In those cases, generate without creator tools or use `ctCleanDownload()` to produce a stripped version.
- **Omit** for HTML shipped to agent workflows (OpenClaw, Hermes) — they have no interactive iteration step.
