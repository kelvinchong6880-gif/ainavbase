---
title: Ai 搜索引擎大全
description: 探索各大领先的 AI 搜索引擎，快速获取精准信息。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "夸克AI", "desc": "集AI搜索、网盘、文档、创作等功能于一体的应...", "logo": "/ai-logos/quarkai.png", "link": "https://www.bing.com/search?q=%E5%A4%B8%E5%85%8BAI"},
  {"name": "秘塔AI搜索", "desc": "最好用的AI搜索工具，没有广告，直达结果", "logo": "/ai-logos/metaso.png", "link": "https://www.bing.com/search?q=%E7%A7%98%E5%A1%94AI%E6%90%9C%E7%B4%A2"},
  {"name": "Perplexity", "desc": "AI搜索引擎与深度研究工具", "logo": "/ai-logos/perplexity.png", "link": "https://www.bing.com/search?q=Perplexity"},
  {"name": "玻尔", "desc": "新一代科研知识库与AI学术搜索平台", "logo": "/ai-logos/boer.png", "link": "https://www.bing.com/search?q=%E7%8E%BB%E5%B0%94"},
  {"name": "SearchGPT", "desc": "OpenAI最新推出的AI搜索引擎", "logo": "/ai-logos/searchgpt.png", "link": "https://www.bing.com/search?q=SearchGPT"},
  {"name": "AMiner", "desc": "智谱AI推出的大模型学术平台", "logo": "/ai-logos/aminer.png", "link": "https://www.bing.com/search?q=AMiner"},
  {"name": "心流", "desc": "阿里旗下推出的AI搜索助手", "logo": "/ai-logos/xinliu.png", "link": "https://www.bing.com/search?q=%E5%BF%83%E6%B5%81"},
  {"name": "点点", "desc": "小红书推出的 AI 搜索应用，主打生活场景", "logo": "/ai-logos/diandian.png", "link": "https://www.bing.com/search?q=%E7%82%B9%E7%82%B9"},
  {"name": "Devv", "desc": "面向程序员的新一代AI搜索引擎", "logo": "/ai-logos/devv.png", "link": "https://www.bing.com/search?q=Devv"},
  {"name": "知乎直答", "desc": "知乎推出的AI搜索引擎，直达问题答案", "logo": "/ai-logos/zhida.png", "link": "https://www.bing.com/search?q=%E7%9F%A5%E4%B9%8E%E7%9B%B4%E7%AD%94"},
  {"name": "蜜惠检索", "desc": "AI 学术检索与研究辅助工具", "logo": "/ai-logos/mihui.png", "link": "https://www.bing.com/search?q=%E8%9C%9C%E6%83%A0%E6%A3%80%E7%B4%A2"},
  {"name": "纳米AI", "desc": "360推出的新一代超级AI搜索工具", "logo": "/ai-logos/namiai.png", "link": "https://www.bing.com/search?q=%E7%BA%B3%E7%B1%B3AI"},
  {"name": "百度AI探索版", "desc": "百度推出的深度AI搜索引擎", "logo": "/ai-logos/baidutansuo.png", "link": "https://www.bing.com/search?q=%E7%99%BE%E5%BA%A6AI%E6%8E%A2%E7%B4%A2%E7%89%88"},
  {"name": "Felo", "desc": "免费AI智能搜索引擎，支持社交联网搜索和多语...", "logo": "/ai-logos/felo.png", "link": "https://www.bing.com/search?q=Felo"},
  {"name": "天工AI搜索", "desc": "昆仑万维最新推出的结合大模型的AI搜索引擎", "logo": "/ai-logos/tiangongsearch.png", "link": "https://www.bing.com/search?q=%E5%A4%A9%E5%B7%A5AI%E6%90%9C%E7%B4%A2"},
  {"name": "Exa AI", "desc": "专门为AI模型设计的搜索引擎平台", "logo": "/ai-logos/exa.png", "link": "https://www.bing.com/search?q=Exa%20AI"},
  {"name": "博查AI搜索", "desc": "支持多模型的AI搜索引擎", "logo": "/ai-logos/bocha.png", "link": "https://www.bing.com/search?q=%E5%8D%9A%E6%9F%A5AI%E6%90%9C%E7%B4%A2"},
  {"name": "WisPaper", "desc": "复旦团队推出的 AI 学术搜索工具", "logo": "/ai-logos/wispaper.png", "link": "https://www.bing.com/search?q=WisPaper"},
  {"name": "CuspAI", "desc": "剑桥大学推出的材料学专业AI搜索工具", "logo": "/ai-logos/cuspai.png", "link": "https://www.bing.com/search?q=CuspAI"},
  {"name": "MaxAEO", "desc": "AI 搜索可见度监测与优化工具", "logo": "/ai-logos/maxaeo.png", "link": "https://www.bing.com/search?q=MaxAEO"},
  {"name": "SheepGeo", "desc": "国内首个AI GEO (生成式引擎优化) 分析平台", "logo": "/ai-logos/sheepgeo.png", "link": "https://www.bing.com/search?q=SheepGeo"},
  {"name": "博简智慧专利", "desc": "AI专利查新检索与撰写平台", "logo": "/ai-logos/bojian.png", "link": "https://www.bing.com/search?q=%E5%8D%9A%E7%AE%80%E6%99%BA%E6%85%A7%E4%B8%93%E5%88%A9"},
  {"name": "链企AI", "desc": "链企智能推出的AI商业搜索和AI标书写作工具", "logo": "/ai-logos/lianqiai.png", "link": "https://www.bing.com/search?q=%E9%93%BE%E4%BC%81AI"},
  {"name": "360AI搜索", "desc": "360推出的新一代AI搜索引擎", "logo": "/ai-logos/360aisearch.png", "link": "https://www.bing.com/search?q=360AI%E6%90%9C%E7%B4%A2"},
  {"name": "问问小宇宙", "desc": "小宇宙推出的AI搜索产品", "logo": "/ai-logos/wenwen.png", "link": "https://www.bing.com/search?q=%E9%97%AE%E9%97%AE%E5%B0%8F%E5%AE%87%E5%AE%99"},
  {"name": "Dexa AI", "desc": "AI播客搜索工具", "logo": "/ai-logos/dexa.png", "link": "https://www.bing.com/search?q=Dexa%20AI"},
  {"name": "XAnswer", "desc": "支持生成思维导图的免费AI搜索引擎", "logo": "/ai-logos/xanswer.png", "link": "https://www.bing.com/search?q=XAnswer"},
  {"name": "Glean", "desc": "专为职场人设计的AI搜索引擎", "logo": "/ai-logos/glean.png", "link": "https://www.bing.com/search?q=Glean"},
  {"name": "AlphaSense", "desc": "专为金融专业人士设计的AI搜索工具", "logo": "/ai-logos/alphasense.png", "link": "https://www.bing.com/search?q=AlphaSense"},
  {"name": "Globe Explorer", "desc": "结构化AI知识搜索引擎", "logo": "/ai-logos/globe.png", "link": "https://www.bing.com/search?q=Globe%20Explorer"},
  {"name": "Reportify", "desc": "AI投资研究问答搜索引擎", "logo": "/ai-logos/reportify.png", "link": "https://www.bing.com/search?q=Reportify"},
  {"name": "Phind", "desc": "专为开发者设计的AI搜索引擎", "logo": "/ai-logos/phind.png", "link": "https://www.bing.com/search?q=Phind"},
  {"name": "iAsk AI", "desc": "快速准确的AI搜索引擎", "logo": "/ai-logos/iask.png", "link": "https://www.bing.com/search?q=iAsk%20AI"},
  {"name": "Consensus", "desc": "AI科研学术搜索引擎", "logo": "/ai-logos/consensus.png", "link": "https://www.bing.com/search?q=Consensus"},
  {"name": "Komo Search", "desc": "简洁直观的AI搜索引擎", "logo": "/ai-logos/komo.png", "link": "https://www.bing.com/search?q=Komo%20Search"},
  {"name": "Searcholic", "desc": "AI驱动的电子书和文档搜索引擎", "logo": "/ai-logos/searcholic.png", "link": "https://www.bing.com/search?q=Searcholic"},
  {"name": "Andi", "desc": "对话式人工智能搜索引擎", "logo": "/ai-logos/andi.png", "link": "https://www.bing.com/search?q=Andi"},
  {"name": "Songtell", "desc": "AI驱动的音乐百科搜索引擎", "logo": "/ai-logos/songtell.png", "link": "https://www.bing.com/search?q=Songtell"},
  {"name": "ThinkAny", "desc": "新时代的AI搜索引擎", "logo": "/ai-logos/thinkany.png", "link": "https://www.bing.com/search?q=ThinkAny"},
  {"name": "Miku", "desc": "快速精准的AI搜索引擎", "logo": "/ai-logos/miku.png", "link": "https://www.bing.com/search?q=Miku"}
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
