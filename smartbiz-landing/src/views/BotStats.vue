<template>
  <div class="p-6 max-w-5xl mx-auto bg-white dark:bg-gray-900 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 mt-10">
    <h1 class="text-2xl font-bold text-center text-indigo-700 dark:text-indigo-300 mb-6">
      Taarifa za Bot: {{ botName }}
    </h1>

    <!-- Stats Summary -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8 text-center">
      <BotStatBox label="Majibu" :value="stats.total_responses" color="indigo" />
      <BotStatBox label="Mafanikio" :value="stats.successes" color="green" />
      <BotStatBox label="Makosa" :value="stats.errors" color="red" />
      <BotStatBox label="Leads" :value="stats.leads" color="yellow" />
    </div>

    <!-- Grafu ya Activity -->
    <div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-xl mb-8">
      <h2 class="text-lg font-semibold mb-3 text-gray-700 dark:text-white">Mwelekeo wa Matumizi (Wiki iliyopita)</h2>
      <ResponsiveContainer width="100%" height="250">
        <LineChart :data="weeklyStats">
          <XAxis dataKey="day" stroke="#999" />
          <YAxis allowDecimals="false" />
          <Tooltip />
          <Line type="monotone" dataKey="messages" stroke="#6366F1" stroke-width="3" />
        </LineChart>
      </ResponsiveContainer>
    </div>

    <!-- Integrations -->
    <div class="mb-8">
      <h2 class="text-lg font-semibold text-gray-700 dark:text-white mb-2">Maingiliano</h2>
      <ul class="space-y-2 text-sm text-gray-700 dark:text-gray-300">
        <li v-for="(integration, i) in integrations" :key="i">
          ✅ {{ integration.platform }} - {{ integration.status }}
        </li>
      </ul>
    </div>

    <!-- Button -->
    <div class="text-center">
      <button
        @click="goToIntegrations"
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-lg font-semibold transition"
      >
        Angalia Maingiliano
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from 'recharts'

import BotStatBox from '@/components/BotStatBox.vue' // ✅ IMPORT

const route = useRoute()
const router = useRouter()
const botId = route.params.id || 1
const botName = 'Msaidizi Mary'

const stats = ref({
  total_responses: 1240,
  successes: 1105,
  errors: 135,
  leads: 342
})

const weeklyStats = ref([
  { day: 'Jumamosi', messages: 100 },
  { day: 'Jumapili', messages: 180 },
  { day: 'Jumatatu', messages: 220 },
  { day: 'Jumanne', messages: 170 },
  { day: 'Jumatano', messages: 260 },
  { day: 'Alhamisi', messages: 200 },
  { day: 'Ijumaa', messages: 210 }
])

const integrations = ref([
  { platform: 'WhatsApp', status: 'Connected' },
  { platform: 'Instagram DM', status: 'Pending' },
  { platform: 'Telegram Bot', status: 'Connected' }
])

const goToIntegrations = () => {
  router.push(`/bots/integration/${botId}`)
}
</script>
