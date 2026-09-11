---
title: Ai 训练模型大全
description: 探索各大领先的 AI 训练模型与大模型库。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "讯飞星辰MaaS", "desc": "一站式AI大模型体验、调用、部署、精调平台", "logo": "/ai-logos/xingchenmaas.png", "link": "#"},
  {"name": "Muse", "desc": "谷歌推出的图像生成与编辑模型", "logo": "/ai-logos/muse.png", "link": "#"},
  {"name": "Cherry Studio", "desc": "开源全能 AI 客户端助手", "logo": "/ai-logos/cherrystudio.png", "link": "#"},
  {"name": "Ollama", "desc": "本地运行Llama和其他大语言模型", "logo": "/ai-logos/ollama.png", "link": "#"},
  {"name": "AnythingLLM", "desc": "开源的全栈 AI 客户端，支持本地部署和API集成", "logo": "/ai-logos/anythingllm.png", "link": "#"},
  {"name": "Chatbox AI", "desc": "开源的AI客户端助手，支持多种主流AI模型", "logo": "/ai-logos/chatbox.png", "link": "#"},
  {"name": "Seed", "desc": "字节跳动 Seed 团队推出的多模态 AI 视频生成...", "logo": "/ai-logos/seed.png", "link": "#"},
  {"name": "魔搭社区", "desc": "阿里达摩院推出的AI模型社区，超过300+开源A...", "logo": "/ai-logos/modelscope.png", "link": "#"},
  {"name": "豆包大模型", "desc": "字节跳动推出的AI大模型家族，包括视频生成、...", "logo": "/ai-logos/doubaomodel.png", "link": "#"},
  {"name": "Dataify", "desc": "数据采集API、高质量数据集、代理资源服务一...", "logo": "/ai-logos/dataify.png", "link": "#"},
  {"name": "无阶未来", "desc": "AI应用与弹性算网平台", "logo": "/ai-logos/wujieweilai.png", "link": "#"},
  {"name": "AutoGPT", "desc": "爆火的实现GPT-4完全自主的实验性开源项目，...", "logo": "/ai-logos/autogpt.png", "link": "#"},
  {"name": "Jan", "desc": "本地运行大模型并进行AI对话的工具，免费开源", "logo": "/ai-logos/jan.png", "link": "#"},
  {"name": "AgentGPT", "desc": "在浏览器中组装、配置和部署自主人工智能的开...", "logo": "/ai-logos/agentgpt.png", "link": "#"},
  {"name": "OpenBMB", "desc": "清华团队支持发起的大规模预训练语言模型库与...", "logo": "/ai-logos/openbmb.png", "link": "#"},
  {"name": "Llama 3", "desc": "Meta最新开源推出的新一代大模型", "logo": "/ai-logos/llama3.png", "link": "#"},
  {"name": "Gemma", "desc": "谷歌推出的新一代轻量级开放模型", "logo": "/ai-logos/gemma.png", "link": "#"},
  {"name": "GPT-4o", "desc": "OpenAI最新发布的多模态AI大模型，可自然流...", "logo": "/ai-logos/gpt4o.png", "link": "#"},
  {"name": "腾讯混元大模型", "desc": "腾讯研发的大语言模型，具备强大的中文创作能...", "logo": "/ai-logos/hunyuan.png", "link": "#"},
  {"name": "书生大模型", "desc": "上海人工智能实验室推出的系列AI模型", "logo": "/ai-logos/shushengmodel.png", "link": "#"},
  {"name": "GPT-4", "desc": "OpenAI旗下最新的GPT-4模型", "logo": "/ai-logos/gpt4.png", "link": "#"},
  {"name": "DALL·E 3", "desc": "OpenAI旗下最新的图像生成模型", "logo": "/ai-logos/dalle3.png", "link": "#"},
  {"name": "文心大模型", "desc": "百度推出的产业级知识增强大模型", "logo": "/ai-logos/wenxinmodel.png", "link": "#"},
  {"name": "LLaMA", "desc": "Meta（Facebook）推出的AI大语言模型", "logo": "/ai-logos/llama.png", "link": "#"},
  {"name": "悟道", "desc": "智源“悟道”大模型，中国首个+世界最大人工智...", "logo": "/ai-logos/wudao.png", "link": "#"},
  {"name": "MiracleVision奇想智能", "desc": "类图推出的AI视觉大模型，支持AI图像、设计和...", "logo": "/ai-logos/miraclevision.png", "link": "#"},
  {"name": "Gradio", "desc": "开源的搭建机器学习模型UI界面的Python库", "logo": "/ai-logos/gradio.png", "link": "#"},
  {"name": "DeepFloyd IF", "desc": "StabilityAI旗下的DeepFloyd团队推出的图片生...", "logo": "/ai-logos/deepfloyd.png", "link": "#"},
  {"name": "Cohere", "desc": "构建AI产品的大语言模型平台", "logo": "/ai-logos/cohere.png", "link": "#"},
  {"name": "序列猴子", "desc": "出门问问推出的一款超大规模的语言模型", "logo": "/ai-logos/xuliehouzi.png", "link": "#"},
  {"name": "BLOOM", "desc": "HuggingFace推出的大型语言模型（LLM）", "logo": "/ai-logos/bloom.png", "link": "#"},
  {"name": "阿里巴巴M6", "desc": "阿里巴巴达摩院推出的超大规模中文预训练模型...", "logo": "/ai-logos/alim6.png", "link": "#"},
  {"name": "Lamini", "desc": "低门槛快速定制大语言模型的引擎", "logo": "/ai-logos/lamini.png", "link": "#"},
  {"name": "StableLM", "desc": "Stability AI推出的开源的类ChatGPT大语言模型", "logo": "/ai-logos/stablelm.png", "link": "#"},
  {"name": "Gen-2", "desc": "Runway最新推出的AI视频生成模型", "logo": "/ai-logos/gen2.png", "link": "#"},
  {"name": "DeepSpeed", "desc": "微软开源的低成本实现类似ChatGPT的模型训练", "logo": "/ai-logos/deepspeed.png", "link": "#"},
  {"name": "PaLM 2", "desc": "Google的下一代大语言模型，超过3400亿参数", "logo": "/ai-logos/palm2.png", "link": "#"},
  {"name": "Segment Anything (SAM)", "desc": "Meta最新推出的AI图像分割模型", "logo": "/ai-logos/sam.png", "link": "#"},
  {"name": "HuggingFace", "desc": "AI模型开发社区", "logo": "/ai-logos/huggingface.png", "link": "#"},
  {"name": "Imagen", "desc": "Google AI文字到图像生成模型", "logo": "/ai-logos/imagen.png", "link": "#"}
]
</script>

# Ai 训练模型大全

精选全球前沿 AI 训练模型和模型库。

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
