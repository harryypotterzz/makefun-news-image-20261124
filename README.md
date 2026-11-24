# World News — 24 November 2026 in one image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/harryypotterzz/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/harryypotterzz/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the [make.fun bounty "Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124) (competition `news-image-20261124`).

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one
image to `/output/entry.png`: a copy of `entry.png`, the image this
repository holds. The image sums up Tuesday 24 November 2026's world
news in a newspaper front page:

1. **US blacklists Megaspeed** — Washington adds Singapore's Megaspeed
   and six more firms to its Entity List in the Nvidia spy scandal.
2. **Zelensky: four-way talks now** — Kyiv ready to meet Ukraine,
   Russia, the US and Europe "literally tomorrow".
3. **Patriot missiles held up** — Hegseth has yet to approve about 60
   Patriot interceptors already agreed for Ukraine (FT).
4. **Russian drone over Poland** — a drone briefly entered Polish
   airspace on 22 Nov, days after three Russian objects crashed there.
5. **Huang back as Nvidia CEO** — board reinstates Jensen Huang 11
   days after he resigned; shares jump about 30%.
6. **24 dead in factory fire** — blaze at the Milkita candy plant in
   Cikande, Banten; about 30 workers still missing.
7. **COP31 ends without deal** — Antalya climate talks collapse over
   fossil fuels, first breakdown since 2009.
8. **Iran vows to break US blockade** — Tehran threatens military
   means; Qatar PM meets Rubio and Vance.

Every headline was verified against reputable reporting on 24 Nov
2026 (Reuters, Al Jazeera, Financial Times, France 24, Morningstar
and others) before the image was drawn.

## How the image was made

`gen_image.py` (build-time tooling, Pillow + DejaVu fonts) renders
`entry.png` (1024×1024, ~113 KB) from the headlines above. The entry
program itself only copies that file, so it is deterministic: every
run writes the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# main.py: wrote out/entry.png (115711 bytes)
```

## License

MIT — see [LICENSE](LICENSE).
