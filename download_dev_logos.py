import urllib.request
import json
import os
import re

domains = {
  "秒哒": "miaoda.baidu.com",
  "秒悟Meoo": "meoo.com",
  "码上飞": "codeflying.net",
  "讯飞星辰MaaS": "maas.xfyun.cn",
  "BigModel": "bigmodel.cn",
  "阿里云百炼": "aliyun.com",
  "扣子-AI办公": "coze.cn",
  "方舟 Coding Plan": "volcengine.com",
  "ZenMux": "zenmux.ai",
  "Google AI Studio": "aistudio.google.com",
  "FastGPT": "fastgpt.io",
  "Zion": "functorz.com",
  "n8n": "n8n.io",
  "Dify": "dify.ai",
  "袋马": "daimax.cn",
  "千问云": "qianwenai.com",
  "StreamLake": "streamlake.com",
  "造化工坊": "zaohua.qq.com",
  "TArk元舟": "tark.dd1010.com",
  "Playabl": "playabl.ai",
  "AstraFlow星图": "ucloud.cn",
  "OpenRouter": "openrouter.ai",
  "SiliconFlow": "siliconflow.cn",
  "OfoxAI": "ofox.ai",
  "QMuse": "qmusespace.com",
  "麦芽AI": "myaifast.com",
  "Trickle AI": "trickle.so",
  "WorldClaw": "worldclaw.ai",
  "TokenDance": "tokendance.ai",
  "MoMA": "ecloud.10086.cn",
  "博查万象": "bochaai.com",
  "B.AI": "b.ai",
  "灵光": "lingguang.com",
  "万小智": "aliyun.com",
  "BASE44": "base44.com",
  "英博云AI算力": "ebtech.com",
  "汇智Token工场": "agentsyun.com",
  "Aippy": "aippy.ai",
  "快马InsCode": "inscode.net",
  "NoCode": "nocode.cn"
}

# Parse index.md to get the logo file mapping
with open('ai/dev/index.md', 'r', encoding='utf-8') as f:
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
