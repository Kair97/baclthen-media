"""Price Decoded renderer v2 — multi-shot beats (illustrations w/ Ken Burns, Flow clips, motion-graphics data cards),
karaoke subtitles, zoom-punch cuts, SFX, music.   Usage: python3 render_pd2.py pd02   (env LIMIT=n to render first n beats)
Inputs: <ep>/beats.py, <ep>/img/<key>.jpg, <ep>/vid/<key>.mp4, cached TTS in <ep>/out/vo_XX.wav
"""
import sys, os, math, subprocess, json
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
_ns = {"__file__": os.path.join(ROOT, "render.py"), "__name__": "pdbase"}
exec(open(os.path.join(ROOT, "render.py")).read().split("\ndef main")[0], _ns)   # reuse palette, fonts, data cards, music, tts
g = _ns
EPD, OUT = g["EPD"], g["OUT"]
BEATS = g["BEATS"]
if os.environ.get("LIMIT"): BEATS = BEATS[:int(os.environ["LIMIT"])]; g["BEATS"] = BEATS
W, H, SR = g["W"], g["H"], g["SR"]; FPS = 24
BG1, ACC, WHITE = g["BG1"], g["ACC"], g["WHITE"]; font = g["font"]; ease = g["ease"]; BG = g["BG"]
GAP = 0.4

def sfx(kind):
    rng = np.random.default_rng(7)
    if kind == "pop":
        L = int(SR * .12); t = np.arange(L) / SR; f = 900 * np.exp(-t * 18) + 300
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30) * .3
    if kind == "whoosh":
        L = int(SR * .4); n = rng.standard_normal(L); t = np.arange(L) / SR
        a = np.convolve(n, np.ones(6) / 6, "same") - np.convolve(n, np.ones(40) / 40, "same")
        return a * np.sin(np.pi * t / t[-1]) ** 2 * .18
    if kind == "ding":
        L = int(SR * .9); t = np.arange(L) / SR
        return (np.sin(2 * np.pi * 1318 * t) + .5 * np.sin(2 * np.pi * 1975 * t)) * np.exp(-t * 4) * .15
    if kind == "boing":
        L = int(SR * .5); t = np.arange(L) / SR; f = 180 + 160 * np.sin(2 * np.pi * 9 * t) * np.exp(-t * 3)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 4) * .25
    if kind == "scratch":
        L = int(SR * .35); t = np.arange(L) / SR; n = rng.standard_normal(L)
        f = 600 + 1400 * (t / t[-1]); car = np.sin(2 * np.pi * np.cumsum(f) / SR)
        return (car * .5 + n * .25) * np.exp(-((t - .15) / .12) ** 2) * .3
    if kind == "tick":
        L = int(SR * .05); t = np.arange(L) / SR
        return np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 90) * .2
    return np.zeros(1)

# ---------- shots ----------
def ill(key, prog, seed):
    """full-bleed illustration with Ken Burns; 'z' suffix = tighter crop of the same image"""
    z = key.endswith("z") and not os.path.exists(os.path.join(EPD, "img", key + ".jpg"))
    base = key[:-1] if z else key
    fr = g["photo_base"](base + ".jpg", 0.0, prog * (0.6 if z else 1.0), seed)
    if z:
        cw, ch = W / 1.3, H / 1.3; cx = W * (.5 + .12 * math.sin(seed * 1.7)); cy = H * (.5 + .08 * math.cos(seed))
        cx = min(max(cx, cw / 2), W - cw / 2); cy = min(max(cy, ch / 2), H - ch / 2)
        fr = fr.crop((cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)).resize((W, H), Image.BILINEAR)
        d = ImageDraw.Draw(fr); d.rounded_rectangle([60, 52, 76, 68], 3, fill=ACC); d.text((90, 46), "PRICE DECODED", font=font("b", 22), fill=WHITE)
    return fr

class Clip:
    def __init__(self, key, nframes):
        path = os.path.join(EPD, "vid", key + ".mp4")
        src = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).decode())
        need = nframes / FPS; speed = max(.6, src / need) if need > src else 1.0
        self.p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-vf", f"setpts=PTS/{speed},fps={FPS},scale={W}:{H}:flags=lanczos",
                                   "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
        self.last = None
    def next(self):
        buf = self.p.stdout.read(W * H * 3)
        if len(buf) == W * H * 3: self.last = Image.frombytes("RGB", (W, H), buf)
        return self.last.copy() if self.last else BG.copy()
    def close(self):
        try: self.p.kill()
        except Exception: pass

def card(v, t, d, seed):
    if v.get("img"):
        img = g["photo_base"](v["img"] + ".jpg", v.get("dim", .55), min(1, t / max(d, .1)), seed)
    else:
        img = BG.copy()
    dr = ImageDraw.Draw(img)
    g["DRAW"][v["type"]](dr, v, t, d)
    return img

