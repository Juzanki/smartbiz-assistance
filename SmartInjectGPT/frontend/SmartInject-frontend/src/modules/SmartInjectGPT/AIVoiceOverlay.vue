<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg mt-6">
    <h3 class="text-xl font-bold mb-3 text-blue-600 dark:text-yellow-400">🔊 AI Voice Reader</h3>

    <textarea
      v-model="textToRead"
      placeholder="Andika au bandika ujumbe wa kusomewa..."
      class="w-full p-3 rounded bg-gray-100 dark:bg-[#1e2e3e] text-sm focus:outline-none"
      rows="4"
    ></textarea>

    <button
      @click="readAloud"
      :disabled="!textToRead.trim()"
      class="mt-3 px-6 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 disabled:opacity-50"
    >
      🔈 Soma Kwa Sauti
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const textToRead = ref('')

const readAloud = () => {
  const utterance = new SpeechSynthesisUtterance(textToRead.value)
  utterance.lang = 'sw-TZ' // Unaweza kubadilisha kwa 'en-US', 'fr-FR', nk.
  utterance.rate = 1
  utterance.pitch = 1
  speechSynthesis.speak(utterance)
}
</script>
