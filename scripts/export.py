#!/usr/bin/env python3
"""Export an infographic HTML to PNG via Playwright.

Usage:
    python scripts/export.py path/to/file.html
    python scripts/export.py --png path/to/file.html

Optional:
    --scale N          device scale factor (default: 2)
    --out DIR          output directory (default: same dir as input)
    --selector CSS     element to capture (default: .infographic-canvas)

Dependencies:
    pip install playwright>=1.40.0
    playwright install chromium
"""

from __future__ import annotations

import argparse
import http.server
import socket
import socketserver
import sys
import threading
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.stderr.write(
        "playwright is not installed. Run:\n"
        "    pip install playwright>=1.40.0\n"
        "    playwright install chromium\n"
    )
    sys.exit(2)


CANVAS_SELECTOR_DEFAULT = ".infographic-canvas"
FONT_SETTLE_MS = 400


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class _SilentHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):  # noqa: A002 - stdlib signature
        pass


def _start_static_server(root: Path) -> tuple[socketserver.TCPServer, int, threading.Thread]:
    port = _find_free_port()
    handler = lambda *a, **kw: _SilentHandler(*a, directory=str(root), **kw)
    httpd = socketserver.TCPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd, port, thread


def _prepare_page_state(page, selector: str) -> None:
    """Force viewer features to final state so PNG capture isn't mid-animation."""
    page.evaluate(
        """(sel) => {
            document.querySelectorAll('[data-counter-to]').forEach(el => {
                const to = Number(el.dataset.counterTo);
                if (!Number.isNaN(to)) {
                    el.textContent = new Intl.NumberFormat('en-US').format(to);
                    el.dataset.counted = '1';
                }
            });
            document.querySelectorAll('.section').forEach(s => s.classList.add('visible'));
            document.querySelectorAll('[data-creator-tools]').forEach(el => {
                el.style.display = 'none';
            });
        }""",
        selector,
    )


def _measure_canvas(page, selector: str) -> tuple[int, int]:
    box = page.evaluate(
        """(sel) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            const r = el.getBoundingClientRect();
            return { w: Math.ceil(r.width), h: Math.ceil(r.height) };
        }""",
        selector,
    )
    if not box:
        raise RuntimeError(f"Canvas element not found: {selector}")
    return box["w"], box["h"]


def export_png(
    html_path: Path,
    out_dir: Path,
    scale: float,
    selector: str,
) -> Path:
    out_path = out_dir / f"{html_path.stem}.png"
    root = html_path.parent
    httpd, port, _ = _start_static_server(root)
    try:
        url = f"http://127.0.0.1:{port}/{html_path.name}"
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            context = browser.new_context(device_scale_factor=scale, viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            page.goto(url, wait_until="load")
            page.wait_for_function("document.fonts && document.fonts.ready.then(() => true)")
            page.wait_for_timeout(FONT_SETTLE_MS)
            _prepare_page_state(page, selector)
            w, h = _measure_canvas(page, selector)
            page.set_viewport_size({"width": w, "height": h})
            page.wait_for_timeout(80)
            el = page.query_selector(selector)
            if el is None:
                raise RuntimeError(f"Canvas element not found: {selector}")
            el.screenshot(path=str(out_path), type="png", omit_background=False)
            browser.close()
    finally:
        httpd.shutdown()
        httpd.server_close()
    return out_path


def main() -> int:
    p = argparse.ArgumentParser(description="Export infographic HTML to PNG")
    p.add_argument("html", help="path to the HTML file")
    p.add_argument("--png", action="store_true", help="(default) export PNG")
    p.add_argument("--scale", type=float, default=2.0, help="device scale factor (default: 2)")
    p.add_argument("--out", type=str, default=None, help="output directory (default: same as input)")
    p.add_argument("--selector", type=str, default=CANVAS_SELECTOR_DEFAULT)
    args = p.parse_args()

    html_path = Path(args.html).resolve()
    if not html_path.exists() or not html_path.is_file():
        sys.stderr.write(f"Input file not found: {html_path}\n")
        return 1

    out_dir = Path(args.out).resolve() if args.out else html_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    try:
        png = export_png(html_path, out_dir, args.scale, args.selector)
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"PNG_EXPORT_FAILED: {e}\n")
        return 1

    elapsed = time.time() - t0
    print(f"\nExport complete ({elapsed:.1f}s):")
    print(f"  HTML: {html_path}")
    print(f"  PNG:  {png}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
