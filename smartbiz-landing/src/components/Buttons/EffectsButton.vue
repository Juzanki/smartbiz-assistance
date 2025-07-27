<template>
  <button
    class="effect-btn flex items-center gap-2 px-5 py-2 rounded-full shadow-lg hover:scale-105 transition duration-300"
    @click="handleClick"
  >
    <span class="text-xl">✨</span>
    <span class="font-semibold tracking-wide">Effects</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['effects-open'])

function handleClick() {
  emit('effects-open')
}
</script>

<style scoped>
.effect-btn {
  @apply bg-gradient-to-r from-purple-500 via-pink-500 to-indigo-500 text-white backdrop-blur-md;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow:
    0 2px 5px rgba(0, 0, 0, 0.1),
    0 4px 10px rgba(147, 51, 234, 0.2);
}

.effect-btn:hover {
  background-position: right center;
  background-size: 200% auto;
  box-shadow:
    0 4px 8px rgba(0, 0, 0, 0.15),
    0 6px 12px rgba(236, 72, 153, 0.3);
}
</style>
