"""Back Then renderer v2 — animated Flow clips + stills with camera moves, karaoke subtitles, sticky captions,
kinetic title cards, SFX, music.  Usage: python3 render_v2.py bt02
Inputs: <ep>/beats.py (BEATS with shots), <ep>/img/<key>.jpg, <ep>/vid/<key>.mp4
"""
import sys, os, math, importlib.util, subprocess, random
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont

EP = sys.argv[1]
ROOT = os.path.dirname(os.path.abspath(__file__))
EPD = os.path.join(ROOT, EP); OUT = os.path.join(EPD, "out"); os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location("beats", os.path.join(EPD, "beats.py"))
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
BEATS = mod.BEATS[:int(os.environ["LIMIT"])] if os.environ.get("LIMIT") else mod.BEATS; VOICE = getattr(mod, "VOICE", "am_puck"); SPEED = getattr(mod, "SPEED", 0.92)
W, H, FPS, SR = 1920, 1080, 24, 24000
GAP = 0.28
CREAM = (244, 236, 216); INK = (24, 24, 24); YEL = (242, 193, 78); RED = (228, 87, 46)
FONT = os.path.join(ROOT, "fonts", "CaveatBrush-Regular.ttf")
def fnt(s): return ImageFont.truetype(FONT, s)

# ---------------- audio ----------------
def tts():
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(ROOT, "kokoro-v1.0.onnx"), os.path.join(ROOT, "voices-v1.0.bin"))
    clips = []
    for i, b in enumerate(BEATS):
        p = os.path.join(OUT, f"vo_{i:02d}.wav")
        if not os.path.exists(p):
            s, sr = k.create(b["text"], voice=VOICE, speed=SPEED, lang="en-us"); sf.write(p, s, sr)
        s, _ = sf.read(p); clips.append(s.astype(np.float32))
    return clips

def music(n):
    out = np.zeros(n, np.float32); bpm = 104; step = 60 / bpm / 2
    scale = [261.63, 293.66, 329.63, 392.0, 440.0, 523.25, 587.33]
    prog = [[0, 2, 4, 6], [1, 3, 5, 2], [0, 2, 4, 5], [3, 1, 4, 2]]
    L = int(SR * .5); tt = np.arange(L) / SR; env = np.exp(-tt * 8)
    t = 0; i = 0; rnd = random.Random(11)
    while t < n / SR:
        bar = int(t / (step * 8)) % 4
        f = scale[prog[bar][i % 4]] * (2 if rnd.random() < .15 else 1)
        s0 = int(t * SR); s1 = min(n, s0 + L)
        tone = (np.sin(2 * np.pi * f * tt) * .6 + np.sin(2 * np.pi * 2 * f * tt) * .25 + np.sign(np.sin(2 * np.pi * f * tt)) * .05) * env
        out[s0:s1] += tone[:s1 - s0] * (.55 if i % 2 else .4)
        if i % 8 == 0:
            bf = scale[prog[bar][0]] / 4; Lb = int(SR * step * 7); tb = np.arange(Lb) / SR
            b = np.sin(2 * np.pi * bf * tb) * np.exp(-tb * 1.5); s1b = min(n, s0 + Lb); out[s0:s1b] += b[:s1b - s0] * .7
        t += step; i += 1
    out /= np.abs(out).max() + 1e-9
    return out * .045

