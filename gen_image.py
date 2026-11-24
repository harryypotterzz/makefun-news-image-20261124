#!/usr/bin/env python3
"""Build-time image generator for the news-image-20261124 entry.

Renders entry.png (1024x1024) from the verified 24 Nov 2026 headlines.
Build-time tooling only (Pillow + DejaVu fonts); the submitted entry
program main.py is stdlib-only and just copies entry.png to /output.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BG = (245, 243, 238)          # warm paper
HEADER_BG = (11, 31, 58)      # dark navy
HEADER_GOLD = (212, 175, 55)  # gold
CARD_BG = (255, 255, 255)
CARD_BORDER = (200, 198, 192)
INK = (18, 24, 33)
MUTED = (90, 96, 108)
STRIP_BG = (11, 31, 58)

# (kicker, headline, body, accent colour)
PANELS = [
    ("USA — CHIPS & SPYING",
     "US blacklists Megaspeed in Nvidia spy scandal",
     "Washington adds Singapore's Megaspeed and six more Southeast Asian firms to its Entity List.",
     (192, 57, 43)),
    ("UKRAINE — PEACE TALKS",
     "Zelensky: four-way talks now",
     "Kyiv says it is ready to meet Ukraine, Russia, the US and Europe \u201cliterally tomorrow\u201d.",
     (36, 113, 163)),
    ("UKRAINE — AIR DEFENCE",
     "Patriot missiles held up",
     "Hegseth has yet to approve about 60 Patriot interceptors already agreed for Ukraine, FT reports.",
     (46, 134, 193)),
    ("POLAND — NATO",
     "Russian drone over Poland",
     "A drone briefly entered Polish airspace on 22 Nov, days after three Russian objects crashed there.",
     (146, 43, 33)),
    ("TECH — NVIDIA",
     "Huang back as Nvidia CEO",
     "Board reinstates Jensen Huang 11 days after he resigned; shares jump about 30%.",
     (30, 132, 73)),
    ("INDONESIA — TRAGEDY",
     "24 dead in factory fire",
     "Blaze at the Milkita candy plant in Cikande, Banten; about 30 workers still missing.",
     (202, 111, 30)),
]

STRIPS = [
    ("COP31 ENDS WITHOUT DEAL",
     "Antalya climate talks collapse over fossil fuels — first breakdown since 2009."),
    ("IRAN VOWS TO BREAK US BLOCKADE",
     "Tehran threatens military means; Qatar PM meets Rubio and Vance."),
]


def wrap(draw, text, font, max_w):
    """Greedy word wrap returning a list of lines fitting max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # --- Header band ---
    d.rectangle([0, 0, W, 118], fill=HEADER_BG)
    f_title = ImageFont.truetype(FONT_BOLD, 58)
    f_date = ImageFont.truetype(FONT_BOLD, 26)
    d.text((24, 14), "WORLD NEWS", font=f_title, fill=(255, 255, 255))
    d.text((24, 76), "TUESDAY, 24 NOVEMBER 2026", font=f_date, fill=HEADER_GOLD)
    # red rule under header
    d.rectangle([0, 118, W, 124], fill=(192, 57, 43))

    # --- 6 main panels: 2 cols x 3 rows ---
    mx, col_w, gap_x = 24, 476, 24
    y0, row_h, gap_y = 134, 234, 14
    f_kick = ImageFont.truetype(FONT_BOLD, 17)
    f_head = ImageFont.truetype(FONT_BOLD, 29)
    f_body = ImageFont.truetype(FONT_REG, 20)
    for i, (kicker, headline, body, accent) in enumerate(PANELS):
        col, row = i % 2, i // 2
        x = mx + col * (col_w + gap_x)
        y = y0 + row * (row_h + gap_y)
        d.rounded_rectangle([x, y, x + col_w, y + row_h], radius=8,
                            fill=CARD_BG, outline=CARD_BORDER, width=2)
        d.rectangle([x + 8, y, x + col_w - 8, y + 6], fill=accent)
        tx = x + 18
        d.text((tx, y + 20), kicker, font=f_kick, fill=accent)
        head_lines = wrap(d, headline, f_head, col_w - 36)
        hy = y + 48
        for ln in head_lines[:2]:
            d.text((tx, hy), ln, font=f_head, fill=INK)
            hy += 36
        body_lines = wrap(d, body, f_body, col_w - 36)
        by = hy + 6
        for ln in body_lines[:3]:
            d.text((tx, by), ln, font=f_body, fill=MUTED)
            by += 27

    # --- 2 supporting strips (two lines each: kicker + body) ---
    f_strip_k = ImageFont.truetype(FONT_BOLD, 20)
    f_strip_b = ImageFont.truetype(FONT_REG, 19)
    sy = 874
    for kicker, body in STRIPS:
        d.rounded_rectangle([mx, sy, W - mx, sy + 62], radius=8, fill=STRIP_BG)
        d.text((mx + 18, sy + 8), kicker, font=f_strip_k, fill=HEADER_GOLD)
        d.text((mx + 18, sy + 34), body, font=f_strip_b,
               fill=(255, 255, 255))
        sy += 72

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {img.size}")


if __name__ == "__main__":
    main()
