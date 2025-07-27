<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg">
    <h3 class="text-xl font-bold mb-3 text-blue-600 dark:text-yellow-400">🚀 Auto Deploy Console</h3>

    <button
      @click="deploy"
      :disabled="loading"
      class="px-5 py-2 bg-green-600 text-white font-semibold rounded hover:bg-green-700 disabled:opacity-50"
    >
      {{ loading ? '⏳ Inatuma...' : '📤 Deploy Now' }}
    </button>

    <div v-if="response" class="mt-4 text-sm p-3 rounded bg-gray-100 dark:bg-[#1b2c3a] text-green-500 dark:text-green-300">
      ✅ {{ response }}
    </div>

    <div v-if="error" class="mt-4 text-sm p-3 rounded bg-red-100 dark:bg-red-900 text-red-600 dark:text-red-300">
      ⚠️ {{ error }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const loading = ref(false)
const response = ref('')
const error = ref('')

const deploy = async () => {
  loading.value = true
  response.value = ''
  error.value = ''

  try {
    const res = await axios.post('http://localhost:8000/api/smartinject/deploy', {
      path: 'SmartInjectGPT/generated/live_system/'
    })

    if (res.data?.status === '✅ Deployed') {
      response.value = res.data.details.feature + ' deployed to ' + res.data.details.env
    } else {
      error.value = res.data.message || 'Deployment failed.'
    }
  } catch (err) {
    error.value = 'Hakuna mawasiliano na server ya kernel.'
  } finally {
    loading.value = false
  }
}
</script>
