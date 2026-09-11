<script setup>
import { ref } from 'vue'

defineProps({
  tool: Object
})

const imgError = ref(false)

const colors = [
  '#f56a00', '#7265e6', '#ffbf00', '#00a2ae', '#1890ff',
  '#52c41a', '#eb2f96', '#fa8c16', '#13c2c2', '#a0d911'
]

const getBgColor = (name) => {
  let hash = 0
  for (let i = 0; i < name.length; i++) {
    hash = name.charCodeAt(i) + ((hash << 5) - hash)
  }
  hash = Math.abs(hash)
  return colors[hash % colors.length]
}
</script>

<template>
  <a :href="tool.link" class="tool-card">
    <div class="logo" :style="{ backgroundColor: imgError ? getBgColor(tool.name) : 'transparent' }">
      <img v-if="!imgError" :src="tool.logo" :alt="tool.name" @error="imgError = true" />
      <span v-else class="avatar-text">{{ tool.name.charAt(0) }}</span>
    </div>
    <div class="info">
      <div class="name">{{ tool.name }}</div>
      <div class="desc" :title="tool.desc">{{ tool.desc }}</div>
    </div>
  </a>
</template>

<style scoped>
.tool-card {
  display: flex;
  align-items: center;
  padding: 16px;
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  text-decoration: none !important;
  transition: border-color 0.25s, background-color 0.25s, transform 0.25s, box-shadow 0.25s;
  color: var(--vp-c-text-1);
}
.tool-card:hover {
  border-color: var(--vp-c-brand);
  background-color: var(--vp-c-bg-soft-up);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}
.logo {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  overflow: hidden;
  margin-right: 14px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.avatar-text {
  color: white;
  font-size: 1.2rem;
  font-weight: 600;
  font-family: system-ui, -apple-system, sans-serif;
}
.info {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.name {
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.desc {
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
