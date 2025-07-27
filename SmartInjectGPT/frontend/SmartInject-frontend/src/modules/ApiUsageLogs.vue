<template>
  <div class="p-6 bg-white dark:bg-[#0d1b2a] min-h-screen">
    <h2 class="text-2xl font-bold mb-4 text-yellow-400">API Usage Logs</h2>

    <div class="grid grid-cols-1 sm:grid-cols-4 gap-4 mb-6">
      <input v-model="filters.api_key_id" type="number" placeholder="API Key ID" class="input" />
      <input v-model="filters.endpoint" type="text" placeholder="Endpoint" class="input" />
      <select v-model="filters.method" class="input">
        <option value="">All Methods</option>
        <option value="GET">GET</option>
        <option value="POST">POST</option>
      </select>
      <input type="date" v-model="filters.start_date" class="input" />
      <input type="date" v-model="filters.end_date" class="input" />
      <button @click="fetchLogs" class="btn col-span-1 sm:col-span-2 bg-yellow-400 hover:bg-yellow-500 text-black font-bold py-2 px-4 rounded">
        Search Logs
      </button>
    </div>

    <div v-if="loading" class="text-center text-gray-500 dark:text-gray-300">Loading logs...</div>
    <div v-else-if="logs.length === 0" class="text-center text-gray-500 dark:text-gray-300">No logs found.</div>

    <table v-else class="table-auto w-full border-collapse mt-4">
      <thead class="bg-[#1b263b] text-yellow-400">
        <tr>
          <th class="px-4 py-2">Time</th>
          <th class="px-4 py-2">API Key</th>
          <th class="px-4 py-2">Endpoint</th>
          <th class="px-4 py-2">Method</th>
          <th class="px-4 py-2">Status</th>
          <th class="px-4 py-2">IP</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="log in logs" :key="log.id" class="text-gray-800 dark:text-gray-200">
          <td class="border px-4 py-2">{{ formatDate(log.timestamp) }}</td>
          <td class="border px-4 py-2">{{ log.api_key_id }}</td>
          <td class="border px-4 py-2">{{ log.endpoint }}</td>
          <td class="border px-4 py-2">{{ log.method }}</td>
          <td class="border px-4 py-2">{{ log.status_code }}</td>
          <td class="border px-4 py-2">{{ log.ip_address }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const logs = ref([])
const loading = ref(false)
const filters = ref({
  api_key_id: '',
  endpoint: '',
  method: '',
  start_date: '',
  end_date: ''
})

const fetchLogs = async () => {
  loading.value = true
  try {
    const params = { ...filters.value }
    const response = await axios.get('/admin/api-logs', { params })
    logs.value = response.data
  } catch (err) {
    console.error('Error fetching logs:', err)
    logs.value = []
  } finally {
    loading.value = false
  }
}

const formatDate = (iso) => new Date(iso).toLocaleString()
</script>

<style scoped>
.input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 8px;
  width: 100%;
}

.btn {
  transition: background 0.3s ease;
}
</style>
