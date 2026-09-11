---
title: Ai 音频工具大全
description: 收录 Suno、Udio、ElevenLabs 等前沿 AI 音乐生成与高质量语音合成工具。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "魔音工坊", "desc": "AI配音工具，轻松配出媲美真人的声音", "logo": "/ai-logos/moyingongfang.png", "link": "#"},
  {"name": "讯飞智作", "desc": "AI文本配音工具，数字人课程、营销视频制作", "logo": "/ai-logos/xunfeizhizuo.png", "link": "#"},
  {"name": "逗哥配音", "desc": "一站式AI配音工具，抖音爆款配音始发地", "logo": "/ai-logos/dougepeiyin.png", "link": "#"},
  {"name": "讯飞译制", "desc": "科大讯飞推出的AI音视频本地化平台", "logo": "/ai-logos/xunfeiyizhi.png", "link": "#"},
  {"name": "Suno", "desc": "高质量的AI音乐创作平台", "logo": "/ai-logos/suno.png", "link": "#"},
  {"name": "音述AI", "desc": "全球首个AI音乐社区", "logo": "/ai-logos/yinshuai.png", "link": "#"},
  {"name": "ElevenLabs", "desc": "AI文本转语音，支持包含中文在内的29种语言", "logo": "/ai-logos/elevenlabs.png", "link": "#"},
  {"name": "琅琅配音", "desc": "智能文本转语音工具", "logo": "/ai-logos/langlangpeiyin.png", "link": "#"},
  {"name": "千音漫语", "desc": "AI声音创作助手，支持声音克隆", "logo": "/ai-logos/qianyinmanyu.png", "link": "#"},
  {"name": "MiniMax Audio", "desc": "MiniMax推出的AI语音合成工具，支持声音克隆", "logo": "/ai-logos/minimaxaudio.png", "link": "#"},
  {"name": "Noiz AI", "desc": "AI配音工具，支持文本转语音和声音克隆", "logo": "/ai-logos/noizai.png", "link": "#"},
  {"name": "Tunee", "desc": "首个对话式音乐创作AI智能体", "logo": "/ai-logos/tunee.png", "link": "#"},
  {"name": "讯飞听见", "desc": "科大讯飞推出的在线AI语音转文字工具", "logo": "/ai-logos/xunfeitingjian.png", "link": "#"},
  {"name": "Gemini Notebook", "desc": "谷歌推出的AI笔记应用，5分钟生成一段对话播客", "logo": "/ai-logos/gemininotebook.png", "link": "#"},
  {"name": "Flow Music", "desc": "Google Labs推出的AI音乐创作平台", "logo": "/ai-logos/flowmusic.png", "link": "#"},
  {"name": "Venus未音", "desc": "腾讯音乐旗下首款一站式AI音乐创作工具", "logo": "/ai-logos/venus.png", "link": "#"},
  {"name": "海绵音乐", "desc": "字节跳动推出的免费AI音乐创作和发现平台", "logo": "/ai-logos/haimianyinyue.png", "link": "#"},
  {"name": "MELO音乐", "desc": "AI 音乐生成平台，支持多模态创作能力", "logo": "/ai-logos/meloyinyue.png", "link": "#"},
  {"name": "MeloLab", "desc": "一站式 AI 音乐生成与编辑平台", "logo": "/ai-logos/melolab.png", "link": "#"},
  {"name": "万象有声", "desc": "AI 一站式有声内容创作平台", "logo": "/ai-logos/wanxiangyousheng.png", "link": "#"},
  {"name": "Nafy AI", "desc": "在线 AI 音乐生成器，支持扩展、替换、翻唱", "logo": "/ai-logos/nafyai.png", "link": "#"},
  {"name": "UniScribe", "desc": "AI 免费在线音视频转文字平台", "logo": "/ai-logos/uniscribe.png", "link": "#"},
  {"name": "轻析 LiteSight", "desc": "AI 视频内容提取工具，自动转文字", "logo": "/ai-logos/litesight.png", "link": "#"},
  {"name": "TurboScribe", "desc": "专业 AI 音视频转文字工具", "logo": "/ai-logos/turboscribe.png", "link": "#"},
  {"name": "多维视界", "desc": "一站式AI音视频智能分析平台", "logo": "/ai-logos/duoweishijie.png", "link": "#"},
  {"name": "天谱乐", "desc": "唱鸭团队推出的首个多模态音乐生成大模型", "logo": "/ai-logos/tianpule.png", "link": "#"},
  {"name": "音疯", "desc": "昆仑万维推出的AI音乐创作平台，一键生成原创...", "logo": "/ai-logos/yinfeng.png", "link": "#"},
  {"name": "Mureka", "desc": "昆仑万维推出的 AI 音乐商用创作平台", "logo": "/ai-logos/mureka.png", "link": "#"},
  {"name": "音潮", "desc": "全栈自研的AI音乐创作平台", "logo": "/ai-logos/yinchao.png", "link": "#"},
  {"name": "音剪", "desc": "喜马拉雅推出的一站式AI音频创作平台", "logo": "/ai-logos/yinjian.png", "link": "#"},
  {"name": "音秘", "desc": "百度推出的AI播客创作工具", "logo": "/ai-logos/yinmi.png", "link": "#"},
  {"name": "MemoAI", "desc": "免费的AI语音转文字工具", "logo": "/ai-logos/memoai.png", "link": "#"},
  {"name": "Reecho睿声", "desc": "超拟真的中英文AI语音克隆/生成平台", "logo": "/ai-logos/reecho.png", "link": "#"},
  {"name": "Udio", "desc": "免费的AI音乐创作工具，每月可生成1200首歌曲", "logo": "/ai-logos/udio.png", "link": "#"},
  {"name": "网易天音", "desc": "网易推出的一站式AI音乐创作工具", "logo": "/ai-logos/wangyitianyin.png", "link": "#"},
  {"name": "Lyrics Into Song AI", "desc": "在线AI音乐创作工具，输入歌词创建个性化歌曲", "logo": "/ai-logos/lyricsintosong.png", "link": "#"},
  {"name": "Stable Audio", "desc": "Stability AI最新推出的音乐生成工具", "logo": "/ai-logos/stableaudio.png", "link": "#"},
  {"name": "TextToSpeech", "desc": "完全免费的AI文字转语音工具", "logo": "/ai-logos/texttospeech.png", "link": "#"},
  {"name": "TTSMaker", "desc": "马克配音（MakVoice）推出的免费AI文字转语...", "logo": "/ai-logos/ttsmaker.png", "link": "#"},
  {"name": "LOVO AI", "desc": "专业的AI文字转语音工具，支持500+声音和100...", "logo": "/ai-logos/lovoai.png", "link": "#"}
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
