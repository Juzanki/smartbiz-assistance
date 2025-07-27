<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4">
    <div class="bg-white w-full max-w-2xl rounded-3xl shadow-2xl p-6 relative animate-fade-in space-y-6">
      <!-- Header -->
      <div class="flex justify-between items-center">
        <h2 class="text-xl font-bold text-indigo-700 flex items-center gap-2">
          ✨ Live Effects Panel
        </h2>
        <button @click="$emit('close')" class="text-red-500 text-2xl hover:text-red-700">✖</button>
      </div>

      <!-- Effects Grid -->
      <div class="grid grid-cols-3 sm:grid-cols-4 gap-4">
        <div
          v-for="effect in effects"
          :key="effect.id"
          class="bg-gray-100 rounded-xl p-3 text-center shadow hover:shadow-md transition cursor-pointer"
          :class="{ 'ring-2 ring-indigo-500': activeEffect === effect.id }"
          @click="applyEffect(effect.id)"
        >
          <img :src="effect.icon" class="w-14 h-14 mx-auto rounded" />
          <div class="mt-2 text-sm font-medium text-gray-700">{{ effect.name }}</div>
        </div>
      </div>

      <!-- Clear Button -->
      <div class="flex justify-end">
        <button
          @click="clearEffect"
          class="text-sm px-5 py-2 rounded-full bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold"
        >
          Clear Effects
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['close', 'set-effect'])

const activeEffect = ref(null)

const effects = [
  { id: 'sparkle', name: 'Sparkle Glow', icon: '/effects/sparkle.png' },
  { id: 'hearts', name: 'Flying Hearts', icon: '/effects/hearts.png' },
  { id: 'fireworks', name: 'Fireworks', icon: '/effects/fireworks.png' },
  { id: 'bubbles', name: 'Floating Bubbles', icon: '/effects/bubbles.png' },
  { id: 'neon', name: 'Neon Glow', icon: '/effects/neon.png' },
  { id: 'stars', name: 'Falling Stars', icon: '/effects/stars.png' },
  { id: 'emojiRain', name: 'Emoji Rain', icon: '/effects/emoji.png' }
]

function applyEffect(effectId) {
  activeEffect.value = effectId
  emit('set-effect', effectId)
}

function clearEffect() {
  activeEffect.value = null
  emit('set-effect', null)
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeInUp 0.4s ease-out;
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
