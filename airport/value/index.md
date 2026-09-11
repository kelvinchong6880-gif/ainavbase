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


const flycatData = {
  name: '飞猫云',
  logo: '/feimaoyun-logo.png', // 根据你保存的文件名更新
  badgeText: '极速稳定',
  rating: '4.8',
  description: '全 IPLC 专线网络，最高 2.5Gbps，原生 IP 解锁各大流媒体',
  coverage: ['香港', '台湾', '日本', '新加坡', '美国', '韩国', '马来西亚等 15+ 地区'],
  reviewLink: '/airport/recommend/flycat',
  status: [
    { label: '30天在线率', value: '99.9%' },
    { label: '节点总数', value: '90+' }
  ],
  streaming: ['Netflix', 'Disney+', 'ChatGPT', 'TikTok', 'YouTube'],
  clients: ['Windows', 'macOS', 'iOS', 'Android'],
  payment: ['支付宝', '微信支付', 'USDT'],
  protocols: ['Shadowsocks', 'Vmess', 'Trojan'],
  ai: ['ChatGPT', 'Gemini', 'Claude AI'],
  lines: ['全 IPLC 专线', '独享原生 IP', 'BGP 中继'],
  support: ['24/7 在线客服', 'TG 群组', '工单系统'],
  plans: [
    { name: '飞猫·学生版', price: '¥84.00/年', traffic: '50GB / 月', devices: '不限' },
    { name: '飞猫·星耀版', price: '¥25.00', traffic: '150GB / 月', devices: '不限' },
    { name: '飞猫·星环版', price: '¥45.00', traffic: '300GB / 月', devices: '不限' },
    { name: '飞猫·银河版', price: '¥85.00', traffic: '600GB / 月', devices: '不限' },
    { name: '飞猫·宇宙版', price: '¥150.00', traffic: '1.0TB / 月', devices: '不限' },
    { name: '飞猫·不限时套餐', price: '¥680.00/次', traffic: '1.0TB / 一次性', devices: '不限' },
    { name: '飞猫·定制套餐', price: '¥550.00', traffic: '500GB / 月 (独享原生IP)', devices: '不限' }
  ],
  coupon: 'w5lO9fqB',
  registerLink: 'https://flycat1.flycatvipaff.cc/#/?code=w5lO9fqB'
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

</script>

# 性价比机场

兼顾价格与速度的高性价比机场。

<ProviderCard :provider="sogoData" />

<ProviderCard :provider="flycatData" />

<ProviderCard :provider="fireflyData" />

<ProviderCard :provider="wuyouData" />

<ProviderCard :provider="xsusData" />

<ProviderCard :provider="xxyunData" />

<ProviderCard :provider="shanshuiData" />