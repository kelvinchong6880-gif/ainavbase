---
title: Ai 设计工具大全
description: 探索 Figma AI、Canva、即时设计等面向 UI/UX 与平面排版的 AI 辅助设计神器。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "Lovart", "desc": "全球首个AI设计Agent", "logo": "/ai-logos/lovart_design.png", "link": "https://www.bing.com/search?q=Lovart"},
  {"name": "绘蛙AI", "desc": "AI电商设计工具", "logo": "/ai-logos/huiwaai.png", "link": "https://www.bing.com/search?q=%E7%BB%98%E8%9B%99AI"},
  {"name": "妙呀", "desc": "阿里潮玩AI平台，一站式潮玩创作", "logo": "/ai-logos/miaoya.png", "link": "https://www.bing.com/search?q=%E5%A6%99%E5%91%80"},
  {"name": "稿定AI", "desc": "一站式AI创作和设计平台", "logo": "/ai-logos/gaodingai.png", "link": "https://www.bing.com/search?q=%E7%A8%BF%E5%AE%9AAI"},
  {"name": "墨刀AI", "desc": "AI秒生原型稿", "logo": "/ai-logos/modaoai.png", "link": "https://www.bing.com/search?q=%E5%A2%A8%E5%88%80AI"},
  {"name": "Holopix AI", "desc": "专为游戏、动漫、插画设计打造的AI设计平台", "logo": "/ai-logos/holopixai.png", "link": "https://www.bing.com/search?q=Holopix%20AI"},
  {"name": "美图设计室", "desc": "AI图像创作和设计平台", "logo": "/ai-logos/meitudesign.png", "link": "https://www.bing.com/search?q=%E7%BE%8E%E5%9B%BE%E8%AE%BE%E8%AE%A1%E5%AE%A4"},
  {"name": "135 AI排版", "desc": "公众号AI图文排版和智能文案生成工具", "logo": "/ai-logos/135ai.png", "link": "https://www.bing.com/search?q=135%20AI%E6%8E%92%E7%89%88"},
  {"name": "堆友AI", "desc": "专为设计师打造的AI设计服务平台", "logo": "/ai-logos/duiyouai.png", "link": "https://www.bing.com/search?q=%E5%A0%86%E5%8F%8BAI"},
  {"name": "OJO", "desc": "全球首个 AI 设计 Agent 团队工作台", "logo": "/ai-logos/ojo.png", "link": "https://www.bing.com/search?q=OJO"},
  {"name": "Figma AI", "desc": "Figma推出的原生AI设计工具", "logo": "/ai-logos/figmaai.png", "link": "https://www.bing.com/search?q=Figma%20AI"},
  {"name": "Seede AI", "desc": "面向普通人的 AI 原生设计工具", "logo": "/ai-logos/seedeai.png", "link": "https://www.bing.com/search?q=Seede%20AI"},
  {"name": "Pixso AI", "desc": "Pixso推出的AI设计工具", "logo": "/ai-logos/pixsoai.png", "link": "https://www.bing.com/search?q=Pixso%20AI"},
  {"name": "Wegic", "desc": "AI网页设计和建站开发工具", "logo": "/ai-logos/wegic.png", "link": "https://www.bing.com/search?q=Wegic"},
  {"name": "Recraft AI", "desc": "免费无限AI画板，生成高质量矢量艺术画、图标...", "logo": "/ai-logos/recraftai.png", "link": "https://www.bing.com/search?q=Recraft%20AI"},
  {"name": "星流AI", "desc": "一站式 AI 设计与创作工具", "logo": "/ai-logos/xingliuai.png", "link": "https://www.bing.com/search?q=%E6%98%9F%E6%B5%81AI"},
  {"name": "Stitch", "desc": "Google Labs 推出的 AI 原生设计工具", "logo": "/ai-logos/stitch.png", "link": "https://www.bing.com/search?q=Stitch"},
  {"name": "Miora", "desc": "腾讯推出的 AI 原生设计协作工具", "logo": "/ai-logos/miora.png", "link": "https://www.bing.com/search?q=Miora"},
  {"name": "Ardot", "desc": "腾讯推出的 AI 智能设计工具", "logo": "/ai-logos/ardot.png", "link": "https://www.bing.com/search?q=Ardot"},
  {"name": "创客贴AI", "desc": "AI辅助的智能在线设计工具", "logo": "/ai-logos/chuangketie.png", "link": "https://www.bing.com/search?q=%E5%88%9B%E5%AE%A2%E8%B4%B4AI"},
  {"name": "Open Design", "desc": "开源本地优先的 AI 设计工作空间", "logo": "/ai-logos/opendesign.png", "link": "https://www.bing.com/search?q=Open%20Design"},
  {"name": "Onlook", "desc": "开源AI视觉编辑工具，设计修改自动同步代码", "logo": "/ai-logos/onlook.png", "link": "https://www.bing.com/search?q=Onlook"},
  {"name": "Ribbi", "desc": "专为设计师打造的自进化创意 AI Agent", "logo": "/ai-logos/ribbi.png", "link": "https://www.bing.com/search?q=Ribbi"},
  {"name": "Tavafa塔维法", "desc": "PS+AI图片处理平台", "logo": "/ai-logos/tavafa.png", "link": "https://www.bing.com/search?q=Tavafa%E5%A1%94%E7%BB%B4%E6%B3%95"},
  {"name": "Interiorize", "desc": "专注于空间改造的 AI 室内设计工具", "logo": "/ai-logos/interiorize.png", "link": "https://www.bing.com/search?q=Interiorize"},
  {"name": "QuiverAI", "desc": "AI矢量图形生成工具，输出可编辑的 SVG 代码", "logo": "/ai-logos/quiverai.png", "link": "https://www.bing.com/search?q=QuiverAI"},
  {"name": "GemDesign", "desc": "AI原生高保真原型设计工具", "logo": "/ai-logos/gemdesign.png", "link": "https://www.bing.com/search?q=GemDesign"},
  {"name": "Pic Copilot", "desc": "阿里国际推出的AI电商设计工具", "logo": "/ai-logos/piccopilot.png", "link": "https://www.bing.com/search?q=Pic%20Copilot"},
  {"name": "魔力工作室", "desc": "Canva可画推出的一站式AI创作套件", "logo": "/ai-logos/canvamagic.png", "link": "https://www.bing.com/search?q=%E9%AD%94%E5%8A%9B%E5%B7%A5%E4%BD%9C%E5%AE%A4"},
  {"name": "码上有创意", "desc": "支付宝推出的AI设计工具，面向商家提供电商设...", "logo": "/ai-logos/mashangyouchuangyi.png", "link": "https://www.bing.com/search?q=%E7%A0%81%E4%B8%8A%E6%9C%89%E5%88%9B%E6%84%8F"},
  {"name": "七色米AI", "desc": "AI 智能营销内容创作平台", "logo": "/ai-logos/qisemi.png", "link": "https://www.bing.com/search?q=%E4%B8%83%E8%89%B2%E7%B1%B3AI"},
  {"name": "爱设计", "desc": "AI在线设计平台，提供多端在线拖拽设计工具", "logo": "/ai-logos/aisheji.png", "link": "https://www.bing.com/search?q=%E7%88%B1%E8%AE%BE%E8%AE%A1"},
  {"name": "PagePop", "desc": "一站式全能AI内容创作和设计平台", "logo": "/ai-logos/pagepop.png", "link": "https://www.bing.com/search?q=PagePop"},
  {"name": "小墨度编辑器", "desc": "行业首创的AI公众号排版工具，30s搞定推文排...", "logo": "/ai-logos/xiaomodu.png", "link": "https://www.bing.com/search?q=%E5%B0%8F%E5%A2%A8%E5%BA%A6%E7%BC%96%E8%BE%91%E5%99%A8"},
  {"name": "美间AI", "desc": "新一代AI画布式创意设计平台", "logo": "/ai-logos/meijianai.png", "link": "https://www.bing.com/search?q=%E7%BE%8E%E9%97%B4AI"},
  {"name": "Calicat", "desc": "ProcessOn团队推出的一站式产研协作平台", "logo": "/ai-logos/calicat.png", "link": "https://www.bing.com/search?q=Calicat"},
  {"name": "Microsoft Designer", "desc": "微软推出的在线设计海报和宣传图工具", "logo": "/ai-logos/microsoftdesigner.png", "link": "https://www.bing.com/search?q=Microsoft%20Designer"},
  {"name": "UXbot", "desc": "AI产品设计工具，一键生成UI与交互式模型", "logo": "/ai-logos/uxbot.png", "link": "https://www.bing.com/search?q=UXbot"},
  {"name": "燕雀光年", "desc": "AI LOGO设计工具", "logo": "/ai-logos/yanqueguangnian.png", "link": "https://www.bing.com/search?q=%E7%87%95%E9%9B%80%E5%85%89%E5%B9%B4"},
  {"name": "标小智LOGO生成器", "desc": "AI Logo设计平台，一键生成企业Logo", "logo": "/ai-logos/biaoxiaozhi.png", "link": "https://www.bing.com/search?q=%E6%A0%87%E5%B0%8F%E6%99%BALOGO%E7%94%9F%E6%88%90%E5%99%A8"}
]
</script>

# Ai 设计工具大全

精选全球前沿 AI 辅助设计、海报生成、UI/UX 原型与自动化排版工具。

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
