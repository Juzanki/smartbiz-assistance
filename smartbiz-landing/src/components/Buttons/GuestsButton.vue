<!-- GuestsButton.vue -->
<template>
  <button
    class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-md hover:scale-110 transition"
    @click="handleClick"
  >
    <span>🧑‍🤝‍🧑</span>
    <span class="font-semibold">+ Guests</span>
  </button>
</template>

<script setup>
const emit = defineEmits(['open-guests'])

function handleClick() {
  emit('open-guests')
}
</script>

<style scoped>
.icon-btn {
  @apply bg-white/10 text-white backdrop-blur-md border border-white/10;
}
</style>


<!-- GuestsPanel.vue -->
<template>
  <div class="fixed inset-0 z-50 bg-black/60 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-3xl p-6 text-black relative">
      <h2 class="text-lg font-bold mb-4 flex justify-between items-center">
        👥 Manage Guests
        <button @click="$emit('close')" class="text-red-500 hover:text-red-700 text-xl">✖</button>
      </h2>

      <!-- Navigation Tabs -->
      <div class="flex space-x-3 mb-6 text-sm font-semibold">
        <button
          v-for="tabOption in tabs"
          :key="tabOption"
          @click="currentTab = tabOption"
          :class="[
            'px-4 py-2 rounded-full transition duration-200',
            currentTab === tabOption ? 'bg-indigo-600 text-white' : 'bg-gray-300 text-gray-800 hover:bg-gray-400'
          ]">
          {{ tabOption }}
        </button>
      </div>

      <!-- Tab Content -->
      <div class="rounded-lg min-h-[200px]">
        <GuestInvitePopup v-if="currentTab === 'Invite'" />
        <GuestRequestList v-else-if="currentTab === 'Requests'" />
        <GuestLiveSlot v-else-if="currentTab === 'Live Guests'" :guest="demoGuest" :stream="demoStream" />
        <RequestToJoin v-else-if="currentTab === 'Request To Join'" />
        <GuestJoinNotification v-else-if="currentTab === 'Notifications'" :guest="demoGuest" :stream="demoStream" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import GuestInvitePopup from './GuestInvitePopup.vue'
import GuestRequestList from './GuestRequestList.vue'
import GuestLiveSlot from './GuestLiveSlot.vue'
import RequestToJoin from './RequestToJoin.vue'
import GuestJoinNotification from './GuestJoinNotification.vue'

// Tabs
const tabs = ['Invite', 'Requests', 'Live Guests', 'Request To Join', 'Notifications']
const currentTab = ref('Invite')

// Demo Props (replace with real)
const demoGuest = ref({ name: 'Guest A' })
const demoStream = ref({ title: 'Engagement Talk' })
</script>

<style scoped>
button:focus {
  outline: none;
}
</style>
