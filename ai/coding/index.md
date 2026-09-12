---
title: Ai 编程工具大全
description: 探索各类前沿 AI 编程工具、IDE 智能体与代码辅助生成神器，提升研发效能。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "TRAE", "desc": "字节旗下AI编程工具，让开发更智能，办公更高...", "logo": "/ai-logos/trae.png", "link": "https://www.bing.com/search?q=TRAE"},
  {"name": "秒哒", "desc": "无代码AI应用开发平台，一句话做应用", "logo": "/ai-logos/miaoda.png", "link": "https://www.bing.com/search?q=%E7%A7%92%E5%93%92"},
  {"name": "码上飞", "desc": "免费生成小程序/APP/网页，一句话生成任意应用", "logo": "/ai-logos/mashangfei_coding.png", "link": "https://www.bing.com/search?q=%E7%A0%81%E4%B8%8A%E9%A3%9E"},
  {"name": "代码小浣熊", "desc": "商汤科技推出的免费AI编程助手", "logo": "/ai-logos/xiaohuanxiong_coding.png", "link": "https://www.bing.com/search?q=%E4%BB%A3%E7%A0%81%E5%B0%8F%E6%B5%A3%E7%86%8A"},
  {"name": "Codex", "desc": "OpenAI 推出的 AI 编程智能体", "logo": "/ai-logos/codex.png", "link": "https://www.bing.com/search?q=Codex"},
  {"name": "Claude Code", "desc": "Anthropic 推出的AI编程工具", "logo": "/ai-logos/claudecode.png", "link": "https://www.bing.com/search?q=Claude%20Code"},
  {"name": "Agent.Space", "desc": "面向 AI 编程 Agent 的云端工作空间", "logo": "/ai-logos/agentspace.png", "link": "https://www.bing.com/search?q=Agent.Space"},
  {"name": "Qoder", "desc": "阿里巴巴推出的 AI Agentic 编程工具", "logo": "/ai-logos/qoder.png", "link": "https://www.bing.com/search?q=Qoder"},
  {"name": "OpenCode", "desc": "开源 AI 编程工具，Claude Code 最佳平替", "logo": "/ai-logos/opencode.png", "link": "https://www.bing.com/search?q=OpenCode"},
  {"name": "Kimi Code", "desc": "Kimi 专为开发者推出的AI编程工具", "logo": "/ai-logos/kimicode.png", "link": "https://www.bing.com/search?q=Kimi%20Code"},
  {"name": "Kilo Code", "desc": "开源的 AI 编程扩展插件", "logo": "/ai-logos/kilocode.png", "link": "https://www.bing.com/search?q=Kilo%20Code"},
  {"name": "Google Antigravity", "desc": "谷歌推出的 AI IDE 编程智能体", "logo": "/ai-logos/antigravity.png", "link": "https://www.bing.com/search?q=Google%20Antigravity"},
  {"name": "Kiro", "desc": "亚马逊公司推出的 AI IDE", "logo": "/ai-logos/kiro.png", "link": "https://www.bing.com/search?q=Kiro"},
  {"name": "Cursor", "desc": "AI代码编辑器，快速进行编程和软件开发", "logo": "/ai-logos/cursor.png", "link": "https://www.bing.com/search?q=Cursor"},
  {"name": "Cline", "desc": "开源免费的 AI 编程智能体", "logo": "/ai-logos/cline.png", "link": "https://www.bing.com/search?q=Cline"},
  {"name": "MiMo Code", "desc": "小米大模型团队开源的新一代 AI 编程助手", "logo": "/ai-logos/mimocode.png", "link": "https://www.bing.com/search?q=MiMo%20Code"},
  {"name": "YouWare", "desc": "一站式 AI 编程社区与开发平台", "logo": "/ai-logos/youware.png", "link": "https://www.bing.com/search?q=YouWare"},
  {"name": "ZCode", "desc": "智谱推出的轻量级AI IDE编程工具", "logo": "/ai-logos/zcode.png", "link": "https://www.bing.com/search?q=ZCode"},
  {"name": "CodeBuddy IDE", "desc": "腾讯推出的全栈开发AI IDE", "logo": "/ai-logos/codebuddy_ide.png", "link": "https://www.bing.com/search?q=CodeBuddy%20IDE"},
  {"name": "Lovable", "desc": "全栈AI编程工具，一句话构建网站应用", "logo": "/ai-logos/lovable.png", "link": "https://www.bing.com/search?q=Lovable"},
  {"name": "CatPaw", "desc": "美团推出的 AI IDE 编程工具", "logo": "/ai-logos/catpaw.png", "link": "https://www.bing.com/search?q=CatPaw"},
  {"name": "Augment Code", "desc": "AI编程辅助工具，专为大型代码库设计", "logo": "/ai-logos/augmentcode.png", "link": "https://www.bing.com/search?q=Augment%20Code"},
  {"name": "AgnesCode", "desc": "Agnes AI 推出的桌面端 AI 编程工作台", "logo": "/ai-logos/agnescode.png", "link": "https://www.bing.com/search?q=AgnesCode"},
  {"name": "MonkeyCode", "desc": "长亭科技开源的 AI 编程助手与企业级开发平台", "logo": "/ai-logos/monkeycode.png", "link": "https://www.bing.com/search?q=MonkeyCode"},
  {"name": "通义灵码", "desc": "阿里推出的免费AI编程工具，基于通义大模型", "logo": "/ai-logos/tongyilingma.png", "link": "https://www.bing.com/search?q=%E9%80%9A%E4%B9%89%E7%81%B5%E7%A0%81"},
  {"name": "GitHub Copilot", "desc": "GitHub推出的AI编程工具", "logo": "/ai-logos/githubcopilot.png", "link": "https://www.bing.com/search?q=GitHub%20Copilot"},
  {"name": "Firebase Studio", "desc": "谷歌推出的AI编程工具，一站式开发全栈应用", "logo": "/ai-logos/firebasestudio.png", "link": "https://www.bing.com/search?q=Firebase%20Studio"},
  {"name": "Windsurf", "desc": "Codeium公司推出的AI编程工具", "logo": "/ai-logos/windsurf.png", "link": "https://www.bing.com/search?q=Windsurf"},
  {"name": "Bolt.new", "desc": "StackBlitz 推出的全栈AI代码工具，可以看作 Art...", "logo": "/ai-logos/boltnew.png", "link": "https://www.bing.com/search?q=Bolt.new"},
  {"name": "InfCode", "desc": "词元无限推出的企业级AI编程工具", "logo": "/ai-logos/infcode.png", "link": "https://www.bing.com/search?q=InfCode"},
  {"name": "CodeFlicker", "desc": "快手推出的AI原生IDE编程工具", "logo": "/ai-logos/codeflicker.png", "link": "https://www.bing.com/search?q=CodeFlicker"},
  {"name": "Clacky AI", "desc": "AI编程工具，打造L3级的Coding Studio", "logo": "/ai-logos/clackyai.png", "link": "https://www.bing.com/search?q=Clacky%20AI"},
  {"name": "Replit Agent", "desc": "AI初创公司Replit推出的AI编程工具", "logo": "/ai-logos/replitagent.png", "link": "https://www.bing.com/search?q=Replit%20Agent"},
  {"name": "Warp Code", "desc": "Warp推出的AI编程工具", "logo": "/ai-logos/warpcode.png", "link": "https://www.bing.com/search?q=Warp%20Code"},
  {"name": "CodeWhisperer", "desc": "亚马逊推出的免费AI编程助手", "logo": "/ai-logos/codewhisperer.png", "link": "https://www.bing.com/search?q=CodeWhisperer"},
  {"name": "Zread", "desc": "专为开发者设计的AI源码解读产品", "logo": "/ai-logos/zread.png", "link": "https://www.bing.com/search?q=Zread"},
  {"name": "Junie", "desc": "JetBrains 推出的 AI 编程助手", "logo": "/ai-logos/junie.png", "link": "https://www.bing.com/search?q=Junie"},
  {"name": "CodeBuddy", "desc": "腾讯推出的AI编程助手", "logo": "/ai-logos/codebuddy.png", "link": "https://www.bing.com/search?q=CodeBuddy"},
  {"name": "Qodo", "desc": "(原CodiumAI) AI开发平台", "logo": "/ai-logos/qodo.png", "link": "https://www.bing.com/search?q=Qodo"},
  {"name": "iFlow CLI", "desc": "心流AI推出的免费终端 AI 智能体", "logo": "/ai-logos/iflowcli.png", "link": "https://www.bing.com/search?q=iFlow%20CLI"}
]
</script>

# Ai 编程工具大全

精选全球前沿 AI 编程工具、IDE 智能体与代码辅助生成神器，提升研发效能。

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
