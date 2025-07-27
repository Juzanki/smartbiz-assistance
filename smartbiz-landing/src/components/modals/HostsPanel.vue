<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4">
    <div class="bg-white w-full max-w-5xl rounded-3xl shadow-2xl p-6 relative animate-fade-in overflow-y-auto max-h-[95vh]">
      
      <!-- Header -->
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-gray-800 flex items-center gap-2">
          👥 Co-Host Control Panel
        </h2>
        <button
          @click="$emit('close')"
          class="text-red-500 text-2xl hover:text-red-700 focus:outline-none transition"
          aria-label="Close panel"
        >
          ✖
        </button>
      </div>

      <!-- Invite Host Section -->
      <div class="mb-6 flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
        <input
          v-model="inviteEmail"
          type="email"
          placeholder="Enter host email..."
          class="flex-1 rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400 transition"
        />
        <button
          @click="sendInvite"
          class="bg-indigo-600 text-white px-5 py-2 rounded-lg font-semibold hover:bg-indigo-700 transition"
        >
          ➕ Invite
        </button>
      </div>

      <!-- Active Hosts -->
      <div v-if="hosts.length" class="mb-8">
        <h3 class="font-semibold text-lg text-gray-700 mb-3">🔵 Active Co-Hosts</h3>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          <HostCard
            v-for="host in hosts"
            :key="host.id"
            :host="host"
            @swap="swapWithMainHost"
            @remove="removeHost"
            @toggleMic="toggleMic"
            @toggleCam="toggleCam"
          />
        </div>
      </div>

      <!-- Grid Panel Section -->
      <div class="mb-8">
        <h3 class="font-semibold text-lg text-gray-700 mb-3">🎛️ Grid Panel</h3>
        <div class="border border-gray-200 rounded-xl p-3 shadow-sm bg-white">
          <GridPanel />
        </div>
      </div>

      <!-- Smart Camera Section -->
      <div class="mb-10">
        <h3 class="font-semibold text-lg text-gray-700 mb-3">📷 Smart Camera</h3>
        <div class="border border-gray-200 rounded-xl overflow-hidden shadow-sm bg-white">
          <SmartCam />
        </div>
      </div>

      <!-- Suggested Friends -->
      <div>
        <h3 class="font-semibold text-lg text-gray-700 mb-3">✨ Suggested Friends</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          <div
            v-for="friend in suggested"
            :key="friend.id"
            class="flex items-center bg-white rounded-xl border p-3 shadow hover:shadow-md transition"
          >
            <img :src="friend.avatar" class="w-10 h-10 rounded-full mr-3 border" alt="Friend avatar" />
            <div class="flex-1">
              <div class="font-medium text-gray-800">{{ friend.name }}</div>
              <div class="text-xs text-gray-500">🎮 Online</div>
            </div>
            <button
              class="bg-pink-500 hover:bg-pink-600 text-white px-3 py-1 text-sm rounded-lg transition"
            >
              Invite
            </button>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import GridPanel from '@/components/Stream/GridPanel.vue'
import SmartCam from '@/components/Common/SmartCam.vue'
import HostCard from '@/components/Stream/HostCard.vue'

// 💬 State
const inviteEmail = ref('')
const debounceTimer = ref(null)

const hosts = ref([
  { id: 1, name: 'Host A', avatar: '/avatars/host1.png', mic: true, cam: true },
  { id: 2, name: 'Host B', avatar: '/avatars/host2.png', mic: false, cam: true }
])

const suggested = ref([
  { id: 101, name: 'Hope🥰', avatar: '/avatars/friend1.jpg' },
  { id: 102, name: 'Mission-Tridah 🌹', avatar: '/avatars/friend2.jpg' },
  { id: 103, name: 'Son of vission 💄', avatar: '/avatars/friend3.jpg' }
])

