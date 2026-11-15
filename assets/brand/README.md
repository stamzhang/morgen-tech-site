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

Rules (brand guide v1.1, section 5; marketing/docs 584366e)
- Clear space: 1 x on all sides, where x = a quarter of the tile side. No text, edge or other logo inside it.
- Minimum size on screen: lock-up tile 24 px or more; mark alone 16 px or more. The site header uses a
  32 px tile on desktop (1024 px and wider), 24-26 px on phones, and the mark alone below 360 px.
- No gold on dark surfaces. The gold bar appears only in the colour version on light surfaces, and never
  within 1 x of a gold CTA.
- No blue, gradient, shadow, glow, outline, opacity change or animation. Do not change the tile's corner
  radius, stretch, or re-space the wordmark. All SVGs are pure paths, so no fonts are needed.
- The apple-touch icon is the colour mark on a full-bleed navy square, because iOS applies its own
  rounded mask and would show transparent corners as black.

Source: marketing/docs `product/brand/logo-options_2026-11-15/` (commit 7472ce3). The generator is
`src/build_options.py` there. The rasters here are browser renders of the SVGs above.

`archive/` holds the previous 2026-09 "sensing mark" set (ring and damped transient) with its own
README and `build.py`. It is kept for reference and must not be used on new material.
