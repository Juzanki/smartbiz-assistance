<template>
  <div
    v-if="status === 'full' || status === 'next'"
    class="absolute top-4 right-4 z-40 bg-gradient-to-r from-purple-600 via-pink-500 to-red-500 text-white text-xs font-semibold px-3 py-1 rounded-full shadow-lg backdrop-blur-sm"
  >
    <span v-if="status === 'full'">🛑 Guest Slot Full</span>
    <span v-else-if="status === 'next'">🟢 You're Next!</span>
  </div>
</template>

<script setup>
const props = defineProps({
  status: {
    type: String,
    default: 'waiting' // or 'full', 'next'
  }
})
</script>