# ---------- karaoke subtitles ----------
SF = font("bl", 58); SFB = font("bl", 64)
_sub_cache = {}
def subs(words, wst, t):
    idx = max([i for i, s in enumerate(wst) if s <= t] or [0])
    c0 = idx // 6 * 6; chunk = words[c0:c0 + 6]
    key = (c0, idx)
    if key in _sub_cache: return _sub_cache[key]
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    ws = [d0.textlength(w, font=SFB if c0 + i == idx else SF) for i, w in enumerate(chunk)]
    total = sum(ws) + 30 * (len(chunk) - 1)
    L = Image.new("RGBA", (W, 160), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    x = (W - total) / 2
    for i, w in enumerate(chunk):
        cur = c0 + i == idx
        d.text((x, 105), w, font=SFB if cur else SF, fill=ACC if cur else WHITE, anchor="ls", stroke_width=9, stroke_fill=(5, 10, 24))
        x += ws[i] + 30
    _sub_cache.clear(); _sub_cache[key] = L
    return L

def main():
    clips = g["tts"]()
    durs = [len(c) / SR + GAP for c in clips]; total = sum(durs) + 1.2; n = int(total * SR)
    voice = np.zeros(n, np.float32); fx = np.zeros(n, np.float32); starts = []; cur = .15
    for i, (c, d) in enumerate(zip(clips, durs)):
        starts.append(cur); i0 = int(cur * SR); voice[i0:i0 + len(c)] += c
        k = BEATS[i].get("sfx") or ("whoosh" if i else None)
        if k:
            s = sfx(k).astype(np.float32); p0 = max(0, i0 - int(.12 * SR)); fx[p0:p0 + len(s)] += s[:n - p0]
        cur += d
    voice /= max(1e-9, np.abs(voice).max()) / .9
    mixa = voice + g["music"](n) * 1.2 + fx; fo = int(1.5 * SR); mixa[-fo:] *= np.linspace(1, 0, fo)
    sf.write(os.path.join(OUT, "mix.wav"), mixa, SR)
    with open(os.path.join(OUT, "subs.srt"), "w") as f:
        for i, (b, s, c) in enumerate(zip(BEATS, starts, clips)):
            f.write(f"{i+1}\n{g['srt_time'](s)} --> {g['srt_time'](s + len(c)/SR)}\n{b['text']}\n\n")
    chaps = [(f"{int(s//60)}:{int(s%60):02d}", b["chapter"]) for b, s in zip(BEATS, starts) if b.get("chapter")]
    if chaps: chaps[0] = ("0:00", chaps[0][1])
    open(os.path.join(OUT, "chapters.txt"), "w").write("\n".join(f"{a} {b}" for a, b in chaps))

    enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-i", os.path.join(OUT, "mix.wav"), "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                            "-g", "96", "-c:a", "aac", "-b:a", "160k", "-shortest", os.path.join(OUT, "master.mp4")], stdin=subprocess.PIPE)
    bounds = starts + [total]; fi = 0
    for bi, b in enumerate(BEATS):
        s, e = (0 if bi == 0 else bounds[bi]), bounds[bi + 1]
        nf = int(round(e * FPS)) - fi
        words = b["text"].split(); speech = len(clips[bi]) / SR; lead = starts[bi] - s
        cl = [len(w) + 2 for w in words]; tot = sum(cl); acc = 0; wst = []
        for c in cl: wst.append(lead + acc / tot * speech); acc += c
        shots = b["shots"]; ns = len(shots)
        # data cards get a bit more time than pictures
        wts = [1.25 if isinstance(x, dict) else 1.0 for x in shots]; cum = np.cumsum([0] + wts) / sum(wts)
        cuts = [int(round(c * nf)) for c in cum]
        clip = None; cur_si = -1
        for k in range(nf):
            si = max(i for i in range(ns) if cuts[i] <= k)
            if si != cur_si:
                if clip: clip.close(); clip = None
                cur_si = si; shot = shots[si]; s0 = cuts[si]; slen = cuts[si + 1] - s0
                if isinstance(shot, str) and shot.startswith("v:"): clip = Clip(shot[2:], slen)
            sk = k - s0; sp = sk / max(1, slen - 1); t = k / FPS
            if isinstance(shot, dict): img = card(shot, sk / FPS, slen / FPS, bi * 7 + si)
            elif shot.startswith("v:"): img = clip.next()
            else: img = ill(shot[2:], sp, bi * 7 + si)
            if sk < 5 and (bi > 0 or si > 0):
                z = 1 + .045 * (1 - sk / 5); cw, chh = W / z, H / z
                img = img.crop(((W - cw) / 2, (H - chh) / 2, (W + cw) / 2, (H + chh) / 2)).resize((W, H), Image.BILINEAR)
            is_card = isinstance(shot, dict)
            if not is_card:
                L = subs(words, wst, t)
                img.paste(L, (0, H - 170), L)
            enc.stdin.write(img.tobytes())
        if clip: clip.close()
        fi += nf
    for _ in range(max(0, int(total * FPS) - fi)): enc.stdin.write(BG.tobytes())
    enc.stdin.close(); enc.wait()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(OUT, "master.mp4"), "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", os.path.join(OUT, "final.mp4")], check=True)
    print("done", round(total, 1))

if __name__ == "__main__":
    main()
