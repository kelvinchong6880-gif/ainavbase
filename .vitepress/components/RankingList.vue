<template>
  <div class="ranking-table">
    <div v-for="(item, index) in items" :key="index" class="ranking-row">
      <div class="rank-col">
        <div class="rank-number" :class="'rank-' + (index + 1)">
          {{ index + 1 }}
        </div>
      </div>
      
      <div class="name-col">
        <img v-if="item.logo" :src="item.logo" :alt="item.name + ' logo'" class="provider-logo" />
        <span class="name">{{ item.name }}</span>
      </div>
      
      <div class="rating-col">
        <span class="star">⭐</span> <span class="rating-num">{{ item.rating }}</span>
      </div>
      
      <div class="desc-col">
        <span class="desc">{{ item.description }}</span>
      </div>
      
      <div class="price-col">
        <span class="currency">¥</span><span class="amount">{{ item.price }}</span> <span class="unit">/ 月</span>
      </div>
      
      <div class="action-col">
        <a :href="item.link" target="_blank" class="register-btn">
          官网注册 ↗
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.ranking-table {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 30px;
  width: 100%;
}

.ranking-row {
  display: flex;
  align-items: center;
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 16px 20px;
  transition: all 0.2s ease;
}

.ranking-row:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.05);
  border-color: var(--vp-c-brand-soft);
}

.rank-col {
  width: 60px;
  flex-shrink: 0;
}

.rank-number {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background-color: var(--vp-c-default-soft);
  color: var(--vp-c-text-2);
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 800;
  font-size: 1rem;
}

.rank-1 { background-color: #f59e0b; color: white; }
.rank-2 { background-color: #94a3b8; color: white; }
.rank-3 { background-color: #f97316; color: white; }

.name-col {
  width: 180px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 12px;
}

.provider-logo {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  object-fit: contain;
  background-color: white;
  border: 1px solid var(--vp-c-divider);
}

.name {
  font-weight: 800;
  font-size: 1.1rem;
  color: var(--vp-c-text-1);
}

.rating-col {
  width: 100px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 4px;
}

.star {
  font-size: 0.9rem;
  color: #f59e0b;
}

.rating-num {
  font-weight: 700;
  color: #f59e0b;
}

.desc-col {
  flex-grow: 1;
  padding: 0 16px;
}

.desc {
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
}

.price-col {
  width: 140px;
  flex-shrink: 0;
  text-align: right;
  padding-right: 24px;
}

.currency {
  font-weight: 700;
  color: var(--vp-c-brand);
  font-size: 0.9rem;
}

.amount {
  font-weight: 800;
  font-size: 1.1rem;
  color: var(--vp-c-brand);
}

.unit {
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
  margin-left: 2px;
}

.action-col {
  width: 120px;
  flex-shrink: 0;
  text-align: right;
}

.register-btn {
  display: inline-block;
  background-color: var(--vp-c-brand-soft);
  color: var(--vp-c-brand) !important;
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none !important;
  transition: all 0.2s;
}

.register-btn:hover {
  background-color: var(--vp-c-brand);
  color: white !important;
}

@media (max-width: 900px) {
  .ranking-row {
    flex-wrap: wrap;
    position: relative;
    padding-bottom: 50px;
  }
  .rank-col { width: 40px; }
  .name-col { width: auto; flex-grow: 1; }
  .rating-col { width: auto; margin-right: 12px; }
  .desc-col { width: 100%; padding: 12px 0 0 40px; }
  .price-col { position: absolute; bottom: 16px; left: 40px; text-align: left; padding-right: 0; }
  .action-col { position: absolute; bottom: 12px; right: 20px; }
}
</style>
