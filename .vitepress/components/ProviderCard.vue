<script setup>
import { computed } from 'vue'

const props = defineProps({
  provider: {
    type: Object,
    required: true
  }
})

const features = computed(() => [
  { title: '运行状态', icon: '⚡', items: props.provider.status },
  { title: '流媒体解锁', icon: '🎬', items: props.provider.streaming },
  { title: '客户端支持', icon: '💻', items: props.provider.clients },
  { title: '支付方式', icon: '💳', items: props.provider.payment },
  { title: '代理协议', icon: '⚙️', items: props.provider.protocols },
  { title: 'AI 解锁能力', icon: '🤖', items: props.provider.ai },
  { title: '线路类型', icon: '🚀', items: props.provider.lines },
  { title: '售后客服', icon: '🎧', items: props.provider.support },
])

const copyCoupon = (code) => {
  navigator.clipboard.writeText(code)
  alert('邀请码已复制: ' + code)
}
</script>

<template>
  <div class="provider-wrapper">
    <!-- Abstract blurred blobs for glassmorphism effect -->
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    
    <div class="provider-card glass-panel">
      <!-- Header -->
      <div class="card-header">
        <div class="logo-wrapper">
          <img :src="provider.logo" :alt="provider.name" class="logo" v-if="provider.logo" />
          <div class="logo-fallback" v-else>{{ provider.name.charAt(0) }}</div>
        </div>
        <div class="header-info">
          <div class="title-row">
            <h2 class="name">{{ provider.name }}</h2>
            <span v-if="provider.badgeText" class="badge badge-recommended">🔥 {{ provider.badgeText }}</span>
            <span class="badge badge-rating">⭐ {{ provider.rating }}</span>
          </div>
          <p class="description">{{ provider.description }}</p>
          <p class="coverage">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            节点覆盖: {{ provider.coverage.join('、') }}
          </p>
        </div>
        <a :href="provider.reviewLink" class="btn-review glass-btn" v-if="provider.reviewLink">
          📄 阅读测评 ➔
        </a>
      </div>

      <!-- Features Grid -->
      <div class="features-grid">
        <div class="feature-col glass-panel-inner" v-for="(col, index) in features" :key="index">
          <h4 class="feature-title">
            <span class="feature-icon">{{ col.icon }}</span>
            {{ col.title }}
          </h4>
          <ul class="feature-list">
            <li v-for="(item, i) in col.items" :key="i" class="feature-item">
              <!-- Custom Icons -->
              <div class="icon-wrapper">
                <svg v-if="col.title === '运行状态'" class="icon-pulse" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                <svg v-else-if="col.title === '线路类型'" class="icon-star" viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                <svg v-else-if="col.title === '代理协议'" class="icon-dot" viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><circle cx="12" cy="12" r="5" /></svg>
                <svg v-else-if="col.title === '售后客服'" class="icon-msg" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                <svg v-else class="icon-check" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              
              <span v-if="item.label" class="item-label">{{ item.label }}</span>
              <span class="item-value" :class="{'bold-value': item.label}">{{ item.value || item }}</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Pricing Table -->
      <div class="pricing-section glass-panel-inner">
        <div class="table-container">
          <table class="pricing-table">
            <thead>
              <tr>
                <th>套餐名称</th>
                <th>价格 (人民币)</th>
                <th>包含流量</th>
                <th>设备数</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(plan, index) in provider.plans" :key="index">
                <td class="plan-name">{{ plan.name }}</td>
                <td class="plan-price">{{ plan.price }}</td>
                <td class="plan-traffic">{{ plan.traffic }}</td>
                <td class="plan-devices">{{ plan.devices }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Footer -->
      <div class="card-footer">
        <div class="coupon-section" v-if="provider.coupon">
          <span class="coupon-label">🎁 本站专属邀请码</span>
          <div class="coupon-box glass-btn" @click="copyCoupon(provider.coupon)">
            <span class="coupon-code">{{ provider.coupon }}</span>
            <svg class="icon-copy" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          </div>
        </div>
        <div class="footer-spacer"></div>
        <a :href="provider.registerLink" class="btn-register" target="_blank" rel="noopener noreferrer">
          前往官网注册 ↗
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.provider-wrapper {
  position: relative;
  margin: 40px 0;
  border-radius: 24px;
  /* To contain the blobs */
  overflow: hidden;
  padding: 2px;
}

/* Background gradient blobs */
.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  z-index: 0;
  opacity: 0.6;
  animation: float 10s infinite ease-in-out alternate;
}
.blob-1 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(129,140,248,0.8) 0%, rgba(192,132,252,0.4) 100%);
  top: -100px;
  left: -50px;
}
.blob-2 {
  width: 250px;
  height: 250px;
  background: radial-gradient(circle, rgba(96,165,250,0.8) 0%, rgba(52,211,153,0.4) 100%);
  bottom: -50px;
  right: -50px;
  animation-delay: -5s;
}

