<template>
  <div class="p-6 max-w-2xl mx-auto bg-white dark:bg-gray-900 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 mt-10">
    <h1 class="text-2xl font-bold text-indigo-700 dark:text-indigo-300 mb-6 text-center">
      Tengeneza Bot Yako Binafsi
    </h1>

    <form @submit.prevent="submitBot" class="space-y-5">
      <!-- Jina la Bot -->
      <IntegrationInput
        label="Jina la Bot"
        placeholder="Mfano: Msaidizi Mary"
        v-model="botName"
      />

      <!-- Kazi ya Bot -->
      <TextAreaInput
        label="Kazi ya Bot"
        placeholder="Bot hii itasaidia kujibu wateja kwenye WhatsApp kuhusu bidhaa zangu..."
        v-model="botPurpose"
      />

      <!-- Package Iliyowekwa -->
      <div>
        <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-1">Kifurushi Ulichochagua</label>
        <div class="flex items-center gap-3 mt-1">
          <PackageTag :name="selectedPackage?.name || 'Hakuna kifurushi'" />
        </div>
      </div>

      <!-- Button -->
      <button
        type="submit"
        class="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-3 rounded-lg font-semibold transition duration-300"
      >
        Thibitisha na Lipia
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import IntegrationInput from '@/components/IntegrationInput.vue'
import TextAreaInput from '@/components/TextAreaInput.vue'
import PackageTag from '@/components/PackageTag.vue'

const route = useRoute()
const router = useRouter()
const toast = useToast()

const botName = ref('')
const botPurpose = ref('')

const selectedPackage = ref({
  name: route.query.package || null
})

const submitBot = () => {
  if (!botName.value || !botPurpose.value || !selectedPackage.value.name) {
    toast.error('Tafadhali jaza taarifa zote muhimu.')
    return
  }

  toast.success(`Bot "${botName.value}" imeandaliwa kwa kifurushi ${selectedPackage.value.name}.`)
  setTimeout(() => {
    router.push('/bots/my')
  }, 1500)
}
</script>
