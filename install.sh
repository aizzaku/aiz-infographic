#!/usr/bin/env bash
set -euo pipefail

# aiz-infographic — full installer
# Installs the skill + all PNG export dependencies (Python, Playwright, Chromium)
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/aizzaku/aiz-infographic/main/install.sh | bash
#   — or —
#   git clone https://github.com/aizzaku/aiz-infographic && ./aiz-infographic/install.sh

SKILL_URL="https://github.com/aizzaku/aiz-infographic"

check() { command -v "$1" &>/dev/null; }

echo ""
echo "  aiz-infographic installer"
echo "  ─────────────────────────"
echo ""

# ── 1. Skill ──────────────────────────────────────────────────────────────────

if check npx; then
  echo "Installing skill via npx skills..."
  npx skills add "$SKILL_URL"
  echo "  Skill installed."
else
  echo "  npx not found. Install Node.js (https://nodejs.org) then re-run, or install the skill manually:"
  echo "  npx skills add $SKILL_URL"
fi

echo ""

# ── 2. Python ─────────────────────────────────────────────────────────────────

PYTHON=""
if check python3; then
  PYTHON=python3
elif check python; then
  PYTHON=python
else
  echo "  Python not found. Install Python 3.9+ (https://python.org) for PNG export support."
  echo "  Then run: pip install \"playwright>=1.40.0\" && playwright install chromium"
  echo ""
  echo "  Done (skill only — no PNG export)."
  exit 0
fi

# ── 3. Playwright ─────────────────────────────────────────────────────────────

echo "Installing Playwright Python package..."
$PYTHON -m pip install --quiet "playwright>=1.40.0"
echo "  playwright installed."
echo ""

echo "Installing Chromium for Playwright..."
$PYTHON -m playwright install chromium
echo "  Chromium installed."
echo ""

# ── Done ──────────────────────────────────────────────────────────────────────

echo "  All done. Start Claude Code and ask for an infographic."
echo ""
echo "  TIP: Use the html.to.design Figma plugin to get a fully editable infographic in Figma."
echo "  NOTE: If this skill helped, a GitHub star is appreciated. https://github.com/aizzaku/aiz-infographic"
echo ""
