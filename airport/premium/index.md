---
title: 优质机场推荐：高端 IPLC 专线极致体验
description: 追求极致速度与延迟？为您推荐全线采用 IPLC/IEPL 国际内网专线的优质高端机场，晚高峰 4K/8K 视频秒开，游戏不丢包。

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
/* 隐藏右侧大纲（如果需要空间） */
.VPDoc.has-aside .aside {
  display: none !important;
}
</style>

<script setup>
import ProviderCard from '../../.vitepress/components/ProviderCard.vue'

const sogoData = {
  name: 'sogo云',
  logo: '/sogoyun-logo.webp',
  badgeText: '极速稳定',
  rating: '4.9',
  description: '全 IPLC/IEPL 专线，原生 IP 解锁流媒体，支持 ChatGPT 和 TikTok，不限设备并发',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国', '韩国', '英国', '法国', '德国', '土耳其', '巴西等'],
  reviewLink: '/airport/recommend/sogo.html',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '80+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android', '路由器'],
  payment: ['支付宝', '微信支付'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['IPLC 专线', 'IEPL 专线', '原生 IP'],
  support: ['高效客服响应', '工单系统'],
  plans: [
    { name: '小包-年付版', price: '¥98.00/年', traffic: '60GB / 月', devices: '不限' },
    { name: '基础版', price: '¥25.00/月', traffic: '150GB / 月', devices: '不限' },
    { name: '优选版', price: '¥45.00/月', traffic: '350GB / 月', devices: '不限' },
    { name: '强化版', price: '¥80.00/月', traffic: '550GB / 月', devices: '不限' },
    { name: '顶配版', price: '¥150.00/月', traffic: '1.1TB / 月', devices: '不限' },
    { name: '基础餐不限时版', price: '¥120.00/次', traffic: '120GB / 一次性', devices: '不限' },
    { name: '优选餐不限时版', price: '¥220.00/次', traffic: '250GB / 一次性', devices: '不限' },
    { name: '强化餐不限时版', price: '¥450.00/次', traffic: '500GB / 一次性', devices: '不限' },
    { name: '至尊餐不限时版', price: '¥850.00/次', traffic: '1.0TB / 一次性', devices: '不限' }
  ],
  coupon: 'BC2BL855',
  registerLink: 'https://wzjc.sogoyunaff.cc/#/?code=BC2BL855'
}


const weifengData = {
  name: '微风',
  logo: '/weifeng-logo.png',
  badgeText: '倾力推荐',
  rating: '4.8',
  description: '全 IPLC 线路，节点速率×1 · 不限速不限设备',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国', '英国'],
  reviewLink: '/airport/recommend/weifeng',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '61' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['IEPL 专线', 'IPLC 专线', 'BGP 中继'],
  support: ['24/7 在线客服', 'TG 群组', '工单系统'],
  plans: [
    { name: '乘风 (Riding)', price: '¥27.00', traffic: '200GB / 月', devices: '不限' },
    { name: '破风 (Breaking)', price: '¥33.00', traffic: '500GB / 月', devices: '不限' },
    { name: '御风 (Mastery)', price: '¥127.00', traffic: '1.2TB / 月', devices: '不限' },
    { name: '清风 (Breeze)', price: '¥137.00', traffic: '100GB / 年', devices: '不限' },
    { name: '信风 · 不限时', price: '¥108.00', traffic: '270GB / 一次性', devices: '不限' },
    { name: '长风 · 不限时', price: '¥370.00', traffic: '570GB / 一次性', devices: '不限' }
  ],
  coupon: 'hM8APccJ',
  registerLink: 'https://edp01.breezenetaff.com/#/?code=hM8APccJ'
}

