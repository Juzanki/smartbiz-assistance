<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-[#0e1a2b] text-gray-800 dark:text-white rounded-xl shadow-xl p-6 space-y-6">
    <h2 class="text-2xl font-bold text-blue-600 dark:text-yellow-400">💡 SmartInjectGPT Prompt Interface</h2>

    <textarea
      v-model="userPrompt"
      placeholder="Describe the dream or feature you want the AI to build..."
      class="w-full p-4 rounded-md bg-gray-100 dark:bg-[#1e2e3e] text-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
      rows="5"
    />

    <button
      @click="sendPrompt"
      :disabled="loading || !userPrompt.trim()"
      class="w-full py-3 px-6 text-white font-bold rounded bg-blue-600 hover:bg-blue-700 disabled:opacity-40"
    >
      {{ loading ? '⏳ Sending to SmartInjectGPT...' : '🚀 Submit Prompt' }}
    </button>

    <!-- Kernel Response -->
    <div v-if="response" class="mt-4 p-4 text-sm rounded" :class="responseStatusClass">
      <strong class="block mb-1">{{ responsePrefix }}</strong>
      <pre class="whitespace-pre-wrap break-words">{{ response }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'

const userPrompt = ref('')
const response = ref('')
const loading = ref(false)

const responsePrefix = computed(() =>
  response.value.startsWith('✅') ? '✅ Kernel Response:' :
  response.value.startsWith('❌') ? '❌ Error:' :
  'ℹ️ Response:'
)

const responseStatusClass = computed(() => {
  if (response.value.startsWith('✅')) return 'bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300'
  if (response.value.startsWith('❌')) return 'bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-300'
  return 'bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-300'
})

const sendPrompt = async () => {
  if (!userPrompt.value.trim()) return
  loading.value = true
  response.value = ''

  try {
    const res = await axios.post('/api/smartinject/run', {
      prompt: userPrompt.value
    })
    response.value = res.data?.message || '✅ Successfully executed by Kernel.'
  } catch (error) {
    response.value = '❌ Failed to contact SmartInjectGPT kernel.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
textarea {
  resize: vertical;
  transition: box-shadow 0.2s ease;
}
</style>
