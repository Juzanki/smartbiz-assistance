<template>
  <div class="p-6">
    <h2 class="text-2xl font-bold mb-4">Developer Dashboard</h2>

    <!-- API Key Section -->
    <div class="mb-6 p-4 bg-white shadow rounded">
      <h3 class="font-semibold text-lg">Your API Key</h3>
      <div class="mt-2 text-gray-700">
        <div v-if="apiKey">
          <code class="bg-gray-100 p-2 rounded">{{ apiKey.key }}</code>
          <p class="text-sm text-green-700 mt-1">Usage: {{ apiKey.usage_count }} requests</p>
        </div>
        <button v-else @click="createApiKey" class="mt-2 bg-blue-600 text-white px-4 py-2 rounded">
          Generate API Key
        </button>
      </div>
    </div>

    <!-- Trained Models Section -->
    <div class="p-4 bg-white shadow rounded">
      <h3 class="font-semibold text-lg mb-2">Your AI Models</h3>
      <ul v-if="models.length" class="list-disc pl-5 text-gray-800">
        <li v-for="m in models" :key="m.model_name">
          <strong>{{ m.model_name }}</strong> — {{ m.num_samples }} samples — {{ m.trained_at.split("T")[0] }}
        </li>
      </ul>
      <p v-else class="text-gray-500">You haven't trained any models yet.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/utils/axios'

const apiKey = ref(null)
const models = ref([])

const fetchApiKey = async () => {
  const res = await axios.get('/developer/api-key')
  apiKey.value = res.data
}

const fetchModels = async () => {
  const res = await axios.get('/developer/models')
  models.value = res.data
}

const createApiKey = async () => {
  const res = await axios.post('/developer/api-key')
  apiKey.value = res.data
}

onMounted(() => {
  fetchApiKey()
  fetchModels()
})
</script>
