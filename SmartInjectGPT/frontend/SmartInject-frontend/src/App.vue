<template>
  <div :class="themeClass" class="min-h-screen flex flex-col transition-all ease-in-out duration-300">
    <!-- Navbar -->
    <header class="bg-[#0c1021] text-white px-4 py-3 shadow-md flex items-center justify-between">
      <!-- Logo & Title -->
      <div class="flex items-center gap-3">
        <img
          src="/logo.svg"
          alt="SmartInjectGPT Logo"
          class="w-10 h-10 rounded-full border-2 border-yellow-400 bg-white shadow"
        />
        <h1 class="text-yellow-400 font-bold text-lg sm:text-xl">SmartInjectGPT</h1>
      </div>

      <!-- Controls -->
      <div class="flex items-center gap-3 text-sm">
        <!-- Language (placeholder) -->
        <span class="text-gray-400 italic">🌐 EN</span>

        <!-- Theme Switch -->
        <select
          v-model="theme"
          @change="switchTheme"
          class="bg-[#1b1e2f] text-white border border-gray-500 rounded px-2 py-1"
        >
          <option value="light">☀️ Light</option>
          <option value="dark">🌙 Dark</option>
        </select>
      </div>
    </header>

    <!-- Navigation -->
    <nav class="flex flex-wrap gap-4 px-4 py-2 bg-[#13182c] text-yellow-300 text-sm border-b border-yellow-600">
      <router-link
        v-if="isLoggedIn"
        to="/dashboardOwner"
        class="hover:text-white transition"
      >
        📊 Dashboard
      </router-link>
      <router-link
        v-if="role === 'admin'"
        to="/manage-admins"
        class="hover:text-white transition"
      >
        🛠 Admin Panel
      </router-link>
      <router-link
        v-if="role === 'owner'"
        to="/systemSettings"
        class="hover:text-white transition"
      >
        👑 Owner Controls
      </router-link>
    </nav>

    <!-- Main Content -->
    <main class="flex-1 px-4 py-6 bg-[var(--bg-color)] text-[var(--text-color)]">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="text-center text-xs text-gray-400 py-4 bg-[#0c1021]">
      © {{ year }} SmartInjectGPT — All rights reserved.
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const year = new Date().getFullYear()

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
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (!localStorage.getItem('theme')) {
      theme.value = e.matches ? 'dark' : 'light'
      document.body.className = themeClass.value
    }
  })
})

const isLoggedIn = ref(!!localStorage.getItem('access_token'))
const role = ref(localStorage.getItem('user_role')?.toLowerCase() || '')
</script>

<style>
/* Theme Variables */
.theme-light {
  --bg-color: #f9fafb;
  --text-color: #111827;
}
.theme-dark {
  --bg-color: #0a0f1a;
  --text-color: #e0e1dd;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  font-family: 'Fira Code', monospace;
  transition: background-color 0.3s ease, color 0.3s ease;
  margin: 0;
}
</style>