def sfx(kind):
    rng = np.random.default_rng(5)
    if kind == "pop":
        L = int(SR * .12); t = np.arange(L) / SR; f = 900 * np.exp(-t * 18) + 300
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30) * .35
    if kind == "whoosh":
        L = int(SR * .4); n = rng.standard_normal(L); t = np.arange(L) / SR
        a = np.convolve(n, np.ones(6) / 6, "same") - np.convolve(n, np.ones(40) / 40, "same")
        return a * np.sin(np.pi * t / t[-1]) ** 2 * .22
    if kind == "ding":
        L = int(SR * .9); t = np.arange(L) / SR
        return (np.sin(2 * np.pi * 1318 * t) + .5 * np.sin(2 * np.pi * 1975 * t)) * np.exp(-t * 4) * .18
    if kind == "boing":
        L = int(SR * .5); t = np.arange(L) / SR; f = 180 + 160 * np.sin(2 * np.pi * 9 * t) * np.exp(-t * 3)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 4) * .3
    if kind == "scratch":
        L = int(SR * .35); t = np.arange(L) / SR; n = rng.standard_normal(L)
        f = 600 + 1400 * (t / t[-1]); car = np.sin(2 * np.pi * np.cumsum(f) / SR)
        return (car * .5 + n * .25) * np.exp(-((t - .15) / .12) ** 2) * .35
    return np.zeros(1)

# ---------------- visuals ----------------
_img = {}
def load_img(key):
    zoomed = key.endswith("z") and not os.path.exists(os.path.join(EPD, "img", key + ".jpg"))
    base = key[:-1] if zoomed else key
    if base not in _img:
        im = Image.open(os.path.join(EPD, "img", base + ".jpg")).convert("RGB")
        bw, bh = int(W * 1.16), int(H * 1.16); sc = max(bw / im.width, bh / im.height)
        im = im.resize((int(im.width * sc) + 1, int(im.height * sc) + 1), Image.LANCZOS)
        _img.clear(); _img[base] = im.crop(((im.width - bw) // 2, (im.height - bh) // 2, (im.width - bw) // 2 + bw, (im.height - bh) // 2 + bh))
    return _img[base], zoomed

def still_frame(key, prog, frame_i, seed):
    big, zoomed = load_img(key); bw, bh = big.size
    r = random.Random(seed)
    z0, z1 = (1.35, 1.48) if zoomed else (1.0, 1.09)
    if r.random() < .35: z0, z1 = z1, z0       # sometimes pull out
    z = z0 + (z1 - z0) * (prog * prog * (3 - 2 * prog))
    fx, fy = (r.uniform(.3, .7), r.uniform(.3, .6)) if zoomed else (.5 + r.uniform(-.15, .15), .5)
    cw, ch = bw / z, bh / z
    b = (frame_i // 3) % 3; jx, jy = [(0, 0), (1.6, -1.2), (-1.3, 1.4)][b]
    dx = (bw - cw) * fx + jx; dy = (bh - ch) * fy + jy
    return big.crop((dx, dy, dx + cw, dy + ch)).resize((W, H), Image.BILINEAR)

class Clip:
    def __init__(self, key, nframes):
        path = os.path.join(EPD, "vid", key + ".mp4")
        src_dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).decode().strip())
        need = nframes / FPS
        speed = 1.0
        if need > src_dur: speed = max(.6, src_dur / need)   # slow down up to 0.6x, then hold last frame
        self.p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-vf",
                                   f"setpts=PTS/{speed},fps={FPS},scale={W}:{H}:flags=lanczos", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                  stdout=subprocess.PIPE)
        self.last = None
    def next(self):
        buf = self.p.stdout.read(W * H * 3)
        if len(buf) == W * H * 3: self.last = Image.frombytes("RGB", (W, H), buf)
        return self.last.copy() if self.last else Image.new("RGB", (W, H), CREAM)
    def close(self):
        try: self.p.kill()
        except Exception: pass

