# Morgen Tech — brand assets (2026-11)

The **MT monogram** (logo option 3, chosen by Chen on 2026-11-15). A square navy tile
holds a serif "M". A horizontal bar sits over the M; read together they form the "T", so the
tile says MT. The tile stands next to the "Morgen Tech" wordmark in the same serif.

Colours: navy `#0D2340`, gold `#F0C040`, white. Nothing else.
- **Colour** (on light backgrounds): navy tile, white M, gold bar, navy wordmark.
- **White** (on navy or dark backgrounds): white tile, navy M and bar (knockout), white wordmark.
  The site header, the home footer and the Impressum use this one.
- **Mono black / mono white**: one-colour print, laser engraving, PCB silkscreen.

The bar is gold only on the navy tile. On any other tile it takes the colour of the M.

Files
- `svg/morgen-tech_lockup_{color,white,mono-black,mono-white}.svg`: the primary lock-up, cropped
  to its content box (viewBox `8 14 353.3 52`). Add clear space when you place it.
- `svg/mark_{color,white,mono-black,mono-white}.svg`: the tile alone (avatars, stamps, small sizes).
- `svg/favicon.svg`: the colour mark. A copy sits at the site root.
- `png/*.png` and `png/*@2x.png`: transparent rasters of every SVG. The lock-up is 104 px tall at 1x
  and 208 px at 2x. The mark is 96 px and 192 px.
- `png/favicon-{16,32,48,180,512}.png`, `png/favicon.ico` (16/32/48) and `png/apple-touch-icon.png`
  (180 px, full-bleed tile, opaque). Copies of the .ico and the apple-touch icon sit at the site root.

Rules of thumb
- Clear space is half the tile height on all sides.
- Use the lock-up at 24 px tall or more. Below that, use the mark alone.
- Never recolour the bar, and never stretch or re-set the type.
- All SVGs are pure paths, so no fonts are needed.

Source: marketing/docs `product/brand/logo-options_2026-11-15/` (commit 7472ce3). The generator is
`src/build_options.py` there. The rasters here are browser renders of the SVGs above.

`archive/` holds the previous 2026-09 "sensing mark" set (ring and damped transient) with its own
README and `build.py`. It is kept for reference and must not be used on new material.
