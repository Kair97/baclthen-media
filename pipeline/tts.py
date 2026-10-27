import sys, os, importlib.util, soundfile as sf
ep=sys.argv[1]; R='/home/claude/pipeline'
spec=importlib.util.spec_from_file_location('b',f'{R}/{ep}/beats.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
from kokoro_onnx import Kokoro
k=Kokoro(f'{R}/kokoro-v1.0.onnx',f'{R}/voices-v1.0.bin'); tot=0
for i,b in enumerate(m.BEATS):
    p=f'{R}/{ep}/out/vo_{i:02d}.wav'
    if not os.path.exists(p):
        a,sr=k.create(b['text'],voice=m.VOICE,speed=m.SPEED,lang='en-us'); sf.write(p,a,sr)
    d=sf.info(p).duration; tot+=d+0.45; print(i,round(d,1),flush=True)
print('TOTAL',round(tot,1),flush=True)
