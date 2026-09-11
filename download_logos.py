import urllib.request
import json
import os
import re

domains = {
  "蛙蛙写作": "wawawriter.com",
  "Loomy": "loomy.xunfei.cn",
  "Laper": "laper.ai",
  "笔灵AI写作": "ibiling.cn",
  "办公小浣熊": "xiaohuanxiong.com",
  "稿定AI文案": "gaoding.com",
  "笔灵AI小说": "ibiling.cn",
  "讯飞绘文": "huiwen.xfyun.cn",
  "沁言学术": "qinyanai.com",
  "切问学术": "qiewenpaper.com",
  "千笔AI论文": "qianbiai.com",
  "66AI论文": "66paper.cn",
  "剧云": "jucloud.com",
  "维普科创助手": "super.cqvip.com",
  "稿易AI论文": "gaoyiai.com",
  "茅茅虫": "mmc.cc",
  "笔目鱼": "bmysci.com",
  "01Agent": "01agent.cn",
  "光速写作": "guangsuxie.com",
  "小鱼AI写作": "xiaoyuxiezuo.com",
  "万能小in": "xiaoin.cn",
  "文优小助": "wenyouxiaozhu.com",
  "排版小星": "paibanxiaoxing.com",
  "墨问": "mowen.cn",
  "新华妙笔": "miaobi.xinhuaskl.com",
  "丹青妙笔": "danqingmiaobi.com",
  "FeelFish": "feelfish.com",
  "Loomi": "loomi.live",
  "ReadPo": "readpo.com",
  "GetDraft": "getdraft.ai",
  "落笔AI写作": "luobi.net",
  "创飞写作": "chuangfeiai.com",
  "超级小说家": "supernovelist.com",
  "材料星AI": "cailiaoxing.com",
  "量子探险": "yfbudong.com",
  "社研通": "sheyantong.cn",
  "Rubriq": "rubriq.com",
  "QuillBot": "quillbot.com",
  "Paperpal": "paperpal.com",
  "创一AI": "creatifyone.com"
}

# Parse index.md to get the logo file mapping
with open('ai/writing/index.md', 'r', encoding='utf-8') as f:
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
