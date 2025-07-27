<template>
  <div class="smoke-trail" :style="style"></div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const style = ref({})

onMounted(() => {
  style.value = {
    animation: 'smokeRise 2.5s ease-out forwards',
    left: `${Math.random() * 60 + 20}%`, // randomize horizontal position
    opacity: 0.85,
  }
})
</script>

<style scoped>
.smoke-trail {
  position: absolute;
  bottom: 0;
  width: 80px;
  height: 80px;
  background: radial-gradient(rgba(200,200,200,0.6), transparent 70%);
  filter: blur(8px);
  pointer-events: none;
  z-index: 1000;
}

/* Animation Keyframes */
@keyframes smokeRise {
  0% {
    transform: translateY(0) scale(0.8);
    opacity: 0.9;
  }
  50% {
    transform: translateY(-100px) scale(1);
    opacity: 0.6;
  }
  100% {
    transform: translateY(-200px) scale(1.2);
    opacity: 0;
  }
}
</style>
