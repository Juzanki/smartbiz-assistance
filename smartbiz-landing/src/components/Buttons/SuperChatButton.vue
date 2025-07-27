<template>
  <button
    class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-md"
    @click="handleClick"
  >
    <span>💬✨</span>
    <span class="font-semibold">Super Chat</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['superchat-open'])

function handleClick() {
  emit('superchat-open') // Trigger kwa kufungua super chat modal au overlay
}
</script>

<style scoped>
/* Optional: Customize style if needed */
</style>