const fireflyData = {
  name: 'Firefly',
  logo: '/firefly-logo.png', // 你已经保存好了
  badgeText: '热门推荐',
  rating: '4.8',
  description: '纯正 IPLC 专线网络，不限速不限设备数',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等主流地区'],
  reviewLink: '/airport/recommend/firefly', // 阅读测评占位链接
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '70+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['全 IPLC 专线', '独享原生 IP', 'BGP 中继'],
  support: ['24/7 在线客服', 'TG 群组', '工单系统'],
  plans: [
    { name: 'Firefly 年付版', price: '¥96.00/年', traffic: '60GB / 月', devices: '不限' },
    { name: 'Firefly Lite', price: '¥25.00', traffic: '150GB / 月', devices: '不限' },
    { name: 'Firefly Plus', price: '¥45.00', traffic: '300GB / 月', devices: '不限' },
    { name: 'Firefly Blaze', price: '¥85.00', traffic: '600GB / 月', devices: '不限' },
    { name: 'Firefly Nova', price: '¥150.00', traffic: '1.0TB / 月', devices: '不限' },
    { name: 'Firefly 不限时', price: '¥100.00/次', traffic: '100GB / 永久有效', devices: '不限' }
  ],
  coupon: '8nDg6OEY',
  registerLink: 'https://vip02.fireflyaff.com/#/?code=8nDg6OEY'
}

const flybitData = {
  name: 'Flybit',
  logo: '/flybit-logo.png', // 根据保存的文件名
  badgeText: '极致性价比',
  rating: '4.8',
  description: 'SS 协议与 Secure 隧道，稳定解锁流媒体与 AI，支持家庭成员共享',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等'],
  reviewLink: '/airport/recommend/flybit',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '60+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['SS协议', 'Secure隧道'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['全 IPLC 专线', '独享原生 IP', 'BGP 中继'],
  support: ['24/7 在线客服', 'TG 群组', '工单系统'],
  plans: [
    { name: '每月 - 128G', price: '¥15.00', traffic: '128GB / 月', devices: '可共享' },
    { name: '每月 - 192G', price: '¥22.00', traffic: '192GB / 月', devices: '可共享' },
    { name: '每月 - 256G', price: '¥28.00', traffic: '256GB / 月', devices: '可共享' },
    { name: '每月 - 512G', price: '¥52.00', traffic: '512GB / 月', devices: '可共享' },
    { name: '不限时 - 128G', price: '¥36.00/次', traffic: '128GB / 不限时', devices: '可共享' },
    { name: '不限时 - 256G', price: '¥68.00/次', traffic: '256GB / 不限时', devices: '可共享' },
    { name: '不限时 - 512G', price: '¥128.00/次', traffic: '512GB / 不限时', devices: '可共享' },
    { name: '不限时 - 1024G', price: '¥238.00/次', traffic: '1024GB / 不限时', devices: '可共享' }
  ],
  coupon: 'Aga7bd1s',
  registerLink: 'https://1.flybit.network/#/register?code=Aga7bd1s'
}

const kuajieData = {
  name: '跨界云',
  logo: '/kaujieyun-logo.png', // 根据你保存的文件名
  badgeText: '稳定优选',
  rating: '4.8',
  description: 'IPLC高端线路，全节点x1倍率，不限制设备登录数',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等'],
  reviewLink: '/airport/recommend/kuajie',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '80+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['IEPL 专线', 'IPLC 专线', 'BGP 中继'],
  support: ['24/7 在线客服', 'TG 群组', '工单系统'],
  plans: [
    { name: '跨界年付版', price: '¥96.00/年', traffic: '60GB / 月', devices: '不限' },
    { name: '轻云 Lite', price: '¥20.00', traffic: '120GB / 月', devices: '不限' },
    { name: '跃云 Leap', price: '¥40.00', traffic: '330GB / 月', devices: '不限' },
    { name: '凌云 Soar', price: '¥90.00', traffic: '830GB / 月', devices: '不限' },
    { name: '无界 Infinity', price: '¥130.00', traffic: '1.8TB / 月', devices: '不限' }
  ],
  coupon: 'hh3QezsW',
  registerLink: 'https://vip02.kuajieaff.com/#/?code=hh3QezsW'
}

</script>

# 优质机场

提供专线、全节点流媒体解锁的高端优质机场。

<ProviderCard :provider="sogoData" />

<ProviderCard :provider="weifengData" />

<ProviderCard :provider="fireflyData" />

<ProviderCard :provider="flybitData" />

<ProviderCard :provider="kuajieData" />