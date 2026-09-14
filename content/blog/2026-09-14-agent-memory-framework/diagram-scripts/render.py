# Rasterizes each language's agent-memory-diagram.svg /
# agent-memory-governance-diagram.svg (see build.py) to the PNGs the
# articles actually reference via {attach} - at 2x the SVG's native
# viewBox size, matching every other image in this article. Requires
# `pip install playwright && playwright install chromium` (not one of
# this repo's own requirements.txt deps - this script is a one-off
# authoring tool, not part of the site build).
#
# Usage: python3 render.py   (run from anywhere; paths are relative to
# this script's own location, not the caller's cwd)
import os
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

jobs = [
    ("agent-memory-diagram.svg", "agent-memory-diagram.png", 1360, 720),
    ("agent-memory-governance-diagram.svg", "agent-memory-governance-diagram.png", 1360, 800),
]

with sync_playwright() as p:
    b = p.chromium.launch()
    for lang in ["en", "de", "fr", "es"]:
        for svg_name, png_name, w, h in jobs:
            svg_path = os.path.join(BASE, lang, svg_name)
            png_path = os.path.join(BASE, lang, png_name)
            with open(svg_path) as f:
                svg_content = f.read()
            html = f"<html><body style='margin:0;padding:0;'>{svg_content}</body></html>"
            page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            page.set_content(html)
            page.wait_for_timeout(50)
            # the inline SVG has width/height=680x360 (or 680x400) natively;
            # scale it up to the target pixel size via CSS on the svg element
            page.eval_on_selector("svg", f"el => {{ el.style.width='{w}px'; el.style.height='{h}px'; }}")
            page.wait_for_timeout(50)
            page.screenshot(path=png_path)
            page.close()
            print("rendered", png_path)
    b.close()
