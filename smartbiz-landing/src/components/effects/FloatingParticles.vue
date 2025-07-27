<template>
  <div class="absolute inset-0 z-10 pointer-events-none">
    <div
      v-for="particle in particles"
      :key="particle.id"
      :style="{
        top: particle.y + '%',
        left: particle.x + '%',
        animationDuration: particle.duration + 's',
        backgroundColor: particle.color
      }"
      class="particle"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { nanoid } from 'nanoid'

const particles = ref([])

function randomColor() {
  const colors = ['#ffffff', '#e0e0e0', '#a0a0ff', '#ff99cc', '#66ffff']
  return colors[Math.floor(Math.random() * colors.length)]
}

function generateParticles(count = 25) {
  particles.value = Array.from({ length: count }).map(() => ({
    id: nanoid(),
    x: Math.random() * 100,
    y: Math.random() * 100,
    duration: 4 + Math.random() * 4,
    color: randomColor()
  }))
}

onMounted(() => {
  generateParticles()
})
</script>

<style scoped>
.particle {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 9999px;
  opacity: 0.3;
  animation: floatUp ease-in-out infinite;
  transition: opacity 0.3s ease;
}

@keyframes floatUp {
  0% {
    transform: translateY(0) scale(0.8);
    opacity: 0.2;
  }
  50% {
    transform: translateY(-60px) scale(1.4);
    opacity: 0.6;
  }
  100% {
    transform: translateY(-120px) scale(0.9);
    opacity: 0;
  }
}
</style>
