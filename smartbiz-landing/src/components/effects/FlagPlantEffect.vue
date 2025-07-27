<template>
  <transition name="fade-slide">
    <div v-if="visible" class="fixed inset-0 z-[9999] pointer-events-none overflow-hidden">
      <!-- 🌠 Falling Hero -->
      <img
        v-if="heroStage === 'falling'"
        src="/effects/hero-fall.png"
        class="absolute w-36 h-auto left-1/2 -translate-x-1/2 top-[-100px] animate-hero-drop z-[2]"
        alt="Falling Hero"
      />

      <!-- 🗻 Standing on Mountain -->
      <div
        v-if="heroStage === 'landed'"
        class="absolute bottom-12 left-1/2 -translate-x-1/2 flex flex-col items-center z-[3]"
      >
        <!-- 🚩 Flags -->
        <div class="flex gap-4 mb-2 animate-flag-wave">
          <img src="/flags/tanzania.png" class="w-10 h-10 rounded shadow" />
          <img src="/flags/smartbiz.png" class="w-10 h-10 rounded shadow" />
        </div>

        <!-- 🦸 Hero -->
        <img
          src="/effects/hero-pose.png"
          class="w-28 h-auto drop-shadow-xl animate-glow-burst"
          alt="Hero Pose"
        />
      </div>

      <!-- 🌄 Base Glow -->
      <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[240px] h-[80px] rounded-full bg-gradient-to-t from-yellow-300/30 to-transparent blur-xl z-[1]" />

      <!-- ✨ Background Spark -->
      <LiveGiftParticles />
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LiveGiftParticles from './LiveGiftParticles.vue'

const visible = ref(true)
const heroStage = ref('falling') // 'falling' → 'landed'

onMounted(() => {
  // After drop animation, show final landing + flags
  setTimeout(() => {
    heroStage.value = 'landed'
  }, 1800)

  // Hide entire component after some time
  setTimeout(() => {
    visible.value = false
  }, 6000)
})
</script>

<style scoped>
@keyframes heroDrop {
  0% {
    top: -150px;
    transform: translateX(-50%) scale(0.8) rotate(0deg);
    opacity: 0.7;
    filter: blur(2px);
  }
  70% {
    top: 60%;
    transform: translateX(-50%) scale(1.2) rotate(15deg);
    opacity: 1;
  }
  100% {
    top: 75%;
    transform: translateX(-50%) scale(1) rotate(0deg);
    filter: blur(0);
  }
}
.animate-hero-drop {
  animation: heroDrop 1.8s ease-out forwards;
  will-change: transform, top, opacity;
}

@keyframes flagWave {
  0%, 100% { transform: rotate(-3deg); }
  50% { transform: rotate(3deg); }
}
.animate-flag-wave {
  animation: flagWave 2s ease-in-out infinite;
  will-change: transform;
}

@keyframes glowBurst {
  0% {
    opacity: 0.2;
    filter: brightness(0.7) drop-shadow(0 0 10px gold);
    transform: scale(0.9);
  }
  50% {
    opacity: 1;
    filter: brightness(1.4) drop-shadow(0 0 30px gold);
    transform: scale(1.1);
  }
  100% {
    filter: drop-shadow(0 0 15px gold);
    transform: scale(1);
  }
}
.animate-glow-burst {
  animation: glowBurst 2.5s ease-out forwards;
  will-change: transform, filter, opacity;
}

/* 🔁 Container fade in/out */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 1s ease;
}
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
}
</style>
