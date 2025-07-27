<template>
  <!-- 🌌 Clickable Backdrop to Close -->
  <div
    class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex justify-center items-end sm:items-center"
    @click.self="$emit('close')"
  >
    <!-- 🏱 Gift Drawer Box -->
    <div
      class="w-full max-w-3xl bg-gradient-to-br from-[#0f172a] via-[#1e293b] to-[#1e40af] rounded-3xl shadow-2xl border border-white/10 overflow-hidden animate-fade-in flex flex-col max-h-[85vh]"
    >
      <!-- 🔝 Header -->
      <div class="flex flex-col items-center px-6 py-5 bg-white/10 border-b border-white/10 relative">
        <div class="absolute top-3 right-4">
          <button @click="$emit('close')" class="text-white/80 hover:text-red-400 text-3xl font-bold">
            &times;
          </button>
        </div>
        <h2 class="text-xl font-bold text-pink-400 flex items-center gap-2 tracking-wide">
          🏱 <span>Select a Gift</span>
        </h2>
        <p class="text-sm text-white/80 font-semibold mt-1 bg-black/30 px-5 py-1.5 rounded-full backdrop-blur-sm shadow">
          🪙 Balance: {{ userCoins.toLocaleString() }} Coins
        </p>
      </div>

      <!-- 🔖 Tabs -->
      <div class="flex items-center gap-2 px-6 pt-4 overflow-x-auto text-sm font-semibold text-white/70 whitespace-nowrap">
        <button
          v-for="tab in tabs"
          :key="tab"
          @click="activeTab = tab"
          :class="[
            'px-4 py-1.5 rounded-full transition border border-white/10 backdrop-blur-md',
            activeTab === tab ? 'bg-pink-500 text-white shadow-md' : 'hover:bg-white/10 hover:text-white'
          ]"
        >
          {{ tab }}
        </button>
      </div>

      <!-- 🧱 Gift Grid -->
      <div class="overflow-y-auto flex-1 p-6 gift-scroll-area">
        <div class="grid grid-cols-3 sm:grid-cols-4 gap-5">
          <div
            v-for="gift in filteredGifts"
            :key="gift.id"
            @click="sendGift(gift)"
            class="flex flex-col items-center bg-white/5 p-4 rounded-2xl border border-white/10 shadow gift-tile cursor-pointer hover:scale-105 transition-transform duration-300"
          >
            <img :src="gift.icon" alt="gift icon" class="w-16 h-16 object-contain mb-2 rounded-md shadow-md" />
            <span class="text-sm font-semibold text-white text-center tracking-wide">{{ gift.name }}</span>
            <span class="text-xs text-yellow-300 font-semibold mt-1 flex items-center gap-1">
              <img src="/icons/smartbiz-coin.png" class="w-3.5 h-3.5" />
              {{ gift.coins.toLocaleString() }}
            </span>
          </div>
        </div>
      </div>

      <!-- 💳 Footer -->
      <div class="flex justify-between items-center px-6 py-4 border-t border-white/10 bg-white/5 backdrop-blur-md">
        <span class="text-xs text-white/70">Need more coins?</span>
        <router-link
          to="/wallet/recharge"
          class="bg-yellow-400 hover:bg-yellow-500 text-black text-xs px-4 py-2 rounded-full font-semibold shadow transition"
          @click="$emit('close')"
        >
          + Recharge
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { giftList } from '@/data/giftList.js'

const props = defineProps({
  gifts: {
    type: Array,
    default: () => giftList
  },
  userCoins: {
    type: Number,
    default: 0
  }
})
const emit = defineEmits(['close', 'send'])

const tabs = ['All', 'Lite', 'Rare', 'Epic', 'Legendary', 'Mythic', 'Supreme']
const activeTab = ref('All')

const filteredGifts = computed(() => {
  if (activeTab.value === 'All') return props.gifts
  return props.gifts.filter(g => g.tier?.toLowerCase() === activeTab.value.toLowerCase())
})

const sendGift = (gift) => {
  emit('send', {
    ...gift,
    timestamp: Date.now()
  })
  setTimeout(() => {
    emit('close')
  }, 150)
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeInDrawer 0.45s cubic-bezier(0.22, 1, 0.36, 1) both;
}
@keyframes fadeInDrawer {
  0% {
    opacity: 0;
    transform: translateY(80px) scale(0.92);
    filter: blur(8px) brightness(0.8);
  }
  60% {
    filter: blur(2px) brightness(1.1);
    transform: translateY(10px) scale(1.02);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0) brightness(1);
  }
}

.gift-tile {
  background: linear-gradient(to bottom right, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-radius: 1rem;
  position: relative;
  overflow: hidden;
}
.gift-tile:hover {
  transform: scale(1.08);
  box-shadow:
    0 0 16px rgba(255, 255, 255, 0.05),
    0 0 22px rgba(255, 105, 180, 0.2),
    0 0 36px rgba(255, 255, 255, 0.06);
}
.gift-tile::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 1rem;
  background: radial-gradient(circle at top left, rgba(255, 255, 255, 0.06), transparent);
  pointer-events: none;
  z-index: 1;
}

.gift-scroll-area {
  scrollbar-width: thin;
}
.gift-scroll-area::-webkit-scrollbar {
  width: 6px;
}
.gift-scroll-area::-webkit-scrollbar-thumb {
  background-color: rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  transition: background-color 0.3s;
}
.gift-scroll-area::-webkit-scrollbar-thumb:hover {
  background-color: rgba(255, 255, 255, 0.3);
}
</style>
