<template>
  <div class="energy-pulse" :style="style"></div>
</template>

<script setup>
import { ref } from 'vue'

// 🌀 Central pulse position
const style = ref({
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%) scale(1)',
})
</script>

<style scoped>
.energy-pulse {
  position: absolute;
  width: 120px;
  height: 120px;
  background: radial-gradient(circle, rgba(0, 255, 255, 0.65), transparent 70%);
  border-radius: 50%;
  animation: pulseWave 1.4s ease-out forwards;
  pointer-events: none;
  z-index: 3;
  filter: blur(12px) brightness(1.2);
}

@keyframes pulseWave {
  0% {
    transform: translate(-50%, -50%) scale(0.3);
    opacity: 1;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.4);
    opacity: 0.6;
  }
  100% {
    transform: translate(-50%, -50%) scale(2.8);
    opacity: 0;
  }
}
</style>
