<template>
  <div class="space-y-6">
    <SmartCard title="🛠 Admin Dashboard">
      <div class="grid gap-4 md:grid-cols-3">
        <SmartCard title="Users">
          <p class="text-sm text-gray-500">👥 Total Users: {{ totalUsers }}</p>
        </SmartCard>

        <SmartCard title="Logs">
          <p class="text-sm text-gray-500">🧾 Log Entries: {{ logCount }}</p>
        </SmartCard>

        <SmartCard title="Security Alerts">
          <p class="text-sm text-red-500">⚠️ Alerts: {{ securityAlerts }}</p>
        </SmartCard>
      </div>
    </SmartCard>
  </div>
</template>

<script setup>
import SmartCard from '@/components/SmartCard.vue'
import { ref, onMounted } from 'vue'

// Placeholder data
const totalUsers = ref(0)
const logCount = ref(0)
const securityAlerts = ref(0)

onMounted(() => {
  // Fetch from backend later
  totalUsers.value = 120
  logCount.value = 354
  securityAlerts.value = 3
})
</script>

<style scoped>
/* Optional styling */
</style>
