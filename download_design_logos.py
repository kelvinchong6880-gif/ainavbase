import urllib.request
import json
import os
import re

domains = {
  "Lovart": "lovart.ai",
  "绘蛙AI": "ihuiwa.com",
  "妙呀": "miaoyaai.cn",
  "稿定AI": "gaoding.com",
  "墨刀AI": "modao.cc",
  "Holopix AI": "holopix.cn",
  "美图设计室": "designkit.cn",
  "135 AI排版": "135editor.com",
  "堆友AI": "d.design",
  "OJO": "ojo.art",
  "Figma AI": "figma.com",
  "Seede AI": "seede.ai",
  "Pixso AI": "pixso.cn",
  "Wegic": "wegic.ai",
  "Recraft AI": "recraft.ai",
  "星流AI": "xingliu.art",
  "Stitch": "stitch.withgoogle.com",
  "Miora": "miora.design",
  "Ardot": "ardot.tencent.com",
  "创客贴AI": "chuangkit.com",
  "Open Design": "open-design.ai",
  "Onlook": "onlook.com",
  "Ribbi": "ribbi.ai",
  "Tavafa塔维法": "tavafa.com",
  "Interiorize": "interiorize.ai",
  "QuiverAI": "quiver.ai",
  "GemDesign": "design.gemcoder.com",
  "Pic Copilot": "piccopilot.com",
  "魔力工作室": "canva.com",
  "码上有创意": "idesign.alipay.com",
  "七色米AI": "qisemi.com",
  "爱设计": "isheji.com",
  "PagePop": "pagepop.ai",
  "小墨度编辑器": "xmyeditor.com",
  "美间AI": "meijian.com",
  "Calicat": "calicat.cn",
  "Microsoft Designer": "designer.microsoft.com",
  "UXbot": "uxbot.cn",
  "燕雀光年": "yanqueai.com",
  "标小智LOGO生成器": "logosc.cn"
}

# Parse index.md to get the logo file mapping
with open('ai/design/index.md', 'r', encoding='utf-8') as f:
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
