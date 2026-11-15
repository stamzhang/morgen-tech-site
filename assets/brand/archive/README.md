# Morgen Tech — brand assets (2026-09)

Successor to the 2015–2019 "MOrgen" filament-spool logo. Same DNA — a geometric
monoline wordmark with a distinctive O — but the O is now a **sensing mark**: a ring
(the probe / the cabinet) around a damped transient (the underdamped ringing on a
control rail that started the company). It is *not* a heartbeat: sharp rise, undershoot,
decaying oscillation, settle.

Colours: navy `#0D2340` (wordmark), blue `#1A6FD4` (ring, "TECH"), gold `#F0C040`
(transient). On dark backgrounds the wordmark is white and the ring `#5FA8F8`.

Files
- `svg/morgen-tech_horizontal_{color,white,mono-black,mono-white}.svg` — primary lock-up.
- `svg/morgen_wordmark_color.svg` — wordmark without "TECH" (RailSentinel co-branding).
- `svg/mark_{color,white,mono}.svg` — the mark alone (avatars, stamps, PCB silkscreen: use mono).
- `svg/favicon.svg` + `png/favicon-{16,32,48,180,512}.png`, `png/favicon.ico`.
- `png/*.png`, `png/*@2x.png` — transparent raster exports of every SVG.

Rules of thumb: clear space = ring diameter on all sides; never below 24 px height for the
lock-up (use the mark alone below that); never recolour the transient; mono versions for
one-colour print, laser engraving and silkscreen. All SVGs are pure paths — no fonts needed.
Source generator: `build.py` (Python, no dependencies) in the same folder.
