# Saber Legacy UI assets

Source and rendered art for the Saber Legacy (Roblox) interface.

- `src/icons.py`: icon set (SVG, 128px cells, white on transparent)
- `src/build.py`: renders the atlas with headless Chromium (`python3 src/build.py ui`)
- `ui/icons.png`: 1024x1024 atlas, 8x8 cells of 128px; `ui/icons.json` maps icon names to cell index
- `ui/icons_preview.png`: the same sheet on a dark background for review

In game, `Client.UI.Icons` holds the uploaded atlas asset id and the cell map.
