"""5段階明度を「白 → 2 → 3 → 4 → 黒」と明るい順に塗る工程ごとの地図画像を作る。
配色は白黒（gray）と青・白・黒（blue）から選ぶ。

各工程の画像: 塗り終わった所はその段階のグレー、まだ塗っていない所は薄くした原画、
今回塗る所は赤い輪郭で囲む。

使い方: python3 make_steps.py <入力画像> [gray|blue]
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

import make_values as mv

# (ファイル名, 見出し, 段階番号 0=白〜4=黒)
STEPS = {
    "gray": [
        ("step1_white", "工程1  白（1）… チューブの白", 0),
        ("step2_gray2", "工程2  グレー2 … 白に黒をほんの少し", 1),
        ("step3_gray3", "工程3  グレー3 … さらに黒を足す", 2),
        ("step4_gray4", "工程4  グレー4 … さらに黒を足す", 3),
        ("step5_black", "工程5  黒（5）… チューブの黒", 4),
    ],
    "blue": [
        ("step1_white", "工程1  白（1）… チューブの白", 0),
        ("step2_lightblue", "工程2  明るい青（2）… 白に青を少し", 1),
        ("step3_midblue", "工程3  中間の青（3）… さらに青を足す", 2),
        ("step4_blue", "工程4  青（4）… チューブの青", 3),
        ("step5_black", "工程5  黒（5）… チューブの黒", 4),
    ],
}
PALETTES = {"gray": mv.gray_palette(5), "blue": mv.BLUE_PALETTE}
OUT_DIRS = {"gray": "steps", "blue": "steps_blue"}
OUTLINE = np.array([220, 40, 30], dtype=np.uint8)


def faded(rgb: np.ndarray) -> np.ndarray:
    """未着手の部分: 彩度を落として白に寄せ、塗った部分と区別できるようにする。"""
    gray = rgb.mean(axis=2, keepdims=True)
    soft = rgb * 0.4 + gray * 0.6
    return (soft * 0.45 + 255 * 0.55).astype(np.uint8)


def outline(mask: np.ndarray) -> np.ndarray:
    edge = mask & ~ndimage.binary_erosion(mask)
    return ndimage.binary_dilation(edge, iterations=1)


def step_image(rgb, idx, palette, done, target) -> Image.Image:
    painted = np.isin(idx, done + [target])
    out = faded(rgb)
    out[painted] = palette[idx[painted]]
    out[outline(idx == target)] = OUTLINE
    return Image.fromarray(out, "RGB")


def titled(img: Image.Image, title: str, font) -> Image.Image:
    pad, cap = 16, 54
    out = Image.new("RGB", (img.width + pad * 2, img.height + cap + pad), "white")
    ImageDraw.Draw(out).text((pad, pad), title, fill="black", font=font)
    out.paste(img, (pad, cap))
    return out


def main():
    src = Path(sys.argv[1])
    kind = sys.argv[2] if len(sys.argv) > 2 else "gray"
    palette = PALETTES[kind]
    out = Path(__file__).parent / "output" / OUT_DIRS[kind]
    out.mkdir(parents=True, exist_ok=True)

    rgb = np.asarray(Image.open(src).convert("RGB"))
    idx = mv.quantize(mv.stretch(mv.to_lightness(rgb)), 5, 7, 7)  # 03_value5 と同じ設定
    font = ImageFont.truetype(mv.FONT, 28)

    frames, done = [], []
    for name, title, target in STEPS[kind]:
        share = (idx == target).mean() * 100
        img = step_image(rgb, idx, palette, done, target)
        titled(img, f"{title}（面積 約{share:.0f}%）", font).save(out / f"{name}.png")
        frames.append((title.split("…")[0].strip(), img))
        done.append(target)
    frames.append(("完成（5段階）", mv.render(idx, palette)))

    sheet_font = ImageFont.truetype(mv.FONT, 22)
    scale, cols, pad, cap = 0.5, 2, 14, 36
    tw, th = int(rgb.shape[1] * scale), int(rgb.shape[0] * scale)
    rows = (len(frames) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + cap + pad) + pad), "white")
    d = ImageDraw.Draw(sheet)
    for i, (title, im) in enumerate(frames):
        x, y = pad + (i % cols) * (tw + pad), pad + (i // cols) * (th + cap + pad)
        d.text((x, y + 4), title, fill="black", font=sheet_font)
        sheet.paste(im.resize((tw, th), Image.LANCZOS), (x, y + cap))
    sheet.save(out / "00_steps_overview.png")
    print("written:", *sorted(p.name for p in out.iterdir()), sep="\n  ")


if __name__ == "__main__":
    main()
