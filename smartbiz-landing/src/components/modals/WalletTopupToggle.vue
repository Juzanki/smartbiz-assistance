<template>
  <button @click="openWalletTopup" class="icon-btn">
    💳 Wallet
  </button>
</template>

<script setup>
const emit = defineEmits(['open'])

function openWalletTopup() {
  emit('open')
}
</script>

<style scoped>
.icon-btn {
  @apply bg-teal-600 hover:bg-teal-500 text-white px-3 py-1 text-sm rounded-full shadow;
}
</style>
