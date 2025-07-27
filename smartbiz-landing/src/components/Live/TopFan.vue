<template>
  <div class="relative">
    <!-- 🌟 TopFan Button -->
    <button @click="togglePanel" class="relative px-3 py-1 text-xs text-white bg-white/10 rounded-full border border-white/10 backdrop-blur-md shadow hover:bg-white/20 transition">
      🌟 Top Fans
      <span v-if="hasNewData" class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-gradient-to-tr from-red-500 to-yellow-300 animate-ping shadow-lg" />
    </button>

    <!-- 🧾 Top Fans Panel -->
    <div v-if="showPanel" class="absolute right-0 mt-2 w-[280px] max-h-[360px] bg-black/70 text-white p-4 rounded-xl border border-white/10 backdrop-blur-xl z-50 shadow-lg">
      <h3 class="text-center text-sm font-bold mb-3">🏆 Top Fans Ranking</h3>
      <ul class="space-y-2 max-h-[260px] overflow-y-auto pr-1">
        <li
          v-for="(fan, index) in visibleFans.slice(0, 5)"
          :key="fan.username"
          class="flex justify-between items-center px-3 py-1 rounded bg-white/5 border border-white/10 text-xs"
        >
          <span class="font-bold text-yellow-300">#{{ index + 1 }}</span>
          <span class="truncate flex-1 mx-2 text-white">
            {{ fan.username }}
            <span v-if="fan.badge" class="ml-1">{{ fan.badge }}</span>
          </span>
          <span class="text-pink-400 font-semibold">{{ formatPoints(fan.totalPoints) }}</span>
        </li>
      </ul>
      <div class="mt-2 text-center text-xs text-gray-400">
        Total Fans: {{ totalFans > 99 ? '99+' : totalFans }}
      </div>
      <button @click="showModal = true" class="text-cyan-300 hover:underline mt-2 text-xs w-full">
        🔍 View All Contributors
      </button>
    </div>

    <!-- 📦 Full Contributors Modal -->
    <div v-if="showModal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center">
      <div class="bg-zinc-900 text-white rounded-xl w-[90vw] max-w-lg max-h-[80vh] p-5 overflow-y-auto border border-white/10 shadow-2xl">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-bold">🎖 All Top Fans</h2>
          <button @click="showModal = false" class="text-sm text-red-400 hover:text-red-200">✖ Close</button>
        </div>
        <ul class="space-y-2">
          <li
            v-for="(fan, index) in visibleFans"
            :key="fan.username"
            class="flex justify-between items-center px-3 py-1 rounded bg-white/5 border border-white/10 text-sm"
          >
            <span class="font-bold text-yellow-300">#{{ index + 1 }}</span>
            <span class="truncate flex-1 mx-2 text-white">
              {{ fan.username }}
              <span v-if="fan.badge" class="ml-1">{{ fan.badge }}</span>
            </span>
            <span class="text-pink-400 font-semibold">{{ formatPoints(fan.totalPoints) }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const showPanel = ref(false)
const showModal = ref(false)
const hasNewData = ref(true)

const allFans = ref([
  { username: 'Juzanki', gifts: 15000, likes: 400, views: 80, badge: '💎' },
  { username: 'VIPQueen', gifts: 8000, likes: 1000, views: 60, badge: '🥈' },
  { username: 'SmartViewer', gifts: 0, likes: 300, views: 100, badge: '🎖' },
  { username: 'SilentFan', gifts: 0, likes: 0, views: 1000 }
])

const sortedFans = computed(() =>
  allFans.value
    .map(f => ({
      ...f,
      totalPoints: f.gifts * 5 + f.likes * 2 + f.views
    }))
    .sort((a, b) => b.totalPoints - a.totalPoints)
)

const visibleFans = computed(() => sortedFans.value.slice(0, 99))
const totalFans = computed(() => allFans.value.length)

function togglePanel() {
  showPanel.value = !showPanel.value
  hasNewData.value = false
}

function formatPoints(num) {
  if (num >= 1000000) return (num / 1000000).toFixed(1).replace(/\.0$/, '') + 'M'
  if (num >= 1000) return (num / 1000).toFixed(1).replace(/\.0$/, '') + 'k'
  return num.toString()
}
</script>
