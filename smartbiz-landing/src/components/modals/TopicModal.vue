<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
    <div class="bg-white rounded-xl shadow-lg p-6 w-full max-w-md">
      <h2 class="text-lg font-bold mb-4 text-black">🗣️ Add Stream Topic</h2>
      <input
        v-model="topic"
        type="text"
        placeholder="Enter a topic (e.g., Let's talk business!)"
        class="w-full px-4 py-2 border rounded mb-4"
      />
      <div class="flex justify-end gap-2">
        <button @click="close" class="px-4 py-2 rounded bg-gray-200 hover:bg-gray-300 text-sm">Cancel</button>
        <button @click="submitTopic" class="px-4 py-2 rounded bg-yellow-500 hover:bg-yellow-400 text-white text-sm">Save</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['close'])

const topic = ref('')

function close() {
  emit('close')
}

function submitTopic() {
  if (topic.value.trim() !== '') {
    console.log('New topic set:', topic.value)
    emit('close')
  }
}
</script>

<style scoped>
/* Optional: You can add animations here */
</style>
