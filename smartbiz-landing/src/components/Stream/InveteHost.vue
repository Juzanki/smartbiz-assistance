<template>
  <div class="w-full flex flex-col sm:flex-row items-stretch sm:items-center gap-3 mb-6">
    <input
      v-model="email"
      type="email"
      placeholder="Enter host email..."
      class="flex-1 rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400 transition"
    />
    <button
      @click="emitInvite"
      class="bg-indigo-600 text-white px-5 py-2 rounded-lg font-semibold hover:bg-indigo-700 transition button-press"
    >
      ➕ Invite
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const email = ref('')

const emit = defineEmits(['invite'])

const emitInvite = () => {
  const trimmed = email.value.trim()
  if (!trimmed || !trimmed.includes('@')) {
    alert('Please enter a valid email address.')
    return
  }
  emit('invite', trimmed)
  email.value = ''
}
</script>

<style scoped>
.button-press {
  transition: transform 0.2s ease;
}
.button-press:active {
  transform: scale(0.96);
}
</style>

