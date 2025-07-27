<template>
  <div class="flex flex-col items-center space-y-1 cursor-pointer group" @click="$emit('toggle')">
    <div class="text-white text-xl animate-spin-slow group-hover:text-blue-400">
      📼
    </div>
    <span class="text-xs text-white/90 group-hover:text-blue-300">Replay</span>
  </div>
</template>

<script setup>
defineEmits(['toggle'])
</script>

<style scoped>
@keyframes spin-slow {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.animate-spin-slow {
  animation: spin-slow 8s linear infinite;
}
</style>
