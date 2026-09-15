# Rasterizes each language's gtm-engineer-stack.svg (see build.py) to the
# PNG the article actually references via {attach} - at 2x the SVG's
# native viewBox size, matching every other image in this article series.
# Requires `pip install playwright && playwright install chromium` (not
# one of this repo's own requirements.txt deps - this script is a one-off
# authoring tool, not part of the site build).
#
# Usage: python3 render.py   (run from anywhere; paths are relative to
# this script's own location, not the caller's cwd)
import os
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SVG_NAME, PNG_NAME, W, H = "gtm-engineer-stack.svg", "gtm-engineer-stack.png", 1120, 1120

with sync_playwright() as p:
    b = p.chromium.launch()
    for lang in ["en", "de", "fr", "es"]:
        svg_path = os.path.join(BASE, lang, SVG_NAME)
        png_path = os.path.join(BASE, lang, PNG_NAME)
        with open(svg_path) as f:
            svg_content = f.read()
        html = f"<html><body style='margin:0;padding:0;'>{svg_content}</body></html>"
        page = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        page.set_content(html)
        page.wait_for_timeout(50)
        # the inline SVG has width/height=560x560 natively; scale it up
        # to the target pixel size via CSS on the svg element
        page.eval_on_selector("svg", f"el => {{ el.style.width='{W}px'; el.style.height='{H}px'; }}")
        page.wait_for_timeout(50)
        page.screenshot(path=png_path)
        page.close()
        print("rendered", png_path)
    b.close()
