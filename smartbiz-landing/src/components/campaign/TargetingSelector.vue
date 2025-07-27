<template>
  <div class="space-y-4">
    <!-- Region Filter -->
    <div>
      <label class="block text-sm font-medium">Select Regions</label>
      <select v-model="form.regions" multiple class="w-full border rounded p-2">
        <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
      </select>
    </div>

    <!-- Tag Filter -->
    <div>
      <label class="block text-sm font-medium">Customer Tags</label>
      <select v-model="form.tags" multiple class="w-full border rounded p-2">
        <option v-for="tag in tags" :key="tag" :value="tag">{{ tag }}</option>
      </select>
    </div>

    <!-- Last Purchase Date -->
    <div>
      <label class="block text-sm font-medium">Last Purchase After</label>
      <input type="date" v-model="form.last_purchase_after" class="w-full border rounded p-2" />
    </div>

    <!-- Replied Filter -->
    <div>
      <label class="block text-sm font-medium">Has Replied</label>
      <select v-model="form.has_replied" class="w-full border rounded p-2">
        <option :value="null">Any</option>
        <option :value="true">Yes</option>
        <option :value="false">No</option>
      </select>
    </div>

    <button @click="preview" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
      Preview Audience
    </button>

    <!-- Preview Results -->
    <div v-if="results.length" class="mt-4">
      <h3 class="text-lg font-semibold mb-2">🎯 {{ results.length }} Targeted Customers</h3>
      <ul class="divide-y bg-white rounded shadow">
        <li v-for="c in results" :key="c.id" class="p-2">
          {{ c.full_name }} - {{ c.phone_number }} <span class="text-sm text-gray-500">({{ c.region }})</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/utils/axios'

const form = ref({
  regions: [],
  tags: [],
  last_purchase_after: null,
  has_replied: null
})

const regions = ref(["Dar es Salaam", "Arusha", "Mwanza", "Dodoma"]) // could be dynamic
const tags = ref([])
const results = ref([])

onMounted(async () => {
  const res = await axios.get('/tags') // if you have this route
  tags.value = res.data.map(t => t.name)
})

const preview = async () => {
  const res = await axios.post('/campaign/target-preview', form.value)
  results.value = res.data
}
</script>
