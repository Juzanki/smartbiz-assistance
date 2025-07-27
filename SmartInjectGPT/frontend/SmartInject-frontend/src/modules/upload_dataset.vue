<template>
  <div class="p-6">
    <h2 class="text-2xl font-bold mb-4">Train Your AI Model</h2>

    <form @submit.prevent="submitDataset" class="space-y-4">
      <div>
        <label class="block font-medium">Model Name</label>
        <input v-model="modelName" class="w-full border p-2 rounded" required />
      </div>

      <div>
        <label class="block font-medium">Upload Dataset (JSON)</label>
        <input type="file" @change="handleFile" accept=".json" class="w-full border p-2 rounded" required />
      </div>

      <button type="submit" class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
        Train Model
      </button>
    </form>

    <p v-if="message" class="mt-4 text-blue-700 font-semibold">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from '@/utils/axios'

const modelName = ref('')
const fileData = ref(null)
const message = ref('')

const handleFile = (event) => {
  const file = event.target.files[0]
  const reader = new FileReader()
  reader.onload = (e) => {
    fileData.value = JSON.parse(e.target.result)
  }
  reader.readAsText(file)
}

const submitDataset = async () => {
  if (!fileData.value) return alert("Please upload a dataset file")

  const payload = {
    model_name: modelName.value,
    dataset: fileData.value
  }

  const res = await axios.post('/ai/train', payload)
  message.value = `Model "${res.data.model_name}" trained with ${res.data.num_samples} samples.`
}
</script>