@keyframes float {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(30px, 30px) scale(1.1); }
}

/* Glassmorphism Panel */
.glass-panel {
  position: relative;
  z-index: 1;
  background: rgba(255, 255, 255, 0.65);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 22px;
  box-shadow: 0 8px 32px rgba(31, 38, 135, 0.08);
  padding: 32px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #1e293b;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.glass-panel:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 40px rgba(31, 38, 135, 0.12);
  border: 1px solid rgba(255, 255, 255, 1);
}

.glass-panel-inner {
  background: rgba(255, 255, 255, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 16px;
}

.glass-btn {
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.7);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}
.glass-btn:hover {
  background: rgba(255, 255, 255, 0.8);
}

/* Header */
.card-header {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  padding-bottom: 24px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  margin-bottom: 28px;
  position: relative;
}

.logo-wrapper {
  flex-shrink: 0;
  position: relative;
}
.logo-wrapper::after {
  content: '';
  position: absolute;
  inset: -4px;
  background: linear-gradient(135deg, #a78bfa, #60a5fa);
  border-radius: 24px;
  z-index: -1;
  opacity: 0.5;
  filter: blur(8px);
}

.logo, .logo-fallback {
  width: 80px;
  height: 80px;
  border-radius: 20px;
  object-fit: cover;
  border: 2px solid rgba(255,255,255,0.8);
}

.logo-fallback {
  background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  font-weight: 800;
}

.header-info {
  flex-grow: 1;
}

.title-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}

.name {
  margin: 0 !important;
  font-size: 26px;
  font-weight: 800;
  color: #0f172a;
  border: none !important;
  padding: 0 !important;
  letter-spacing: -0.5px;
}

.badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 700;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}

.badge-recommended {
  background: linear-gradient(135deg, rgba(244, 63, 94, 0.15) 0%, rgba(253, 164, 175, 0.15) 100%);
  color: #e11d48;
  border: 1px solid rgba(253, 164, 175, 0.4);
}

.badge-rating {
  background: rgba(251, 191, 36, 0.15);
  color: #d97706;
  border: 1px solid rgba(253, 230, 138, 0.5);
}

.description {
  margin: 0 0 10px 0 !important;
  font-size: 15px;
  color: #475569;
  line-height: 1.6;
}

.coverage {
  margin: 0 !important;
  font-size: 13px;
  color: #64748b;
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255,255,255,0.4);
  padding: 4px 10px;
  border-radius: 12px;
  display: inline-flex;
}

.btn-review {
  display: inline-flex;
  align-items: center;
  padding: 10px 20px;
  color: #4f46e5;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.3s ease;
  white-space: nowrap;
}
.btn-review:hover {
  transform: scale(1.03);
  color: #4338ca;
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 32px;
}

@media (max-width: 1024px) {
  .features-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 640px) {
  .features-grid { grid-template-columns: 1fr; }
  .card-header { flex-direction: column; align-items: flex-start; }
  .btn-review { position: static; margin-top: 12px; }
}

.feature-col {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  transition: all 0.3s ease;
}
.feature-col:hover {
  background: rgba(255, 255, 255, 0.6);
  transform: translateY(-2px);
}

