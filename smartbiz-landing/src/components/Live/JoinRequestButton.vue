<template>
  <div class="fixed bottom-4 right-4 z-40">
    <button
      :disabled="requested"
      @click="sendRequest"
      class="bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2 rounded-full shadow-lg text-sm transition"
    >
      <span v-if="!requested">🙋‍♂️ Request to Join</span>
      <span v-else-if="countdown > 0">⏳ Wait {{ countdown }}s</span>
      <span v-else>🔁 Retry?</span>
    </button>

    <!-- Smart Message -->
    <p v-if="smartMessage" class="mt-2 text-white text-xs text-center bg-black/50 rounded px-2 py-1">
      🤖 {{ smartMessage }}
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Emit request to parent
const emit = defineEmits(['request-sent', 'notify-host'])

// States
const requested = ref(false)
const countdown = ref(0)
const smartMessage = ref('')
const retryDelay = 20 // seconds

let countdownInterval = null

const sendRequest = () => {
  const streamIsFull = false // 🧠 Replace this with real logic if needed

  if (streamIsFull) {
    smartMessage.value = 'All guest slots are full. Please try again later.'
    return
  }

  emit('request-sent', {
    name: 'You (Guest)',
    avatar: '/you-avatar.png',
    timestamp: Date.now()
  })

  emit('notify-host') // 🔔 notify for sound on host side

  requested.value = true
  smartMessage.value = 'Request sent to host. Please wait...'

  // Start Retry countdown
  countdown.value = retryDelay
  countdownInterval = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(countdownInterval)
      smartMessage.value = 'No response. You may retry.'
      requested.value = false
    }
  }, 1000)
}
</script>
