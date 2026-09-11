import urllib.request
import json
import os
import re

domains = {
  "LibTV": "liblib.tv",
  "即梦AI": "jimeng.jianying.com",
  "Seko": "seko.sensetime.com",
  "updream": "updream.bilibili.com",
  "小云雀": "xyq.jianying.com",
  "SoundView": "soundviewai.com",
  "蛙蛙漫剧": "wawawriter.com",
  "绘蛙AI视频": "ihuiwa.com",
  "LiblibAI": "liblib.art",
  "AniShort": "anishort.ai",
  "白日梦": "aibrm.com",
  "有言": "youyan3d.com",
  "蝉镜": "chanjing.cc",
  "VibeKnow": "vibeknow.com",
  "立刻MV": "dubmic.com",
  "ArtarchStudio": "artarch.ai",
  "Seedance": "seed.bytedance.com",
  "可灵AI": "klingai.com",
  "魔法星云": "xingyun3d.com",
  "Pollo AI": "pollo.ai",
  "OnSolo": "onsolo.ai",
  "海艺剧场": "seavideo.tv",
  "立刻成片": "dubmic.com",
  "MetaDig": "waytometa.cn",
  "Higgsfield": "higgsfield.ai",
  "TapNow": "tapnow.ai",
  "造剧": "zaoju.art",
  "Pavo": "pavo-ai.work",
  "RHTV": "runninghub.cn",
  "Vidu": "vidu.studio",
  "Renoise": "renoise.ai",
  "JoyAI": "joyai.com",
  "漫小芽": "manxiaoya.com",
  "Preview": "preview.io",
  "知漫剧": "jiaxunai.cn",
  "Lumen Flow": "lumenflow.net",
  "TapVid": "tapvid.ai",
  "Lumina": "ai.byteplus.com",
  "纳逗Pro": "nadoupro.iqiyi.com",
  "TDream": "tdream.qq.com"
}

# Parse index.md to get the logo file mapping
with open('ai/video/index.md', 'r', encoding='utf-8') as f:
    content = f.read()

# match {"name": "...", ... "logo": "/ai-logos/wawa.png", ...}
matches = re.finditer(r'{"name":\s*"([^"]+)",[^}]*"logo":\s*"([^"]+)"', content)

success_count = 0

for match in matches:
    name = match.group(1)
    logo_path = match.group(2)
    
    if name in domains:
        domain = domains[name]
        # Use Google's favicon API to fetch a 128x128 icon
        url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
        
        # relative path
        rel_path = logo_path.lstrip('/')
        # It's in 'public' directory
        abs_path = os.path.join('public', rel_path)
        
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(abs_path, 'wb') as out_file:
                out_file.write(response.read())
            success_count += 1
            print(f"Downloaded {name} from {domain} to {abs_path}")
        except Exception as e:
            print(f"Failed to download {name}: {e}")

print(f"Finished. Successfully downloaded {success_count} logos.")
