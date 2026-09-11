import urllib.request
import json
import os
import re

domains = {
  "Loomy": "loomy.xunfei.cn",
  "Lovart": "lovart.ai",
  "Seko": "seko.sensetime.com",
  "小云雀": "xyq.jianying.com",
  "爱派AiPy": "aipyaipy.com",
  "Atoms": "atoms.dev",
  "WorkBuddy": "workbuddy.ai",
  "WaClaw": "waclaw.ihuiwa.com",
  "马上飞": "codeflying.net",
  "ArkClaw": "volcengine.com",
  "扣子Coze": "coze.cn",
  "讯飞星辰Agent": "agent.xfyun.cn",
  "01Agent": "01agent.cn",
  "TraeWork": "trae.cn",
  "堆友Agent": "d.design",
  "AutoClaw": "autoglm.zhipuai.cn",
  "OpenClaw": "openclaw.ai",
  "Tabbit": "tabbit.com",
  "切问学术": "qiewenpaper.com",
  "豆包工作": "doubao.com",
  "QwenWork": "qwenwork.ai",
  "QwenPaw": "agentscope.io",
  "AionClaw": "aionclaw.com",
  "Tokera AI": "tokera.com.cn",
  "Floatboat": "floatboat.ai",
  "Flowith": "flowith.io",
  "千问办公": "qwenwork.cn",
  "ByteCP": "quchiai.com",
  "TipKay": "tipkay.com",
  "纳米Work": "work.n.cn",
  "KroWork": "krowork.com",
  "觅游": "meyo123.com",
  "虾345": "xia345.com",
  "Sophclaw": "sophnet.com",
  "LobsterAI": "lobsterai.youdao.com",
  "Nile": "nile.shop",
  "Kevvee": "kevvee.com",
  "Matrix": "matrix.build",
  "Manus": "manus.im",
  "腾讯Marvis": "marvis.qq.com"
}

# Parse index.md to get the logo file mapping
with open('ai/agent/index.md', 'r', encoding='utf-8') as f:
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
