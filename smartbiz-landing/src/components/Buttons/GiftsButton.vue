<template>
  <!-- 🎁 Gift Trigger Button -->
  <button
    class="gifts-btn"
    @click="handleToggle"
    aria-label="Open Gift Drawer"
  >
    <span class="text-xl">🎁</span>
    <span class="text-xs font-semibold tracking-wide">Gifts</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['toggle'])

const handleToggle = () => {
  console.log('🎁 GiftsButton clicked')
  emit('toggle')
}
</script>

<style scoped>
.gifts-btn {
  @apply flex flex-col items-center gap-1 px-4 py-2 rounded-full text-white text-xs font-semibold transition-transform duration-300 ease-in-out shadow-md;

  background: linear-gradient(to right, rgba(236, 72, 153, 0.6), rgba(219, 39, 119, 0.6));
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow:
    0 4px 12px rgba(236, 72, 153, 0.2),
    0 2px 8px rgba(236, 72, 153, 0.15);
}

.gifts-btn:hover {
  background: linear-gradient(to right, #f472b6, #ec4899);
  transform: scale(1.08);
  box-shadow:
    0 6px 16px rgba(236, 72, 153, 0.3),
    0 3px 10px rgba(236, 72, 153, 0.2);
}

.gifts-btn:focus-visible {
  outline: none;
  box-shadow:
    0 0 0 3px rgba(236, 72, 153, 0.5),
    0 0 0 6px rgba(236, 72, 153, 0.3);
}
</style>