// ✉️ Invite Host
const sendInvite = () => {
  const email = inviteEmail.value.trim()
  if (!email || !email.includes('@')) {
    showToast('❌ Please enter a valid email.')
    return
  }

  clearTimeout(debounceTimer.value)
  debounceTimer.value = setTimeout(() => {
    const name = email.split('@')[0].replace(/\W/g, ' ').slice(0, 18)
    hosts.value.push({
      id: Date.now(),
      name: name || 'New Host',
      avatar: '/avatars/default.png',
      mic: true,
      cam: true
    })
    showToast(`✅ Invite sent to ${email}`)
    inviteEmail.value = ''
  }, 300)
}

// 🗑 Remove Host
const removeHost = (id) => {
  const host = hosts.value.find(h => h.id === id)
  if (!host) return
  hosts.value = hosts.value.filter(h => h.id !== id)
  showToast(`🗑 Removed ${host.name}`)
}

// 🔄 Swap with Main Host
const swapWithMainHost = (id) => {
  const index = hosts.value.findIndex(h => h.id === id)
  if (index < 1) return // Skip if already main

  const [host] = hosts.value.splice(index, 1)
  hosts.value.unshift(host)
  showToast(`🔁 ${host.name} is now the main host`)
}

// 🎙 Toggle Mic
const toggleMic = (id) => {
  const host = hosts.value.find(h => h.id === id)
  if (host) host.mic = !host.mic
}

// 📷 Toggle Camera
const toggleCam = (id) => {
  const host = hosts.value.find(h => h.id === id)
  if (host) host.cam = !host.cam
}

// ✅ Toast Notification (can replace with Toast lib later)
const showToast = (msg) => {
  const toast = document.createElement('div')
  toast.innerText = msg
  toast.className = 'fixed top-6 left-1/2 -translate-x-1/2 bg-black/90 text-white px-4 py-2 rounded-xl shadow-lg z-[9999] transition-opacity'
  document.body.appendChild(toast)

  setTimeout(() => {
    toast.style.opacity = '0'
    setTimeout(() => toast.remove(), 400)
  }, 2800)
}
</script>
<style scoped>
/* ✨ Entry Animation */
.animate-fade-in {
  animation: fadeInPanel 0.45s ease-out both;
  will-change: opacity, transform, filter;
}
@keyframes fadeInPanel {
  0% {
    opacity: 0;
    transform: translateY(40px) scale(0.95);
    filter: blur(2px);
  }
  80% {
    filter: blur(0.2px);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}

/* 💡 Panel Glow Effect */
.panel-glow {
  box-shadow:
    0 8px 24px rgba(0, 0, 0, 0.15),
    0 0 0 2px rgba(99, 102, 241, 0.2);
  border-radius: 1.5rem;
  transition: box-shadow 0.3s ease-in-out;
}
.panel-glow:hover {
  box-shadow:
    0 10px 32px rgba(0, 0, 0, 0.2),
    0 0 0 3px rgba(99, 102, 241, 0.3);
}

/* 🟣 Invite Button Tap Feedback */
.button-press {
  transition: transform 0.15s ease, box-shadow 0.2s ease;
}
.button-press:active {
  transform: scale(0.96);
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.3);
}

/* 🧍 Suggested Friend Card Hover */
.friend-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  transform-origin: center;
}
.friend-card:hover {
  transform: translateY(-4px) scale(1.025);
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.12);
}

/* 🎙 Mic & 📷 Cam Toggle Buttons */
.toggle-icon {
  transition: transform 0.2s ease, color 0.2s ease;
  cursor: pointer;
}
.toggle-icon:hover {
  transform: scale(1.15);
  color: #6366f1;
}

/* 📱 Responsive Adjustments */
@media (max-width: 640px) {
  .animate-fade-in {
    padding: 1rem;
  }

  .friend-card {
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
    padding: 1rem;
  }

  .panel-glow {
    border-radius: 1rem;
  }
}
</style>
