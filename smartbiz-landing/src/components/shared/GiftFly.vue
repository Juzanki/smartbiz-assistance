<template>
  <transition :name="gift?.animation || 'fly'">
    <div
      v-if="visible"
      :class="[
        'absolute bottom-24 left-1/2 transform -translate-x-1/2 z-50 flex flex-col items-center space-y-2',
        fadeOut ? 'fly-out' : ''
      ]"
    >
      <!-- 🔊 Sound Effect -->
      <audio v-if="gift?.sound" :src="gift.sound" autoplay />

      <!-- 🌟 Extra Visual Effect (SVG or image) -->
      <div
        v-if="gift?.effect"
        class="absolute -z-10 w-40 h-40 bg-cover bg-center animate-spin-slow"
        :style="{ backgroundImage: `url(${gift.effect})` }"
      ></div>

      <!-- 🎁 Gift Icon -->
      <img
        :src="gift?.icon"
        :alt="gift?.name"
        class="w-24 h-24 object-contain drop-shadow-xl gift-glow"
      />

      <!-- 💬 Gift Label -->
      <p class="text-white text-sm font-bold bg-black/50 px-3 py-1 rounded-full backdrop-blur">
        🎁 {{ gift?.name }} sent by {{ gift?.sender || 'Anonymous' }}!
      </p>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const props = defineProps({
  gift: Object, // expects { icon, name, animation, duration, sound, effect, sender }
})

const visible = ref(true)
const fadeOut = ref(false)

watch(() => props.gift, (newGift) => {
  if (newGift) {
    visible.value = true
    fadeOut.value = false

    const duration = newGift.duration || 7000

    setTimeout(() => {
      fadeOut.value = true
    }, duration - 1500)

    setTimeout(() => {
      visible.value = false
    }, duration)
  }
}, { immediate: true })
</script>

<style scoped>
/* 🌈 Glow effect on gift icon */
.gift-glow {
  animation: glowGift 2s ease-in-out infinite alternate;
}
@keyframes glowGift {
  from {
    filter: drop-shadow(0 0 10px #facc15) brightness(1.2);
    transform: scale(1);
  }
  to {
    filter: drop-shadow(0 0 25px #facc15) brightness(1.4);
    transform: scale(1.05);
  }
}

/* 🕊️ Fly Entrance and Exit */
.fly-enter-from,
.fly-leave-to {
  opacity: 0;
  transform: translateY(60px) scale(0.8);
}
.fly-enter-active,
.fly-leave-active {
  transition: all 0.6s ease;
}

/* 🚀 Exit Fly Motion */
.fly-out {
  animation: flyExit 1.4s ease forwards;
}
@keyframes flyExit {
  0% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
  100% {
    opacity: 0;
    transform: translateY(-100px) scale(0.85);
  }
}

/* 🧨 Quantum Pop Animation */
.quantum-pop-enter-active {
  animation: quantumPop 3s ease-in-out;
}
@keyframes quantumPop {
  0% { transform: scale(0); opacity: 0; }
  50% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(1); opacity: 0; }
}

/* 🌌 Orbit Flip Animation */
.orbit-flip-enter-active {
  animation: orbitFlip 4s ease-in-out;
}
@keyframes orbitFlip {
  0% { transform: rotateY(0deg) scale(0.8); opacity: 0; }
  50% { transform: rotateY(360deg) scale(1.1); opacity: 1; }
  100% { transform: rotateY(720deg) scale(1); opacity: 0; }
}

/* 🔁 Slow Spin (for SVG effect layer) */
.animate-spin-slow {
  animation: spinSlow 8s linear infinite;
}
@keyframes spinSlow {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
