<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-[#0a0f1a] to-[#1e293b] px-4 py-10">
    <div class="w-full max-w-md bg-white dark:bg-[#111827] shadow-xl rounded-3xl p-8 border border-yellow-500 transition-all duration-300">
      
      <!-- Logo + Title -->
      <div class="text-center mb-6">
        <img
          src="/logo.svg"
          alt="SmartInjectGPT Logo"
          class="mx-auto h-20 w-20 rounded-full border border-yellow-400 shadow-lg bg-white object-contain"
        />
        <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-yellow-400 mt-4">SmartInjectGPT Login</h2>
        <p class="text-sm text-gray-500 dark:text-gray-300">Command Center Access</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="login" class="space-y-5">
        <div>
          <label class="block text-sm text-gray-700 dark:text-gray-200 mb-1">Email</label>
          <input
            v-model="email"
            type="email"
            required
            placeholder="admin@smartinject.ai"
            class="w-full px-4 py-2 rounded-lg bg-gray-50 dark:bg-[#1e293b] border border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-yellow-400 text-sm dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm text-gray-700 dark:text-gray-200 mb-1">Password</label>
          <input
            v-model="password"
            type="password"
            required
            placeholder="••••••••"
            class="w-full px-4 py-2 rounded-lg bg-gray-50 dark:bg-[#1e293b] border border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-yellow-400 text-sm dark:text-white"
          />
        </div>

        <div class="flex items-center justify-between text-sm">
          <label class="inline-flex items-center text-gray-600 dark:text-gray-300">
            <input type="checkbox" v-model="remember" class="mr-2 rounded" /> Remember me
          </label>
          <router-link to="/forgot-password" class="text-yellow-400 hover:underline">Forgot?</router-link>
        </div>

        <button
          type="submit"
          class="w-full py-2 rounded-lg bg-yellow-400 text-dark font-bold text-sm hover:bg-yellow-300 transition shadow">
          🔐 Login Now
        </button>
      </form>

      <!-- Footer Message -->
      <p class="text-center text-xs text-gray-400 dark:text-gray-500 mt-6">
        Don't have access? Contact the SmartBiz Owner.
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const remember = ref(false)
const router = useRouter()

const login = () => {
  if (email.value === 'owner@smartinject.ai' && password.value === '123456') {
    localStorage.setItem('access_token', 'owner-token')
    localStorage.setItem('user_role', 'owner')
    router.push('/dashboardOwner')
  } else if (email.value === 'admin@smartinject.ai' && password.value === 'admin123') {
    localStorage.setItem('access_token', 'admin-token')
    localStorage.setItem('user_role', 'admin')
    router.push('/admin')
  } else {
    alert('❌ Invalid credentials. Please check and try again.')
  }
}
</script>

<style scoped>
body {
  font-family: 'Fira Code', monospace;
}
</style>
