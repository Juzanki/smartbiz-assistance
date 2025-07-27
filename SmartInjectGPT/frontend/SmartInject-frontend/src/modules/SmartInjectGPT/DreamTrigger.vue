<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg mt-6">
    <h3 class="text-xl font-bold mb-4 text-blue-600 dark:text-yellow-400">🌙 Dream Trigger</h3>

    <textarea
      v-model="dream"
      placeholder="Andika ndoto au maono unayotaka AI ijenge mfano: 'Nahitaji mfumo wa AI wa maombi ya harusi kwa mkoa wa Kagera...'"
      class="w-full p-4 rounded bg-gray-100 dark:bg-[#1e2e3e] text-sm focus:outline-none"
      rows="5"
    ></textarea>

    <button
      @click="sendDream"
      :disabled="!dream.trim()"
      class="mt-4 px-6 py-2 bg-purple-600 text-white font-semibold rounded hover:bg-purple-700 disabled:opacity-50"
    >
      ✨ Tuma Ndoto kwa Kernel
    </button>

    <div v-if="result" class="mt-4 text-green-500 dark:text-green-300 text-sm">
      ✅ {{ result }}
    </div>
    <div v-if="error" class="mt-4 text-red-500 dark:text-red-300 text-sm">
      ⚠️ {{ error }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const dream = ref('')
const result = ref('')
const error = ref('')

const sendDream = async () => {
  result.value = ''
  error.value = ''
  try {
    const res = await axios.post('http://localhost:8000/api/smartinject/dream', {
      dream: dream.value
    })
    result.value = res.data?.message || 'Imefanikiwa.'
  } catch (err) {
    error.value = 'Imeshindwa kutuma ndoto kwa kernel.'
  }
}
</script>
