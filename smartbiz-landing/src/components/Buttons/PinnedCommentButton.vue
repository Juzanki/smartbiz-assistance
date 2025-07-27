<template>
  <button
    class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-md"
    @click="handleClick"
  >
    <span>📌</span>
    <span class="font-semibold">Pin Comment</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['pin-comment'])

function handleClick() {
  emit('pin-comment')
}
</script>

<style scoped></style>
