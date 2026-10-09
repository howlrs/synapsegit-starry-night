"""制作写真を明度5段階に直し、計画の見本と並べて比べる（添削用）。
使い方: python3 valuecheck.py <project_dir> <out_dir>
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
proj, out = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(proj))
import make_values as mv

W, H = 1500, 991  # キャンバス 118x78cm 相当（約1.51:1）
# 1400px幅プレビュー座標での四隅（左上・右上・右下・左下）。辺のはみ出しを避けるため少し内側
QUADS = {
    "20261009_step1_before.jpg": [(60, 100), (1340, 98), (1342, 943), (57, 945)],
    "20261009_step1_after.jpg": [(24, 86), (1362, 48), (1379, 956), (21, 972)],
    "20261009_step2-3_after.jpg": [(28, 68), (1368, 44), (1382, 954), (21, 972)],
}

def rectify(path, quad):
    im = Image.open(path)
    k = im.width / 1400
    q = [(x * k, y * k) for x, y in quad]
    data = [c for pt in (q[0], q[3], q[2], q[1]) for c in pt]  # PIL QUAD: 左上, 左下, 右下, 右上
    return im.transform((W, H), Image.QUAD, data, Image.BICUBIC)

def levels(img):
    l = mv.stretch(mv.to_lightness(np.asarray(img.convert("RGB"))))
    return mv.quantize(l, 5, 7, 7)

def frac(idx):
    return [round(float((idx == i).mean()) * 100, 1) for i in range(5)]

font = ImageFont.truetype(mv.FONT, 28)
small = ImageFont.truetype(mv.FONT, 22)
panels = []
plan = np.asarray(Image.open(proj / "output/03_value5.png").convert("L"))
tones = mv.level_tones(5)
plan_idx = np.abs(plan[..., None].astype(int) - tones[None, None, :].astype(int)).argmin(-1)
print("plan", frac(plan_idx))
panels.append(("計画の見本（明度5段階）", mv.render(plan_idx, mv.BLUE_PALETTE).resize((W, int(W * plan.shape[0] / plan.shape[1]))), frac(plan_idx)))
for name, title in [("20261009_step1_after.jpg", "工程1 白の後（4.jpg）"), ("20261009_step2-3_after.jpg", "現在（5.jpg）")]:
    rect = rectify(proj / "photos/registered" / name, QUADS[name])
    rect.save(out / f"rect_{name}")
    idx = levels(rect)
    sky = idx[: int(H * 0.62)]
    print(name, "all", frac(idx), "sky(上62%)", frac(sky))
    panels.append((title + " を5段階に変換", mv.render(idx, mv.BLUE_PALETTE), frac(idx)))
    if name.startswith("20261009_step2-3"):
        gray = Image.fromarray(mv.lightness_to_gray(mv.stretch(mv.to_lightness(np.asarray(rect.convert("RGB"))))), "L").convert("RGB")
        panels.append(("現在（5.jpg）のグレースケール", gray, None))

# 2列の比較シート
tw = 700
pad, cap, foot = 16, 44, 40
rows = []
for title, im, fr in panels:
    th = int(im.height * tw / im.width)
    rows.append((title, im.resize((tw, th), Image.LANCZOS), fr))
cell_h = max(r[1].height for r in rows) + cap + foot
sheet = Image.new("RGB", (pad + 2 * (tw + pad), pad + 2 * (cell_h + pad)), "white")
d = ImageDraw.Draw(sheet)
labels = ["1白", "2", "3", "4", "5黒"]
for i, (title, im, fr) in enumerate(rows):
    x = pad + (i % 2) * (tw + pad)
    y = pad + (i // 2) * (cell_h + pad)
    d.text((x, y + 6), title, fill="black", font=font)
    sheet.paste(im, (x, y + cap))
    if fr:
        txt = "面積  " + "  ".join(f"{l}:{v:.0f}%" for l, v in zip(labels, fr))
        d.text((x, y + cap + im.height + 8), txt, fill="black", font=small)
sheet.save(out / "valuecheck_20261009.png")
print("saved", out / "valuecheck_20261009.png", sheet.size)