.feature-title {
  font-size: 14px;
  font-weight: 800;
  color: #1e293b;
  margin: 0 0 4px 0 !important;
  display: flex;
  align-items: center;
  gap: 8px;
  border: none !important;
  padding: 0 !important;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.feature-icon {
  font-size: 16px;
  opacity: 0.9;
}

.feature-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13.5px;
  color: #334155;
  margin: 0 !important;
  padding: 0 !important;
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 6px;
  background: rgba(255,255,255,0.7);
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.icon-check { color: #10b981; }
.icon-star { color: #f59e0b; }
.icon-dot { color: #3b82f6; }
.icon-pulse { color: #ef4444; }
.icon-msg { color: #8b5cf6; }

.item-label {
  color: #64748b;
  font-size: 13px;
}

.bold-value {
  font-weight: 700;
  color: #0f172a;
}

/* Pricing Table */
.pricing-section {
  padding: 8px;
  margin-bottom: 24px;
  overflow-x: auto;
}

.pricing-table {
  display: table !important;
  width: 100% !important;
  border-collapse: separate !important;
  border-spacing: 0 6px !important;
  text-align: left;
  margin: 0 !important;
  border: none !important;
}

.pricing-table th, .pricing-table td, .pricing-table tr {
  border: none !important;
}

.pricing-table th {
  padding: 10px 20px !important;
  color: #64748b;
  font-weight: 700;
  font-size: 13px;
  background: transparent !important;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.pricing-table td {
  padding: 14px 20px !important;
  font-size: 14px;
  white-space: nowrap;
  background: rgba(255, 255, 255, 0.4) !important;
  transition: all 0.2s ease;
}

.pricing-table tr {
  background: transparent !important;
}

.pricing-table tr td:first-child { border-top-left-radius: 12px; border-bottom-left-radius: 12px; }
.pricing-table tr td:last-child { border-top-right-radius: 12px; border-bottom-right-radius: 12px; }

.pricing-table tr:hover td {
  background: rgba(255, 255, 255, 0.8) !important;
  transform: scale(1.01);
}

.plan-name {
  color: #475569;
  font-weight: 600;
}

.plan-price {
  color: #4f46e5;
  font-weight: 800;
  font-size: 16px;
}

.plan-traffic, .plan-devices {
  color: #475569;
}

/* Footer */
.card-footer {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  padding-top: 24px;
  border-top: 1px solid rgba(0, 0, 0, 0.06);
}

.coupon-section {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.coupon-label {
  font-size: 12px;
  color: #e11d48;
  font-weight: 800;
  letter-spacing: 0.5px;
}

.coupon-box {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 8px 16px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.coupon-box:hover {
  background: rgba(255, 255, 255, 0.9);
  border-color: rgba(255, 255, 255, 1);
  transform: translateY(-1px);
}

.coupon-code {
  color: #e11d48;
  font-family: 'Courier New', Courier, monospace;
  font-weight: 800;
  font-size: 16px;
  letter-spacing: 2px;
}

.icon-copy {
  color: #64748b;
}

.footer-spacer {
  flex-grow: 1;
}

.btn-register {
  background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
  color: white !important;
  padding: 14px 32px;
  border-radius: 14px;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.3s ease;
  box-shadow: 0 8px 20px rgba(79, 70, 229, 0.3);
}

.btn-register:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px rgba(79, 70, 229, 0.4);
  background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
}

/* Dark Mode (VitePress uses html.dark) */
:global(html.dark) .glass-panel {
  background: rgba(30, 30, 32, 0.65);
  border-color: rgba(255, 255, 255, 0.08);
  color: #f1f5f9;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
}
:global(html.dark) .glass-panel:hover {
  border-color: rgba(255, 255, 255, 0.15);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
}
:global(html.dark) .glass-panel-inner {
  background: rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.05);
}
:global(html.dark) .glass-btn {
  background: rgba(0, 0, 0, 0.4);
  border-color: rgba(255, 255, 255, 0.1);
}
:global(html.dark) .glass-btn:hover {
  background: rgba(0, 0, 0, 0.6);
}
:global(html.dark) .name { color: #f8fafc; }
:global(html.dark) .description { color: #94a3b8; }
:global(html.dark) .feature-title { color: #e2e8f0; }
:global(html.dark) .feature-item { color: #cbd5e1; }
:global(html.dark) .item-label { color: #94a3b8; }
:global(html.dark) .bold-value { color: #f8fafc; }
:global(html.dark) .icon-wrapper { background: rgba(0,0,0,0.4); }
:global(html.dark) .card-header, :global(html.dark) .card-footer { border-color: rgba(255, 255, 255, 0.05); }
:global(html.dark) .pricing-table th { color: #94a3b8; border: none !important; }
:global(html.dark) .pricing-table td { background: rgba(0, 0, 0, 0.2) !important; border: none !important; }
:global(html.dark) .pricing-table tr:hover td { background: rgba(0, 0, 0, 0.4) !important; }
:global(html.dark) .plan-name, :global(html.dark) .plan-traffic, :global(html.dark) .plan-devices { color: #cbd5e1; }
:global(html.dark) .plan-price { color: #818cf8; }
:global(html.dark) .btn-review { color: #818cf8; }
:global(html.dark) .btn-review:hover { color: #a5b4fc; }
:global(html.dark) .coverage { background: rgba(0,0,0,0.3); color: #94a3b8; }
</style>
