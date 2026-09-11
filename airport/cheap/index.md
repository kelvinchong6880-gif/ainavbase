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

const wuyouData = {
  name: '无忧',
  logo: '/wuyou-logo.png', // 已保存
  badgeText: '推荐',
  rating: '4.8',
  description: '全 IPLC 专线，节点速率x1·不限速不限设备',
  coverage: ['香港', '新加坡', '日本', '台湾', '美国'],
  reviewLink: '/airport/recommend/wuyou',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '110' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['IEPL 专线', 'IPLC 专线', 'BGP 中继'],
  support: ['24/7 在线客服', 'TG 群组', '工单系统'],
  plans: [
    { name: '舒心链接', price: '¥19.00', traffic: '100GB / 月', devices: '不限' },
    { name: '省心链接', price: '¥33.00', traffic: '200GB / 月', devices: '不限' },
    { name: '随心链接', price: '¥77.00', traffic: '500GB / 月', devices: '不限' },
    { name: '忘忧链接', price: '¥117.00', traffic: '1000GB / 月', devices: '不限' },
    { name: '不限时流量包', price: '¥108.00/次', traffic: '100GB / 不限时', devices: '不限' }
  ],
  coupon: 's1kH64A8',
  registerLink: 'https://wep01.worryfreeaff.com/#/?code=s1kH64A8'
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

const xsusData = {
  name: 'XSUS',
  logo: '/xsus-logo.png', // 根据保存的文件名
  badgeText: '稳定多能',
  rating: '4.8',
  description: '自有机房专柜，IEPL 企业专线，全平台网络解锁支持',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等全球多地接入'],
  reviewLink: '/airport/recommend/xsus',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '80+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['IEPL 专线', 'BGP 中继', '专柜接入'],
  support: ['24/7 在线客服', 'TG 群组', '工单系统'],
  plans: [
    { name: 'P-Small 基础套餐', price: '¥12.00', traffic: '168GB / 月', devices: '不超过 5 个 IP' },
    { name: 'P-Plus 进阶套餐', price: '¥24.00', traffic: '336GB / 月', devices: '不超过 5 个 IP' },
    { name: 'P-Max 专业套餐', price: '¥30.00', traffic: '420GB / 月', devices: '不超过 5 个 IP' },
    { name: 'P-Ultra 极限套餐', price: '¥70.00', traffic: '1024GB / 月', devices: '不超过 5 个 IP' },
    { name: 'IEPL-Small 企业专线', price: '¥52.00/季', traffic: '50GB / 月', devices: '不超过 5 个 IP' },
    { name: 'IEPL-Plus 企业专线', price: '¥88.00/季', traffic: '100GB / 月', devices: '不超过 5 个 IP' },
    { name: 'P-188G 流量不限时', price: '¥65.00/次', traffic: '188GB / 不限时', devices: '不超过 5 个 IP' },
    { name: 'P-240G 流量不限时', price: '¥82.00/次', traffic: '240GB / 不限时', devices: '不超过 5 个 IP' },
    { name: 'P-400G 流量不限时', price: '¥122.00/次', traffic: '400GB / 不限时', devices: '不超过 5 个 IP' },
    { name: 'P-1024G 流量不限时', price: '¥260.00/次', traffic: '1024GB / 不限时', devices: '不超过 5 个 IP' }
  ],
  coupon: 'QQh1M1i9',
  registerLink: 'https://xsus.cloud/register?code=QQh1M1i9'
}

const xxyunData = {
  name: '小新云 (xxyun)',
  logo: '/xxyun-logo.png', // 根据保存的文件名
  badgeText: '安全稳定',
  rating: '4.8',
  description: 'BGP + 中转线路，超大带宽保障，7x24在线客户服务支持',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国等'],
  reviewLink: '/airport/recommend/xxyun',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '50+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['BGP + 中转', '专线接入', '解锁流媒体'],
  support: ['7x24在线服务', 'TG 群组', '工单系统'],
  plans: [
    { name: '初级 — 月付 100G', price: '¥9.99', traffic: '100GB / 月', devices: '不限设备' },
    { name: '中级 — 月付 300G', price: '¥19.90', traffic: '300GB / 月', devices: '不限设备' },
    { name: '高级 — 月付 1000G', price: '¥39.90', traffic: '1000GB / 月', devices: '不限设备' }
  ],
  coupon: 'pi9fB906',
  registerLink: 'https://www.xx-yun.com/?code=pi9fB906'
}
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

# 便宜机场

低价、高性价比的平民机场推荐。

<ProviderCard :provider="wuyouData" />

<ProviderCard :provider="kuajieData" />

<ProviderCard :provider="flybitData" />

<ProviderCard :provider="xsusData" />

<ProviderCard :provider="xxyunData" />

<ProviderCard :provider="nanocloudData" />

<ProviderCard :provider="phantomData" />