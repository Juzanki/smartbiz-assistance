<template>
  <SmartCard title="📡 Live Prompt Tracker">
    <div class="space-y-4">
      <SmartAlert v-if="error" :message="error" type="error" />

      <div v-if="logs.length === 0" class="text-sm text-gray-400 italic">No activity recorded yet.</div>

      <SmartTable v-else :headers="headers" :rows="logs" />
    </div>
  </SmartCard>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import SmartCard from '@/components/SmartCard.vue'
import SmartAlert from '@/components/SmartAlert.vue'
import SmartTable from '@/components/SmartTable.vue'

const logs = ref([])
const error = ref('')

const headers = ['Timestamp', 'User', 'Prompt', 'Model', 'Tokens']

const fetchLogs = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8010/ai/logs')
    logs.value = res.data.logs.map(log => [
      log.timestamp,
      log.user,
      log.prompt.slice(0, 60) + (log.prompt.length > 60 ? '...' : ''),
      log.model,
      log.tokens
    ])
  } catch (err) {
    error.value = 'Failed to load prompt logs.'
  }
}

onMounted(fetchLogs)
</script>

<style scoped>
</style>
