<template>
  <transition-group
    name="gift"
    tag="div"
    class="fixed inset-0 z-[9999] pointer-events-none overflow-hidden"
  >
    <div
      v-for="gift in gifts"
      :key="gift.id + '-' + gift.timestamp"
      class="absolute inset-0 flex items-center justify-center"
    >
      <div
        class="relative flex flex-col items-center justify-center animate-gift-entry space-y-4"
        :class="[gift.animation || 'explode-enter-active']"
        :style="{ animationDuration: (gift.duration || 7000) + 'ms' }"
      >
        <!-- 🌠 Background Effect Layer (Optional) -->
        <img
          v-if="gift.effect"
          :src="gift.effect"
          alt="effect"
          class="absolute inset-0 w-full h-full object-contain opacity-40 animate-spin-slow pointer-events-none z-[1]"
        />

        <!-- 🎥 Fullscreen Video Gift or Fallback Icon -->
        <component
          :is="gift.video ? 'video' : 'img'"
          :src="gift.video || gift.icon"
          class="relative z-[2] object-contain rounded-2xl border border-white/10 backdrop-blur-md shadow-2xl bg-black/20"
          :class="[
            'drop-shadow-[0_0_60px_rgba(255,255,255,0.2)]',
            gift.video ? 'w-[22rem] md:w-[28rem] lg:w-[32rem]' : 'w-40 md:w-56 lg:w-72'
          ]"
          v-bind="gift.video ? {
            autoplay: true,
            loop: false,
            muted: true,
            playsinline: true
          } : {}"
        />

        <!-- 🏷️ Gift Name Label -->
        <div
          v-if="gift.name"
          class="z-[3] mt-3 px-6 py-2 rounded-full text-white font-extrabold text-xl tracking-wide shadow-md backdrop-blur-md bg-gradient-to-r from-black/60 via-black/30 to-black/60 border border-white/10"
        >
          {{ gift.name }}
        </div>
      </div>
    </div>
  </transition-group>
</template>
<script setup>
import { ref, watch, nextTick } from 'vue'

const props = defineProps({
  gifts: {
    type: Array,
    required: true,
  },
})

// 🎁 Zawadi zinazopaswa kuonekana kwa sasa
const visibleGifts = ref([])

// 🧠 Kuhifadhi zawadi zilizocheza ili kuepuka kurudia
const playedTimestamps = new Set()

// 🎧 Play sauti kwa zawadi
function playSoundOnce(src, uniqueKey) {
  if (!src || playedTimestamps.has(uniqueKey)) return

  try {
    const audio = new Audio(src)
    audio.volume = 0.85
    audio.play()
    playedTimestamps.add(uniqueKey)
  } catch (err) {
    console.warn('🔇 Sound error:', err)
  }
}

// 🧼 Ondoa zawadi baada ya muda maalum
function scheduleRemoval(uniqueKey, duration) {
  setTimeout(() => {
    visibleGifts.value = visibleGifts.value.filter(gift =>
      gift.id + '-' + gift.timestamp !== uniqueKey
    )
  }, duration + 350) // buffer kidogo
}

// 🕵🏽‍♀️ Watch: on new incoming gifts
watch(
  () => props.gifts,
  (newGifts) => {
    newGifts.forEach(gift => {
      const uniqueKey = `${gift.id}-${gift.timestamp}`
      const alreadyVisible = visibleGifts.value.some(g => `${g.id}-${g.timestamp}` === uniqueKey)
      if (!alreadyVisible) {
        visibleGifts.value.push(gift)

        // Cheza sauti ya zawadi hii mara moja tu
        playSoundOnce(gift.sound, uniqueKey)

        // Pangilia kuondolewa baada ya muda maalum
        const duration = gift.duration || 7000
        scheduleRemoval(uniqueKey, duration)
      }
    })
  },
  { deep: true }
)
</script>

<style scoped>
/* 🌌 BASE STYLING */
.animate-gift {
  animation-fill-mode: both;
  will-change: transform, opacity, filter;
  position: relative;
  z-index: 10;
  filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.1));
}

