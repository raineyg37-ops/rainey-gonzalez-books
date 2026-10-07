"""Build the social preview for the real four-page free-sample hub."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "free-sample-pages-card.png"
PAPER = "#fff9ed"
SEA = "#176b70"
INK = "#153b40"
GOLD = "#e9bd72"

im = Image.new("RGB", (1200, 630), PAPER)
d = ImageDraw.Draw(im)
d.rectangle((0, 0, 470, 630), fill=SEA)
d.text((54, 48), "RAINEY GONZALEZ BOOKS", font=ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 26), fill=PAPER)
headline = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 63)
for y, line in [(140, "Try a real"), (213, "page before"), (286, "the book.")]:
    d.text((54, y), line, font=headline, fill=PAPER)
d.line((54, 406, 402, 406), fill=GOLD, width=8)
d.text((54, 437), "4 free sample pages", font=ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 35), fill=PAPER)
d.text((54, 493), "No signup · Personal use", font=ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26), fill=PAPER)

sources = [
    "free-narwhal-coloring-page.png",
    "the-math-isnt-mathing-free-page.png",
    "lets-unpack-that-free-page.png",
    "free-bride-trivia-page.png",
]
for i, filename in enumerate(sources):
    src = Image.open(ASSETS / filename).convert("RGB")
    src.thumbnail((140, 390), Image.Resampling.LANCZOS)
    left = 496 + i * 173
    top = 116 + (i % 2) * 24
    d.rounded_rectangle((left - 6, top - 6, left + 146, top + 396), radius=9, fill="white", outline=GOLD, width=3)
    im.paste(src, (left + (140 - src.width) // 2, top + (390 - src.height) // 2))
d.text((514, 554), "COLORING  ·  ALPHABET  ·  PARTY ACTIVITY", font=ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 20), fill=INK)
im.save(OUT, optimize=True)
print(OUT)
