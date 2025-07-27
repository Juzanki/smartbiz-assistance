<template>
  <transition name="express-fade">
    <div
      v-if="visible"
      class="fixed bottom-0 left-1/2 -translate-x-1/2 z-[9998] pointer-events-none flex flex-col items-center"
    >
      <!-- 🌟 Flying Island / Mirror Animation -->
      <img
        :src="effectImage"
        alt="Express Gift Effect"
        class="w-[280px] md:w-[360px] h-auto object-contain animate-fly-in-up drop-shadow-2xl"
      />

      <!-- 🏷️ Gift Label -->
      <div class="mt-2 text-white text-base font-bold bg-black/60 px-4 py-1 rounded-full shadow backdrop-blur-sm">
        🚄 {{ labelText }}
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  effectImage: {
    type: String,
    default: '/effects/express-island.png'
  },
  labelText: {
    type: String,
    default: 'SMARTBIZ EXPRESS ARRIVAL'
  },
  duration: {
    type: Number,
    default: 5000
  }
})

const visible = ref(true)

onMounted(() => {
  setTimeout(() => {
    visible.value = false
  }, props.duration)
})
</script>

<style scoped>
/* 🎬 Express Fade + Float-In */
@keyframes flyInUp {
  0% {
    opacity: 0;
    transform: translateY(100px) scale(0.9);
    filter: blur(4px);
  }
  60% {
    opacity: 1;
    transform: translateY(-10px) scale(1.05);
    filter: blur(1px);
  }
  100% {
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}
.animate-fly-in-up {
  animation: flyInUp 1.2s ease-out;
  will-change: transform, opacity, filter;
}

.express-fade-enter-active,
.express-fade-leave-active {
  transition: opacity 0.8s ease;
}
.express-fade-enter-from,
.express-fade-leave-to {
  opacity: 0;
}
</style>
