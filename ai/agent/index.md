---
title: Ai 智能体大全
description: 探索各类前沿 AI 智能体、Agent 助手与自动化工作流，体验真正的 AI 原生生产力。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "Loomy", "desc": "桌面端 AI 智能体，每天免费5000积分！", "logo": "/ai-logos/loomy_agent.png", "link": "#"},
  {"name": "Lovart", "desc": "全球首个 AI 设计智能体", "logo": "/ai-logos/lovart.png", "link": "#"},
  {"name": "Seko", "desc": "首个创编一体的AI视频创作Agent", "logo": "/ai-logos/seko_agent.png", "link": "#"},
  {"name": "小云雀", "desc": "小云雀 Seedance2.5 正式上线", "logo": "/ai-logos/xiaoyunque_agent.png", "link": "#"},
  {"name": "爱派AiPy", "desc": "本地Manus、国内能用、内网能用，开源免费", "logo": "/ai-logos/aipy.png", "link": "#"},
  {"name": "Atoms", "desc": "第一支自动构建真实业务的 AI 团队", "logo": "/ai-logos/atoms.png", "link": "#"},
  {"name": "WorkBuddy", "desc": "腾讯云推出的AI原生桌面智能体工作台", "logo": "/ai-logos/workbuddy.png", "link": "#"},
  {"name": "WaClaw", "desc": "阿里续蛙团队推出的电商垂直 AI Agent", "logo": "/ai-logos/waclaw.png", "link": "#"},
  {"name": "马上飞", "desc": "一句话生成微信小程序、APP、H5网页", "logo": "/ai-logos/mashangfei.png", "link": "#"},
  {"name": "ArkClaw", "desc": "火山引擎推出的云端托管版OpenClaw服务", "logo": "/ai-logos/arkclaw.png", "link": "#"},
  {"name": "扣子Coze", "desc": "免费全能的AI办公智能体", "logo": "/ai-logos/coze.png", "link": "#"},
  {"name": "讯飞星辰Agent", "desc": "科大讯飞推出的AI智能体开发平台", "logo": "/ai-logos/xunfeixingchen.png", "link": "#"},
  {"name": "01Agent", "desc": "AI图文创作智能体，支持生成、排版、编辑、发...", "logo": "/ai-logos/01agent.png", "link": "#"},
  {"name": "TraeWork", "desc": "字节跳动推出的 AI 原生工作台", "logo": "/ai-logos/traework.png", "link": "#"},
  {"name": "堆友Agent", "desc": "集成大厂专家设计 Skill 的AI设计智能体", "logo": "/ai-logos/duiyouagent.png", "link": "#"},
  {"name": "AutoClaw", "desc": "智谱推出的国内首个一键安装本地版OpenClaw", "logo": "/ai-logos/autoclaw.png", "link": "#"},
  {"name": "OpenClaw", "desc": "开源免费的个人 AI 助手", "logo": "/ai-logos/openclaw.png", "link": "#"},
  {"name": "Tabbit", "desc": "美团光年之外推出的AI原生浏览器", "logo": "/ai-logos/tabbit.png", "link": "#"},
  {"name": "切问学术", "desc": "FudanNLP团队推出的AI学术智能体", "logo": "/ai-logos/qiewen.png", "link": "#"},
  {"name": "豆包工作", "desc": "字节跳动推出的 AI Agent 办公产品", "logo": "/ai-logos/doubaowork.png", "link": "#"},
  {"name": "QwenWork", "desc": "千问办公国际版，一站式AI生产力平台", "logo": "/ai-logos/qwenwork.png", "link": "#"},
  {"name": "QwenPaw", "desc": "阿里 AgentScope 团队开源的个人 AI 智能体工...", "logo": "/ai-logos/qwenpaw.png", "link": "#"},
  {"name": "AionClaw", "desc": "真正能动手交付成品的桌面 AI 智能体，每日登...", "logo": "/ai-logos/aionclaw.png", "link": "#"},
  {"name": "Tokera AI", "desc": "做账号、看竞品、定策略、出内容的一站式 AI ...", "logo": "/ai-logos/tokera.png", "link": "#"},
  {"name": "Floatboat", "desc": "专为“一人公司”打造的 AI Agent 原生工作空间", "logo": "/ai-logos/floatboat.png", "link": "#"},
  {"name": "Flowith", "desc": "瀑布式AI智能体工具", "logo": "/ai-logos/flowith.png", "link": "#"},
  {"name": "千问办公", "desc": "阿里推出的一站式 AI Agent 办公工具", "logo": "/ai-logos/qianwenwork.png", "link": "#"},
  {"name": "ByteCP", "desc": "曲尺AI推出的AI办公智能体", "logo": "/ai-logos/bytecp.png", "link": "#"},
  {"name": "TipKay", "desc": "AI内容创作运营平台，多 Agent 桌面 AI 客户端", "logo": "/ai-logos/tipkay.png", "link": "#"},
  {"name": "纳米Work", "desc": "360旗下纳米团队推出的 AI 办公智能体", "logo": "/ai-logos/namiwork.png", "link": "#"},
  {"name": "KroWork", "desc": "快手推出的桌面端通用 AI 智能体", "logo": "/ai-logos/krowork.png", "link": "#"},
  {"name": "觅游", "desc": "美团推出的 AI 原生 Agent 社区", "logo": "/ai-logos/miyou.png", "link": "#"},
  {"name": "虾345", "desc": "面向AI Agent生态的综合型导航与信息聚合平台", "logo": "/ai-logos/xia345.png", "link": "#"},
  {"name": "Sophclaw", "desc": "Sophnet 算能云算力平台推出的全能型 AI 数字...", "logo": "/ai-logos/sophclaw.png", "link": "#"},
  {"name": "LobsterAI", "desc": "网易推出的全场景办公助手 Agent", "logo": "/ai-logos/lobsterai.png", "link": "#"},
  {"name": "Nile", "desc": "面向 Agent 时代的 AI 原生电商分发平台", "logo": "/ai-logos/nile.png", "link": "#"},
  {"name": "Kevvee", "desc": "全球首个 AI 出海内容 GTM 策略 Agent", "logo": "/ai-logos/kevvee.png", "link": "#"},
  {"name": "Matrix", "desc": "超长时间自动化运行的主动式多 Agent 协作平台", "logo": "/ai-logos/matrix.png", "link": "#"},
  {"name": "Manus", "desc": "蝴蝶效应公司推出的首款自主通用AI Agent", "logo": "/ai-logos/manus.png", "link": "#"},
  {"name": "腾讯Marvis", "desc": "腾讯应用宝团队推出的操作系统级 AI 助手", "logo": "/ai-logos/marvis.png", "link": "#"}
]
</script>

# Ai 智能体大全

精选全球前沿 AI 智能体 (Agent)、桌面助手与自动化工作流平台。

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
