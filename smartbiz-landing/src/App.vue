<template>
  <div class="app-wrapper">
    <!-- ✅ Clean Main View Only -->
    <main class="max-w-6xl mx-auto px-4 py-4">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// 🎨 Force light theme only (no switch)
const theme = ref('light')
const themeClass = computed(() => 'theme-light')

onMounted(() => {
  document.body.className = themeClass.value
})
</script>

<style scoped>
/* 🎨 Light theme only */
.theme-light {
  --bg-color: #ffffff;
  --text-color: #111111;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  margin: 0;
  padding: 0;
  font-family: system-ui, sans-serif;
  transition: background-color 0.2s ease;
}

.app-wrapper {
  min-height: 100vh;
  background-color: var(--bg-color);
  color: var(--text-color);
}

/* 🧩 Responsive tightening */
main {
  padding-top: 1rem;
  padding-bottom: 2rem;
}
</style>
