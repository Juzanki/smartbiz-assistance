<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg">
    <h3 class="text-xl font-bold mb-3 text-blue-600 dark:text-yellow-400">🧠 Kernel Monitor</h3>

    <div v-if="loading" class="text-yellow-500 text-sm">🔄 Inapokea taarifa kutoka kernel...</div>
    <div v-if="error" class="text-red-500 text-sm">⚠️ {{ error }}</div>

    <ul v-if="status" class="mt-4 space-y-2 text-sm">
      <li><strong>Uptime:</strong> {{ status.uptime }}</li>
      <li><strong>Modules Active:</strong> {{ status.modules_active }}</li>
      <li><strong>Pending Tasks:</strong> {{ status.pending_tasks }}</li>
      <li><strong>Last Sync:</strong> {{ status.last_sync }}</li>
      <li><strong>Status:</strong> <span :class="statusClass">{{ status.kernel_status }}</span></li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const status = ref(null)
const loading = ref(true)
const error = ref('')
const statusClass = ref('')

const fetchStatus = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/smartinject/status')
    status.value = res.data

    // Dynamically apply class based on status
    statusClass.value =
      res.data.kernel_status === 'active'
        ? 'text-green-500'
        : res.data.kernel_status === 'paused'
        ? 'text-yellow-500'
        : 'text-red-500'
  } catch (e) {
    error.value = 'Imeshindwa kuwasiliana na kernel.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchStatus)
</script>
