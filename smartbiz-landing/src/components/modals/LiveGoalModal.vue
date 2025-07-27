<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
    <div class="bg-white rounded-xl shadow-lg p-6 w-full max-w-md">
      <h2 class="text-lg font-bold mb-4 text-black">🎯 Set a Live Goal</h2>
      <input
        v-model="goal"
        type="text"
        placeholder="Enter your goal (e.g., 1K Likes)"
        class="w-full px-4 py-2 border rounded mb-4"
      />
      <div class="flex justify-end gap-2">
        <button @click="close" class="px-4 py-2 rounded bg-gray-200 hover:bg-gray-300 text-sm">Cancel</button>
        <button @click="submitGoal" class="px-4 py-2 rounded bg-indigo-600 hover:bg-indigo-500 text-white text-sm">Save</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['close'])

const goal = ref('')

function close() {
  emit('close')
}

function submitGoal() {
  if (goal.value.trim() !== '') {
    console.log('Live Goal Set:', goal.value)
    emit('close')
  }
}
</script>

<style scoped>
/* Optional custom styling */
</style>
