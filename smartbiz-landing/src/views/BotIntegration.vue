<template>
  <div class="p-6 max-w-3xl mx-auto bg-white dark:bg-gray-900 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 mt-10">
    <h1 class="text-2xl font-bold text-center text-indigo-700 dark:text-indigo-300 mb-6">
      Maingiliano ya Bot: {{ botName }}
    </h1>

    <div class="space-y-8">
      <!-- WhatsApp Integration -->
      <div class="bg-gray-50 dark:bg-gray-800 p-5 rounded-lg border border-gray-200 dark:border-gray-600">
        <h2 class="text-lg font-semibold mb-2 text-green-700 dark:text-green-300">📱 WhatsApp Webhook</h2>
        <IntegrationInput
          label="Webhook URL"
          placeholder="https://api.whatsapp.com/webhook/your-bot-id"
          v-model="integrations.whatsapp"
        />
      </div>

      <!-- Instagram DM Integration -->
      <div class="bg-gray-50 dark:bg-gray-800 p-5 rounded-lg border border-gray-200 dark:border-gray-600">
        <h2 class="text-lg font-semibold mb-2 text-pink-600 dark:text-pink-300">📸 Instagram DM Token</h2>
        <IntegrationInput
          label="Access Token"
          placeholder="EAABsbCS1iHgBAB..."
          v-model="integrations.instagram"
        />
      </div>

      <!-- Telegram Bot Integration -->
      <div class="bg-gray-50 dark:bg-gray-800 p-5 rounded-lg border border-gray-200 dark:border-gray-600">
        <h2 class="text-lg font-semibold mb-2 text-blue-600 dark:text-blue-300">💬 Telegram Bot Token</h2>
        <IntegrationInput
          label="Bot Token"
          placeholder="123456789:AAHdPxxxxxx"
          v-model="integrations.telegram"
        />
      </div>

      <!-- HTML Widget Embed -->
      <div class="bg-gray-50 dark:bg-gray-800 p-5 rounded-lg border border-gray-200 dark:border-gray-600">
        <h2 class="text-lg font-semibold mb-2 text-indigo-600 dark:text-indigo-300">🌐 HTML Widget (Embed Code)</h2>
        <label class="block text-sm text-gray-600 dark:text-gray-300 mb-1">Embed Code:</label>
        <textarea
          readonly
          rows="4"
          class="w-full px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-white border border-gray-300 dark:border-gray-600"
        ><script src="https://smartbiz.ai/bots/embed/{{ botId }}"></script></textarea>
      </div>

      <!-- Save Button -->
      <div class="text-center mt-8">
        <button
          @click="saveIntegrations"
          class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg font-semibold"
        >
          💾 Hifadhi Maingiliano
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useToast } from 'vue-toastification'
import IntegrationInput from '@/components/IntegrationInput.vue'

const route = useRoute()
const toast = useToast()

const botId = route.params.id || 1
const botName = 'Msaidizi Mary'

const integrations = ref({
  whatsapp: '',
  instagram: '',
  telegram: ''
})

const saveIntegrations = () => {
  // Placeholder logic - API call goes here
  toast.success('Maingiliano yamehifadhiwa kikamilifu!')
}
</script>
