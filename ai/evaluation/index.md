---
title: Ai 模型评测大全
description: 探索各大领先的 AI 模型评测平台与基准测试榜单。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "MagicArena", "desc": "字节推出的视觉生成模型对战...", "logo": "/ai-logos/magicarena.png", "link": "https://www.bing.com/search?q=MagicArena"},
  {"name": "MMLU", "desc": "大规模多任务语言理解基准", "logo": "/ai-logos/mmlu.png", "link": "https://www.bing.com/search?q=MMLU"},
  {"name": "Open LLM Leaderboard", "desc": "Hugging Face推出的开源大模...", "logo": "/ai-logos/openllmleaderboard.png", "link": "https://www.bing.com/search?q=Open%20LLM%20Leaderboard"},
  {"name": "C-Eval", "desc": "一个全面的中文基础模型评估...", "logo": "/ai-logos/ceval.png", "link": "https://www.bing.com/search?q=C-Eval"},
  {"name": "FlagEval", "desc": "智源研究院推出的FlagEval (...", "logo": "/ai-logos/flageval.png", "link": "https://www.bing.com/search?q=FlagEval"},
  {"name": "SuperCLUE", "desc": "中文通用大模型综合性测评基准", "logo": "/ai-logos/superclue.png", "link": "https://www.bing.com/search?q=SuperCLUE"},
  {"name": "AGI-Eval", "desc": "AI大模型评测社区", "logo": "/ai-logos/agieval.png", "link": "https://www.bing.com/search?q=AGI-Eval"},
  {"name": "OpenCompass", "desc": "上海人工智能实验室推出的大...", "logo": "/ai-logos/opencompass.png", "link": "https://www.bing.com/search?q=OpenCompass"},
  {"name": "CMMLU", "desc": "一个综合性的大模型中文评估...", "logo": "/ai-logos/cmmlu.png", "link": "https://www.bing.com/search?q=CMMLU"},
  {"name": "MMBench", "desc": "全方位的多模态大模型能力评...", "logo": "/ai-logos/mmbench.png", "link": "https://www.bing.com/search?q=MMBench"},
  {"name": "HELM", "desc": "斯坦福大学推出的大模型评测...", "logo": "/ai-logos/helm.png", "link": "https://www.bing.com/search?q=HELM"},
  {"name": "LMArena", "desc": "AI模型评估平台", "logo": "/ai-logos/lmarena.png", "link": "https://www.bing.com/search?q=LMArena"},
  {"name": "LLMEval3", "desc": "由复旦大学NLP实验室推出的...", "logo": "/ai-logos/llmeval3.png", "link": "https://www.bing.com/search?q=LLMEval3"},
  {"name": "H2O EvalGPT", "desc": "H2O.ai推出的基于Elo评级方法...", "logo": "/ai-logos/h2oevalgpt.png", "link": "https://www.bing.com/search?q=H2O%20EvalGPT"},
  {"name": "PubMedQA", "desc": "生物医学研究问答数据集和模...", "logo": "/ai-logos/pubmedqa.png", "link": "https://www.bing.com/search?q=PubMedQA"}
]
</script>

# Ai 模型评测大全

精选全球前沿 AI 模型评测平台和性能榜单。

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
