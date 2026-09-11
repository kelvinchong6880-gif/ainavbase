import urllib.request
import json
import os
import re

domains = {
  "即梦": "jimeng.jianying.com",
  "绘蛙": "ihuiwa.com",
  "Lovart": "lovart.ai",
  "LiblibAI-哩布哩布AI": "liblib.art",
  "稿定AI": "gaoding.com",
  "阿贝智能": "abeiai.com",
  "美图设计室": "designkit.cn",
  "Midjourney": "midjourney.com",
  "Stable Diffusion": "stability.ai",
  "Civitai": "civitai.com",
  "吐司AI": "tusi.cn",
  "造点AI": "zaodian.quark.cn",
  "RunningHub": "runninghub.cn",
  "通义万相": "wanxiang.aliyun.com",
  "可灵AI": "klingai.com",
  "秒画": "miaohua.sensetime.com",
  "WHEE": "whee.com",
  "鸣哩": "wuli.art",
  "insMind": "insmind.com",
  "抠抠图": "koukoutu.com",
  "图改改": "tugaigai.com",
  "Epixa": "epixa.cn",
  "AlphaVow": "alphavow.com",
  "ChatArt": "chatartpro.com",
  "Krene": "krene.com",
  "AI改图神器": "img.logosc.cn",
  "米粿AI": "miguocomics.com",
  "咖图AI": "katuai.cn",
  "视觉工厂": "shijuegongchang.com",
  "秒绘AI": "miaohuiai.cc",
  "妙话AI": "imiaohua.com",
  "炉米Lumi": "artistrylab.net",
  "Krea AI": "krea.ai",
  "Kira": "kira.art",
  "Photoroom": "photoroom.com",
  "Ribbet.ai": "ribbet.ai",
  "万相营造": "agi.taobao.com",
  "悟空图像PhotoSir": "photosir.com",
  "360智图": "pic.360.com",
  "像素蛋糕": "pixcakes.com"
}

# Parse index.md to get the logo file mapping
with open('ai/image/index.md', 'r', encoding='utf-8') as f:
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
