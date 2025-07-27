<template>
  <button
    class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-md"
    @click="handleClick"
  >
    <span>🎙️</span>
    <span class="font-semibold">Voice Chat</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['toggle-voice'])

function handleClick() {
  emit('toggle-voice')
}
</script>

<style scoped></style>
