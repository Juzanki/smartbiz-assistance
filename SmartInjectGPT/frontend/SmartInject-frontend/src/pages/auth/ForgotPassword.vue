<template>
  <div class="min-h-screen flex items-center justify-center bg-[#0a0f1a] text-light font-mono px-4">
    <div class="w-full max-w-md bg-dark-800 p-8 rounded-2xl shadow-lg border border-yellow-400">
      <h2 class="text-yellow-400 text-2xl font-bold text-center mb-6">Forgot Password?</h2>

      <form @submit.prevent="submit" class="space-y-4">
        <div>
          <label class="text-sm block mb-1">Email Address</label>
          <input
            v-model="email"
            type="email"
            required
            placeholder="Enter your account email"
            class="w-full p-2 rounded bg-dark-700 text-light border border-gray-600"
          />
        </div>

        <div>
          <label class="text-sm block mb-1">Verification Code</label>
          <div class="flex gap-2">
            <input
              v-model="code"
              type="text"
              placeholder="Enter code"
              class="flex-1 p-2 rounded bg-dark-700 text-light border border-gray-600"
            />
            <button
              type="button"
              @click="sendCode"
              class="bg-yellow-400 text-dark font-bold px-3 rounded hover:bg-yellow-300"
            >
              Send Code
            </button>
          </div>
        </div>

        <div>
          <label class="text-sm block mb-1">New Password</label>
          <input
            v-model="newPassword"
            type="password"
            required
            placeholder="Enter new password"
            class="w-full p-2 rounded bg-dark-700 text-light border border-gray-600"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-yellow-400 text-dark font-bold py-2 rounded hover:bg-yellow-300 transition"
        >
          Reset Password
        </button>
      </form>

      <p class="text-xs text-center text-gray-400 mt-6">
        If you no longer have access to the email, contact the owner manually.
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const code = ref('')
const newPassword = ref('')
const router = useRouter()

const sendCode = () => {
  if (!email.value) return alert('Enter your email first.')
  // Simulate sending email
  alert(`Verification code sent to ${email.value}`)
  // In production, send via backend API
}

const submit = () => {
  if (!code.value || code.value !== '123456') {
    alert('Invalid or expired code')
    return
  }

  alert('✅ Password reset successful.')
  router.push('/login')
}
</script>

<style scoped>
body {
  font-family: 'Fira Code', monospace;
}
</style>
