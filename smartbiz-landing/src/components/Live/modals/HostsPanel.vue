<template>
  <div class="fixed inset-0 z-50 bg-black/60 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-3xl p-6 text-black relative">
      <h2 class="text-lg font-bold mb-4 flex justify-between items-center">
        👤 Manage Hosts
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
      <div v-if="currentTab === 'Invite'" class="mb-6 flex gap-2">
        <input v-model="inviteEmail" type="email" placeholder="Enter host email..." class="flex-1 px-3 py-2 rounded border border-gray-300" />
        <button @click="sendInvite" class="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700">Invite</button>
      </div>

      <div v-if="currentTab === 'Host List'" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        <div v-for="host in hosts" :key="host.id" class="bg-gray-100 rounded-lg p-4 text-center shadow relative">
          <img :src="host.avatar" class="w-16 h-16 mx-auto rounded-full mb-2 border border-white" />
          <div class="font-semibold">{{ host.name }}</div>

          <!-- Toggle mic/cam -->
          <div class="flex justify-center mt-2 gap-2 text-gray-600 text-lg">
            <button @click="host.mic = !host.mic" :class="host.mic ? 'text-green-500' : 'text-red-400'" title="Mic">
              <i :class="host.mic ? 'i-tabler-microphone' : 'i-tabler-microphone-off'" />
            </button>
            <button @click="host.cam = !host.cam" :class="host.cam ? 'text-green-500' : 'text-red-400'" title="Camera">
              <i :class="host.cam ? 'i-tabler-camera' : 'i-tabler-camera-off'" />
            </button>
          </div>

          <!-- Controls -->
          <div class="mt-3 space-x-2">
            <button @click="swapWithMainHost(host.id)" class="text-xs text-blue-600 hover:underline">🔁 Swap</button>
            <button @click="removeHost(host.id)" class="text-xs text-red-500 hover:underline">🗑 Remove</button>
          </div>
        </div>
      </div>

      <!-- Placeholder for future tabs -->
      <div v-if="currentTab === 'Pending'">
        <p class="text-gray-500 text-center">📄 No pending invites.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Tabs
const tabs = ['Invite', 'Host List', 'Pending']
const currentTab = ref('Invite')

const inviteEmail = ref('')
const hosts = ref([
  { id: 1, name: 'Host A', avatar: '/avatars/host1.png', mic: true, cam: true },
  { id: 2, name: 'Host B', avatar: '/avatars/host2.png', mic: false, cam: true }
])

const sendInvite = async () => {
  if (!inviteEmail.value.trim()) return

  const email = inviteEmail.value.trim()
  const name = email.split('@')[0]

  try {
    const res = await fetch('/api/invite-host', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email })
    })

    if (!res.ok) throw new Error('Failed to invite')

    hosts.value.push({
      id: Date.now(),
      name,
      avatar: '/avatars/default.png',
      mic: true,
      cam: true
    })
    inviteEmail.value = ''
  } catch (err) {
    alert(`❌ Failed to invite host: ${err.message}`)
  }
}

const swapWithMainHost = (id) => {
  const index = hosts.value.findIndex(h => h.id === id)
  if (index > -1) {
    const [host] = hosts.value.splice(index, 1)
    hosts.value.unshift(host)
    alert(`🔁 ${host.name} is now the main host`)
  }
}

const removeHost = (id) => {
  hosts.value = hosts.value.filter(h => h.id !== id)
}
</script>
