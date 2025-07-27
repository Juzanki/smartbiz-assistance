<template>
  <SmartCard title="🔐 Admin Logs">
    <SmartTable :columns="columns" :rows="logs" />
  </SmartCard>
</template>

<script setup>
import SmartCard from '@/components/SmartCard.vue'
import SmartTable from '@/components/SmartTable.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const columns = [
  { label: 'Timestamp', key: 'timestamp' },
  { label: 'User', key: 'user' },
  { label: 'Action', key: 'action' },
  { label: 'IP', key: 'ip' }
]

const logs = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8010/admin/logs')
    logs.value = res.data.logs || []
  } catch (err) {
    console.error('Failed to fetch logs', err)
  }
})
</script>

<style scoped>
</style>
