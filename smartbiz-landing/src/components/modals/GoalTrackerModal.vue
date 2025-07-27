<template>
  <div class="fixed inset-0 bg-black/60 flex items-center justify-center z-50">
    <div class="bg-white p-6 rounded-xl shadow-lg max-w-md w-full">
      <h2 class="text-lg font-bold mb-4">🎯 Lengo la Muda Halisi</h2>
      <form @submit.prevent="submitGoal">
        <label class="block mb-2 font-medium">Lengo:</label>
        <input v-model="goalText" type="text" class="w-full p-2 border border-gray-300 rounded mb-4" placeholder="Mfano: Fikia watazamaji 1,000" />

        <label class="block mb-2 font-medium">Thamani:</label>
        <input v-model="goalValue" type="number" class="w-full p-2 border border-gray-300 rounded mb-4" />

        <div class="flex justify-end gap-2">
          <button type="button" @click="$emit('close')" class="text-gray-600 hover:text-black text-sm">✖️ Funga</button>
          <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded">✅ Hifadhi</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const goalText = ref('')
const goalValue = ref(0)

function submitGoal() {
  console.log('🚀 Lengo Limesetwa:', goalText.value, goalValue.value)
  // Hapa unaweza kutuma data backend au kui-display mahali pengine
  goalText.value = ''
  goalValue.value = 0
  // Funga modal
  emit('close')
}
const emit = defineEmits(['close'])
</script>
