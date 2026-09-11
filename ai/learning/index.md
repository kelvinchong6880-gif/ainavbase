---
title: Ai 学习网站大全
description: 探索各大领先的 AI 学习网站与在线课程平台。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "AI大学堂", "desc": "科大讯飞推出的在线AI学习平台", "logo": "/ai-logos/aidxx.png", "link": "#"},
  {"name": "AI分享圈", "desc": "最好最全的AI免费资源分享网站", "logo": "/ai-logos/aishare.png", "link": "#"},
  {"name": "OpenAI Academy", "desc": "OpenAI 推出的免费 AI 学习平台", "logo": "/ai-logos/openai_academy.png", "link": "#"},
  {"name": "Day of AI", "desc": "麻省理工学院（MIT）推出的...", "logo": "/ai-logos/dayofai.png", "link": "#"},
  {"name": "fast.ai", "desc": "免费开源的深度学习和AI学习...", "logo": "/ai-logos/fastai.png", "link": "#"},
  {"name": "学吧导航", "desc": "学习爱好者首选的学霸导航网站", "logo": "/ai-logos/xuebadh.png", "link": "#"},
  {"name": "LearnBuddy", "desc": "腾讯推出的专家同行的AI自主...", "logo": "/ai-logos/learnbuddy.png", "link": "#"},
  {"name": "Lynote", "desc": "面向学生、研究者和职场人士...", "logo": "/ai-logos/lynote.png", "link": "#"},
  {"name": "Coursera", "desc": "知名MOOC平台，提供众多人...", "logo": "/ai-logos/coursera.png", "link": "#"},
  {"name": "Elements of AI", "desc": "免费在线AI通识学习课程", "logo": "/ai-logos/elementsofai.png", "link": "#"},
  {"name": "DeepLearning.AI", "desc": "深度学习和人工智能学习平台", "logo": "/ai-logos/deeplearningai.png", "link": "#"},
  {"name": "动手学深度学习", "desc": "结合理论与实践的深度学习教...", "logo": "/ai-logos/d2l.png", "link": "#"},
  {"name": "MachineLearningMastery", "desc": "免费在线的机器学习平台，提...", "logo": "/ai-logos/mlmastery.png", "link": "#"},
  {"name": "Generative AI for Begin...", "desc": "微软推出的面向初学者的免费...", "logo": "/ai-logos/genai_begin.png", "link": "#"},
  {"name": "ML for Beginners", "desc": "微软推出的免费开源的机器学...", "logo": "/ai-logos/ml_begin.png", "link": "#"},
  {"name": "Kaggle", "desc": "机器学习和数据科学社区", "logo": "/ai-logos/kaggle.png", "link": "#"},
  {"name": "神经网络入门", "desc": "Brilliant推出的Introduction to ...", "logo": "/ai-logos/brilliant.png", "link": "#"},
  {"name": "Trancy", "desc": "AI驱动的语言学习工具", "logo": "/ai-logos/trancy.png", "link": "#"},
  {"name": "Reading Coach", "desc": "微软推出的免费个性化AI阅读...", "logo": "/ai-logos/readingcoach.png", "link": "#"},
  {"name": "飞桨AI Studio", "desc": "百度推出的AI学习与实训社区", "logo": "/ai-logos/paddleaistudio.png", "link": "#"},
  {"name": "腾讯扣叮", "desc": "腾讯推出的青少年编程教育平台", "logo": "/ai-logos/codingqq.png", "link": "#"},
  {"name": "阿里云AI学习路线", "desc": "阿里云推出的人工智能学习路...", "logo": "/ai-logos/aliyunai.png", "link": "#"},
  {"name": "Udacity AI学院", "desc": "Udacity推出的School of AI，...", "logo": "/ai-logos/udacity.png", "link": "#"},
  {"name": "Google AI", "desc": "Google AI学习平台", "logo": "/ai-logos/googleai.png", "link": "#"},
  {"name": "ShowMeAI知识社区", "desc": "人工智能领域的资料库和学习...", "logo": "/ai-logos/showmeai.png", "link": "#"},
  {"name": "txyz", "desc": "AI文献阅读和学术研究辅助平台", "logo": "/ai-logos/txyz.png", "link": "#"}
]
</script>

# Ai 学习网站大全

精选全球前沿 AI 学习网站和知识社区。

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
