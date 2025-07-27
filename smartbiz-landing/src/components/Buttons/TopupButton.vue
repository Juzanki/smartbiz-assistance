<template>
  <button
    class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-md"
    @click="handleClick"
  >
    <span>💰</span>
    <span class="font-semibold">Top Up</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['open-topup'])

function handleClick() {
  emit('open-topup')
}
</script>

<style scoped></style>
