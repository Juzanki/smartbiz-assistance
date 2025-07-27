<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
    <div class="bg-white rounded-3xl shadow-2xl w-full max-w-xl p-6 relative animate-fade-in space-y-6">
      <!-- Header -->
      <div class="flex justify-between items-center">
        <h2 class="text-xl font-bold text-indigo-700 flex items-center gap-2">
          ✨ Visual Effects
        </h2>
        <button @click="$emit('close')" class="text-red-500 text-xl hover:text-red-700">✖</button>
      </div>

      <!-- Effects Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
        <button
          v-for="effect in effects"
          :key="effect.id"
          @click="toggleEffect(effect.id)"
          :class="['effect-btn', activeEffects.includes(effect.id) ? 'active-effect' : '']"
        >
          <span class="text-2xl">{{ effect.icon }}</span>
          <span class="text-sm font-medium">{{ effect.name }}</span>
        </button>
      </div>
    </div>

    <!-- Effect Layers -->
    <div class="pointer-events-none absolute inset-0 z-40">
      <div v-if="activeEffects.includes('sparkles')" class="effect-layer sparkle-layer"></div>
      <div v-if="activeEffects.includes('glow')" class="effect-layer glow-layer"></div>
      <div v-if="activeEffects.includes('hearts')" class="effect-layer heart-layer"></div>
      <div v-if="activeEffects.includes('stars')" class="effect-layer star-layer"></div>
      <div v-if="activeEffects.includes('bokeh')" class="effect-layer bokeh-layer"></div>
      <div v-if="activeEffects.includes('neon')" class="effect-layer neon-layer"></div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeEffects = ref([])

const effects = [
  { id: 'sparkles', name: 'Sparkles', icon: '✨' },
  { id: 'glow', name: 'Glow Aura', icon: '💫' },
  { id: 'hearts', name: 'Hearts', icon: '❤️' },
  { id: 'stars', name: 'Starfall', icon: '🌟' },
  { id: 'bokeh', name: 'Bokeh Blur', icon: '🔮' },
  { id: 'neon', name: 'Neon Grid', icon: '⚡' }
]

function toggleEffect(id) {
  const index = activeEffects.value.indexOf(id)
  if (index > -1) {
    activeEffects.value.splice(index, 1)
  } else {
    activeEffects.value.push(id)
  }
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeInUp 0.4s ease-out both;
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.effect-btn {
  @apply flex flex-col items-center justify-center bg-white/10 hover:bg-white/20 text-indigo-200 px-4 py-3 rounded-xl transition font-semibold shadow-lg;
}
.active-effect {
  @apply bg-indigo-500 text-white scale-105 shadow-xl;
}

.effect-layer {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
}

.sparkle-layer {
  background-image: url('/effects/sparkles.gif');
  background-size: cover;
  opacity: 0.4;
}

.glow-layer {
  background: radial-gradient(circle, rgba(255,255,255,0.1), transparent 60%);
  animation: pulse 2s infinite;
}

.heart-layer::before {
  content: '💖💗💓💞';
  font-size: 4rem;
  animation: floatUp 3s infinite ease-in-out;
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
}

.star-layer {
  background-image: url('/effects/starfield.gif');
  background-size: cover;
  opacity: 0.3;
}

.bokeh-layer {
  background-image: url('/effects/bokeh.png');
  background-repeat: repeat;
  animation: bokehFade 6s infinite alternate;
  opacity: 0.15;
}

.neon-layer {
  background: repeating-linear-gradient(45deg, rgba(0,255,255,0.1), rgba(255,0,255,0.1) 10px);
  mix-blend-mode: lighten;
  animation: glowPulse 3s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.2; }
  50% { opacity: 0.4; }
}
@keyframes glowPulse {
  0%, 100% { filter: brightness(1.1); }
  50% { filter: brightness(1.5); }
}
@keyframes floatUp {
  0% { transform: translateY(0) scale(1); opacity: 1; }
  100% { transform: translateY(-100px) scale(1.2); opacity: 0; }
}
@keyframes bokehFade {
  0% { opacity: 0.1; }
  100% { opacity: 0.4; }
}
</style>
