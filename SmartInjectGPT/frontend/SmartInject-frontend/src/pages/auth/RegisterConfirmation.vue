<template>
  <div class="min-h-screen bg-[#0a0f1a] text-light flex items-center justify-center font-mono px-4">
    <div class="w-full max-w-md bg-dark-800 p-8 rounded-2xl shadow-xl border border-yellow-400 text-center animate-fade-in">
      <div class="text-4xl mb-4 text-yellow-400">✅</div>
      <h2 class="text-2xl font-bold text-yellow-400 mb-2">Registration Successful!</h2>
      <p class="text-sm text-gray-400 mb-6 leading-relaxed">
        You have successfully created your <span class="text-yellow-400 font-mono">{{ role.toUpperCase() }}</span> account.<br />
        You can now log in and begin using SmartInjectGPT securely.
      </p>

      <router-link
        to="/login"
        class="inline-block bg-yellow-400 text-dark font-bold px-6 py-2 rounded hover:bg-yellow-300 transition"
      >
        Proceed to Login
      </router-link>

      <p class="text-xs text-gray-500 mt-4">If you’re not redirected in 10 seconds, click the button above.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const role = ref('user')
const router = useRouter()

onMounted(() => {
  role.value = localStorage.getItem('user_role') || 'user'

  // Optional auto-redirect after delay
  setTimeout(() => {
    router.push('/login')
  }, 10000)
})
</script>

<style scoped>
/* Animation */
@keyframes fade-in {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.animate-fade-in {
  animation: fade-in 0.6s ease-out;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
