---
title: Ai 搜索引擎大全
description: 探索各大领先的 AI 搜索引擎，快速获取精准信息。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "夸克AI", "desc": "集AI搜索、网盘、文档、创作等功能于一体的应...", "logo": "/ai-logos/quarkai.png", "link": "#"},
  {"name": "秘塔AI搜索", "desc": "最好用的AI搜索工具，没有广告，直达结果", "logo": "/ai-logos/metaso.png", "link": "#"},
  {"name": "Perplexity", "desc": "AI搜索引擎与深度研究工具", "logo": "/ai-logos/perplexity.png", "link": "#"},
  {"name": "玻尔", "desc": "新一代科研知识库与AI学术搜索平台", "logo": "/ai-logos/boer.png", "link": "#"},
  {"name": "SearchGPT", "desc": "OpenAI最新推出的AI搜索引擎", "logo": "/ai-logos/searchgpt.png", "link": "#"},
  {"name": "AMiner", "desc": "智谱AI推出的大模型学术平台", "logo": "/ai-logos/aminer.png", "link": "#"},
  {"name": "心流", "desc": "阿里旗下推出的AI搜索助手", "logo": "/ai-logos/xinliu.png", "link": "#"},
  {"name": "点点", "desc": "小红书推出的 AI 搜索应用，主打生活场景", "logo": "/ai-logos/diandian.png", "link": "#"},
  {"name": "Devv", "desc": "面向程序员的新一代AI搜索引擎", "logo": "/ai-logos/devv.png", "link": "#"},
  {"name": "知乎直答", "desc": "知乎推出的AI搜索引擎，直达问题答案", "logo": "/ai-logos/zhida.png", "link": "#"},
  {"name": "蜜惠检索", "desc": "AI 学术检索与研究辅助工具", "logo": "/ai-logos/mihui.png", "link": "#"},
  {"name": "纳米AI", "desc": "360推出的新一代超级AI搜索工具", "logo": "/ai-logos/namiai.png", "link": "#"},
  {"name": "百度AI探索版", "desc": "百度推出的深度AI搜索引擎", "logo": "/ai-logos/baidutansuo.png", "link": "#"},
  {"name": "Felo", "desc": "免费AI智能搜索引擎，支持社交联网搜索和多语...", "logo": "/ai-logos/felo.png", "link": "#"},
  {"name": "天工AI搜索", "desc": "昆仑万维最新推出的结合大模型的AI搜索引擎", "logo": "/ai-logos/tiangongsearch.png", "link": "#"},
  {"name": "Exa AI", "desc": "专门为AI模型设计的搜索引擎平台", "logo": "/ai-logos/exa.png", "link": "#"},
  {"name": "博查AI搜索", "desc": "支持多模型的AI搜索引擎", "logo": "/ai-logos/bocha.png", "link": "#"},
  {"name": "WisPaper", "desc": "复旦团队推出的 AI 学术搜索工具", "logo": "/ai-logos/wispaper.png", "link": "#"},
  {"name": "CuspAI", "desc": "剑桥大学推出的材料学专业AI搜索工具", "logo": "/ai-logos/cuspai.png", "link": "#"},
  {"name": "MaxAEO", "desc": "AI 搜索可见度监测与优化工具", "logo": "/ai-logos/maxaeo.png", "link": "#"},
  {"name": "SheepGeo", "desc": "国内首个AI GEO (生成式引擎优化) 分析平台", "logo": "/ai-logos/sheepgeo.png", "link": "#"},
  {"name": "博简智慧专利", "desc": "AI专利查新检索与撰写平台", "logo": "/ai-logos/bojian.png", "link": "#"},
  {"name": "链企AI", "desc": "链企智能推出的AI商业搜索和AI标书写作工具", "logo": "/ai-logos/lianqiai.png", "link": "#"},
  {"name": "360AI搜索", "desc": "360推出的新一代AI搜索引擎", "logo": "/ai-logos/360aisearch.png", "link": "#"},
  {"name": "问问小宇宙", "desc": "小宇宙推出的AI搜索产品", "logo": "/ai-logos/wenwen.png", "link": "#"},
  {"name": "Dexa AI", "desc": "AI播客搜索工具", "logo": "/ai-logos/dexa.png", "link": "#"},
  {"name": "XAnswer", "desc": "支持生成思维导图的免费AI搜索引擎", "logo": "/ai-logos/xanswer.png", "link": "#"},
  {"name": "Glean", "desc": "专为职场人设计的AI搜索引擎", "logo": "/ai-logos/glean.png", "link": "#"},
  {"name": "AlphaSense", "desc": "专为金融专业人士设计的AI搜索工具", "logo": "/ai-logos/alphasense.png", "link": "#"},
  {"name": "Globe Explorer", "desc": "结构化AI知识搜索引擎", "logo": "/ai-logos/globe.png", "link": "#"},
  {"name": "Reportify", "desc": "AI投资研究问答搜索引擎", "logo": "/ai-logos/reportify.png", "link": "#"},
  {"name": "Phind", "desc": "专为开发者设计的AI搜索引擎", "logo": "/ai-logos/phind.png", "link": "#"},
  {"name": "iAsk AI", "desc": "快速准确的AI搜索引擎", "logo": "/ai-logos/iask.png", "link": "#"},
  {"name": "Consensus", "desc": "AI科研学术搜索引擎", "logo": "/ai-logos/consensus.png", "link": "#"},
  {"name": "Komo Search", "desc": "简洁直观的AI搜索引擎", "logo": "/ai-logos/komo.png", "link": "#"},
  {"name": "Searcholic", "desc": "AI驱动的电子书和文档搜索引擎", "logo": "/ai-logos/searcholic.png", "link": "#"},
  {"name": "Andi", "desc": "对话式人工智能搜索引擎", "logo": "/ai-logos/andi.png", "link": "#"},
  {"name": "Songtell", "desc": "AI驱动的音乐百科搜索引擎", "logo": "/ai-logos/songtell.png", "link": "#"},
  {"name": "ThinkAny", "desc": "新时代的AI搜索引擎", "logo": "/ai-logos/thinkany.png", "link": "#"},
  {"name": "Miku", "desc": "快速精准的AI搜索引擎", "logo": "/ai-logos/miku.png", "link": "#"}
]
</script>

# Ai 搜索引擎大全

精选全球前沿 AI 搜索引擎工具。

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
