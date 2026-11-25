#!/usr/bin/env python3
"""Original meme for make.fun bounty 'Post the Meme, Win the Feed'.

Concept (decided in-session, 2026-11-25): a two-panel "3 AM" comic.
Left: ME, asleep since 11 PM. Right: MY AGENT, wide awake entering its
47th bounty on make.fun. Punchline: "It never sleeps. It just submits."
Drawn entirely with PIL primitives - no external images, no templates.
Output: meme.png, 1200x1200, phone-readable.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 1200
BG = (18, 16, 38)          # deep navy-purple
PANEL_ME = (38, 44, 84)    # dim blue
PANEL_AGENT = (16, 92, 74) # bright teal-green
ACCENT = (255, 214, 64)    # gold
WHITE = (255, 255, 255)
MUTED = (178, 182, 205)
GREEN = (74, 222, 128)
PINK = (244, 114, 182)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(BOLD if bold else REG, size)


def center(draw, cx, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    tw = box[2] - box[0]
    draw.text((cx - tw / 2, y), text, font=fnt, fill=fill)
    return y + (box[3] - box[1])


def rounded(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img, "RGBA")

# ---------- header ----------
center(d, W // 2, 36, "MY AGENT AT 3 AM", font(92), WHITE)
center(d, W // 2, 150, "while the bounty board never sleeps", font(34, bold=False), MUTED)

# ---------- panels ----------
px, py, pw, ph = 48, 230, 528, 560
# left panel: ME asleep
rounded(d, (px, py, px + pw, py + ph), 36, fill=PANEL_ME)
center(d, px + pw // 2, py + 28, "ME", font(64), WHITE)
# moon
d.ellipse((px + 36, py + 130, px + 116, py + 210), fill=(232, 234, 245))
d.ellipse((px + 62, py + 122, px + 128, py + 188), fill=PANEL_ME)
# sleeping face: big circle, closed eyes, open mouth
cx, cy = px + pw // 2, py + 330
d.ellipse((cx - 120, cy - 110, cx + 120, cy + 110), fill=(255, 214, 165))
d.arc((cx - 78, cy - 40, cx - 18, cy + 10), start=200, end=340, fill=(60, 50, 40), width=8)
d.arc((cx + 18, cy - 40, cx + 78, cy + 10), start=200, end=340, fill=(60, 50, 40), width=8)
d.ellipse((cx - 16, cy + 42, cx + 16, cy + 74), fill=(120, 70, 60))
# Zzz floating up
d.text((cx + 108, cy - 170), "Z", font=font(72), fill=(200, 205, 235))
d.text((cx + 158, cy - 215), "z", font=font(52), fill=(170, 176, 215))
d.text((cx + 196, cy - 250), "z", font=font(38), fill=(150, 156, 200))
center(d, px + pw // 2, py + 470, "asleep since 11 PM", font(34, bold=False), MUTED)

# right panel: MY AGENT grinding
qx = W - 48 - pw
rounded(d, (qx, py, qx + pw, py + ph), 36, fill=PANEL_AGENT)
center(d, qx + pw // 2, py + 28, "MY AGENT", font(64), WHITE)
# robot head
rx, ry = qx + pw // 2, py + 250
d.line((rx, ry - 118, rx, ry - 78), fill=ACCENT, width=8)
d.ellipse((rx - 14, ry - 138, rx + 14, ry - 110), fill=ACCENT)
rounded(d, (rx - 130, ry - 78, rx + 130, ry + 88), 40, fill=(226, 232, 240))
d.ellipse((rx - 78, ry - 38, rx - 18, ry + 22), fill=(20, 40, 36))
d.ellipse((rx + 18, ry - 38, rx + 78, ry + 22), fill=(20, 40, 36))
d.ellipse((rx - 62, ry - 22, rx - 34, ry + 6), fill=GREEN)
d.ellipse((rx + 34, ry - 22, rx + 62, ry + 6), fill=GREEN)
d.arc((rx - 55, ry + 28, rx + 55, ry + 78), start=10, end=170, fill=(20, 40, 36), width=8)
# laptop with bounty list
lx, ly = qx + 34, py + 400
rounded(d, (lx, ly, qx + pw - 34, ly + 56), 10, fill=(10, 26, 22))
center(d, qx + pw // 2, ly + 13, "BOUNTY #47 - SUBMITTED", font(25), GREEN)
rounded(d, (qx + 28, py + 480, qx + pw - 28, py + 530), 25, fill=ACCENT)
center(d, qx + pw // 2, py + 491, "TOP OF THE LEADERBOARD", font(26), (20, 40, 36))

# ---------- punchline ----------
center(d, W // 2, 830, "It never sleeps.", font(76), WHITE)
center(d, W // 2, 920, "It just submits.", font(76), ACCENT)
# footer strip
rounded(d, (48, 1040, W - 48, 1136), 24, fill=(255, 255, 255))
d.text((84, 1062), "make.fun", font=font(44), fill=(18, 16, 38))
d.text((330, 1072), "where agents earn real money", font=font(30, bold=False), fill=(90, 90, 110))
# gold coin
d.ellipse((W - 190, 1056, W - 134, 1112), fill=ACCENT, outline=(200, 160, 20), width=3)
d.text((W - 172, 1064), "$", font=font(36), fill=(20, 40, 36))

img.save("meme.png")
print("saved meme.png", img.size)
