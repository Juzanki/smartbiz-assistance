<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg mt-6">
    <h3 class="text-xl font-bold mb-4 text-blue-600 dark:text-yellow-400">📈 Auto Feedback & Self-Learning</h3>

    <button
      @click="runFeedback"
      :disabled="loading"
      class="px-6 py-2 bg-emerald-600 text-white rounded hover:bg-emerald-700 disabled:opacity-50"
    >
      {{ loading ? '⏳ Inapima...' : '📊 Pima Mafanikio ya Injection' }}
    </button>

    <div v-if="report" class="mt-4 text-sm p-4 bg-gray-100 dark:bg-[#1b2c3a] rounded">
      <p><strong>📁 Module:</strong> {{ report.module }}</p>
      <p><strong>✅ Mafanikio:</strong> {{ report.success }}</p>
      <p><strong>🧠 Maoni ya AI:</strong></p>
      <pre class="whitespace-pre-wrap text-gray-800 dark:text-gray-300 mt-1">{{ report.ai_feedback }}</pre>
    </div>

    <div v-if="error" class="mt-4 text-red-500 dark:text-red-300 text-sm">
      ⚠️ {{ error }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const loading = ref(false)
const report = ref(null)
const error = ref('')

const runFeedback = async () => {
  loading.value = true
  report.value = null
  error.value = ''

  try {
    const res = await axios.get('http://localhost:8000/api/smartinject/feedback')
    report.value = res.data
  } catch (err) {
    error.value = 'Imeshindwa kupata ripoti ya AI.'
  } finally {
    loading.value = false
  }
}
</script>
