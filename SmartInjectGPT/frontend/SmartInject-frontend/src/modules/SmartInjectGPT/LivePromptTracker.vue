<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg mt-6">
    <h3 class="text-xl font-bold mb-3 text-blue-600 dark:text-yellow-400">📡 Live Prompt Tracker</h3>

    <div v-if="loading" class="text-yellow-400 text-sm">⏳ Inasubiri shughuli kutoka kernel...</div>

    <div class="space-y-2 text-sm">
      <div
        v-for="(entry, index) in logs"
        :key="index"
        class="p-3 rounded bg-gray-100 dark:bg-[#1b2c3a] border-l-4"
        :class="{
          'border-blue-500': entry.status === 'started',
          'border-green-500': entry.status === 'done',
          'border-yellow-500': entry.status === 'waiting'
        }"
      >
        <strong>📥 {{ entry.prompt }}</strong>
        <div class="text-xs mt-1">
          <span class="text-gray-500 dark:text-gray-300">⏱ {{ entry.timestamp }}</span><br />
          <span class="italic text-green-500" v-if="entry.status === 'done'">✅ Completed</span>
          <span class="italic text-yellow-500" v-else-if="entry.status === 'waiting'">⏳ Waiting...</span>
          <span class="italic text-blue-500" v-else>🚧 In progress...</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const logs = ref([])
const loading = ref(true)

const fetchLogs = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/smartinject/live-log')
    logs.value = res.data || []
  } catch (err) {
    logs.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchLogs()
  setInterval(fetchLogs, 5000) // refresh kila sekunde 5
})
</script>
