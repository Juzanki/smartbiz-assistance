<template>
  <div class="shockwave" :style="style"></div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const style = ref({
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
})
</script>

<style scoped>
.shockwave {
  position: absolute;
  width: 60px;
  height: 60px;
  border: 6px solid rgba(255, 255, 255, 0.6);
  border-radius: 50%;
  animation: explode 1.2s ease-out forwards;
  pointer-events: none;
  z-index: 9999;
  filter: blur(1px);
}

@keyframes explode {
  0% {
    transform: translate(-50%, -50%) scale(0.2);
    opacity: 1;
    border-width: 8px;
  }
  60% {
    opacity: 0.5;
  }
  100% {
    transform: translate(-50%, -50%) scale(5);
    opacity: 0;
    border-width: 2px;
  }
}
</style>
