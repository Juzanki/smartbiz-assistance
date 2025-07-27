<template>
  <!-- 🌌 Gift Drawer Backdrop -->
  <transition name="fade">
    <div
      v-if="visible"
      class="fixed inset-0 z-[90] flex justify-center items-end sm:items-center bg-black/50 backdrop-blur-xl"
      @click.self="$emit('close')"
    >
      <!-- 🎁 Drawer Panel -->
      <div class="w-full max-w-4xl bg-gradient-to-br from-[#0f172a]/90 via-[#1e293b]/90 to-[#334155]/90 rounded-t-3xl sm:rounded-2xl shadow-2xl border border-white/10 overflow-hidden animate-fade-in flex flex-col max-h-[88vh]">

        <!-- 🔝 Drawer Header -->
        <div class="flex justify-between items-center px-6 py-4 border-b border-white/10 bg-white/5 backdrop-blur-sm">
          <h2 class="text-lg font-bold text-pink-400 flex items-center gap-2">
            🎁 <span>Select a Gift</span>
          </h2>

          <!-- 💰 Coin Balance -->
          <div class="flex items-center gap-1 text-yellow-300 text-xs font-bold bg-white/10 px-3 py-1 rounded-full border border-yellow-400/30 shadow-inner">
            <img src="/icons/smartbiz-coin.png" alt="Coin" class="w-4 h-4" />
            <span>{{ userCoins.toLocaleString() }}</span>
          </div>

          <!-- ❌ Close -->
          <button @click="$emit('close')" class="text-white/80 hover:text-red-500 text-xl">
            <i class="i-tabler-x"></i>
          </button>
        </div>

        <!-- 🧭 Filter Tabs + Sorting -->
        <div class="flex items-center justify-between px-6 py-3 bg-black/20 border-b border-white/10 backdrop-blur-sm">
          <!-- 🎯 Filter -->
          <div class="flex gap-2 overflow-x-auto text-sm font-semibold text-white/70">
            <button
              v-for="tab in tabs"
              :key="tab"
              @click="activeTab = tab"
              :class="[
                'px-3 py-1 rounded-full transition-all whitespace-nowrap border border-white/10',
                activeTab === tab
                  ? 'bg-pink-500 text-white shadow'
                  : 'hover:bg-white/10 hover:text-white'
              ]"
            >
              {{ tab }}
            </button>
          </div>

          <!-- 🔽 Sort Dropdown -->
          <select
            v-model="sortOrder"
            class="px-3 py-1 bg-white/10 border border-white/20 text-white text-xs rounded-full outline-none backdrop-blur"
          >
            <option value="default">Sort</option>
            <option value="price">Price ↑</option>
          </select>
        </div>

        <!-- 🎁 Gift Grid -->
        <div class="flex-1 overflow-y-auto px-6 py-4 gift-scroll-area">
          <div class="grid grid-cols-3 sm:grid-cols-4 gap-5">
            <GiftItem
              v-for="gift in sortedGifts"
              :key="gift.id"
              :src="gift.icon"
              :name="gift.name"
              :coins="gift.coins"
              :video="gift.video"
              :animation="gift.animation"
              :effectClass="gift.effectClass"
              :tier="gift.tier"
              :selected="selectedGiftId === gift.id"
              @click="selectGift(gift)"
            />
          </div>
        </div>

        <!-- 💳 Sticky Recharge CTA -->
        <div class="sticky bottom-0 px-6 py-4 border-t border-white/10 bg-black/30 backdrop-blur-md flex justify-between items-center">
          <span class="text-xs text-white/60">Need more coins?</span>
          <button
            @click="handleRecharge"
            class="bg-gradient-to-r from-yellow-300 to-yellow-500 text-black px-5 py-1.5 rounded-full font-semibold shadow hover:scale-105 transition-transform text-xs flex items-center gap-2"
          >
            <img src="/icons/smartbiz-coin.png" alt="coin" class="w-4 h-4" />
            Recharge / Buy Coins
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>
<script setup>
import { ref, computed, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { giftList } from '@/data/giftList.js'
import GiftItem from '../shared/GiftItem.vue'

// 🌐 Router & Toast
const router = useRouter()
const toast = useToast()

// 🎯 Props & Emits
const props = defineProps({
  visible: { type: Boolean, default: false },
  receiver: { type: Object, default: null },
  autoCloseAfterSend: { type: Boolean, default: false }
})
const emit = defineEmits(['close', 'send', 'gift-sent'])

// 💰 Coin Balance
const userCoins = ref(1_000_000)

// 🔍 Search, Sort & Selection
const searchTerm = ref('')
const sortOrder = ref('default')
const selectedGiftId = ref(null)
const sending = ref(false)

// 🧭 Tabs
const tabs = ['All', 'Lite', 'Rare', 'Epic', 'Legendary', 'Mythic', 'Supreme']
const activeTab = ref('All')

// 🎁 Filtered Gifts
const filteredGifts = computed(() => {
  const keyword = searchTerm.value.toLowerCase().trim()
  return giftList.filter(gift => {
    const matchTier = activeTab.value === 'All' || gift.tier === activeTab.value
    const matchSearch = gift.name.toLowerCase().includes(keyword)
    return matchTier && matchSearch
  })
})

// ↕️ Sorted Gifts
const sortedGifts = computed(() => {
  if (sortOrder.value === 'price') {
    return [...filteredGifts.value].sort((a, b) => a.coins - b.coins)
  }
  return filteredGifts.value
})

// 💳 Navigate to Recharge Page
const handleRecharge = () => {
  router.push('/wallet/recharge')
}

// 🎉 Placeholder for future coin burst animation
const coinBurst = (iconPath) => {
  console.log(`💥 Coin burst triggered for icon: ${iconPath}`)
}

// 🎁 Send Gift Logic
const selectGift = async (gift) => {
  if (!gift || sending.value) return

  // Check balance
  if (userCoins.value < gift.coins) {
    toast.error('😢 Not enough coins! Redirecting...')
    return router.push('/wallet/recharge')
  }

  sending.value = true
  selectedGiftId.value = gift.id
  userCoins.value -= gift.coins

  // Prepare gift payload
  const payload = {
    ...gift,
    to: props.receiver,
    timestamp: Date.now()
  }

  // Emit gift event to parent (LiveRoom.vue)
  emit('send', payload)
  emit('gift-sent', payload)

  // Visual effect placeholder
  coinBurst(gift.icon)

  // Show success feedback
  toast.success(`🎁 Sent "${gift.name}"!`, { timeout: 2500 })

  // Auto-close drawer and return to stream
  if (props.autoCloseAfterSend) {
    await nextTick()
    emit('close') // Trigger v-show=false in parent
  }

  // Reset selection
  setTimeout(() => {
    selectedGiftId.value = null
    sending.value = false
  }, 600)
}
</script>
<style scoped>
/* 🌌 Entrance Animation */
@keyframes fade-in {
  0% {
    opacity: 0;
    transform: translateY(60px) scale(0.95);
    filter: blur(5px) brightness(0.85);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0) brightness(1);
  }
}
.animate-fade-in {
  animation: fade-in 0.45s cubic-bezier(0.22, 1, 0.36, 1) both;
  will-change: opacity, transform, filter;
}

