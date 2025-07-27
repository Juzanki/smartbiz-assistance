<template>
  <div class="host-card">
    <img :src="host.avatar" class="host-avatar" />
    <div class="host-name">{{ host.name }}</div>

    <!-- Mic & Cam toggles -->
    <div class="icon-controls">
      <button @click="$emit('toggleMic', host.id)" :class="host.mic ? 'text-green-500' : 'text-gray-400'">
        <i :class="host.mic ? 'i-tabler-microphone' : 'i-tabler-microphone-off'" />
      </button>
      <button @click="$emit('toggleCam', host.id)" :class="host.cam ? 'text-green-500' : 'text-gray-400'">
        <i :class="host.cam ? 'i-tabler-camera' : 'i-tabler-camera-off'" />
      </button>
    </div>

    <!-- Swap / Remove buttons -->
    <div class="host-actions">
      <button @click="$emit('swap', host.id)" class="text-blue-500 hover:underline">🔁 Swap</button>
      <button @click="$emit('remove', host.id)" class="text-red-500 hover:underline">🗑 Remove</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  host: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.host-card {
  @apply bg-gradient-to-br from-gray-100 to-white rounded-xl p-4 text-center shadow-md hover:shadow-xl transition border border-white/40;
}
.host-avatar {
  @apply w-16 h-16 rounded-full mx-auto border border-gray-300 shadow;
}
.host-name {
  @apply mt-2 font-semibold truncate text-gray-700;
}
.icon-controls {
  @apply flex justify-center mt-2 gap-3 text-xl;
}
.host-actions {
  @apply flex justify-center gap-2 mt-3 text-sm;
}
</style>
