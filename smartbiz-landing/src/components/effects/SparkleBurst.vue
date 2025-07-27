<template>
  <div class="sparkle-container">
    <div v-for="n in 12" :key="n" class="sparkle" :style="getStyle(n)"></div>
  </div>
</template>

<script setup>
const getStyle = (index) => {
  const angle = (360 / 12) * index
  return {
    transform: `rotate(${angle}deg) translate(0, -60px)`,
    animationDelay: `${Math.random() * 0.3}s`,
  }
}
</script>

<style scoped>
.sparkle-container {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 1001;
}

.sparkle {
  position: absolute;
  width: 8px;
  height: 8px;
  background: radial-gradient(circle, white, transparent);
  border-radius: 50%;
  animation: burst 1s ease-out forwards;
  opacity: 0;
}

@keyframes burst {
  0% {
    opacity: 0;
    transform: scale(0.2);
  }
  40% {
    opacity: 1;
    transform: scale(1.2);
  }
  100% {
    opacity: 0;
    transform: scale(0) translateY(-80px);
  }
}
</style>
