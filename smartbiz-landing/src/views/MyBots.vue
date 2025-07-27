<template>
  <div class="p-6 min-h-screen bg-gray-50 dark:bg-gray-900">
    <h1 class="text-2xl font-bold mb-6 text-center text-indigo-700 dark:text-indigo-300">
      Bots Zangu Binafsi
    </h1>

    <div v-if="myBots.length" class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="bot in myBots"
        :key="bot.id"
        class="bg-white dark:bg-gray-800 rounded-2xl shadow-md border border-gray-200 dark:border-gray-700 p-5 flex flex-col justify-between"
      >
        <div class="mb-4">
          <h2 class="text-xl font-semibold text-indigo-600 dark:text-indigo-300">
            {{ bot.name }}
          </h2>

          <!-- ✅ Package badge -->
          <PackageTag :name="bot.package" />

          <p class="text-sm mt-2">
            <span
              :class="[
                'inline-block px-2 py-1 rounded-full text-xs font-medium mt-1',
                bot.status === 'active'
                  ? 'bg-green-100 text-green-700 dark:bg-green-700 dark:text-white'
                  : 'bg-red-100 text-red-700 dark:bg-red-700 dark:text-white'
              ]"
            >
              {{ bot.status.toUpperCase() }}
            </span>
          </p>

          <p class="text-sm text-gray-600 dark:text-gray-400 mt-3">
            🗓 Tarehe ya mwisho wa malipo: <br />
            <span class="font-medium">{{ formatDate(bot.expiry_date) }}</span>
          </p>
        </div>

        <!-- Buttons -->
        <div class="flex gap-2 mt-auto">
          <button
            class="w-full bg-blue-500 hover:bg-blue-600 text-white px-3 py-2 rounded-lg text-sm font-semibold"
            @click="viewBot(bot.id)"
          >
            Angalia
          </button>
          <button
            class="w-full bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-2 rounded-lg text-sm font-semibold"
            @click="editBot(bot.id)"
          >
            Rekebisha
          </button>
          <button
            class="w-full bg-indigo-600 hover:bg-indigo-700 text-white px-3 py-2 rounded-lg text-sm font-semibold"
            @click="renewBot(bot.id)"
          >
            Lipia tena
          </button>
        </div>
      </div>
    </div>

    <div v-else class="text-center mt-20 text-gray-500 dark:text-gray-400">
      <p>Huna bots yoyote bado. Anza kwa kuchagua kifurushi.</p>
      <router-link
        to="/bots/packages"
        class="inline-block mt-4 bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2 rounded-lg font-semibold"
      >
        + Tengeneza Bot
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import PackageTag from '@/components/PackageTag.vue' // ✅ IMPORT

const router = useRouter()

// Dummy bots
const myBots = ref([
  {
    id: 1,
    name: 'Msaidizi Mary',
    package: 'ProBot',
    status: 'active',
    expiry_date: '2025-12-31'
  },
  {
    id: 2,
    name: 'Lead Hunter',
    package: 'BasicBot',
    status: 'inactive',
    expiry_date: '2025-06-30'
  }
])

const viewBot = (id) => {
  router.push(`/bots/stats/${id}`)
}

const editBot = (id) => {
  router.push(`/bots/edit/${id}`)
}

const renewBot = (id) => {
  router.push(`/bots/renew/${id}`)
}

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'short', day: 'numeric' }
  return new Date(dateString).toLocaleDateString('sw-TZ', options)
}
</script>
