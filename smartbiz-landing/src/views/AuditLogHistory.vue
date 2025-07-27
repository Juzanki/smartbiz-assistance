<template>
  <div class="p-6 sm:p-8 min-h-screen bg-gradient-to-br from-slate-900 to-gray-950 text-white">
    <!-- 🔍 Header -->
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-2xl font-bold text-cyan-400 flex items-center gap-2">
        <i class="i-lucide-clipboard-list" /> Audit Log History
      </h1>
    </div>

    <!-- 🧾 Audit Table -->
    <div class="overflow-x-auto rounded-xl border border-cyan-800/40 bg-white/5 shadow-lg">
      <table class="min-w-full text-sm text-left text-white divide-y divide-gray-700">
        <thead class="bg-cyan-800/30 text-cyan-300 uppercase text-xs tracking-wider">
          <tr>
            <th class="px-4 py-3">#</th>
            <th class="px-4 py-3">User ID</th>
            <th class="px-4 py-3">Action</th>
            <th class="px-4 py-3">Target</th>
            <th class="px-4 py-3">Timestamp</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-800">
          <tr v-for="(log, index) in paginatedLogs" :key="log.id" class="hover:bg-white/5 transition">
            <td class="px-4 py-3">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
            <td class="px-4 py-3">
              <span class="inline-block px-2 py-1 bg-cyan-700/40 text-xs rounded-md">
                {{ log.user_id }}
              </span>
            </td>
            <td class="px-4 py-3">{{ log.action }}</td>
            <td class="px-4 py-3">{{ log.target }}</td>
            <td class="px-4 py-3 text-gray-400 italic">{{ formatDate(log.timestamp) }}</td>
          </tr>
          <tr v-if="logs.length === 0">
            <td colspan="5" class="px-4 py-6 text-center text-gray-400">
              No audit logs found.
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 📄 Pagination -->
    <div v-if="totalPages > 1" class="mt-6 flex justify-center items-center gap-2">
      <button @click="currentPage--" :disabled="currentPage === 1" class="px-3 py-1 text-sm bg-cyan-700/30 rounded hover:bg-cyan-700/50 disabled:opacity-30">
        Prev
      </button>
      <span class="text-sm text-gray-300">Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="currentPage++" :disabled="currentPage === totalPages" class="px-3 py-1 text-sm bg-cyan-700/30 rounded hover:bg-cyan-700/50 disabled:opacity-30">
        Next
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const logs = ref([])
const currentPage = ref(1)
const itemsPerPage = 10

onMounted(async () => {
  try {
    const res = await axios.get('/api/admin/audit')
    logs.value = res.data
  } catch (err) {
    console.error('Failed to load audit logs:', err)
  }
})

function formatDate(ts) {
  return new Date(ts).toLocaleString()
}

const totalPages = computed(() => Math.ceil(logs.value.length / itemsPerPage))

const paginatedLogs = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return logs.value.slice(start, start + itemsPerPage)
})
</script>

<style scoped>
::-webkit-scrollbar {
  height: 8px;
}
::-webkit-scrollbar-thumb {
  background: rgba(45, 212, 191, 0.3);
  border-radius: 4px;
}
</style>
