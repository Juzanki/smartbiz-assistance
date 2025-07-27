<!-- src/views/my_logs.vue -->
<template>
  <div class="p-6 min-h-screen bg-[#0a1f44] text-white font-sans">
    <div class="max-w-3xl mx-auto">

      <!-- 🧭 Top Header -->
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold flex items-center gap-1 text-white">
          📋 <span>Activity Log</span>
        </h1>
        <span class="text-xs text-white/70">Last updated: {{ lastUpdated }}</span>
      </div>

      <!-- 🧭 Tabs -->
      <div class="flex gap-3 mb-4 text-sm flex-wrap">
        <button
          v-for="tab in tabs"
          :key="tab.label"
          :class="[
            'px-4 py-2 rounded-full transition',
            currentTab === tab.label ? 'bg-blue-600 text-white' : 'bg-white/10 text-white/60 hover:bg-white/20'
          ]"
          @click="currentTab = tab.label"
        >
          {{ tab.label }} ({{ tab.count }})
        </button>
        <div class="ml-auto text-xs text-white/60 pt-2">
          Showing {{ filteredLogs.length }} logs
        </div>
      </div>

      <!-- 🔍 Search + Tools -->
      <div class="flex flex-wrap gap-3 items-center justify-between mb-4">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search logs..."
          class="px-3 py-2 rounded-lg bg-white/10 text-white placeholder-white/50 border border-white/20 w-full max-w-sm focus:outline-none focus:ring focus:ring-blue-400"
        />
        <div class="flex gap-2 items-center">
          <label class="flex items-center gap-1 text-sm text-white/80">
            <input type="checkbox" v-model="autoRefresh" class="accent-blue-500" />
            Auto Refresh
          </label>
          <button
            @click="exportToCSV"
            class="px-4 py-2 bg-green-600 hover:bg-green-700 rounded-lg text-white shadow"
          >
            📥 Export CSV
          </button>
        </div>
      </div>

      <!-- 🧊 Grouped Logs by Date -->
      <div
        v-for="(group, dateLabel) in groupedLogs"
        :key="dateLabel"
        class="mb-6 bg-white/10 border border-white/10 rounded-xl shadow-md backdrop-blur p-5"
      >
        <h2 class="text-sm font-bold text-white/80 mb-4">{{ dateLabel }}</h2>
        <ul>
          <li
            v-for="(log, index) in group"
            :key="index"
            class="py-3 border-b border-white/10 last:border-b-0"
          >
            <div class="text-sm font-medium text-white">
              {{ getIcon(log.action) }} {{ log.action }}
            </div>
            <div class="text-xs text-white/60">{{ log.timestamp }}</div>
          </li>
        </ul>
      </div>

      <!-- 🔁 Refresh Button -->
      <div class="text-right mt-6">
        <button
          class="px-4 py-2 bg-blue-600 hover:bg-blue-700 active:scale-95 text-white rounded-lg shadow transition-all duration-200"
          @click="refreshLogs"
        >
          🔄 Refresh Logs
        </button>
      </div>

      <!-- ✅ Toast -->
      <transition name="fade">
        <div
          v-if="showToast"
          class="fixed bottom-6 right-6 bg-green-600 text-white text-sm px-4 py-2 rounded-lg shadow-lg"
        >
          🔄 Logs updated successfully!
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const logs = ref([])
const lastUpdated = ref(new Date().toLocaleString())
const searchQuery = ref('')
const autoRefresh = ref(false)
const showToast = ref(false)

const currentTab = ref('All Logs')

let intervalId = null

const loadLogs = () => {
  logs.value = [
    { action: 'User logged in', timestamp: '2025-07-02 08:00 AM', type: 'User' },
    { action: 'System backup completed', timestamp: '2025-07-01 10:00 PM', type: 'System' },
    { action: 'Updated profile picture', timestamp: '2025-07-01 05:44 AM', type: 'User' },
    { action: 'Subscribed to SmartBiz Pro', timestamp: '2025-06-30 09:21 PM', type: 'User' },
    { action: 'Accessed dashboard', timestamp: '2025-06-30 08:00 PM', type: 'System' },
    { action: 'Changed password', timestamp: '2025-06-29 03:15 PM', type: 'User' },
    { action: 'Logged out', timestamp: '2025-06-28 02:50 PM', type: 'User' }
  ]
}

const tabs = computed(() => {
  const userCount = logs.value.filter(l => l.type === 'User').length
  const sysCount = logs.value.filter(l => l.type === 'System').length
  return [
    { label: 'All Logs', count: logs.value.length },
    { label: 'User Logs', count: userCount },
    { label: 'System Logs', count: sysCount }
  ]
})

const filteredLogs = computed(() =>
  logs.value
    .filter(log =>
      (currentTab.value === 'All Logs' || log.type === currentTab.value.replace(' Logs', '')) &&
      log.action.toLowerCase().includes(searchQuery.value.toLowerCase())
    )
    .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
)

const getIcon = (action) => {
  if (action.includes('logged')) return '👤'
  if (action.includes('profile')) return '🖼️'
  if (action.includes('dashboard')) return '📊'
  if (action.includes('Subscribed')) return '💎'
  if (action.includes('password')) return '🔐'
  if (action.includes('backup')) return '🗄️'
  return '📝'
}

const refreshLogs = () => {
  loadLogs()
  lastUpdated.value = new Date().toLocaleString()
  showToast.value = true
  setTimeout(() => (showToast.value = false), 3000)
}

// Group logs by human-readable date
const groupedLogs = computed(() => {
  const groups = {}
  const today = new Date().toDateString()
  const yesterday = new Date(Date.now() - 86400000).toDateString()

  filteredLogs.value.forEach(log => {
    const logDate = new Date(log.timestamp).toDateString()
    const group =
      logDate === today
        ? '📅 Today'
        : logDate === yesterday
        ? '🕓 Yesterday'
        : '📂 Older'
    if (!groups[group]) groups[group] = []
    groups[group].push(log)
  })

  return groups
})

const exportToCSV = () => {
  const csvContent = 'data:text/csv;charset=utf-8,Action,Timestamp\n' +
    logs.value.map(log => `"${log.action}","${log.timestamp}"`).join('\n')

  const encodedUri = encodeURI(csvContent)
  const link = document.createElement('a')
  link.setAttribute('href', encodedUri)
  link.setAttribute('download', `activity_logs_${Date.now()}.csv`)
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

watch(autoRefresh, (enabled) => {
  if (enabled) {
    intervalId = setInterval(refreshLogs, 10000)
  } else {
    clearInterval(intervalId)
  }
})

onMounted(() => {
  loadLogs()
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
