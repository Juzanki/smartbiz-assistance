<template>
  <div class="fixed inset-0 z-50 bg-black/60 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-3xl p-6 text-black relative">
      <h2 class="text-lg font-bold mb-4 flex justify-between items-center">
        👥 Manage Guests
        <button @click="$emit('close')" class="text-red-500 hover:text-red-700 text-xl">✖</button>
      </h2>

      <!-- Navigation Tabs -->
      <div class="flex space-x-3 mb-6 text-sm font-semibold text-white">
        <button v-for="tabOption in tabs" :key="tabOption"
          @click="currentTab = tabOption"
          :class="['px-4 py-2 rounded-full', currentTab === tabOption ? 'bg-indigo-600' : 'bg-gray-400']">
          {{ tabOption }}
        </button>
      </div>

      <!-- Tab Content -->
      <div class="rounded-lg">
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
