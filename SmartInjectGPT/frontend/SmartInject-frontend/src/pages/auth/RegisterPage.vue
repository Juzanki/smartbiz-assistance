<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-tr from-[#1f2937] to-[#0f172a] p-6">
    <div class="bg-white dark:bg-[#111827] shadow-2xl rounded-2xl w-full max-w-lg p-6 space-y-6 border border-yellow-500">
      <div class="text-center">
        <!-- Uploadable Logo Placeholder -->
        <label class="cursor-pointer block mb-4">
          <input type="file" @change="handleLogoUpload" accept="image/*" hidden />
          <img :src="logoUrl" alt="SmartInjectGPT Logo" class="mx-auto h-20 w-20 object-cover rounded-full shadow border border-yellow-400 bg-white" />
          <span class="text-xs text-gray-400 mt-2 inline-block">Click to upload logo</span>
        </label>

        <h2 class="text-2xl font-bold text-gray-800 dark:text-yellow-400 mt-2">Create an Account</h2>
        <p class="text-sm text-gray-500 dark:text-gray-300">Join the SmartInjectGPT mission</p>
      </div>

      <form @submit.prevent="register" class="space-y-4">
        <div>
          <label class="block text-sm text-gray-700 dark:text-gray-300">Full Name</label>
          <input v-model="form.name" type="text" required placeholder="Jane Doe"
            class="w-full p-2 rounded bg-gray-50 dark:bg-[#1e293b] border focus:ring-2 focus:ring-yellow-400 dark:text-white" />
        </div>

        <div>
          <label class="block text-sm text-gray-700 dark:text-gray-300">Email</label>
          <input v-model="form.email" type="email" required placeholder="you@example.com"
            class="w-full p-2 rounded bg-gray-50 dark:bg-[#1e293b] border focus:ring-2 focus:ring-yellow-400 dark:text-white" />
        </div>

        <div>
          <label class="block text-sm text-gray-700 dark:text-gray-300">Password</label>
          <input v-model="form.password" type="password" required placeholder="••••••••"
            class="w-full p-2 rounded bg-gray-50 dark:bg-[#1e293b] border focus:ring-2 focus:ring-yellow-400 dark:text-white" />
        </div>

        <div>
          <label class="block text-sm text-gray-700 dark:text-gray-300">Confirm Password</label>
          <input v-model="form.confirm" type="password" required placeholder="••••••••"
            class="w-full p-2 rounded bg-gray-50 dark:bg-[#1e293b] border focus:ring-2 focus:ring-yellow-400 dark:text-white" />
        </div>

        <button type="submit" class="w-full bg-yellow-400 hover:bg-yellow-300 text-dark font-bold py-2 rounded transition">
          ✨ Create Account
        </button>
      </form>

      <p class="text-xs text-center text-gray-500 dark:text-gray-400 mt-4">
        Already have an account? <router-link to="/login" class="text-yellow-400 hover:underline">Login</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({ name: '', email: '', password: '', confirm: '' })
const logoUrl = ref('/logo.svg')

const handleLogoUpload = (e) => {
  const file = e.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (event) => {
      logoUrl.value = event.target.result
    }
    reader.readAsDataURL(file)
  }
}

const register = () => {
  if (form.value.password !== form.value.confirm) {
    alert('❌ Passwords do not match')
    return
  }

  // Simulate success — Replace with actual API integration
  alert(`🎉 Welcome, ${form.value.name}!`)
  router.push('/register-confirmation')
}
</script>

<style scoped>
body {
  font-family: 'Fira Code', monospace;
  transition: all 0.3s ease;
}
</style>
