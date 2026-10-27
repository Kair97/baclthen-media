"""Price Decoded motion-graphics renderer.
Usage: python3 render.py ep01
Produces ep01/out/video.mp4, ep01/out/subs.srt, ep01/out/chapters.txt
"""
import sys, os, math, importlib.util, subprocess, json
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter

EP = sys.argv[1]
ROOT = os.path.dirname(os.path.abspath(__file__))
EPD = os.path.join(ROOT, EP)
OUT = os.path.join(EPD, "out"); os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location("beats", os.path.join(EPD, "beats.py"))
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
BEATS = mod.BEATS
VOICE = getattr(mod, "VOICE", "am_michael")
SPEED = getattr(mod, "SPEED", 1.0)

W, H, FPS, SR = 1920, 1080, 30, 24000
GAP = 0.45
# palette
BG1 = (9, 20, 46); BG2 = (14, 33, 72)
ACC = (198, 244, 50); NEG = (255, 96, 96)
WHITE = (244, 247, 252); MUTED = (143, 163, 199); FAINT = (40, 62, 104)
F = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(F + {"bl":"InterDisplay-Black.otf","b":"InterDisplay-Bold.otf","sb":"Inter-SemiBold.otf","m":"Inter-Medium.otf","r":"Inter-Regular.otf"}[w], s)

def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def mix(c1, c2, a): return tuple(int(c1[i] + (c2[i] - c1[i]) * a) for i in range(3))

# ---------- background ----------
def make_bg():
    y = np.linspace(0, 1, H)[:, None]; x = np.linspace(0, 1, W)[None, :]
    g = np.clip(0.6 * y + 0.4 * (1 - x), 0, 1)[..., None]
    arr = (np.array(BG1) * g + np.array(BG2) * (1 - g))
    # vignette
    d = np.sqrt((x - .5) ** 2 + (y - .5) ** 2)[..., None]
    arr = arr * (1 - 0.35 * np.clip(d * 1.4, 0, 1))
    img = Image.fromarray(arr.astype(np.uint8))
    dr = ImageDraw.Draw(img)
    for gx in range(0, W, 96): dr.line([(gx, 0), (gx, H)], fill=(18, 36, 72), width=1)
    for gy in range(0, H, 96): dr.line([(0, gy), (W, gy)], fill=(18, 36, 72), width=1)
    # brand mark
    dr.rounded_rectangle([60, 52, 76, 68], 3, fill=ACC)
    dr.text((90, 46), "PRICE DECODED", font=font("b", 22), fill=WHITE)
    return img
BG = make_bg()

