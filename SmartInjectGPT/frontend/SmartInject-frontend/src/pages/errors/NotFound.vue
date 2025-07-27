<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#0a0f1a] text-light text-center px-6 font-mono">
    <!-- Icon -->
    <div class="text-yellow-400 text-6xl animate-bounce mb-4">⚠️</div>

    <!-- Main Message -->
    <h1 class="text-3xl sm:text-4xl font-bold text-yellow-400 mb-2">404 — Page Not Found</h1>
    <p class="text-gray-400 max-w-md mb-6 text-sm sm:text-base">
      The page you are looking for might have been removed, renamed, or is temporarily unavailable.
    </p>

    <!-- Extra Info -->
    <div class="text-xs sm:text-sm text-gray-500 mb-6">
      <p><strong>Requested Path:</strong> {{ path }}</p>
      <p><strong>Auto-redirecting in {{ countdown }}s...</strong></p>
      <div class="w-40 h-1 mt-2 bg-gray-700 rounded overflow-hidden mx-auto">
        <div
          class="h-full bg-yellow-400 transition-all duration-1000"
          :style="{ width: `${(countdown / 10) * 100}%` }"
        ></div>
      </div>
    </div>

    <!-- Button -->
    <router-link
      to="/"
      class="bg-yellow-400 text-dark font-bold px-4 py-2 rounded hover:bg-yellow-300 transition"
    >
      Go to Home
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const path = route.fullPath
const countdown = ref(10)

onMounted(() => {
  const timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(timer)
      router.push('/')
    }
  }, 1000)
})
</script>

<style scoped>
/* Hakuna haja ya kuweka `body {}` hapa kwani global theme-dark inashughulikia */
</style>
