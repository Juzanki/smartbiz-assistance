<template>
  <div class="min-h-screen bg-[#0d1b2a] text-white p-6">
    <h2 class="text-2xl font-bold text-yellow-400 mb-6">System Activity Logs</h2>

    <div class="bg-[#1b263b] p-4 rounded-xl shadow overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="text-left text-yellow-300 border-b border-gray-600">
            <th>User</th>
            <th>Role</th>
            <th>Action</th>
            <th>Module</th>
            <th>IP Address</th>
            <th>Device</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="log in logs"
            :key="log.id"
            class="border-b border-gray-700 hover:bg-[#0d1b2a]/70 transition"
          >
            <td class="font-semibold">
              <span :class="log.role === 'owner' ? 'text-yellow-400' : log.role === 'admin' ? 'text-blue-300' : 'text-purple-300'">
                {{ log.user_email || 'System' }}
              </span>
            </td>
            <td>
              <span
                class="px-2 py-1 text-xs rounded-full font-semibold"
                :class="{
                  'bg-yellow-500 text-[#0d1b2a]': log.role === 'owner',
                  'bg-blue-500 text-white': log.role === 'admin',
                  'bg-purple-600 text-white': log.role === 'system'
                }"
              >
                {{ log.role }}
              </span>
            </td>
            <td class="text-green-300">{{ log.action }}</td>
            <td>{{ log.module || 'General' }}</td>
            <td>{{ log.ip_address || 'N/A' }}</td>
            <td>{{ log.device || 'Unknown' }}</td>
            <td>{{ formatTime(log.timestamp) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const logs = ref([])

const fetchLogs = async () => {
  try {
    const res = await axios.get('/api/activity/logs')
    logs.value = res.data
  } catch (err) {
    console.error('Failed to load activity logs', err)
  }
}

const formatTime = (timestamp) => {
  const d = new Date(timestamp)
  return d.toLocaleString()
}

onMounted(fetchLogs)
</script>

<style scoped>
table th,
table td {
  padding: 0.5rem;
}
</style>
