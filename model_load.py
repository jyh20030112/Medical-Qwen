# model_download.py
from modelscope import snapshot_download

model_dir = snapshot_download('qwen/Qwen3-4B-Base', cache_dir='./', revision='master')