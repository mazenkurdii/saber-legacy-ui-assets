# Renders icons.py into one 1024x1024 atlas (8x8 cells of 128px) plus a soft glow
# in the last cell, and writes the cell index map used by Client.UI.Icons.
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from icons import ICONS
from playwright.sync_api import sync_playwright
OUT = sys.argv[1]
names = list(ICONS.keys())
cells = []
for i, n in enumerate(names):
    x, y = (i % 8) * 128, (i // 8) * 128
    cells.append(f'<svg style="position:absolute;left:{x}px;top:{y}px" width="128" height="128" viewBox="0 0 128 128">{ICONS[n]}</svg>')
glow_index = 63
gx, gy = (glow_index % 8) * 128, (glow_index // 8) * 128
cells.append(f'<div style="position:absolute;left:{gx}px;top:{gy}px;width:128px;height:128px;background:radial-gradient(circle at center, rgba(255,255,255,1) 0%, rgba(255,255,255,.45) 30%, rgba(255,255,255,0) 70%)"></div>')
html = f'<html><body style="margin:0;background:transparent"><div style="position:relative;width:1024px;height:1024px">{"".join(cells)}</div></body></html>'
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1024, "height": 1024})
    pg.set_content(html)
    pg.screenshot(path=os.path.join(OUT, "icons.png"), omit_background=True)
    # preview on dark background for review
    pg.set_content(html.replace("background:transparent", "background:#151a22"))
    pg.screenshot(path=os.path.join(OUT, "icons_preview.png"))
    b.close()
index = {n: i for i, n in enumerate(names)}
index["Glow"] = glow_index
json.dump(index, open(os.path.join(OUT, "icons.json"), "w"), indent=1)
print(len(names), "icons")
# Flatten to pure white glyphs: black cut-outs (keyholes, grip slots) become transparent.
from PIL import Image
im = Image.open(os.path.join(OUT, "icons.png")).convert("RGBA")
px = im.load()
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]
        lum = (r + g + b) / 3
        px[x, y] = (255, 255, 255, int(a * lum / 255))
im.save(os.path.join(OUT, "icons.png"))
