# -*- coding: utf-8 -*-
"""Setzt alle freigestellten Kerzen auf den einheitlichen Creme-Hintergrund."""
import os, subprocess
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

M = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(M, "cut")
OUT = os.path.join(M, "fertig")
os.makedirs(OUT, exist_ok=True)
G = r"C:\Users\manue\Documents\Claude\Kerzenküche\galerie\bilder"
B = "https://pikaso.cdnpk.net/private/production/"
T = "/sam-mask.png?token=exp=1791849600~hmac="


def bg(W, H):
    y = np.linspace(0, 1, H)[:, None]
    top = np.array([248, 244, 237.]); mid = np.array([238, 231, 220.]); table = np.array([226, 214, 197.]); hz = 0.80
    b = np.where(y < hz, top + (mid - top) * (y / hz), mid + (table - mid) * ((y - hz) / (1 - hz)))
    b = np.broadcast_to(b.reshape(H, 1, 3), (H, W, 3)).copy()
    xx = np.linspace(-1, 1, W)[None, :]; yy = np.linspace(-1, 1, H)[:, None]
    b *= (1 - 0.07 * (xx ** 2 + 0.5 * yy ** 2))[:, :, None]
    return Image.fromarray(np.clip(b, 0, 255).astype(np.uint8)).convert("RGBA")


def shadow(c, x0, x1, base, blur):
    W, H = c.size
    sh = Image.new("L", (W, H), 0); d = ImageDraw.Draw(sh)
    w = x1 - x0
    d.ellipse((x0 + w * 0.05, base - max(8, w * 0.045), x1 - w * 0.05, base + max(7, w * 0.035)), fill=110)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    s2 = Image.new("RGBA", (W, H), (80, 60, 45, 0)); s2.putalpha(sh)
    return Image.alpha_composite(c, s2)


def load(png, bright=1.0):
    fg = Image.open(png).convert("RGBA"); fg = fg.crop(fg.split()[3].getbbox())
    if bright != 1.0:
        a = fg.split()[3]; fg = ImageEnhance.Brightness(fg.convert("RGB")).enhance(bright).convert("RGBA"); fg.putalpha(a)
    return fg


def place(c, fg, cx, base, h):
    s = h / fg.height; fg = fg.resize((max(1, int(fg.width * s)), int(h)), Image.LANCZOS)
    x = int(cx - fg.width / 2)
    c = shadow(c, x, x + fg.width, base, max(10, c.size[1] / 90))
    c.alpha_composite(fg, (x, int(base - fg.height)))
    return c


def save(c, name):
    c.convert("RGB").save(os.path.join(OUT, name + ".jpg"), "JPEG", quality=85, optimize=True, progressive=True)


# ---------- 1) Einzelkerzen: 4:5 Hochformat
EINZEL = {
    "taufkerze-blaue-rosen-sonne-fische": ("taufkerze-blaue-rosen-sonne-fische.png", 1.03),
    "taufkerze-bordeaux-kreuz-taube": ("taufkerze-bordeaux-kreuz-taube.png", 1.03),
    "jubilaeumskerze-fotodruck": ("jubilaeumskerze-fotodruck.png", 1.03),
    "schulanfangskerze-abc-schultueten": ("schulanfangskerze-abc-schultueten.png", 1.0),
    "trauerkerze-stiller-abschied": ("trauerkerze-stiller-abschied.png", 1.03),
    "hochzeitskerze-blaetterkranz": (os.path.join("..", "hochzeit.png"), 1.0),
    "trauerkerze-fuer-immer-in-unserem-herzen": (os.path.join("..", "trauer.png"), 1.0),
}
for name, (png, br) in EINZEL.items():
    fg = load(os.path.join(C, png), br)
    W, H = 1200, 1500
    c = bg(W, H)
    h = min(H * 0.80, W * 0.80 * fg.height / fg.width)
    c = place(c, fg, W / 2, int(H * 0.91), h)
    save(c, name)

# ---------- 2) Collagen neu: Kerzen nebeneinander auf Creme
def reihe(c, files, y_base, h, x0, x1, br=1.03):
    fgs = [load(os.path.join(C, f), br) for f in files]
    n = len(fgs); step = (x1 - x0) / n
    for i, fg in enumerate(fgs):
        c = place(c, fg, x0 + step * (i + 0.5), y_base, h)
    return c

W = H = 1600
c = bg(W, H); c = reihe(c, ["taufe-blau-1.png", "taufe-blau-2.png", "taufe-blau-3.png"], int(H * 0.88), H * 0.70, 80, W - 80)
save(c, "taufkerzen-blau-kreuz-lebensbaum")
c = bg(W, H); c = reihe(c, ["taufe-rosa-1.png", "taufe-rosa-2.png", "taufe-rosa-3.png"], int(H * 0.88), H * 0.70, 80, W - 80)
save(c, "taufkerzen-rosa-maedchen")
c = bg(W, H)
c = reihe(c, ["geburtstag-1.png", "geburtstag-2.png", "geburtstag-3.png"], int(H * 0.46), H * 0.38, 60, W - 60)
c = reihe(c, ["geburtstag-4.png", "geburtstag-5.png", "geburtstag-6.png"], int(H * 0.93), H * 0.38, 60, W - 60)
save(c, "geburtstagskerzen-jubilaeum")

