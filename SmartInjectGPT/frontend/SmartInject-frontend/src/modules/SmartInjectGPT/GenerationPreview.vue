<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg">
    <h3 class="text-xl font-bold mb-3 text-blue-600 dark:text-yellow-400">👁️ Generation Preview</h3>

    <div v-if="loading" class="text-yellow-400 text-sm">⏳ Inapakia mafaili kutoka kernel...</div>
    <div v-if="error" class="text-red-500 text-sm">⚠️ {{ error }}</div>

    <ul v-if="files.length" class="mt-4 space-y-4 text-sm">
      <li
        v-for="file in files"
        :key="file.filename"
        class="p-4 rounded bg-gray-100 dark:bg-[#1b2c3a] border dark:border-gray-700"
      >
        <div class="font-semibold text-blue-700 dark:text-yellow-300">{{ file.filename }}</div>
        <pre class="mt-2 whitespace-pre-wrap text-xs text-gray-700 dark:text-gray-300 bg-white dark:bg-[#0f1e2f] p-2 rounded overflow-x-auto">
{{ file.content }}
        </pre>
      </li>
    </ul>

    <div v-else-if="!loading" class="text-gray-500 mt-4">Hakuna mafaili bado yaliyotengenezwa.</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const files = ref([])
const loading = ref(true)
const error = ref('')

const fetchFiles = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/smartinject/generated')
    files.value = res.data || []
  } catch (err) {
    error.value = 'Imeshindwa kupakua mafaili kutoka kernel.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchFiles)
</script>
