---
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

const shanshuiData = {
  name: '山水云',
  logo: '/shanshuiyun-logo.png', // 请将刚发的 logo 图片保存到 public 目录下并命名为 shanshuiyun-logo.png
  badgeText: '老牌经典',
  rating: '4.7',
  description: '三网优化高端线路，解锁 GPT, Tiktok 等全流媒体，全球众多冷门国家接入',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国', '冷门国家'],
  reviewLink: '/airport/recommend/shanshuiyun',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '70+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['中转直连节点', '三网优化专线'],
  support: ['24小时工单', 'TG 群组', 'TG 频道'],
  plans: [
    { name: '100G/月-琴', price: '¥15.00/月', traffic: '100GB / 月', devices: '3 个设备' },
    { name: '200G/月-棋', price: '¥25.00/月', traffic: '200GB / 月', devices: '5 个设备' },
    { name: '500G/月-书', price: '¥50.00/月', traffic: '500GB / 月', devices: '5 个设备' },
    { name: '200G/月-棋pro', price: '¥60.00/月', traffic: '200GB / 月', devices: '2 个设备' },
    { name: '500G/月-书pro', price: '¥150.00/月', traffic: '500GB / 月', devices: '5 个设备' },
    { name: '100G/不限时', price: '¥320.00/次', traffic: '100GB / 永久', devices: '2 个设备' }
  ],
  coupon: 'Rh44jFWe',
  registerLink: 'https://sldm1.ssyylf.com/#/register?code=Rh44jFWe'
}

const shanyueData = {
  name: '闪跃',
  logo: '/shanyue-logo.png', // 根据你保存的文件名
  badgeText: '极速稳定',
  rating: '4.8',
  description: '全 IPLC 专线，晚高峰不限速，原生 IP 解锁全流媒体',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等'],
  reviewLink: '/airport/recommend/shanyue',
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
    { name: '闪动 (Flicker)', price: '¥24.00', traffic: '150GB / 月', devices: '不限' },
    { name: '飞跃 (Leap)', price: '¥44.00', traffic: '300GB / 月', devices: '不限' },
    { name: '瞬移 (Teleport)', price: '¥84.00', traffic: '600GB / 月', devices: '不限' },
    { name: '跃迁 (Warp)', price: '¥134.00', traffic: '1.0TB / 月', devices: '不限' },
    { name: '闪跃年付版', price: '¥96.00/年', traffic: '60GB / 月', devices: '不限' },
    { name: '闪跃无限时版', price: '¥150.00/次', traffic: '100GB / 不限时', devices: '不限' }
  ],
  coupon: 'cs0ekCMG',
  registerLink: 'https://wep01.flashleapaff.com/#/?code=cs0ekCMG'
}
</script>

# 老牌机场

运营时间长、信誉好的老牌机场。

<ProviderCard :provider="sogoData" />

<ProviderCard :provider="weifengData" />

<ProviderCard :provider="shanshuiData" />

<ProviderCard :provider="shanyueData" />