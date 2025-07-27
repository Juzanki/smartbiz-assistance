<template>
  <div class="p-6 bg-white rounded-xl shadow space-y-4 text-gray-800">
    <h2 class="text-lg font-bold">🔭 Vision Console</h2>

    <div class="flex gap-3">
      <button @click="scan" class="px-4 py-2 bg-blue text-white rounded hover:bg-blue-600 transition">Scan Sources</button>
      <button @click="loadReport" class="px-4 py-2 bg-green text-white rounded hover:bg-green-600 transition">View Report</button>
      <button @click="reset" class="px-4 py-2 bg-red text-white rounded hover:bg-red-600 transition">Reset Log</button>
    </div>

    <div v-if="report.length > 0" class="mt-4 overflow-x-auto">
      <table class="w-full border collapse text-sm">
        <thead class="bg-gray-100">
          <tr>
            <th class="p-2 border">Topic</th>
            <th class="p-2 border">Source</th>
            <th class="p-2 border">Risk</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, i) in report" :key="i" class="border-t">
            <td class="p-2 border">{{ entry.topic }}</td>
            <td class="p-2 border text-blue underline truncate max-w-xs">
              <a :href="entry.source" target="_blank">{{ entry.source }}</a>
            </td>
            <td class="p-2 border">{{ entry.risk }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p v-else class="text-gray-500">No vision reports found.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const report = ref([])

const scan = async () => {
  await axios.get('http://127.0.0.1:8010/vision/scan')
  loadReport()
}

const loadReport = async () => {
  const res = await axios.get('http://127.0.0.1:8010/vision/report')
  report.value = res.data.report
}

const reset = async () => {
  await axios.delete('http://127.0.0.1:8010/vision/reset')
  report.value = []
}
</script>
