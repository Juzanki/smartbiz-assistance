<template>
  <DashboardLayout>
    <div class="p-6 space-y-6 relative">
      <!-- AI Smart Title -->
      <div class="flex items-center justify-between">
        <h2 class="text-3xl font-extrabold text-gradient bg-gradient-to-r from-blue-500 via-purple-500 to-indigo-500 bg-clip-text text-transparent">
          🧐 Live Drone Monitor with AI Insight
        </h2>
        <span class="text-xs bg-gradient-to-r from-green-400 to-emerald-600 text-white px-3 py-1 rounded-full animate-pulse shadow-md">
          AI-Powered • Real-Time
        </span>
      </div>

      <!-- Animated Loading if No Drones -->
      <div v-if="!missions.length" class="text-center py-16">
        <img src="/ai/ai-drone-idle.gif" class="w-48 mx-auto opacity-80 mb-4" />
        <p class="text-gray-500 dark:text-gray-400 text-lg">🚫 No active drone missions detected</p>
        <p class="text-xs text-sky-500 mt-1">AI is on standby, waiting for the next flight plan...</p>
      </div>

      <!-- 🚀 Live Drone Table -->
      <div v-else class="overflow-auto rounded-2xl shadow-2xl border border-white/10 backdrop-blur-xl bg-white/5">
        <table class="min-w-full text-sm text-white font-mono tracking-wide">
          <thead class="bg-gradient-to-r from-sky-700 to-indigo-800 text-white uppercase text-xs sticky top-0">
            <tr>
              <th class="px-4 py-3 text-left">Drone ID</th>
              <th class="px-4 py-3 text-left">Product</th>
              <th class="px-4 py-3 text-left">📍 Location</th>
              <th class="px-4 py-3 text-left">⚙️ Status</th>
              <th class="px-4 py-3 text-left">⏳ ETA</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="mission in missions"
              :key="mission.id"
              class="border-t border-white/10 hover:bg-white/5 transition-all duration-200"
            >
              <td class="px-4 py-3">{{ mission.drone_id }}</td>
              <td class="px-4 py-3">{{ mission.product_name }}</td>
              <td class="px-4 py-3">{{ mission.destination }}</td>
              <td class="px-4 py-3">
                <span
                  :class="statusClass(mission.status)"
                  class="font-bold px-3 py-1 rounded-full text-xs"
                >
                  {{ mission.status }}
                </span>
              </td>
              <td class="px-4 py-3">
                <Countdown :eta="mission.eta" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- AI Assistant Prompt -->
      <div class="absolute top-2 right-4 bg-gradient-to-br from-purple-900 to-black text-white text-xs px-3 py-1 rounded-full shadow-md animate-bounce">
        🤖 AI: Monitoring altitude & route health...
      </div>
    </div>
  </DashboardLayout>
</template>
<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import axios from 'axios'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

// ✅ Import audio files from public folder using plain path
const droneDelivered = new Audio('/assets/sounds/delivered.mp3')
const droneFailed = new Audio('/assets/sounds/failed.mp3')

const missions = ref([])
const previousStatuses = ref({})
const refreshInterval = ref(null)

// 🔊 Play sound when status changes
const playDelivered = () => droneDelivered.play()
const playFailed = () => droneFailed.play()

// 🚀 Fetch drone missions and trigger AI logic
const fetchMissions = async () => {
  try {
    const token = localStorage.getItem('access_token')
    const { data } = await axios.get('/drones/missions', {
      headers: { Authorization: `Bearer ${token}` }
    })

    data.forEach((mission) => {
      const prev = previousStatuses.value[mission.id]
      if (prev && prev !== mission.status) {
        if (mission.status === 'delivered') playDelivered()
        if (mission.status === 'failed') playFailed()
      }
      previousStatuses.value[mission.id] = mission.status
    })

    missions.value = data
    console.log(`[AI] ${data.length} missions fetched.`)
  } catch (err) {
    console.warn('[AI] Failed to fetch missions:', err)
  }
}

// 🎨 Mission status styling
const statusClass = (status) => {
  return {
    'bg-yellow-100 text-yellow-800': status === 'in-transit',
    'bg-green-100 text-green-800': status === 'delivered',
    'bg-red-100 text-red-800': status === 'failed',
    'bg-blue-100 text-blue-800': status === 'scheduled',
    'bg-gray-100 text-gray-700': !['in-transit', 'delivered', 'failed', 'scheduled'].includes(status)
  }
}

onMounted(() => {
  fetchMissions()
  refreshInterval.value = setInterval(fetchMissions, 30000)
})

onBeforeUnmount(() => {
  clearInterval(refreshInterval.value)
})
</script>

<style scoped>
/* 🌐 Global Table Aesthetic */
table {
  @apply w-full border-collapse text-sm font-mono text-white;
  background: linear-gradient(to bottom right, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.9));
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  overflow: hidden;
}

/* 🧊 Header Row */
th {
  @apply text-left uppercase text-xs px-4 py-3 tracking-widest;
  background-image: linear-gradient(to right, #0284c7, #4f46e5);
  color: white;
  white-space: nowrap;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

/* 🛰️ Data Rows */
td {
  @apply px-4 py-3 text-white whitespace-nowrap transition-colors duration-300;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

tr:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

/* 🌈 Status Badge Enhancements */
.status-badge {
  @apply font-bold px-3 py-1 rounded-full text-xs;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.05);
}

/* 🧠 AI Monitor Badge */
.ai-badge {
  @apply absolute top-2 right-4 text-xs text-white px-3 py-1 rounded-full shadow-md animate-bounce;
  background: linear-gradient(135deg, #7e22ce, #0f172a);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* 🌀 Animated Row Transition */
tr {
  transition: all 0.3s ease-in-out;
}

/* 🔆 Blinking effect (e.g., for ETA countdown) */
.blink {
  animation: blink 1.2s infinite;
}
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.25; }
}
</style>
