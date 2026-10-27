"""Cut vertical 1080x1920 Shorts/Reels/TikToks out of a finished 16:9 episode.
Usage: python3 make_shorts.py <episode_dir> <shorts.json>
shorts.json: [{"name":"short1_x","start":215.3,"dur":24.8,"top1":"ROMANS PUT THIS","top2":"ON EVERYTHING",
               "cta":"Full episode on Back Then","style":"backthen"|"pricedecoded"}]
Output: <episode_dir>/shorts/<name>.mp4  (keep each 20-58 s; start/dur from out/subs.srt beat timings)
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts") + "/"
INTER = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"

def overlay(path, s):
    W, H = 1080, 1920; im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    pd = s.get("style") == "pricedecoded"
    big = INTER if pd and os.path.exists(INTER) else F + "PermanentMarker-Regular.ttf"
    f1, f2 = ImageFont.truetype(big, 92), ImageFont.truetype(big, 112)
    box, ink, acc = ((9, 20, 46, 240), (244, 247, 252), (198, 244, 50)) if pd else ((255, 251, 236, 235), (20, 20, 20), (228, 87, 46))
    d.rounded_rectangle([50, 250, 1030, 560], 40, fill=box, outline=(20, 20, 20), width=8)
    d.text((540, 345), s["top1"], font=f1, fill=ink, anchor="mm")
    d.text((540, 470), s["top2"], font=f2, fill=acc, anchor="mm", stroke_width=4, stroke_fill=(20, 20, 20))
    f3 = ImageFont.truetype(F + "CaveatBrush-Regular.ttf", 66)
    d.rounded_rectangle([140, 1420, 940, 1530], 30, fill=(20, 20, 20, 255))
    d.text((515, 1475), s.get("cta", "Full episode on YouTube"), font=f3, fill=(242, 193, 78), anchor="mm")
    d.polygon([(880, 1450), (880, 1500), (915, 1475)], fill=(242, 193, 78))
    im.save(path)

def main():
    ep, cfg = sys.argv[1], json.load(open(sys.argv[2]))
    src = os.path.join(ep, "out", "final.mp4"); out = os.path.join(ep, "shorts"); os.makedirs(out, exist_ok=True)
    for s in cfg:
        ov = os.path.join(out, s["name"] + "_ov.png"); overlay(ov, s); dst = os.path.join(out, s["name"] + ".mp4")
        fc = ("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30,"
              "eq=brightness=-0.08[bg];[b]scale=1080:-2[fg];[bg][fg]overlay=0:620[v1];[v1][1:v]overlay=0:0,format=yuv420p[v]")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(s["start"]), "-t", str(s["dur"]), "-i", src, "-i", ov,
                        "-filter_complex", fc, "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-preset", "medium", "-crf", "23",
                        "-r", "24", "-c:a", "aac", "-b:a", "128k", "-af", f"afade=t=in:d=0.2,afade=t=out:st={s['dur']-0.6}:d=0.6",
                        "-movflags", "+faststart", dst], check=True)
        print("short:", dst)

if __name__ == "__main__":
    main()
