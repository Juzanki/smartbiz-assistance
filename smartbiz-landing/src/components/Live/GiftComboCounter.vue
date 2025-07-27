<template>
  <transition name="combo-pop">
    <div
      v-if="visible && count > 1"
      class="absolute top-[10%] left-1/2 -translate-x-1/2 z-[999] bg-gradient-to-r from-yellow-400 via-red-500 to-pink-500 text-white font-bold px-6 py-2 rounded-full shadow-2xl text-2xl flex items-center gap-2 animate-pulse backdrop-blur-md"
    >
      <span>🔥 COMBO x{{ count }}</span>
    </div>
  </transition>
</template>

<script setup>
import { ref, watch, onBeforeUnmount } from 'vue'

// 👇 Prop mpya kutoka kwa LiveGiftAnimations
const props = defineProps({
  comboCount: {
    type: Number,
    required: true,
  }
})

const visible = ref(false)
const count = ref(0)
let hideTimer = null

// ⏱ Watch comboCount na onyesha ikiwa ni zaidi ya 1
watch(() => props.comboCount, (newCount) => {
  if (newCount > 1) {
    count.value = newCount
    visible.value = true
    resetTimer()
  }
})

// 🕒 Ficha combo baada ya muda mfupi
function resetTimer() {
  if (hideTimer) clearTimeout(hideTimer)
  hideTimer = setTimeout(() => {
    visible.value = false
    count.value = 0
  }, 2500)
}

onBeforeUnmount(() => {
  if (hideTimer) clearTimeout(hideTimer)
})
</script>

<style scoped>
@keyframes comboPop {
  0% {
    transform: scale(0.6) translateY(-20px);
    opacity: 0;
  }
  60% {
    transform: scale(1.15) translateY(0);
    opacity: 1;
  }
  100% {
    transform: scale(1) translateY(0);
  }
}
.combo-pop-enter-active {
  animation: comboPop 0.5s ease-out;
}
</style>
