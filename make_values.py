"""ゴッホ「星月夜」から明度で抽象化した参考画像を作る（白黒版と、青・白・黒版）。

使い方: python3 make_values.py <入力画像> [出力ディレクトリ]
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage

FONT = "/mnt/c/Windows/Fonts/meiryob.ttc"


def to_lightness(rgb: np.ndarray) -> np.ndarray:
    """sRGB → CIE L*（0〜100）。人の目の明るさ感に近い明度。"""
    c = rgb.astype(np.float64) / 255.0
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    y = lin @ np.array([0.2126, 0.7152, 0.0722])
    f = np.where(y > (6 / 29) ** 3, np.cbrt(y), y / (3 * (6 / 29) ** 2) + 4 / 29)
    return 116 * f - 16


def lightness_to_gray(l_star: np.ndarray) -> np.ndarray:
    """L* → sRGB のグレー値（0〜255）。"""
    f = (l_star + 16) / 116
    y = np.where(f > 6 / 29, f**3, 3 * (6 / 29) ** 2 * (f - 4 / 29))
    c = np.where(y <= 0.0031308, 12.92 * y, 1.055 * np.power(np.clip(y, 0, None), 1 / 2.4) - 0.055)
    return np.clip(c * 255 + 0.5, 0, 255).astype(np.uint8)


def stretch(l_star: np.ndarray, lo_pct=0.5, hi_pct=99.5) -> np.ndarray:
    lo, hi = np.percentile(l_star, [lo_pct, hi_pct])
    return np.clip((l_star - lo) / (hi - lo) * 100, 0, 100)


def quantize(l_star: np.ndarray, levels: int, smooth: int, clean: int) -> np.ndarray:
    """平滑化 → 等間隔の明度段階に量子化 → 小さな斑点を除去。戻り値は段階番号（0=最も明るい）。"""
    s = ndimage.median_filter(l_star, size=smooth)
    s = ndimage.gaussian_filter(s, sigma=smooth / 4)
    edges = np.linspace(0, 100, levels + 1)[1:-1]
    idx = (levels - 1) - np.digitize(s, edges)  # 0=明るい
    img = Image.fromarray(idx.astype(np.uint8))
    for _ in range(2):
        img = img.filter(ImageFilter.ModeFilter(clean))
    return np.asarray(img)


def level_tones(levels: int) -> np.ndarray:
    """段階ごとの表示グレー。白(L*=97)〜黒(L*=12)を明度で等分。"""
    return lightness_to_gray(np.linspace(97, 12, levels))


def gray_palette(levels: int) -> np.ndarray:
    return np.repeat(level_tones(levels)[:, None], 3, axis=1)


def gray_labels(levels: int) -> list[str]:
    return ["1 白"] + [str(i) for i in range(2, levels)] + [f"{levels} 黒"]


def lab_to_rgb(lab) -> np.ndarray:
    """CIE L*a*b*（D65）→ sRGB（0〜255）。"""
    lab = np.asarray(lab, dtype=np.float64)
    fy = (lab[..., 0] + 16) / 116
    f = np.stack([fy + lab[..., 1] / 500, fy, fy - lab[..., 2] / 200], axis=-1)
    xyz = np.where(f > 6 / 29, f**3, 3 * (6 / 29) ** 2 * (f - 4 / 29)) * [0.95047, 1.0, 1.08883]
    lin = xyz @ np.array([[3.2406, -1.5372, -0.4986], [-0.9689, 1.8758, 0.0415], [0.0557, -0.2040, 1.0570]]).T
    lin = np.clip(lin, 0, 1)
    c = np.where(lin <= 0.0031308, 12.92 * lin, 1.055 * lin ** (1 / 2.4) - 0.055)
    return np.clip(c * 255 + 0.5, 0, 255).astype(np.uint8)


# 青・白・黒の5段階。明度は白黒版と同じ（L*=97, 76, 55, 33, 12）で、2〜4に青みを付ける。
# 4はウルトラマリン等のチューブの青（乾くとかなり暗い）を想定した色。
BLUE_PALETTE = lab_to_rgb([(97, 0, -1), (76, -2, -24), (55, 8, -48), (33, 22, -60), (12, 0, -2)])
BLUE_LABELS = ["1 白", "2 明るい青", "3 中間の青", "4 青", "5 黒"]


def render(idx: np.ndarray, palette: np.ndarray) -> Image.Image:
    return Image.fromarray(palette[idx], "RGB")


def legend_strip(palette: np.ndarray, labels: list[str], width: int, font) -> Image.Image:
    h = 70
    strip = Image.new("RGB", (width, h), "white")
    d = ImageDraw.Draw(strip)
    w = width / len(palette)
    for i, (color, label) in enumerate(zip(palette, labels)):
        x0, x1 = int(i * w), int((i + 1) * w)
        d.rectangle([x0, 0, x1, h - 1], fill=tuple(int(v) for v in color), outline="black")
        light = to_lightness(color[None, :])[0] > 55
        d.text(((x0 + x1) / 2, h / 2), label, fill="black" if light else "white", font=font, anchor="mm")
    return strip


def with_legend(img: Image.Image, palette: np.ndarray, labels: list[str], title: str) -> Image.Image:
    font = ImageFont.truetype(FONT, 26)
    pad = 16
    strip = legend_strip(palette, labels, img.width, font)
    out = Image.new("RGB", (img.width + pad * 2, img.height + strip.height + 70 + pad * 2), "white")
    d = ImageDraw.Draw(out)
    d.text((pad, pad + 4), title, fill="black", font=font)
    out.paste(img, (pad, pad + 50))
    out.paste(strip, (pad, pad + 50 + img.height + 10))
    return out


def contact_sheet(items, cols=2, scale=0.5) -> Image.Image:
    font = ImageFont.truetype(FONT, 22)
    thumbs = [(t, im.convert("RGB").resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)) for t, im in items]
    tw, th = thumbs[0][1].size
    pad, cap = 14, 36
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + cap + pad) + pad), "white")
    d = ImageDraw.Draw(sheet)
    for i, (title, im) in enumerate(thumbs):
        x = pad + (i % cols) * (tw + pad)
        y = pad + (i // cols) * (th + cap + pad)
        d.text((x, y + 4), title, fill="black", font=font)
        sheet.paste(im, (x, y + cap))
    return sheet


def main():
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent / "output"
    out.mkdir(parents=True, exist_ok=True)

    rgb = np.asarray(Image.open(src).convert("RGB"))
    l_star = stretch(to_lightness(rgb))

    gray = Image.fromarray(lightness_to_gray(l_star), "L")
    gray.save(out / "01_grayscale.png")

    results = [("グレースケール（全ディテール）", gray)]
    for name, levels, smooth, clean in [
        ("02_value7", 7, 5, 5),
        ("03_value5", 5, 7, 7),
        ("04_value3", 3, 9, 9),
        ("05_notan2", 2, 21, 11),
    ]:
        idx = quantize(l_star, levels, smooth, clean)
        img = render(idx, gray_palette(levels))
        img.save(out / f"{name}.png")
        title = f"{levels}段階の明度" if levels > 2 else "2値（ノタン：明暗の大きな形）"
        with_legend(img, gray_palette(levels), gray_labels(levels), title).save(out / f"{name}_legend.png")
        results.append((title, img))
        if levels == 5:
            blue = render(idx, BLUE_PALETTE)
            blue.save(out / "03_value5_blue.png")
            with_legend(blue, BLUE_PALETTE, BLUE_LABELS, "5段階の明度（青・白・黒）").save(out / "03_value5_blue_legend.png")

    contact_sheet(results).save(out / "00_overview.png")
    print("written:", *sorted(p.name for p in out.iterdir()), sep="\n  ")


if __name__ == "__main__":
    main()
