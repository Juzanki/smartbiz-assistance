<template>
  <div :class="themeClass">
    <!-- 🔝 Header -->
    <header class="bg-white dark:bg-gray-900 shadow-md py-4">
      <div class="max-w-7xl mx-auto px-6 flex items-center justify-between">
        <!-- 🔷 Logo + Welcome -->
        <div class="flex items-center gap-4">
          <img
            src="/icons/logo.png"
            alt="SmartBiz Logo"
            class="w-12 h-12 rounded-full shadow border border-yellow-400 bg-white"
          />
          <UserGreeting :msg="$t('welcome')" />
        </div>

        <!-- 🌍 Language & Theme -->
        <div class="flex items-center gap-4">
          <LanguageSwitcher />
          <select
            v-model="theme"
            @change="switchTheme"
            class="px-3 py-1 rounded-md border dark:border-gray-600 dark:bg-gray-800 dark:text-white"
          >
            <option value="light">☀️ Light</option>
            <option value="dark">🌙 Dark</option>
          </select>
        </div>
      </div>
    </header>

    <!-- 📂 Navigation Links (Role-Based) -->
    <nav class="max-w-7xl mx-auto px-6 py-4 flex flex-wrap gap-4 text-blue-700 dark:text-yellow-300">
      <router-link v-if="isLoggedIn" to="/dashboard" class="hover:underline">📊 Dashboard</router-link>
      <router-link v-if="role === 'admin'" to="/dashboard/admin" class="hover:underline">🛠️ Admin Panel</router-link>
      <router-link v-if="role === 'owner'" to="/dashboard/owner" class="hover:underline">👑 Owner Controls</router-link>
    </nav>

    <!-- 🧩 Main App View -->
    <main class="max-w-7xl mx-auto px-6 py-10">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import UserGreeting from './components/UserGreeting.vue'
import LanguageSwitcher from './components/LanguageSwitcher.vue'

// 🌗 Theme state (with fallback)
const detectSystemTheme = () =>
  window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'

const theme = ref(localStorage.getItem('theme') || detectSystemTheme())
const themeClass = computed(() => (theme.value === 'dark' ? 'theme-dark' : 'theme-light'))

const switchTheme = () => {
  localStorage.setItem('theme', theme.value)
  document.body.className = themeClass.value
}

onMounted(() => {
  document.body.className = themeClass.value
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      theme.value = e.matches ? 'dark' : 'light'
      document.body.className = themeClass.value
    }
  })
})

// 🔐 Auth & Role
const isLoggedIn = ref(!!localStorage.getItem('access_token'))
const role = ref(localStorage.getItem('user_role') || '')
</script>

<style scoped>
/* 🌈 Light/Dark theme support */
.theme-light {
  --bg-color: #ffffff;
  --text-color: #111111;
}
.theme-dark {
  --bg-color: #0d1117;
  --text-color: #f0f0f0;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: background-color 0.3s ease;
}
</style>
