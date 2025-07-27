<template>
  <div class="min-h-screen flex items-center justify-center bg-dark text-light">
    <div class="p-6 bg-dark-800 rounded-xl shadow-lg border border-yellow-400 text-center">
      <h2 class="text-yellow-400 text-2xl fw-bold mb-3">Logging Out...</h2>
      <div class="spinner-border text-warning mb-3" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <p class="text-sm text-gray-400">Redirecting to login page shortly...</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  // Clear all tokens and sensitive data
  localStorage.removeItem('access_token')
  localStorage.removeItem('user_role')
  localStorage.removeItem('fingerprint')
  localStorage.removeItem('session_token')
  localStorage.removeItem('lang')

  // Optional: clear everything
  // localStorage.clear()

  // Redirect after short delay
  setTimeout(() => {
    router.push('/login')
  }, 1500)
})
</script>

<style scoped>
.bg-dark {
  background-color: #0a0f1a;
}

.bg-dark-800 {
  background-color: #1f2733;
}

.text-light {
  color: #f8f9fa;
}
</style>
