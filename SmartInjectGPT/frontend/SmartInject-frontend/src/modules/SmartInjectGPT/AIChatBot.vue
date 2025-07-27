<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg mt-6">
    <h3 class="text-xl font-bold mb-4 text-blue-600 dark:text-yellow-400">🤖 SmartInjectGPT Assistant Bot</h3>

    <div class="flex flex-col gap-2">
      <div v-for="(item, index) in chat" :key="index" class="text-sm p-3 rounded bg-gray-100 dark:bg-[#1b2c3a]">
        <strong v-if="item.role === 'user'" class="text-blue-600">🧑‍💻 Wewe:</strong>
        <strong v-else class="text-purple-400">🤖 AI:</strong>
        <div class="mt-1 whitespace-pre-wrap">{{ item.message }}</div>
      </div>
    </div>

    <textarea
      v-model="userInput"
      placeholder="Andika swali au ombi lako hapa..."
      class="w-full p-3 mt-4 rounded bg-gray-100 dark:bg-[#1e2e3e] text-sm focus:outline-none"
      rows="3"
      @keydown.enter.prevent="askBot"
    ></textarea>

    <button
      @click="askBot"
      :disabled="!userInput.trim()"
      class="mt-2 px-6 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 disabled:opacity-50"
    >
      🗣 Tuma kwa Bot
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const userInput = ref('')
const chat = ref([])

const askBot = async () => {
  const question = userInput.value.trim()
  if (!question) return

  // Ongeza user message kwenye chat history
  chat.value.push({ role: 'user', message: question })
  userInput.value = ''

  try {
    const res = await axios.post('http://localhost:8000/api/smartinject/chat', {
      message: question
    })
    const aiResponse = res.data?.reply || '⚠️ AI haikujibu.'
    chat.value.push({ role: 'bot', message: aiResponse })
  } catch (err) {
    chat.value.push({ role: 'bot', message: '❌ AI haikuweza kujibu kwa sasa.' })
  }
}
</script>
