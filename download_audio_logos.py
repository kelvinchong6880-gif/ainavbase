import urllib.request
import json
import os
import re

domains = {
  "魔音工坊": "moyin.com",
  "讯飞智作": "xfzhizuo.cn",
  "逗哥配音": "douge.club",
  "讯飞译制": "yizhi.iflyrec.com",
  "Suno": "suno.com",
  "音述AI": "yinshu.me",
  "ElevenLabs": "elevenlabs.io",
  "琅琅配音": "lang123.top",
  "千音漫语": "qianyin123.com",
  "MiniMax Audio": "minimax.io",
  "Noiz AI": "noiz.ai",
  "Tunee": "tunee.ai",
  "讯飞听见": "iflyrec.com",
  "Gemini Notebook": "notebooklm.google.com",
  "Flow Music": "flowmusic.google",
  "Venus未音": "y.qq.com",
  "海绵音乐": "haimianyinyue.com",
  "MELO音乐": "51melo.com",
  "MeloLab": "melolab.ai",
  "万象有声": "audimind.com",
  "Nafy AI": "nafy.ai",
  "UniScribe": "uniscribe.co",
  "轻析 LiteSight": "litesight.cn",
  "TurboScribe": "turboscribe.ai",
  "多维视界": "dwsj.cn",
  "天谱乐": "tianpuyue.cn",
  "音疯": "yinfeng.cn",
  "Mureka": "mureka.ai",
  "音潮": "yinchaoyongxian.com",
  "音剪": "audioeditor.ximalaya.com",
  "音秘": "audiomyst.baidu.com",
  "MemoAI": "memo.ac",
  "Reecho睿声": "reecho.ai",
  "Udio": "udio.com",
  "网易天音": "tianyin.music.163.com",
  "Lyrics Into Song AI": "lyricsintosong.ai",
  "Stable Audio": "stableaudio.com",
  "TextToSpeech": "texttospeech.im",
  "TTSMaker": "ttsmaker.com",
  "LOVO AI": "lovo.ai"
}

# Parse index.md to get the logo file mapping
with open('ai/audio/index.md', 'r', encoding='utf-8') as f:
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