_PHOTO = {}
def photo_base(name, dim, prog, seed):
    key = (name, dim)
    if key not in _PHOTO:
        im = Image.open(os.path.join(EPD, "img", name)).convert("RGB")
        bw, bh = int(W * 1.12), int(H * 1.12)
        sc = max(bw / im.width, bh / im.height)
        im = im.resize((int(im.width * sc) + 1, int(im.height * sc) + 1), Image.LANCZOS)
        im = im.crop(((im.width - bw) // 2, (im.height - bh) // 2, (im.width - bw) // 2 + bw, (im.height - bh) // 2 + bh))
        arr = np.asarray(im).astype(np.float32)
        y = np.linspace(-1, 1, bh)[:, None]; x = np.linspace(-1, 1, bw)[None, :]
        vig = (1 - 0.35 * np.clip((x ** 2 + y ** 2) / 2, 0, 1)) * (1 - 0.38 * np.exp(-(y / 0.32) ** 2))
        arr = arr * (1 - dim) * vig[..., None] + np.array(BG1, np.float32) * dim
        _PHOTO[key] = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    big = _PHOTO[key]; bw, bh = big.size
    z = 1.0 + 0.10 * prog  # slow push-in
    cw, ch = bw / z, bh / z
    dx = (bw - cw) * (0.5 + 0.25 * math.sin(seed)); dy = (bh - ch) * (0.5 + 0.2 * math.cos(seed))
    fr = big.crop((dx, dy, dx + cw, dy + ch)).resize((W, H), Image.BILINEAR)
    dr = ImageDraw.Draw(fr)
    dr.rounded_rectangle([60, 52, 76, 68], 3, fill=ACC)
    dr.text((90, 46), "PRICE DECODED", font=font("b", 22), fill=WHITE)
    return fr

def text_c(dr, xy, s, f, fill, anchor="mm", spacing=14):
    dr.multiline_text(xy, s, font=f, fill=fill, anchor=anchor, align="center", spacing=spacing)

def src_line(dr, s, a):
    if s: dr.text((W - 60, H - 50), "Source: " + s, font=font("r", 22), fill=mix(BG1, MUTED, a), anchor="rs")

def fmt_num(v, unit, ref=None):
    ref = v if ref is None else ref
    dec = 0 if float(ref).is_integer() else 1
    if unit == "$B": return f"${v:.1f}B"
    if unit == "%": return f"{v:.{dec}f}%"
    return f"{v:.{dec}f}"

# ---------- visuals: each returns (frame, is_static_after) ----------
def v_title(dr, v, t, d):
    a = ease(t / .8)
    dr.text((W // 2, 430 + 30 * (1 - a)), v["sub"].upper(), font=font("sb", 34), fill=mix(BG1, ACC, a), anchor="mm")
    text_c(dr, (W // 2, 560 + 40 * (1 - a)), v["title"], font("bl", 150), mix(BG1, WHITE, a))
    w = int(520 * ease((t - .3) / .8)); dr.rectangle([W // 2 - w // 2, 660, W // 2 + w // 2, 668], fill=ACC)
    return t > 1.2

def v_chapter(dr, v, t, d):
    a = ease(t / .7)
    dr.text((W // 2, 420), "CHAPTER " + v["n"], font=font("sb", 36), fill=mix(BG1, ACC, a), anchor="mm")
    text_c(dr, (W // 2, 540 + 30 * (1 - a)), v["title"], font("bl", 110), mix(BG1, WHITE, a))
    return t > 1.0

def v_quote(dr, v, t, d):
    a = ease(t / .8)
    dr.text((W // 2, 360), v["kicker"], font=font("sb", 32), fill=mix(BG1, ACC, a), anchor="mm")
    text_c(dr, (W // 2, 560 + 30 * (1 - a)), v["line"], font("b", 92), mix(BG1, WHITE, a), spacing=24)
    src_line(dr, v.get("src"), a)
    return t > 1.1

def v_bigstat(dr, v, t, d):
    a = ease(t / 1.4); col = NEG if v.get("neg") or v["value"] < 0 else ACC
    val = v["value"] * a
    dr.text((W // 2, 500), v["fmt"].format(val), font=font("bl", 300), fill=mix(BG1, col, ease(t / .4)), anchor="mm")
    dr.text((W // 2, 720), v["label"], font=font("m", 46), fill=mix(BG1, WHITE, ease((t - .3) / .6)), anchor="mm")
    src_line(dr, v.get("src"), ease(t / .6))
    return t > 1.5

def v_compare(dr, v, t, d):
    for i, (val, lab) in enumerate([v["left"], v["right"]]):
        a = ease((t - i * .5) / .7); cx = W // 2 + (-430 if i == 0 else 430)
        col = NEG if val.startswith("-") else ACC
        dr.text((cx, 500 + 30 * (1 - a)), val, font=font("bl", 200), fill=mix(BG1, col, a), anchor="mm")
        dr.text((cx, 680), lab, font=font("m", 44), fill=mix(BG1, WHITE, a), anchor="mm")
    dr.line([(W // 2, 380), (W // 2, 720)], fill=FAINT, width=3)
    src_line(dr, v.get("src"), ease(t / .6))
    return t > 1.4

def v_bars(dr, v, t, d):
    items = v["items"]; n = len(items); mx = max(x[1] for x in items)
    dr.text((140, 200), v["title"], font=font("b", 64), fill=mix(BG1, WHITE, ease(t / .5)), anchor="ls")
    top, bot = 300, 900; slot = (bot - top) / n; bh = min(130, slot * .6)
    lab_f = font("m", 42); val_f = font("bl", 64)
    for i, (lab, val) in enumerate(items):
        a = ease((t - .2 - i * .35) / 1.0)
        y = top + slot * i + (slot - bh) / 2
        dr.text((140, y - 14), lab, font=lab_f, fill=mix(BG1, MUTED, a), anchor="ls")
        x1 = 140 + (1500 * val / mx) * a
        col = ACC if i == n - 1 else (110, 140, 190)
        dr.rounded_rectangle([140, y, max(150, x1), y + bh], 10, fill=mix(BG1, col, min(1, a * 2)))
        dr.text((x1 + 24, y + bh / 2), fmt_num(val * a if a < 1 else val, v["unit"], val), font=val_f, fill=mix(BG1, WHITE, a), anchor="lm")
    src_line(dr, v.get("src"), ease(t / .6))
    return t > .2 + n * .35 + 1.1

def v_readings(dr, v, t, d):
    items = list(v["items"]); lead = v.get("lead")
    if lead: items = [lead] + items
    n = len(items); mx = max(abs(x[1]) for x in items)
    dr.text((140, 200), v["title"], font=font("b", 60), fill=mix(BG1, WHITE, ease(t / .5)), anchor="ls")
    zero = 600; scale = 300 / mx; left, right = 160, W - 160; slot = (right - left) / n; bw = slot * .56
    dr.line([(left - 20, zero), (right + 20, zero)], fill=FAINT, width=3)
    for i, (lab, val) in enumerate(items):
        a = ease((t - .2 - i * .18) / .8)
        cx = left + slot * i + slot / 2; h = val * scale * a
        col = NEG if val < 0 else ACC
        y0, y1 = sorted([zero, zero - h])
        dr.rounded_rectangle([cx - bw / 2, y0, cx + bw / 2, max(y0 + 2, y1)], 8, fill=mix(BG1, col, min(1, a * 2)))
        ty = zero - h - 36 if val >= 0 else zero - h + 36
        dr.text((cx, ty), f"{val:+.1f}%", font=font("b", 40), fill=mix(BG1, WHITE, a), anchor="mm")
        dr.text((cx, 900), lab, font=font("m", 34), fill=mix(BG1, MUTED, a), anchor="mm")
    src_line(dr, v.get("src"), ease(t / .6))
    return t > .2 + n * .18 + 1.0

def v_bullets(dr, v, t, d):
    items = v["items"]; n = len(items)
    dr.text((W // 2, 230), v["title"], font=font("b", 64), fill=mix(BG1, WHITE, ease(t / .5)), anchor="mm")
    step = max(.35, min(1.2, (d * .6) / n)); top = 360; gap = min(120, 560 / n)
    for i, s in enumerate(items):
        a = ease((t - .4 - i * step) / .5); y = top + i * gap
        x = 620 + 40 * (1 - a)
        dr.rounded_rectangle([x, y - 14, x + 28, y + 14], 6, fill=mix(BG1, ACC, a))
        dr.text((x + 60, y), s, font=font("sb", 54), fill=mix(BG1, WHITE, a), anchor="lm")
    return t > .4 + n * step + .6

def v_flow(dr, v, t, d):
    st = v["steps"]; n = len(st); step = max(.4, min(1.4, d * .6 / n))
    bw, bh = 380, 170; gap = (W - 160 - n * bw) / (n - 1)
    for i, s in enumerate(st):
        a = ease((t - .2 - i * step) / .5); x = 80 + i * (bw + gap); y = H // 2 - bh // 2
        dr.rounded_rectangle([x, y, x + bw, y + bh], 22, outline=mix(BG1, ACC if i == n - 1 else MUTED, a), width=4, fill=mix(BG1, (16, 38, 80), a))
        text_c(dr, (x + bw / 2, y + bh / 2), s.replace(" ", "\n", 1) if len(s) > 14 else s, font("sb", 40), mix(BG1, WHITE, a), spacing=8)
        if i < n - 1:
            aa = ease((t - .2 - i * step - .3) / .4); ax = x + bw + 10
            dr.line([(ax, H // 2), (ax + (gap - 20) * aa, H // 2)], fill=ACC, width=5)
    dr.text((W // 2, 300), "Why premiums lag behind costs", font=font("b", 56), fill=mix(BG1, WHITE, ease(t / .5)), anchor="mm")
    return t > .2 + n * step + .8

def v_step(dr, v, t, d):
    a = ease(t / .7)
    r = 120; cx, cy = W // 2, 400
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(BG1, ACC, a))
    dr.text((cx, cy), v["n"], font=font("bl", 150), fill=BG1, anchor="mm")
    dr.text((W // 2, 650 + 30 * (1 - a)), v["title"], font=font("bl", 96), fill=mix(BG1, WHITE, a), anchor="mm")
    dr.text((W // 2, 760), v["sub"], font=font("m", 46), fill=mix(BG1, MUTED, ease((t - .3) / .6)), anchor="mm")
    return t > 1.1

def v_endcard(dr, v, t, d):
    a = ease(t / .8)
    dr.rounded_rectangle([W // 2 - 60, 260, W // 2 + 60, 380], 24, fill=mix(BG1, ACC, a))
    text_c(dr, (W // 2, 500), v["title"], font("bl", 130), mix(BG1, WHITE, a))
    dr.text((W // 2, 640), v["next"], font=font("sb", 52), fill=mix(BG1, ACC, ease((t - .4) / .6)), anchor="mm")
    dr.text((W // 2, 960), "For education only. Not financial advice.", font=font("r", 28), fill=mix(BG1, MUTED, a), anchor="mm")
    return t > 1.3

DRAW = dict(title=v_title, chapter=v_chapter, quote=v_quote, bigstat=v_bigstat, compare=v_compare, bars=v_bars,
            readings=v_readings, bullets=v_bullets, flow=v_flow, step=v_step, endcard=v_endcard)

# ---------- TTS ----------
def tts():
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(ROOT, "kokoro-v1.0.onnx"), os.path.join(ROOT, "voices-v1.0.bin"))
    clips = []
    for i, b in enumerate(BEATS):
        p = os.path.join(OUT, f"vo_{i:02d}.wav")
        if not os.path.exists(p):
            s, sr = k.create(b["text"], voice=VOICE, speed=SPEED, lang="en-us")
            sf.write(p, s, sr)
        s, sr = sf.read(p); assert sr == SR
        clips.append(s.astype(np.float32))
    return clips

def music(n):
    t = np.arange(n) / SR; out = np.zeros(n, np.float32)
    chords = [[110, 164.81, 220, 277.18], [98, 146.83, 196, 246.94], [87.31, 130.81, 174.61, 220], [98, 146.83, 196, 293.66]]
    seg = 8.0
    for ci in range(int(len(t) / SR / seg) + 1):
        f = chords[ci % 4]; s0 = int(ci * seg * SR); s1 = min(n, int((ci + 1) * seg * SR + 2 * SR))
        if s0 >= n: break
        tt = t[s0:s1] - t[s0]; env = np.minimum(1, tt / 2.0) * np.minimum(1, np.maximum(0, (seg + 2 - tt) / 2.0))
        for fr in f:
            out[s0:s1] += (np.sin(2 * np.pi * fr * tt) * .5 + np.sin(2 * np.pi * fr * 2.003 * tt) * .15) * env
    out /= np.abs(out).max() + 1e-9
    return out * 0.045

def srt_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}"

def main():
    clips = tts()
    durs = [len(c) / SR + GAP for c in clips]; durs[0] += .3
    total = sum(durs) + 1.0
    n = int(total * SR); voice = np.zeros(n, np.float32)
    starts = []; cur = .3
    for c, d in zip(clips, durs):
        starts.append(cur); i0 = int(cur * SR); voice[i0:i0 + len(c)] += c; cur += d
    voice /= max(1e-9, np.abs(voice).max()) / .89
    mixa = voice + music(n)
    fade = int(SR * 1.5); mixa[-fade:] *= np.linspace(1, 0, fade)
    sf.write(os.path.join(OUT, "mix.wav"), mixa, SR)
    # subtitles & chapters
    with open(os.path.join(OUT, "subs.srt"), "w") as f:
        for i, (b, s, c) in enumerate(zip(BEATS, starts, clips)):
            f.write(f"{i+1}\n{srt_time(s)} --> {srt_time(s + len(c)/SR)}\n{b['text']}\n\n")
    chaps = [("0:00", "The paradox")]
    for b, s in zip(BEATS, starts):
        if b["v"]["type"] == "chapter":
            chaps.append((f"{int(s//60)}:{int(s%60):02d}", b["v"]["title"]))
    with open(os.path.join(OUT, "chapters.txt"), "w") as f:
        f.write("\n".join(f"{a} {b}" for a, b in chaps))
    json.dump(dict(total=total, starts=starts), open(os.path.join(OUT, "timing.json"), "w"))
    # video
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", os.path.join(OUT, "mix.wav"), "-c:v", "libx264", "-preset", "medium", "-tune", "animation", "-crf", "22",
           "-maxrate", "1100k", "-bufsize", "2200k", "-pix_fmt", "yuv420p", "-g", "120",
           "-c:a", "aac", "-b:a", "96k", "-shortest", "-movflags", "+faststart", os.path.join(OUT, "video.mp4")]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    blank = BG.tobytes()
    frames_total = int(total * FPS); fi = 0
    bounds = starts + [total]
    for bi, b in enumerate(BEATS):
        s, e = (0 if bi == 0 else bounds[bi]), bounds[bi + 1]
        d = e - s; nf = int(round(e * FPS)) - fi
        static = None
        for k in range(nf):
            t = k / FPS
            if static is not None and t < d - .25:
                p.stdin.write(static); continue
            if b["v"].get("img"):
                img = photo_base(b["v"]["img"], b["v"].get("dim", .55), t / d, bi)
                fi_in = min(1, t / .35)
                if fi_in < 1: img = Image.blend(BG, img, fi_in)
            else:
                img = BG.copy()
            dr = ImageDraw.Draw(img)
            done = DRAW[b["v"]["type"]](dr, b["v"], t, d)
            if b["v"].get("img"): done = False
            # fade out last .25s
            fo = (d - t) / .25
            if fo < 1: img = Image.blend(BG, img, max(0, fo))
            fr = img.tobytes()
            if done and fo >= 1: static = fr
            p.stdin.write(fr)
        fi += nf
    while fi < frames_total: p.stdin.write(blank); fi += 1
    p.stdin.close(); p.wait()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(OUT, "video.mp4"), "-c:v", "copy",
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", os.path.join(OUT, "final.mp4")], check=True)
    print("done", total, "sec")

if __name__ == "__main__":
    main()
