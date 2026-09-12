---
title: Ai 音频工具大全
description: 收录 Suno、Udio、ElevenLabs 等前沿 AI 音乐生成与高质量语音合成工具。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "魔音工坊", "desc": "AI配音工具，轻松配出媲美真人的声音", "logo": "/ai-logos/moyingongfang.png", "link": "https://www.bing.com/search?q=%E9%AD%94%E9%9F%B3%E5%B7%A5%E5%9D%8A"},
  {"name": "讯飞智作", "desc": "AI文本配音工具，数字人课程、营销视频制作", "logo": "/ai-logos/xunfeizhizuo.png", "link": "https://www.bing.com/search?q=%E8%AE%AF%E9%A3%9E%E6%99%BA%E4%BD%9C"},
  {"name": "逗哥配音", "desc": "一站式AI配音工具，抖音爆款配音始发地", "logo": "/ai-logos/dougepeiyin.png", "link": "https://www.bing.com/search?q=%E9%80%97%E5%93%A5%E9%85%8D%E9%9F%B3"},
  {"name": "讯飞译制", "desc": "科大讯飞推出的AI音视频本地化平台", "logo": "/ai-logos/xunfeiyizhi.png", "link": "https://www.bing.com/search?q=%E8%AE%AF%E9%A3%9E%E8%AF%91%E5%88%B6"},
  {"name": "Suno", "desc": "高质量的AI音乐创作平台", "logo": "/ai-logos/suno.png", "link": "https://www.bing.com/search?q=Suno"},
  {"name": "音述AI", "desc": "全球首个AI音乐社区", "logo": "/ai-logos/yinshuai.png", "link": "https://www.bing.com/search?q=%E9%9F%B3%E8%BF%B0AI"},
  {"name": "ElevenLabs", "desc": "AI文本转语音，支持包含中文在内的29种语言", "logo": "/ai-logos/elevenlabs.png", "link": "https://www.bing.com/search?q=ElevenLabs"},
  {"name": "琅琅配音", "desc": "智能文本转语音工具", "logo": "/ai-logos/langlangpeiyin.png", "link": "https://www.bing.com/search?q=%E7%90%85%E7%90%85%E9%85%8D%E9%9F%B3"},
  {"name": "千音漫语", "desc": "AI声音创作助手，支持声音克隆", "logo": "/ai-logos/qianyinmanyu.png", "link": "https://www.bing.com/search?q=%E5%8D%83%E9%9F%B3%E6%BC%AB%E8%AF%AD"},
  {"name": "MiniMax Audio", "desc": "MiniMax推出的AI语音合成工具，支持声音克隆", "logo": "/ai-logos/minimaxaudio.png", "link": "https://www.bing.com/search?q=MiniMax%20Audio"},
  {"name": "Noiz AI", "desc": "AI配音工具，支持文本转语音和声音克隆", "logo": "/ai-logos/noizai.png", "link": "https://www.bing.com/search?q=Noiz%20AI"},
  {"name": "Tunee", "desc": "首个对话式音乐创作AI智能体", "logo": "/ai-logos/tunee.png", "link": "https://www.bing.com/search?q=Tunee"},
  {"name": "讯飞听见", "desc": "科大讯飞推出的在线AI语音转文字工具", "logo": "/ai-logos/xunfeitingjian.png", "link": "https://www.bing.com/search?q=%E8%AE%AF%E9%A3%9E%E5%90%AC%E8%A7%81"},
  {"name": "Gemini Notebook", "desc": "谷歌推出的AI笔记应用，5分钟生成一段对话播客", "logo": "/ai-logos/gemininotebook.png", "link": "https://www.bing.com/search?q=Gemini%20Notebook"},
  {"name": "Flow Music", "desc": "Google Labs推出的AI音乐创作平台", "logo": "/ai-logos/flowmusic.png", "link": "https://www.bing.com/search?q=Flow%20Music"},
  {"name": "Venus未音", "desc": "腾讯音乐旗下首款一站式AI音乐创作工具", "logo": "/ai-logos/venus.png", "link": "https://www.bing.com/search?q=Venus%E6%9C%AA%E9%9F%B3"},
  {"name": "海绵音乐", "desc": "字节跳动推出的免费AI音乐创作和发现平台", "logo": "/ai-logos/haimianyinyue.png", "link": "https://www.bing.com/search?q=%E6%B5%B7%E7%BB%B5%E9%9F%B3%E4%B9%90"},
  {"name": "MELO音乐", "desc": "AI 音乐生成平台，支持多模态创作能力", "logo": "/ai-logos/meloyinyue.png", "link": "https://www.bing.com/search?q=MELO%E9%9F%B3%E4%B9%90"},
  {"name": "MeloLab", "desc": "一站式 AI 音乐生成与编辑平台", "logo": "/ai-logos/melolab.png", "link": "https://www.bing.com/search?q=MeloLab"},
  {"name": "万象有声", "desc": "AI 一站式有声内容创作平台", "logo": "/ai-logos/wanxiangyousheng.png", "link": "https://www.bing.com/search?q=%E4%B8%87%E8%B1%A1%E6%9C%89%E5%A3%B0"},
  {"name": "Nafy AI", "desc": "在线 AI 音乐生成器，支持扩展、替换、翻唱", "logo": "/ai-logos/nafyai.png", "link": "https://www.bing.com/search?q=Nafy%20AI"},
  {"name": "UniScribe", "desc": "AI 免费在线音视频转文字平台", "logo": "/ai-logos/uniscribe.png", "link": "https://www.bing.com/search?q=UniScribe"},
  {"name": "轻析 LiteSight", "desc": "AI 视频内容提取工具，自动转文字", "logo": "/ai-logos/litesight.png", "link": "https://www.bing.com/search?q=%E8%BD%BB%E6%9E%90%20LiteSight"},
  {"name": "TurboScribe", "desc": "专业 AI 音视频转文字工具", "logo": "/ai-logos/turboscribe.png", "link": "https://www.bing.com/search?q=TurboScribe"},
  {"name": "多维视界", "desc": "一站式AI音视频智能分析平台", "logo": "/ai-logos/duoweishijie.png", "link": "https://www.bing.com/search?q=%E5%A4%9A%E7%BB%B4%E8%A7%86%E7%95%8C"},
  {"name": "天谱乐", "desc": "唱鸭团队推出的首个多模态音乐生成大模型", "logo": "/ai-logos/tianpule.png", "link": "https://www.bing.com/search?q=%E5%A4%A9%E8%B0%B1%E4%B9%90"},
  {"name": "音疯", "desc": "昆仑万维推出的AI音乐创作平台，一键生成原创...", "logo": "/ai-logos/yinfeng.png", "link": "https://www.bing.com/search?q=%E9%9F%B3%E7%96%AF"},
  {"name": "Mureka", "desc": "昆仑万维推出的 AI 音乐商用创作平台", "logo": "/ai-logos/mureka.png", "link": "https://www.bing.com/search?q=Mureka"},
  {"name": "音潮", "desc": "全栈自研的AI音乐创作平台", "logo": "/ai-logos/yinchao.png", "link": "https://www.bing.com/search?q=%E9%9F%B3%E6%BD%AE"},
  {"name": "音剪", "desc": "喜马拉雅推出的一站式AI音频创作平台", "logo": "/ai-logos/yinjian.png", "link": "https://www.bing.com/search?q=%E9%9F%B3%E5%89%AA"},
  {"name": "音秘", "desc": "百度推出的AI播客创作工具", "logo": "/ai-logos/yinmi.png", "link": "https://www.bing.com/search?q=%E9%9F%B3%E7%A7%98"},
  {"name": "MemoAI", "desc": "免费的AI语音转文字工具", "logo": "/ai-logos/memoai.png", "link": "https://www.bing.com/search?q=MemoAI"},
  {"name": "Reecho睿声", "desc": "超拟真的中英文AI语音克隆/生成平台", "logo": "/ai-logos/reecho.png", "link": "https://www.bing.com/search?q=Reecho%E7%9D%BF%E5%A3%B0"},
  {"name": "Udio", "desc": "免费的AI音乐创作工具，每月可生成1200首歌曲", "logo": "/ai-logos/udio.png", "link": "https://www.bing.com/search?q=Udio"},
  {"name": "网易天音", "desc": "网易推出的一站式AI音乐创作工具", "logo": "/ai-logos/wangyitianyin.png", "link": "https://www.bing.com/search?q=%E7%BD%91%E6%98%93%E5%A4%A9%E9%9F%B3"},
  {"name": "Lyrics Into Song AI", "desc": "在线AI音乐创作工具，输入歌词创建个性化歌曲", "logo": "/ai-logos/lyricsintosong.png", "link": "https://www.bing.com/search?q=Lyrics%20Into%20Song%20AI"},
  {"name": "Stable Audio", "desc": "Stability AI最新推出的音乐生成工具", "logo": "/ai-logos/stableaudio.png", "link": "https://www.bing.com/search?q=Stable%20Audio"},
  {"name": "TextToSpeech", "desc": "完全免费的AI文字转语音工具", "logo": "/ai-logos/texttospeech.png", "link": "https://www.bing.com/search?q=TextToSpeech"},
  {"name": "TTSMaker", "desc": "马克配音（MakVoice）推出的免费AI文字转语...", "logo": "/ai-logos/ttsmaker.png", "link": "https://www.bing.com/search?q=TTSMaker"},
  {"name": "LOVO AI", "desc": "专业的AI文字转语音工具，支持500+声音和100...", "logo": "/ai-logos/lovoai.png", "link": "https://www.bing.com/search?q=LOVO%20AI"}
]
</script>

# Ai 音频工具大全

精选全球前沿 AI 音乐生成、高质量语音合成合成、配音、音效克隆与转写神器。

<div class="tool-grid">
  <ToolCard v-for="t in tools" :key="t.name" :tool="t" />
</div>

<style>
.tool-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 24px;
}
</style>
