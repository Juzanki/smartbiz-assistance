<template>
  <button
    class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-md"
    @click="handleClick"
  >
    <span>👥</span>
    <span class="font-semibold">+ Hosts</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['open-hosts'])

function handleClick() {
  emit('open-hosts') // Trigger event to parent (e.g. open modal)
}
</script>

<style scoped>
/* Optional additional styling */
</style>
