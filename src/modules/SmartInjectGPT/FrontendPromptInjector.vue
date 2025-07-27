<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white rounded-xl shadow-xl p-6 dark:bg-[#0e1a2b] text-gray-800 dark:text-white">
    <h2 class="text-2xl font-bold mb-4 text-blue-600 dark:text-yellow-400">💡 SmartInjectGPT Prompt Interface</h2>
    
    <textarea
      v-model="userPrompt"
      placeholder="Andika ndoto au kipengele unachotaka kujengwa hapa..."
      class="w-full p-4 rounded-md bg-gray-100 dark:bg-[#1e2e3e] text-lg focus:outline-none"
      rows="5"
    />

    <button
      @click="sendPrompt"
      :disabled="loading"
      class="mt-4 px-6 py-2 bg-blue-600 text-white font-semibold rounded hover:bg-blue-700 disabled:opacity-50"
    >
      {{ loading ? '⏳ Inachakata...' : '🚀 Tuma kwa SmartInjectGPT' }}
    </button>

    <div v-if="response" class="mt-6 p-4 bg-green-100 dark:bg-green-900 rounded text-sm">
      <strong>✅ Jibu la Kernel:</strong><br />
      {{ response }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const userPrompt = ref('')
const response = ref('')
const loading = ref(false)

const sendPrompt = async () => {
  if (!userPrompt.value.trim()) return
  loading.value = true
  response.value = ''

  try {
    const res = await axios.post('/api/smartinject/run', {
      prompt: userPrompt.value
    })
    response.value = res.data?.message || 'Imefanikiwa!'
  } catch (error) {
    response.value = '⚠️ Imeshindwa kuwasiliana na kernel.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
textarea {
  resize: vertical;
}
</style>
