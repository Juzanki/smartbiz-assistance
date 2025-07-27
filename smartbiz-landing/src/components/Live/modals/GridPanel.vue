<template>
  <div class="relative w-full min-h-screen bg-gradient-to-br from-black via-indigo-950 to-gray-900 p-6">
    <!-- 🎛️ Grid Mode Selector -->
    <div class="flex items-center justify-between mb-6 text-white">
      <h2 class="text-xl font-bold tracking-wide">🧬 Smart Grid Panel</h2>
      <select v-model="gridMode" class="bg-black/30 border border-white/20 rounded px-4 py-2 text-white">
        <option value="1x1">🔲 1x1</option>
        <option value="2x2">🧩 2x2</option>
        <option value="3x3">🔳 3x3</option>
        <option value="6x6">🧠 6x6</option>
        <option value="dynamic">♾️ Dynamic</option>
      </select>
    </div>

    <!-- 🧱 GRID DISPLAY -->
    <div :class="gridClasses" class="gap-4 transition-all duration-500">
      <div
        v-for="(slot, index) in computedSlots"
        :key="index"
        class="relative border border-white/10 bg-white/5 rounded-xl backdrop-blur-md flex items-center justify-center shadow-lg hover:shadow-pink-500/50 group overflow-hidden"
      >
        <template v-if="slot.occupied">
          <!-- 🎥 Guest Stream View -->
          <div class="flex flex-col items-center text-white text-sm">
            <img :src="slot.avatar" class="w-12 h-12 rounded-full border border-white shadow" />
            <div class="mt-2 font-bold">{{ slot.name }}</div>
            <div class="flex gap-2 mt-1 text-xs">
              <button @click="toggleMic(slot)" :class="slot.mic ? 'text-green-400' : 'text-red-400'">🎙</button>
              <button @click="toggleCam(slot)" :class="slot.cam ? 'text-blue-400' : 'text-gray-400'">📷</button>
              <button @click="expandSlot(index)" class="hover:text-yellow-300">🔍</button>
              <button @click="removeGuest(index)" class="hover:text-red-500">🗑</button>
            </div>
          </div>
        </template>
        <template v-else>
          <!-- 👑 Royal Chair if empty -->
          <div class="text-pink-400 font-bold text-xs animate-pulse">👑 Empty Royal Slot</div>
        </template>

        <!-- 💡 Overlay for hover -->
        <div
          class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 flex items-center justify-center transition"
        >
          <button
            @click="assignGuest(index)"
            class="bg-pink-500 hover:bg-pink-600 text-white px-4 py-1 rounded-full text-xs"
          >
            + Assign Guest
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const gridMode = ref('2x2')
const guestPool = [
  { name: 'Zena', avatar: '/avatars/user1.png', mic: true, cam: true },
  { name: 'Amani', avatar: '/avatars/user2.png', mic: false, cam: true },
  { name: 'Baraka', avatar: '/avatars/user3.png', mic: true, cam: false },
  { name: 'Malaika', avatar: '/avatars/user4.png', mic: true, cam: true },
  { name: 'Juzzy', avatar: '/avatars/user5.png', mic: true, cam: true },
  { name: 'Fahima', avatar: '/avatars/user6.png', mic: false, cam: false }
]

const slots = ref(Array.from({ length: 9 }, () => ({ occupied: false, name: '', avatar: '', mic: false, cam: false })))

const gridClasses = computed(() => {
  switch (gridMode.value) {
    case '1x1': return 'grid grid-cols-1';
    case '2x2': return 'grid grid-cols-2';
    case '3x3': return 'grid grid-cols-3';
    case '6x6': return 'grid grid-cols-6';
    case 'dynamic': return `grid grid-cols-${Math.ceil(Math.sqrt(slots.value.length))}`
    default: return 'grid grid-cols-2';
  }
})

const computedSlots = computed(() => {
  const count = gridMode.value === '1x1' ? 1 : gridMode.value === '2x2' ? 4 : gridMode.value === '3x3' ? 9 : gridMode.value === '6x6' ? 36 : 16
  return Array.from({ length: count }, (_, i) => slots.value[i] || { occupied: false })
})

function assignGuest(index) {
  const guest = guestPool[Math.floor(Math.random() * guestPool.length)]
  slots.value[index] = { ...guest, occupied: true }
}

function toggleMic(slot) {
  slot.mic = !slot.mic
}

function toggleCam(slot) {
  slot.cam = !slot.cam
}

function removeGuest(index) {
  slots.value[index] = { occupied: false }
}

function expandSlot(index) {
  alert(`🔍 Expand Guest at Slot #${index + 1}`)
}
</script>

<style scoped>
.grid > div {
  min-height: 150px;
  transition: all 0.4s ease;
}
</style>
