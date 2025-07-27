<template>
  <div class="spotlight-wrapper">
    <div class="spotlight"></div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const rotation = ref(0)

onMounted(() => {
  rotation.value = Math.floor(Math.random() * 360) // random rotation
})
</script>

<style scoped>
.spotlight-wrapper {
  position: absolute;
  top: 10%;
  left: 50%;
  transform: translateX(-50%);
  width: 300px;
  height: 300px;
  pointer-events: none;
  z-index: 999;
}

.spotlight {
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, rgba(255,255,255,0.7), transparent 70%);
  border-radius: 50%;
  animation: rotateLight 3s ease-out forwards;
  filter: blur(12px);
  transform: rotate(0deg);
}

@keyframes rotateLight {
  0% {
    transform: scale(0.4) rotate(0deg);
    opacity: 0.2;
  }
  50% {
    transform: scale(1.1) rotate(180deg);
    opacity: 0.7;
  }
  100% {
    transform: scale(1) rotate(360deg);
    opacity: 0;
  }
}
</style>
