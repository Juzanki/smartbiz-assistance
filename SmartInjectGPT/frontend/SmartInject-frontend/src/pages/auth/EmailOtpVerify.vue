<template>
  <div class="min-h-screen bg-[#0a0f1a] text-light flex items-center justify-center px-4 font-mono">
    <div class="w-full max-w-md bg-dark-800 p-8 rounded-2xl shadow-lg border border-yellow-400 text-center">
      <div class="text-3xl mb-4 text-yellow-400">📩</div>
      <h2 class="text-xl font-bold text-yellow-400 mb-2">Email Verification</h2>
      <p class="text-sm text-gray-400 mb-6">
        A verification code has been sent to your email.<br />
        Please enter the code to continue.
      </p>

      <form @submit.prevent="verify" class="space-y-4">
        <input
          v-model="otp"
          type="text"
          maxlength="6"
          required
          placeholder="Enter 6-digit code"
          class="w-full p-2 rounded bg-dark-700 text-light border border-gray-600 text-center tracking-widest text-lg"
        />

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-yellow-400 text-dark font-bold py-2 rounded hover:bg-yellow-300 transition disabled:opacity-60"
        >
          {{ loading ? 'Verifying...' : 'Verify' }}
        </button>
      </form>

      <div class="text-xs text-gray-500 mt-4">
        Didn't receive it?
        <button
          @click="resend"
          :disabled="resending"
          class="text-yellow-400 hover:underline ml-1"
        >
          {{ resending ? 'Sending...' : 'Resend Code' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const otp = ref('')
const loading = ref(false)
const resending = ref(false)
const router = useRouter()

const verify = async () => {
  if (!otp.value || otp.value.length !== 6) {
    alert('⚠️ Please enter a valid 6-digit code.')
    return
  }

  loading.value = true

  try {
    // TODO: Replace with real API call
    await new Promise(resolve => setTimeout(resolve, 1000))

    if (otp.value === '123456') {
      alert('✅ Email verified successfully.')
      router.push('/login')
    } else {
      alert('❌ Invalid code. Please try again.')
    }
  } catch (err) {
    alert('❌ Verification failed. Please try again later.')
  } finally {
    loading.value = false
  }
}

const resend = async () => {
  resending.value = true

  try {
    // TODO: Replace with real backend API call
    await new Promise(resolve => setTimeout(resolve, 1500))
    alert('📧 New code has been sent to your email.')
  } catch (err) {
    alert('⚠️ Failed to resend. Please try again.')
  } finally {
    resending.value = false
  }
}
</script>

<style scoped>
input::placeholder {
  color: #999;
  font-size: 1rem;
}
</style>
