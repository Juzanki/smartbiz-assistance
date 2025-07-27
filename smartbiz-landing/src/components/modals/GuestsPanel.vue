<template>
  <div class="fixed bottom-0 inset-x-0 z-50 bg-white/90 backdrop-blur-md rounded-t-3xl shadow-2xl p-5 max-h-[85vh] overflow-y-auto animate-slide-up">
    <!-- Title -->
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
        🎥 Guest Management
      </h2>
      <button @click="$emit('close')" class="text-red-500 text-xl hover:text-red-700">✖</button>
    </div>

    <!-- Invite Section -->
    <div class="bg-gray-100 rounded-xl p-4 mb-6 shadow-inner">
      <input
        v-model="inviteInput"
        type="text"
        placeholder="🔍 Invite guest by name or email"
        class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-400"
      />
      <button
        @click="sendInvite"
        class="mt-3 w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition font-semibold"
      >
        Invite to Go Live
      </button>
    </div>

    <!-- Join Requests -->
    <div v-if="joinRequests.length" class="mb-6">
      <h3 class="text-md font-semibold text-gray-700 mb-3">📥 Join Requests</h3>
      <div class="space-y-3">
        <div
          v-for="guest in joinRequests"
          :key="guest.id"
          class="flex items-center justify-between bg-white p-3 rounded-xl shadow-sm hover:shadow-md transition"
        >
          <div class="flex items-center gap-3">
            <img :src="guest.avatar" class="w-10 h-10 rounded-full border shadow" />
            <span class="font-medium text-gray-800">{{ guest.name }}</span>
          </div>
          <div class="flex gap-2">
            <button
              @click="approveGuest(guest.id)"
              class="bg-green-500 hover:bg-green-600 text-white text-xs px-3 py-1 rounded-full font-semibold"
            >
              Accept
            </button>
            <button
              @click="rejectGuest(guest.id)"
              class="bg-red-500 hover:bg-red-600 text-white text-xs px-3 py-1 rounded-full font-semibold"
            >
              Decline
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Current Guests -->
    <div v-if="hosts.length">
      <h3 class="text-md font-semibold text-gray-700 mb-3">🎙️ Live Guests / Co-Hosts</h3>
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
        <div
          v-for="host in hosts"
          :key="host.id"
          class="bg-gradient-to-br from-white via-gray-50 to-gray-100 rounded-xl p-4 text-center shadow hover:shadow-lg transition"
        >
          <img :src="host.avatar" class="w-16 h-16 rounded-full mx-auto mb-2 border border-gray-300" />
          <div class="font-semibold text-sm truncate text-gray-800">{{ host.name }}</div>

          <!-- Controls -->
          <div class="flex justify-center gap-3 mt-3 text-xl">
            <button @click="toggleMic(host)" :class="host.micOn ? 'text-green-500' : 'text-gray-400'">
              <i :class="host.micOn ? 'i-tabler-microphone' : 'i-tabler-microphone-off'" />
            </button>
            <button @click="toggleCam(host)" :class="host.camOn ? 'text-green-500' : 'text-gray-400'">
              <i :class="host.camOn ? 'i-tabler-camera' : 'i-tabler-camera-off'" />
            </button>
            <button
              @click="removeHost(host.id)"
              class="text-red-500 text-sm hover:underline ml-2"
              title="Remove"
            >
              🗑
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const inviteInput = ref('')
const hosts = ref([
  { id: 1, name: 'Host A', avatar: '/avatars/host1.png', micOn: true, camOn: true },
  { id: 2, name: 'Host B', avatar: '/avatars/host2.png', micOn: false, camOn: true }
])
const joinRequests = ref([
  { id: 3, name: 'Stella', avatar: '/avatars/user3.png' },
  { id: 4, name: 'Henry', avatar: '/avatars/user4.png' }
])

const sendInvite = () => {
  if (!inviteInput.value.trim()) return
  hosts.value.push({
    id: Date.now(),
    name: inviteInput.value,
    avatar: '/avatars/default.png',
    micOn: false,
    camOn: false
  })
  inviteInput.value = ''
}

const toggleMic = (host) => host.micOn = !host.micOn
const toggleCam = (host) => host.camOn = !host.camOn
const removeHost = (id) => hosts.value = hosts.value.filter(h => h.id !== id)
const approveGuest = (id) => {
  const guest = joinRequests.value.find(g => g.id === id)
  if (guest) {
    hosts.value.push({ ...guest, micOn: false, camOn: false })
    joinRequests.value = joinRequests.value.filter(g => g.id !== id)
  }
}
const rejectGuest = (id) => joinRequests.value = joinRequests.value.filter(g => g.id !== id)
</script>

<style scoped>
.animate-slide-up {
  animation: slideUp 0.4s ease-out;
}
@keyframes slideUp {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0%);
    opacity: 1;
  }
}
</style>
