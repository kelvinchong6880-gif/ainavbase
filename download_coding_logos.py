import urllib.request
import json
import os
import re

domains = {
  "TRAE": "trae.ai",
  "秒哒": "miaoda.baidu.com",
  "码上飞": "codeflying.net",
  "代码小浣熊": "xiaohuanxiong.com",
  "Codex": "openai.com",
  "Claude Code": "claude.ai",
  "Agent.Space": "agent.space",
  "Qoder": "qoder.com",
  "OpenCode": "opencode.ai",
  "Kimi Code": "kimi.com",
  "Kilo Code": "kilo.ai",
  "Google Antigravity": "antigravity.google",
  "Kiro": "kiro.dev",
  "Cursor": "cursor.com",
  "Cline": "cline.bot",
  "MiMo Code": "mimo.xiaomi.com",
  "YouWare": "youware.com",
  "ZCode": "zcode.z.ai",
  "CodeBuddy IDE": "codebuddy.cn",
  "Lovable": "lovable.dev",
  "CatPaw": "catpaw.meituan.com",
  "Augment Code": "augmentcode.com",
  "AgnesCode": "agnes-ai.com",
  "MonkeyCode": "monkeycode.cc",
  "通义灵码": "lingma.aliyun.com",
  "GitHub Copilot": "github.com",
  "Firebase Studio": "firebase.google.com",
  "Windsurf": "codeium.com",
  "Bolt.new": "bolt.new",
  "InfCode": "tokensinfinity.com",
  "CodeFlicker": "codeflicker.ai",
  "Clacky AI": "clacky.ai",
  "Replit Agent": "replit.com",
  "Warp Code": "warp.dev",
  "CodeWhisperer": "aws.amazon.com",
  "Zread": "zread.ai",
  "Junie": "junie.jetbrains.com",
  "CodeBuddy": "codebuddy.ai",
  "Qodo": "qodo.ai",
  "iFlow CLI": "iflow.cn"
}

# Parse index.md to get the logo file mapping
with open('ai/coding/index.md', 'r', encoding='utf-8') as f:
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
