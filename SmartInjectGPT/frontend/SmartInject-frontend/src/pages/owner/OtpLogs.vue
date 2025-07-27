<template>
  <div class="min-h-screen bg-[#0d1b2a] text-white p-6">
    <h2 class="text-2xl font-bold text-yellow-400 mb-6">OTP Access Logs</h2>

    <div class="bg-[#1b263b] p-4 rounded-xl shadow overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="text-left text-yellow-300 border-b border-gray-600">
            <th>Email</th>
            <th>OTP Code</th>
            <th>Status</th>
            <th>IP Address</th>
            <th>Device</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="log in otpLogs"
            :key="log.id"
            class="border-b border-gray-700 hover:bg-[#0d1b2a]/70 transition"
          >
            <td>{{ log.email }}</td>
            <td>{{ log.otp_code }}</td>
            <td :class="log.success ? 'text-green-400' : 'text-red-400'">
              {{ log.success ? 'Success' : 'Failed' }}
            </td>
            <td>{{ log.ip_address }}</td>
            <td>{{ log.device || 'Unknown' }}</td>
            <td>{{ formatDate(log.timestamp) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const otpLogs = ref([])

const fetchOtpLogs = async () => {
  try {
    const res = await axios.get('/api/otp/logs')
    otpLogs.value = res.data
  } catch (err) {
    console.error('Failed to fetch OTP logs', err)
  }
}

const formatDate = (isoString) => {
  const d = new Date(isoString)
  return d.toLocaleString()
}

onMounted(fetchOtpLogs)
</script>

<style scoped>
table th,
table td {
  padding: 0.5rem;
}
</style>
