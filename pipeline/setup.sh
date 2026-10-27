#!/bin/bash
# Fresh-session setup: copies the pipeline to /home/claude/pipeline and fetches the voice models.
set -e
R=$(cd "$(dirname "$0")" && pwd)
mkdir -p /home/claude/pipeline
cp -r "$R"/*.py "$R"/fonts /home/claude/pipeline/
pip install --break-system-packages -q kokoro-onnx soundfile pillow numpy >/dev/null 2>&1 || pip install -q kokoro-onnx soundfile pillow numpy
cd /home/claude/pipeline
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s $f ] || curl -sSL -o $f https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f
done
which ffmpeg >/dev/null || (apt-get install -y -qq ffmpeg >/dev/null)
echo "pipeline ready in /home/claude/pipeline"
