<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#0a0f1a] text-light text-center px-4 font-mono">
    <!-- Warning Icon -->
    <div class="text-red-500 text-6xl animate-pulse mb-4">⛔</div>

    <!-- Title -->
    <h1 class="text-2xl sm:text-3xl font-bold text-yellow-400 mb-2">403 - Unauthorized Access</h1>

    <!-- Message -->
    <p class="text-gray-400 max-w-md mb-6 text-sm sm:text-base">
      Your current role does not have permission to access this panel.<br />
      This incident has been logged for intelligent security analysis.
    </p>

    <!-- Diagnostic Info -->
    <div class="text-xs sm:text-sm text-gray-500 mb-6 space-y-1">
      <p><strong>🧾 Detected Role:</strong> <span class="text-yellow-400">{{ roleDisplay || 'N/A' }}</span></p>
      <p><strong>🎯 Expected Role:</strong> <span class="text-yellow-400">{{ expectedRole }}</span></p>
      <p><strong>🛰 Fingerprint:</strong> {{ fingerprint.slice(0, 25) }}...</p>
      <p><strong>⏳ Auto-redirecting to login in {{ countdown }}s...</strong></p>
      <div class="w-40 h-1 bg-gray-700 rounded overflow-hidden mx-auto">
        <div
          class="h-full bg-red-500 transition-all duration-1000"
          :style="{ width: `${(countdown / 10) * 100}%` }"
        ></div>
      </div>
    </div>

    <!-- Action Button -->
    <router-link
      to="/login"
      class="bg-yellow-400 text-dark font-semibold px-4 py-2 rounded hover:bg-yellow-300 transition"
    >
      🔐 Go to Login
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const countdown = ref(10)
const expectedRole = route.query.role || 'owner'
const roleDisplay = localStorage.getItem('user_role')
const fingerprint = localStorage.getItem('fingerprint') || 'unknown'

onMounted(() => {
  const interval = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(interval)
      localStorage.clear()
      router.push('/login')
    }
  }, 1000)
})
</script>

<style scoped>
/* Hakuna haja ya ku-overwrite `body` hapa – inasimamiwa globally na theme system */
</style>