def title_card(text, t):
    img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img)
    for gx in range(0, W, 80): d.line([(gx, 0), (gx, H)], fill=(233, 223, 199))
    for gy in range(0, H, 80): d.line([(0, gy), (W, gy)], fill=(233, 223, 199))
    import re as _re
    parts = [p.strip() for p in _re.split(r'(?<=[.!?:])\s+|\s+(?==)', text) if p.strip()]
    lines = []
    for part in parts:
        cur = ""
        for w in part.split():
            if len(cur + " " + w) > 18 and cur: lines.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        lines.append(cur)
    size = 200 if len(lines) <= 2 else 150
    f = fnt(size); y = H // 2 - (len(lines) - 1) * size * .55
    for li, line in enumerate(lines):
        a = max(0, min(1, (t - li * .18) / .25)); s = 1 + .25 * (1 - a) * math.cos(a * 6)
        col = YEL if li == len(lines) - 1 else (255, 255, 255)
        tmp = Image.new("RGBA", (W, size + 60), (0, 0, 0, 0)); td = ImageDraw.Draw(tmp)
        td.text((W // 2, (size + 60) // 2), line, font=f, fill=col, anchor="mm", stroke_width=14, stroke_fill=INK)
        if s != 1: tmp = tmp.resize((int(W * s), int((size + 60) * s)), Image.BILINEAR)
        tmp.putalpha(tmp.getchannel("A").point(lambda v: int(v * a)))
        img.paste(tmp, (int(W // 2 - tmp.width // 2), int(y + li * size * 1.08 - tmp.height // 2)), tmp)
    # hand-drawn red squiggle underline that draws itself in
    ly = int(y + (len(lines) - 1) * size * 1.08 + size * .62); lw = min(W - 300, int(f.getlength(lines[-1]) + 80))
    prog = max(0, min(1, (t - len(lines) * .18 - .1) / .35)); x0 = W // 2 - lw // 2
    pts = [(x0 + i * lw / 60, ly + 9 * math.sin(i * .55) + (i % 2) * 2) for i in range(int(61 * prog))]
    if len(pts) > 1: d.line(pts, fill=RED, width=12, joint="curve")
    return img

def sticky(img, text, t, seed):
    if not text or t < .3: return
    a = max(0, min(1, (t - .3) / .3)); c1 = 1.70158
    s = 1 + (c1 + 1) * (a - 1) ** 3 + c1 * (a - 1) ** 2
    f = fnt(80); d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    x0, y0, x1, y1 = d0.textbbox((0, 0), text, font=f); pad = 30
    card = Image.new("RGBA", (x1 - x0 + pad * 2 + 14, y1 - y0 + pad * 2 + 14), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
    d.rounded_rectangle([10, 12, card.width - 1, card.height - 1], 24, fill=(0, 0, 0, 80))
    d.rounded_rectangle([1, 1, card.width - 12, card.height - 13], 24, fill=(255, 251, 236, 255), outline=INK, width=6)
    d.text((pad - x0, pad - y0 - 2), text, font=f, fill=INK)
    card = card.resize((max(1, int(card.width * s)), max(1, int(card.height * s)))).rotate(random.Random(seed).choice([-3, -2, 2, 3]), expand=True)
    img.paste(card, (70, 60), card)

def subs_overlay(words, starts, t):
    """karaoke: chunks of up to 6 words; current word yellow + bigger"""
    idx = max(0, sum(1 for s in starts if s <= t) - 1)
    c0 = (idx // 6) * 6; chunk = words[c0:c0 + 6]
    f = fnt(76); fb = fnt(86)
    layer = Image.new("RGBA", (W, 200), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    widths = [d.textlength(w, font=fb if c0 + i == idx else f) for i, w in enumerate(chunk)]
    total = sum(widths) + 38 * (len(chunk) - 1); x = (W - total) / 2
    for i, w in enumerate(chunk):
        gi = c0 + i; cur = gi == idx
        d.text((x, 110), w, font=fb if cur else f, fill=YEL if cur else (255, 255, 255), anchor="ls", stroke_width=10, stroke_fill=INK)
        x += widths[i] + 38
    return layer, (c0, idx)

def srt_time(x): return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int((x%1)*1000):03d}"

def main():
    clips = tts()
    durs = [len(c) / SR + GAP for c in clips]; total = sum(durs) + 1.0; n = int(total * SR)
    voice = np.zeros(n, np.float32); fx = np.zeros(n, np.float32); starts = []; cur = .1
    for i, (c, d) in enumerate(zip(clips, durs)):
        starts.append(cur); i0 = int(cur * SR); voice[i0:i0 + len(c)] += c
        k = BEATS[i].get("sfx") or ("whoosh" if i else None)
        if k:
            s = sfx(k).astype(np.float32); p0 = max(0, i0 - int(.1 * SR)); fx[p0:p0 + len(s)] += s[:n - p0]
        if BEATS[i].get("cap"):
            s = sfx("pop").astype(np.float32); p0 = i0 + int(.3 * SR); fx[p0:p0 + len(s)] += s[:n - p0]
        cur += d
    voice /= max(1e-9, np.abs(voice).max()) / .9
    mixa = voice + music(n) + fx; fo = int(SR); mixa[-fo:] *= np.linspace(1, 0, fo)
    sf.write(os.path.join(OUT, "mix.wav"), mixa, SR)
    with open(os.path.join(OUT, "subs.srt"), "w") as f:
        for i, (b, s, c) in enumerate(zip(BEATS, starts, clips)):
            f.write(f"{i+1}\n{srt_time(s)} --> {srt_time(s + len(c)/SR)}\n{b['text']}\n\n")
    chaps = [(f"{int(s//60)}:{int(s%60):02d}", b["chapter"]) for b, s in zip(BEATS, starts) if b.get("chapter")]
    if chaps: chaps[0] = ("0:00", chaps[0][1])
    open(os.path.join(OUT, "chapters.txt"), "w").write("\n".join(f"{a} {b}" for a, b in chaps))

    enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-i", os.path.join(OUT, "mix.wav"), "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
                            "-g", "96", "-c:a", "aac", "-b:a", "160k", "-shortest", os.path.join(OUT, "master.mp4")], stdin=subprocess.PIPE)
    bounds = starts + [total]; fi = 0
    for bi, b in enumerate(BEATS):
        s, e = (0 if bi == 0 else bounds[bi]), bounds[bi + 1]; d = e - s
        nf = int(round(e * FPS)) - fi
        words = b["text"].split(); speech = len(clips[bi]) / SR
        lead = starts[bi] - s
        cl = [len(w) + 2 for w in words]; tot = sum(cl); acc = 0; wst = []
        for c in cl: wst.append(lead + acc / tot * speech); acc += c
        shots = b["shots"]; ns = len(shots); per = nf / ns
        sub_cache = None; sub_key = None; clip = None; cur_shot = -1
        for k in range(nf):
            t = k / FPS; si = min(ns - 1, int(k / per))
            if si != cur_shot:
                if clip: clip.close(); clip = None
                cur_shot = si; kind, key = shots[si].split(":", 1); s_start = int(si * per); s_len = int((si + 1) * per) - s_start
                if kind == "v": clip = Clip(key, s_len)
            sk = k - s_start; sp = sk / max(1, s_len - 1)
            if kind == "v": img = clip.next()
            elif kind == "i": img = still_frame(key, sp, k, bi * 10 + si)
            else: img = title_card(key, sk / FPS)
            # zoom punch at shot start
            if sk < 5:
                z = 1 + .05 * (1 - sk / 5); cw, chh = W / z, H / z
                img = img.crop(((W - cw) / 2, (H - chh) / 2, (W + cw) / 2, (H + chh) / 2)).resize((W, H), Image.BILINEAR)
            if si == 0: sticky(img, b.get("cap"), t, bi)
            if kind != "t":
                layer, key2 = subs_overlay(words, wst, t)
                img.paste(layer, (0, H - 230), layer)
            d2 = ImageDraw.Draw(img); d2.text((W - 36, H - 26), "Back Then", font=fnt(36), fill=(30, 30, 30), anchor="rs")
            enc.stdin.write(img.tobytes())
        if clip: clip.close()
        fi += nf
    tail = int(total * FPS) - fi
    blank = Image.new("RGB", (W, H), CREAM).tobytes()
    for _ in range(max(0, tail)): enc.stdin.write(blank)
    enc.stdin.close(); enc.wait()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(OUT, "master.mp4"), "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", os.path.join(OUT, "final.mp4")], check=True)
    print("done", round(total, 1))

if __name__ == "__main__":
    main()
