---
title: Ai 聊天助手大全
description: 探索各大领先的 AI 聊天对话模型与虚拟角色伴侣，提升交互体验。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "豆包", "desc": "豆包工作任务改版，新用户免费领30天会员", "logo": "/ai-logos/doubao.png", "link": "#"},
  {"name": "千问", "desc": "全能AI助手，基于Qwen模型", "logo": "/ai-logos/qianwen.png", "link": "#"},
  {"name": "讯飞星火", "desc": "AI智能助手，PPT生成、深度研究", "logo": "/ai-logos/xinghuo.png", "link": "#"},
  {"name": "ChatGPT", "desc": "OpenAI 推出的AI聊天机器人", "logo": "/ai-logos/chatgpt.png", "link": "#"},
  {"name": "Claude", "desc": "Anthropic公司推出的对话式AI智能助手", "logo": "/ai-logos/claude.png", "link": "#"},
  {"name": "Gemini", "desc": "Google推出的AI聊天对话机器人Gemini", "logo": "/ai-logos/gemini.png", "link": "#"},
  {"name": "Kimi智能助手", "desc": "月之暗面推出的AI智能助手", "logo": "/ai-logos/kimi.png", "link": "#"},
  {"name": "DeepSeek", "desc": "幻方量化推出的AI智能助手和开源大模型", "logo": "/ai-logos/deepseek.png", "link": "#"},
  {"name": "Z.ai", "desc": "智谱面向全球推出的AI模型体验平台", "logo": "/ai-logos/zai.png", "link": "#"},
  {"name": "腾讯元宝", "desc": "腾讯推出的免费AI智能助手", "logo": "/ai-logos/yuanbao.png", "link": "#"},
  {"name": "Grok", "desc": "马斯克旗下xAI推出的人工智能助手", "logo": "/ai-logos/grok.png", "link": "#"},
  {"name": "Duck.ai", "desc": "DuckDuckGo 推出的免费 AI 聊天平台", "logo": "/ai-logos/duckai.png", "link": "#"},
  {"name": "MiniMax", "desc": "MiniMax推出的AI智能问答助手", "logo": "/ai-logos/minimax.png", "link": "#"},
  {"name": "LongCat", "desc": "美团推出的自研大模型AI对话平台", "logo": "/ai-logos/longcat.png", "link": "#"},
  {"name": "文心一言", "desc": "百度推出的基于文心大模型的AI智能助手", "logo": "/ai-logos/wenxinyiyan.png", "link": "#"},
  {"name": "智谱清言", "desc": "智谱推出的全能AI助手", "logo": "/ai-logos/zhipuqingyan.png", "link": "#"},
  {"name": "逗逗AI", "desc": "AI游戏陪玩，支持原神、黑神话、LOL！", "logo": "/ai-logos/doudouai.png", "link": "#"},
  {"name": "知达AI", "desc": "专为教育全场景打造的AI智能助教", "logo": "/ai-logos/zhidaai.png", "link": "#"},
  {"name": "华为小艺", "desc": "华为旗下小艺AI助手网页版，已接入DeepSeek-...", "logo": "/ai-logos/xiaoyi.png", "link": "#"},
  {"name": "Lorka AI", "desc": "多模型 AI 聚合对话平台", "logo": "/ai-logos/lorka.png", "link": "#"},
  {"name": "问小白", "desc": "AI智能助手，支持DeepSeek满血版", "logo": "/ai-logos/wenxiaobai.png", "link": "#"},
  {"name": "百灵大模型", "desc": "蚂蚁集团推出的 Ling-1T 大模型对话体验平台", "logo": "/ai-logos/bailing.png", "link": "#"},
  {"name": "书生大模型", "desc": "上海人工智能实验室推出的系列AI模型", "logo": "/ai-logos/shusheng.png", "link": "#"},
  {"name": "阶跃AI", "desc": "阶跃星辰推出的支持多模态的AI聊天机器人", "logo": "/ai-logos/jieyueai.png", "link": "#"},
  {"name": "百小医", "desc": "百川智能推出的AI家庭医生平台", "logo": "/ai-logos/baixiaoyi.png", "link": "#"},
  {"name": "天工AI", "desc": "昆仑万维推出的AI智能助手", "logo": "/ai-logos/tiangong.png", "link": "#"},
  {"name": "商量SenseChat", "desc": "商汤科技推出的免费AI聊天助手", "logo": "/ai-logos/sensechat.png", "link": "#"},
  {"name": "Qwen Chat", "desc": "阿里通义推出的 Qwen 最新模型体验平台", "logo": "/ai-logos/qwenchat.png", "link": "#"},
  {"name": "Me.bot", "desc": "心识宇宙推出的个性化AI伴侣产品", "logo": "/ai-logos/mebot.png", "link": "#"},
  {"name": "Saylo", "desc": "AI驱动的故事角色扮演游戏应用，沉浸式的剧本...", "logo": "/ai-logos/saylo.png", "link": "#"},
  {"name": "Poe", "desc": "问答社区Quora推出的问答机器人工具", "logo": "/ai-logos/poe.png", "link": "#"},
  {"name": "Copilot", "desc": "微软推出的网页版Copilot助手", "logo": "/ai-logos/copilot.png", "link": "#"},
  {"name": "Character.AI", "desc": "创建虚拟角色并与其对话", "logo": "/ai-logos/characterai.png", "link": "#"},
  {"name": "Meta AI助手", "desc": "Meta推出的免费AI聊天助手", "logo": "/ai-logos/metaai.png", "link": "#"},
  {"name": "Bing新必应", "desc": "微软推出的新版结合了ChatGPT功能的必应", "logo": "/ai-logos/bing.png", "link": "#"},
  {"name": "Koko AI", "desc": "Seele公司推出的「AI+3D」情感陪伴产品", "logo": "/ai-logos/kokoai.png", "link": "#"},
  {"name": "通义星尘", "desc": "用AI定制属于你自己的IP角色", "logo": "/ai-logos/tongyixingchen.png", "link": "#"},
  {"name": "CueMe", "desc": "夸克推出的AI智能对话助手，支持2万字长文写作", "logo": "/ai-logos/cueme.png", "link": "#"},
  {"name": "造梦次元", "desc": "AI互动内容平台，虚拟角色逗你开心", "logo": "/ai-logos/zaomeng.png", "link": "#"},
  {"name": "Museland", "desc": "沉浸式AI角色扮演产品", "logo": "/ai-logos/museland.png", "link": "#"}
]
</script>

# Ai 聊天助手大全

精选全球前沿 AI 聊天模型、问答机器人与虚拟角色互动平台。

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
