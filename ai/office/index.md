---
title: Ai 办公工具大全
description: 探索各类高效 AI PPT、智能文档与图表生成工具，全面提升办公效率。
---

<script setup>
import ToolCard from '../../.vitepress/components/ToolCard.vue'

const tools = [
  {"name": "Loomy", "desc": "免费一键生成PPT，每天领5000积分！", "logo": "/ai-logos/loomy_office.png", "link": "https://www.bing.com/search?q=Loomy"},
  {"name": "办公小浣熊", "desc": "专业 AI 办公智能体", "logo": "/ai-logos/xiaohuanxiong_office.png", "link": "https://www.bing.com/search?q=%E5%8A%9E%E5%85%AC%E5%B0%8F%E6%B5%A3%E7%86%8A"},
  {"name": "AiPPT", "desc": "AI快速生成高质量PPT", "logo": "/ai-logos/aippt.png", "link": "https://www.bing.com/search?q=AiPPT"},
  {"name": "文多多AiPPT", "desc": "AI一键生成PPT，支持AI配图和智能资料整合", "logo": "/ai-logos/wenduoduo.png", "link": "https://www.bing.com/search?q=%E6%96%87%E5%A4%9A%E5%A4%9AAiPPT"},
  {"name": "千问AiPPT", "desc": "阿里千问推出的AI PPT创作工具", "logo": "/ai-logos/qianwenaippt.png", "link": "https://www.bing.com/search?q=%E5%8D%83%E9%97%AEAiPPT"},
  {"name": "咔片PPT", "desc": "AI PPT制作工具，设计美化全流程自动化", "logo": "/ai-logos/kapianppt.png", "link": "https://www.bing.com/search?q=%E5%92%94%E7%89%87PPT"},
  {"name": "博思AiPPT", "desc": "PPT效率神器，AI一键生成PPT", "logo": "/ai-logos/bosiaippt.png", "link": "https://www.bing.com/search?q=%E5%8D%9A%E6%80%9DAiPPT"},
  {"name": "iSlide AiPPT", "desc": "AI一键设计精美PPT，只需一句标题", "logo": "/ai-logos/islide.png", "link": "https://www.bing.com/search?q=iSlide%20AiPPT"},
  {"name": "二狗PPT", "desc": "去 AI 味中式职场 PPT 生成工具", "logo": "/ai-logos/ergouppt.png", "link": "https://www.bing.com/search?q=%E4%BA%8C%E7%8B%97PPT"},
  {"name": "稿定PPT", "desc": "稿定推出的PPT模板资源库", "logo": "/ai-logos/gaodingppt.png", "link": "https://www.bing.com/search?q=%E7%A8%BF%E5%AE%9APPT"},
  {"name": "Pi智能PPT", "desc": "一键生成PPT，复制精美模板", "logo": "/ai-logos/pippt.png", "link": "https://www.bing.com/search?q=Pi%E6%99%BA%E8%83%BDPPT"},
  {"name": "讯飞智文", "desc": "一键生成PPT和Word", "logo": "/ai-logos/xunfeizhiwen.png", "link": "https://www.bing.com/search?q=%E8%AE%AF%E9%A3%9E%E6%99%BA%E6%96%87"},
  {"name": "笔格AiPPT", "desc": "高效的AI PPT生成工具", "logo": "/ai-logos/bigeaippt.png", "link": "https://www.bing.com/search?q=%E7%AC%94%E6%A0%BCAiPPT"},
  {"name": "百度文库AI助手", "desc": "基于文心一言的一站式智能文档助手", "logo": "/ai-logos/baiduwenku.png", "link": "https://www.bing.com/search?q=%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93AI%E5%8A%A9%E6%89%8B"},
  {"name": "Gamma", "desc": "AI幻灯片演示生成工具", "logo": "/ai-logos/gamma.png", "link": "https://www.bing.com/search?q=Gamma"},
  {"name": "笔灵AiPPT", "desc": "一键生成PPT和千字演讲稿", "logo": "/ai-logos/bilingaippt.png", "link": "https://www.bing.com/search?q=%E7%AC%94%E7%81%B5AiPPT"},
  {"name": "AiPPT插件", "desc": "AiPPT推出的AI PPT制作工具（插件版）", "logo": "/ai-logos/aippt_plugin.png", "link": "https://www.bing.com/search?q=AiPPT%E6%8F%92%E4%BB%B6"},
  {"name": "Napkin", "desc": "将文本内容快速转换成演示图像的AI办公工具", "logo": "/ai-logos/napkin.png", "link": "https://www.bing.com/search?q=Napkin"},
  {"name": "Swishy", "desc": "AI 动态设计与动画生成平台", "logo": "/ai-logos/swishy.png", "link": "https://www.bing.com/search?q=Swishy"},
  {"name": "ChartGen", "desc": "AI图表生成工具，快速生成专业图表", "logo": "/ai-logos/chartgen.png", "link": "https://www.bing.com/search?q=ChartGen"},
  {"name": "Diagrimo", "desc": "Tenorshare AI推出的AI图表生成工具", "logo": "/ai-logos/diagrimo.png", "link": "https://www.bing.com/search?q=Diagrimo"},
  {"name": "PicDoc", "desc": "AI文本转图表工具，一键生成多种视觉图表", "logo": "/ai-logos/picdoc.png", "link": "https://www.bing.com/search?q=PicDoc"},
  {"name": "Kimi PPT助手", "desc": "Kimi全新自研的PPT助手，一键生成PPT", "logo": "/ai-logos/kimippt.png", "link": "https://www.bing.com/search?q=Kimi%20PPT%E5%8A%A9%E6%89%8B"},
  {"name": "夸克PPT", "desc": "夸克团队推出的AI PPT生成工具", "logo": "/ai-logos/kuakeppt.png", "link": "https://www.bing.com/search?q=%E5%A4%B8%E5%85%8BPPT"},
  {"name": "GAIPPT", "desc": "AI智能美化PPT工具，上传PPT一键美化", "logo": "/ai-logos/gaippt.png", "link": "https://www.bing.com/search?q=GAIPPT"},
  {"name": "美图AI PPT", "desc": "美图秀秀推出的免费在线AI生成PPT设计工具", "logo": "/ai-logos/meituppt.png", "link": "https://www.bing.com/search?q=%E7%BE%8E%E5%9B%BEAI%20PPT"},
  {"name": "飞象老师", "desc": "猿辅导推出的国内首个AI教学和备课工具", "logo": "/ai-logos/feixiang.png", "link": "https://www.bing.com/search?q=%E9%A3%9E%E8%B1%A1%E8%80%81%E5%B8%88"},
  {"name": "一点PPT", "desc": "一句话生成专业PPT，AI自动排版配图", "logo": "/ai-logos/yidianppt.png", "link": "https://www.bing.com/search?q=%E4%B8%80%E7%82%B9PPT"},
  {"name": "NarraLand", "desc": "AI智能演示内容创作平台", "logo": "/ai-logos/narraland.png", "link": "https://www.bing.com/search?q=NarraLand"},
  {"name": "课灵 PPT", "desc": "AI免费生成PPT课件", "logo": "/ai-logos/kelingppt.png", "link": "https://www.bing.com/search?q=%E8%AF%BE%E7%81%B5%20PPT"},
  {"name": "清言PPT", "desc": "智谱清言联合AiPPT推出的PPT生成智能体", "logo": "/ai-logos/qingyanppt.png", "link": "https://www.bing.com/search?q=%E6%B8%85%E8%A8%80PPT"},
  {"name": "万兴智演", "desc": "万兴科技推出的AI PPT和演示制作软件", "logo": "/ai-logos/wanxing.png", "link": "https://www.bing.com/search?q=%E4%B8%87%E5%85%B4%E6%99%BA%E6%BC%94"},
  {"name": "麦当秀MindShow", "desc": "在线PPT生成工具", "logo": "/ai-logos/mindshow.png", "link": "https://www.bing.com/search?q=%E9%BA%A6%E5%BD%93%E7%A7%80MindShow"},
  {"name": "VoxDeck", "desc": "创新的AI演示文稿生成工具", "logo": "/ai-logos/voxdeck.png", "link": "https://www.bing.com/search?q=VoxDeck"},
  {"name": "AiBiao", "desc": "AI文生图表工具，支持生成柱状图、折线图、饼...", "logo": "/ai-logos/aibiao.png", "link": "https://www.bing.com/search?q=AiBiao"},
  {"name": "ChatBA", "desc": "AI幻灯片生成工具", "logo": "/ai-logos/chatba.png", "link": "https://www.bing.com/search?q=ChatBA"},
  {"name": "Decktopus AI", "desc": "AI驱动的在线演示文稿生成器", "logo": "/ai-logos/decktopus.png", "link": "https://www.bing.com/search?q=Decktopus%20AI"},
  {"name": "Powerpresent AI", "desc": "AI演示文稿生成工具", "logo": "/ai-logos/powerpresent.png", "link": "https://www.bing.com/search?q=Powerpresent%20AI"},
  {"name": "希沃白板", "desc": "专为互动教学设计的AI课件生成器", "logo": "/ai-logos/xiwo.png", "link": "https://www.bing.com/search?q=%E5%B8%8C%E6%B2%83%E7%99%BD%E6%9D%BF"},
  {"name": "秒出PPT", "desc": "一键生成PPT，智能辅助编辑", "logo": "/ai-logos/miaochuppt.png", "link": "https://www.bing.com/search?q=%E7%A7%92%E5%87%BAPPT"}
]
</script>

# Ai 办公工具大全

精选全球前沿 AI 智能办公、PPT 生成及图表制作平台。

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
