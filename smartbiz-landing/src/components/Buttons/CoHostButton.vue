<template>
  <button
    class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-md"
    @click="handleClick"
  >
    <span>👥</span>
    <span class="font-semibold">Co-Host</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['toggle-cohost'])

function handleClick() {
  emit('toggle-cohost')
}
</script>

<style scoped></style>
