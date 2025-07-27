<template>
  <div class="p-6 min-h-screen bg-gray-50 dark:bg-gray-900">
    <h1 class="text-3xl font-bold text-center mb-10 text-indigo-700 dark:text-indigo-300">
      AI Bots Marketplace
    </h1>

    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
      <BotCard
        v-for="pkg in botPackages"
        :key="pkg.id"
        :pkg="pkg"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BotCard from '@/components/BotCard.vue' // ✅ Component ya kifurushi

const botPackages = ref([
  {
    id: 1,
    name: 'BasicBot',
    description: 'Bot ya msingi kwa mahitaji madogo au mtumiaji binafsi.',
    price_monthly: 10000,
    price_yearly: 100000,
    features: [
      'Support 1 social media',
      'Up to 300 messages/month',
      'Basic AI responses',
      'Silent mode support'
    ]
  },
  {
    id: 2,
    name: 'ProBot',
    description: 'Bot ya kati kwa biashara ndogo au wauzaji wanaotaka automation.',
    price_monthly: 25000,
    price_yearly: 250000,
    features: [
      'Support 3 social media',
      'Up to 1000 messages/month',
      'Smart replies + memory',
      'Basic integration tools'
    ]
  },
  {
    id: 3,
    name: 'EliteBot',
    description: 'Bot ya nguvu kwa biashara kubwa au huduma ya kitaalamu.',
    price_monthly: 50000,
    price_yearly: 500000,
    features: [
      'Support unlimited platforms',
      'Unlimited messages',
      'Advanced AI memory',
      'Full integration + analytics'
    ]
  },
  {
    id: 4,
    name: 'CustomBot',
    description: 'Bot ya kipekee inayobinafsishwa kwa masharti maalum.',
    price_monthly: 75000,
    price_yearly: 750000,
    features: [
      'Custom AI training',
      'Team collaboration',
      'Dedicated support',
      'Offline + API usage'
    ]
  }
])
</script>