/* ✨ Sparkling Background Pulse */
@keyframes sparkle {
  0%, 100% {
    box-shadow:
      0 0 6px rgba(255,255,255,0.05),
      0 0 14px rgba(255,105,180,0.15),
      0 0 26px rgba(255,105,180,0.08);
  }
  50% {
    box-shadow:
      0 0 10px rgba(255,255,255,0.12),
      0 0 32px rgba(255,105,180,0.3),
      0 0 60px rgba(255,105,180,0.15);
  }
}

/* 🧧 Gift Card Base Style */
.gift-card {
  position: relative;
  padding: 14px;
  border-radius: 20px;
  background: linear-gradient(145deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
  border: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(10px);
  animation: sparkle 5.5s ease-in-out infinite;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.gift-card:hover {
  transform: scale(1.06);
  box-shadow:
    0 0 12px rgba(255,255,255,0.08),
    0 0 26px rgba(255,105,180,0.25);
}

/* 🔘 Highlight for Selected Gift */
@keyframes pulse-border {
  0% {
    box-shadow: 0 0 0 rgba(255,105,180,0.3);
  }
  50% {
    box-shadow:
      0 0 16px rgba(255,105,180,0.7),
      0 0 32px rgba(255,105,180,0.4);
  }
  100% {
    box-shadow: 0 0 0 rgba(255,105,180,0.2);
  }
}
.gift-selected {
  border: 2px solid rgba(255,105,180,0.75);
  animation: pulse-border 1.6s ease-in-out infinite;
}

/* 💡 Shine Overlay on Hover */
.glow-shine::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.015));
  background-size: 400% 100%;
  animation: shine-slide 3s linear infinite;
}
@keyframes shine-slide {
  0% {
    background-position: -200% center;
  }
  100% {
    background-position: 200% center;
  }
}

/* 🧲 Scroll-Snap Behavior */
.gift-grid {
  scroll-snap-type: y mandatory;
}
.gift-grid > * {
  scroll-snap-align: start;
}

/* 💸 Recharge Button — Golden Glow */
.glow-button {
  background: linear-gradient(to right, #facc15, #fde047);
  color: #111;
  font-weight: 600;
  padding: 0.5rem 1.25rem;
  border-radius: 9999px;
  box-shadow: 0 0 16px rgba(253, 224, 71, 0.4);
  transition: transform 0.25s ease, box-shadow 0.3s ease;
}
.glow-button:hover {
  transform: scale(1.08);
  box-shadow:
    0 0 30px rgba(253, 224, 71, 0.55),
    0 0 60px rgba(253, 224, 71, 0.3);
}

/* 🏷️ Gift Name Text */
.gift-name {
  text-align: center;
  color: white;
  font-size: 0.82rem;
  font-weight: 600;
  margin-top: 6px;
  text-shadow: 0 1px 2px rgba(0,0,0,0.4);
}

/* 🪙 Coins Display */
.gift-coins {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
  margin-top: 2px;
  font-size: 0.75rem;
  font-weight: bold;
  color: #facc15;
}
.gift-coins img {
  width: 14px;
  height: 14px;
  object-fit: contain;
}
</style>
