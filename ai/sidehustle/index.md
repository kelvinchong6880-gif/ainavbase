---
title: Ai 副业工具大全
description: 探索能够帮助你实现流量变现、自媒体运营与副业搞钱的 AI 效率工具。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "CakeGrowth", "desc": "首个专注 AI 应用的一站式联盟...", "logo": "/ai-logos/cakegrowth.png", "link": "#"},
  {"name": "模觉", "desc": "AI数据众包与专家服务平台", "logo": "/ai-logos/mojue.png", "link": "#"},
  {"name": "Linktree", "desc": "链接聚合工具，支持多链接整...", "logo": "/ai-logos/linktree.png", "link": "#"},
  {"name": "Bitly", "desc": "链接管理平台与 URL 短链接服...", "logo": "/ai-logos/bitly.png", "link": "#"},
  {"name": "PartnerStack", "desc": "领先的合作伙伴生态系统平台", "logo": "/ai-logos/partnerstack.png", "link": "#"},
  {"name": "impact.com", "desc": "AI 原生合作伙伴关系管理平台", "logo": "/ai-logos/impact.png", "link": "#"},
  {"name": "微信公众平台", "desc": "腾讯推出的官方内容创作与服...", "logo": "/ai-logos/mpweixin.png", "link": "#"},
  {"name": "头条号", "desc": "字节跳动推出的内容创作平台", "logo": "/ai-logos/toutiaohao.png", "link": "#"},
  {"name": "新榜", "desc": "新媒体数据服务平台", "logo": "/ai-logos/newrank.png", "link": "#"},
  {"name": "稀土掘金", "desc": "领先的技术内容社区与开发者...", "logo": "/ai-logos/juejin.png", "link": "#"},
  {"name": "知乎", "desc": "内容创作者的一站式创作服务...", "logo": "/ai-logos/zhihu.png", "link": "#"},
  {"name": "CSDN", "desc": "专业的开发者社区", "logo": "/ai-logos/csdn.png", "link": "#"},
  {"name": "百家号", "desc": "百度推出的内容创作平台，集...", "logo": "/ai-logos/baijiahao.png", "link": "#"},
  {"name": "小红书创作服务平台", "desc": "一站式创作者服务工作平台", "logo": "/ai-logos/xiaohongshu.png", "link": "#"},
  {"name": "小报童", "desc": "flomo 团队推出的付费内容服...", "logo": "/ai-logos/xiaobot.png", "link": "#"},
  {"name": "知识星球", "desc": "内容创作者的知识社群运营工具", "logo": "/ai-logos/zsxq.png", "link": "#"},
  {"name": "小鹅通", "desc": "专注私域运营的一站式SaaS平台", "logo": "/ai-logos/xiaoe.png", "link": "#"}
]
</script>

# Ai 副业工具大全

发掘各类能够帮助你实现流量变现、自媒体运营与副业搞钱的 AI 效率工具和平台。

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
