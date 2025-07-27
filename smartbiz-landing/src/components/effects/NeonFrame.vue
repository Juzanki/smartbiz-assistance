<template>
  <div class="neon-frame" :style="frameStyle"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const frameStyle = ref({
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%) scale(1)',
})
</script>

<style scoped>
.neon-frame {
  position: absolute;
  width: 180px;
  height: 180px;
  border: 4px solid rgba(0, 217, 255, 0.8);
  border-radius: 16px;
  box-shadow:
    0 0 20px rgba(0, 217, 255, 0.9),
    0 0 60px rgba(0, 217, 255, 0.6),
    0 0 100px rgba(0, 217, 255, 0.4);
  animation: pulseGlow 2s ease-in-out forwards;
  pointer-events: none;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

@keyframes pulseGlow {
  0% {
    transform: translate(-50%, -50%) scale(0.5);
    opacity: 0.1;
  }
  40% {
    transform: translate(-50%, -50%) scale(1.1);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}
</style>
