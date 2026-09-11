import urllib.request
import json
import os
import re

domains = {
  "Loomy": "loomy.xunfei.cn",
  "办公小浣熊": "xiaohuanxiong.com",
  "AiPPT": "aippt.com",
  "文多多AiPPT": "docmee.cn",
  "千问AiPPT": "tongyi.aliyun.com",
  "咔片PPT": "cappt.cc",
  "博思AiPPT": "pptgo.cn",
  "iSlide AiPPT": "islide.cc",
  "二狗PPT": "2dogppt.com",
  "稿定PPT": "gaoding.com",
  "Pi智能PPT": "pi.design",
  "讯飞智文": "zhiwen.xfyun.cn",
  "笔格AiPPT": "bigppt.cn",
  "百度文库AI助手": "wenku.baidu.com",
  "Gamma": "gamma.app",
  "笔灵AiPPT": "ibiling.cn",
  "AiPPT插件": "aippt.cn",
  "Napkin": "napkin.ai",
  "Swishy": "swishy.ai",
  "ChartGen": "chartgen.ai",
  "Diagrimo": "tenorshare.ai",
  "PicDoc": "picdoc.ai",
  "Kimi PPT助手": "kimi.com",
  "夸克PPT": "ppt.quark.cn",
  "GAIPPT": "gaippt.com",
  "美图AI PPT": "design.meitu.com",
  "飞象老师": "feixianglaoshi.com",
  "一点PPT": "1dppt.com",
  "NarraLand": "narraland.com",
  "课灵 PPT": "kolinkai.cn",
  "清言PPT": "chatglm.cn",
  "万兴智演": "zhiyan.wondershare.cn",
  "麦当秀MindShow": "mindshow.cc",
  "VoxDeck": "voxdeck.ai",
  "AiBiao": "aibiao.com",
  "ChatBA": "chatba.com",
  "Decktopus AI": "decktopus.com",
  "Powerpresent AI": "powerpresent.ai",
  "希沃白板": "seewo.com",
  "秒出PPT": "10sppt.com"
}

# Parse index.md to get the logo file mapping
with open('ai/office/index.md', 'r', encoding='utf-8') as f:
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