# ---------- 3) Deko: Kerzen an Originalposition, ohne Figuren/Bonsai
DEKO = {
    "formkerzen-creme-gedreht": ["5679875676" + T + "a6ef27a2fab3d6e006d4ad641544ef8a4d6c80e6ea9ef1ae380c1b74459d8294",
                                 "5679876342" + T + "24cf2d3c98dae4ca346a5677aea8c4877fec5a258f3e32f30f26db31a3fc9d78"],
    "formkerzen-pink": ["5679876892" + T + "428058b638b0031001cb3ade370e224f77a1b121039c93fa454e07750782412f",
                        "5679877603" + T + "3916f8de6cff9356745b96e81d1adcc74b3fa415041f812f3fc0e3f7d5912efd",
                        "5679878168" + T + "fc966955e61a01d3e728f89abdf72acb60e357e0bf1229624afda62712bda8aa",
                        "5679878708" + T + "21cd1853ba059625aef7d40352bb3d31a398638170f2b6f855e402da52035938",
                        "5679879351" + T + "fa43c8f8d1014ad05c4b35f00e88cc55c96cc5ac5692d59a3e6b2316749c1430",
                        "5679858793" + T + "a0eb6256c401496aaf513501346c0a8203f61f4f21400101fe85c43a0fe3f039"],
    "kugelkerzen-blau-pyramide": ["5679879981" + T + "df3f7ba5b054f0e1be6999a00d26ee0f7f1fd62d9191fe244b66f2e44a582652",
                                  "5679880603" + T + "48aec16743294a50ad21f5b4f21dbf1bea6c3136e282f9040469f0064921a805",
                                  "5679881172" + T + "32837432709f32b314df93e6b9f42abd909035558f34a12f2a192c193469acfd"],
    "schichtkerzen-tuerkis-gruen": ["5679860261" + T + "e8c8b89e588b354922d5bfb5e9a9a27fd007c19b1c221576ea245f2c006ea154",
                                    "5679881856" + T + "9d2e06699b12dcbdf14e7e94a63cf727554168da78e3273fb8e67a584b3d5e80"],
    "formkerzen-weiss-kugel-blau": ["5679862066" + T + "4108961057906435d5b4d864d5739d4b4ee4464ad60419cb3f42765b79afc7f2",
                                    "5679883652" + T + "d6ea88495185efd398247367a6d76425aaeb916928321a5940319cbaba5a6ca1",
                                    "5679884282" + T + "688f891182fce535a92518b2c8b11a791422382421c2bf94d127692be13c4013",
                                    "5679928006" + T + "065b7a4297aa46e60d42a9c6e4095f6c4192391810a974750a5a262ab1b68384"],
    "sechseckkerze-blau-weiss": ["5679834845" + T + "261f96775c812932ac0c5a17824b1bec62345ebe8f5a66ed4559d1a94a8e90af"],
}
os.makedirs(os.path.join(C, "masken"), exist_ok=True)
for name, urls in DEKO.items():
    foto = Image.open(os.path.join(G, name + ".jpg")).convert("RGB")
    Wf, Hf = foto.size
    teile = []
    for i, u in enumerate(urls):
        f = os.path.join(C, "masken", f"{name}-{i}.png")
        if not os.path.exists(f):
            subprocess.run(["curl", "-s", "-o", f, B + u], check=True)
        m = Image.open(f).convert("L").resize((Wf, Hf))
        m = m.point(lambda v: 255 if v > 127 else 0).filter(ImageFilter.GaussianBlur(0.8))
        bb = m.getbbox()
        if bb:
            teile.append((bb[3], m, bb))
    # doppelte Masken (gleiche Kerze mehrfach erkannt) entfernen
    eindeutig = []
    for t in teile:
        a = np.asarray(t[1]) > 127
        if all((a & b).sum() / max(1, (a | b).sum()) < 0.5 for b in [np.asarray(u[1]) > 127 for u in eindeutig]):
            eindeutig.append(t)
    print(name, len(teile), "->", len(eindeutig), "Kerzen")
    teile = eindeutig
    # Kerzen einzeln ausschneiden (gleicher Maßstab) und als Reihe auf eine Standfläche stellen
    teile.sort(key=lambda t: t[2][0])  # von links nach rechts wie im Foto
    stuecke = []
    for base, m, bb in teile:
        layer = foto.convert("RGBA"); layer.putalpha(m)
        stuecke.append(layer.crop(bb))
    gap = int(max(st.width for st in stuecke) * 0.12)
    rw = sum(st.width for st in stuecke) + gap * (len(stuecke) - 1)
    rh = max(st.height for st in stuecke)
    W, H = 1200, 1500
    s_ = min(W * 0.84 / rw, H * 0.70 / rh)
    c = bg(W, H)
    base_y = int(H * 0.86)
    x = (W - rw * s_) / 2
    for st in stuecke:
        st2 = st.resize((max(1, int(st.width * s_)), max(1, int(st.height * s_))), Image.LANCZOS)
        c = shadow(c, int(x), int(x + st2.width), base_y, 14)
        c.alpha_composite(st2, (int(x), base_y - st2.height))
        x += st2.width + gap * s_
    save(c, name)

print("fertig:", sorted(os.listdir(OUT)))
