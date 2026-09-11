import urllib.request
import json
import os
import re

domains = {
  "豆包": "doubao.com",
  "千问": "tongyi.aliyun.com",
  "讯飞星火": "xinghuo.xfyun.cn",
  "ChatGPT": "chatgpt.com",
  "Claude": "claude.ai",
  "Gemini": "gemini.google.com",
  "Kimi智能助手": "kimi.moonshot.cn",
  "DeepSeek": "deepseek.com",
  "Z.ai": "z.ai",
  "腾讯元宝": "yuanbao.tencent.com",
  "Grok": "grok.com",
  "Duck.ai": "duck.ai",
  "MiniMax": "minimaxi.com",
  "LongCat": "longcat.chat",
  "文心一言": "yiyan.baidu.com",
  "智谱清言": "chatglm.cn",
  "逗逗AI": "doudou.fun",
  "知达AI": "zida.school",
  "华为小艺": "xiaoyi.huawei.com",
  "Lorka AI": "lorka.ai",
  "问小白": "wenxiaobai.com",
  "百灵大模型": "ant-ling.com",
  "书生大模型": "intern-ai.org.cn",
  "阶跃AI": "stepfun.com",
  "百小医": "baichuan-ai.com",
  "天工AI": "tiangong.cn",
  "商量SenseChat": "chat.sensetime.com",
  "Qwen Chat": "chat.qwen.ai",
  "Me.bot": "me.bot",
  "Saylo": "sayloai.com",
  "Poe": "poe.com",
  "Copilot": "copilot.microsoft.com",
  "Character.AI": "character.ai",
  "Meta AI助手": "meta.ai",
  "Bing新必应": "bing.com",
  "Koko AI": "seeles.ai",
  "通义星尘": "xingchen.aliyun.com",
  "CueMe": "cueme.cn",
  "造梦次元": "ciyuan.ideaflow.pro",
  "Museland": "museland.ai"
}

# Parse index.md to get the logo file mapping
with open('ai/chat/index.md', 'r', encoding='utf-8') as f:
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
