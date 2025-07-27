<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg">
    <h3 class="text-xl font-bold mb-3 text-blue-600 dark:text-yellow-400">📜 Prompt History</h3>

    <div v-if="loading" class="text-yellow-400 text-sm">⏳ Inapakia historia...</div>
    <div v-if="error" class="text-red-500 text-sm">⚠️ {{ error }}</div>

    <ul v-if="history.length" class="space-y-4 text-sm mt-4">
      <li v-for="item in history" :key="item.timestamp" class="p-3 rounded bg-gray-100 dark:bg-[#1b2c3a]">
        <div><strong>📝 Prompt:</strong> {{ item.prompt }}</div>
        <div><strong>📅 Muda:</strong> {{ item.timestamp }}</div>
        <div><strong>📦 Majibu:</strong> {{ item.response }}</div>
      </li>
    </ul>

    <div v-else-if="!loading" class="text-gray-500 mt-4">Hakuna prompt bado...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const history = ref([])
const loading = ref(true)
const error = ref('')

const fetchHistory = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/smartinject/history')
    history.value = res.data || []
  } catch (err) {
    error.value = 'Imeshindwa kupakua historia kutoka kernel.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchHistory)
</script>
