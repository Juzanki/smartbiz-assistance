<template>
  <div class="absolute inset-0 z-[2] pointer-events-none overflow-hidden">
    <div
      v-for="(firework, index) in fireworks"
      :key="index"
      class="absolute w-1.5 h-1.5 rounded-full opacity-90 blur-sm"
      :style="firework.style"
      :class="firework.class"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const fireworks = ref([])

const colors = [
  'from-yellow-400 to-red-500',
  'from-pink-400 to-purple-600',
  'from-blue-400 to-cyan-500',
  'from-green-400 to-lime-500',
  'from-white to-white'
]

const generateFireworks = () => {
  const temp = []
  for (let i = 0; i < 40; i++) {
    const x = Math.random() * 100
    const y = Math.random() * 100
    const delay = Math.random() * 1
    const duration = 1.2 + Math.random() * 1

    temp.push({
      style: {
        top: `${y}%`,
        left: `${x}%`,
        animationDelay: `${delay}s`,
        animationDuration: `${duration}s`,
      },
      class: `bg-gradient-to-br ${colors[Math.floor(Math.random() * colors.length)]} animate-firework-burst`
    })
  }
  fireworks.value = temp
}

onMounted(() => {
  generateFireworks()
})
</script>

<style scoped>
@keyframes firework-burst {
  0% {
    transform: scale(0.3) translateY(0);
    opacity: 1;
  }
  60% {
    transform: scale(1.2) translateY(-20px);
    opacity: 0.9;
  }
  100% {
    transform: scale(0.9) translateY(-100px);
    opacity: 0;
  }
}
.animate-firework-burst {
  animation-name: firework-burst;
  animation-timing-function: ease-out;
  animation-fill-mode: forwards;
}
</style>
