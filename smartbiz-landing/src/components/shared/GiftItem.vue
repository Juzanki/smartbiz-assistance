<template>
  <div
    class="gift-card gift-item flex flex-col items-center justify-center w-full relative cursor-pointer overflow-visible glow-shine transition-transform duration-300 ease-out"
    :class="[
      tierClass,
      effectClass,
      isSelected ? 'gift-selected' : ''
    ]"
    :data-animation="animation"
    @click="$emit('click')"
    role="button"
    tabindex="0"
  >
    <!-- 🎥 Background Video -->
    <video
      v-if="video"
      :src="video"
      autoplay
      muted
      loop
      playsinline
      class="absolute inset-0 w-full h-full object-contain opacity-20 pointer-events-none z-0 rounded-2xl"
    ></video>

    <!-- 🎁 Gift Icon -->
    <div class="gift-icon w-16 h-16 rounded-2xl overflow-hidden shadow-md border border-white/10 backdrop-blur-sm relative z-10">
      <div class="absolute inset-0 gift-glow-overlay pointer-events-none z-10" />
      <img
        :src="src"
        :alt="name"
        class="w-full h-full object-contain p-1 relative z-20 gift-img-glow"
      />
    </div>

    <!-- 🏷️ Gift Name -->
    <span class="gift-name mt-1 z-20">
      {{ name }}
    </span>

    <!-- 🪙 Coin Display -->
    <div class="gift-coins mt-0.5 z-20">
      <img src="/icons/smartbiz-coin.png" class="w-3 h-3" />
      {{ formattedCoins }}
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  src: { type: String, required: true },
  name: { type: String, required: true },
  coins: { type: Number, required: true },
  tier: { type: String, default: '' },
  video: { type: String, default: '' },
  effectClass: { type: String, default: '' },
  animation: { type: String, default: '' },
  selected: { type: Boolean, default: false }
})

defineEmits(['click'])

const formattedCoins = computed(() => {
  const v = props.coins
  if (v < 1_000) return `${v}`
  if (v < 1_000_000) return `${(v / 1_000).toFixed(1)}K`
  return `${(v / 1_000_000).toFixed(1)}M`
})

const tierClass = computed(() => {
  switch (props.tier?.toLowerCase()) {
    case 'rare':
      return 'border-purple-400 shadow-[0_0_12px_rgba(168,85,247,0.4)]'
    case 'epic':
      return 'border-pink-500 shadow-[0_0_14px_rgba(236,72,153,0.45)]'
    case 'legendary':
      return 'border-yellow-400 shadow-[0_0_16px_rgba(251,191,36,0.5)]'
    case 'mythic':
      return 'border-cyan-400 shadow-[0_0_18px_rgba(34,211,238,0.5)]'
    case 'supreme':
      return 'border-red-500 shadow-[0_0_20px_rgba(239,68,68,0.5)]'
    default:
      return 'border-white/10 shadow-none'
  }
})

const isSelected = computed(() => props.selected)
</script>

<style scoped>
/* Styles controlled from parent component (e.g., GiftDrawer.vue or global) */
</style>
