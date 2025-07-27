<template>
  <div class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center">
    <div class="bg-white rounded-xl p-6 w-[90vw] max-w-sm text-black shadow-xl relative">
      <h2 class="text-lg font-bold text-pink-600 mb-4">💬 Send SuperChat</h2>

      <input
        v-model="message"
        type="text"
        class="w-full border px-4 py-2 rounded mb-3"
        placeholder="Enter your SuperChat message"
      />
      <input
        v-model.number="amount"
        type="number"
        class="w-full border px-4 py-2 rounded mb-4"
        placeholder="Amount (Coins)"
      />

      <div class="flex justify-between">
        <button @click="send" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Send</button>
        <button @click="$emit('close')" class="text-gray-500 hover:underline">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['close', 'send'])

const message = ref('')
const amount = ref(10)

const send = () => {
  if (!message.value.trim()) {
    alert('Please enter a message.')
    return
  }
  emit('send', { message: message.value, amount: amount.value })
  emit('close')
}
</script>
