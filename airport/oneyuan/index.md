---
title: 一元机场推荐：一元白嫖试用好帮手
description: 为您寻找月付一元甚至提供免费试用节点的便宜机场，适合仅需临时科学上网或偶尔查阅海外资料的用户。

outline: false
---

<style>
/* 强制放宽 VitePress 包含侧边栏时的默认宽度限制 */
:root {
  --vp-layout-max-width: 1600px;
}
.VPDoc .container,
.VPDoc .content,
.VPDoc .content-container,
.vp-doc,
.VPDoc.has-sidebar .content,
.VPDoc.has-aside .content-container {
  max-width: 1200px !important;
}
/* 隐藏右侧大纲 */
.VPDoc.has-aside .aside {
  display: none !important;
}
</style>

<script setup>
import ProviderCard from '../../.vitepress/components/ProviderCard.vue'

const nanocloudData = {
  name: 'Nanocloud',
  logo: '/nanocloud-logo.png',
  badgeText: '一元极配',
  rating: '4.6',
  description: '提供极高性价比的 1 元超值月付套餐，带宽最高可达无限制，非常适合轻度冲浪与备用。',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等'],
  reviewLink: '/airport/recommend/nanocloud',
  status: [
    { label: '30天在线率', value: '98%' },
    { label: '活跃用户', value: '10k+' }
  ],
  streaming: ['Netflix', 'Disney+', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付'],
  protocols: ['Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Claude'],
  lines: ['BGP 中转', '高速专线'],
  support: ['TG 频道', '工单系统'],
  plans: [
    { name: '猎户座 (一元)', price: '¥1.00', traffic: '100GB / 月', devices: '2台' },
    { name: '白羊座', price: '¥10.00', traffic: '300GB / 月', devices: '5台' },
    { name: '双鱼座', price: '¥15.00', traffic: '480GB / 月', devices: '8台' },
    { name: '射手座', price: '¥20.00', traffic: '650GB / 月', devices: '10台' }
  ],
  coupon: 'N9ufsEQG',
  registerLink: 'https://edu.yuque.men/auth/register?code=N9ufsEQG'
}
const phantomData = {
  name: 'Phantom',
  logo: '/Phantom-logo.webp',
  badgeText: '一元体验',
  rating: '4.5',
  description: '新晋高性价比机场，提供 1 元天蝎座超值体验套餐，满足日常轻度查阅需求。',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等'],
  reviewLink: '/airport/recommend/phantom',
  status: [
    { label: '30天在线率', value: '99%' },
    { label: '节点数量', value: '30+' }
  ],
  streaming: ['Netflix', 'Disney+', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付'],
  protocols: ['Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Claude'],
  lines: ['公网中转', 'BGP 接入'],
  support: ['TG 群组', '工单系统'],
  plans: [
    { name: '天蝎座 (一元)', price: '¥1.00', traffic: '100GB / 月', devices: '不限' },
    { name: '水瓶座', price: '¥10.00', traffic: '300GB / 月', devices: '不限' },
    { name: '双子座', price: '¥20.00', traffic: '650GB / 月', devices: '不限' }
  ],
  coupon: 'VUBbg83u',
  registerLink: 'https://pin.dianping.men/auth/register?code=VUBbg83u'
}
</script>

# 一元机场

主打极致性价比，提供 1 元级别极低门槛月付套餐的机场推荐，非常适合轻度冲浪查阅资料，或作为主力线路的备用防失联节点使用。

<ProviderCard :provider="nanocloudData" />

<ProviderCard :provider="phantomData" />