/* 🌠 Entry & Exit Transition */
.gift-enter-active,
.gift-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.gift-enter-from,
.gift-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

/* 🌀 FLOAT UP */
@keyframes float-up {
  0% {
    opacity: 0;
    transform: translateY(60px) scale(0.85) rotate(-6deg);
    filter: blur(4px) brightness(0.8);
  }
  80% {
    opacity: 1;
    transform: translateY(-8px) scale(1.05);
    filter: blur(0) brightness(1.1);
  }
  100% {
    transform: translateY(0) scale(1);
    filter: brightness(1);
  }
}
.float-up {
  animation-name: float-up;
}

/* 🔄 3D Orbit Flip */
@keyframes orbit-flip {
  0% {
    transform: rotateY(0deg) scale(0.6);
    opacity: 0;
  }
  50% {
    transform: rotateY(180deg) scale(1.2);
    opacity: 1;
    filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.2));
  }
  100% {
    transform: rotateY(360deg) scale(1);
    opacity: 0;
  }
}
.orbit-flip {
  animation-name: orbit-flip;
  transform-style: preserve-3d;
}

/* ✨ Spiral Spark */
@keyframes spiral-spark {
  0% {
    transform: scale(0.3) rotate(0deg);
    opacity: 0;
    filter: brightness(0.6) blur(3px);
  }
  60% {
    transform: scale(1.4) rotate(180deg);
    opacity: 1;
    filter: brightness(1.5) blur(0);
  }
  100% {
    transform: scale(1) rotate(360deg);
    opacity: 0;
    filter: brightness(1);
  }
}
.spiral-spark {
  animation-name: spiral-spark;
}

/* 🔥 Flame Rise */
@keyframes flame-rise {
  0% {
    transform: translateY(40px) scale(0.8) skewY(-3deg);
    opacity: 0;
    filter: hue-rotate(60deg) blur(2px);
  }
  60% {
    transform: translateY(-12px) scale(1.1);
    opacity: 1;
    filter: hue-rotate(0deg);
  }
  100% {
    transform: translateY(0) scale(1);
    opacity: 0;
  }
}
.flame-rise {
  animation-name: flame-rise;
}

/* 🚗 Drive In */
@keyframes drive-in {
  0% {
    transform: translateX(-120%) scale(0.8) rotate(-10deg);
    opacity: 0;
  }
  60% {
    transform: translateX(10%) scale(1.2) rotate(3deg);
    opacity: 1;
  }
  100% {
    transform: translateX(0) scale(1) rotate(0);
    opacity: 0;
  }
}
.drive-in {
  animation-name: drive-in;
}

/* 👑 Crown Zoom */
@keyframes crown-zoom {
  0% {
    transform: scale(0.4) rotate(0deg);
    opacity: 0;
    filter: drop-shadow(0 0 10px rgba(255, 215, 0, 0.3));
  }
  50% {
    transform: scale(1.4) rotate(25deg);
    opacity: 1;
    filter: drop-shadow(0 0 35px gold);
  }
  100% {
    transform: scale(1) rotate(0deg);
    opacity: 0;
  }
}
.crown-zoom {
  animation-name: crown-zoom;
}

/* 🌟 Shine Rise */
@keyframes shine-rise {
  0% {
    opacity: 0;
    transform: translateY(50px) scale(0.8);
    filter: brightness(0.7) blur(3px);
  }
  60% {
    opacity: 1;
    transform: translateY(-10px) scale(1.1);
    filter: brightness(1.5);
  }
  100% {
    opacity: 0;
    transform: translateY(0) scale(1);
    filter: brightness(1);
  }
}
.shine-rise {
  animation-name: shine-rise;
}

/* 🌈 Bonus Fade Scale Pop */
@keyframes fade-scale {
  0% {
    transform: scale(0.3);
    opacity: 0;
  }
  50% {
    transform: scale(1.2);
    opacity: 1;
  }
  100% {
    transform: scale(1);
    opacity: 0;
  }
}
.animate-fade-scale {
  animation: fade-scale 2.5s ease-in-out forwards;
}
</style>
