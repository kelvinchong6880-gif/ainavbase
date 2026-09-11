---
title: Ai 提示词指令大全
description: 探索各大领先的 AI 提示词指令库与创作平台。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "PromptPilot", "desc": "火山方舟推出的AI提示词解决...", "logo": "/ai-logos/promptpilot.png", "link": "#"},
  {"name": "幕简AI提示词商城", "desc": "AI提示词交易与管理平台，支...", "logo": "/ai-logos/mujian.png", "link": "#"},
  {"name": "提示工程指南", "desc": "提示工程指南（Prompt Engine...", "logo": "/ai-logos/promptingguide.png", "link": "#"},
  {"name": "Google AI提示词库", "desc": "谷歌推出的AI提示词库", "logo": "/ai-logos/googleprompt.png", "link": "#"},
  {"name": "MeiGen", "desc": "免费 AI Prompt 社区与一键生...", "logo": "/ai-logos/meigen.png", "link": "#"},
  {"name": "PromptPerfect", "desc": "PromptPerfect 是一款专业好...", "logo": "/ai-logos/promptperfect.png", "link": "#"},
  {"name": "Stable Diffusion Prompt...", "desc": "OpenArt平台推出的免费提示...", "logo": "/ai-logos/sdprompt.png", "link": "#"},
  {"name": "LocalBanana", "desc": "专注于AI图像Prompt收集与结...", "logo": "/ai-logos/localbanana.png", "link": "#"},
  {"name": "PromptHero", "desc": "AI提示词优化与搜索平台", "logo": "/ai-logos/prompthero.png", "link": "#"},
  {"name": "ClickPrompt", "desc": "在线AI提示词设计工具", "logo": "/ai-logos/clickprompt.png", "link": "#"},
  {"name": "AI Prompt Generator", "desc": "AI Prompt Generator是什么 A...", "logo": "/ai-logos/aipromptgen.png", "link": "#"},
  {"name": "AI Short", "desc": "AI提示词管理和共享平台，多...", "logo": "/ai-logos/aishort.png", "link": "#"},
  {"name": "LangGPT", "desc": "LangGPT是什么 LangGPT是一...", "logo": "/ai-logos/langgpt.png", "link": "#"},
  {"name": "Generrated", "desc": "AI提示词参考平台", "logo": "/ai-logos/generrated.png", "link": "#"},
  {"name": "PublicPrompts", "desc": "PublicPrompts是什么 PublicP...", "logo": "/ai-logos/publicprompts.png", "link": "#"},
  {"name": "Snack Prompt", "desc": "输入正确的提示词，可以让Ch...", "logo": "/ai-logos/snackprompt.png", "link": "#"},
  {"name": "AIPRM", "desc": "AI 提示词库和提示词管理工具", "logo": "/ai-logos/aiprm.png", "link": "#"},
  {"name": "PromptFolder", "desc": "AI提示词生成和管理工具", "logo": "/ai-logos/promptfolder.png", "link": "#"},
  {"name": "AI Prompt Genius", "desc": "AI提示词库创建和管理工具", "logo": "/ai-logos/aipromptgenius.png", "link": "#"},
  {"name": "PromptBase", "desc": "AI Prompt交易平台", "logo": "/ai-logos/promptbase.png", "link": "#"},
  {"name": "AI Prompt Library", "desc": "免费的AI 提示词资源平台", "logo": "/ai-logos/aipromptlib.png", "link": "#"},
  {"name": "Awesome ChatGPT Pro...", "desc": "AI提示词收集和整理工具", "logo": "/ai-logos/awesomechatgpt.png", "link": "#"},
  {"name": "Learning Prompt", "desc": "免费的AI提示词学习平台", "logo": "/ai-logos/learningprompt.png", "link": "#"}
]
</script>

# Ai 提示词指令大全

精选全球前沿 AI 提示词指令与 Prompt 工程平台。

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
